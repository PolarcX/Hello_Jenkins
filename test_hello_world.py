import pytest
from Hello_world import *

#hello
def test_hello():
    result = hello()
    assert result == "Hello!"
