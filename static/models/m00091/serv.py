import http.server
import socketserver
import os
import socket

def start_server():
    # Путь к файлу, который вы хотите раздать
    file_path = r"C:\Users\sours\OneDrive\Рабочий стол\GIT\R2-HTML-DB\static\models\m00091\test.html"

    # Директория, где находится файл
    directory = os.path.dirname(file_path)

    # Имя файла
    file_name = os.path.basename(file_path)

    # Переключаемся в директорию с файлом
    os.chdir(directory)

    # Класс для обработки запросов
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/' or self.path == f'/{file_name}':
                self.path = file_name
            return super().do_GET()

    # Порт для сервера
    port = 8000

    # Получаем IP-адрес хоста
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    with socketserver.TCPServer(("0.0.0.0", port), CustomHandler) as httpd:
        print(f"Сервер запущен на порту {port}. Доступен по адресу: http://{local_ip}:{port}")
        print("Для завершения нажмите Ctrl+C")
        httpd.serve_forever()

if __name__ == "__main__":
    start_server()
