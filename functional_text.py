from selenium import webdriver

browser = webdriver.Chrome('/Users/ieonsang/study/tdd/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
