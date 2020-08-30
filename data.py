import settings, pickle, os, sys

class Data:
    def add(self, inputs, result):
        fileData = self.get()
        sampleDict = dict()
        sampleDict['inputs'] = inputs
        resultEncoded = [0 for i in range(10)]
        resultEncoded[int(result)] = 1
        sampleDict['result'] = resultEncoded
        fileData.append(sampleDict)

        filehandler = open(settings.data_file, 'wb')
        pickle.dump(fileData, filehandler)
        filehandler.close()
    def get(self):
        unserialisedDict = []
        if os.path.exists(settings.data_file) and os.path.getsize(settings.data_file) > 0:
            file = open(settings.data_file, 'rb')
            unserialisedDict = pickle.load(file)
            file.close()
        else:
            open(settings.data_file, 'a').close()
        return unserialisedDict

if __name__ == '__main__':
    pass
