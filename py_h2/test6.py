hotel = {
    "Room 101": {"status": "free", "price": 100},
    "Room 102": {"status": "free", "price": 80},
}

while True:
    print("\n--- Hotel menu ---")
    print("1. See all rooms")
    print("2. Book room")
    print("3. Exit")
   
    
    choice = input("Choose option (1/2/3): ")

    if choice == "1":
        print(hotel)
    
    elif choice == "2":
        room = input("Which room do you want? ")
        if room in hotel and hotel[room]["status"] == "free":
            hotel[room]["status"] = "occupied"
            print(f"✅ {room} Booked!")
        else:
            print("❌ Room is booked or there is no room!.")
            
    elif choice == "3":
        print("Bye!")
        break  # ეს წყვეტს ციკლს და თიშავს პროგრამას
    
        
