from models.book import *

book_1= Book("Where the Crawdads Sing", "Delia Owens", "Coming-of-age murder mysetery", False)
book_2= Book("The Lost Lights of St Kilda", "Elizabeth Gifford", "Love story", False)
book_3= Book(" The Shadow of the Wind", "Carlos Ruiz Zafon", "Thriller", False)
book_4= Book("Kafka on the Shore", "Haruki Murakami", "Magical realism", False)
book_5= Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez", "Magical Realism", False)
book_6= Book("Snow Falling on Cedars", "David Gutterson", "Mystery historical drama", False)

books = [book_1, book_2, book_3, book_4, book_5, book_6]

def add_new_book(book):
    books.append(book)

def delete_book_index(index):
    books.pop(index)