# Name : Ida Bagus Ryogassa Avatara
# ID   : 2440100323


def convert_to_days():
    hours = int(input("Enter Number of Hours: "))
    minutes = int(input("Enter Number of Minutes: "))
    seconds = int(input("Enter Number of Seconds: "))
    return get_days(hours, minutes, seconds)


def get_days(hours, minutes, seconds):
    days = round(float((hours * 3600 + minutes * 60 + seconds) / 86400), 4)
    print("The Number of Days is: ", days)


convert_to_days()
