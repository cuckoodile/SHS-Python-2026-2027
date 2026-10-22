# CONDITIONALS
# Syntax:
"""
if condition:
    execution block
    print
print()


elif condition:
    execution block

else:
    execution block
"""

# name = input("Who are you? ").title()

# BeaUTY AnD ThE BEaSt =title==> Beauty And The Beast
# BeaUTY AnD ThE BEaSt =capitalize==> Beauty and the beast
# DRY Principle

# if name == "Ian":
#     print(f"Hello {name}")

# elif name == "Chounce":
#     print(f"Hi {name}")

# elif name == "Pam":
#     print(f"Hi {name}")

# else:
#     print(f"Welcome {name}")

# SWITCH STATEMENT

# name = input("Who are you? ").title()

# match(name):
#     case "Ian":
#         print(f"Hi {name}")
#     case "Chounce":
#         print(f"Hi {name}")
#     case "Pam":
#         print(f"Hi {name}")
#     case _:
#         print(f"Welcome {name}")


time = input("What time is it? ")
# 00:00     1:25

hour, min = time.split(":")

hour = int(hour)
min = int(min)

print(f"Hour: {hour}  Minute: {min}")

if min > 60:
    print()

elif min < 0:
    print()

# Breakfast
elif hour == 6 or (hour == 7 and min == 0):
    print("It's Breakfast Time!")

# Lunch
elif hour == 12 or (hour == 13 and min == 0) :
    print("It's Lunch Time!")

# Dinner
elif hour == 18 or (hour == 19 and min == 0):
    print("It's Dinner Time!")

