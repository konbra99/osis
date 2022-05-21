import os
import numpy as np


def saveTestData(folder, number_of_jobs, number_of_machines, array):
    with open(f'{folder}/m_{number_of_machines}_n_{number_of_jobs}', "w+") as file:
        file.write(str(number_of_jobs) + " " + str(number_of_machines))
        for jobs in array:
            file.write('\n')
            for job in jobs:
                file.write(str(job) + " ")


def generateRandomJobs(folder, number_of_machines, pmin, pmax):
    number_of_jobs = np.random.randint(
        pmin, pmax, (number_of_machines, np.random.randint(5, 50)))
    saveTestData(folder, len(
        number_of_jobs[0]), number_of_machines, number_of_jobs)


def createRandomJobsFolder(name, machines, repeat=10):
    os.mkdir(name)
    for _ in range(repeat):
        generateRandomJobs(name, machines, 1, 100)


def createRandomJobsExperiment():
    machineSizes = [5, 10, 20, 30, 40, 50]
    for machines in machineSizes:
        createRandomJobsFolder(f'machines_{machines}', machines)


def generateRandomMachines(folder, number_of_jobs, pmin, pmax):
    number_of_machines = np.random.randint(
        pmin, pmax, (np.random.randint(1, 500), number_of_jobs))
    saveTestData(folder, number_of_jobs, len(
        number_of_machines), number_of_machines)


def createRandomMachinesFolder(name, jobs, repeat=10):
    os.mkdir(name)
    for _ in range(repeat):
        generateRandomMachines(name, jobs, 1, 100)


def createRandomMachinesExperiment():
    jobSizes = [5, 10, 20, 30, 40, 50]
    for jobs in jobSizes:
        createRandomMachinesFolder(f'jobs_{jobs}', jobs)


if __name__ == '__main__':
    createRandomJobsExperiment()
    createRandomMachinesExperiment()
