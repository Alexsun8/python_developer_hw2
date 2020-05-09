import csv
import psycopg2

from homework.Descriptor import *
import logging
from homework.Decorators import Pat_create_logs, Pat_save_logs, PC_create, PC_create_db


class Patient:
    first_name = Name()
    last_name = Name()
    birth_date = Date()
    phone = Phone()
    document_type = DocType()
    document_id = DocId()
    created = False

    formatter = logging.Formatter("%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s")
    handler = logging.FileHandler('/home/alexsun8/kib/python_developer_hw2/homework/Good_Logs.txt', 'a', 'utf-8')
    handlerbad = logging.FileHandler('/home/alexsun8/kib/python_developer_hw2/homework/Bad_Logs.txt', 'a', 'utf-8')
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

    @Pat_create_logs
    def __init__(self, *args):
        self.created = False
        self.first_name = args[0]
        self.last_name = args[1]
        self.birth_date = args[2]
        self.phone = args[3]
        self.document_type = args[4]
        self.document_id = args[5]
        self.created = True

    @staticmethod
    def create(*args):
        return Patient(*args)

    @Pat_save_logs
    def save(self):
        data = [self.first_name, self.last_name, self.birth_date, self.phone, self.document_type, self.document_id]

        with psycopg2.connect(
                database="postgres",
                user="alex",
                password="1234",
                host="127.0.0.1",
                port="5432") as con:
            with con.cursor() as cursor:
                postgres_insert_query = """ INSERT INTO PATIENTS(FIRST_NAME, LAST_NAME, BIRTH_DATE, PHONE, DOCUMENT_TYPE, DOCUMENT_ID) VALUES (%s,%s,%s,%s,%s,%s)"""
                cursor.execute(postgres_insert_query, data)
                con.commit()

    def __str__(self):
        if not self.created:
            return ""
        data = ' '.join(
            [self.first_name, self.last_name, self.birth_date, self.phone, self.document_type, self.document_id])
        return data

    def is_created(self):
        return self.created


class PatientCollection:
    # @PC_create
    # def __init__(self, path_to_file):
    #     self.filepath = path_to_file

    @PC_create_db
    def __init__(self, db, user_, password_, host_, port_):
        self.database = db
        self.user = user_
        self.password = password_
        self.host = host_
        self.port = port_

    def __iter__(self):
        with psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port) as con:
            with con.cursor() as cursor:
                postgreSQL_select_Query = "select * from PATIENTS"

                cursor.execute(postgreSQL_select_Query)
                records = cursor.fetchall()

                for row in records:
                    a = Patient(*row)
                    yield a

    def limit(self, num=-1):
        if num < 1:
            raise ValueError("Argument in limit should be >1.")
        with psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port) as con:
            with con.cursor() as cursor:
                postgreSQL_select_Query = "select * from PATIENTS"

                cursor.execute(postgreSQL_select_Query)

                if num > -1:
                    records = cursor.fetchmany(num)
                else:
                    records = cursor.fetchall


                for row in records:
                    # print("PAT: ", row[0], row[1], row[2], row[3], row[4], row[5])
                    a = Patient(*row)
                    yield a

    def count(self):
        count = -1
        with psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port) as con:
            with con.cursor() as cursor:
                comm = """SELECT * FROM PATIENTS"""
                cursor.execute(comm)
                count = len(cursor.fetchall())

        return count
