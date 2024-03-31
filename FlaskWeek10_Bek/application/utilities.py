def get_time_slot(time):
    if time < 12:
        return "morning"
    elif time < 18:
        return "afternoon"
    else:
        return "evening"
