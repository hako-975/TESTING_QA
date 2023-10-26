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

# ... (other test functions for Temp)

# Test Speed class
def test_calculate_speed():
    speed = Speed()
    assert speed.calculate_speed("FREEZE", "VERY LOW") == [80, 100, 100]
    assert speed.calculate_speed("COLD", "HIGH") == [80, 100, 100]
    # Add more test cases for different combinations of temperature and pressure.

# Mock user input for tests
@pytest.mark.parametrize("temperature, pressure, expected_speed", [
    ("FREEZE", "VERY LOW", [80, 100, 100]),
    ("COLD", "HIGH", [80, 100, 100]),
    # Add more test cases here
])
def test_speed_calculation_with_input(monkeypatch, temperature, pressure, expected_speed):
    # Mock user input
    monkeypatch.setattr('builtins.input', lambda _: f"{temperature}\n{pressure}\n")
    
    # Now you can run your script
    speed = Speed()
    speed_values = speed.calculate_speed(temperature, pressure)
    
    # Assertions
    assert speed_values == expected_speed

# You can also add test functions for the graphing functionality if you want to test the plotting.

# Remember to adjust the test cases and method calls according to your specific requirements.
