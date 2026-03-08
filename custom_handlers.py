def custom_round(number):
    number = round(number, 1)
    integer_part = int(number)
    decimal_part = number - integer_part
    if decimal_part >= 0.5:
        return integer_part + 1
    else:
        return integer_part

