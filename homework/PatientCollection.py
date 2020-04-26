import os
from homework.Log import collectinfo, collecterr
from homework.Patient import Patient


class PatientCollection:
    pat = Patient()

    def __init__(self, path_to_file):
        if not os.path.isfile(path_to_file):
            collecterr.error("File not accessible")
        self.filepath = path_to_file
        collectinfo.info("File exist")

    def __iter__(self):
        fileBytePos = 0
        while True:
            inFile = open(self.filepath)
            inFile.seek(fileBytePos)
            data = inFile.readline()
            if data[:len(data) - 2] == '\n':
                data = data[:len(data) - 2]
            if not data:
                collecterr.warning("Argument in limit was greater than Collections size, that's why we printed it all.")
                inFile.close()
                return
            self.pat.create(*data.split(' '))
            yield self.pat
            fileBytePos = inFile.tell()
            inFile.close()

    def limit(self, num):
        if num < 1:
            collecterr.error("Argument in limit should be >1.")
            return
        counter = 0
        fileBytePos = 0
        while True:
            inFile = open(self.filepath)
            inFile.seek(fileBytePos)
            data = inFile.readline()
            if data[:len(data) - 2] == '\n':
                data = data[:len(data) - 2]
            if not data or counter == num:
                collecterr.warning("Argument in limit was greater than Collections size, that's why we printed it all.")
                inFile.close()
                return
            self.pat.create(*data.split(' '))
            yield self.pat
            fileBytePos = inFile.tell()
            inFile.close()

