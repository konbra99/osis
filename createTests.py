import os
import numpy as np


def saveTestData(folder, number_of_jobs, number_of_machines, array):
    with open(f'{folder}/m_{number_of_machines}_n_{number_of_jobs}', "w+") as file:
        file.write(str(number_of_jobs) + " " + str(number_of_machines))
        for jobs in array:
            file.write('\n')
            for job in jobs:
                file.write(str(job) + " ")


def generateFile(folder, number_of_jobs, number_of_machines, pmin, pmax):
    jobs = np.random.randint(
        pmin, pmax, (number_of_machines, number_of_jobs))
    saveTestData(folder, number_of_jobs, number_of_machines, jobs)


def generateRandomJobs(folder, number_of_machines, pmin, pmax):
    generateFile(folder, np.random.randint(5, 50),
                 number_of_machines, pmin, pmax)


def createRandomJobsFolder(name, machines, repeat=10):
    os.mkdir(name)
    for _ in range(repeat):
        generateRandomJobs(name, machines, 1, 100)


def createRandomJobsExperiment():
    machineSizes = [5, 10, 20, 30, 40, 50]
    for machines in machineSizes:
        createRandomJobsFolder(f'machines_{machines}', machines)


def generateRandomMachines(folder, number_of_jobs, pmin, pmax):
    generateFile(folder, number_of_jobs, np.random.randint(1, 500), pmin, pmax)


def createRandomMachinesFolder(name, jobs, repeat=10):
    os.mkdir(name)
    for _ in range(repeat):
        generateRandomMachines(name, jobs, 1, 100)


def createRandomMachinesExperiment():
    jobSizes = [5, 10, 20, 30, 40, 50]
    for jobs in jobSizes:
        createRandomMachinesFolder(f'jobs_{jobs}', jobs)


def createLengthGroup(folder, pmin, pmax):
    os.mkdir(folder)
    jobSizes = [5, 10, 20, 30, 50]
    machineSizes = [5, 10, 20]
    for n in jobSizes:
        for m in machineSizes:
            generateFile(folder, n, m, pmin, pmax)


def createGroupsExperiment():
    createLengthGroup('short_tests', 1, 10)
    createLengthGroup('long_tests', 50, 150)


if __name__ == '__main__':
    #createRandomJobsExperiment()
   # createRandomMachinesExperiment()
    createGroupsExperiment()