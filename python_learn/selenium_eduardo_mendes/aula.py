from selenium.webdriver import Firefox

url = 'https://curso-python-selenium.netlify.app/aula_03.html#'

browser = Firefox()

browser.get(url)

#a = browser.find_element('name', 'a')
#a.send_keys('geckodriver')
#a.submit()

#browser.quit()
