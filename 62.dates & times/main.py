
import datetime

date = datetime.date(2025, 1, 2)

print(date)


# --- to get the date right now ----
today = datetime.date.today()

print(today)



# ---- work with time --------------
time = datetime.time(12, 30, 0)

print(time)


# --- to get the time right now -------
now = datetime.datetime.now()

# we can format the appearance of the string 
# https://docs.python.org/3/library/datetime.html - you can get idea how to add format specifiers
now = now.strftime("%H:%M:%S %d-%m-%y")

print(now)



# ------ exercise - we will see the current date and time has passed a target date and time ----------
target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")

