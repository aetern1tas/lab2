import csv
import random


def long_title():
    count = 0
    with open('books-en.csv', 'r') as file:
        table = csv.reader(file, delimiter=';')
        next(table)
        for row in table:
            if len(row[1]) > 30:
                count += 1
    print(f"Книг с длинным названием: {count}")

def cheap_books():
    author = input('Введите автора: ')
    found = False
    with open('books-en.csv', 'r') as file:
        table = csv.reader(file, delimiter=';')
        next(table)
        for row in table:
            price = row[6].replace(',', '.')
            if row[2] == author and float(price) < 150:
                print(row[1])
                found = True
    if not found:
        print('Книг не найдено. Попробуйте снова')


def generate_bibliografy():
    with open('books-en.csv', 'r') as file:
        table = list(csv.reader(file, delimiter=';'))[1:]
        selected_books = random.sample(table, 20)

        with open('bibliography.txt', 'w') as output_file:
            for i, book in enumerate(selected_books, 1):
                author = book[2]
                title = book[1]
                year = book[3]
                reference = f"{author}. {title} - {year}"
                output_file.write(f"{i}. {reference}\n")
    
    print("Файл 'bibliography.txt' создан")



def main():
    long_title()
    cheap_books()
    generate_bibliografy()

if __name__ == "__main__":
    main()