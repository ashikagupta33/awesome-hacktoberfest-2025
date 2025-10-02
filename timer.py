import time

def countdown(minutes, label):
    seconds = minutes * 60
    print(f"\n⏳ {label} - {minutes} minutes")
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_str = f"{mins:02d}:{secs:02d}"
        print(f"\r {time_str}", end="")
        time.sleep(1)
        seconds -= 1
    print(f"\n {label} complete!\n")

def pomodoro_session(cycles=4):
    for i in range(cycles):
        print(f"\n Pomodoro #{i+1}")
        countdown(25, "Focus Time")
        if i < cycles - 1:
            countdown(5, "Break Time")
    print(" All Pomodoro sessions complete!")

def main():
    print(" Welcome to Pomodoro Timer")
    try:
        cycles = int(input("How many Pomodoro cycles? (default 4): ") or "4")
        pomodoro_session(cycles)
    except ValueError:
        print(" Invalid input. Exiting.")

if __name__ == "__main__":
    main()
