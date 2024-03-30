def get_time_slot(time):
    if time < 12:
        return "Morning"
    elif time < 16:
        return "Afternoon"
    else:
        return "Evening"
