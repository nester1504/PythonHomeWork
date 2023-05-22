def check_rhythm(poem):
    lines = poem.split()
    vowel_counts = []

    for line in lines:
        words = line.split('-')
        vowel_count = sum(
            1 for word in words for char in word if char.lower() in 'aeiouаеёиоуыэюя')
        vowel_counts.append(vowel_count)

    if len(set(vowel_counts)) == 1:
        return 'Парам пам-пам'
    else:
        return 'Пам парам'


poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)
