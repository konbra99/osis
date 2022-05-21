import os
import numpy as np


def generateRandomMachines(number_of_jobs, pmin, pmax):
    number_of_machines = np.random.randint(
        pmin, pmax, (number_of_machines, np.random.randint(5, 50)))
    with open('gereneratedMachinesFor' + str(number_of_jobs) + '.txt', 'w+') as file:
        file.write(number_of_jobs + " " + number_of_machines)
        for jobs in number_of_machines:
            file.write('\n')
            for job in jobs:
                file.write(job)


class Parameter:
    def __init__(self, n, m):
        self.n = n
        self.m = m


def generateRandomJobs(number_of_machines, pmin, pmax):
    pass


def createTestFolder(name, parameters):
    os.mkdir(name)
    pass
