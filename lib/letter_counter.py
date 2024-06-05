# File: lib/letter_counter.py

class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 0
        for char in self.text:
            if not char.isalpha(): 
                continue #i.e. if there's a space/non alphabetic character
            counter[char] = counter.get(char, 0) + 1
            if counter[char] > most_common_count:
                most_common = char
                most_common_count = counter.get(char, 1)
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]
