# Book and Encyclopedia Program

## Overview

This project is an interactive Python command-line application for creating and displaying information about books and encyclopedias. It demonstrates object-oriented programming, inheritance, method overriding, input validation, exception handling, and regular expressions.

## Features

- Create a standard book or an encyclopedia.
- Reuse common book attributes through inheritance.
- Override `print_info()` in the `Encyclopedia` class to display additional details.
- Validate titles, authors, publishers, publication dates, editions, and page counts.
- Use regular expressions to check date and edition formats.
- Handle invalid input and common input interruptions.
- Allow users to enter multiple records during one run.

## Project Structure

```text
Book-Encyclopedia/
├── main.py
|-- classes
      |-- Book.py
      ├── Encyclopedia.py
|-- tests
      |-- test_parsing.py
      ├── parsing_test_cases.csv
└── README.md
```

| File | Purpose |
|---|---|
| `main.py` | Runs the interactive menu, collects input, and validates user entries. |
| `Book.py` | Defines the base `Book` class and its common attributes and display method. |
| `Encyclopedia.py` | Defines `Encyclopedia`, a subclass of `Book` with edition and page-count attributes. |
| `README.md` | Describes the project and explains how to run it. |

## Requirements

- Python 3.10 or later is recommended.
- No third-party packages are required; the program uses Python's standard library.

## Running the Program

1. Open a terminal in the project directory.
2. Run:

   ```bash
   python main.py
   ```

   Depending on your installation, you may need to use `python3 main.py` or `py main.py`.

3. Follow the menu prompts to choose a book type and enter its information.
4. When asked, choose whether to create another entry.

## Class Design

### `Book`

`Book` is the parent class. It stores the attributes shared by books and encyclopedias:

- `title`
- `author`
- `publisher`
- `publication_date`

Its `print_info()` method displays these common details.

### `Encyclopedia`

`Encyclopedia` inherits from `Book` and adds:

- `edition` — a string such as `"1st"` or `"2nd"`.
- `pages` — an integer representing the number of pages.

It overrides `print_info()`: the method first displays the common information using the parent class method, then displays the edition and page count.

This demonstrates **inheritance** and **method overriding**.

## Input Validation

The program checks user input before constructing the objects. The expected rules include:

| Field | Validation |
|---|---|
| Title | Must not be empty and must be no longer than 100 characters. |
| Author | Must not be empty, must contain at least one letter, and may contain letters, spaces, apostrophes, periods, and hyphens; maximum 100 characters. |
| Publisher | Must not be empty and must be no longer than 100 characters. |
| Publication date | Accepts `YYYY-MM-DD` or `YYYY/MM/DD`, and checks that the date exists on the calendar. |
| Edition | Requires a number from 1 to 9999 followed by the correct ordinal suffix (`st`, `nd`, `rd`, or `th`). |
| Page count | Must be an integer from 1 to 100,000. |
| Menu choice | Must match one of the available choices. |
| Continue choice | Must be `Y` or `N`. |

Invalid entries should prompt the user to try again instead of creating an object with invalid data.

## Regular Expressions (Regex)

Regular expressions are patterns used to match text. The program uses Python's built-in `re` module.

### Publication date pattern

```python
re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_text)
```

- `\d` matches a digit.
- `{4}` requires four digits for the year.
- `-` matches a literal hyphen.
- `{2}` requires two digits for the month and day.
- `re.fullmatch()` requires the entire input to match the pattern.

The program normalizes slash-separated dates by replacing `/` with `-` before checking the pattern. It then uses `datetime.strptime()` to verify that the date is a real calendar date. For example, `2024-02-29` is valid, while `2023-02-29` is not.

### Edition pattern

```python
re.fullmatch(
    r"[1-9]\d{0,3}(st|nd|rd|th)",
    edition,
    re.IGNORECASE
)
```

- `[1-9]` requires the first digit to be from 1 through 9.
- `\d{0,3}` allows up to three additional digits.
- `(st|nd|rd|th)` matches one of the four ordinal suffixes.
- `re.IGNORECASE` allows uppercase or lowercase suffix letters.
- `re.fullmatch()` prevents extra characters before or after the edition.

This pattern checks the general structure, but it does not by itself guarantee that the suffix matches the number. The program applies additional logic for that rule. For example, `21st` is valid, but `21th` is not. Numbers ending in 11, 12, or 13 use `th`, as in `11th`, `12th`, and `13th`.

## Error Handling

The program uses validation loops and exception handling to make input more robust.

- Invalid values are rejected and the user is asked to try again.
- `ValueError` is handled when a date cannot be parsed or a numeric value is invalid.
- Page counts are checked for integer format and permitted range.
- `KeyboardInterrupt` and `EOFError` are handled at the top level so the program can exit more gracefully when input is interrupted.

## Concepts Demonstrated

- Classes and objects
- Constructors and instance attributes
- Inheritance
- Method overriding
- Loops and conditional statements
- User input and output
- String processing and regular expressions
- Date parsing with `datetime`
- Exception handling
- Organizing a Python project across multiple modules

## Possible Future Improvements

- Add automated unit tests for the input-validation functions.
- Save entries to a file or database.
- Allow users to search, edit, and delete saved entries.
- Support additional publication-date formats.
- Add more book subclasses with their own specialized attributes.
