from lib.diary import *

"""
test with regular input. Output is int
"""
def test_count_words_with_regular_input():
    result = count_words("Hello how are you doing today?")
    assert result == 6

"""
Test with white space only should result in 0
"""
def test_count_words_with_whitespace_input():
    result = count_words("   ")
    assert result == 0

"""Test with hypenated words should count as 1"""
def test_count_words_with_hypenated_input():
    result = count_words("hello-everyone how-are-you?")
    assert result == 2