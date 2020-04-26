import logging

# u should uncomment lines, and comment 2 times  1 line line on comment and it'll start write logs in 2 files
# handler = logging.FileHandler('Logs.txt', 'a', 'utf-8')
handler = logging.FileHandler('/home/alexsun8/kib/ДЗ2/python_developer_hw2/homework/Good_Logs.txt', 'a', 'utf-8')
handler2 = logging.FileHandler('/home/alexsun8/kib/ДЗ2/python_developer_hw2/homework/Bad_Logs.txt', 'a', 'utf-8')
formatter = logging.Formatter("%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s")
handler.setFormatter(formatter)
# handlerbad = handler
handlerbad = handler2


# logs in Patient class
patinfo = logging.getLogger("Patient info")
patinfo.setLevel(logging.INFO)
patinfo.addHandler(handler)
paterr = logging.getLogger("Patient errors")
paterr.setLevel(logging.ERROR)
paterr.addHandler(handlerbad)

# logs in Pat. Colle
collectinfo = logging.getLogger("Collection info")
collectinfo.setLevel(logging.INFO)
collectinfo.addHandler(handler)
collecterr = logging.getLogger("Collection errors")
collecterr.setLevel(logging.ERROR)
collecterr.addHandler(handlerbad)

# logs in Descriptors in data valid
validator = logging.getLogger("Validator")
validator.setLevel(logging.INFO)
validator.addHandler(handler)
validerr = logging.getLogger("Validator errors")
validerr.setLevel(logging.ERROR)
validerr.addHandler(handlerbad)

# for logging in console
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)

collectinfo.addHandler(consoleHandler)
collecterr.addHandler(consoleHandler)
patinfo.addHandler(consoleHandler)
paterr.addHandler(consoleHandler)
validator.addHandler(consoleHandler)
validerr.addHandler(consoleHandler)
