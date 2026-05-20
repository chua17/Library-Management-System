"""LibraryService class that manages all library operations."""

from book import Book
from member import Member
from loan import Loan
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError
)


class LibraryService:
    """Service class for managing library operations.
    
    Handles all operations related to books, members, and loans.
    """
    
    def __init__(self):
        """Initialize the LibraryService."""
        self._books = {}  # Dictionary to store books by book_id
        self._members = {}  # Dictionary to store members by member_id
        self._loans = []  # List to store all loan records
        self._loan_counter = 0  # Counter for generating loan IDs
    
    # ============= BOOK OPERATIONS =============
    
    def add_book(self, book_id, title, author):
        """Add a new book to the library.
        
        Args:
            book_id (str): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book
            
        Returns:
            Book: The created Book object
        """
        book = Book(book_id, title, author)
        self._books[book_id] = book
        return book
    
    def view_books(self):
        """Get a list of all books in the library.
        
        Returns:
            list: List of Book objects
        """
        return list(self._books.values())
    
    # ============= MEMBER OPERATIONS =============
    
    def register_member(self, member_id, name, email):
        """Register a new member to the library.
        
        Args:
            member_id (str): Unique identifier for the member
            name (str): Name of the member
            email (str): Email address of the member
            
        Returns:
            Member: The created Member object
        """
        member = Member(member_id, name, email)
        self._members[member_id] = member
        return member
    
    def view_members(self):
        """Get a list of all members in the library.
        
        Returns:
            list: List of Member objects
        """
        return list(self._members.values())
    
    # ============= LOAN OPERATIONS =============
    
    def borrow_book(self, book_id, member_id):
        """Process a book borrowing request.
        
        Args:
            book_id (str): ID of the book to borrow
            member_id (str): ID of the member borrowing
            
        Returns:
            Loan: The created Loan object
            
        Raises:
            BookNotFoundError: If the book is not found
            MemberNotFoundError: If the member is not found
            BookUnavailableError: If the book is not available
        """
        # Lookup book
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")
        
        # Lookup member
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError("Member not found.")
        
        # Check if book is available
        if not book.available:
            raise BookUnavailableError("Book is already borrowed.")
        
        # Create loan
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        
        # Mark book as borrowed
        book.borrow()
        
        # Create and store loan record
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)
        
        return loan
    
    def return_book(self, loan_id):
        """Process a book return request.
        
        Args:
            loan_id (str): ID of the loan to close
            
        Returns:
            Loan: The closed Loan object
            
        Raises:
            LoanNotFoundError: If the loan is not found
        """
        # Find the loan
        loan = None
        for l in self._loans:
            if l.loan_id == loan_id:
                loan = l
                break
        
        if loan is None:
            raise LoanNotFoundError(f"Loan {loan_id} not found.")
        
        # Return the book
        loan.book.return_book()
        
        # Close the loan
        loan.close_loan()
        
        return loan
    
    def view_loans(self):
        """Get a list of all loans in the library.
        
        Returns:
            list: List of Loan objects
        """
        return self._loans
