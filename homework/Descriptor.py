from homework.DataIsValid import *
# from homework.Log import validator,validerr

class   Name:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
        # return instance.__dict__[self.name]

    def __set__(self, instance, val):
        if not isinstance(val, str):
            instance.paterr.error('Invalid name.')
            instance.paterr.error("Error. User was not created.")
            raise TypeError("not str")
        elif instance.is_created():
            instance.paterr.error("You can't change name")
            instance.paterr.error("Error. User was not created.")
            raise AttributeError("can't change name")
        # val = sub(" ", "-", val)
        n = nameReal(val)
        if not n:
            instance.paterr.error("Wrong name")
            instance.paterr.error("Error. User was not created.")
            raise ValueError("wrong name")
        instance.__dict__[self.name] = n
        instance.patinfo.debug(["name is okey:", val])


    def __set_name__(self, owner, name):
        self.name = name



class Phone:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, number):
        if not isinstance(number, str):
            instance.paterr.error('Invalid number.')
            instance.paterr.error("Error. User was not created.")
            raise TypeError("not str")
        prov = phoneIsValid(number)
        if not prov:
            instance.paterr.error('Invalid number. +code-xxx-xxx-xx-xx')
            instance.paterr.error("Error. User was not created.")
            raise ValueError("phone error")
        number = prov
        instance.__dict__[self.name] = number
        instance.patinfo.debug(["number is okey: ", number])
        if instance.is_created():
            instance.patinfo.info(["number is okey: ", number])

    def __set_name__(self, owner, name):
        self.name = name


class DocType():
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, type):
        if not isinstance(type, str):
            instance.paterr.error('Invalid type.')
            instance.paterr.error("Error. User was not created.")
            raise TypeError("not str")
        prov = docTypeIsValid(type)
        if not prov:
            instance.paterr.error('Invalid doc type. паспорт, загран или права')
            instance.paterr.error("Error. User was not created.")
            raise ValueError("doctype error")
        instance.__dict__[self.name] = prov
        instance.patinfo.debug(["Doc type is okey:", prov])
        if instance.is_created():
            instance.patinfo.info(["Dov type is okey: ", prov])

    def __set_name__(self, owner, name):
        self.name = name


class DocId:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance,id):
        if not isinstance(id, str):
            instance.paterr.error('Invalid id.')
            instance.paterr.error("Error. User was not created.")
            raise TypeError("not str")
        self.type = instance.document_type
        prov = docIdIsValid(id, self.type)
        if not prov:
            instance.paterr.error('Invalid doc id. паспорт(10 цифр), загран(9 цифр) или права(10 цифр)')
            instance.paterr.error("Error. User was not created.")
            raise ValueError("docid error")
        instance.__dict__[self.name] = prov
        instance.patinfo.debug(["Doc id okey: ", prov])
        if instance.is_created():
            instance.patinfo.info(["Doc id is okey: ", prov])

    def __set_name__(self, owner, name):
        self.name = name
        self.type = None


class Date:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, date):
        if not isinstance(date, str):
            instance.paterr.error('Invalid name.')
            instance.paterr.error("Error. User was not created.")
            raise TypeError("not str")
        prov = dateIsValid(date)
        if not prov:
            instance.paterr.error('Invalid date. year-month-day')
            instance.paterr.error("Error. User was not created.")
            raise ValueError("date error")
        instance.__dict__[self.name] = prov
        instance.patinfo.debug(["Date is okey: ", prov])
        if instance.is_created():
            instance.patinfo.info(["Date is okey: ", prov])

    def __set_name__(self, owner, name):
        self.name = name
