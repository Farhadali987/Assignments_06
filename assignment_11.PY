class Book:
    
    total_books = 0

    def __init__(self,title,author):
        self.title = title
        self.author = author

        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):

         cls.total_books += 1

b1 = Book("English","William Shakespeare")
b2 = Book("Math","Archimedes ")
print('total counts',Book.total_books)
