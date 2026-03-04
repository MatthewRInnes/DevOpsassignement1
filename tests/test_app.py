import pytest
from app import (
    kg_to_grams,
    grams_to_kg,
    kg_to_pounds,
    pounds_to_kg,
    grams_to_pounds,
    pounds_to_grams,
    main_conversion_function,
)

# Example cases for conversion functions
def test_kg_to_grams():
    assert kg_to_grams(1) == 1000

def test_grams_to_kg():
    assert grams_to_kg(1000) == 1

def test_kg_to_pounds():
    assert pytest.approx(kg_to_pounds(1), rel=0.01) == 2.20462

def test_pounds_to_kg():
    assert pytest.approx(pounds_to_kg(2.20462), rel=1e-5) == 1

def test_grams_to_pounds():
    assert pytest.approx(grams_to_pounds(1000), rel=1e-5) == 2.20462

def test_pounds_to_kg_main_function():
    """Test that main_conversion_function correctly converts pounds to kg (no erroneous negative sign)."""
    result = main_conversion_function(1, 'pounds', 'kg')
    expected = 0.453592  # 1 pound = 0.453592 kg
    assert result == pytest.approx(expected, rel=1e-5)
