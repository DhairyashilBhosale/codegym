import csv

class BookLibraryInfo():

	def __init__(self, csv_file_path):
		self.csv_file_path = csv_file_path
		self.book_info = dict()
		
	def _parse_csv(self):
		'''
		parse_csv file and update book_info dict
		'''
		with open(self.csv_file_path) as csv_file:
			_book_info = csv.reader(csv_file, delimiter=',')
			next(_book_info, None)
			for _row in _book_info:
				self.book_info[_row[0]] = {'author': _row[1], 'catogory' : _row[2:]}
			
	def get_info(self):
		'''
		return book info
		'''
		_book_cat = dict()
		self._parse_csv()
		#iterate over book_info
		for book_id, data in self.book_info.items():
			for cat in data['catogory']:
				if cat not in _book_cat:
					_book_cat[cat] = 1
				else:
					_book_cat[cat] += 1
					
		self.book_info.update(_book_cat)
		print("Adult Book Count: ",self.book_info['adult'])
		print("Teen Book Count: ",self.book_info['teen'])
		print("kid(10+) Book Count: ",self.book_info['kid(10+)'])
		print("kid(3-5) Book Count: ",self.book_info['kid(3-5)'])
		
if __name__ == "__main__":

	book_library = BookLibraryInfo('input.csv')
	book_library.get_info()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
