# 🔐 Smart Password Generator

A simple Python-based **Smart Password Generator** that creates random passwords based on user-defined requirements. It allows users to choose password length and include uppercase letters, lowercase letters, numbers, and special symbols.

## 📌 Project Overview

The Smart Password Generator is a beginner-friendly Python project designed to generate random passwords according to user preferences. It uses Python's built-in `random` and `string` modules to generate passwords.

## ✨ Features

- Generate random passwords.
- Choose custom password length.
- Include uppercase letters (A–Z).
- Include lowercase letters (a–z).
- Include numbers (0–9).
- Include special symbols (@, #, $, %, etc.).
- Basic password strength indication.
- Simple and user-friendly command-line interface.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Modules:**
  - `random` – To select random characters.
  - `string` – To access letters, digits, and special characters.

## 📂 Project Structure

```text
Smart_Password_Generator/
│
├── password_generator.py
└── README.md
```

## ⚙️ Installation and Setup

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Clone the Repository

```bash
git clone https://github.com/your-username/Smart-Password-Generator.git
```

### Step 3: Open the Project Folder

```bash
cd Smart-Password-Generator
```

### Step 4: Run the Program

```bash
python password_generator.py
```

## 🚀 How to Use

1. Run the Python program.
2. Enter your desired password length.
3. Choose whether to include uppercase letters.
4. Choose whether to include lowercase letters.
5. Choose whether to include numbers.
6. Choose whether to include special symbols.
7. The program generates a random password.
8. View the basic password strength indication.

## 💻 Example Output

```text
===================================
      SMART PASSWORD GENERATOR
===================================

Enter password length: 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include special symbols? (y/n): y

Your Generated Password: A#8kP2@mQ9$x

Password Strength: Strong
```

*Note: The generated password will be different each time.*

## 🎯 Project Objective

The main objective of this project is to understand Python programming concepts such as:

- Random number and character generation.
- Conditional statements.
- User input handling.
- String manipulation.
- Working with Python built-in modules.

## 🔮 Future Enhancements

- Graphical User Interface (GUI) using Tkinter.
- Copy generated password to clipboard.
- Password history management.
- Advanced password strength checker.
- Custom character selection.
- Secure password generation using Python's `secrets` module.

## 🔒 Security Note

This beginner project uses Python's `random` module for educational purposes. For real-world password generation, Python's `secrets` module is recommended because it provides cryptographically secure random values.

## 👩‍💻 Author

**Nibha**

Data Science Student

## 📄 License

This project is created for educational and learning purposes.
