from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()
browser.get('https://www.instagram.com')
time.sleep(3)
username_input = browser.find_element_by_css_selector('input[name="username"]').send_keys('rc0fficial')
password_input = browser.find_element_by_css_selector('input[name="password"]').send_keys('DOnGDInG9552374@#')

login_button = browser.find_element_by_xpath('//button[@type="submit"]')
login_button.click()

time.sleep(2)
notNowButton = WebDriverWait(browser, 15).until(
    lambda d: d.find_element_by_xpath('//button[text()="Not Now"]'))
notNowButton.click()
time.sleep(2)
notNowButton = WebDriverWait(browser, 15).until(
    lambda d: d.find_element_by_xpath('//button[text()="Not Now"]'))
notNowButton.click()
# time.sleep(2)
# notNowButton = WebDriverWait(browser, 15).until(
#     lambda d: d.find_element_by_xpath('//button[text()="Turn On"]'))
# notNowButton.click()

time.sleep(2)

for i in range(50):
    browser.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button/div').click()
    browser.refresh()
    time.sleep(5)