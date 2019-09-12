#Time Conversion Program
#Author: Ahmad As Sami
# Date: 25th May 2019
#Description: Find how many hours, minutes, and seconds.

total_secs=7684

hours=total_secs//3600
secs_still_remaining=total_secs%3600
minutes=secs_still_remaining//60
secs_still_remaining=secs_still_remaining%60
print(hours)
print(minutes)
print(secs_still_remaining)