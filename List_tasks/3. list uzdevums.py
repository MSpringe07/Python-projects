def create_month_calendar():
    # Define the names of the days (shortened).
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # Create a list to represent the calendar.
    calendar = []

    # Create the header row with day names.
    header = "| ".join(days_of_week)
    calendar.append(header)
    # Fill in the calendar with day numbers.
    day_number = 1
    while day_number <= 31:
        week = []

        for _ in range(7):
            if day_number <= 31:
                week.append(f"{day_number:2d}")
                day_number += 1
            else:
                week.append("  ")  # Empty space for days beyond the month.

        calendar.append(" | ".join(week))
    
    return calendar

def main():
    calendar = create_month_calendar()

    # Print the calendar.
    for row in calendar:
        print(row)

if __name__ == "__main__":
    main()