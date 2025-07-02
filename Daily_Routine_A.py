"""
Name : Yash Chaudhari
Date : 01-07-2025
Project : Daily Routine Analyze 
"""
# hours of Sleep.
sleep = float(input('how many hours did you sleep ?'))

# hour of study.
study = float(input('how many hours did you study ?'))

# hour of free time.
free = float(input('how many hours you were free ?'))

#  hour of workout.
workout = float(input('how many hours you work out ?'))

# total  number of hours in a day.
total = float(sleep + study + free + workout)

# Check total numbers of hours is no more then 24 hours.
if total > 24 :
    print('you used ',total,' hours Today. it is Wrong there is only 24 hours in a day.')

# Checkin if the schedule is good or bad and give an  reviews or sugetions.
# Review on sleep
if  sleep <= 7.5 :
    print("you didn't sleep enough.")
if sleep == (8) :
    print('well done you sleep time is great.')
if sleep > 8:
    print('you sleep over.')

# Riview on study
if study > 3 :
    print("good job you study great !")
else :
    print("you need to study more this is not good for you future")

# Rivew on free time
if free > 4 :
    print("you spent too much on Phone/TV")
else :
    print("spent you free as doing stuff you enjoy ! ")

#Revew on workout

if workout <  0.5 :
    print("you atlest need to workout for 30 minutes.")
elif workout > 2.5 :
    print("you need give rest too the body for now dont do more then 2.5 hours of workout")
else :
    print("great keep it up")

# asking peerson feeling of the day
feeling = input("how do you feel today happy/sad/tired ?")

# giveing suggstion

# if happy
if feeling == 'happy':
    print("That's great to hear! Keep it up!")

# if sad
if  feeling == 'sad' :
    print("Sorry to hear that. Keep doing good things — tomorrow will be better.")

# if tired
if feeling == 'tired' :
    print("Take enough rest today and get ready for a better tomorrow.")