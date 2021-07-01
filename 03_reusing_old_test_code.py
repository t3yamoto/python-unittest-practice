import unittest


def testSomething():
    something = makeSomething()
    assert something.name is not None


def makeSomethingDB():
    print("makeSomethingDB")


def deleteSomethingDB():
    print("deleteSomethingDB")


class makeSomething:
    def __init__(self):
        self.name = "Name"


if __name__ == "__main__":
    testcase = unittest.FunctionTestCase(
        testSomething, setUp=makeSomethingDB, tearDown=deleteSomethingDB
    )
    testcase.run()
