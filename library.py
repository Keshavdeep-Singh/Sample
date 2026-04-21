# Data storage
books = []
issued_books = []

# Add book
def add_book():
    name = input("Enter book name: ")
    books.append(name)
    print("Book added")

# Show books
def show_books():
    if len(books) == 0:
        print("No books available.")
    else:
        print("Available Books: ")
        for b in books:
            print(b)

# Issue book
def issue_book():
    if len(books) == 0:
        print("No books available.")
        return
    
    name = input("Enter book name to issue: ")

    if name in books:   
        books.remove(name)
        issued_books.append(name)
        print(name,"Book issued.")
    else:
        print("Book is not available.")

# Return book
# def return_book():
#     name = input("Enter book name to return: ")

#     if name in issued_books:
#         issued_books.remove(name)
#         books.append(name)
#         print(name,"Book returned.")
#     else:
#         print(name," was not issued.")

# Main menu
def library():
    while True:
        print("-"*10,"Menu","-"*10)
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        print("-"*30,"\n")

        choice = int(input("Enter choice: "))
        print("-"*30,'\n')
        if choice == 1:
            add_book()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank you")
            break
        else:
            print("Invalid choice")

# Run
library()