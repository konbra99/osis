from algorytm import algorithm
import numpy as np
from timeit import default_timer as timer
import os


class Statistic:
    def __init__(self, results):
        results = np.array(results)
        self.minValue = results.min()
        self.maxValue = results.max()
        self.meanValue = np.mean(results)
    
    def __str__(self):
        return f'{self.minValue};{self.meanValue};{self.maxValue}'


def measuredAlgorithm(file):
    before = timer()
    makespan = algorithm(file)
    after = timer()
    return makespan, after - before


def runTests(testsFolder):
    for _, _, files in os.walk(testsFolder):
        makespans = []
        times = []
        for file in files:
            makespan, time = measuredAlgorithm(file)
            makespans.append(makespan)
            times.append(time)
        
        print(f'{testsFolder};{Statistic(makespan)};{Statistic(times)}')
