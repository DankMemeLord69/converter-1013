import prompt


def input_unit(units):
    while True:
        firstunit = prompt.string("Выберите единицу : ")
        if firstunit in units:
            break
    return firstunit


def get_factor(unit_for_chek, units_table):
    for unit in units_table:
        if unit_for_chek == unit['единица измерения']:
            return unit['множитель']


def convert():
    units_table = [{'единица измерения': 'RUB', 'множитель': 1},
                   {'единица измерения': 'USD', 'множитель': 60.2179},
                   {'единица измерения': 'EUR', 'множитель': 61.5416},
                   {'единица измерения': 'CNY', 'множитель': 84.4637},
                   ]
    units = [unit['единица измерения'] for unit in units_table]
    user_num = prompt.real("Введите число: ")
    for unit in units_table:
        print(unit['единица измерения'])

    firstunit = input_unit(units)
    secondunit = input_unit(units)

    firstfactor = get_factor(firstunit, units_table)
    secondfactor = get_factor(secondunit, units_table)

    result = float(user_num) * firstfactor / secondfactor
    print(result)