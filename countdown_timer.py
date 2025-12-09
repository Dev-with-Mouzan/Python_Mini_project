import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!")

if __name__ == "__main__":
    print("Countdown Timer")
    try:
        t = int(input("Enter time in seconds: "))
        countdown_timer(t)
    except ValueError:
        print("Invalid input. Please enter a number.")
