from unittest.mock import MagicMock, Mock, patch


class ProductionClass:
    def method():
        pass


with patch.object(ProductionClass, "method", return_value=None) as mock_method:
    thing = ProductionClass()
    thing.method(1, 2, 3)

mock_method.assert_called_once_with(1, 2, 3)
# mock_method.assert_called_once_with(1, 2)

# ---

foo = {"key": "value"}
original = foo.copy()

with patch.dict(foo, {"newkey": "newvalue"}, clear=True):
    assert foo == {"newkey": "newvalue"}

assert foo == original

# ---

mock = MagicMock()
mock.__str__.return_value = "foobarbaz"
print(str(mock))
mock.__str__.assert_called_with()

# ---

mock = Mock()
mock.__str__ = Mock(return_value="wheeeeeee")
print(str(mock))
