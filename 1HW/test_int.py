import pytest


def test_1():
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0  # oh my god, sorry for the "copy past"


def test_2():
    assert 654 < 655 < 656


def test_3():
    with pytest.raises(AssertionError):
        assert 36 * 36 * 36 * 36 != 36 ** 4


class Test_4():
    __my_weight = 75
    my_height = 175

    def test_4(self):
        assert self.my_height - 10 ** 2 == self.__my_weight  # ok, i'm not fatty


@pytest.mark.parametrize('mas', [175, 176, 178, 179, 180])
def test_5(mas):
    try:
        assert mas % 5 == 0
    except AssertionError:
        print(mas)
