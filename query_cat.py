import csv
import re
import os.path
from settings_query_cat import CAT_KEYWORDS


def csv_reader(filename: str) -> list:
    """Чтение csv-файла и построчная запись содержимого в список"""
    try:
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            result = list(reader)
    except:
        return None
    return result


def csv_writer(filename: str, results: dict) -> None:
    """Запись словаря результатов в csv-файл в формате: ключ(письмо пользователя);категория(самое релевантное из значений"""
    with open(filename, 'w', encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for letter, categories in results.items():
            writer.writerow([letter, categories[0]])


def query_categorization(keywords: dict, user_letters: list) -> dict:
    """Категоризация списка текстовых значений в соответствии со словарем
    ключевых слов"""
    results = {}
    for user_letter in user_letters:
        user_letter = user_letter[0]
        categories = []
        for category, keywords in CAT_KEYWORDS.items():
            for keyword in keywords:
                reg_exp = r"\b{}\w{}\b".format(keyword[:-1], "{0,3}").lower()
                if re.findall(reg_exp, user_letter.lower()):
                    categories.append(category)
                    break
        results[user_letter] = categories
    return results


def main() -> None:
    while(True):
        csv_filename = input("Введите имя csv-файла с письмами пользователей: ")
        if os.path.exists(csv_filename):
            break
        print("Файл не найден.")

    user_letters = csv_reader(csv_filename)
    if user_letters:
        results = query_categorization(CAT_KEYWORDS, user_letters)
        csv_writer("result.csv", results)
        print("Результат категоризации запросов сохранен в файл result.csv")
    else:
        print("Csv-файл содержит не корректные данные")


if __name__ == '__main__':
    main()
