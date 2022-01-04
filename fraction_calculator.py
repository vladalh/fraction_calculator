import math


def calculating_fractions(x1, x2, y1, y2, sign):
    """
    x1, x2 - numerator and denominator of the first fraction
    y1, y2 - numerator and denominator of the second fraction
    sign - mathematical action
    """
    devisor = math.gcd(x2, y2)
    whole = "whole"
    if sign == '+':
        if y1 == y2:
            num = x1 + x2
            denom = y1
        else:
            num = (x1 * y2) + (x2 * y1)
            denom = y1 * y2
        result = f"{int(num // devisor)} / {int(denom // devisor)}"

    elif sign == '-':
        if y1 == y2:
            num = x1 - x2
            denom = y1
        else:
            num = (x1 * y2) - (x2 * y1)
            denom = y1 * y2
        result = f"{int(num // devisor)} / {int(denom // devisor)}"

    elif sign == '*':
        num = x1 * x2
        denom = y1 * y2
        result = f"{int(num // devisor)} / {int(denom // devisor)}"

    elif sign == '/':
        num = x1 * y2
        denom = y1 * x2
        result = f"{int(num // devisor)} / {int(denom // devisor)}"

    if num < denom:
        return result
    else:
        return f"{int(num // denom)} {whole} {int((num % denom) // devisor)}/{int((denom) // devisor)}"


# vladalh@mail.ru
