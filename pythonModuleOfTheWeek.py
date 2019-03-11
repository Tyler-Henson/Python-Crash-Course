"""
Problem 9-15 of Python Crash Course
"""
import queue as q

my_que = q.Queue()

for i in range(0, 10):
    my_que.put(i*10)
    print('1', end=' ')

while not my_que.empty():
    print(my_que.get(), end=' ')

