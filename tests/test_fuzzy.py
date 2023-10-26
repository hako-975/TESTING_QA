# tests/test_fuzzy.py

from fuzzy import Temp, Pressure, Speed

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
    assert pressure.very_low(0.1) == 1
    assert pressure.very_low(0.3) == 0
    assert pressure.very_low(0.15) == 1

def test_low():
    pressure = Pressure()
    assert pressure.low(0.3) == 0
    assert pressure.low(0.5) == 0.5
    assert pressure.low(0.7) == 0.5
    assert pressure.low(0.6) == 0
    assert pressure.low(0.8) == 0
