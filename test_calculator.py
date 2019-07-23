# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:40:08 2019

@author: Steven
"""

"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)