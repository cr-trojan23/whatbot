from selenium import webdriver
import time


firefox_driver = webdriver.Firefox(executable_path="/home/kiaria/Documents/github_projects/whatbot/geckodriver")
firefox_driver.get("https://web.whatsapp.com")

time.sleep(5)

unres_contacts = firefox_driver.find_elements_by_class_name("_2Q3SY")
print(unres_contacts)