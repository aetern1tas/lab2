import csv

def task1():
    count = 0
    with open('books-en.csv', 'r') as file:
        table = csv.reader(file, delimiter=';')
        next(table)
        for row in table:
            if len(row[1]) > 30:
                count += 1
    print(f"Книг с длинным названием: {count}")

def task2():
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

def main():
    task1()
    task2()

if __name__ == "__main__":
    main()