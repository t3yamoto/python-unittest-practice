import unittest


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget("The widget")

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50), "incorrect default size")

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150), "wrong size after resize")

    def tearDown(self):
        self.widget.dispose()


class Widget:
    def __init__(self, name):
        self.name = name
        self.height = 50
        self.width = 50

    def resize(self, height, width):
        self.height = height
        self.width = width

    def size(self):
        return self.height, self.width

    def dispose(self):
        print("Disposed")


if __name__ == "__main__":
    unittest.main()
