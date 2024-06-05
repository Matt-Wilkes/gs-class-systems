### Class Structure

# File: lib/diary.py

```python
class Diary:
    def __init__(self):
        pass

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass
```


# File: lib/diary_entry.py

```python
class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass
```



### Tests

### diary
```python
'''
Initially
The diary entry is empty
'''
def test_diary_entries_are_empty_initially():
    diary = Diary()
    assert diary.entries == []


'''
Given a words per minute of 5
And no diary entries
Return a reading time of 0
'''
def test_entries_empty_return_zero():
    diary = Diary()
    assert diary.reading_time(5) == 0

```

### diary entry

```python
'''
Given an empty Title or Contents
An error is raised 
'''
def test_empty_title_or_contents():
    with pytest.raises(Exception) as err:
        DiaryEntry("","")
    error_message = str(err.value)
    assert error_message == "Title or Content is empty"
    

'''
When a diary entry is created with a title and contents
The format attribute returns a formatted title and contents
"My Title: These are the contents"
'''

def test_diary_entry_format():
    diary_entry = DiaryEntry("Test Driven Development", "Test Driven Development might drive you mad, but before you let it do that, make sure you've written a test")
    result = diary_entry.format()
    assert result == "Test Driven Development: Test Driven Development might drive you mad, but before you let it do that, make sure you've written a test"

'''
When we call the count_words method
the number of words in the contents are returned as an int
'''

def test_diary_entry_length():
    diary_entry = DiaryEntry("Test Driven Development", "This is a string for a word count")
    result = diary_entry.count_words()
    assert result == 8
    
'''
When we call the reading time method and pass in words per minute
an estimate of the number of minutes (rounded up) to read the content is returned
'''

def test_diary_entry_wpm():
    diary_entry = DiaryEntry("Test Driven Development", "This is a string for a word count")
    result = diary_entry.reading_time(200)
    assert result == 1
'''
Given a reading time of 0
an error message should be returned
'''

def test_diary_entry_wpm():
    diary_entry = DiaryEntry("Test Driven Development", "This is a string for a word count")
    with pytest.raises(Exception) as err:
        diary_entry.reading_time(0)
    error_message = str(err.value)
    assert error_message == 'No reading time has been entered'

    
'''
Given a diary content of 15 words
With a WPM of 2
And a minutes of 2
reading chunk returns the first 4 words
'''
def test_reading_chunk_two_wpm_two_minutes():
    diary_entry = DiaryEntry("Test Driven Development", "In a small town nestled between rolling hills and dense forests, there lived a rabbit")
    result = diary_entry.reading_chunk(2, 2) 
    assert result == "In a small town"
    
'''
Given a diary content of 15 words
With a WPM of 2
And a minutes of 4
#reading_chunk returns the first 8 words
'''
def test_reading_chunk_two_wpm_four_minutes():
    diary_entry = DiaryEntry("Test Driven Development", "In a small town nestled between rolling hills and dense forests, there lived a rabbit")
    result = diary_entry.reading_chunk(2, 4) 
    assert result == "In a small town nestled between rolling hills"

'''
Given a contents of 15 words
And a wpm of 2 and a 2 minutes
first time #reading_chunk returns "In a small town"
next time #reading_chunk returns "nestled between rolling hills"
next time #reading_chunk returns "and dense forests, there"
'''

def test_reading_chunk_two_wpm_and_two_minutes_called_three_times():
    diary_entry = DiaryEntry("Test Driven Development", "In a small town nestled between rolling hills and dense forests, there lived a rabbit")
    assert diary_entry.reading_chunk(2, 2) == "In a small town"
    assert diary_entry.reading_chunk(2, 2) == "nestled between rolling hills"
    assert diary_entry.reading_chunk(2, 2) == "and dense forests, there"

'''
Given a contents of 15 words
And a wpm of 2 and a 2 minutes
first time #reading_chunk returns "In a small town"
next time with a wpm of 2 and 1 minutes #reading_chunk returns "nestled between"
next time with a wpm of 2 and 2 minutes #reading_chunk returns "rolling hills and dense"
'''

def test_reading_chunk_two_wpm_and_two_minutes_called_three_times():
    diary_entry = DiaryEntry("Test Driven Development", "In a small town nestled between rolling hills and dense forests, there lived a rabbit")
    assert diary_entry.reading_chunk(2, 2) == "In a small town"
    assert diary_entry.reading_chunk(2, 1) == "nestled between"
    assert diary_entry.reading_chunk(2, 2) == "rolling hills and dense"
   
''' 
Given a contents of 15 words
And a wpm of 2 and 3 minutes
if #reading_chunk is called repeatedly
the last chunk is the last words in the text even if shorter than words that can be read
the next chunk after that is the start of the chunk again
'''

def test_reading_chunk_with_multiple_calls_wraps_correctly():
    diary_entry = DiaryEntry("Test Driven Development", "In a small town nestled between rolling hills and dense forests, there lived a rabbit")
    assert diary_entry.reading_chunk(2, 3) == "In a small town nestled between"
    assert diary_entry.reading_chunk(2, 3) == "rolling hills and dense forests, there"
    assert diary_entry.reading_chunk(2, 3) == "lived a rabbit"
    assert diary_entry.reading_chunk(2, 3) == "In a small town nestled between"

''' 
Given a contents of 15 words
And a wpm of 5 and 1 minutes
if #reading_chunk is called repeatedly
and the last chunk equals the last words in the text
the next chunk should be the first chunk again
'''

def test_reading_chunk_wraps_around_after_multiple_calls():
    diary_entry = DiaryEntry("Test Driven Development", "In a small town nestled between rolling hills and dense forests, there lived a rabbit")
    assert diary_entry.reading_chunk(5, 1) == "In a small town nestled"
    assert diary_entry.reading_chunk(5, 1) == "between rolling hills and dense"
    assert diary_entry.reading_chunk(5, 1) == "forests, there lived a rabbit"
    assert diary_entry.reading_chunk(5, 2) == "In a small town nestled between rolling hills and dense"

```
### Integration


