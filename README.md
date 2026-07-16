1. # 📚 Library Management System (Python)

A simple command-line Library Management System built using Python to practice core programming concepts such as functions, lists, loops, conditionals, and user input.

## Features

* 📖 Borrow a book
* 📚 Return a book
* 🔍 Check book availability
* 📋 Display available books
* 🔄 Interactive menu-driven interface

## Concepts Used

* Functions
* Parameters and return values
* Lists and list operations (`append`, `remove`)
* Conditional statements (`if`, `elif`, `else`)
* Loops (`while`)
* User input handling

## Purpose

This project was developed as part of my Python learning journey to strengthen my understanding of procedural programming before moving on to Object-Oriented Programming (OOP) and Data Structures & Algorithms (DSA).

### Future Improvements

* Convert the project into an Object-Oriented Programming (OOP) version
* Store book data in files or a database
* Add user authentication





2. ## User Account Validator (OOP Practice)

A small Python project demonstrating encapsulation, validation, and 
admin-gated access control using a `Data` class.

### What it demonstrates
- **Encapsulation** — sensitive data (`password`) is protected using name-mangled 
  private attributes (`self.__password`)
- **Data validation** — custom methods validate email format and password length
- **Access control** — an admin-only method (`admin_check`) gates access to 
  sensitive account data behind a key comparison
- **Clean return values** — methods return data rather than printing directly, 
  keeping the class flexible and reusable

### How it works
The `Data` class represents a user account with an email and password. It includes:
- `email_validate()` — checks the email contains `@` and `.com`
- `pass_validate()` — checks the password meets a minimum length
- `admin_check(key)` — only reveals validated account details if the correct 
  admin key is provided

### Note
This is a learning project focused on OOP fundamentals, not a production-ready 
authentication system. Real-world apps would hash passwords, store secrets in 
environment variables, and add rate-limiting on key attempts.
* Track borrowed books and due dates
* Improve input validation and error handling
