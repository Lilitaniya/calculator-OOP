def calc(action, kind):
    data = action.split()
    sign = data[1]

    if kind == "Число":
        if sign == "+":
            answer = float(data[0]) + float(data[2])
        elif sign == "-":
            answer = float(data[0]) - float(data[2])
        elif sign == "*":
            answer = float(data[0]) * float(data[2])
        elif sign == "/":
            if data[2] == "0":
                answer = "Деление на ноль невозможно"
            else:
                answer = float(data[0]) / float(data[2])
        else:
            answer = "Неизвестная операция"

    else:
        first_num = complex(data[0])
        second_num = complex(data[2])
        if sign == "+":
            answer = first_num + second_num
        elif sign == "-":
            answer = first_num - second_num
        elif sign == "*":
            answer = first_num * second_num
        elif sign == "/":
            answer = first_num / second_num
        else:
            answer = "Неизвестная операция"

    # Округляем результат до 2 знаков после запятой
    if isinstance(answer, float):
        answer = round(answer, 2)
    elif isinstance(answer, complex):
        answer = complex(round(answer.real, 2), round(answer.imag, 2))

    # Убираем "+0j" из вывода, если мнимая часть равна нулю
    if isinstance(answer, complex) and answer.imag == 0:
        answer = answer.real

    return answer

