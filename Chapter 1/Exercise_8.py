current_hour = int(input("Enter the current hour: "))
waiting_time = int(input("How long do you want to wait: "))
alarm_sound = (current_hour + waiting_time) % 24

print("The alarm will sound at " + str(alarm_sound) + "h.")