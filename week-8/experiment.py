import random

def makeWidgets(distribution):

    if distribution == "A":
        return random.gauss(2, 0.5)
    elif distribution == "B":
        return random.gauss(2.2, 0.5)
    elif distribution == "C":
        return random.gauss(1.5,10)
    else:
        print('getSample must include distribution parameter equal to "A" or "B"')
        