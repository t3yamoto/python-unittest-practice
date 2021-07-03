from unittest.mock import MagicMock, Mock


class ProductionClass:
    def method():
        pass


thing = ProductionClass()
thing.method = MagicMock(return_value=3)
thing.method(3, 4, 5, key="value")

thing.method.assert_called_with(3, 4, 5, key="value")
# thing.method.assert_called_with(4, 5, key="value")

# ---

mock = Mock(side_effect=KeyError("foo"))
# mock()

# ---

values = {"a": 1, "b": 2, "c": 3}


def side_effect(arg):
    return values[arg]


mock.side_effect = side_effect
print(mock("a"), mock("b"), mock("c"))

mock.side_effect = [5, 4, 3, 2, 1]
print(mock(), mock(), mock())
