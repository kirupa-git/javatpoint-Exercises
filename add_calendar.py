import calendar

try:
    user_year = int(input("Year:"))
    user_month = int(input("Month:"))

    def request_calendar():
        print(calendar.month(user_year, user_month))
    request_calendar()

except ValueError:
    print("Entered input is invalid")






