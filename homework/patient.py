import csv
import os
from homework.Descriptor import *
import logging
# from homework.config import CSV_PATH


class Patient:
    first_name = Name()
    last_name = Name()
    birth_date = Date()
    phone = Phone()
    document_type = DocType()
    document_id = DocId()
    created = False

    formatter = logging.Formatter("%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s")
    handler = logging.FileHandler('/home/alexsun8/kib/ДЗ2/python_developer_hw2/homework/Good_Logs.txt', 'a', 'utf-8')
    handlerbad = logging.FileHandler('/home/alexsun8/kib/ДЗ2/python_developer_hw2/homework/Bad_Logs.txt', 'a', 'utf-8')
    handler.setFormatter(formatter)
    # handlerbad = handler
    # handlerbad = handler2

    # logs in Patient class
    patinfo = logging.getLogger("Patient info")
    patinfo.setLevel(logging.INFO)
    patinfo.addHandler(handler)
    paterr = logging.getLogger("Patient errors")
    paterr.setLevel(logging.ERROR)
    paterr.addHandler(handlerbad)

    def __init__(self, *args):
        if len(args) == 0:
            self.created = False
            self.patinfo.debug("Empty Patient was created")
            # patinfo.info("Empty Patient was created")
            return
        elif not len(args) == 6:
            self.created = False
            self.paterr.error(
                "There shold be 6 args: first_name_, last_name_, birth_date_, phone_, document_type_, document_id_. Patient wasn't created")
            return
        # try:

        self.created = False
        self.first_name = args[0]
        self.last_name = args[1]
        self.birth_date = args[2]
        self.phone = args[3]
        self.document_type = args[4]
        self.document_id = args[5]
        if not (
                self.first_name or self.last_name or self.birth_date or self.phone or self.document_type or self.document_id):
            raise AttributeError
        self.created = True
        self.patinfo.info("User was created")
        # except:
        #     self.created = False
        #     self.paterr.error("Error. User was not created.")
        #     raise AttributeError

    @staticmethod
    def create(*args):
        return Patient(*args)

    def save(self):
        if not self.created:
            self.paterr.warning("User is NONE, so it wasn't saved.")
        filename = "PatienList.csv"
        try:
            with open(filename, "a", newline="", encoding='utf-8') as file:
                writer = csv.writer(file)
        except:
            raise AttributeError("Can't open csv file")

        try:
            data = [self.first_name, self.last_name, self.birth_date, self.phone, self.document_type, self.document_id]
             # filename = CSV_PATH
            with open(filename, "a", newline="", encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(data)
            self.patinfo.info("User was saved.")
        except:
            self.paterr.error("User was not saved!")
            raise AttributeError

    def __str__(self):
        if not self.created:
            return ""
        data = ' '.join(
            [self.first_name, self.last_name, self.birth_date, self.phone, self.document_type, self.document_id])
        # self.patinfo.info(data)
        return data

    def is_created(self):
        return self.created


class PatientCollection:
    def __init__(self, path_to_file):
        if not os.path.isfile(path_to_file):
            raise ValueError("Path does,")
        self.filepath = path_to_file

    def __iter__(self):
        with open('PatienList.csv', 'r', encoding='utf-8') as File:
            reader = csv.reader(File)
            for row in reader:
                a = Patient(*row)
                yield a

    def limit(self, num):
        if num < 1:
            raise ValueError("Argument in limit should be >1.")
        counter = 0
        with open('PatienList.csv', 'r', encoding='utf-8') as File:
            reader = csv.reader(File)
            for row in reader:
                if counter >=num:
                    return
                a = Patient(*row)
                yield a

