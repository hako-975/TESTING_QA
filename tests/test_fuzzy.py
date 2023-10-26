# tests/test_fuzzy.py
from fuzzy import Temp, Pressure, Speed
import pytest

pytestmark = pytest.mark.disable_output_capturing

# Test Temp class
def test_freeze():
    temp = Temp()
    assert temp.freeze(30) == 1
    assert temp.freeze(40) == 0
    assert temp.freeze(20) == 1

def test_cold():
    temp = Temp()
    assert temp.cold(30) == 0
    assert temp.cold(50) == 0.5
    assert temp.cold(70) == 0.5
    assert temp.cold(80) == 0
    assert temp.cold(90) == 0

def test_warm():
    temp = Temp()
    assert temp.warm(60) == 1
    assert temp.warm(70) == 0.5
    assert temp.warm(50) == 0.5
    assert temp.warm(80) == 0
    assert temp.warm(90) == 0

def test_hot():
    temp = Temp()
    assert temp.hot(80) == 1
    assert temp.hot(90) == 0.5
    assert temp.hot(70) == 0.5
    assert temp.hot(100) == 1
    assert temp.hot(110) == 0

# Test Pressure class
def test_very_low():
    pressure = Pressure()
