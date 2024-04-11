import random
score = float(input("Score.....\n>"))
max_score = float(input("Max score......\n>"))
def percentage(x, y):
    fun_result = (y / x) * 100
    return fun_result
random_number = random.randint(1, 10)
random_pick = int(input("Pick a number from 1 to 10 and if you get it right I might answer:\n>"))
if random_pick == random_number:
    print("Fine... " + str(round(percentage(max_score, score), 2)) + "%")
else:
    print("Wrong, better luck next time loser")