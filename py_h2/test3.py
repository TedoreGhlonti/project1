bank_account = {
    "owner": "Nino",
    "balance": 500,
    "status": "active",
    "limit": 1000
}

for k, v in bank_account.items():
    if k == "balance" and v < 100:
        print("Low balance alert!")
    elif k == "status" and v == "blocked":
        print("Contact the bank!")
    elif k == "limit" and v > 500 and bank_account["balance"] > 400:
        print("You are a VIP customer!")

            
            



