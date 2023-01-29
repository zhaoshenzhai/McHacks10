import matplotlib.pyplot as plt
import numpy as np


def gen_pie(vibe):
    plt.pie(vibe, labels=["Positive", "Neutral", "Negative"], autopct='%.0f%%')
    plt.show()
    plt.close()


def gen_hist(cpds):
    cpdsFiltered = []
    for cpd in cpds:
        if cpd != 0:
            cpdsFiltered.append(cpd)

    plt.hist(cpdsFiltered, bins=50)
    plt.show()
    plt.close()


def compare(vibe1, vibe2, sr1, sr2):
    x = np.arange(3)
    width = 0.2

    # plot data in grouped manner of bar type
    plt.bar(x - 0.2, vibe1, width, color='cyan')
    plt.bar(x, vibe2, width, color='orange')
    plt.xticks(x, ["positive", "negative", "neutral"])
    plt.xlabel("Sentiments")
    plt.ylabel("Scores")
    plt.title(sr1 + " vs " + sr2)
    plt.legend([sr1, sr2])
    plt.show()
    plt.close()
