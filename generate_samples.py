import random, sys, copy

from data import Data

data = Data()
one = data.get()
print(one)
sys.exit()


samplesWithNoise = []

for i in range(5000):
    newSample = copy.deepcopy(one)
    #newSample['inputs'] = one
    #newSample['result'] = [0,1,0,0,0,0,0,0,0,0]

    for j in range(20):
        rand = random.randrange(0, 400)
        newSample['inputs'][rand] = 1

    samplesWithNoise.append(newSample)

    # k = 0
    # for i in range(20):
    #     line = ''
    #     for j in range(20):
    #         line = line + ' ' + str(newSample['inputs'][k])
    #         k = k + 1
    #     print(line)
    #
    # print()




