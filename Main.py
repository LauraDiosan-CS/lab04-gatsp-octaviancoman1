

from AI.l4try.GA import GA
from AI.l4try.dataReading import readNet2, readNet3


def run():
    while True:
        print("1. RUN: \n")
        print("0. Exit\n")

        cmd = input()
        if cmd == "1":
            print("introduceti numele fisierului de unde se citesc datele: \n")
            filename = input()
            if (filename != ""):
                print("marimea populatiei = \n")
                populationSize = int(input())
                print("numarul de generatii = \n")
                noGenerations = int(input())
                graph = readNet3(filename)
                ga = GA(populationSize, graph)
                ga.initialization()
                #ga.evaluation()
                contor = 0
                gen = contor + 1
                contor +=1
                best = ga.bestChromosome()
                print("generation " + str(gen) + " " + str(best.repres) + " fitness " + str(best.fitness))
                while (contor < noGenerations):
                    ga.oneGeneration()
                    #ga.newPopulation()
                    best = ga.bestChromosome()
                    # print(best.fitness)
                    gen = contor + 1
                    print("generation " + str(gen) + " " + str(best.repres) + " fitness "+str(best.fitness))
                    contor += 1

        else:
            break


run()
