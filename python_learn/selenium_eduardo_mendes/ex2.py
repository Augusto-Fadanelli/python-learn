from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

browser = Firefox()
browser.get(url)

ancora = browser.find_element(By.ID, 'ancora')

ps = browser.find_elements(By.TAG_NAME, 'p')
n_esperado = list(ps[1].text)
n_esperado = n_esperado[-1]

while(True):
    ancora.send_keys('geckodriver' + Keys.ENTER)

    ps = browser.find_elements(By.TAG_NAME, 'p')
    aux = list(ps[-1].text)

    if aux[-1] == n_esperado:
        break
 
