from pybrain.tools.shortcuts import buildNetwork #network
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet #dataset
from pybrain.supervised.trainers import BackpropTrainer #traning algorithm


import matplotlib.pylab as plt
#import numpy as np

ds = SupervisedDataSet(15, 10)

one = (
    0, 0, 1,
    0, 0, 1,
    0, 0, 1,
    0, 0, 1,
    0, 0, 1
)
oneResult = (
    0,1,0,0,0,0,0,0,0,0,0
)
#ds.addSample((0, 0), (0,))
#ds.addSample((0, 1), (1,))
#ds.addSample((1, 0), (1,))
#ds.addSample((1, 1), (0,))

#print(ds['input'])
#print(ds['target'])

net = buildNetwork(15, 7, 7, 10, bias=True, hiddenclass=TanhLayer)

# указываем какую сеть и какими данными обучать
trainer = BackpropTrainer(net, ds)

iterations = []
errors = []
for iteration in range(1, 1000):
    iterations.append(iteration)
    errors.append(trainer.train())
# далее вызываю метод activate с входными значениями  - это получение ответа от заданных параметров
print(net.activate((2, 1)))

plt.plot(iterations, errors)
plt.xlabel('iterations')
plt.ylabel('errors')
#plt.show()

# обучаем до сходимости(тут не совсем понял, но предположил, что обучает пока значение ошибки не будет удовлетворительным)
#print(trainer.trainUntilConvergence())


