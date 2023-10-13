def is_palindrome(word):
    return word == word[::-1]

input_string = input("Введіть рядок слів, розділених пробілами: ")
words = input_string.split()

shortest_palindrome = None
shortest_length = float('inf')

for word in words:
    if is_palindrome(word) and len(word) < shortest_length:
        shortest_palindrome = word
        shortest_length = len(word)

if shortest_palindrome:
    print(f"Найкоротше слово-паліндром: {shortest_palindrome}")
else:
    print("У введеному рядку немає слов-паліндромів.")
