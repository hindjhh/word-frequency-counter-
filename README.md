# Word Frequency Counter

A beginner Python project that analyzes a sentence or paragraph, counts how many times each word appears, identifies the most frequent word, and allows users to search for a specific word.

## Features

- **Word Frequency:** Count and display the frequency of each unique word.
- **Most Frequent Word:** Identify the word or words that appear most frequently.
- **Search a Word:** Search for a specific word and display its frequency.
- **Text Cleaning:** Convert words to lowercase and remove punctuation.
- **Input Validation:** Handle empty paragraphs, invalid text, and invalid menu choices.
- **Interactive Menu:** Navigate through the available features using a simple console menu.

## Technologies Used

- Python 3
- Built-in Python functions and data structures:
  - Lists
  - Dictionaries
  - Loops and conditional statements
  - Functions
  - String methods

## Getting Started

### Prerequisites

Make sure Python 3 is installed on your computer.

Check your Python installation by running:

```bash
python3 --version
```

### Installation

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd python-word-frequency-counter
   ```

3. Run the program:

   ```bash
   python3 main.py
   ```

   Replace `main.py` with the actual name of your Python file if it is different.

## How to Use

1. Run the program.
2. Enter a sentence or paragraph when prompted.
3. Select an option from the menu:

   - `1` — Display the frequency of each word.
   - `2` — Display the most frequent word or words.
   - `3` — Search for the frequency of a specific word.
   - `4` — Exit the program.

4. Follow the prompts to interact with the application.

## Example

**Input paragraph:**

```text
Python is fun and Python is powerful
```

**Example word frequency output:**

```text
python:2
is:2
fun:1
and:1
powerful:1
```

**Most frequent words:**

```text
python:2
is:2
```

## What I Learned

Through this project, I practiced:

- Breaking a program into reusable functions.
- Processing and cleaning text.
- Counting occurrences using dictionaries.
- Validating user input.
- Using loops to manage an interactive menu.
- Handling empty or invalid input.
- Testing program behavior with different inputs.

## Future Improvements

- Support more advanced punctuation and word-cleaning rules.
- Sort word frequencies from highest to lowest.
- Display the results in a more organized format.
- Add automated unit tests.
- Allow users to analyze text files.

## Author

Created as my first Python project while developing my programming skills.

---

*This project is part of my journey toward becoming an intermediate Python programmer.*