import Test

class TestSupplier:
    testList = []

    def __init__(self):
        test1 = Test('Вопрос номер 1', 'Посчитайте выражение 2 + 2', '4')
        test2 = Test('Вопрос номер 2', 'Посчитайте выражение 3 + 3', '6')
        self.testList = [test1, test2]
        pass

    def getTestList(self):
        return self.testList

