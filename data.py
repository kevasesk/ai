import settings, pickle, os

class Data:
    def add(self, dataItem):
        fileData = self.get()
        fileData.append(dataItem)

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
