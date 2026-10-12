from classes.Book import Book

class Encyclopedia(Book):
   def __init__(self, title, author, publisher, publication_date, edition, pages):
      Book.__init__(self, title, author, publisher, publication_date)
      self.edition = edition
      self.pages = pages

   def print_info(self):
      Book.print_info(self)
      print(f"Edition: {self.edition}")
      print(f"Number of Pages: {self.pages}")