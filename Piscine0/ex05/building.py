import sys
import string

def count_characters(text: str) -> None:
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    digit_count = sum(1 for char in text if char.isdigit())
    space_count = sum(1 for char in text if char.isspace())
    punctuation_count = sum(1 for char in text if char in string.punctuation)

    print(f"The text contains {len(text)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")

def main():
    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        raise AssertionError("more than one argument is provided")

    count_characters(text)

if __name__ == "__main__":
    main()
