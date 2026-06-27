def main_library():
    library_stock = ['Harry Potter', 'The Hobbit', 'Goosebumps']
    return library_stock

def return_book(lib):
    returned_book_added= input("Please enter the name of the book you want to return: ")
    lib.append(returned_book_added)

    print(f"Book added!, current stock {lib}")
    return lib


def book_borrow(lib):
    print("Available books", lib)
    book_borrow = input("Which book do you want to borrow: ")
    if book_borrow in lib:
        lib.remove(book_borrow)
    print(lib)




def book_available(lib):
    check_book = input("Search for a book by entering its title: ")
    if check_book in lib:
        print("Book is available")
    else:
        print("Book is not available")
    





def final_run(lib):
    while True:
        print("\nWelcome to the Library!!")
        print("1. Return Book")
        print("2. Borrow Book")
        print("3. Book Availability")
        print("4. Exit")

        options = int(input("Choose an option (1,2,3,4): "))
        if options == 1:
            lib = return_book(lib)
        
        elif options == 2:
            lib = book_borrow(lib)
        
        elif options == 3:
            lib = book_available(lib)

        elif options == 4:
            break

        else:
            print("Invalid option choose again")

        
library = main_library()
final_run(library)
        





    