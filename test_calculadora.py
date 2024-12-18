# test_calculadora.py

import pytest
from calculadora import Calculadora

def test_suma():
    calc = Calculadora()
    resultado = calc.suma(2, 3)
    assert resultado == 5

def test_resta():
    calc = Calculadora()
    resultado = calc.resta(5, 3)
    assert resultado == 2

def test_multiplicacion():
    calc = Calculadora()
    resultado = calc.multiplicacion(2, 3)
    assert resultado == 6

def test_division():
    calc = Calculadora()
    resultado = calc.division(6, 3)
    assert resultado == 2
