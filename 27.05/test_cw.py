from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest

@pytest.fixture
def open_browser():
    browser = webdriver.Chrome()
    browser.get('https://blog.hubspot.com/marketing/surf-internet-websites')
    yield browser
    browser.close()

def test_link_is_displayed(open_browser):
    browser = open_browser
    link = browser.find_element(By.LINK_TEXT, 'Know Your Meme')
    # is_displayed() - проверяет, есть ли элемент на веб-сайте
    assert link.is_displayed()

@pytest.mark.metka
def test_link_is_displayed_v2(open_browser):
    browser = open_browser
    links = ['GeoGuesser',
             'Know Your Meme',
             'The Oatmeal',
             'Supercook',
             'OCEARCH Shark Tracker',
             'The Oregon Trail',
             'Giphy',
             'Wayback Machine',
             'Apartment Therapy',
             'Imgur',
             'Gravity Points',
             'Pottermore',
             'The Toast',
             'The Onion',
             'Cracked',
             'Mental Floss',
             'HowStuffWorks',
             'Lifehacker',
             'Mix',
             'Space.com',
             'Zillow',
             'Wikipedia']    
    for link in links:
        link_value = browser.find_element(By.LINK_TEXT, link)
        assert link_value.is_displayed()

# click() тыкает на элемент
def test_search_field(open_browser):
    pass

'''
1. Почитай о конструкции By (Selenium)
2. Написать тест, который тыкает на кнопку поиска элемента и находит его
Ссылка: https://blog.hubspot.com
3. Почитать об is_displayed(), click() (Selenium)
Документация о Selenium: https://selenium-python.readthedocs.io/locating-elements.html
'''
