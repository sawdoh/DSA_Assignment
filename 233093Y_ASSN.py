""""
Sean Heng ChuanJie
233093Y
IT 2553 - Tutorial Group 03
"""


class Book:
    def __init__(self, isbn, title, category, publisher, year_published):
        self.isbn = isbn
        self.title = title
        self.category = category
        self.publisher = publisher
        self.year_published = year_published

    def display(self):
        # return f"ISBN: {self.isbn}, Title: {self.title}, Category: {self.category}, Publisher: {self.publisher}, Year Published: {self.year_published}"
        return f"ISBN: {self.isbn}\n, Title: {self.title}\n, Category: {self.category}\n, Publisher: {self.publisher}\n, Year Published: {self.year_published}\n{'-'*30}"

class BookManagement:
    def __init__(self):
        self.books = []

    def populate_data(self):
        self.books = []
        self.books.append(Book("B102", "The don't laugh challenge", "Humour", "Oreilly", 2019))
        self.books.append(Book("B107", "How to draw everything for kids", "Kids Art", "Wiley", 1998))
        self.books.append(Book("B101", "Book on Planet Earth", "Science", "Oreilly", 2021))
        self.books.append(Book("B105", "Kids Encyclopedia", "Encyclopedia", "Ladybird", 1999))
        self.books.append(Book("B104", "I am 10 and amazing", "Inspiration", "Wiley", 2022))
        self.books.append(Book("B106", "Ocean Animals", "Science", "Oreilly", 2023))
        self.books.append(Book("B103", "Inspiring Stories for Kids", "Inspiration", "Oreilly", 2022))
        # self.books.append(Book("B110", "Coding for Kids", "Coding", "Popular", 2024))
        print("Books populated!\n")

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(book.display())

def display_menu():
    print("\nMenu:")
    print("1. Add new Books")
    print("2. Display all books")
    print("3. Sort books by Category (Bubble Sort) Ascend")
    print("4. Sort books by Publisher (Selection Sort) Descend")
    print("9. Populate data")
    print("0. Exit")

def bubble_sort_books(books):
    n = len(books)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if books[j].category > books[j+1].category:
                books[j], books[j+1] = books[j+1], books[j]
                swapped = True
        if not swapped:
            break
        # disply the pass
        # print("Pass", i + 1, ":", [book.isbn for book in books])

        print(f"Pass {i + 1}:")
        print("-"*30)
        for book in books:
            print(f"Book ISBN Number:  {book.isbn}")
        print("-" * 30)
        if not swapped:
            break


def selection_sort_books(books):
    n = len(books)
    for i in range(n-1):
        max_idx = i

        for j in range(i+1, n):
            if books[j].publisher > books[max_idx].publisher:
                max_idx = j

        # swap max w/ first
        books[i], books[max_idx] = books[max_idx], books[i]
        # display
        # print("Pass", i+1, ":", [book.isbn for book in books])
        print(f"Pass {i + 1}:")
        print("-" * 30)
        for book in books:
            print(f"Book ISBN Number:  {book.isbn}")
        print("-"*30)





def main():
    book_management = BookManagement()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '2':
            book_management.display_books()
        elif choice == '1':
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            category = input("Enter Category: ")
            publisher = input("Enter Publisher: ")
            year_published = int(input("Enter Year Published: "))
            new_book = Book(isbn, title, category, publisher, year_published)
            book_management.add_book(new_book)
            print("Book added successfully!")
        elif choice == '3':
            if book_management.books:
                print("Sorting books by Category using Bubble Sort...")
                bubble_sort_books(book_management.books)
                print("Books sorted by Category:")
                book_management.display_books()
            else:
                print("No books to sort.")
        elif choice == '4':
            if book_management.books:
                print("Sorting books by Publisher using Selection Sort...")
                selection_sort_books(book_management.books)
                print("Books sorted by Publisher:")
                book_management.display_books()
            else:
                print("No books to sort.")
        elif choice == '9':
            book_management.populate_data()
        elif choice == '0':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
