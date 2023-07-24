import time
import os

def focus_clock(total_work_time, total_break_time):
    while True:
        # Work phase
        print("Focus on your work.")
        time.sleep(total_work_time)
        os.system("cls" if os.name == "nt" else "clear")  # Clear the console after work phase

        # Break phase
        print("Take a short break.")
        time.sleep(total_break_time)
        os.system("cls" if os.name == "nt" else "clear")  # Clear the console after break phase

if __name__ == "__main__":
    work_time_minutes = 25
    break_time_minutes = 5

    total_work_time = work_time_minutes * 60
    total_break_time = break_time_minutes * 60

    focus_clock(total_work_time, total_break_time)
