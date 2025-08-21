from main import multiply
import pytest


def test_multiply():
    assert 4 == multiply(9, 10)
