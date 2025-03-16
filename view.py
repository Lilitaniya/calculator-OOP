
def get_value():
    print("Это калькулятор")
    kind_operation = input("Для целых числе нажмите 1, для дробных выыберите 2. Дробные числа вводятся через точку: ")
    
    while True:
        inp = input("Введите необходимую формулу, разделяя пробелами знаки: ")
        try_act = inp
        data = try_act.split()

        if len(data) == 3:
            if data[1] == "+" or data[1] == "-" or data[1] == "*" or data[1] == "/":
                print("Спасибо!")
                break

        print("Что-то пошло не так, попробуйте снова.")

    return inp, kind_operation


def output(result):
    try:
        if result.is_integer():
            print(f"Ваш результат", int(result))
        elif isinstance(result, float):
            print(f"Ваш результат:", result)
        else: print(result)
    except:
        print(result)
