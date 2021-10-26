import json

class jsonReaderWriter:
    "Reads and writes JSON"
    def __init__(self, jsonFile):
        self.file = open(jsonFile, "r+")
        self.parsedJsonList = None
    def printInfo(self, message):
        print("[JSONParse] {0}".format(message))
    def readFile(self):
        self.parsedJsonList = json.load(self.file)
    def writeFile(self):
        self.file.truncate(0)
        json.dump(self.parsedJsonList, self.file, ensure_ascii=True, indent=4)
    def closeFile(self):
        self.file.close()
    def debugPrintList(self):
        self.printInfo(str(self.parsedJsonList))
    def retrieveClients(self):
        return self.parsedJsonList["Clients"]