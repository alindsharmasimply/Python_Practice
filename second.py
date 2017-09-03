seconds_per_day = 24 * 60 * 60
seconds_per_hour = 60 * 60
seconds_per_minute = 60
seconds = input("Enter the no. of seconds")

days = seconds / seconds_per_day
seconds = seconds % seconds_per_day

hours = seconds / seconds_per_hour
seconds = seconds % seconds_per_hour

minutes = seconds / seconds_per_minute
seconds = seconds / seconds_per_minute

print "The equivalent duration is %02d:%02d:%02d:%02d" % (days, hours, minutes, seconds)