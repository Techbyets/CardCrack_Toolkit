import random
import time

# ANSI color escape codes for colored text output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
END = "\033[0m"

account_types = {
    1: "Savings",
    2: "Checking",
    3: "Transaction"
}

# Sample data for random generation
first_names = ["John", "Jane", "Alex", "Emily", "Michael", "Sarah", "David", "Laura"]
last_names = ["Doe", "Smith", "Johnson", "Brown", "Williams", "Jones", "Garcia", "Miller"]
security_questions = [
    "What is your mother's maiden name?",
    "What is the name of your first pet?",
    "What was the name of your elementary school?",
    "What city were you born in?"
]
streets = ["Main Street", "Oak Street", "Pine Avenue", "Elm Road", "Maple Street"]
cities = ["Anytown", "Springfield", "Rivertown", "Maplewood", "Greenfield"]
states = ["CA", "NY", "TX", "FL", "IL"]
email_domains = ["example.com", "mail.com", "test.com", "sample.com"]
random_answers = ["Smith", "Buddy", "Lincoln", "Chicago"]

# Functions to generate random data
def generate_random_name(gender):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

def generate_credit_card_number(card_type):
    card_length = 16
    if card_type == "Visa":
        prefix = "4"
    elif card_type == "Mastercard":
        prefix = "5"
    else:
        raise ValueError("Invalid card type.")
    
    remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(card_length - len(prefix) - 1)])
    card_number = prefix + remaining_digits
    checksum = luhn_checksum(card_number)
    
    return card_number + str(checksum)

def luhn_checksum(card_number):
    digits = [int(d) for d in card_number]
    odd_digits = digits[-2::-2]
    even_digits = [sum(divmod(2 * d, 10)) for d in digits[-1::-2]]
    total = sum(odd_digits + even_digits)
    return (10 - (total % 10)) % 10

def generate_expiration_date():
    month = random.randint(1, 12)
    year = random.randint(23, 30)  # assuming cards valid up to 2030
    return f"{month:02d}/{year}"

def generate_cvv():
    return f"{random.randint(100, 999)}"

def generate_balance():
    return f"${random.randint(100, 10000):,.2f}"

def generate_dob():
    year = random.randint(1950, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # to avoid invalid dates
    return f"{month:02d}/{day:02d}/{year}"

def generate_ssn():
    return f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"

def generate_security_questions():
    return {q: random.choice(random_answers) for q in security_questions}

def generate_address():
    street = random.choice(streets)
    city = random.choice(cities)
    state = random.choice(states)
    postal_code = f"{random.randint(10000, 99999)}"
    country = "United States"
    return f"{street}, {city}, {state}, {postal_code}, {country}"

def generate_email(name):
    username = name.lower().replace(" ", ".")
    domain = random.choice(email_domains)
    return f"{username}@{domain}"

def generate_phone_number():
    return f"+1 (555) {random.randint(100, 999)}-{random.randint(1000, 9999)}"

def get_card_type():
    print("Choose a card type:")
    print("1. Visa")
    print("2. Mastercard")
    choice = input("Enter the number corresponding to the card type: ")
    if choice == "1":
        return "Visa"
    elif choice == "2":
        return "Mastercard"
    else:
        print("Invalid choice. Please try again.")
        return get_card_type()

def get_gender():
    print("Choose a gender:")
    print("1. Male")
    print("2. Female")
    choice = input("Enter the number corresponding to the gender: ")
    if choice == "1":
        return "Male"
    elif choice == "2":
        return "Female"
    else:
        print("Invalid choice. Please try again.")
        return get_gender()

def show_banner():
    print(RED + "=======================================")
    print("           CardCrack Toolkit           ")
    print("                 Version 1.3           ")
    print("=======================================" + END)
    print()

def show_loading_screen():
    print(YELLOW + "Loading..." + END)
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(END)

def show_thank_you_message():
    print(GREEN + "\nThank you for using this tool!" + END)
    print(YELLOW + "For more tools and updates, visit my " + CYAN + "GitHub: https://github.com/Techbyets" + END)
    print(YELLOW + "You can also join my Telegram channel: " + CYAN + "https://t.me/DroidDevHub" + END)

# Main code
if __name__ == "__main__":
    show_loading_screen()
    show_banner()

    card_type = get_card_type()
    gender = get_gender()
    
    cardholder_name = generate_random_name(gender)
    credit_card_number = generate_credit_card_number(card_type)
    expiration_date = generate_expiration_date()
    cvv = generate_cvv()
    balance = generate_balance()
    dob = generate_dob()
    ssn = generate_ssn()
    security_qas = generate_security_questions()
    address = generate_address()
    email = generate_email(cardholder_name)
    phone = generate_phone_number()

    print(RED + "=======================================")
    print(BOLD + GREEN + "    Card Information Generated Successfully" + END)
    print(RED + "=======================================" + END)
    print()
    print(BOLD + f"Cardholder Name: {cardholder_name}" + END)
    print(BOLD + f"Date of Birth: {dob}" + END)
    print(BOLD + f"Social Security Number: {ssn}" + END)
    print(BOLD + f"Credit Card Number: {credit_card_number}" + END)
    print(BOLD + f"Card Type: {card_type}" + END)
    print(BOLD + f"Expiration Date: {expiration_date}" + END)
    print(BOLD + f"CVV: {cvv}" + END)
    print(BOLD + f"Balance: {balance}" + END)
    print()
    print(BOLD + "Security Questions:" + END)
    for question, answer in security_qas.items():
        print(BOLD + f"  {question} Answer: {answer}" + END)
    print()
    print(BOLD + f"Country: United States" + END)
    print()
    print(BOLD + f"Billing Address: {address}" + END)
    print()
    print(BOLD + f"Email Address: {email}" + END)
    print()
    print(BOLD + f"Phone Number: {phone}" + END)

    show_thank_you_message()
