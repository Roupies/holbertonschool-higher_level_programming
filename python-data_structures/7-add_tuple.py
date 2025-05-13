#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Complète les tuples avec des zéros si nécessaire
    a1, a2 = (tuple_a + (0, 0))[:2]  # Limiter à 2 éléments
    b1, b2 = (tuple_b + (0, 0))[:2]  # Limiter à 2 éléments

    # Additionne les premiers et deuxièmes éléments
    return (a1 + b1, a2 + b2)
