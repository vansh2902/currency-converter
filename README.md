# Currency Converter

A simple command-line currency converter written in Python. It converts any amount from one currency to another using live exchange rates from the free Frankfurter API.

## Features

- Live exchange rates from the Frankfurter API (api.frankfurter.app)
- Convert between any supported currency pair (USD, EUR, INR, GBP, JPY, and more)
- Enter the amount you want to convert
- Keeps running in a loop until you press q to quit

## Tech Used

- Python 3
- requests library
- Frankfurter REST API (returns rates as JSON)

## How to Run

1. Make sure Python 3 is installed.
2. Install the requests library:

   ```
   pip install requests
   ```

3. Run the script:

   ```
   python currency_converter.py
   ```

4. Type the currency you want to convert from (for example USD), the amount, and the currency you want to convert to (for example INR). Type q to quit.

## About

This is a beginner Python project. I built it to practice working with APIs, JSON data, loops, and user input. Feedback and suggestions are welcome!
