"""This is the programm for creating a phonebook and working with it.""" 

import json
import sys

HEADER = """Програма для управління особистою телефонною книгою.
Функціональність дозволяє:
"""

def print_functionality(): # displaying a list of possible functional options on the screen
    print(HEADER)
    print('0. Друк повідомлення про допомогу.')
    print("1. Створити новий контакт.")
    print("2. Показати всі контакти.")
    print("3. Пошук по імені.")
    print("4. Пошук за прізвищем.")
    print("5. Пошук за ПІБ.")
    print("6. Пошук за номером телефону.")
    print("7. Пошук за містом або областю.")
    print("8. Видалити запис для вказаного номера телефону.")
    print("9. Оновити запис для вказаного номера телефону.")
    print("10. Вийти")

def load_phonebook(filename): # downloading the phonebook from a file in JSON format
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено. Створіть новий файл.")
        return {}
    except json.JSONDecodeError:
        print("Помилка читання JSON даних.")
        return {}

def save_phonebook(filename, phonebook): # saving the phone book to a file in JSON format
    with open(filename, 'w') as file:
        json.dump(phonebook, file, indent=4)

def create_contact(phonebook): # creating a new contact in the phone book
    first_name = input("Введіть ім'я: ")
    last_name = input("Введіть прізвище: ")
    middle_name = input("Введіть по-батькові: ")
    phone_number = input("Введіть номер телефону: ")
    city = input("Введіть місто: ")
    region = input("Введіть область: ")
    phonebook[phone_number] = {
        "Ім'я": first_name,
        "Прізвище": last_name,
        "По-батькові": middle_name,
        "Повне ім'я": f"{first_name} {middle_name} {last_name}",
        "Номер телефону": phone_number,
        "Місто": city,
        "Область": region
    }

def show_phonebook(phonebook): # displaying all contacts in the phone book
    for phone_number, details in phonebook.items():
        print(f"{details['full_name']} - {phone_number} - {details['city']}, {details['region']}")

def search_entry(phonebook, key, value): # search for contacts in the phone book
    results = [entry for entry in phonebook.values() if entry.get(key) == value]
    for result in results:
        print(result)

def delete_entry(phonebook, phone_number): # deleting an entry from the phone book
    if phone_number in phonebook:
        del phonebook[phone_number]
        print(f"Запис з номером телефону {phone_number} видалено.")
    else:
        print("Номер телефону не знайдено в телефонній книзі.")

def update_entry(phonebook, phone_number): # updating information about a contact in the phone book
    if phone_number in phonebook:
        first_name = input("Введіть нове ім'я: ")
        last_name = input("Введіть нове прізвище: ")
        middle_name = input("Введіть нове по-батькові: ")
        city = input("Введіть нове місто: ")
        region = input("Введіть нову область: ")
        phonebook[phone_number].update({
            "Ім'я": first_name,
            "Прізвище": last_name,
            "По-батькові": middle_name,
            "Повне ім'я": f"{first_name} {middle_name} {last_name}",
            "Місто": city,
            "Область": region
        })
        print(f"Запис з номером телефону {phone_number} оновлено.")
    else:
        print("Номер телефону не знайдено в телефонній книзі.")

def main(): # basic phonebook management program
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть назву телефонної книги як перший аргумент.")
        return
    filename = sys.argv[1]
    phonebook = load_phonebook(filename)
    print_functionality()
    
    while True:
        choice = int(input("Ваш вибір: "))
        
        if choice == 0:
            print_functionality()
        elif choice == 1:
            create_contact(phonebook)
        elif choice == 2:
            show_phonebook(phonebook)
        elif choice == 3:
            name = input("Введіть ім'я для пошуку: ")
            search_entry(phonebook, "first_name", name)
        elif choice == 4:
            surname = input("Введіть прізвище для пошуку: ")
            search_entry(phonebook, "last_name", surname)
        elif choice == 5:
            full_name = input("Введіть ПІБ для пошуку: ")
            search_entry(phonebook, "full_name", full_name)
        elif choice == 6:
            phone_number = input("Введіть номер телефону для пошуку: ")
            search_entry(phonebook, "phone_number", phone_number)
        elif choice == 7:
            city = input("Введіть місто для пошуку: ")
            search_entry(phonebook, "city", city)
        elif choice == 8:
            phone_number = input("Введіть номер телефону для видалення: ")
            delete_entry(phonebook, phone_number)
        elif choice == 9:
            phone_number = input("Введіть номер телефону для оновлення: ")
            update_entry(phonebook, phone_number)
        elif choice == 10:
            save_phonebook(filename, phonebook)
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":     
    main()