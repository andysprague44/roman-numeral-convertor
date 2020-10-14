import pytest
from application.convertor import convert


class TestLogicFunctions:
    def test_can_run_tests(self):
        assert(1 == 1)

    def test_can_convert_I_returns_1(self):
        number = convert('I')
        assert(number == 1)
