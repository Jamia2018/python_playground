hours = (input("Enter Hours:"))
wage = int(input("Enter Hourly wages:"))
hours = hours.split()   
week_hours = [int(x) for x in hours]
total_hours = sum(week_hours)   
if total_hours <= 40:
     total_wages= wage * total_hours
   
else:
    total_wages = (40 * wage) + ((total_hours - 40) * wage * 1.5)
print("Total wages:", total_wages)