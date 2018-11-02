# User Class Start
class User(object):
    # Constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}   
    # Get email function
    def get_email(self):
        return self.email
    # Change email function
    def change_email(self, address):
        print("The email have been updated from {old} to {new}". format(old = self.email, new = address))
        self.email = address 
    # Represent string
    def __repr__(self):
        return "User {name}, email: {email}, books read: {count}".format(name = self.name, email = self.email, count = len(self.books))
    # Equals function    
    def __eq__(self, other_user):
        if self.name == other_user.name:
            if self.email == other_user.email:
                return True
        return False
    # Read book function
    def read_book(self, book, rating = None):
        self.books[book.title] = rating
    # Get average rating function
    def get_average_rating(self):
        average = 0
        count = 0
        for book in self.books:
            if self.books[book] != None:
                average += self.books[book]
                count += 1
            if average != 0:
                average = average / count
        return average
# User Class End
    
# Book Class Start
class Book(object):
    # Constructor
    def __init__(self, title, isbn):
        if type(title) is str:
            self.title = title
        else:
            print("Title can only be of type String.")
        if type(isbn) is int:
            self.isbn = isbn
        else:
            print("ISBN can only be of type Int.")
        self.ratings = []
     # Hash
    def __hash__(self):
        return hash((self.title, self.isbn))   
    # Equals function
    def __eq__(self, other_book):
        print("Checking")
        if self.title == other_book.title:
            if self.isbn == other_book.isbn:
                return True  
        return False
    # repersent
    def __repr__(self):
        return "Title: {title} ISBN: {isbn}".format(title = self.title, isbn = self.isbn)
    # Get title function
    def get_title(self):
        return self.title   
    # Get ISBN Function
    def get_isbn(self):
        return self.isbn
    # Set ISBN function
    def set_isbn(self, new_isbn):
        if type(new_isbn) == int:
            print("ISBN has been updated from {old} to {new}".format(old = self.isbn, new = new_isbn))
            self.isbn = new_isbn
        else:
            print("ISBN did not update because ISBN can only be of type Int.")
    # Add rating function
    def add_rating(self, rating):
        if rating != None:
            if 0 <= rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")
    # Get average rating
    def get_average_rating(self):
        average = 0
        count = 0
        if len(self.ratings) > 0:
            for rating in self.ratings:
                average += rating
                count += 1
            average = average / count
        return average
# Book Class End    

# Fiction SubClass Start
class Fiction(Book):
    # Constructor
    def __init__(self, title, author, isbn):
        # Calling Parent Class
        super().__init__(title, isbn) 
        self.author = author
    # Represent function
    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)
    # Get author function
    def get_author(self):
        return self.author
# Fiction SubClass End

# Non Fiction SubClass Start
class Non_Fiction(Book):
    # Constructor
    def __init__(self, title, subject, level, isbn):
        # Calling Parent Class
        super().__init__(title, isbn) 
        self.subject = subject
        self.level = level
    # Represent function
    def __repr__(self):
        return "{title}, a {level} manual on {subject}". format(title = self.title, level = self.level, subject = self.subject)
    # Get subject function
    def get_subject(self):
        return self.subject
    # Get level function
    def get_level(self):
        return self.level
# Non Fiction SubClass End

# TomeRater class Start
class TomeRater(object):
    # Constructor
    def __init__(self):
        self.users = {}
        self.books = {}
    # create book
    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book
    # create novel
    def create_novel(self, author, title, isbn):
        new_novel = Fiction(title, author, isbn)
        return new_novel
    # create non fiction
    def create_non_fiction(self, title, subject, level, isbn):
        non_fic = Non_Fiction(title, subject, level, isbn)
        return non_fic
    # Add User
    def add_user(self, name, email, user_books = None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book,email)
    # book to user
    def add_book_to_user(self, book, email, rating = None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book]+= 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {email}!".format(email = email))
    # Print catalog
    def print_catalog(self):
        print("Catalog:")
        for books in self.books:
            print(books)
    # Print Users
    def print_users(self):
        print("Users:")
        for users in self.users.values():
            print(users)
    # Most read book
    def most_read_book(self):
        most_read_count = 0
        most_read = None
        for book in self.books:
            if self.books[book] > most_read_count:
                most_read_count = self.books[book]
                most_read =book
        return most_read
    # Highest rated book
    def highest_rated_book(self):
        highest_rating = 0
        high_rated_book = None
        for book in self.books:
            if book.get_average_rating() > highest_rating:
                highest_rating = book.get_average_rating()
                high_rated_book = book
        return high_rated_book
    # Most positive User
    def most_positive_user(self):
        most_positive = 0
        positive_user = None
        for user in self.users.values():
            if user.get_average_rating() > most_positive:
                most_positive = user.get_average_rating()
                positive_user = user
        return positive_user
# TomeRater class End
