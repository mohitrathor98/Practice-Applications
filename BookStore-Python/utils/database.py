'''
	Concerned with storing and retrieving books to and from database

	After fetching from database, data are in list of tuple format
	e.g: [(a,b,c), (d,e,f)]

'''
from .database_connection import DatabaseConnection

books = []

def create_book_table():
	
	try:
	
		with DatabaseConnection('bookdata.db') as connection:
			cursor = connection.cursor()
			cursor.execute('CREATE TABLE IF NOT EXISTS books( \
				book text primary key, 			\
				author text,					\
				read integer					\
			);')
		
	except:
		raise


def add_book(name, author):

	try:
		with DatabaseConnection('bookdata.db') as connection:
			cursor = connection.cursor()
			cursor.execute('INSERT INTO books VALUES (?, ?, 0)', (name, author))
	
	except:
		raise


def get_book_list():
    
	try:
		with DatabaseConnection('bookdata.db') as connection:
			cursor = connection.cursor()
			cursor.execute('SELECT * FROM books')
			books = cursor.fetchall()
	except:
		raise

	return books


def search_book( book_name:str ):
	try:
		with DatabaseConnection('bookdata.db') as connection:
			cursor = connection.cursor()
			cursor.execute('SELECT * FROM books')
			books = cursor.fetchall()

		for book in books:
			if book[0] == book_name:
				return True
		return False
	
	except:
		raise

	return books

def mark_book_as_read(book_name: str):

	try:
		with DatabaseConnection('bookdata.db') as connection:
			cursor = connection.cursor()
			cursor.execute('UPDATE books SET read = 1 WHERE book == ?', (book_name, ))

	except:
		raise


def remove_book(book_name: str):
    
	try:
		with DatabaseConnection('bookdata.db') as connection:
			cursor = connection.cursor()
			cursor.execute('DELETE FROM books WHERE book == ?', (book_name, ))
		
	except:
		raise
