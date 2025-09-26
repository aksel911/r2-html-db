import pyodbc
import os
import shutil
from pathlib import Path
import logging
from typing import List, Tuple, Optional

# Настройка логирования с поддержкой UTF-8
import sys

# Настраиваем консольный вывод для UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('image_processor.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SQLImageProcessor:
    def __init__(self, server: str, database: str, username: str = None, password: str = None):
        """
        Инициализация подключения к SQL Server
        
        Args:
            server: Имя сервера SQL Server
            database: Имя базы данных
            username: Имя пользователя (опционально для Windows Authentication)
            password: Пароль (опционально для Windows Authentication)
        """
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = None
        
        # Пути к папкам
        self.source_folder = Path("D:/FOR_R2_ONLINE/R2OnlineFiles/GITHUB/R2-HTML-DB/static")
        self.destination_folder = Path("D:/FOR_R2_ONLINE/R2OnlineFiles/GITHUB/R2-HTML-DB/static/all_items")
        
        # Создаем папку назначения если не существует
        self.destination_folder.mkdir(parents=True, exist_ok=True)
    
    def connect(self) -> bool:
        """Установка соединения с базой данных"""
        try:
            if self.username and self.password:
                # SQL Server Authentication
                connection_string = (
                    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                    f'SERVER={self.server};'
                    f'DATABASE={self.database};'
                    f'UID={self.username};'
                    f'PWD={self.password}'
                )
            else:
                # Windows Authentication
                connection_string = (
                    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                    f'SERVER={self.server};'
                    f'DATABASE={self.database};'
                    f'Trusted_Connection=yes;'
                )
            
            self.connection = pyodbc.connect(connection_string)
            logger.info(f"Successfully connected to database {self.database}")
            return True
            
        except Exception as e:
            logger.error(f"Database connection error: {e}")
            return False
    
    def get_all_iids(self) -> List[int]:
        """Получение всех IID из таблицы DT_Item"""
        try:
            cursor = self.connection.cursor()
            query = "SELECT IID FROM [FNLParm].[dbo].[DT_Item]"
            cursor.execute(query)
            
            iids = [row[0] for row in cursor.fetchall()]
            logger.info(f"Found {len(iids)} IID in DT_Item table")
            return iids
            
        except Exception as e:
            logger.error(f"Error getting IID: {e}")
            return []
    
    def get_item_resource_info(self, iid: int) -> Optional[Tuple[str, int, int]]:
        """
        Получение информации о ресурсе для конкретного IID
        
        Args:
            iid: ID элемента
            
        Returns:
            Tuple с (RFileName, RPosX, RPosY) или None если не найдено
        """
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT RFileName, RPosX, RPosY 
            FROM [FNLParm].[dbo].[DT_ItemResource] 
            WHERE ROwnerID = ? AND RType = 2
            """
            cursor.execute(query, (iid,))
            result = cursor.fetchone()
            
            if result:
                return (result[0], result[1], result[2])
            else:
                logger.warning(f"Resource for IID {iid} not found")
                return None
                
        except Exception as e:
            logger.error(f"Error getting resource for IID {iid}: {e}")
            return None
    
    def find_and_copy_image(self, iid: int, resource_info: Tuple[str, int, int]) -> bool:
        """
        Поиск и копирование изображения
        
        Args:
            iid: ID элемента
            resource_info: Tuple с (RFileName, RPosX, RPosY)
            
        Returns:
            True если файл успешно скопирован, False в противном случае
        """
        rfilename, rposx, rposy = resource_info
        
        # Удаляем расширение .dds и формируем имя PNG файла
        base_name = rfilename.replace('.dds', '')
        source_filename = f"{base_name}_{rposx}_{rposy}.png"
        source_path = self.source_folder / source_filename
        
        # Проверяем существование исходного файла
        if not source_path.exists():
            logger.warning(f"File {source_filename} not found in {self.source_folder}")
            return False
        
        # Формируем путь для целевого файла
        destination_filename = f"{iid}.png"
        destination_path = self.destination_folder / destination_filename
        
        try:
            # Копируем файл
            shutil.copy2(source_path, destination_path)
            logger.info(f"File copied: {source_filename} -> {destination_filename}")
            return True
            
        except Exception as e:
            logger.error(f"Error copying file {source_filename}: {e}")
            return False
    
    def process_all_items(self) -> dict:
        """
        Обработка всех элементов из DT_Item
        
        Returns:
            Словарь со статистикой обработки
        """
        stats = {
            'total_items': 0,
            'successful_copies': 0,
            'resource_not_found': 0,
            'image_not_found': 0,
            'copy_errors': 0
        }
        
        # Получаем все IID
        iids = self.get_all_iids()
        if not iids:
            logger.error("Failed to get IID from database")
            return stats
        
        stats['total_items'] = len(iids)
        logger.info(f"Starting processing {len(iids)} items")
        
        for i, iid in enumerate(iids, 1):
            if i % 100 == 0 or i == 1:  # Логируем каждый 100-й элемент
                logger.info(f"Processing IID {iid} ({i}/{len(iids)})")
            
            # Получаем информацию о ресурсе
            resource_info = self.get_item_resource_info(iid)
            if resource_info is None:
                stats['resource_not_found'] += 1
                continue
            
            # Копируем изображение
            if self.find_and_copy_image(iid, resource_info):
                stats['successful_copies'] += 1
            else:
                stats['image_not_found'] += 1
        
        return stats
    
    def close_connection(self):
        """Закрытие соединения с базой данных"""
        if self.connection:
            self.connection.close()
            logger.info("Database connection closed")
    
    def __enter__(self):
        """Контекстный менеджер - вход"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Контекстный менеджер - выход"""
        self.close_connection()

def main():
    """Основная функция"""
    # Конфигурация подключения к базе данных
    SERVER = "localhost"  # Замените на имя вашего сервера
    DATABASE = "FNLParm"
    # USERNAME = None  # Для Windows Authentication оставьте None
    # PASSWORD = None  # Для Windows Authentication оставьте None
    
    # Для SQL Server Authentication раскомментируйте и заполните:
    USERNAME = "sa"
    PASSWORD = "pass"
    
    try:
        with SQLImageProcessor(SERVER, DATABASE, USERNAME, PASSWORD) as processor:
            if processor.connect():
                logger.info("Starting image processing...")
                
                stats = processor.process_all_items()
                
                # Выводим статистику
                logger.info("=== PROCESSING STATISTICS ===")
                logger.info(f"Total items: {stats['total_items']}")
                logger.info(f"Successfully copied: {stats['successful_copies']}")
                logger.info(f"Resource not found: {stats['resource_not_found']}")
                logger.info(f"Image not found: {stats['image_not_found']}")
                logger.info(f"Copy errors: {stats['copy_errors']}")
                
                success_rate = (stats['successful_copies'] / stats['total_items']) * 100 if stats['total_items'] > 0 else 0
                logger.info(f"Success rate: {success_rate:.2f}%")
                
            else:
                logger.error("Failed to connect to database")
                
    except KeyboardInterrupt:
        logger.info("Processing interrupted by user")
    except Exception as e:
        logger.error(f"Critical error: {e}")

if __name__ == "__main__":
    main()