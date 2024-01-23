from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from fixture.contact import ContactHelper
from fixture.session import SessionHelper


class AppContact:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.contact = ContactHelper(self)
        self.session = SessionHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()
