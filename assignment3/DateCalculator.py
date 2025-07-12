class DateCalculator:
    def __init__(self, year: object, month: object, day: object) -> None:
        self.year= year
        self.month = month
        self.day = day

    def calculate_day_of_the_week(self):
        #Adjust month and year for January and February
        if self.month == 1 or self.month == 2:
            self.month += 12
            self.year -= 1

        q = self.day
        m = self.month
        K = self.year % 100
        J = self.year // 100

        # Apply Zeller's Congruence formula
        h = (q+ (13* (m+1)) //5+K+(K//4) +(J//4) +5*J) % 7

        # Mapping h to days of the week
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]

#Taking user input
year = int(input("Enter the year (e.g., 2024): "))
month = int(input("Enter the month (e.g., 1-12): "))
day = int(input("Enter the day (e.g., 1-31): "))

date =  DateCalculator(year, month,day)
day_of_week = date.calculate_day_of_the_week()

months = ["", "January","February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#output
print(f"\nYay! {months [month]} {day}, {year} was a {day_of_week}!")
