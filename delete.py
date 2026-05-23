FILENAME = 'books.json'

def delete_book(books):
    """Удаляет книгу по её номеру из списка."""
    if not books:
        print("\n Список книг пуст.")
        return

    while True:
        choice = input(f"\n Введите номер книги для удаления (1-{len(books)}), или 0 для отмены: ")
        
        if choice == '0':
            print(" Отмена удаления.")
            return
            
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(books):
                removed_book = books.pop(index)
                print(f"🗑 Книга '{removed_book['название']}' удалена!")
                return
        
        print(f" Неверный номер. Введите число от 1 до {len(books)} или 0.")