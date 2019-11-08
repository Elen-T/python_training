import re
from model.contacts import Contacts

# Задание №21: Переделать тесты для проверки информации о контактах на главной странице

def test_info_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    for contact in contact_from_home_page :
        assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(db.get_contact_by_id(contact.id))
        assert contact.all_emails_from_home_page == merge_emails_like_on_home_page(db.get_contact_by_id(contact.id))
        assert contact.firstname == (db.get_contact_by_id(contact.id).firstname).strip()
        assert contact.lastname == (db.get_contact_by_id(contact.id).lastname).strip()
        assert contact.address == (db.get_contact_by_id(contact.id).address).strip()


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work,
                                                                                           contact.phone2, contact.homephone]))))


def clear(s):
    return re.sub("[() -]", "",
                  s)  # регуляр выражение, 1й параметр - шаблон(что надо заменять), 2й - на что заменять,3й - где (тк в форме редактирования номер телефона может содержать эти символы  )


'''def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,
                                        contact.secondaryphone]))))  # склеиваем с помощью перевода строки, map - применяем функцию lambda (clear) ко всем элементам списка,(перед этим делаем фильт, чтобы отобрать не пустые значения) потом к результату map применяем фильтр (оставляем все не пустые строки)

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
    # склеиваем с помощью перевода строки, map - применяем функцию lambda (clear) ко всем элементам списка,(перед этим делаем фильт, чтобы отобрать не пустые значения) потом к результату map применяем фильтр (оставляем все не пустые строки)

def test_info_on_home_page(app):  #
    contact_from_home_page = app.contact.get_contact_list()[0]  # объект кот прочитали с главной страницы, проверка для 1го контакта (индекс 0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)  # получаем информацию о контакте из формы редактирования
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)  # сравниваем с результатом склейк
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address'''
