import pandas
import matplotlib.pyplot as plt


def plotData(dataAlgo, dataSolver, title):
    parameter = dataAlgo['parameter']
    plot(parameter, dataAlgo, dataSolver, 'time', f'Czas [s] - {title}', f'Czas [s] - {title}.png')
    plot(parameter, dataAlgo, dataSolver, 'makespan', f'Makespan - {title}', f'Makespan - {title}.png')


def plot(parameter, dataAlgo, dataSolver, col, title, file):
    min = f'min_{col}'
    avg = f'avg_{col}'
    max = f'max_{col}'
    minAlgo = dataAlgo[min]
    avgAlgo = dataAlgo[avg]
    maxAlgo = dataAlgo[max]
    minSolver = dataSolver[min]
    avgSolver = dataSolver[avg]
    maxSolver = dataSolver[max]
    
    plt.clf()
    plt.title(title)
    plt.plot(parameter, minAlgo, label='Minimum Algorithm')
    plt.plot(parameter, avgAlgo, label='Average Algorithm')
    plt.plot(parameter, maxAlgo, label='Maximum Algorithm')
    plt.plot(parameter, minSolver, label='Minimum Solver')
    plt.plot(parameter, avgSolver, label='Average Solver')
    plt.plot(parameter, maxSolver, label='Maximum Solver')
    plt.legend()
    plt.savefig(file)


def singleParameterPlot(fileAlgo, fileSolver):
    resultsAlgo = fileResults(fileAlgo, '-- Algo -----')
    resultsSolver = fileResults(fileSolver, '-- Solver ----')

    plotData(resultsAlgo[0], resultsSolver[0], 'losowa liczba maszyn')
    plotData(resultsAlgo[1], resultsSolver[1], 'losowa liczba zadań')


def fileResults(file, text):
    results = pandas.read_csv(file, sep=';')
    print(text)
    print(results)

    randomMachines = results[results['type'] == 'jobs']
    randomJobs = results[results['type'] == 'machines']
    return randomMachines, randomJobs


if __name__ == '__main__':
    # short = pandas.read_csv('short.csv')
    # long = pandas.read_csv('long.csv')
    singleParameterPlot('wyniki_algo.csv', 'wyniki_solver.csv')
