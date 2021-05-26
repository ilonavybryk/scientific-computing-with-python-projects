def add_time(start, duration, day=None):

    starttime, period = start.split()
    start_h, start_m = starttime.split(':')
    duration_h, duration_m = duration.split(':')
    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    strattime_in_m = int(start_h) * 60 + int(start_m)
    duration_in_m = int(duration_h) * 60 + int(duration_m)
    total_m = strattime_in_m + duration_in_m

    def new_hours(minutes):
        new_hour = (minutes // 60) % 12
        if new_hour == 0:
            new_hour = 12
        
        return new_hour
    new_h = new_hours(total_m)
    def new_minutes(minutes):
        new_minute = (minutes % 60)
        if new_minute < 10:
            new_minute = "0" + str(new_minute)
        else:
            new_minute = str(new_minute)
        return new_minute
    new_m = new_minutes(total_m)
    def new_periods(p):
        if p == "PM" and (total_m // (60*12)) % 2 == 0:
            new_period = "PM"
        elif p == "AM" and (total_m // (60*12)) % 2 == 1:
            new_period = "PM"
        else:
            new_period = "AM"
        return new_period
    new_p = new_periods(period)
    def day_count(minutes, period):
        if period == "AM":
            days_counts =  minutes // (60 * 24)
            if days_counts < 1 :
                x = ""
            if days_counts == 1:
                x = " (next day)"
            if days_counts > 1:
                x = "(" + str(days_counts) + " days later)"
            return x
        if period == "PM":
            days_counts =  (minutes + 12 * 60) // (60 * 24)
            if days_counts < 1 :
                y = ""
            elif days_counts == 1:
                y = " (next day)"
            else: 
                y = "(" + str(days_counts) + " days later)"
            return y
    day_c = day_count(total_m, period)
    if period == "AM":
        how_many_days = total_m // (60 * 24)
    else:
        how_many_days = (total_m + 12 * 60) // (60 * 24)

    if day != None:
        week_day_count = int(weekday.index(day.lower().capitalize())) + int(how_many_days)
        new_weekday = ", " + weekday[week_day_count % 7] 
    else:
        new_weekday = ""
    
    new_time = str(new_h) + ':' + str(new_m) + ' ' + str(new_p) + new_weekday + ' ' + day_c 
    return new_time

print(add_time("8:16 PM", "466:02", "tuesday"))