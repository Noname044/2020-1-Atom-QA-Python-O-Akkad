import pytest

my_str = "I just want to sleep"


def test_1():
    with pytest.raises(AssertionError):
        assert my_str == "i just want to sleep"


def test_2():
    assert len(my_str) > 10


def test_3():
    with pytest.raises(AssertionError):
        assert 'digit'.isdigit() == True


class Test_4:
    class_str = 'ssssssssssssssssssss'

    def test_4(self):
        with pytest.raises(AssertionError):
            assert self.class_str.count('s') == 21


@pytest.mark.parametrize('sm_str', "I'm fine")
def test_5(sm_str):
    with pytest.raises(AssertionError):
        assert 'True' in sm_str
