#!/usr/bin/env python
# -*- coding: utf-8 -*-

from udkm1Dsim.atoms import Atom, AtomMixed
import numpy as np


def test_atom():
    Dy = Atom('Dy')
    assert Dy.symbol == 'Dy'
    assert Dy.id == 'Dy'
    assert Dy.ionicity == 0
    assert Dy.name == 'Dysprosium'
    assert Dy.atomic_number_z == 66
    assert Dy.mass_number_a == 162.5
    assert round(Dy.mass, 28) == 2.698e-25
    # check if python hash works the same on different systems
    assert np.array_equal(Dy.atomic_form_factor_coeff[10],
                          np.array([1.17404e+01, -9.99900e+03, 2.25052e-01]))
    assert np.array_equal(Dy.cromer_mann_coeff,
                          np.array([66.0, 0.0, 26.507, 17.6383, 14.5596, 2.96577, 2.1802, 0.202172,
                                    12.1899, 111.874, 4.29728]))
    Oxygen = Atom('O', id='myOxygen', ionicity=-1)
    assert Oxygen.symbol == 'O'
    assert Oxygen.id == 'myOxygen'
    assert Oxygen.ionicity == -1


def test_atom_mixed():
    FeCo = AtomMixed('FeCo')
    assert FeCo.name == 'FeCo'
    assert FeCo.id == 'FeCo'
