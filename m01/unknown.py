### m01/unknown.py
import time

# Ask the user for a number of seconds
seconds = int(input("Enter the number of seconds for the countdown: "))

# Ask the user to hit enter when ready
input("Press enter when you're ready to start the countdown timer: ")

# Countdown
prev_message_len = 0
for remaining in range(seconds, -1, -1):
    # Create the f-string and assign to variable
    message = f"Seconds remaining: {remaining}"
    # Clear the previous message by printing spaces based on its length
    if prev_message_len > 0:
        print("\r" + " " * prev_message_len, end="", flush=True)
    # Print the new message
    print(f"\r{message}", end="", flush=True)
    prev_message_len = len(message)
    if remaining == 0:
        print("\a")
    else:
        time.sleep(1)
