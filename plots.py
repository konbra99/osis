import pandas
import matplotlib.pyplot as plt


def plotData(data, title):
    parameter = data['parameter']
    plotMakespan(parameter, data, title)
    plotTime(parameter, data, title)


def plotMakespan(parameter, data, title):
    minMakespan = data['min_makespan']
    avgMakespan = data['avg_makespan']
    maxMakespan = data['max_makespan']
    plt.clf()
    plt.title(f'Makespan przy {title}')
    plt.plot(parameter, minMakespan, label='Minimum')
    plt.plot(parameter, avgMakespan, label='Average')
    plt.plot(parameter, maxMakespan, label='Maximum')
    plt.legend()
    plt.savefig(title + ' makespan.png')


def plotTime(parameter, data, title):
    minTime = data['min_time']
    avgTime = data['avg_time']
    maxTime = data['max_time']
    plt.clf()
    plt.title(f'Czas przetwarzania (w sekundach) dla {title}')
    plt.plot(parameter, minTime, label='Minimum')
    plt.plot(parameter, avgTime, label='Average')
    plt.plot(parameter, maxTime, label='Maximum')
    plt.legend()
    plt.savefig(title + ' czas.png')


def singleParameterPlot(file):
    results = pandas.read_csv('grupy.csv', sep=';')
    print(results)

    randomMachines = results[:6]
    randomJobs = results[6:]

    plotData(randomMachines, 'losowej liczby maszyn')
    plotData(randomJobs, 'losowej liczby zadań')



if __name__ == '__main__':
    short = pandas.read_csv('short.csv')
    long = pandas.read_csv('long.csv')
    
