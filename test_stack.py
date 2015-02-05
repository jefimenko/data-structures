import pytest
from stack import Level
from stack import Stack


# Tests for Levels object
def test_level_cons():
    # For no data passed into Level(), this should fail
    a = Level()
    b = Level(1)
    assert b.data == 1
    c = Level('asdf)
    assert c.data == 'asdf'
