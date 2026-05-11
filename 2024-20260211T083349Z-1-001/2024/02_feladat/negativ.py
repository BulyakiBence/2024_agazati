import random
def negativ(szam):
    if szam < 0:
        return True
    else:
        return False
negativak = []
for i in range(100):
    i = random.randint(-50, 50)
    if negativ(i):
        negativak.append(i)
print(f"ennyi negatív szerepelt köztük {len(negativak)}")