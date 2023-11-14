from lib.diary import *

"""
Test input of more than 5 words should return first 
5 words followed by '...' 
"""
def test_string_more_than_five_words():
    result = make_snippet("Hello everyone how are you today, I hope you are doing well.")
    assert result == "Hello everyone how are you..."


"""
Test input with 5 words should just return those 5 words
"""
def test_string_with_exactly_five_words():
    result = make_snippet("today was a good day")
    assert result == "today was a good day"

"""
Test input with less than 5 words should just return those words
"""
def test_string_with_less_than_five_words():
    result = make_snippet("I am good")
    assert result == "I am good"

"""
test input which is longer than five words where the fith word
has punctutation and would make the output look strange
e.g. today was a good day.... or day,..."""
def test_removing_punctuation_from_fith_word():
    result = make_snippet("Today was a good day, we did a lot of fun stuff")
    assert result == "Today was a good day..."

def test_empty_string_should_return_empty_string():
    result = make_snippet('')
    assert result == ''
