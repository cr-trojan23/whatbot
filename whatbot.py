from selenium import webdriver
import time
firefox_driver = webdriver.Firefox(executable_path="/home/kiaria/Documents/github_projects/whatbot/geckodriver")
firefox_driver.get("https://web.whatsapp.com")

time.sleep(5)

contact_name = input("Enter the contact name: ")
contact_box = firefox_driver.find_element_by_xpath('//span[@title="{}"]'.format(contact_name))
contact_box.click()

text_box = firefox_driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
for i in range(2001):
    msg = ""
    text_box.send_keys(msg)
    send_button = firefox_driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]')
    send_button.click() 