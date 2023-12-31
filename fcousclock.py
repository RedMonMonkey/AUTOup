import time

def pomodoro_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        minutes_remaining = seconds // 60
        seconds_remaining = seconds % 60
        print(f"Remaining Time: {minutes_remaining:02d}:{seconds_remaining:02d}")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Take a short break.")

# 设置专注时长为25分钟
pomodoro_timer(25)
