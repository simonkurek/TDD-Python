import pytest
from main import fizzBuzz as fb

def test_fizz():
    assert fb(3) == 'fizz'

def test_buzz():
    assert fb(5) == 'buzz'

def test_fizzbuzz():
    assert fb(15) == 'fizzbuzz'

def test_fizz_multi():
    assert fb(6) == 'fizz'

def test_buzz_multi():
    assert fb(10) == 'buzz'

def test_fizzbuzz_multi():
    assert fb(30) == 'fizzbuzz'

def test_default():
    assert fb(7) == 7