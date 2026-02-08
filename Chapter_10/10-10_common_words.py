from pathlib import Path


def count_common_word_in_file(path, target_word="the"):
    """Print the total word count and how often target_word appears in one file.

    path can be either a Path object or a filename string.
    """
    # Make sure we are working with a Path object so we can call read_text().
    path = Path(path)

    try:
        # Read the entire contents of the text file into a single string.
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        # If the file is missing, print a friendly message and stop.
        print(f"Sorry, the file {path} does not exist.")
        return

    # Split the text into a list of individual words.
    words = contents.split()

    # Get the total number of words in the file.
    total_words = len(words)

    # Count how many times the target word appears, ignoring capitalization.
    target_lower = target_word.lower()
    target_count = sum(1 for word in words if word.lower() == target_lower)

    # Display a short summary for this file.
    print(f"\nFile: {path}")
    print(f"  Total words: {total_words}")
    print(f"  '{target_word}' appears about {target_count} times.")


def main():
    """Count a common word in several book files in this folder."""
    # List of files we want to analyze for the common word.
    filenames = [
        "alice.txt",
        "little_women.txt",
        "moby_dick.txt",
        "the_new_hackers_dictionary.txt",
    ]

    # The word we consider "common" for this exercise.
    target_word = "the"

    print(f"Counting occurrences of '{target_word}' in multiple files:\n")
    for name in filenames:
        count_common_word_in_file(name, target_word)


if __name__ == "__main__":
    main()