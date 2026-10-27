from classes.Book import Book

class Encyclopedia(Book):
   def __init__(self, title="Unknown", author="Unknown", publisher="BGSU", publication_date="2000/01/01", edition="1st", pages=0):
      Book.__init__(self, title, author, publisher, publication_date)
      self.edition = edition
      self.pages = pages

   def print_info(self):
      Book.print_info(self)
      print(f"Edition: {self.edition}")
      print(f"Number of Pages: {self.pages}")