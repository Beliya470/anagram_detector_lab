import pytest
from lib.anagram import Anagram

def test_can_create_anagram_instance():
    word = "listen"
    anagram = Anagram(word)
    assert isinstance(anagram, Anagram), f"Expected instance of Anagram but got {type(anagram)}"

def test_can_find_anagram():
    word = "listen"
    anagram = Anagram(word)
    result = anagram.match(['enlists', 'google', 'inlets', 'banana'])
    assert result == ['inlets'], f"Expected ['inlets'] but got {result}"

def test_returns_empty_list_for_no_anagram():
    word = "hello"
    anagram = Anagram(word)
    result = anagram.match(['world', 'test', 'data'])
    assert result == [], f"Expected [] but got {result}"
