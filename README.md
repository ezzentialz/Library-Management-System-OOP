📚 Library Management System
✨ Overview
This is a simple Object-Oriented Programming (OOP) project designed to manage books and their various types within a library system. It demonstrates core OOP principles including Encapsulation, Inheritance, and Polymorphism, making it an excellent example for understanding how these concepts work together in a practical application.

This project can serve as a foundational piece in your Python portfolio, showcasing your ability to design and implement structured, maintainable code using OOP.

🌟 Features
Book Management:
Add new books (Physical or E-books) to the library.
List all available books with their specific details.
Search for books by title.
Remove books by ISBN.
Object-Oriented Design:
Encapsulation: All book and library data are kept private and accessed via well-defined methods (getters/setters).
Inheritance: PhysicalBook and EBook classes inherit common properties from the base Book class, promoting code reusability.
Polymorphism: The system can treat different types of books (PhysicalBook, EBook) uniformly through a common interface (__str__ method), showcasing dynamic behavior based on object type.
🏗️ Project Structure (OOP Classes)
The system is built upon the following classes:

Book (Base Class): Represents a generic book with basic attributes like title, author, and ISBN. It provides getter methods and a string representation.
PhysicalBook (Child Class): Inherits from Book and adds a location attribute. It overrides the __str__ method to provide specific details for physical copies.
EBook (Child Class): Inherits from Book and adds a file_size attribute. It also overrides the __str__ method for E-book specific information.
Library: Manages a collection of Book objects (which can be PhysicalBook or EBook instances). It provides methods to add, list, find, and remove books.
🚀 How to Run
Save the Code: Save the provided Python code (all classes and the testing section) into a file named library_system.py.
Run from Terminal: Open your terminal or command prompt, navigate to the directory where you saved the file, and run the command:
Bash

python library_system.py
🧪 Example Usage
The library_system.py includes a testing section at the end to demonstrate its functionalities:

Python

# Create a Library instance
lb = Library()

# Create different types of books
pb = PhysicalBook("Harry Potter", "JK Rolling", "a01", "New arrival")
eb = Ebook("Learning Python", "Mor Gemini Ai", "o001", 50)

# Add books to the library
lb.add_book(pb)
lb.add_book(eb)

# List all books in the library
lb.list_all_books()

# Search for a book by title
found_book = lb.find_book_by_title("Harry Potter")
if found_book:
    print(f"Here is the book: {found_book}")
else:
    print(f"No book found")

# Remove a book by ISBN
removed_status = lb.remove_book("a01")
if removed_status:
    print(f"The book has been removed.")
else:
    print(f"The book hasn't been removed.")

# List books again to see the changes
lb.list_all_books()
🤝 Contributing
Feel free to explore, modify, or extend this project. Suggestions and improvements are always welcome!

💖 From the Developer
This project was a significant learning step in understanding Object-Oriented Programming principles. It was challenging at times, but highly rewarding to see how encapsulation, inheritance, and polymorphism work together to create a flexible and organized system.

🌟 Future Enhancements (Ideas for Next Steps)
Add functionality to manage Library Members (another set of OOP classes!).
Implement a borrow/return system for books.
Add a simple text-based user interface (TUI) for interaction.
Store data in a file (CSV/JSON) or a simple database to persist information.
