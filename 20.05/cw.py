from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://cpstest.org')


for elem in range(100):
    black_window = browser.find_element(by=By.XPATH,
                                    value="//div[@id='clickarea']/button")
    black_window.click()

browser.close()

'''
1. Почитать об XPATH
https://ru.wikipedia.org/wiki/XPath
2. Почитать об HTML
https://ru.wikipedia.org/wiki/HTML
3. Написать XPATH для сайта ROZETKA, который будет искать следующее:
 - Кнопку "Каталог"
 - Кнопку "Корзинка"
 - Кнопку "Товары для дома"
 - Первый товар на главной странице сайта в рекомендациях
'''
