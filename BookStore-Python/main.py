from utils import database

USER_CHOICE = '''
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: '''

def add_book():
	
	book_name = input("Book Name: ")
	author_name = input("Author name: ")
	database.add_book(book_name, author_name)

def list_books():

	book_list = database.get_book_list()
	for book in book_list:
		print(f"{book[0]} by {book[1]}\tRead Status:", end=' ')

		if book[2] == 0:
			print("False")
		else:
			print("True")

def read_book():

	book_name = input("Book to read: ")
	check_availability = database.search_book(book_name)
	if check_availability:
		database.mark_book_as_read(book_name)
	else:
		print(f"{book_name} not found")

def delete_book():

	book_name = input("Book to delete: ")
	check_availability = database.search_book(book_name)
	if check_availability:
		database.remove_book(book_name)
	else:
		print(f"{book_name} is not found")

def menu():

	database.create_book_table()
	user_input = ''
	
	while user_input != 'q':
		user_input = input(USER_CHOICE)
		if user_input == 'a':
			add_book()
			
		elif user_input == 'l':
			list_books()
			
		elif user_input == 'r':
			read_book()
		
		elif user_input == 'd':
			delete_book()


if __name__ == '__main__':
	menu()
