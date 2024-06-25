
from page_Object.Advanced_name_search import IMDb
import os
import sys
import time

class Test_Advanced_name_search:
    url = "https://www.imdb.com/search/name/"

    def test_initialize_driver(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        #validation the page
        act_title = self.driver.title

        if act_title == "Advanced name search":
            assert True
        else:
            assert False
        # create a class instance
        self.imdb = IMDb(setup)
        self.driver.implicitly_wait(10)
        #click EXpand Button
        self.imdb.click_expand()
        self.driver.implicitly_wait(10)
        #Fill the actor name
        self.imdb.fill_name("vijay")
        #Fill the actor Dob
        self.imdb.fill_dob("1974-06", "1974-07")
        #Fill the Birthday
        self.imdb.fill_birthday("06-22")
        #Select the Select Awqads and recognition
        self.imdb.select_awards_recognition()
        #Select the topics
        self.imdb.select_page_topics()
        #Select the gender
        self.imdb.select_gender()
        #EDnter the credits
        self.imdb.credits("Naalaiya Theerpu")
        #Close the driver
        self.driver.close()


