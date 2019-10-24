import re


def test_phones_on_home_page(app): # тест читает данные с главной страницы, режет на части и сравнивает с формой редактирования
    contact_from_home_page=app.contact.get_contact_list()[0] # объект кот прочитали с главной страницы, проверка для 1го контакта (индекс 0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)    # получаем информацию о контакте из формы редактирования
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page) # сравниваем с результатом склейки


def test_phones_on_contact_view_page(app):# тест сравнивает данные с формы редактирования со страницей просмотра контакта
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)  # получаем информацию о контакте из формы редактирования
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone ==contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s) # регуляр выражение, 1й параметр - шаблон(что надо заменять), 2й - на что заменять,3й - где (тк в форме редактирования номер телефона может содержать эти символы  )


def merge_phones_like_on_home_page(contact):
   return "\n".join(filter(lambda x: x !="",
                           map(lambda x: clear(x),
                               filter(lambda x: x is not None,
                                      [contact.homephone,  contact.mobilephone, contact.workphone, contact.secondaryphone])))) # склеиваем с помощью перевода строки, map - применяем функцию lambda (clear) ко всем элементам списка,(перед этим делаем фильт, чтобы отобрать не пустые значения) потом к результату map применяем фильтр (оставляем все не пустые строки)
