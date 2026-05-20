# Library Management System

A comprehensive Python-based library management system that allows users to manage books, members, and borrowing transactions.

## Features

### 1. **Add Book** (Feature 1)
Add new books to the library collection with the following details:
- Book ID (unique identifier)
- Title
- Author
- Initial availability status (set to `True` by default)

### 2. **Register Member** (Feature 2)
Register new members in the library system with:
- Member ID (unique identifier)
- Full Name
- Email Address

### 3. **Borrow Book** (Feature 3)
Manage book borrowing with comprehensive error handling:
- Input: Book ID and Member ID
- Validates that both book and member exist
- Checks if the book is available
- Creates a loan record with auto-generated Loan ID (format: L001, L002, etc.)
- Updates book availability status
- Raises exceptions for:
  - `BookNotFoundError`: Book doesn't exist
  - `MemberNotFoundError`: Member doesn't exist
  - `BookUnavailableError`: Book is already borrowed

### 4. **Return Book** (Feature 4)
Process book returns:
- Input: Loan ID
- Validates loan exists
- Marks book as available
- Closes the loan record with return date
- Raises `LoanNotFoundError` if loan doesn't exist

### 5. **View Books** (Feature 5)
Display all books with status:
- Lists all books in the library
- Shows availability status (Available/Borrowed)
- Displays: Book ID, Title, Author, Status
- Shows "No books found" if library is empty

### 6. **View Members** (Feature 6)
Display all registered members:
- Lists all library members
- Shows: Member ID, Name, Email
- Shows "No members found" if no members registered

### 7. **View Loans** (Feature 7)
Display all loan transactions:
- Lists all active and closed loans
- Shows loan status (Active/Closed)
- Displays: Loan ID, Member Name, Book Title, Status
- Shows "No loans found" if no loans exist

### 8. **Exit** (Feature 8)
Gracefully exit the program:
- Displays closing message
- Breaks out of the main loop
- Terminates program execution

## Project Structure

```
Library-Management-System/
├── book.py              # Book class definition
├── member.py            # Member class definition
├── loan.py              # Loan class definition
├── exceptions.py        # Custom exception classes
├── library_service.py   # Core service for library operations
├── main.py              # Main program with CLI interface
├── requirements.txt     # Project dependencies
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Class Hierarchy

### Book
- `book_id`: str
- `title`: str
- `author`: str
- `available`: bool
- Methods: `borrow()`, `return_book()`

### Member
- `member_id`: str
- `name`: str
- `email`: str

### Loan
- `loan_id`: str
- `book`: Book object
- `member`: Member object
- `loan_date`: datetime
- `return_date`: datetime (None if active)
- `is_active`: bool
- Methods: `close_loan()`

### LibraryService
Core service managing:
- `add_book(book_id, title, author)` → Book
- `view_books()` → List[Book]
- `register_member(member_id, name, email)` → Member
- `view_members()` → List[Member]
- `borrow_book(book_id, member_id)` → Loan
- `return_book(loan_id)` → Loan
- `view_loans()` → List[Loan]

## Exception Handling

Custom exceptions for robust error management:
- `LibraryException`: Base exception class
- `BookNotFoundError`: Book not found in library
- `MemberNotFoundError`: Member not found
- `BookUnavailableError`: Book already borrowed
- `LoanNotFoundError`: Loan record not found

## How to Use

### Prerequisites
- Python 3.7 or higher
- No external dependencies required

### Running the Program

```bash
python main.py
```

### Example Workflow

1. **Start the program**
   ```
   python main.py
   ```

2. **Add a book** (Choose option 1)
   ```
   Enter Book ID: B001
   Enter Book Title: Python Programming
   Enter Book Author: Guido van Rossum
   ```

3. **Register a member** (Choose option 2)
   ```
   Enter Member ID: M001
   Enter Member Name: John Doe
   Enter Member Email: john@example.com
   ```

4. **Borrow a book** (Choose option 3)
   ```
   Enter Book ID: B001
   Enter Member ID: M001
   Output: John Doe borrowed Python Programming
   ```

5. **View books** (Choose option 5)
   ```
   Books:
     B001 - Python Programming by Guido van Rossum [Borrowed]
   ```

6. **View loans** (Choose option 7)
   ```
   Loans:
     L001 - John Doe borrowed Python Programming [Active]
   ```

7. **Return a book** (Choose option 4)
   ```
   Enter Loan ID: L001
   Output: John Doe returned Python Programming
   ```

8. **Exit** (Choose option 8)
   ```
   Program closed.
   ```

## Data Flow

### Add Book Flow
```
User Input (Book ID, Title, Author)
    ↓
Validation
    ↓
Create Book Object
    ↓
Store in _books dictionary
    ↓
Confirmation Message
```

### Borrow Book Flow
```
User Input (Book ID, Member ID)
    ↓
Validate Book Exists → BookNotFoundError
    ↓
Validate Member Exists → MemberNotFoundError
    ↓
Validate Book Available → BookUnavailableError
    ↓
Generate Loan ID
    ↓
Mark Book as Borrowed
    ↓
Create Loan Record
    ↓
Confirmation Message
```

## Error Handling

The system implements comprehensive error handling:
- Input validation for all user inputs
- Custom exceptions for business logic errors
- Try-catch blocks in CLI layer
- User-friendly error messages

## Testing

You can test the system with various scenarios:

1. **Valid operations**: Add books, register members, borrow/return books
2. **Error cases**:
   - Try to borrow non-existent book
   - Try to borrow for non-existent member
   - Try to borrow already borrowed book
   - Try to return with invalid loan ID
3. **Edge cases**:
   - Empty inputs
   - Duplicate IDs
   - Multiple operations

## Future Enhancements

- Database integration (SQLite/PostgreSQL)
- User authentication
- Fine calculation for overdue books
- Book reservation system
- Member fine tracking
- Export/Import functionality
- GUI interface
- REST API endpoints

## License

MIT License - Feel free to use, modify, and distribute.

## Author

Library Management System - Educational Project
