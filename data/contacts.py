# отдельный пакет работы с тестовыми данными для теста добавление контакта
from model.contacts import Contacts

testdata = [
    Contacts(firstname="firstname1", middlename="middlename1", lastname="lastname1", nickname="nickname1"),
    Contacts(firstname="firstname2", middlename="middlename2", lastname="lastname2", nickname="nickname2"),
]
