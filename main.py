from classes.Book import Book
from classes.Encyclopedia import Encyclopedia
from datetime import datetime
import re

def read_book_type():
    while True:
        print("\nSelect a book type:")
        print("1. Regular Book")
        print("2. Encyclopedia")

        choice = input("Enter your choice: ").strip()

        if choice in ("1", "2"):
            return choice

        print("Invalid choice. Please select 1 or 2.")


def read_title():
    while True:
        title = input("Enter the title: ").strip()

        if not title: 
            print("Title cannot be empty.")
            continue
            
        if len(title) > 100:
            print("Title cannot exceed 100 characters.")
            continue

        return title


def read_author():
    while True:
        author = input("Enter the author: ").strip()

        if not author:
            print("Author cannot be empty.")
            continue

        if not any(char.isalpha() for char in author):
            print("Author must contain at least one letter.")
            continue

        if not all(
            char.isalpha() or char.isspace()
            or char in "'’.-"
            for char in author
        ):
            print("Author contains invalid characters.")
            continue

        if len(author) > 100:
            print("Author cannot exceed 100 characters.")
            continue

        return author


def read_publisher():
    while True:
        publisher = input("Enter the publisher: ").strip()

        if not publisher: 
            print("Publisher cannot be empty.")
            continue

        if len(publisher) > 100:
            print("Publisher cannot exceed 100 characters.")
            continue

        return publisher
                    
def read_publication_date():
    while True:
        date_text = input(
            "Enter the publication date (YYYY-MM-DD or YYYY/MM/DD): "
        ).strip()

        # Normalize slashes to hyphens
        date_text = date_text.replace("/", "-")

        # Step 1: Check the format
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_text):
            print("Invalid date format. Use YYYY-MM-DD or YYYY/MM/DD.")
            continue

        # Step 2: Check whether the date exists
        try:
            publication_date = datetime.strptime(
                date_text, "%Y-%m-%d"
            ).date()

            return publication_date.isoformat()

        except ValueError:
            print("Invalid calendar date. Please enter a real date.")


def read_edition():
    while True:
        edition = input("Enter the edition (e.g., 1st, 2nd, 3rd): ").strip()

        # Check that the input contains digits followed by an ordinal suffix
        if not re.fullmatch(r"[1-9]\d{0,3}(st|nd|rd|th)", edition, re.IGNORECASE):
            print("Invalid edition format. Enter an edition from 1st to 9999th.")
            continue

        # Extract the number
        number = int(re.match(r"\d+", edition).group())

        # Determine the correct suffix
        if 11 <= number % 100 <= 13:
            expected_suffix = "th"
        elif number % 10 == 1:
            expected_suffix = "st"
        elif number % 10 == 2:
            expected_suffix = "nd"
        elif number % 10 == 3:
            expected_suffix = "rd"
        else:
            expected_suffix = "th"

        # Validate the suffix
        if edition.lower().endswith(expected_suffix):
            return edition.lower()

        print(f"Invalid suffix. Edition #{number} should end in '{expected_suffix}'.")


def read_num_pages():
    while True:
        try:
            num_pages = int(input("Enter the number of pages: "))

            if num_pages <= 0:
                print("Number of pages must be positive.")
                continue

            if num_pages > 100000:
                print("Number of pages cannot exceed 100,000.")
                continue

            return num_pages

        except ValueError:
            print("Please enter a valid whole number.")


def read_continue_choice():
    while True:
        choice = input(
            "\nWould you like to enter another book? (Y/N): "
        ).strip().lower()

        if choice in ("y", "n"):
            return choice

        print("Invalid response. Please enter Y or N.")


def main():
    continue_input = "y"

    while continue_input == "y":
        choice = read_book_type()

        title = read_title()
        author = read_author()
        publisher = read_publisher()
        publication_date = read_publication_date()

        if choice == "1":
            book = Book(
                title, author, publisher, publication_date
            )

        else:
            edition = read_edition()
            num_pages = read_num_pages()

            book = Encyclopedia(
                title,
                author,
                publisher,
                publication_date,
                edition,
                num_pages
            )

        print()
        book.print_info()

        continue_input = read_continue_choice()

    print("Goodbye!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")
    except EOFError:
        print("\nNo more input available. Goodbye!")