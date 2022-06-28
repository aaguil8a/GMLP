import json          # attribute getter, item getter
from operator import attrgetter, itemgetter
from copy import copy
from functions import reduce

from numpy import sort # functions that you give it an object and you give it a key or an attribute name.
                                            # and then you say, hey get me this thing this other thing and it does that for you.


class Book:
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return str(self)
    
    
def get_books(filename, raw=False):
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data['books']
        return [Book(**book) for book in data['books']]






## lambda ###
           # automatically return the last value that they calculate
                      #argu      #return
total = reduce(lambda x, y: x + y, [b.price for b in BOOKS])
long_books = filter(lambda book: book.number_of_pages >=600, BOOKS)
good_deals = filter(lambda book: book.price <= 6, BOOKS)






############### REDUCE #####################

# def product(x,y):
#     return x * y


# def product(x,y):
#         return x * y

# print(reduce(product, [1,2,3,4,5]))


# def add_book_prices(book1, book2):
#     return book1 + book2

# total = reduce(add_book_prices, [b.price for b in BOOKS])



# def factorial(n):
#     if n == 1:
#         return 1
    
#     else:
#         return n * factorial(n-1)

# print(factorial(5))
    
# BOOKS = get_books('books.json')
# # it is bunch of dictionaries
# # how to sort it, itemgetter
# RAW_BOOKS = get_books('books.json', raw=True)



# # pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))

# # pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages')) # can use reverse=True

# # sorted()

# # print(pages_sort [0].number_of_pages, pages_sort [-1].number_of_pages)

# # print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])


# important_list = [5,3,1,2,4]
# # important_list.sort() # bad idea, sorts list in place
# # sorted(important_list) # Sorts a copy of the list

# # what sorted does is it returns you a sorted copy of the list.
# # sorted does not sort the original list

# # Sorted takes the original list, makes a copy,
# # sorts that copy, sends you back that copy.


# # So what do we do if we want important_list
# # to be sorted for something, right.


# # what if I want to sort something that isn't just the natural state of the list, right?
# # how to sort different things?


# def sales_price(book):
#     """ Apply a 20% discount to the book's price"""
#     book = copy(book)
#     book.price = round(book.price - book.price*.2, 2)
#     return book

# # this is map function 
# # sales_price = list(map(sales_price, BOOKS))
# # # list compreh      
# # sales_books = [sales_price(book) for book in BOOKS]

# # the above code do the same thing.

# # print(BOOKS[0].price)
# # print(sales_price[0].price)


# # sales_books = [sales_price(book) for book in BOOKS]


# # Filter ##

# # def is_long_book(book):
# #     """Does a book have 600+ pages?"""
# #     return book.number_of_pages >= 600


# # long_books = list(filter(is_long_book, BOOKS))

# # long_books = [book for book in BOOKS if book.number_of_pages >= 600]
# # print(len(BOOKS))
# # print(len(long_books))

# #### chianing ### 
# def has_roland(book):
#     return any(['Roland' in subject for subject in book.subjects])





# def titlecase(book):
#     book = copy(book)
#     book.title = book.title.title()
#     return book

# # print(list(map(titlecase, filter(has_roland, BOOKS))))

# def is_good_deal(book):
#     return book.price <= 5

# cheap_books = sorted(     
#                             # turn all books into 20 percet, then we fillter using is_good_deal
#     filter(is_good_deal, map(sales_price, BOOKS)),
#     # then we sorted all of them by whatever that new updated cheap price was
#     key=attrgetter('price')

# )

# print(cheap_books[0].price)






