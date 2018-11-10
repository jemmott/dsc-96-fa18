import random

def makeWidgets(distribution):

    if distribution == "A":
        return int(random.random()>0.5002)
    elif distribution == "B":
        return int(random.random()>0.5006)
    elif distribution == "C":
        return int(random.random()>0.36)
    else:
        print('makeWidgets must include distribution parameter equal to "A" or "B" o "C" ')