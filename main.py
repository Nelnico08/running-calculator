import sys
sys.path.insert(0, "C:/Users/nelso/Calculadora_running_test/moduls")
from moduls.Running import *
from moduls.estimator import *
from moduls.converter import *

while True:
    #Preguntar al usuario si desea obtener el pace, time o distance
    answer = "wrong"
    while answer not in ["pace","time","distance"]:
        answer = input('What do you want to know? pace, time or distance?(type pace, time or distance) ').lower()

        if answer not in ["pace","time","distance"]:
            print('Please type pace, time or distance specifically')
    
    #Segun la respuesta dada, llamar a la funcion correspondiente
    if answer == "pace":
        mm, ss = Running.pace()
        seconds = secondsConverter(ss)
        print(f"\nPace (in minutes per kilometers): {mm}:{seconds}")
    elif answer == "time":
        crono = Running.time()
        hh, sec = divmod(crono,3600)
        mm, ss = divmod(sec, 60)
        mins = minsConverter(mm)
        seconds = secondsConverter(ss)
        print(f"\nThe time to complete the distance is: {hh}:{mins}:{seconds}")
    else:
        distance = Running.dist()
        print(f"\nDistance: {distance}km.")
    
    #Una vez el usuario dio todos los datos y obtuvo la informacion deseada,
    #mostrar los times y pace aproximados para otras distances
    print("\nYour approximate times and paces for other distances are:")
    estimator()
    break