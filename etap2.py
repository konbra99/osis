import localsolver
import sys


class Parameters:
    n = 0
    m = 0
    p = []


def solverAlgorithm(file):
    buildParametersFromFile(file)
    with localsolver.LocalSolver() as localSolver:
        Parameters.p = timesToModelArray(localSolver.model)
        return solve(localSolver)


def buildParametersFromFile(filename):
    fileIterator = getFileIterator(filename)
    Parameters.n = next(fileIterator)
    Parameters.m = next(fileIterator)
    for _ in range(Parameters.m):
        machineTimes = [next(fileIterator) for _ in range(Parameters.n)]
        Parameters.p.append(machineTimes)


def getFileIterator(filename):
    with open(filename) as f:
        return iter([int(elem) for elem in f.read().split()])


def timesToModelArray(model):
    return [model.array(Parameters.p[i]) for i in range(Parameters.m)]


def solve(localSolver):
    _, makespan = constructModel(localSolver)
    localSolver.param.time_limit = 5
    localSolver.solve()
    return makespan.value


def constructModel(localSolver):
    model = localSolver.model

    jobs = [model.list(Parameters.n) for _ in range(Parameters.m)]
    for i in range(Parameters.m):
        model.constraint(model.eq(model.count(jobs[i]), Parameters.n))

    C = [None] * Parameters.m
    C[0] = firstMachineFinishTimes(model, jobs)
    for i in range(1, Parameters.m):
        C[i] = nextMachineFinishTimes(model, jobs, C, i)

    makespan = C[Parameters.m - 1][Parameters.n - 1]
    model.minimize(makespan)
    model.close()

    return jobs, makespan


def firstMachineFinishTimes(model, jobs):
    def firstMachineFinish(j, previous):
        return previous + Parameters.p[0][jobs[0][j]]

    selector = model.lambda_function(firstMachineFinish)
    return model.array(model.range(0, Parameters.n), selector)


def nextMachineFinishTimes(model, jobs, C, i):
    def nextMachineFinish(j, previous):
        previousIndex = model.sum([k * (jobs[i - 1][k] == jobs[i][j]) for k in range(Parameters.n)])
        return model.max(previous, C[i - 1][previousIndex]) + Parameters.p[i][jobs[i][j]]

    selector = model.lambda_function(nextMachineFinish)
    return model.array(model.range(0, Parameters.n), selector)


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solverAlgorithm(sys.argv[1])
    else:
        print("Usage: python flowshop.py inputFile [outputFile]")
