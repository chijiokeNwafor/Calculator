import calculator


class TestCalculator:
    def test_addtion(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 6 == calculator.multiplication(2, 3)