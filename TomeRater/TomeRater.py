class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("This users email has been updated")

    def __repr__(self):
        return "This users name is: {name}. \n This users email is: {email}. \n This user read this many books: {books} \n" .format(name=self.name, email = self.email, books=len(self.books))

    def __eq__(self, other_user):
        x = [self.name, self.email]
        if x == other_user:
            return "this user has the same name and email as someone in the database"

    def read_book(self, book, rating=None):
        self.books.update({book: rating})

    def get_average_rating(self):
        x = sum(self.books.values())
        z = len(self.books.values())
        return x/z


class Book(object):
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.ratings = []

    def __repr__(self):
        return "{book} with isbn {isbn}. \n".format(book=self.title, isbn=self.isbn)

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def get_price(self):
        return self.price

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("this isbn has been updated \n")

    def add_rating(self, rating):
        try:
            if rating <= 4 and rating >0:
                self.ratings += rating
                return None
            else:
                return "Invalid Rating"
        except TypeError:
            return "Invalid Rating"

    def __eq__(self, other_book):
        if Book.price == other_book.price and Book.title == other_book.title and Book.isbn == other_book.isbn:
            return other_book

    def get_average_rating(self):
        x = sum(self.ratings)
        z = len(self.ratings)
        return x/z

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn, price):
        Book.__init__(self, title, isbn, price)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author} with isbn {isbn}. \n".format(title=self.title, author=self.author, isbn=self.isbn)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn, price):
        Book.__init__(self, title, isbn, price)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a	{level}	manual on {subject} with isbn {isbn}. \n".format(title=self.title, level=self.level, subject=self.subject, isbn=self.isbn)


class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn, price):
        return Book(title, isbn, price)

    def create_novel(self, title, author, isbn, price):
        return Fiction(title, author, isbn, price)

    def create_non_fiction(self, title, subject, level, isbn, price):
        return Non_Fiction(title, subject, level, isbn, price)

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            book.add_rating(rating)
            self.books[book] = self.books.get(book, 0) + 1

    def add_user(self, name, email, books=None):
        if email not in self.users and email:
            self.users[email] = User(name, email)
            if books is not None:
                for book in books:
                    self.add_book_to_user(book, email)
        else:
            print("This user already exists.")

    def print_catalog(self):
        print(self.books.keys())

    def print_users(self):
        print(self.users.values())

    def most_read_book(self):
        return max(self.books, key=self.books.get)

    def highest_rated_book(self):
        bestrating = 0
        bestbook = None
        for x in self.books.keys():
            if User.get_average_rating(self) > bestrating:
                bestrating = User.get_average_rating(self)
                bestbook = x
        return str(bestbook)

    def most_positive_user(self):
        bestuser = None
        bestrating = 0
        for x in self.users.values():
            if User.get_average_rating(self) > bestrating:
                bestrating = User.get_average_rating(self)
                bestuser = x
        return str(bestuser)

    def get_n_most_expensive_books(self, n):
        book_prices = []
        for book in self.books.keys():
            book_prices.append((book.title, book.price))
        book_prices.sort(reverse=True)
        if n > len(self.books.values()):
            return "there are not this many books in the library"
        else:
            return book_prices[0:n]

    def get_worth_of_user(self, user_email):
        user_books = self.users[user_email].books
        sum = 0
        for book in user_books:
            sum += book.price
        return "this user read {n} dollars worth of books".format(n=sum)















