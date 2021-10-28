# noinspection PyUnresolvedReferences
import json as jsonlib


class NotFoundInJsonDB(Exception):
    """Exception raised for errors in the JSON lookup
    """

    def __init__(self, error_name, message="Cannot find in json file. Check for corruption or empty file."):
        self.error_name = error_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.error_name} -> {self.message}'


def printInfo(message):
    print("[JSONParse] {0}".format(message))


class JSONReaderWriter:
    """Reads and writes JSON"""

    def __init__(self, json_file):
        self.temp = None
        self.file = open(json_file, "r+")
        self.parsedJsonList = None

    def readFile(self):
        self.parsedJsonList = jsonlib.load(self.file)

    def writeFile(self):
        self.file.truncate(0)
        jsonlib.dump(self.parsedJsonList, self.file, ensure_ascii=True, indent=4)

    def closeFile(self):
        self.file.close()

    def debugPrintList(self):
        printInfo(str(self.parsedJsonList))

    def retrieveFromJSON(self, to_be_retrieved):
        self.temp = self.parsedJsonList.get(to_be_retrieved)
        if self.temp:
            return self.temp
        else:
            raise NotFoundInJsonDB(to_be_retrieved)
