# String formatting utilities


def shout(text):
    """Return the text uppercased with an exclamation mark."""
    return text.upper() + "!"


def whisper(text):
    """Return the text lowercased with ellipsis."""
    return text.lower() + "..."


def titleize(text):
    """Return the text in title case."""
    return text.title()


if __name__ == "__main__":
    sample = "Launch School is great"
    print(shout(sample))
    print(whisper(sample))
    print(titleize(sample))