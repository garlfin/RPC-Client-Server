import res.database.res.json as JSON

jsonRead = JSON.jsonReaderWriter("c:/Users/0442246/OneDrive - Miami-Dade County Public Schools/Desktop/bbfl/rpc/py/res/database/res/testfile.json")
jsonRead.readFile()
jsonRead.writeFile()
jsonRead.closeFile()