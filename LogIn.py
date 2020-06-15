from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

try:
    link = "https://rozetka.com.ua/"
    browser = webdriver.Chrome()
    browser.get(link)

    l1 = browser.find_element_by_class_name('side-menu__toggler')
    l1.click()
    
    l2 = browser.find_element_by_class_name('menu-main__link_type_login')
    l2.click()

    email = browser.find_element_by_id('auth_email')
    email.send_keys('dm.test2207@gmail.com')

    pas = browser.find_element_by_id('auth_pass')
    pas.send_keys('Test123')

    button = browser.find_element_by_class_name('auth-modal__submit')
    button.click()

    browser.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rz-main-page/div/main/main-page-content/app-fat-menu-tablet/nav/ul/li[2]/a').click()
    browser.get('https://rozetka.com.ua/mobile-phones/c80003/filter/')
    browser.get('https://rozetka.com.ua/apple_iphone_se_64gb_black/p205192903/')
    time.sleep(2)
    target = browser.find_element_by_link_text('Купить')
    actions = ActionChains(browser)
    actions.move_to_element(target)
    actions.perform()

    browser.find_elements_by_css_selector('#205192903>button.buy-button').click()
    browser.find_elements_by_class_name('header-actions__button_type_basket').click()

    
finally:
    time.sleep(15)
    browser.quit()