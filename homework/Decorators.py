import os
import psycopg2


def Pat_create_logs(ini):
    def wrapper_pc(self, *args):
        if len(args) == 0:
            self.patinfo.debug("Empty Patient was created")
            return
        elif not len(args) == 6:
            self.paterr.error(
                "There should be 6 args: first_name_, last_name_, birth_date_, phone_, document_type_, document_id_. Patient wasn't created")
            return
        ini(self, *args)
        if not (
                self.first_name or self.last_name or self.birth_date or self.phone or self.document_type or self.document_id):
            self.created = False
            raise AttributeError
        self.patinfo.info("User was created")

    return wrapper_pc


def Pat_save_logs(save):
    def wrapper_ps(self):
        if not self.created:
            self.paterr.warning("User is NONE, so it wasn't saved.")
        # try:
        #     with open(filename, "a", newline="", encoding='utf-8') as file:
        #         writer = wr(file)
        # except:
        #     raise AttributeError("Can't open csv file")
        try:
            save(self)
            self.patinfo.info("User was saved.")
        except:
            self.paterr.error("User was not saved!")
            raise AttributeError

    return wrapper_ps


def PC_create(ini):
    def wrapper_pcc(self, path):
        if not os.path.isfile(path):
            raise ValueError("Path does exist")
        ini(self, path)

    return wrapper_pcc


def Name_set(set):
    def wrapper_ns(self, instance, val):
        # raise TypeError
        if not isinstance(val, str):
            instance.paterr.error('Invalid name.')
            instance.paterr.error("Error. User was not created.")
            raise TypeError("not str")

        if instance.is_created():
            instance.paterr.error("You can't change name")
            instance.paterr.error("Error. User was not created.")
            raise AttributeError("can't change name")

        if not set(self, instance, val):
            instance.paterr.error("Wrong name")
            instance.paterr.error("Error. User was not created.")
            raise ValueError("wrong name")

        instance.patinfo.debug(["name is okey:", instance.__dict__[self.name]])

    return wrapper_ns


def set_descr(set):
    def wrapper_sd(self, instance, val):
        d_t = self.name
        if not isinstance(val, str):
            instance.paterr.error(['Invalid ', d_t])
            instance.paterr.error("Error. User was not created.")
            raise TypeError("not str")

        if not set(self, instance, val):
            instance.paterr.error(['Invalid value ', d_t])
            instance.paterr.error("Error. User was not created.")
            raise ValueError([d_t, " error"])

        instance.patinfo.debug([d_t, "   is okey: ", instance.__dict__[self.name]])
        if instance.is_created():
            instance.patinfo.info([d_t, "  is okey: ", instance.__dict__[self.name]])

    return wrapper_sd


def PC_create_db(ini):
    def wrapper_pcidb(self, db="postgres", user_="alex", password_="1234", host_="127.0.0.1", port_="5432"):
        with psycopg2.connect(
                database="postgres",
                user="alex",
                password="1234",
                host="127.0.0.1",
                port="5432") as con:
            pass

        ini(self, db, user_, password_, host_, port_)

    return wrapper_pcidb
