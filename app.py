from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = 'C:\\Users\\tordsyabe\\Documents\\selenium\\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get("https://john-llave.odoo.com/web")

login = driver.find_element_by_name("login")
login.send_keys("extordsllave@gmail.com")
password = driver.find_element_by_name("password")
password.send_keys("hopeful2609")

password.send_keys(Keys.RETURN)


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Sales"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "o_data_row"))
    )

    element.click()

    page_number = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "o_pager_limit"))
    )

    print(page_number.text)


    while True:

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div/div[1]/div[1]/div[1]/button[8]"))).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Next']"))).click()

except:
    pass




