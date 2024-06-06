import os
import time
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By

class Driver:
    driver: webdriver.Chrome
    timeout = 5

    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.headless = headless
        self.driver = webdriver.Chrome(options=options)

    def quit(self):
        self.driver.quit()

    def login(self):
        self.driver.get("https://www.bankofamerica.com/")
        self.driver.find_element(By.ID, "onlineId1").send_keys(os.environ.get('USERNAME'))
        self.driver.find_element(By.ID, "passcode1").send_keys(os.environ.get('PASSWORD'))
        self.driver.find_element(By.ID, "signIn").click()
        time.sleep(self.timeout)

        if self.driver.current_url == "https://secure.bankofamerica.com/login/sign-in/signOnSuccessRedirect.go":
            self.driver.find_element(By.ID, "btnARContinue").click()
            print("input 2fa code: ")
            time.sleep(self.timeout)
            # some way to msg through discord to ask for the code
            self.driver.find_element(By.CLASS_NAME, "authcode").send_keys(input())
            self.driver.find_element(By.ID, "yes-recognize").click()
            self.driver.find_element(By.ID, "continue-auth-number").click()
            time.sleep(self.timeout)

    def get_accounts(self) -> List[dict]:
        result = []

        for account in self.driver.find_elements(By.CLASS_NAME, "AccountItem"):
                print("Found account: {}".format(account.get_name()))
                result.append(account)
        
        return result


