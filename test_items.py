import time


def test_button_add_to_basket_exist_on_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
    print("страница товара на сайте содержит кнопку добавления в корзину")


