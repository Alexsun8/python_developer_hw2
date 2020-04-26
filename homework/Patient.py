from homework.Descriptor import *
from homework.Log import patinfo, paterr


class Patient:
    first_name = Name()
    last_name = Name()
    birth_date = Date()
    phone = Phone()
    document_type = DocType()
    document_id = DocId()
    created = False

    def __init__(self, *args):
        if len(args) == 0:
            self.created = False
            patinfo.info("Empty Patient was created")
            return
        elif not len(args) == 6:
            self.created = False
            paterr.error(
                "There shold be 6 args: first_name_, last_name_, birth_date_, phone_, document_type_, document_id_. Patient wasn't created")
            return
        try:
            # self.created = False
            self.first_name = args[0]
            self.last_name = args[1]
            self.birth_date = args[2]
            self.phone = args[3]
            self.document_type = args[4]
            self.document_id = args[5]
            self.created = True
            if not (
                    self.first_name or self.last_name or self.birth_date or self.phone or self.document_type or self.document_id):
                raise AttributeError
            patinfo.info("User was created")
        except:
            self.created = False
            paterr.error("Error. User was not created.")

    def create(self, *args):
        if not len(args) == 6:
            self.created = False
            paterr.error(
                "There shold be 6 args: first_name_, last_name_, birth_date_, phone_, document_type_, document_id_. Patient wasn't created")
            return

        try:
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
            patinfo.info("User was created")
        except:
            self.created = False
            paterr.error("Error. User was not created.")

    def save(self):
        if not self.created:
            paterr.warning("User is NONE, so it wasn't saved.")
        try:
            data = ' '.join(
                [self.first_name, self.last_name, self.birth_date, self.phone, self.document_type, self.document_id,
                 '\n'])
            filename = "PatientList.csv"
            with open(filename, 'a+') as file:
                file.write(data)
            patinfo.info("User was saved.")
        except:
            paterr.error("User was not saved!")

    def __str__(self):
        if not self.created:
            return ""
        data = ' '.join(
            [self.first_name, self.last_name, self.birth_date, self.phone, self.document_type, self.document_id])
        return data


# pat = Patient("Alice", "asdasd", "2003-02-30", "89234445553", "pfuhfy", "627 78 99977")
# pat.save()
# pat.create("Alice", "as", "2003-02-26", "89234445553", "ghfdf", "627 78 99977")
# pat.save()
# pat.last_name = "Johnson"
# pat.birth_date = "01-02-1990"
# # print(pat)
#
# pat = Patient()
# pat.create("bob", "as", "2003-02-26", "89234445553", "gfcgjhn", "627 78 99977")
# pat.save()
