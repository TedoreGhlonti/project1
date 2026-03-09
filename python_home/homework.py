users = [
    {
        "name": "Lasha",
        "contacts": {"email": "lasha@gmail.com", "city": "Tbilisi"}
    },
    {
        "name": "Mari",
        "contacts": {"email": "mari@gmail.com", "city": "Batumi"}
    }
]

def get_user_emails(user_list):
    emails = []
    for user in user_list:
        new_email = user["contacts"]["email"]
        emails.append(new_email)

    return emails

result = get_user_emails(users)
print(result)




