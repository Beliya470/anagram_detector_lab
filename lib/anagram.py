class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        return [candidate for candidate in candidates if self.is_anagram(candidate)]

    def is_anagram(self, candidate):
        return self.word != candidate.lower() and sorted(self.word) == sorted(candidate.lower())
