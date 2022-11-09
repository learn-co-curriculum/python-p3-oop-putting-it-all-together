#!/usr/bin/env python3

from shoe import Shoe

import io
import sys

class TestShoe:
    '''Shoe in shoe.py'''

    def test_initialize_with_brand(self):
        '''gets initialized with a brand.'''
        Shoe("Adidas")

    def test_has_brand(self):
        '''has the brand passed to __init__.'''
        stan_smith = Shoe("Adidas")
        assert(stan_smith.brand == "Adidas")

    def test_has_color(self):
        '''can be assigned a color.'''
        stan_smith = Shoe("Adidas")
        stan_smith.color = "White"
        assert(stan_smith.color == "White")

    def test_has_size(self):
        '''can be assigned a size.'''
        stan_smith = Shoe("Adidas")
        stan_smith.size = 11
        assert(stan_smith.size == 11)

    def test_has_material(self):
        '''can be assigned a material.'''
        stan_smith = Shoe("Adidas")
        stan_smith.material = "Leather"
        assert(stan_smith.material == "Leather")

    def test_has_condition(self):
        '''can be assigned a condition.'''
        stan_smith = Shoe("Adidas")
        stan_smith.condition = "Used"
        assert(stan_smith.condition == "Used")

    def test_can_cobble(self):
        '''says that the shoe has been repaired.'''
        stan_smith = Shoe("Adidas")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.cobble()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Your shoe is as good as new!\n")

    def test_cobble_makes_new(self):
        '''has "New" condition after repair.'''
        stan_smith = Shoe("Adidas")
        stan_smith.condition = "Used"
        stan_smith.cobble()
        assert(stan_smith.condition == "New")
