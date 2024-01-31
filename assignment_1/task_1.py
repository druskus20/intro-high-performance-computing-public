#!/usr/bin/env python

import time
import numpy as np
from timeit import default_timer as timeit_timer

def timer_time():
    return time.time()
def timer_timeit():
    return timeit_timer()
def timer_ns():
    return time.time_ns()

def checktick(time_function):
    M = 200
    timesfound = np.empty((M,))
    for i in range(M):
        t1 = time_function()
        t2 = time_function()
        while (t2 - t1) < 1e-16: # if zero then we are below clock granularity, retake timing
            t2 = time_function()
        t1 = t2 # this is outside the loop
        timesfound[i] = t1 # record the time stamp
        minDelta = 1000000
        Delta = np.diff(timesfound) # it should be cast to int only when needed
        minDelta = Delta.min()
    return minDelta

def main(): 
    print(f"Clock granularity timer_ns: {checktick(timer_ns) / 1.0e9} [s]")
    print(f"Clock granularity timer_time: {checktick(timer_time)} [s]")
    print(f"Clock granularity timer_timeit: {checktick(timer_timeit)} [s]")

if __name__ == "__main__":
    main()
