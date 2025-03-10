from datetime import datetime
from datetime import timedelta
from datetime import datetime, timezone, timedelta
import time

# now = datetime.now()

# current_datetime = datetime.now()
# print(f"Year: {current_datetime.year}")
# print(f"Month: {current_datetime.month}")
# print(f"Day: {current_datetime.day}")
# print(f"Hour: {current_datetime.hour}")
# print(f"Minute: {current_datetime.minute}")
# print(f"Second: {current_datetime.second}")
# print(f"Microsecond: {current_datetime.microsecond}")
# print(f": {current_datetime.tzinfo}")
# print(f"Date: {current_datetime.date()}")
# print(f"Time: {current_datetime.time()}")

# specific_date = datetime(year=2020, month=1, day=7)
# specific_time = datetime(year=2020, month=1, day=7, hour=12, minute=30, second=45)
# print(specific_time)
# print(specific_date)

# day_of_week = now.weekday()
# print(f"Day of week: {day_of_week}")  

# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)

# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# difference = seventh_day_2020 - seventh_day_2019
# print(difference)  
# print(difference.total_seconds())  

# now = datetime.now()
# future_date = now + timedelta(days=-1110)  
# print(future_date)

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# four_weeks_interval = timedelta(weeks=4)
# print(seventh_day_2020 + four_weeks_interval) 
# print(seventh_day_2020 - four_weeks_interval)

# # Створення об'єкта datetime
# date = datetime(year=2023, month=12, day=18)
# # Отримання порядкового номера
# ordinal_number = date.toordinal()
# print(f"Порядковий номер дати {date} становить {ordinal_number}")

# # Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
# napoleon_burns_moscow = datetime(year=1812, month=9, day=14)
# # Поточна дата
# current_date = datetime.now()
# # Розрахунок кількості днів
# days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
# print(days_since)

# now = datetime.now()
# # Форматування дати і часу
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_date) 
# # Форматування лише дати
# formatted_date_only = now.strftime("%A, %d %B %Y")
# print(formatted_date_only)
# # Форматування лише часу
# formatted_time_only = now.strftime("%I:%M %p")
# print(formatted_time_only)  
# # Форматування лише дати
# formatted_date_only = now.strftime("%d.%m.%Y")
# print(formatted_date_only)

# my_string = "2020-01-07 14:30:45"
# datetime_object = datetime.strptime(my_string, "%Y-%m-%d %H:%M:%S")
# print(datetime_object)

# now = datetime.now()
# day_of_week = now.isoweekday()
# print(f"Сьогодні: {day_of_week}") 

# # Час у конкретній часовій зоні
# timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
# timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)
# # Конвертація у формат ISO 8601
# iso_format_with_timezone = timezone_datetime.isoformat()
# print(iso_format_with_timezone)

# time = datetime.now()
start = time.perf_counter()
time.sleep(3)
end = time.perf_counter()
print(end-start)