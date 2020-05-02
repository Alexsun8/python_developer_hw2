from copy import deepcopy
from re import fullmatch, sub, search
from datetime import date as dt


# from homework.Log import validerr

def nameReal(name_):
    pattern = "[0-9]"
    name = sub(pattern, "", name_)
    if len(name) == 0:
        return None
    return name


def dateIsValid(date):
    pattern1 = "\d{4}.\d{2}.\d{2}"  # y-m-d
    pattern2 = "\d{2}.\d{2}.\d{4}"  # d-m-y
    match1 = fullmatch(pattern1, date)
    match2 = fullmatch(pattern2, date)

    if match1:
        try:
            d = str(dt(int(date[:4]), int(date[5:7]), int(date[8:])))
        except:
            return None
    elif match2:
        try:
            d = dt(int(date[8:]), int(date[5:7]), int(date[:4]))
        except:
            return None
    else:
        return None
    return d


def phoneIsValid(phone_):
    pattern = "[^+,0,1,2,3,4,5,6,7,8,9]"
    phone = sub(pattern, "", phone_)
    if len(phone) < 10:
        return None
    if phone[0] == '8' or phone[0] == '7':
        phone = ''.join(['+7', phone[1:]])
    elif not phone[0] == '+' or not phone[1] == '7':
        # validerr.paterr.warning(["Only Russians numbers are valid. +7-xxx-xxx-xx-xx or 8-xxx-xxx-xx-xx. Your num: ", phone])
        return None

    if not len(phone) == 12:
        # validerr.paterr.warning(["Only Russians numbers are valid. len !=12  . Your num: ", phone])
        return None
    if not (phone[2:5] == '495' or phone[2:5] == '499' or phone[2] == '9'):
        # validerr.paterr.warning(["Only Russians numbers are valid. +7-499-... or +7-495-... or +7-9..-.... Your num: ", phone])
        return None
    return phone


def docTypeIsValid(doc_type):
    if not isinstance(doc_type, str):
        return None
    doc_type = doc_type.lower()

    passport = "паспорт"
    passportruen = "gfcgjhn"
    zPassport = "загран"
    zpassportruen = "pfuhfy"
    prav1 = "водительск"
    prav1ruen = "djlbntkmcr"
    prav2 = "права"
    prav2ruen = "ghfdf"

    if search(zPassport, doc_type) or search(zpassportruen, doc_type):
        return "загран"
    elif search(passport, doc_type) or search(passportruen, doc_type):
        return "паспорт"
    elif search(prav1, doc_type) or search(prav2, doc_type) or search(prav1ruen, doc_type) or search(prav2ruen,
                                                                                                     doc_type):
        return "права"

    return None


def docIdIsValid(id, type=None):
    pattern = "[^0,1,2,3,4,5,6,7,8,9]"
    id = sub(pattern, "", id)
    if len(id) == 10:
        if type == "паспорт" or type == "права" or not type:
            return id
        else:
            # validerr.paterr.warning(["Zpass - len ==9. In dr and pass-10. Your type: ", type, ". Your id: ", id])
            return None
    elif len(id) == 9 and (type == "загран" or not type):
        # validerr.paterr.warning(["Zpass - len ==9. In dr and pass-10. Your type: ", type, ". Your id: ", id])
        return id
    else:
        return None
