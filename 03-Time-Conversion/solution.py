# Problem 3: Time Conversion
def timeConversion(s):
    period = s[-2:]
    hour = int(s[:2])
    rest = s[2:-2]
    
    if period == "AM":
        if hour == 12:
            hour_str = "00"
        else:
            hour_str = f"{hour:02d}"
    else:  # PM
        if hour == 12:
            hour_str = "12"
        else:
            hour_str = f"{hour + 12:02d}"
            
    return f"{hour_str}{rest}"