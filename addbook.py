def get_valid_rating():
    """Запрашивает у пользователя оценку и проверяет, что это число от 1 до 5."""
    while True:
        rating = input("Оценка (от 1 до 5): ")
        if rating.isdigit():
            rating = int(rating)
            if 1 <= rating <= 5:
                return rating
        print("Оценка должна быть целым числом от 1 до 5.")

def add_book(books):
    """Добавляет новую книгу в список."""
    print("\n--- Добавление новой книги ---")
    author = input("Автор: ").strip()
    title = input("Название: ").strip()
    rating = get_valid_rating()
    date = input("Дата прочтения (ГГГГ-ММ-ДД): ").strip()

    book = {
        "автор": author,
        "название": title,
        "оценка": rating,
        "дата_прочтения": date
    }
    books.append(book)
    print("Книга успешно добавлена!")
