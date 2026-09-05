import timer
import random
import matplotlib.pyplot as plt

def create_random_list(N):
    return random.sample(range(1, N+1), N)

x = []
ypython = []
ystupid = []

for order in range(2,5):
    Nelements = 10**order
    x.append(Nelements)
    # Method 1:  Python built-in sort
    # start timer
    a = create_random_list(Nelements)
    print(a)
    clock = timer.Timer()
    clock.start()
    a.sort()
    ypython.append(clock.stop())
    print(a)

    # start timer
    a = create_random_list(Nelements)
    print(a)
    clock = timer.Timer()
    clock.start()
    for i in range(Nelements):
        for j in range(Nelements):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    ystupid.append(clock.stop())
    print(a)

fig = plt.figure()
plt.plot(x, ypython)
plt.plot(x, ystupid)
plt.xlabel("N")
plt.ylabel("Time")
plt.title("Timer")
plt.grid()
plt.yscale("log")
plt.xscale("log")

plt.show()

