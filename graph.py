import matplotlib.pyplot as plt
import entity
import entityManager

graphed = False
data = [[] for i in range(len(entity.types))]

def dataUpdate():
    for i in range(len(entityManager.counts)):
        data[i].append(entityManager.counts[i])

def createGraph():
    global graphed
    if not graphed:
        plt.title("Entities Per Type")
        for j in range(len(data)):
            plt.plot([i for i in range(len(data[0]))], data[j])
        plt.legend([e.capitalize() for e in entity.types])
        plt.xlabel("Ticks")
        plt.ylabel("Entities")
        plt.show()
        graphed = True

