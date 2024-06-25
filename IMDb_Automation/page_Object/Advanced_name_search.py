from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

class IMDb:
    def __init__(self, driver):
        self.driver = driver
        self.expand = (By.CSS_SELECTOR, "#__next > main > div.ipc-page-content-container.ipc-page-content-container--center.sc-e51f9d6d-0.Fmvqg > div.ipc-page-content-container.ipc-page-content-container--center > section > section > div > section > section > div:nth-child(2) > div > section > div.ipc-page-grid.ipc-page-grid--bias-left.ipc-page-grid__item.ipc-page-grid__item--span-2 > div.sc-57ba0b6e-0.dyvviw.ipc-page-grid__item.ipc-page-grid__item--span-1 > div > button > span")
        self.expand_button = (By.XPATH, '//span[text()="Expand all"]')
        self.name_input = (By.XPATH, '(//input[@type="text"])[2]')
        self.enter_dob_field = (By.XPATH, '(//input[@type="text"])[3]')
        self.end_dob_field = (By.XPATH, '(//input[@type="text"])[4]')
        self.birthday_input = (By.XPATH, '(//input[@type="text"])[5]')
        self.awards_recognition_button = (By.XPATH, '//*[@id="accordion-item-awardsAccordion"]/div/section/button[1]')
        self.page_topics_button = (By.XPATH, '//*[@id="accordion-item-pageTopicsAccordion"]/div/div/section/button[1]')
        self.gender_button = (By.XPATH, '//*[@id="accordion-item-genderIdentityAccordion"]/div/section/button[1]')
        self.credits_input = (By.XPATH, '//*[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input')

    #Click the expand button
    def click_expand(self):
        element_expand = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.expand))
        self.driver.execute_script("arguments[0].click();", element_expand)
        #Fill the name

    def fill_name(self, name):
        name_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.name_input))
        name_input.send_keys(name)

    # Fill the dob

    def fill_dob(self, start_date, end_date):
        start_dob = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.enter_dob_field))
        start_dob.send_keys(start_date)

        end_dob = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.end_dob_field))
        end_dob.send_keys(end_date)

    #Fill the birthday

    def fill_birthday(self, birthday):
        birthday_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.birthday_input))
        birthday_input.send_keys(birthday)

    # Select the awards and recognition

    def select_awards_recognition(self):
        awards_recognition_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.awards_recognition_button))

        clicked = False
        for _ in range(3):
            try:
                awards_recognition_button.click()
                clicked = True
                break
            except Exception as e:
                print(f"Error clicking element: {e}")
                time.sleep(2)

        if not clicked:
            print("Failed to click the element after multiple attempts.")

    # Select the page topics

    def select_page_topics(self):
        page_topics_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.page_topics_button))
        clicked = False
        for _ in range(3):
            try:
                page_topics_button.click()
                clicked = True
                break
            except Exception as e:
                print(f"Error clicking element: {e}")
                time.sleep(2)

        if not clicked:
            print("Failed to click the element after multiple attempts.")

    # Select the gender

    def select_gender(self):
        gender_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.gender_button))
        clicked = False
        for _ in range(3):
            try:
                gender_button.click()
                clicked = True
                break
            except Exception as e:
                print(f"Error clicking element: {e}")
                time.sleep(2)

        if not clicked:
            print("Failed to click the element after multiple attempts.")

    # Enter the credits

    def credits(self, credit):
        credits_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.credits_input))
        credits_input.send_keys(credit)
        credits_input.send_keys(Keys.ENTER)














