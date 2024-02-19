class Library:
    def __init__(self):
        try:
            self.file = open("books.txt", "a+")
        except Exception as e:
            print("An error occurred while opening the file:", e)
            exit()

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)  
        books = self.file.read().splitlines()
        if not books:
            print("No books found.")
        else:
            print("ID\tTitle\t\tAuthor")
            print("-" * 30)
            for i, book in enumerate(books, 1):
                book_info = book.split(',')
                print(f"{i}\t{book_info[0]}\t\t{book_info[1]}")

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        release_year = input("Enter the release year: ")
        num_pages = input("Enter the number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        self.list_books()
        try:
            book_id = int(input("Enter the ID of the book to remove: "))
            self.file.seek(0)
            books = self.file.readlines()
            if 1 <= book_id <= len(books):
                del books[book_id - 1]
                self.file.seek(0)
                self.file.truncate()
                self.file.writelines(books)
                print("Book removed successfully.")
            else:
                print("Invalid book ID.")
        except ValueError:
            print("Invalid input. Please enter a valid ID.")

def menu():
    print("*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

def main():
    lib = Library()
    while True:
        menu()
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.add_book()
        elif choice == '3':
            lib.remove_book()
        elif choice == '4':
            del lib
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()