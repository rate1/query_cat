import csv
import re
from settings_query_cat import cat_keywords


def csv_reader(filename: str) -> list:
    """Чтение csv-файла и построчная запись содержимого в список"""
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        result = list(reader)
    return result


def csv_writer(filename: str, results: dict) -> None:
    """Запись словаря результатов в csv-файл в формате: ключ;список значений"""
    with open(filename, 'w', encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for letter, categories in results.items():
            writer.writerow([letter, categories])


def query_categorization(keywords: dict, user_letters: list) -> dict:
    """Категоризация списка текстовых значений в соответствии со словарем
    ключевых слов"""
    results = {}
    for user_letter in user_letters:
        user_letter = user_letter[0]
        categories = []
        for category, keywords in cat_keywords.items():
            for keyword in keywords:
                reg_exp = r"\b{}".format(keyword[:-1])
                if re.findall(reg_exp, user_letter):
                    categories.append(category)
                    break
        results[user_letter] = categories
    return results


def main() -> None:
    csv_filename = input("Введите имя *.csv файла для парсинга: ")
    user_letters = csv_reader(csv_filename)
    results = query_categorization(cat_keywords, user_letters)
    csv_writer("result.csv", results)


if __name__ == '__main__':
    main()
