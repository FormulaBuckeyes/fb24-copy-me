print("hello world")

#X marks the spot
#I spent more time on this than i'd like to admit
for i in range (8):
    for j in range (8):
        if (i == j or  8-(j+1) == i):
            print("*", end= "")
        else:
            print("     ", end= "")
    print("\n")

