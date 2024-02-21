hours1 = int(input("Enter the number of hours for the first timestamp: "))
minutes1 = int(input("Enter the number of minutes for the first timestamp: "))
seconds1 = int(input("Enter the number of seconds for the first timestamp: "))


hours2 = int(input("Enter the number of hours for the second timestamp: "))
minutes2 = int(input("Enter the number of minutes for the second timestamp: "))
seconds2 = int(input("Enter the number of seconds for the second timestamp: "))

total_seconds1 = hours1 * 3600 + minutes1 * 60 + seconds1
total_seconds2 = hours2 * 3600 + minutes2 * 60 + seconds2

# Calculate the difference in seconds
difference_seconds = total_seconds2 - total_seconds1

print(difference_seconds)
