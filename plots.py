from turtle import color
import pandas
import matplotlib.pyplot as plt


def plotData(dataAlgo, dataSolver, title):
    parameter = dataAlgo['parameter']
    plot(parameter, dataAlgo, dataSolver, 'time', f'Czas [s] - {title}', f'algo_time_{title}.png')
    plot(parameter, dataAlgo, dataSolver, 'makespan', f'Makespan - {title}', f'algo_span_{title}.png')


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
    plt.plot(parameter, minAlgo, label='Minimum Algorithm', color='skyblue')
    plt.plot(parameter, avgAlgo, label='Average Algorithm', color='royalblue')
    plt.plot(parameter, maxAlgo, label='Maximum Algorithm', color='darkblue')
    #plt.plot(parameter, minSolver, label='Minimum Solver', color='palegreen')
    #plt.plot(parameter, avgSolver, label='Average Solver', color='limegreen')
    #plt.plot(parameter, maxSolver, label='Maximum Solver', color='darkgreen')
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


def compareTypes(size, col, value):
    plt.clf()
    titleSize = 'Grupa długa, kolumna' if size == 'long' else 'Grupa krótka, kolumna'
    plt.title(f'{titleSize} {value}')
    plotGroup('algo', size, col, value)
    plotGroup('solver', size, col, value)
    plt.legend()
    plt.savefig(f'{size}_{value}_{col}_{value}.png')


def compareSizes(type, col, value):
    plt.clf()
    titleType = 'Algorytm NEH, kolumna' if type == 'algo' else 'Solver, kolumna'
    plt.title(f'{titleType} {value}')
    plotGroup(type, 'short', col, value)
    plotGroup(type, 'long', col, value)
    plt.legend()
    plt.savefig(f'{type}_{value}_{col}_{value}.png')


def plotGroup(type, size, col, value):
    print(f'--- {type} -- {size} ------')
    data = pandas.read_csv(f'{type}_group_{size}.csv', sep=';')
    print(data.groupby(col).mean()[value])
    data.groupby(col).mean()[value].plot(x=col, y=value, label=f'{type} {size}')


def meanInfo(file):
    print(f'--- mean -- {file} ----')
    vals = ['avg_time', 'avg_makespan']
    print(pandas.read_csv(file, sep=';')[vals].mean())

if __name__ == '__main__':
    cols = ['n', 'm']
    vals = ['avg_time', 'avg_makespan']
    meanInfo('algo_group_short.csv')
    meanInfo('solver_group_short.csv')
    meanInfo('algo_group_long.csv')
    meanInfo('solver_group_long.csv')
    for col in cols:
        for val in vals:
            compareTypes('short', col, val)
            compareTypes('long', col, val)
    for col in cols:
        for val in vals:
            compareSizes('algo', col, val)
            compareSizes('solver', col, val)
    # singleParameterPlot('wyniki_algo.csv', 'wyniki_solver.csv')
