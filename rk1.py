from dataclasses import dataclass


@dataclass
class Book:
    id: int
    title: str
    pages: int
    library_id: int


@dataclass
class Library:
    id: int
    name: str


@dataclass
class BookLibrary:
    book_id: int
    library_id: int


def main():
    libraries = [
        Library(1, "Городская библиотека"),
        Library(2, "Районная библиотека"),
        Library(3, "Университетская библиотека"),
    ]
    books = [
        Book(1, "Мастер и Маргарита", 480, 1),
        Book(2, "Алые паруса", 128, 1),
        Book(3, "Алиса в Стране чудес", 192, 2),
        Book(4, "Капитанская дочка", 160, 3),
    ]

    # Связь многие-ко-многим: «Алые паруса» есть в двух библиотеках.
    book_libraries = [
        BookLibrary(1, 1),
        BookLibrary(2, 1),
        BookLibrary(2, 3),
        BookLibrary(3, 2),
        BookLibrary(4, 3),
    ]

    library_names = {library.id: library.name for library in libraries}
    book_titles = {book.id: book.title for book in books}

    print("В1. Книги на букву «А» и их библиотеки")
    for book in books:
        if book.title.startswith("А"):
            print(f"{book.title} — {library_names[book.library_id]}")

    # Для каждой непустой библиотеки находим минимум страниц.
    min_pages = []
    for library in libraries:
        pages = [book.pages for book in books if book.library_id == library.id]
        if pages:
            min_pages.append((library.name, min(pages)))

    print("\nВ2. Минимальное число страниц по библиотекам")
    for name, pages in sorted(min_pages, key=lambda item: item[1]):
        print(f"{name} — {pages} стр.")

    # Собираем пары по таблице связей и сортируем по названию книги.
    pairs = [
        (book_titles[link.book_id], library_names[link.library_id])
        for link in book_libraries
    ]

    print("\nВ3. Все пары «книга — библиотека»")
    for title, name in sorted(pairs, key=lambda item: item[0]):
        print(f"{title} — {name}")


if __name__ == "__main__":
    main()
