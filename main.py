from Book import Book
from Encyclopedia import Encyclopedia

continue_input = "Y"

def main():
    continue_input = "Y"

    while continue_input.lower() == "y":
        print("\nSelect a book type:")
        print("1. Regular Book")
        print("2. Encyclopedia")

        choice = input("Enter your choice: ")

        if choice != "1" and choice != "2":
            print("Invalid choice. Please select 1 or 2.")
            continue

        title = input("Enter the title: ")
        author = input("Enter the author: ")
        publisher = input("Enter the publisher: ")
        publication_date = input("Enter the publication date: ")

        if choice == "1":
            book = Book(title, author, publisher, publication_date)

        else:
            edition = input("Enter the edition: ")

            while True:
                try:
                    num_pages = int(input("Enter the number of pages: "))
                    if num_pages > 0:
                        break
                    print("Number of pages must be positive.")
                except ValueError:
                    print("Please enter a valid whole number.")

            book = Encyclopedia(
                title, author, publisher, publication_date, edition, num_pages
            )
        print()
        book.print_info()

        continue_input = input("\nWould you like to enter another book? (Y/y to continue): ")

    print("Goodbye!")

if __name__ == "__main__":
   main()