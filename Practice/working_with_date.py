from datetime import date, time, datetime

def main():
    # today = date.today()
    # print("Today is {}".format(today) )
    # print("Date components: {} {} {}".format(today.day, today.month, today.year))
    # print("Today's weekday #: {}".format(today.weekday()) )

    current_datetime = datetime.now()
    print("Now: {}".format(current_datetime))
    print(current_datetime.strftime("%Y"))
    print(current_datetime.strftime("%A, %d %B, %y"))


if __name__ == "__main__":
    main()