from collections import Counter
import numpy as np
from matplotlib import pyplot as plt
import math

num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,
               13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,
               9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,
               7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,
               5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,
               4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,
               2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def sum_of_squares(v):
    return np.dot(v,v)

def ex1():
    friends_count=Counter(num_friends)
    xs=range(101)
    ys=[friends_count[x] for x in xs]
    plt.bar(xs,ys)
    plt.axis([0,101,0,25])
    plt.xlabel("# of friends")
    plt.ylabel("# of people")
    plt.title("friends statics shown")
    plt.show()

def ex2():
    num_points=len(num_friends)
    largest_value=max(num_friends)  #100
    smallest_value=min(num_friends) #1
    sorted_value=sorted(num_friends)

ex1()
