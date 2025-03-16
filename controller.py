import view
import operations
import log

def button_click():
    value_lst, kind_oper = view.get_value()
    log.logwrite("Пользователь ввел: ", value_lst)
    result = operations.calc(value_lst, kind_oper)
    log.logwrite("Результат подсчета: ", result)
    view.output(result)
