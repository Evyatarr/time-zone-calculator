# Time Zone Calculator

def time_shift(time, change):
    current_time = time.split(":")
    h = int(current_time[0])
    m = int(current_time[1])
    if 0 > m or m > 59:
        print("Invalid time inserted")
        time_zone_change()
    elif 0 > h or h > 23:
        print("Invalid time inserted")
        time_zone_change()
    else:
        pass

    h += int(change)
    h = h % 24
    h = str(h)
    m = str(m)
    print(f"The time is: {(h.zfill(2))}:{m.zfill(2)} ")


def time_zone_change():
    while True:
        enter_time = input("Enter time: \n")
        if (":") in enter_time:
            break
    while True:
        users_zone = input("Choose country:\n1.TLV\n2.LDN\n3.NYC\n4.TYO\n")
        if users_zone in ["TLV", "LDN", "NYC", "TYO", "1", "2", "3", "4"]:
            break
    if users_zone == "TLV" or users_zone == "1":
        time_shift(enter_time, "3")
    elif users_zone == "LDN" or users_zone == "2":
        time_shift(enter_time, "0")
    elif users_zone == "NYC" or users_zone == "3":
        time_shift(enter_time, "-4")
    elif users_zone == "TYO" or users_zone == "4":
        time_shift(enter_time, "9")

    
    
    
time_zone_change()
