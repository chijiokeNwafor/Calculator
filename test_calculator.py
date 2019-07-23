import calculator


class TestCalculator:
    

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)
