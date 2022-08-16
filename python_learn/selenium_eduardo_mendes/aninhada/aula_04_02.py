from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


def find_by_text(browser, tag, text):
    """Encontrar o elemento com o texto `text`.

    Args:
        - browser = Instancia do browser [firefox, chrome, ...]
        - tag = Tag onde o texto será procurado
        - text = Conteúdo que deve estar na tag
    """

    elements = browser.find_elements(By.TAG_NAME, tag)

    for e in elements:
        if e.text == text:
            return e


def find_by_href(browser, link):
    """Encontrar o elemento `a` com o link `link`.

    Args:
        - browser = Instancia do browser [firefox, chrome, ...]
        - link = Link que será procurado em todas as tags `a`
    """

    elements = browser.find_elements(By.TAG_NAME, 'a')

    for e in elements:
        if link in e.get_attribute('href'):
            return e

if __name__ == '__main__':
    browser = Firefox()
    browser.get('http://selenium.dunossauro.live/aula_04_a.html')

    #result = find_by_text(browser, 'li', 'DuckDuckGo')
    #print(result.text)

    elemento_ddg = find_by_href(browser, 'ddg')
    print(elemento_ddg.text)
    print(elemento_ddg.get_attribute('href'))

