from time import time, sleep
import threading

start = time()


def race(name, times):
    print("Runner", name, "starts running!")
    sleep(times)
    print(name, "finished")


race("John", 5)
race("Mike", 7)

end = time()

print(f"\nThe relay team time is {end - start:.2f} seconds\n")


start2 = time()

t1 = threading.Thread(target=race, args=("John", 5))
t2 = threading.Thread(target=race, args=("Mike", 7))

t1.start()
t2.start()

t1.join()
end1 = time()
t2.join()
end2 = time()

print(f"\nJohn time is {end1 - start2:.2f} seconds")
print(f"Mike time is {end2 - start2:.2f} seconds")


time1 = end - start
time2 = end2 - start2

print(f"\nThe race lasted {time1 - time2:.2f} seconds less than the relay!")
print(f"It means race is {time1 / time2:.1f} times faster than relay race!")
