from lib.diaryentry import DiaryEntry
import math

class Diary:
    def __init__(self):
        self.entries = []
    
    def add(self, entry):
        self.entries.append(entry)
    
    def all(self):
        if len(self.entries) > 0:
            return self.entries
        return "The diary is empty"
    
    def count_words(self):
        word_count = 0
        for entry in self.entries:
            word_count += DiaryEntry.count_words(entry)
        return word_count
            
    def reading_time(self, wpm):
        self.wpm = wpm
        if self.wpm == 0:
            raise Exception("WPM needs to be more than 0")
        return math.ceil(self.count_words()/wpm)
    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        self.wpm = wpm
        self.minutes = minutes
        self.available = wpm * minutes
        if self.wpm <= 0 or self.minutes <= 0:
            raise Exception("Zero cannot be entered")
        while self.available > 0:
            for entry in self.entries:
                if len(entry.contents.split()) == self.available:
                    return entry
                else: 
                    self.available -= 1
        raise Exception("No diary entries can be read in given time")
        
        