from fraction_calculator import calculating_fractions


def main():
    numerator1 = int(input("Enter the numerator1 :"))
    denominator1 = int(input("Enter the denominator :"))
    operator = input("Enter operator +, -, *, / :")
    numerator2 = int(input("Enter the numerator2 :"))
    denominator2 = int(input("Enter the denominator :"))

    print(calculating_fractions(numerator1, numerator2, denominator1, denominator2, operator))


if __name__ == "__main__":
    main()
