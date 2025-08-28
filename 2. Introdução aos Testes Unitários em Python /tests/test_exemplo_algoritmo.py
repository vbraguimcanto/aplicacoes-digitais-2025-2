from exemplo_algoritmo import soma
import pytest

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
    assert soma(-2, -3) == -5

def test_soma_com_numeros_grandes():
    assert soma(1000000, 2000000) == 3000000

def test_soma_com_numeros_negativos():
    assert soma(-5, -5) == -10
    assert soma(-10, 5) == -5   

def test_soma_com_zero():
    assert soma(0, 5) == 5
    assert soma(5, 0) == 5
    assert soma(0, 0) == 0

def test_soma_com_numeros_fracionarios():
    assert soma(2.5, 3.5) == 6.0
    assert soma(-1.5, 1.5) == 0.0
    assert soma(0.0, 0.0) == 0.0

def test_soma_com_numeros_mistos():
    assert soma(2, 3.5) == 5.5
    assert soma(-1, 1.5) == 0.5
    assert soma(0, 0.0) == 0.0 

def test_soma_numeros_invalidos():
    with pytest.raises(TypeError):
        soma("2", 3)