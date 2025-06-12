import pytest
from fraction import Fraction

def test_initialization():
    assert str(Fraction(6, 8)) == "3/4"
    assert str(Fraction(-3, -4)) == "3/4"
    assert str(Fraction(3, -4)) == "-3/4"
    assert str(Fraction(0, 5)) == "0/1"
    with pytest.raises(ValueError):
        Fraction(3, 0)

def test_repr_and_str():
    f = Fraction(2, 3)
    assert str(f) == "2/3"
    assert repr(f) == "Fraction(2, 3)"

def test_addition():
    assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)
    assert Fraction(3, 4) + 1 == Fraction(7, 4)
    assert 1 + Fraction(3, 4) == Fraction(7, 4)

def test_subtraction():
    assert Fraction(3, 4) - Fraction(1, 2) == Fraction(1, 4)
    assert Fraction(3, 4) - 1 == Fraction(-1, 4)
    assert 1 - Fraction(3, 4) == Fraction(1, 4)

def test_multiplication():
    assert Fraction(2, 3) * Fraction(3, 4) == Fraction(1, 2)
    assert Fraction(2, 3) * 3 == Fraction(2, 1)
    assert 3 * Fraction(2, 3) == Fraction(2, 1)

def test_division():
    assert Fraction(2, 3) / Fraction(1, 4) == Fraction(8, 3)
    assert Fraction(2, 3) / 2 == Fraction(1, 3)
    assert 2 / Fraction(2, 3) == Fraction(3, 1)

def test_comparisons():
    assert Fraction(1, 2) == Fraction(2, 4)
    assert Fraction(1, 2) != Fraction(3, 4)
    assert Fraction(1, 3) < Fraction(1, 2)
    assert Fraction(1, 3) <= Fraction(1, 3)
    assert Fraction(3, 4) > Fraction(1, 2)
    assert Fraction(3, 4) >= Fraction(3, 4)
    assert Fraction(3, 1) == 3
    assert Fraction(3, 1) < 4
    assert Fraction(5, 1) > 4

def test_other_methods():
    assert -Fraction(1, 2) == Fraction(-1, 2)
    assert abs(Fraction(-3, 4)) == Fraction(3, 4)
    assert float(Fraction(1, 2)) == 0.5
