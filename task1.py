from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:  # Проверка, что значение не пустое
            raise ValueError("Name cannot be empty")
        super().__init__(value)  # Вызов конструктора родительского класса Field
                
class Phone(Field):
    def __init__(self, value):
        if len(str(value)) != 10:  #валідація номеру
          raise ValueError("The number is not valid. Should be 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if not isinstance(phone, Phone):
            phone = Phone(phone)
            self.phones.append(phone.value)
    
    def remove_phone(self, phone):
        if not isinstance(phone, Phone):
            phone = Phone(phone)
        if phone.value in self.phones:
            self.phones.remove(phone.value)
            return self.phones
        raise ValueError("Dont have this phone on the list")
    
    def edit_phone(self, phone, new_phone):
        if not isinstance(phone, Phone):
            phone = Phone(phone)
        if not isinstance(new_phone, Phone):
            new_phone = Phone(new_phone)
        if not phone.value in self.phones:
            raise ValueError("Dont have this phone on the list. Cant be changed")
        index = self.phones.index(phone.value)
        self.phones[index] = new_phone.value

    def find_phone(self, phone_number):
        if not isinstance(phone_number, Phone):
            phone_number = Phone(phone_number)
        for phone in self.phones:
            if phone == phone_number.value:
                return phone_number
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"
    

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError("Value must be a Record instance")
        self.data[record.name.value] = record.phones

    def find(self, name):
        if name in self.data:
            phone_list = self.data[name]
            record = Record(name)
            for i in phone_list:
                record.add_phone(i)
        return record
    
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
        else:
            return "The name is not found"
        
    def __str__(self):
        result = f"------------My Phonebook------------\n"
        for i in self.data:
            message = f"Contact name: {i}, phones: {self.data[i]}\n"
            result = result + message
        return result + f"-------------------------------------"


# Перевірка з ДЗ
# book = AddressBook()

# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")

# # Додавання запису John до адресної книги
# book.add_record(john_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # Виведення всіх записів у книзі
     
# print(book)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# # Видалення запису Jane
# book.delete("Jane")
# print(book)