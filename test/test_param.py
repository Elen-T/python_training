from selenium import webdriver
import pytest
import os
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link2', ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1","236899/step/1","236903/step/1","236904/step/1","236905/step/1"])
def test_guest_should_see_login_link(browser, link2):
    link = f"https://stepik.org/lesson/{link2}/"
    browser.get(link)
    #answer = math.log(int(time.time()))
    time.sleep(10)
    #input1 = browser.find_element_by_css_selector("textarea.string-quiz__textarea.ember-text-area.ember-view")
    #input1 = browser.find_element_by_class_name("textarea")
    input1 = browser.find_element_by_css_selector(".textarea")
    #input1 = browser.find_element_by_css_selector("div.quiz-component ember-view > textarea.textarea.string-quiz__textarea.ember-text-area.ember-view")
    #input1.send_keys(answer)
    #input1.send_keys(int(math.log(int(time.time()))))
    input1.send_keys(str(math.log(int(time.time()))))
    time.sleep(4)
    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    time.sleep(4)
    assert browser.find_element_by_class_name("smart-hints__hint").text == "Correct!"

