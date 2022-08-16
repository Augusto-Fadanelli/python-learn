from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

browser = Chrome()
browser.get('http://selenium.dunossauro.live/aula_04_a.html')

lista_n_ordenada = browser.find_element(By.TAG_NAME, 'ul')
lis = lista_n_ordenada.find_elements(By.TAG_NAME, 'li')
print(lis[0].find_element(By.TAG_NAME, 'a').text)

