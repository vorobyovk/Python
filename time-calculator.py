
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError as e:
            return str(e)
        except IndexError:
            return "Invalid command format."
        except TypeError:
            return "Invalid input type."
    return inner

@input_error
def parse_input(user_input):
    if not user_input.strip():
        return None, []
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args
    except ValueError:
        return None, []


def add_time(time1, time2):
  hours1, minutes1 = map(int, time1.split("."))
  hours2, minutes2 = map(int, time2.split("."))
  total_minutes = (hours1 * 60 + minutes1) + (hours2 * 60 + minutes2)
  total_hours = total_minutes // 60
  remaining_minutes = total_minutes % 60
  return f"{total_hours}.{remaining_minutes:02d}"



def main():
  # Пример использования функции
  # Вводим два времени в формате "часы.минуты"
  # Например: "10.30" и "2.15"
  # Выводим сумму этих времен
  # Пример: Сумма 10.30 и 2.15 равна 12.45
    # time1 = input("Введите первое время (часы.минуты): ")
    i = 0
    result = None
    while True:
        try:
            user_input = input("Please input command: ").strip()     
            if not user_input:
                print("Please enter a command.")
                continue
            command, args = parse_input(user_input)
            if command is None:
                print("Invalid input format.")
                continue
            if command == "close":
                print("Goodbye!\n")
                print(f"Сумма равна {result}")
                break
            elif command == "add":
                i+= 1
                if i > 1:
                    time1 = result
                    time2 = args[0]
                    result = add_time(time1, time2)
                    continue
                else:
                    time1 = args[0]
                    time2 = args[1]
                    result = add_time(time1, time2)                
                print(f"Сумма равна {result}")            
        except: 
            print("Ошибка: Введите время в формате 'часы.минуты' (например, 10.30).")

if __name__ == "__main__":
    main()
