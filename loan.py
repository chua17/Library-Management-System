"""Loan class for the Library Management System."""

from datetime import datetime


class Loan:
    """Represents a loan transaction in the library.
    
    Attributes:
        loan_id (str): Unique identifier for the loan
        book: The Book object being borrowed
        member: The Member object borrowing the book
        loan_date (datetime): Date when the book was borrowed
        return_date (datetime): Date when the book was returned (if applicable)
        is_active (bool): Whether the loan is currently active
    """
    
    def __init__(self, loan_id, book, member):
        """Initialize a Loan object.
        
        Args:
            loan_id (str): Unique identifier for the loan
            book: The Book object being borrowed
            member: The Member object borrowing the book
        """
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.loan_date = datetime.now()
        self.return_date = None
        self.is_active = True
    
    def close_loan(self):
        """Close the loan by setting return date and marking as inactive."""
        self.return_date = datetime.now()
        self.is_active = False
    
    def __repr__(self):
        """Return string representation of the loan."""
        status = "Active" if self.is_active else "Closed"
        return f"{self.loan_id} - {self.member.name} borrowed {self.book.title} [{status}]"
