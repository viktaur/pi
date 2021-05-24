# def set_numpy_decimal_places(places, width=0):
#     return '{0:' + str(width) + '.' + str(places) + 'f}'

n = eval(input("Number of iterations: "))

pi = 3

for i in range(n):
    a = 2 * (i + 1)

    if i % 2 == 0:
        pi += 4 / ((a) * (a+1) * (a+2))
    else:
        pi -= 4 / ((a) * (a+1) * (a+2))

print(pi)