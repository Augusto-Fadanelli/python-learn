from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

browser = Firefox()
browser.get(url)

key = browser.find_element(By.TAG_NAME, 'h1')

ps = browser.find_elements(By.TAG_NAME, 'p')

dicionario = {
        key.text : {
            'texto1' : ps[0].text,
            'texto2' : ps[1].text,
            'texto3' : ps[2].text,
            }
        }

print(dicionario)
