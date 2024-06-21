library = {}

def add_book():

    book_info = input("\nEnter the title, genre, and price of the book (separated by |): ") 
    title, genre, price = book_info.split("|")  
    library[title] = (genre, float(price)) 
    print("\nAdded %s to the library." % title) 
    return True

def remove_book():
    
    title = input("Enter the title of the book to remove: ")
    if title in library:
        del library[title] 
        print("\nRemoved %s from the library." % title)
        return True
    else:
        print(title, "not found in the library.") 
        return False

def get_book_info():

    title = input("Enter the title of the book: ")
    if title in library:
        genre, price = library[title]
        print("Title: %s\nGenre: %s\nPrice: $%.2f" % (title, genre, price))
    else:
        print("Error: %s not found in the library." % title) 

def list_books():

    if not library:
        print("\nThe library is empty.\n")
        return False
    print()
    for title, (genre, price) in sorted(library.items()):
        print("\n%s (%s, $%.2f)" % (title, genre, price)) 
    print()
    return True

def list_books_by_genre():

    genre = input("Enter the genre to search for: ")
    genre_books = [(title, price) for title, (book_genre, price) in library.items() if book_genre.lower() == genre.lower()] 
    if genre_books:
        genre_books.sort()
        print("\n")
        for title, price in genre_books:
            print("%s ($%.2f)" % (title, price))  
        print()
        return True
    else:
        print("No books found in the %s genre." % genre)
        return False

while True:
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_book_return = add_book()
        if add_book_return:
            list_books()
    elif choice == "2":
        remove_book_return = remove_book()
        if remove_book_return:
            list_books()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

print("Goodbye!")