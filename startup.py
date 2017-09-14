from datetime import datetime 

current = datetime.now()
month = ["January", "Februray", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

month_num = current.month
day = str(current.day)
year = str(current.year)

hour = str(current.hour % 12)
minute = str(current.minute)
second = str(current.second)

print "Today's date is " + month[month_num - 1] + " " + day + ", " + year
print "The current time is " + hour +":" + minute + ":" + second