import pyodbc

def process_script_text(script_text):
    """Обрабатывает текст скрипта и извлекает информацию."""
    lines = script_text.split('\n')
    item_ids = []
    probabilities = []

    current_item_id = None
    for line in lines:
        if "pushitem2(" in line:
            # Извлекаем ItemID из строки
            start_index = line.index("pushitem2(") + 10
            end_index = line.index(",", start_index)
            current_item_id = line[start_index:end_index].strip()
        elif "rand <=" in line:
            # Извлекаем вероятность из строки
            start_index = line.index("<=") + 2
            probability = line[start_index:].strip()
            item_ids.append(current_item_id)
            probabilities.append(int(probability))

    return list(zip(item_ids, probabilities))

def fetch_script_from_db(npc_id):
    """Получает текст скрипта из базы данных."""
    connection_string = "Driver={SQL Server};Server=localhost;Database=FNLParm;UID=sa;PWD=pass;"
    query = f"SELECT mScriptText FROM TblDialogScript WHERE mMId = {npc_id}"
    
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0] if result else None

def fetch_item_names_from_db(item_ids):
    """Получает названия предметов из базы данных."""
    connection_string = "Driver={SQL Server};Server=localhost;Database=FNLParm;UID=sa;PWD=pass;"
    query = f"SELECT IID, IName FROM DT_Item WHERE IID IN ({','.join(map(str, item_ids))})"
    
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return {row.IID: row.IName for row in cursor.fetchall()}

def main():
    npc_id = 929  # ID NPC (например, Золотой: 929, Изумрудный: 2578)
    script_text = fetch_script_from_db(npc_id)
    
    if not script_text:
        print("Скрипт не найден в базе данных.")
        return
    
    item_data = process_script_text(script_text)
    item_ids = [item[0] for item in item_data]
    item_names = fetch_item_names_from_db(item_ids)
    
    print("Результат обработки:")
    for item_id, probability in item_data:
        item_name = item_names.get(int(item_id), "Неизвестный предмет")
        print(f"ID: {item_id}, Название: {item_name}, Шанс: {probability}%")

if __name__ == "__main__":
    main()
