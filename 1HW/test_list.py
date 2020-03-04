import pytest

byears = [1956, 1977, 1995, 1998, 2010]

leapyears = [1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000]


def test_class_eq():
    for i in byears:
        try:
            assert i % 5 == 0
        except AssertionError:
            print('divided with remainder:', i)


def test_bndr_cndtn():
    for i in byears:
        try:
            assert i < 2000
        except AssertionError:
            print('Must be before 2000:', i)


def test_pair_wise():
    for i in leapyears:
        for j in byears:
            try:
                assert i != j
            except AssertionError:
                print('Leap year:', j)


class Test_4:
    name = 'Oleg'
    year = 21

    def test_class(self):
        for i in byears:
            with pytest.raises(AssertionError):
                assert 2020 - i == self.year


@pytest.mark.parametrize('par1', [1920])
def test_par(par1):
    for i in byears:
        with pytest.raises(Exception):
            assert i == par1
