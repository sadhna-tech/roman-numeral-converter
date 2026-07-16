roman_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman_to_int(roman):
    total = 0
    prev = 0

    for char in reversed(roman.upper()):
        value = roman_map.get(char)

        if value is None:
            return None

        if value < prev:
            total -= value
        else:
            total += value
            prev = value

    return total


def int_to_roman(num):
    if num < 1 or num > 3999:
        return None

    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = ""

    for value, symbol in values:
        while num >= value:
            result += symbol
            num -= value

    return result


print("Roman Numeral Converter")
print("1. Roman to Integer")
print("2. Integer to Roman")

choice = input("Choose an option (1/2): ")

if choice == "1":
    roman = input("Enter Roman Numeral: ")
    result = roman_to_int(roman)

    if result is None:
        print("Invalid Roman Numeral!")
    else:
        print("Result:", result)

elif choice == "2":
    try:
        number = int(input("Enter Integer (1-3999): "))
        result = int_to_roman(number)

        if result:
            print("Result:", result)
        else:
            print("Number must be between 1 and 3999.")
    except ValueError:
        print("Please enter a valid integer.")

else:
    print("Invalid option.")