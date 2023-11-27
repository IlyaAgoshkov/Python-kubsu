from operator import itemgetter
# Считывание входных данных
n = int(input())  # Считываем количество строк
word_count = {}   # Словарь для подсчета слов

# Заполнение словаря словами и их частотами
for _ in range(n):
    line = input().lower().split()  # Предполагаем, что слова разделены пробелами и нечувствительны к регистру
    for word in line:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


# Сортировка по слову (возрастание)
sorted_words = sorted(word_count.items(), key=itemgetter(0))

# Сортировка по частоте (убывание), сохраняя порядок слов
sorted_words = sorted(sorted_words, key=itemgetter(1), reverse=True)

# Вывод результатов
for word, freq in sorted_words:
    print(word)