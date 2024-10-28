import sys

def convertMorseCode(text: str) -> str:
    """
    convertMorseCode
    """
    convert = ""
    morse = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        " ": "/ ",
    }
    text = text.upper()
    for char in text:
        convert += morse[char]
        convert += " "
    return convert


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        for char in str(sys.argv[1]):
            if not (char.isalpha() or char.isdigit() or char.isspace()):
                raise AssertionError("the arguments are bad")
        print(convertMorseCode(sys.argv[1]))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
