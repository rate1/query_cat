import csv
from settings_query_cat import keywords


def csv_reader(filename: str) -> list:
    pass


def csv_writer(filename: str, results: dict) -> None:
    pass


def query_categorization(keywords: dict, user_letters: list) -> dict:
    pass


def main() -> None:
    csv_filename = input("Введите имя *.csv файла для парсинга: ")
    user_letters = csv_reader(csv_filename)
    results = query_categorization(keywords, user_letters)
    csv_writer("result.csv", results)


if __name__ == '__main__':
    main()
