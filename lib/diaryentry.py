import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == '' or contents == '':
            raise Exception("Title or Content is empty")
        self.title = title
        self.contents = contents
        self.read_so_far = 0
        
    def format(self):
        return f'{self.title}: {self.contents}'


    def count_words(self):
        self.entry_length = len(self.contents.split())
        return self.entry_length
  
    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception('No reading time has been entered')
        time_to_read = math.ceil(self.count_words()/wpm)
        return time_to_read 

    def reading_chunk(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        words = self.contents.split()
        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + words_user_can_read
        words_chunk = words[chunk_start:chunk_end]
        if chunk_end < len(words):
            self.read_so_far = chunk_end
        else:
            self.read_so_far = 0
        
        return ' '.join(words_chunk)