import requests
print("----Currency Converter----")

while True:
    
    cur1 = input("Enter which currency you what to convert from :").upper()
    if cur1 == "q".upper():
            print("Thank you!")
            break
    
    amount = float(input("Enter amount : "))
    cur2 = input("Enter which currency you what to convert to :").upper()

    response = requests.get(f"https://api.frankfurter.app/latest?from={cur1}&to={cur2}")

    data = response.json()
    
    if "rates" not in data:
        print("Sorry, this currency is not supported.")
        print()
        continue
        
    rate = data["rates"][cur2]

    final_amount = amount*rate

    print(f"Current rate : 1 {cur1} = {rate} {cur2}")
    print(f"{cur1} {amount} in {cur2} = {cur2} {final_amount}")
    print("press q to quit ")
    
