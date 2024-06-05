
# from lib.diary import *
# from lib.diaryentry import *
# import pytest

# '''
# Given a diary entry is created
# entries_list should be populated with the entry
# '''
# def test_diary_entry_updates_entries_list():
#     diary = Diary()
#     diary_entry1 = DiaryEntry("first entry","This is my first entry")
#     diary.add(diary_entry1)
#     assert diary.entries == [diary_entry1]
    
# '''
# Given there are diary entries
# return a list of entries
# '''

# def test_all_returns_diary_entries():
#     diary = Diary()
#     diary_entry1 = DiaryEntry("first entry","This is my first entry")
#     diary.add(diary_entry1)
#     assert diary.all() == [diary_entry1]

# '''
# Given there are no diary entries
# Return a string "The diary is empty"
# '''
# def test_empty_diary_returns_error():
#     diary = Diary()
#     assert diary.all() == "The diary is empty"

# '''
# Given there are multiple diary entries
# a list of the entries should be returned
# '''

# def test_all_returns_multiple_diary_entries():
#     diary = Diary()
#     diary_entry1 = DiaryEntry("first entry","This is my first entry")
#     diary_entry2 = DiaryEntry("second entry","This is my second entry")
#     diary_entry3 = DiaryEntry("third entry","This is my third entry")
#     diary.add(diary_entry1)
#     diary.add(diary_entry2)
#     diary.add(diary_entry3)
#     assert diary.all() == [diary_entry1, diary_entry2, diary_entry3]

# '''
# Given 1 diary entries exists with 5 words
# count_words should return 5
# '''

# def test_count_words_returns_5():
#     diary = Diary()
#     diary_entry1 = DiaryEntry("first entry","This is my first entry")
#     diary.add(diary_entry1)
#     assert diary.count_words() == 5
    
#     '''
# Given three diary entries exist with combined word count of 15
# count_words should return the total of all the words in the diary content (15)
# '''

# def test_count_words_returns_15():
#     diary = Diary()
#     diary_entry1 = DiaryEntry("first entry","This is my first entry")
#     diary_entry2 = DiaryEntry("second entry","This is my second entry")
#     diary_entry3 = DiaryEntry("third entry","This is my third entry")
#     diary.add(diary_entry1)
#     diary.add(diary_entry2)
#     diary.add(diary_entry3)
#     assert diary.count_words() == 15
    
# '''
# Given the diary entries are empty
# count-words should return a count of 0
# '''

# def test_count_words_returns_zero_for_empty_diary():
#     diary = Diary()
#     assert diary.count_words() == 0
    
# '''
# Given a words per minute of 5 and content containing 10 words
# reading_time should return 2
# '''
# def test_reading_time_5_wpm_10_words():
#     diary = Diary()
#     diary_entry1 = DiaryEntry("first entry","This is my first entry, one two three four five")
#     diary.add(diary_entry1)
#     assert diary.reading_time(5) == 2

# '''
# Given a words per minute of 5 and content containing 10 words
# reading_time should return 2
# '''
# def test_reading_time_5_wpm_20_words():
#     diary = Diary()
#     diary_entry1 = DiaryEntry("first entry","This is my first entry, one two three four five")
#     diary_entry2 = DiaryEntry("second entry","This is my second entry, one two three four five")
#     diary.add(diary_entry1)
#     diary.add(diary_entry2)
#     assert diary.reading_time(5) == 4
    
# '''
# Given a wpm of 0
# an error should be returned 
# '''
# def test_reading_time_zero_wpm_errors():
#     diary = Diary()
#     diary_entry1 = DiaryEntry("first entry","This is my first entry, one two three four five")
#     diary.add(diary_entry1)
#     with pytest.raises(Exception) as err:
#         diary.reading_time(0)
#     error_message = str(err.value)
#     assert error_message == "WPM needs to be more than 0"
    
    
# '''
# Given wpm of 5 and 2 minutes
# And an entry with a word length of 10
# find_best_entry_for_reading_time should return the entry with 10 words
# '''

# def test_find_best_entry_for_reading_time_10_words():
#     diary = Diary()
#     diary_entry1 = DiaryEntry("first entry","This is my first entry, one two three four five")
#     diary.add(diary_entry1)
#     assert diary.find_best_entry_for_reading_time(5, 2) == diary_entry1
    
# '''
# Given entries contains three entries
# 8 words, 9 words and 11 words
# And 5 wpm with 2 minutes is passed
# find_best_entry_for_reading_time should return the entry with 9 words
# '''
# def test_find_best_entry_for_reading_time_three_entries():
#     diary = Diary()
#     diary_entry1 = DiaryEntry("first entry", "one two three four five six seven eight")
#     diary_entry2 = DiaryEntry("second entry", "one two three four five six seven eight nine")
#     diary_entry3 = DiaryEntry("third entry", "one two three four five six seven eight nine ten eleven")
#     diary.add(diary_entry1)
#     diary.add(diary_entry2)
#     diary.add(diary_entry3)
#     assert diary.find_best_entry_for_reading_time(5, 2) == diary_entry2
    
# '''
# Given entries contains three entries
# 3 words, 6 words and 15 words
# And 5 wpm with 2 minutes is passed
# find_best_entry_for_reading_time should return the entry with 9 words
# '''
# def test_find_best_entry_for_reading_time_three_entries():
#     diary = Diary()
#     diary_entry1 = DiaryEntry("first entry", "one two three")
#     diary_entry2 = DiaryEntry("second entry", "one two three four five six")
#     diary_entry3 = DiaryEntry("third entry", "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen")
#     diary.add(diary_entry1)
#     diary.add(diary_entry2)
#     diary.add(diary_entry3)
#     assert diary.find_best_entry_for_reading_time(5, 2) == diary_entry2

# '''
# Given 5 wpm and 2 minutes
# If all entries are above 10 words
# an exception should be raised
# '''
# def test_find_best_entry_for_reading_time_all_entries_above_time_available():
#     diary = Diary()
#     diary_entry1 = DiaryEntry("first entry", "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen")
#     diary_entry2 = DiaryEntry("second entry", "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen")
#     diary_entry3 = DiaryEntry("third entry", "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen")
#     diary.add(diary_entry1)
#     diary.add(diary_entry2)
#     diary.add(diary_entry3)
#     with pytest.raises(Exception) as err:
#         diary.find_best_entry_for_reading_time(5, 2) == "No diary entries can be read in given time"
#     error_message = str(err.value)
#     assert error_message == "No diary entries can be read in given time"

# '''
# Given wpm is 0
# find_best_entry_for_reading_time should return an error

# '''
# def test_find_best_entry_for_reading_time_zero_wpm_error():
#     diary = Diary()
#     diary_entry1 = DiaryEntry("first entry", "one two three four five ")
#     diary.add(diary_entry1)
#     with pytest.raises(Exception) as err:
#         diary.find_best_entry_for_reading_time(0, 2) == "No diary entries can be read in given time"
#     error_message = str(err.value)
#     assert error_message == "Zero cannot be entered"
    
# '''
# Given minutes is zero
# find_best_entry_for_reading_time should return an error
# '''

# def test_find_best_entry_for_reading_time_zero_wpm_error():
#     diary = Diary()
#     diary_entry1 = DiaryEntry("first entry", "one two three four five ")
#     diary.add(diary_entry1)
#     with pytest.raises(Exception) as err:
#         diary.find_best_entry_for_reading_time(5, 0) == "No diary entries can be read in given time"
#     error_message = str(err.value)
#     assert error_message == "Zero cannot be entered"

