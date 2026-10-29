

slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


print("Welcome to the Parking Lot Program")

while True:
    print("--- Current Parking Lot Space ---")
    print(slots)
   
    filled = 0
    empty = 0
    for space in slots:
        if space == 1:
            filled = filled + 1
        else:
            empty = empty + 1
            
    print("Filled spaces: " + str(filled))
    print("Available spaces: " + str(empty))
    print("---------------------------------")
    
    print("1. Park automatically")
    print("2. Park in a specific slot")
    print("3. Leave a slot")
    print("4. Close program")

    choice = input("Pick an option (1-4): ")

    if choice == "1":
        found_space = False
        for index in range(20):
           if slots[index] == 0:
                slots[index] = 1
                slot_number = index + 1
                print("Success: Car parked automatically in slot " + str(slot_number))
                found_space = True
                break

