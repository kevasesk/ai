from pybrain.tools.shortcuts import buildNetwork #network
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet #dataset
from pybrain.supervised.trainers import BackpropTrainer #traning algorithm
import numpy as np
import settings

import matplotlib.pylab as plt
#import numpy as np


class Network:

    inputs = []
    result = None
    ds = None
    net = None

    def network(self):
        if Network.ds is None :
            Network.ds = SupervisedDataSet(settings.inputs, settings.outputs)
            Network.net = buildNetwork(settings.inputs, settings.hidden_neurons1, settings.hidden_neurons2, settings.outputs,
                               bias=True, hiddenclass=TanhLayer)

            #should add samples
            Network.ds.addSample(Network.inputs, Network.result)
        # one = (
        #     0, 0, 1,
        #     0, 0, 1,
        #     0, 0, 1,
        #     0, 0, 1,
        #     0, 0, 1
        # )
        # oneResult = (
        #     0, 1, 0, 0, 0, 0, 0, 0, 0, 0
        # )


        # ds.addSample((0, 1), (1,))
        # ds.addSample((1, 0), (1,))
        # ds.addSample((1, 1), (0,))

        # print(ds['input'])
        # print(ds['target'])



        # указываем какую сеть и какими данными обучать
        trainer = BackpropTrainer(Network.net, Network.ds)

        iterations = []
        errors = []
        for iteration in range(1, settings.iterations):
            iterations.append(iteration)
            errors.append(trainer.train())
        # далее вызываю метод activate с входными значениями  - это получение ответа от заданных параметров
        print(Network.net.activate((2, 1)))

        plt.plot(iterations, errors)
        plt.xlabel('iterations')
        plt.ylabel('errors')
        plt.show()

        # обучаем до сходимости(тут не совсем понял, но предположил, что обучает пока значение ошибки не будет удовлетворительным)
        print(trainer.trainUntilConvergence())

    @staticmethod
    def learn(field, number):
        for i in range(len(field)):
            for j in range(len(field[0])):  #TODO wrong. only for square
                Network.inputs.append(field[i][j])

        Network.result = [0 for i in range(10)]
        Network.result[number] = 1
        Network.learn()

    @staticmethod
    def activate(field):
        for i in range(len(field)):
            for j in range(len(field[0])):  # TODO wrong. only for square
                Network.inputs.append(field[i][j])

        Network.result = [0 for i in range(10)]
        Network.get_result()

