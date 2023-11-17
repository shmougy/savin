def count_case_pairs_and_vowels(word):

    upper_lower_pairs = 0
    vowel_count = 0

    for i in range(len(word) - 1):
        current_char = word[i]
        next_char = word[i + 1]

        # проверяем является ли текущий символ верхним и следующий нижним или наоборот
        if current_char.isupper() and next_char.islower() or current_char.islower() and next_char.isupper():
            upper_lower_pairs += 1

    # подсчитываем гласные
    vowels = "aeiouAEIOU"
    for char in word:
        if char in vowels:
            vowel_count += 1

    return upper_lower_pairs, vowel_count


# получаем слово
word = input("Введите слово: ")

# вызываем функцию для подсчета пар и гласных
pairs, vowels = count_case_pairs_and_vowels(word)

print(f"Количество пар верхнего и нижнего регистра: {pairs}")
print(f"Количество гласных букв: {vowels}")
