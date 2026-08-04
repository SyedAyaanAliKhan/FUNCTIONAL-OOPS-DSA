class Library:
    def __init__(self):
        self.members = []
        self.books = ["harry potter", "the hobbit", "goosebumps", "marvel comics"]


    def book_borrowed(self, borrowed_input):
        if borrowed_input in self.books:
            self.books.remove(borrowed_input)
            return f"updated stock {self.books}"
        else:
            return "Book not in stock"



    def book_returned(self, returned_book):
        self.books.append(returned_book)
        return f"updated stock {self.books}"



class Person:
    def __init__(self, name, password, id):
        self.name = name
        self.__password = password
        self.id = id


    def auth(self, check_pass):
        if check_pass == self.__password:
            return "Access Granted"
        else:
            return "Invalid credentials"

    @property
    def password(self):
        return "****"

    @password.setter
    def password(self, new_pass):
        if len(new_pass) < 4:
            print("Password must be at least 4 digits")
        else:
            self.__password = new_pass

        

class Member(Person):
    def __init__(self, name, password, id, mem_key):
        super().__init__(name, password, id)
        self.mem_key = mem_key        

    def mem_verify(self, mem_verify):
        if mem_verify == self.mem_key:
            return "Access Granted"
        else:
            return "Access Denied"

class LibraryAdmin(Person):
    def __init__(self, name, password, id, admin_key):
        super().__init__(name, password, id)
        self.admin_key = admin_key

    def key_verify(self, verification):
        if verification == self.admin_key:
            return "Access Granted"
        else:
            return "Access Denied"



lib  = Library()
member1 = Member("Ayaan", "123", "ayaan123", "000") #members key = 000
action1 = input("Enter your members key to log in the online library: ")
check = member1.mem_verify(action1)
if check == "Access Granted":
    userask = input("Do you want to borrow or return a book: ").lower()
    if userask == "return":
        returned_book = input("Enter the name of the book you want to return: ").lower()
        print(lib.book_returned(returned_book))

    elif userask == "borrow":
        print(f"Available Stock - {lib.books}")
        borrowed_book = input("Enter the name of the book you want to borrow: ").lower()
        print(lib.book_borrowed(borrowed_book))
    else:
        print("Please choose if you want to return or borrow a book")
else:
    print("Invalid Key")

