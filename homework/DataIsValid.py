from copy import deepcopy
from re import fullmatch, sub, search
# from homework.Log import validerr

def nameReal(name_):
    pattern = "[0-9]"
    name = sub(pattern, "", name_)
    if len(name)==0:
        return False
    return name



def dateIsReal(date):
    year = int(date[:4])
    if year < 1900 or year > 2020:
        # validerr.paterr.warning(["It should be: 1900<year<=2020. Your year: ", year])
        return False

    month = int(date[5:7])
    if month < 0 or month > 12:
        # validerr.paterr.warning(["It should be: 0<month<=12. Your month: ", month])
        return False

    day = int(date[8:])
    if day < 1 or day > 31:
        # validerr.paterr.warning(["It should be: 0<day<32. Your day: ", day])
        return False

    if month == 2 and day > 29:
        # validerr.paterr.warning("In Feb only 28 or 29 days")
        return False

    if month == 2 and day == 29:
        print("WOW!")
    return date


def dateIsValid(date):
    pattern1 = "\d{4}.\d{2}.\d{2}"  # y-m-d
    pattern2 = "\d{2}.\d{2}.\d{4}"  # d-m-y
    match1 = fullmatch(pattern1, date)
    match2 = fullmatch(pattern2, date)
    if match1:
        return dateIsReal(date)
    elif match2:
        dateNew = deepcopy(date[len(date) - 4:])
        dateNew = '-'.join([dateNew, date[len(date) - 7:len(date) - 5]])
        dateNew = '-'.join([dateNew, date[:2]])
        if dateIsReal(dateNew):
            return dateNew
        else:
            return False
    else:
        return False

# print(dateIsReal("1978-01-05"))

def phoneIsValid( phone_):
    pattern = "[^+,0,1,2,3,4,5,6,7,8,9]"
    phone = sub(pattern, "", phone_)
    if len(phone)<10:
        return False
    if phone[0] == '8' or phone[0]=='7':
        phone = ''.join(['+7', phone[1:]])
    elif not phone[0] == '+' or not phone[1] == '7':
        # validerr.paterr.warning(["Only Russians numbers are valid. +7-xxx-xxx-xx-xx or 8-xxx-xxx-xx-xx. Your num: ", phone])
        return False

    if not len(phone) == 12:
        # validerr.paterr.warning(["Only Russians numbers are valid. len !=12  . Your num: ", phone])
        return False
    if not (phone[2:5] == '495' or phone[2:5] == '499' or phone[2] == '9'):
        # validerr.paterr.warning(["Only Russians numbers are valid. +7-499-... or +7-495-... or +7-9..-.... Your num: ", phone])
        return False
    return phone



def docTypeIsValid(doc_type):
    if not isinstance(doc_type, str):
        return False
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

    return False


def docIdIsValid(id, type=None):
    pattern = "[^0,1,2,3,4,5,6,7,8,9]"
    id = sub(pattern, "", id)
    if len(id) == 10:
        if type == "паспорт" or type == "права" or not type:
            return id
        else:
            # validerr.paterr.warning(["Zpass - len ==9. In dr and pass-10. Your type: ", type, ". Your id: ", id])
            return False
    elif len(id) == 9 and (type == "загран" or not type):
        # validerr.paterr.warning(["Zpass - len ==9. In dr and pass-10. Your type: ", type, ". Your id: ", id])
        return id
    else:
        return False
