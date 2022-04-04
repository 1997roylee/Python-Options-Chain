import json

def toJSON(filename, data):
    outFile = open(filename, "w")
    outFile.write(str(data))
    outFile.close()
    return True