import json

def toJSON(filename, data):
    outFile = open(filename, "w")
    # print(data);
    outFile.write(str(data))
    # json.dump(data, outFile, indent = 4)
    outFile.close()
    return True