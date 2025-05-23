from datetime import datetime, timezone
import sqlite3
import psutil


def print_info(timestamp, cpu_usage, free_ram, disk_usage):
    print(datetime.fromisoformat(timestamp).strftime("%Y-%m-%d %H:%M:%S"))
    print(f" - ЦП: {cpu_usage}%")
    print(f" - Доступно ОЗУ: {free_ram / 1e+9:0.2f} ГБ")
    print(f" - Использовано диска: {disk_usage}")


connection = sqlite3.connect("sys_mon.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS snapshots (
	datetime TEXT PRIMARY KEY,
	cpu_usage REAL,
	free_ram INTEGER,
	disk_usage REAL
)
""")

print("Выберите что хотите сделать:")
print("1. Запустить мониторинг")
print("2. Посмотреть сохранённые данные")
action = int(input("> "))
match action:
    case 1:
        while True:
            cpu_usage = psutil.cpu_percent(2.5)
            free_ram = psutil.virtual_memory().available
            disk_usage = psutil.disk_usage('/').percent
            timestamp = datetime.now().isoformat()
            cursor.execute("INSERT INTO snapshots VALUES (?, ?, ?, ?)",
                           (timestamp, cpu_usage, free_ram, disk_usage))
            print_info(timestamp, cpu_usage, free_ram, disk_usage)
            connection.commit()
    case 2:
        date = datetime.strptime(input("Введите дату (YYYY-MM-DD): "), "%Y-%m-%d").strftime("%Y-%m-%d")
        cursor.execute("SELECT * FROM snapshots WHERE DATE(datetime) = ?", (date,))
        for values in cursor.fetchall():
            print_info(values[0], values[1], values[2], values[3])