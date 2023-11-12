# Декоратор помилок (Error Decorator for function)
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Contact not found"
    return wrapper

contacts = {}

# Функція привітання (Function Hello)
@input_error
def hello():
    return "How can I help you?"

# Функція додавання контакту (Function add contacts to dict)
@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}"

# Функція зміни контакту (Function change contacts in dict)
@input_error
def change_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} changed to {phone}"
    else:
        raise IndexError

# Функція виводу номера телефона по імені (Function output phone number per name contact)
@input_error
def phone_number(name):
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}"
    else:
        raise IndexError

# Функція виводу всіх контактів (Function output all contacts in dict)
@input_error
def show_all():
    if not contacts:
        return "No contacts found"
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

# Основна функція бота (Main function)
def main():
    while True:
        command = input("Enter a command: ").lower()

        if command == "hello":
            print(hello())
            
        elif command.startswith("add"):
            _, name, phone = command.split(" ")
            print(add_contact(name, phone))

        elif command.startswith("change"):
            _, name, phone = command.split(" ")
            print(change_contact(name, phone))

        elif command.startswith("phone"):
            _, name = command.split(" ")
            print(phone_number(name))

        elif command == "show all":
            print(show_all())

        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()


