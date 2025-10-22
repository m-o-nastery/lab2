import random
import csv

def read_line(Books):
    twenty_books = []
    for i in range(20):
        Books.seek(0)
        reader = csv.DictReader(Books, delimiter=';')

        for row in range(random.randint(1, 300)):
            fields = next(reader)

        if len(str(fields["Дата поступления"])[6:10]) == 0:
            twenty_books.append([f"{i + 1}. {fields['Автор (ФИО)']}. {fields['Название']} - дата поступления неизвестна"])
        elif len(str(fields["Автор (ФИО)"])) == 0:
            twenty_books.append([f"{i + 1}. Автор неизвестен. {fields['Название']} - {str(fields['Дата поступления'])[6:10]}"])
        elif len(str(fields["Дата поступления"])[6:10]) == 0 and len(str(fields["Автор (ФИО)"])) == 0:
            twenty_books.append([f"{i + 1}. Автор неизвестен. {fields['Название']} - дата поступления неизвестна"])
        else:
            twenty_books.append([f"{i + 1}. {fields['Автор (ФИО)']}. {fields['Название']} - {str(fields['Дата поступления'])[6:10]}"])
    return twenty_books


if __name__ == '__main__':
    with open('books.csv') as Books, open('twenty_books.csv', 'w', newline='', encoding='utf-8') as Twenty_books:
        writer = csv.writer(
            Twenty_books, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\'
        )
        writer.writerows(read_line(Books))
