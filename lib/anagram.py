class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, candidates):
        word_sorted = sorted(self.word)
        matches = []
        for candidate in candidates:
            if candidate != self.word and sorted(candidate) == word_sorted:
                matches.append(candidate)
        return matches
     
    