from homework.DataIsValid import *
from homework.Decorators import Name_set, set_descr


class Name:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    @Name_set
    def __set__(self, instance, val):
        n = nameReal(val)
        if not n:
            return None

        instance.__dict__[self.name] = n
        return n

    def __set_name__(self, owner, name):
        self.name = name


class Phone:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    @set_descr
    def __set__(self, instance, number):
        prov = phoneIsValid(number)
        if not prov:
            return None

        instance.__dict__[self.name] = prov
        return prov

    def __set_name__(self, owner, name):
        self.name = name


class DocType():
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    @set_descr
    def __set__(self, instance, type):
        prov = docTypeIsValid(type)
        if not prov:
            return None

        instance.__dict__[self.name] = prov
        return prov

    def __set_name__(self, owner, name):
        self.name = name


class DocId:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    @set_descr
    def __set__(self, instance, id):
        self.type = instance.document_type
        prov = docIdIsValid(id, self.type)

        if not prov:
            return None

        instance.__dict__[self.name] = prov
        return prov

    def __set_name__(self, owner, name):
        self.name = name
        self.type = None


class Date:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    @set_descr
    def __set__(self, instance, date):
        prov = dateIsValid(date)
        if not prov:
            return None
        instance.__dict__[self.name] = prov
        return prov

    def __set_name__(self, owner, name):
        self.name = name
