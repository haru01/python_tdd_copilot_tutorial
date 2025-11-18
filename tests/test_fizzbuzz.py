import pytest
from tests.fizzbuz import fizzbuzz


class TestFizzBuzz:
    def test_returns_1_when_given_1(self):
        """1を渡すと"1"を返す"""
        assert fizzbuzz(1) == "1"

    def test_returns_fizz_when_given_3(self):
        """3を渡すと"Fizz"を返す"""
        assert fizzbuzz(3) == "Fizz"

    def test_returns_buzz_when_given_5(self):
        """5を渡すと"Buzz"を返す"""
        assert fizzbuzz(5) == "Buzz"

    def test_returns_fizzbuzz_when_given_15(self):
        """15を渡すと"FizzBuzz"を返す"""
        assert fizzbuzz(15) == "FizzBuzz"

    def test_returns_fizz_for_multiple_of_3(self):
        """3の倍数(6, 9)で"Fizz"を返す"""
        assert fizzbuzz(6) == "Fizz"
        assert fizzbuzz(9) == "Fizz"

    def test_returns_buzz_for_multiple_of_5(self):
        """5の倍数(10, 20)で"Buzz"を返す"""
        assert fizzbuzz(10) == "Buzz"
        assert fizzbuzz(20) == "Buzz"

    def test_returns_fizzbuzz_for_multiple_of_15(self):
        """15の倍数(30, 45)で"FizzBuzz"を返す"""
        assert fizzbuzz(30) == "FizzBuzz"
        assert fizzbuzz(45) == "FizzBuzz"

    def test_returns_number_for_non_multiples(self):
        """3でも5でも割り切れない数はそのまま文字列で返す"""
        assert fizzbuzz(2) == "2"
        assert fizzbuzz(7) == "7"
        assert fizzbuzz(13) == "13"

    def test_handles_zero_as_fizzbuzz(self):
        """0は両方の倍数として扱い"FizzBuzz"を返す"""
        assert fizzbuzz(0) == "FizzBuzz"

    def test_handles_negative_numbers(self):
        """負の数でも同じルールが適用される"""
        assert fizzbuzz(-3) == "Fizz"
        assert fizzbuzz(-5) == "Buzz"
        assert fizzbuzz(-15) == "FizzBuzz"

    def test_raises_type_error_for_non_int(self):
        """整数以外を渡すとTypeErrorを送出する"""
        with pytest.raises(TypeError):
            fizzbuzz("3")
        with pytest.raises(TypeError):
            fizzbuzz(3.5)
        with pytest.raises(TypeError):
            fizzbuzz(None)