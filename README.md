# Meal Time Activity
Create a python I/O program that asks the user for a 24-hour time format, then return a message if it is: Breakfast Time, Lunch Time, or Dinner Time depending on the user input.

# Time Condition Per Return
- Breakfast Time: 7:00 - 8:00
- Lunch Time: 12:00 - 13:00
- Dinner Time: 6:00 - 7:00

# Notes:
- Time in between the stated time conditions are accepted as True.
- Assume that the user input will always be in a 24-hours time format

# How To Test:
1. 7:00
> It's Breakfast Time!

2. 6:59
> ...

3. 12:48
> It's Lunch Time!

4. 6:27
> It's Dinner Time!

5. 25:00
> ...

6. 06:252
> ...

# Bonus (+5 exam):
- Allow the user to input an AM and PM format i.e.: `1:25PM` then convert it into 24-hour format before doing any condition check.

## How To Check:
1. 01:25 AM
> ...

2. 6:30 AM
> It's Breakfast Time!

3. 6:59 PM
> It's Dinner Time!