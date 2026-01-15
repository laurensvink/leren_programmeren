import random

soorten = ["harten", "klaveren", "schoppen", "ruiten"]
waarden = ["2","3","4","5","6","7","8","9","10","boer","vrouw","heer","aas"]
deck = []

for s in soorten:
    for w in waarden:
        deck.append(s + " " + w)

deck.append("joker")
deck.append("joker")

random.shuffle(deck)

for i in range(7):
    print("kaart", i + 1, ":", deck[i])

print()
print("deck (" + str(len(deck) - 7) + " kaarten):", deck[7:])
