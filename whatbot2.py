from selenium import webdriver
import time
import math
firefox_driver = webdriver.Firefox(executable_path="/home/kiaria/Documents/github_projects/whatbot/geckodriver")
firefox_driver.get("https://web.whatsapp.com")

input()

while True:
    new_messages = firefox_driver.find_elements_by_class_name("_38M1B")
    if len(new_messages) > 0:
        current_chat = new_messages[-1]
        actions = webdriver.common.action_chains.ActionChains(firefox_driver)
        actions.move_to_element_with_offset(current_chat, 0, -30)
        try:
            actions.click()
        except Exception as ex:
            pass
        try:
            name = firefox_driver.find_elements_by_class_name("_1Lc2C eHxwV _3-8er").text