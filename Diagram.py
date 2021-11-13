from matplotlib import pyplot as plt

class Diagram:

    def show(self, result_list, result_label = ["Правильно", "Неверно"]):
        plt.figure(figsize =(10, 7))
        plt.pie(result_list, labels = result_label)
        plt.show()
