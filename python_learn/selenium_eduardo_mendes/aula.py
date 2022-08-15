from time import sleep

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://curso-python-selenium.netlify.app/aula_03.html#'

browser = Firefox()
browser.get(url)

sleep(1)

a = browser.find_element(By.TAG_NAME, 'a')

for click in range(10):
    ps = browser.find_elements(By.TAG_NAME, 'p')
    a.send_keys('geckodriver' + Keys.ENTER)
    print(f'Valor do último p: {ps[-1].text} valor do click: {click}')

#browser.quit()
