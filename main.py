"""Main module for the Library Management System."""

from library_service import LibraryService
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError
)


def display_menu():
    """Display the main menu for the library system."""
    print("\n" + "="*50)
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")
    print("="*50)


def add_book(service):
    """Handle adding a new book to the library.
    
    Args:
        service (LibraryService): The library service instance
    """
    try:
        print("\n--- Add Book ---")
        book_id = input("Enter Book ID: ").strip()
        if not book_id:
            print("Error: Book ID cannot be empty.")
            return
        
        title = input("Enter Book Title: ").strip()
        if not title:
            print("Error: Title cannot be empty.")
            return
        
        author = input("Enter Book Author: ").strip()
        if not author:
            print("Error: Author cannot be empty.")
            return
        
        book = service.add_book(book_id, title, author)
        print(f"Book added: {book.title}")
    except Exception as e:
        print(f"Error: {e}")


def register_member(service):
    """Handle registering a new member.
    
    Args:
        service (LibraryService): The library service instance
    """
    try:
        print("\n--- Register Member ---")
        member_id = input("Enter Member ID: ").strip()
        if not member_id:
            print("Error: Member ID cannot be empty.")
            return
        
        name = input("Enter Member Name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            return
        
        email = input("Enter Member Email: ").strip()
        if not email:
            print("Error: Email cannot be empty.")
            return
        
        member = service.register_member(member_id, name, email)
        print(f"Member registered: {member.name}")
    except Exception as e:
        print(f"Error: {e}")


def borrow_book(service):
    """Handle borrowing a book.
    
    Args:
        service (LibraryService): The library service instance
    """
    try:
        print("\n--- Borrow Book ---")
        book_id = input("Enter Book ID: ").strip()
        if not book_id:
            print("Error: Book ID cannot be empty.")
            return
        
        member_id = input("Enter Member ID: ").strip()
        if not member_id:
            print("Error: Member ID cannot be empty.")
            return
        
        loan = service.borrow_book(book_id, member_id)
        print(f"{loan.member.name} borrowed {loan.book.title}")
    except BookNotFoundError as e:
        print(f"Error: {e}")
    except MemberNotFoundError as e:
        print(f"Error: {e}")
    except BookUnavailableError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def return_book(service):
    """Handle returning a book.
    
    Args:
        service (LibraryService): The library service instance
    """
    try:
        print("\n--- Return Book ---")
        loan_id = input("Enter Loan ID: ").strip()
        if not loan_id:
            print("Error: Loan ID cannot be empty.")
            return
        
        loan = service.return_book(loan_id)
        print(f"{loan.member.name} returned {loan.book.title}")
    except LoanNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def view_books(service):
    """Display all books in the library.
    
    Args:
        service (LibraryService): The library service instance
    """
    print("\n--- View Books ---")
    books = service.view_books()
    if not books:
        print("No books found.")
    else:
        print("\nBooks:")
        for book in books:
            print(f"  {book}")


def view_members(service):
    """Display all members in the library.
    
    Args:
        service (LibraryService): The library service instance
    """
    print("\n--- View Members ---")
    members = service.view_members()
    if not members:
        print("No members found.")
    else:
        print("\nMembers:")
        for member in members:
            print(f"  {member}")


def view_loans(service):
    """Display all loans in the library.
    
    Args:
        service (LibraryService): The library service instance
    """
    print("\n--- View Loans ---")
    loans = service.view_loans()
    if not loans:
        print("No loans found.")
    else:
        print("\nLoans:")
        for loan in loans:
            print(f"  {loan}")


def main():
    """Main function to run the library management system."""
    service = LibraryService()
    
    print("\n*** Welcome to Library Management System ***")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == "1":
            add_book(service)
        elif choice == "2":
            register_member(service)
        elif choice == "3":
            borrow_book(service)
        elif choice == "4":
            return_book(service)
        elif choice == "5":
            view_books(service)
        elif choice == "6":
            view_members(service)
        elif choice == "7":
            view_loans(service)
        elif choice == "8":
            print("\nProgram closed.")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
