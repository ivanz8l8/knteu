def process_string(input_string):
    if len(input_string) % 2 == 0:
        mid = len(input_string) // 2
        first_half = input_string[:mid]
        second_half = input_string[mid:]
        modified_string = first_half + second_half.upper()
        return modified_string
    else:
        return input_string  

try:
    N = int(input("Введіть кількість рядків: "))
    result = []

    for _ in range(N):
        user_input = input("Введіть рядок з парною довжиною: ")
        modified_input = process_string(user_input)
        result.append(modified_input)

    print("Результат:")
    for modified_string in result:
        print(modified_string)

except ValueError:
    print("Будь ласка, введіть правильне ціле число для кількості рядків.")
