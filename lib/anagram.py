class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, candidates):
        return [w for w in candidates if self.word != w and sorted(self.word) == sorted(w)]
    