"""Word Finder: finds random words from a dictionary."""


import random

class WordFinder:
    def __init__(self, dictionary_file):
        """Initialize the WordFinder with a dictionary file."""
        self.words = self.load_words(dictionary_file)

    def load_words(self, dictionary_file):
        """Load words from a dictionary file and return them as a list."""
        with open(dictionary_file, 'r') as file:
            words = file.readlines()
        return [word.strip() for word in words]

    def random_word(self):
        """Return a random word from the loaded dictionary."""
        return random.choice(self.words)


