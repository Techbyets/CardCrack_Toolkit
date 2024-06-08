# CardCrack Toolkit

CardCrack Toolkit is a Python tool designed to generate realistic credit card and personal information for testing and development purposes.

## Features

- Generates random credit card numbers (Visa, Mastercard)
- Generates cardholder name, date of birth, SSN, expiration date, CVV, and balance
- Generates random security questions and answers
- Generates random addresses, email addresses, and phone numbers
- Customizable with different datasets for names, addresses, and more

## Prerequisites

Make sure you have Python installed on your system. You can install Python from [python.org](https://www.python.org/downloads/).

## Installation

1. **Install necessary packages:**

    If you're using a Debian-based system (termux), run:

    ```bash
    apt update
    apt upgrade
    apt install python
    apt install git
    ```

2. **Clone the repository:**

    ```bash
    git clone https://github.com/Techbyets/CardCrack_Toolkit.git
    cd CardCrack_Toolkit
    ```

## Usage

1. **Run the script:**

    ```bash
    python cardcrack_toolkit.py
    ```

2. **Follow the prompts:**

    - Choose the card type (Visa or Mastercard)
    - Choose the gender for the cardholder name
    - The tool will generate and display the card and personal information

## Example Output

plaintext
=======================================
    Card Information Generated Successfully
=======================================

Cardholder Name: Alex Smith
Date of Birth: 09/23/1954
Social Security Number: 719-29-3245
Credit Card Number: 4253363919998110
Card Type: Visa
Expiration Date: 03/23
CVV: 382
Balance: $6,315.00

Security Questions:
  What is your mother's maiden name? Answer: Doe
  What is the name of your first pet? Answer: Buddy
  What was the name of your elementary school? Answer: Lincoln Elementary
  What city were you born in? Answer: Springfield

Country: United States

Billing Address: Main Street, Rivertown, CA, 40684, United States

Email Address: alex.smith@sample.com

Phone Number: +1 (555) 735-4323


## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome any improvements and suggestions.

## Contact

For more tools and updates, visit my [GitHub](https://github.com/Techbyets). You can also join my Telegram channel: [DroidDevHub](https://t.me/DroidDevHub).

## Disclaimer

This tool is intended for educational and testing purposes only. Do not use the generated information for any illegal activities.
