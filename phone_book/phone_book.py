phone_number = {}
lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
punctuations = ".'- "
allowed_letters = lower + upper + punctuations
allowed_digits = "0123456789"


def read(message):
    return input(message)


def read_name():
    while True:
        name = read("Enter the person’s name: ")
        if len(name) < 1:
            print("Name is too short")
            continue  # try to read another name
        invalid_letters = False
        for letter in name:
            if letter not in allowed_letters:
                print(f"Letter ’{letter}’ is not legal in a name; try again.")
                invalid_letters = True
                break

        if invalid_letters:
            continue
        return name


def read_number():
    while True:
        number = read("Enter the person’s phone number (10 digits): ")
        if len(number) != 10:
            print("Phone number must have exactly 10 digits; try again.")
            continue  # try to read another phone number
        invalid_digit = False
        for digit in number:
            if digit not in allowed_digits:
                print("Phone number must have exactly 10 digits; try again.")
                invalid_digit = True
                break
        if invalid_digit:
            continue
        return number


def read_query():
    return read("Enter the substring to search for: ")


def add():
    """
    Args:
        name: str valid person’s name
        number: str valid phone number

    adds the (name,phone) pair to the database
    """
    print("Add a person’s name and associated phone number.")
    name, number = read_name(), read_number()
    phone_number[name] = number


def delete():
    """
    Args:
        name: str valid person’s name

    removes that person’s item from the database
    """
    print("Delete a person’s name.")
    name = read_name()
    try:
        number = phone_number[name]
        del phone_number[name]
        print(f"Successfully deleted {(name, number)}")
    except KeyError:
        print(f"{name} is not in the database.")


def find():
    """
    Args:
        query: a str from the user that is to be used
         to search the names in the database

    Returns: a list of all (name, phone) where the query is a substring in name
    """
    print("Find database entries by substring of a person’s name.")
    query = read_query()
    for name, phone in phone_number.items():
        if query in name:
            print(f"Found ({name}, {phone})")


def show():
    print("Show all the items in the database.")
    for name, phone in phone_number.items():
        print(f"{name} has phone number {phone}.")


command_dict = {
    'a': add,
    'd': delete,
    'f': find,
    'q': quit,
    's': show

}


def main():
    while True:
        command_name = input("Enter a one-letter command [adfqs]: ")
        command = command_dict[command_name]
        # run the command
        command()


if __name__ == "__main__":
    main()
