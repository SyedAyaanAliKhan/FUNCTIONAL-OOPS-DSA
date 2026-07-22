1. # 🔐 User Account Validator (OOP Practice)

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



