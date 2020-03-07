import pytest

bear = {
    'Paulaner': 'Munich',
    'Wolpertinger': 'Bavaria',
    'Prazacka': 'Czech',
    'Guinness': 'Dublin',
    'Garage': 'Ufa',
    'Baltika': 'Saint Petersburg'
}

favorite = {
    'Paulaner': 'Munich',
    'Wolpertinger': 'Bavaria',
    'Grandfathers bear': 'Moscow'
}


def test_1():
    for k in favorite:
        try:
            assert favorite[k] == bear[k]
        except KeyError:
            print('Oppa u have unique sort of bear', favorite[k])


def test_2():
    for k in bear:
        if bear[k] == 'Czech':
            with pytest.raises(AssertionError):
                assert k == 'Pilzner'


def test_3():
    try:
        assert 'Garage' in favorite == True
    except Exception:
        print('whyyyy?')


class Test_4:
    bad_bear = {
        'Garage': 'Ufa',
        'Baltika': 'Saint Petersburg'
    }

    def test_bueee(self):
        for k in bear:
            for key in self.bad_bear:
                try:
                    assert k != key
                except AssertionError:
                    print('fufufu', key)


@pytest.mark.parametrize('dic', Test_4.bad_bear)
def test_5(dic):
    # for k in dic:
    with pytest.raises(AssertionError):
        assert dic == 'Tuborg'