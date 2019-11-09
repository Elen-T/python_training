import re
from model.contacts import Contacts

# Задание №21: Переделать тесты для проверки информации о контактах на главной странице

def test_contact_info_on_home_page(app, db):
    contact_from_ui = sorted(app.contact.get_contact_list(), key=Contacts.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contacts.id_or_max)
    for db_contact in range(len(contact_from_db)):
        for ui_contact in range(len(contact_from_ui)):
            #assert contact_from_ui[ui_contact].id == contact_from_db[db_contact].id
            assert contact_from_ui[ui_contact].firstname == contact_from_db[db_contact].firstname
            assert contact_from_ui[ui_contact].lastname == contact_from_db[db_contact].lastname
            assert contact_from_ui[ui_contact].address == contact_from_db[db_contact].address
            assert contact_from_ui[db_contact].all_phones_from_home_page == "\n".join(
                filter(lambda x: x is not None,
                       [contact_from_db[db_contact].home_tel,
                        contact_from_db[db_contact].mobile_tel,
                        contact_from_db[db_contact].work_tel,
                        contact_from_db[db_contact].second_phone]))
        #ui_contact += 1
    #db_contact += 1

'''def test_info_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    for contact in contact_from_home_page :
        assert contact.all_emails_from_home_page == merge_emails_like_on_home_page(db.get_contact_by_id(contact.id))
        assert contact.firstname == (db.get_contact_by_id(contact.id).firstname).strip()
        assert contact.lastname == (db.get_contact_by_id(contact.id).lastname).strip()
        assert contact.address == (db.get_contact_by_id(contact.id).address).strip()
        assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(db.get_contact_by_id(contact.id))'''


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work, contact.phone2]))))


def clear(s):
    return re.sub("[() -]", "", s)  # регуляр выражение, 1й параметр - шаблон(что надо заменять), 2й - на что заменять,3й - где (тк в форме редактирования номер телефона может содержать эти символы  )


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
