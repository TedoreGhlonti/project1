months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()
    
    try:
        if "/" in date:
            m, d, y = date.split("/")
            month = int(m)
            day = int(d)
            year = int(y)
        
        elif "," in date:
            new_date = date.replace(",", "")
            m, d, y = new_date.split(" ")
        
            if m in months:
                month = months.index(m) + 1
                day = int(d)
                year = int(y)
            else:
                continue
        else:
            continue
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break

    except (ValueError, NameError, IndexError):
        pass

