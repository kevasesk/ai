from pybrain.tools.shortcuts import buildNetwork #network
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet #dataset
from pybrain.supervised.trainers import BackpropTrainer #traning algorithm
from os import listdir
from os.path import isfile, join
from PIL import Image
from data import Data

import numpy as np
import os, settings, pickle, sys
import matplotlib.pylab as plt


class Network:

    inputs = []
    result = None
    ds = None
    net = None

    def initNetwork(self):
        if self.ds is None:
            self.loadNetworkFromFile()
            if self.ds is None:
                self.ds = SupervisedDataSet(settings.inputs, settings.outputs)
                self.net = buildNetwork(settings.inputs, settings.hidden_neurons1,
                                        settings.outputs,
                                        bias=True, hiddenclass=TanhLayer)
                self.saveNetworkToFile()

    def loadNetworkFromFile(self):
        if os.path.exists(settings.memory_file) and os.path.getsize(settings.memory_file) > 0:
            file = open(settings.memory_file, 'rb')
            unserialisedDict = pickle.load(file)
            self.ds = unserialisedDict['ds']
            self.net = unserialisedDict['net']
            file.close()
        else:
            open(settings.memory_file, 'a').close()

    def saveNetworkToFile(self):
        serialisedDict = dict()
        serialisedDict['ds'] = self.ds
        serialisedDict['net'] = self.net
        filehandler = open(settings.memory_file, 'wb')
        pickle.dump(serialisedDict, filehandler)
        filehandler.close()

    def addSample(self, inputs, result):
        self.initNetwork()
        inputsEncoded = self.convertInputs(inputs)
        resultEncoded = [0 for i in range(10)]
        resultEncoded[int(result)] = 1
        self.ds.addSample(inputsEncoded, resultEncoded)
        self.saveNetworkToFile()

    def activate(self, field):
        self.initNetwork()
        inputs = self.convertInputs(field)
        trainer = BackpropTrainer(self.net, self.ds)

        iterations = []
        errors = []
        for iteration in range(1, settings.iterations):
            iterations.append(iteration)
            errors.append(trainer.train())
        # далее вызываю метод activate с входными значениями  - это получение ответа от заданных параметров
        networkResult = self.net.activate(inputs)
        print(self.formatNumbersForForm(networkResult))
        return self.formatNumbersForForm(networkResult)

    def convertInputs(self, inputs):
        result = []
        for row in inputs:
            result += row

        return result
    def formatNumbersForForm(self, results):
        formatedResults = []
        for res in results:
            if res < 0:
                formatedResults.append(0)
            if res >= 0 and res < 1:
                formatedResults.append(int(res * 100))
            if res > 1:
                formatedResults.append(0)
        return formatedResults

if __name__ == '__main__':
    network = Network()
    network.loadSamples()
    pass

