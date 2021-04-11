"""Rolul acestui modul este acela de a introduce functii pentru transmiterea de mesaje.
Fisier: hello.py
Autor: airman
Versiune Python: 3.7"""
default_name = 'Ghita'

def hello_python():
    """Returneaza un mesaj de tipul Hello Python!"""
    return 'Hello Python!'

def hello_name(name = default_name):
    """Returneaza un mesaj personalizat sau Hello Ghita! daca nu se transmite un nume."""
    if len(name) <= 2:
        raise ValueError("Invalid name!")
    return 'Hello {}!'.format(name)
