from collections import UserDict


class Field:                    # Створення базового класу.
    def __init__(self, value):
        self.value = value


class Name(Field):              # Клас для зберігання імені контакту.
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):             # Клас для зберігання номеру телефону.
    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def validate(self):         # Метод валідації номера телефону.
        if self.value is not None:
            if len(self.value) != 10 or not self.value.isdigit():
                raise ValueError("Phone number must contain 10 digits")


class Record:                   # Клас для зберігання та модифікації інформації.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):  # Метод додавання котакту.
        phone_field = Phone(phone)
        phone_field.validate()
        self.phones.append(phone_field)

    def remove_phone(self, phone):  # метод видалення контакту.
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone): # Метод редагування контакту.
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        raise ValueError(f'Phone: {old_phone} not found!')

    def find_phone(self, phone):    # Метод пошуку контакту.
        for p in self.phones:
            if p.value == phone:
                return p
        return None


class AddressBook(UserDict):        # Клас для зберігання та управління записів.
    def add_record(self, record):   # Додавання запису.
        self.data[record.name.value] = record

    def find(self, name):           # Пошук запису за ім'ям.
        return self.data.get(name)

    def delete(self, name):         # Видалення запису.
        if name in self.data:
            del self.data[name]


if 'main' == __name__:
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")