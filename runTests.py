import sys
from algorytm import algorithm
from etap2perm import solverAlgorithm
import numpy as np
from timeit import default_timer as timer
import localsolver
import os


class Statistic:
    def __init__(self, results):
        results = np.array(results)
        self.minValue = results.min()
        self.maxValue = results.max()
        self.meanValue = np.mean(results)

    def __str__(self):
        return f'{self.minValue};{self.meanValue};{self.maxValue}'


def measureTime(funciton):
    def measured(*args, **kwargs):
        before = timer()
        result = funciton(*args, **kwargs)
        after = timer()
        return result, after - before

    return measured


def runTests(testsFolder, algo='algo'):
    testedAlgorithm = algorithm if algo == 'algo' else solverAlgorithm
    testedAlgorithm = measureTime(testedAlgorithm)
    for _, _, files in os.walk(testsFolder):
        makespans = []
        times = []
        for file in files:

            makespan, time = testedAlgorithm(f'{testsFolder}/{file}')
            makespans.append(makespan)
            times.append(time)

        type = ';'.join(testsFolder.split('\\')[-1].split('_'))
        return f'{type};{Statistic(makespans)};{Statistic(times)}'


def runGroupedTests(algo='algo'):
    short = []
    for root, dirs, _ in os.walk('short_tests'):
        for dir in dirs:
            short.append(runTests(os.path.join(root, dir), algo))

    long = []
    for root, dirs, _ in os.walk('long_tests'):
        for dir in dirs:
            long.append(runTests(os.path.join(root, dir), algo))
    
    return short, long


def main(algo, outFile):
    algo = sys.argv[1]
    jobs = [5, 10, 20, 30, 40, 50]
    machines = [5, 10, 20, 30, 40, 50]
    results = []
    #for j in jobs:
    #    results.append(runTests(f'jobs_{j}', algo))
    #for m in machines:
    #    results.append(runTests(f'machines_{m}', algo))
    s, l = runGroupedTests(algo)
    with open(outFile+'_short.csv', 'w') as f:
        f.write('n;m;min_makespan;avg_makespan;max_makespan;min_time;avg_time;max_time\n')
        for result in s:
            f.write(result + '\n')
    with open(outFile+'_long.csv', 'w') as f:
        f.write('n;m;min_makespan;avg_makespan;max_makespan;min_time;avg_time;max_time\n')
        for result in l:
            f.write(result + '\n')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
