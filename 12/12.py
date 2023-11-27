def replace_keywords(text, keywords):
    for keyword in keywords:
        text = text.replace(keyword, '*' * len(keyword))
    return text


def main():
    input_file = input("Введите имя исходного файла: ")
    keywords_file = input("Введите имя файла со служебными словами: ")
    output_file = input("Введите имя нового файла: ")

    with open(input_file, 'r') as file:
        text = file.read()

    with open(keywords_file, 'r') as keywords_file:
        keywords = [line.strip() for line in keywords_file]

    # Замена служебных слов в тексте
    text = replace_keywords(text, keywords)

    with open(output_file, 'w') as output_file:
        output_file.write(text)

    print("Замена завершена. Результат сохранен в", output_file)


if __name__ == "__main__":
    main()