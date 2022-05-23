import localsolver
import sys


class Parameters:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.p = []


def solverAlgorithm(file):
    global parameters
    parameters = Parameters()
    buildparametersFromFile(file)
    with localsolver.LocalSolver() as localSolver:
        return solve(localSolver)


def buildparametersFromFile(filename):
    fileIterator = getFileIterator(filename)
    parameters.n = next(fileIterator)
    parameters.m = next(fileIterator)
    for _ in range(parameters.m):
        machineTimes = [next(fileIterator) for _ in range(parameters.n)]
        parameters.p.append(machineTimes)


def getFileIterator(filename):
    with open(filename) as f:
        return iter([int(elem) for elem in f.read().split()])


def timesToModelArray(model):
    return [model.array(parameters.p[i]) for i in range(parameters.m)]


def solve(localSolver):
    makespan = constructModel(localSolver)
    localSolver.param.iteration_limit = 3
    localSolver.param.verbosity = 0
    localSolver.solve()
    return makespan.value


def constructModel(localSolver):
    model = localSolver.model

    jobs = model.list(parameters.n)
    model.constraint(model.eq(model.count(jobs), parameters.n))
    parameters.p = [model.array(parameters.p[m]) for m in range(parameters.m)]

    end = [None] * parameters.m
    firstSelector = model.lambda_function(
        lambda i, prev: prev + parameters.p[0][jobs[i]])
    end[0] = model.array(model.range(0, parameters.n), firstSelector)

    for machine in range(1, parameters.m):
        current = machine
        endSelector = model.lambda_function(lambda i, prev:
                                            model.max(prev, end[current - 1][i]) +
                                            parameters.p[current][jobs[i]])
        end[machine] = model.array(model.range(0, parameters.n), endSelector)

    makespan = end[parameters.m - 1][parameters.n - 1]
    model.minimize(makespan)
    model.close()

    return makespan


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        print('wynik', solverAlgorithm(sys.argv[1]))
    else:
        print("Usage: python etap2perm.py inputFile")
