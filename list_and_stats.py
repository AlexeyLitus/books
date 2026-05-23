from collections import Counter

def show_average_rating(books):
    """Показывает среднюю оценку всех книг."""
    if not books:
        print("\n Список книг пуст.")
        return

    total = sum(book['оценка'] for book in books)
    average = total / len(books)
    print(f"\n Средняя оценка ваших книг: {average:.2f}")

def authors_statistics(books):
    """Показывает статистику по авторам (сколько книг у каждого)."""
    if not books:
        print("\n Список книг пуст.")
        return

    authors = [book['автор'] for book in books]
    counter = Counter(authors)

    print("\n Статистика по авторам:")
    for author, count in counter.items():
        print(f"• {author}: {count} книг")

def show_books(books):
    """Показывает все книги в списке."""
    if not books:
        print("\n Список книг пуст.")
        return

    print("\n Ваш список прочитанных книг:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['название']} | {book['автор']} | Оценка: {book['оценка']} | Дата: {book['дата_прочтения']}")