from lib.tasks import *

""""Test to make sure if #TODO is in text it
returns True"""
def test_returns_true_if_TODO_in_text():
    result = check_todo("#TODO make a cup of tea")
    assert result == True

"""Test to make sure if #TODO isn't in text
then it returns False"""
def test_returns_false_if_TODO_not_in():
    result = check_todo("Make a cup of tea")
    assert result == False

"""Test to make sure returns False if the word
todo is in the text, but it is in lower case"""
def test_return_false_if_TODO_not_in_uppercase():
    result = check_todo("#todo make a cup of tea")
    assert result == False

"""test that zero length string still returns false
rather than any error"""
def test_zero_length_string():
    result = check_todo("")
    assert result == False

"""Test to make sure no error if no-str is passed
in as argument"""
def test_no_error_for_non_string_input():
    result = check_todo(1343)
    assert result == False