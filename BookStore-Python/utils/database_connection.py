import sqlite3

class DatabaseConnection:

	def __init__(self, host):
		self.connection = None
		self.host = host
	
	# enter and exit dunder method are used
	# context manager and is executed when we enter
	# and exit a context(with DatabaseConnection('') as 
	# connection)
	def __enter__(self):
		self.connection = sqlite3.connect(self.host)
		return self.connection

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.connection.commit()
		self.connection.close()
