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
            assert k in bear and favorite[k] == bear[k]
        except AssertionError:
            print('Oppa u have unique sort of bear', k)


def test_2():
    if 'Pilzner' in bear:
        with pytest.raises(AssertionError):
            assert bear['Pilzner'] == 'Czech'
    else:
        print('uuffff')


def test_3():
    try:
        assert 'Garage' in favorite
    except AssertionError:
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
