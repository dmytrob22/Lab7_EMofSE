import matplotlib.pyplot as plt


class Plotter:
    @staticmethod
    def plot_frequencies(observed):
        plt.bar(range(0, 21), observed, color="blue", alpha=0.7, label="Observed")
        plt.xlabel("Values")
        plt.ylabel("Frequencies")
        plt.title("Frequencies of Input Sample")
        plt.legend()
        plt.show()
