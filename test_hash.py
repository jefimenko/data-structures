from hash import Hash
import pytest
from io import open

def test_create():
    something = Hash(10)
    assert isinstance(something.h_list, list)
    assert len(something.h_list) == 10


def test_bad_create():
    with pytest.raises(TypeError):
        something = Hash()


# def test_not_string():
#     something = Hash(10)

def test_duplicate_key_different_value():
    """a get on a hash table should return the last value put in"""
    hash_table = Hash(10)
    word = 'asd'
    values = range(4)
    for value in values:
        hash_table.set(word, value)
    # last value in was 3
    assert hash_table.get(word) == 3


def test_hash():
    something = Hash(10)
    hashed_val = something.hash('hello')
    assert hashed_val == 2


def test_set():
    something = Hash(10)
    something.set('asdf', 10)

    sum = 0
    for char in 'asdf':
        sum += ord(char)
    assert ('asdf', 10) in something.h_list[sum % 10]


def test_get():
    something = Hash(10)
    something.set('asdf', 10)
    assert something.get('asdf') == 10

def test_on_word():
    """testing on word dictionary built into UNIX"""
    infile = open('/usr/share/dict/words', 'r')
    full_text = []
    for line in infile:
        full_text.append(line.strip())
    allbins = Hash(10000)
    # for word in full_text:
    #     allbins.set(word, word)
    # for word in full_text:
    #     assert allbins.get(word) == word

