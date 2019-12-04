import pytest
from Hello_world import *

def test_hello():
    result = hello()
    assert result == "Hello!"
