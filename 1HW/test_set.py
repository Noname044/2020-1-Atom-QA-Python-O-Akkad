import pytest

all_books = {159357468, 357159246, 84269317, 571535955, 791354826, 789456123, 74852963, 456987123}

costly_books = {159357468, 357159246, 84269317, 571535955, 791354826}

stolen_books = {159357468, 789456123, 74852963, 456987123, 791354826}


def test_1():
    with pytest.raises(AssertionError):
        assert costly_books | stolen_books != all_books


def test_2():
    with pytest.raises(AssertionError):
        assert len(all_books) > 10


def test_3():
    try:
        assert costly_books & stolen_books == 0
    except AssertionError:
        print('fck we lost IMPORTANT book')


class Test_4:
    _author = 'AkkadOA'
    my_books = {159357468}

    def test_mybook(self):
        try:
            assert costly_books & self.my_books == 0
        except AssertionError:
            print("oh, good")


@pytest.mark.parametrize('id', Test_4.my_books)
def test_parametr(id):
    try:
        assert id in stolen_books == 0
    except AssertionError:
        print("pff, stolen")
