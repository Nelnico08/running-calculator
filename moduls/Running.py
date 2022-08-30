import decimal

class Running():

    distance = 0
    paceTime = 0
    crono = 0

    def pace():

        time, minuts, seconds = 0, 100, 100
        while True:
            try:
                print("\Input the time:\n")
                time = 3600 * int(input("hour/s: "))
                while minuts not in range (0,60):
                    minuts = int(input("Minutes: "))
                    if minuts not in range (0,60):
                        print("Please input a value between 0 y 59")
                time = time + 60*minuts
                while seconds not in range (0,60):
                    seconds = int(input("Seconds: "))
                    if seconds not in range(0,60):
                        print("Please input a value between 0 y 59")
                Running.crono = time + seconds
            except:
                print("Please input a number")
            else:
                break
        
        while True:
            try:
                print("\Input the distance in kilometers\n")
                Running.distance = float(input("distance: "))
            except:
                print("Please input a number")
            else:
                break
        
        pace = int(Running.crono/Running.distance)
        Running.paceTime = divmod(pace, 60)

        return Running.paceTime

    def time():

        pace, minuts, seconds = 0, 100, 100
        while True:
            try:
                print("\nInput the average race pace in minutes per kilometers:\n")
                while minuts not in range(0,60):
                    minuts = int(input("Minutes: "))
                    if minuts not in range(0,60):
                        print("Please input a value between 0 y 59")
                pace = 60 * minuts
                while seconds not in range(0,60):
                    seconds = int(input("Seconds: "))
                    if seconds not in range(0,60):
                        print("Please input a value between 0 y 59")
                pace = pace + seconds
            except:
                print("Please input a number")
            else:
                break
                
        while True:
            try:
                print("\nInput the distance in kilometers:\n")
                Running.distance = float(input("distance: "))
            except:
                print("Please input a number")
            else:
                break
        
        Running.crono = int(pace * Running.distance)

        return Running.crono

    def dist():

        time, min_crono, seg_crono, min_paceTime, seg_paceTime = 0, 100, 100, 100, 100
        while True:
            try:
                print("\nInput the time:\n")
                time = 3600 * int(input("Hour/s: "))
                while min_crono not in range(0,60):
                    min_crono = int(input("Minutes: "))
                    if min_crono not in range(0,60):
                        print("Please input a value between 0 y 59")
                time = time + 60 * min_crono
                while seg_crono not in range(0,60):
                    seg_crono = int(input("Seconds: "))
                    if seg_crono not in range(0,60):
                        print("Please input a value between 0 y 59")
                Running.crono = time + seg_crono
            except:
                print("Please input a number")
            else:
                break
                
        while True:
            try:
                print("\nInput the average race pace in minutes per kilometers:\n")
                while min_paceTime not in range(0,60):
                    min_paceTime = int(input("Minutes: "))
                    if min_paceTime not in range(0,60):
                        print("Please input a value between 0 y 59")
                pace = 60 * min_paceTime
                while seg_paceTime not in range(0,60):
                    seg_paceTime = int(input("Seconds: "))
                    if seg_paceTime not in range(0,60):
                         print("Please input a value between 0 y 59")
                Running.paceTime = pace + seg_paceTime
            except:
                print("Please input a number")
            else:
                break

        dist = Running.crono/Running.paceTime
        d = decimal.Decimal(dist)
        Running.distance = float(round(d,3))
        
        return Running.distance
