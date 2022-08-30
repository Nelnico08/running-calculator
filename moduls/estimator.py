from Running import *
from converter import *

def estimator():
    for i in range(1,41):
        if i < 10:
            t = int(Running.crono*(i/Running.distance)**1.06)
            hh, sec = divmod(t, 3600)
            mm, ss = divmod(sec,60)
            mmConverter = minsConverter(mm)
            ssConverter = secondsConverter(ss)
            pace = int(t/i)
            paceTime = divmod(pace,60)
            mins, seconds = paceTime
            minsConvert = minsConverter(mins)
            secondsConvert = secondsConverter(seconds)
            print(f"\nTime({i}km): {hh}:{mmConverter}:{ssConverter}")
            print(f"Pace({i}km): {minsConvert}:{secondsConvert}")
        elif i == 20:
            t = int(Running.crono*(21.1/Running.distance)**1.06)
            hh, sec = divmod(t, 3600)
            mm, ss = divmod(sec,60)
            mmConverter = minsConverter(mm)
            ssConverter = secondsConverter(ss)
            pace = int(t/21.1)
            paceTime = divmod(pace,60)
            mins, seconds = paceTime
            minsConvert = minsConverter(mins)
            secondsConvert = secondsConverter(seconds)
            print(f"\nTime(half maraton): {hh}:{mmConverter}:{ssConverter}")
            print(f"Pace(half maraton): {minsConvert}:{secondsConvert}")
        elif i == 40:
            t = int(Running.crono*(42.2/Running.distance)**1.06)
            hh, sec = divmod(t, 3600)
            mm, ss = divmod(sec,60)
            mmConverter = minsConverter(mm)
            ssConverter = secondsConverter(ss)
            pace = int(t/42.2)
            paceTime = divmod(pace,60)
            mins, seconds = paceTime
            minsConvert = minsConverter(mins)
            secondsConvert = secondsConverter(seconds)
            print(f"\nTime(maraton): {hh}:{mmConverter}:{ssConverter}")
            print(f"Pace(maraton): {minsConvert}:{secondsConvert}")
        elif i % 5 == 0:
            t = int(Running.crono*(i/Running.distance)**1.06)
            hh, sec = divmod(t, 3600)
            mm, ss = divmod(sec,60)
            mmConverter = minsConverter(mm)
            ssConverter = secondsConverter(ss)
            pace = int(t/i)
            paceTime = divmod(pace,60)
            mins, seconds = paceTime
            minsConvert = minsConverter(mins)
            secondsConvert = secondsConverter(seconds)
            print(f"\nTime({i}km): {hh}:{mmConverter}:{ssConverter}")
            print(f"Pace({i}km): {minsConvert}:{secondsConvert}")
        else:
            pass