```python
'''
Given a diary entry is created
entries_list should be populated with the entry
'''
def test_diary_entry_updates_entries_list():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry","This is my first entry")
    diary.add(diary_entry1)
    assert diary.entries == [diary_entry1]
    
'''
Given there are diary entries
return a list of entries
'''

def test_all_returns_diary_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry","This is my first entry")
    diary.add(diary_entry1)
    assert diary.all() == [diary_entry1]

'''
Given there are no diary entries
Return a string "The diary is empty"
'''
def test_empty_diary_returns_error():
    diary = Diary()
    assert diary.all() == "The diary is empty"

'''
Given there are multiple diary entries
a list of the entries should be returned
'''

def test_all_returns_multiple_diary_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry","This is my first entry")
    diary_entry2 = DiaryEntry("second entry","This is my second entry")
    diary_entry3 = DiaryEntry("third entry","This is my third entry")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.all() == [diary_entry1, diary_entry2, diary_entry3]

'''
Given 1 diary entries exists with 5 words
count_words should return 5
'''

def test_count_words_returns_5():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry","This is my first entry")
    diary.add(diary_entry1)
    assert diary.count_words() == 5
    
    '''
Given three diary entries exist with combined word count of 15
count_words should return the total of all the words in the diary content (15)
'''

def test_count_words_returns_15():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry","This is my first entry")
    diary_entry2 = DiaryEntry("second entry","This is my second entry")
    diary_entry3 = DiaryEntry("third entry","This is my third entry")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.count_words() == 15
    
'''
Given the diary entries are empty
count-words should return a count of 0
'''

def test_count_words_returns_zero_for_empty_diary():
    diary = Diary()
    assert diary.count_words() == 0
    
'''
Given a words per minute of 5 and content containing 10 words
reading_time should return 2
'''
def test_reading_time_5_wpm_10_words():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry","This is my first entry, one two three four five")
    diary.add(diary_entry1)
    assert diary.reading_time(5) == 2

'''
Given a words per minute of 5 and content containing 10 words
reading_time should return 2
'''
def test_reading_time_5_wpm_20_words():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry","This is my first entry, one two three four five")
    diary_entry2 = DiaryEntry("second entry","This is my second entry, one two three four five")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.reading_time(5) == 4
    
'''
Given a wpm of 0
an error should be returned 
'''
def test_reading_time_zero_wpm_errors():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry","This is my first entry, one two three four five")
    diary.add(diary_entry1)
    with pytest.raises(Exception) as err:
        diary.reading_time(0)
    error_message = str(err.value)
    assert error_message == "WPM needs to be more than 0"
    
    
'''
Given wpm of 5 and 2 minutes
And an entry with a word length of 10
find_best_entry_for_reading_time should return the entry with 10 words
'''

def test_find_best_entry_for_reading_time_10_words():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry","This is my first entry, one two three four five")
    diary.add(diary_entry1)
    assert diary.find_best_entry_for_reading_time(5, 2) == diary_entry1
    
'''
Given entries contains three entries
8 words, 9 words and 11 words
And 5 wpm with 2 minutes is passed
find_best_entry_for_reading_time should return the entry with 9 words
'''
def test_find_best_entry_for_reading_time_three_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry", "one two three four five six seven eight")
    diary_entry2 = DiaryEntry("second entry", "one two three four five six seven eight nine")
    diary_entry3 = DiaryEntry("third entry", "one two three four five six seven eight nine ten eleven")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.find_best_entry_for_reading_time(5, 2) == diary_entry2
    
'''
Given entries contains three entries
3 words, 6 words and 15 words
And 5 wpm with 2 minutes is passed
find_best_entry_for_reading_time should return the entry with 9 words
'''
def test_find_best_entry_for_reading_time_three_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry", "one two three")
    diary_entry2 = DiaryEntry("second entry", "one two three four five six")
    diary_entry3 = DiaryEntry("third entry", "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.find_best_entry_for_reading_time(5, 2) == diary_entry2

'''
Given 5 wpm and 2 minutes
If all entries are above 10 words
an exception should be raised
'''
def test_find_best_entry_for_reading_time_all_entries_above_time_available():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry", "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen")
    diary_entry2 = DiaryEntry("second entry", "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen")
    diary_entry3 = DiaryEntry("third entry", "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(5, 2) == "No diary entries can be read in given time"
    error_message = str(err.value)
    assert error_message == "No diary entries can be read in given time"

'''
Given wpm is 0
find_best_entry_for_reading_time should return an error

'''
def test_find_best_entry_for_reading_time_zero_wpm_error():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry", "one two three four five ")
    diary.add(diary_entry1)
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(0, 2) == "No diary entries can be read in given time"
    error_message = str(err.value)
    assert error_message == "Zero cannot be entered"
    
'''
Given minutes is zero
find_best_entry_for_reading_time should return an error
'''

def test_find_best_entry_for_reading_time_zero_wpm_error():
    diary = Diary()
    diary_entry1 = DiaryEntry("first entry", "one two three four five ")
    diary.add(diary_entry1)
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(5, 0) == "No diary entries can be read in given time"
    error_message = str(err.value)
    assert error_message == "Zero cannot be entered"
```
