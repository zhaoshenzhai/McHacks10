import matplotlib.pyplot as plt

def gen_pie(vibe):
    plt.pie(vibe, labels = ["Positive", "Neutral", "Negative"], autopct='%.0f%%')
    plt.show()
    plt.close()

def gen_hist(cpds):
    cpdsFiltered = []
    for cpd in cpds:
        if cpd != 0:
            cpdsFiltered.append(cpd)
    
    plt.hist(cpdsFiltered, bins = 50)
    plt.show()
    plt.close()
