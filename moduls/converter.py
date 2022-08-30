def minsConverter(mins):
    if mins < 10:
        minsToStr = str(mins)
        minuts = f"0{minsToStr}"
    else:
        minuts = mins
    
    return minuts
    
def secondsConverter (seconds):
    if seconds < 10:
        secondsToStr = str(seconds)
        sec = f"0{secondsToStr}"
    else:
            sec = seconds
        
    return sec