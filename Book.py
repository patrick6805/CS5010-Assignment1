class Book:
   def __init__(self, title, author, publisher, publication_date):
      self.title = title
      self.author = author
      self.publisher = publisher
      self.publication_date = publication_date

   def print_info(self):
      print("Book Information:")
      print(f"Book Title: {self.title}")
      print(f"Author: {self.author}")
      print(f"Publisher: {self.publisher}")
      print(f"Publication Date: {self.publication_date}")