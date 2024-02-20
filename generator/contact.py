import random
import string
import jsonpickle
from model.contact import Contact
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits_string(maxlen):
    digits = string.digits
    return "".join([random.choice(digits) for i in range(random.randrange(maxlen))])


def random_letters_string(prefix, maxlen):
    letters = string.ascii_letters + " "*2
    return prefix + "".join([random.choice(letters) for i in range(random.randrange(maxlen))])


def random_email():
    symbols_for_mail_name = string.ascii_letters + string.digits + "." + "-" + "_"
    generated_mail_name = ''.join([random.choice(symbols_for_mail_name) for i in range(random.randrange(1, 15))])
    generated_domain_name = ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(2, 10))])
    generated_main_domain = ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(2, 5))])
    random_emails = f"{generated_mail_name}@{generated_domain_name}.{generated_main_domain}"
    return random_emails


testdata = [Contact(firstname=random_letters_string("firstname", 10), lastname=random_letters_string("lastname", 10),
                    address=random_string("address", 30),
                    home=random_digits_string(11), mobile=random_digits_string(11), work=random_digits_string(11),
                                email1=random_email(), email2=random_email(), email3=random_email())]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
