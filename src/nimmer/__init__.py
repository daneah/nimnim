import sys


STOP_WORDS = {
    "of",
    "the",
    "and",
}


def nim(sentence: str) -> str:
    # split sentence by spaces
    words = sentence.split(" ")

    # removing stop words
    words_for_acronym = [word for word in words if word and word not in STOP_WORDS]

    # first letter of each word
    letters = [word[0] for word in words_for_acronym]

    # capitalize each letter
    return "".join(letter.upper() for letter in letters)


if __name__ == "__main__":
    sentence = sys.argv[1]
    print(nim(sentence))
