import numpy as np
from copy import copy
import sys


class Parameters:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.p = []

    def __str__(self):
        return str(self.p)


def buildParametersFromFile(filename):
    fileIterator = getFileIterator(filename)

    parameters = Parameters()
    parameters.n = next(fileIterator)
    parameters.m = next(fileIterator)
    processTimes = []
    for _ in range(parameters.m):
        machineTimes = [next(fileIterator) for _ in range(parameters.n)]
        processTimes.append(machineTimes)
    parameters.p = np.array(processTimes)

    return parameters


def getFileIterator(filename):
    with open(filename) as f:
        return iter([int(elem) for elem in f.read().split()])


def calculateMakespan(parameters, permutation, n=-1):
    times = []
    time = 0

    if n == -1:
        n = parameters.n

    for j in range(0, n):
        time += parameters.p[0][permutation[j]]
        times.append(time)

    for i in range(1, parameters.m):
        oldTimes = copy(times)
        time = oldTimes[0] + parameters.p[i][permutation[0]]
        times = [time]
        for j in range(1, n):
            time = max(time, oldTimes[j]) + parameters.p[i][permutation[j]]
            times.append(time)

    return times[-1]


def summedJobTimes(parameters):
    sums = []
    for j in range(parameters.n):
        sum = 0
        for i in range(parameters.m):
            sum += parameters.p[i][j]

        sums.append(sum)

    return np.array(sums)


def sortTimes(sums):
    return np.argsort(sums)[::-1][:len(sums)]


def insertionSort(parameters, sorted):
    sequence = [sorted[0]]

    for j in range(1, parameters.n):
        job = sorted[j]
        minSpan = sys.maxsize
        for place in range(0, j + 1):
            temporary = copy(sequence)
            temporary.insert(place, job)
            span = calculateMakespan(parameters, temporary, n=j+1)
            if span < minSpan:
                minSpan = span
                nextSequence = temporary
        sequence = nextSequence

    return sequence, minSpan


def algorithm(file, verbose=False):
    parameters = buildParametersFromFile('instances/example.txt')
    sums = summedJobTimes(parameters)
    sortedTimes = sortTimes(sums)
    sequence, makespan = insertionSort(parameters, sortedTimes)
    if verbose:
        print(f'sequence: {sequence}\nmakspan: {makespan}')
    
    return makespan
