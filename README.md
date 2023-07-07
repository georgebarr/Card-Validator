# Credit Card Validator

<br>

*Please note that there is currently no active development ongoing for this project. It is expected to remain as it is, unless there are specific updates or feature requests in the future.*

<br>

## Description

<br>

This GitHub repository contains a simple Python program designed to validate credit card numbers. The program allows users to input a credit card number, and it will determine whether the provided card number is valid or not. 

This program can be used as a starting point for implementing credit card validation logic into larger projects or as a standalone tool for verifying card numbers. It offers a straightforward and user-friendly way to determine the validity of credit card numbers.

<br>

## Test Credit Card Account Numbers

<br>

| Credit Card Type          | Credit Card Number     |
|---------------------------|-----------------------|
| American Express          | 378282246310005       |
| American Express          | 371449635398431       |
| American Express Corporate| 378734493671000       |
| Australian BankCard       | 5610591081018250      |
| Diners Club               | 30569309025904        |
| Diners Club               | 38520000023237        |
| Discover                  | 6011111111111117      |
| Discover                  | 6011000990139424      |
| JCB                       | 3530111333300000      |
| JCB                       | 3566002020360505      |
| MasterCard                | 5555555555554444      |
| MasterCard                | 5105105105105100      |
| Visa                      | 4111111111111111      |
| Visa                      | 4012888888881881      |
| Visa                      | 4222222222222         |

<i>All information from [paypalobjects.com](https://www.paypalobjects.com/en_AU/vhelp/paypalmanager_help/credit_card_numbers.htm).</i>

<br>

## Installation & Usage

<br>

1. Clone the repository:
  ```bash
  git clone https://github.com/georgebarr/card-validator.git
  ```

2. Navigate to the project directory:
  ```bash
  cd card-validator
  ```

3. Run the program:
  ```bash
  python cardValidator.py
  ```

*Depending on your operating system and shell, you may need to use `python3` instead of `python`.*

<br>

## Steps used

<br>

1. Removes any '-' or ' ' _(spaces)_ in the card number.

<br>

2. Adds all digits in the odd places from right to left.

<br>

3. Doubles every second digit from right to left. If the result is a two-digit number, then the program adds the two numbers together to get a single digit _(e.g. 18 = 1 and 8 = 9)_

<br>

4. Sums the totals of the previous two steps and if the sum is divisible by 10, the credit card number is valid.

<br>

## Inspiration

<br>

The inspiration and idea for this project came from [Bro Code](https://www.youtube.com/channel/UC4SVo0Ue36XCfOyb5Lh1viQ) on YouTube. 

<br>
