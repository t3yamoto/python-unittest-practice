from unittest.mock import patch


class ClassName1:
    pass


class ClassName2:
    pass


@patch("ClassName2")
@patch("ClassName1")
def test(MockClass1, MockClass2):
    ClassName1()
    ClassName2()
    assert MockClass1 is ClassName1
    assert MockClass2 is ClassName2
    assert MockClass1.called
    assert MockClass2.called


test()
