## 1. 🔐 User Account Validator (OOP Practice)

A simple Python project demonstrating **Object-Oriented Programming (OOP)** concepts such as **encapsulation**, **data validation**, and **admin-gated access control** using a `Data` class.

---

## ✨ Features

- 🔒 Encapsulates the password using a private attribute (`self.__password`)
- 📧 Validates email addresses with basic format checking
- 🔑 Restricts access to user information through an admin key
- ✅ Validates password length before returning user data
- 🧩 Demonstrates classes, objects, constructors, and methods
- ♻️ Uses reusable methods that return values instead of printing directly

---

## ⚙️ How It Works

The `Data` class stores a user's email and password and provides methods to:

- 📧 Validate the email format
- 🔐 Verify the password meets the minimum length requirement
- 🛡️ Check the admin key before allowing access to the validated account information

---

## 📚 Concepts Used

- 🏗️ Object-Oriented Programming (OOP)
- 🔒 Encapsulation
- ⚡ Constructors (`__init__`)
- 🧠 Conditional Statements
- 📥 User Input
- ✔️ Data Validation
- 🎯 Access Control

---

## 🚀 Future Improvements

- 🔐 Hash passwords instead of storing them as plain text
- 📧 Improve email validation using Regular Expressions (Regex)
- 👥 Support multiple user accounts
- 💾 Store user data in a database
- 🌍 Load the admin key from environment variables
- 🚫 Add retry limits for invalid admin key attempts
- 🛡️ Build a complete authentication and login system

---

## ⚠️ Note

This project was created for learning and practicing **Python OOP fundamentals**. It focuses on understanding encapsulation, validation, and basic access control rather than implementing a production-ready authentication system.

---

## 2. 🏦 Bank Account Management System (OOP Practice)

A simple Python project demonstrating **Object-Oriented Programming (OOP)** concepts such as **encapsulation**, **data validation**, and **exception handling** through a command-line banking system.

---

## ✨ Features

* 🏦 Deposit money into a bank account
* 💸 Withdraw money with insufficient balance protection
* 💰 View the current account balance
* 🔒 Uses a protected attribute (`self._balance`) to store account balance
* ⚠️ Handles invalid inputs using exception handling
* 🧩 Demonstrates classes, objects, constructors, and methods
* ♻️ Uses reusable methods that return values instead of printing directly

---

## ⚙️ How It Works

The `BankAccount` class stores the account owner's name and balance and provides methods to:

* 💰 Deposit money into the account
* 💸 Withdraw money while checking for sufficient funds
* 📊 Display the current account balance
* ⚠️ Validate transaction amounts and prevent invalid operations

---

## 📚 Concepts Used

* 🏗️ Object-Oriented Programming (OOP)
* 🔒 Encapsulation
* ⚡ Constructors (`__init__`)
* 🧠 Conditional Statements
* 📥 User Input
* ✔️ Data Validation
* 🚨 Exception Handling
* 🔁 Loops

---

## 🚀 Future Improvements

* 📝 Add transaction history
* 👥 Support multiple bank accounts
* 💾 Save account data to a file or database
* 🔢 Generate unique account numbers
* 💳 Add fund transfers between accounts
* 📈 Include interest calculation and account types
* 🔐 Implement PIN or password-based authentication

---

## ⚠️ Note

This project was created for learning and practicing **Python OOP fundamentals**. It focuses on understanding encapsulation, validation, exception handling, and basic banking operations rather than implementing a production-ready banking system.


---


### 3.📚 Library Management System (Python OOP)

A simple **Library Management System** built using **Object-Oriented Programming (OOP)** principles in Python. This project allows library members to borrow and return books while demonstrating key OOP concepts such as **inheritance, encapsulation, constructors, properties, and method overriding through class specialization**.

---

## 🚀 Features

* 📖 View available books in the library
* 📥 Borrow a book (removes it from stock)
* 📤 Return a book (adds it back to stock)
* 🔐 Member authentication using a membership key
* 🔒 Password encapsulation using private attributes
* ⚙️ Password getter and setter using Python properties
* 👤 Separate classes for Members and Library Admins

---

## 🛠️ OOP Concepts Used

### 1. Classes & Objects

* `Library`
* `Person`
* `Member`
* `LibraryAdmin`

### 2. Constructors

Each class uses the `__init__()` constructor to initialize object attributes.

### 3. Inheritance

Both `Member` and `LibraryAdmin` inherit from the `Person` class.

### 4. Encapsulation

The password is stored as a private attribute (`__password`) and accessed through getter and setter methods.

### 5. Properties

Python's `@property` and `@password.setter` decorators are used to safely access and modify passwords.

### 6. Method Specialization

Different authentication methods are implemented for members and administrators using separate class methods.

---

## 📂 Project Structure

```
Library Management System
│
├── Library
│   ├── book_borrowed()
│   └── book_returned()
│
├── Person
│   ├── auth()
│   ├── password (Property)
│   └── password Setter
│
├── Member (inherits Person)
│   └── mem_verify()
│
├── LibraryAdmin (inherits Person)
│   └── key_verify()
│
└── Main Program
```

---

## ▶️ How It Works

1. The user enters the membership key.
2. If the key is valid, access to the library is granted.
3. The user chooses to:

   * Borrow a book
   * Return a book
4. The library stock is updated accordingly.
5. If the membership key is incorrect, access is denied.

---

## 📚 Default Library Books

```
Harry Potter
The Hobbit
Goosebumps
Marvel Comics
```

---

## 🔑 Default Member Credentials

| Item        | Value |
| ----------- | ----- |
| Member Name | Ayaan |
| Member Key  | 000   |

---

## ▶️ Example Output

```
Enter your members key to log in the online library: 000

Do you want to borrow or return a book:
borrow

Available Stock -
['harry potter', 'the hobbit', 'goosebumps', 'marvel comics']

Enter the name of the book you want to borrow:
harry potter

updated stock ['the hobbit', 'goosebumps', 'marvel comics']
```

---

## 💻 Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

---

## 🎯 Learning Objectives

This project was created to practice:

* Object-Oriented Programming in Python
* Inheritance
* Encapsulation
* Constructors
* Properties (Getter & Setter)
* Working with Lists
* User Input Handling
* Basic Library Inventory Management

---

## 📌 Future Improvements

* Add multiple members with unique accounts
* Store data in files or a database
* Implement book search functionality
* Allow admins to add or remove books
* Track borrowed books by each member
* Generate borrowing history
* Improve authentication using usernames and passwords

---

## 👨‍💻 Author

**Ayaan**

A beginner-friendly Python project demonstrating the fundamentals of Object-Oriented Programming through a simple library management system.



##
