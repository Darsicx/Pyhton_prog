import datetime
import pytz
import random

contador=0
diccionario=dict()

for x in range(1,10):
    diccionario[x]=pytz.all_timezones[random.randint(1,len(pytz.all_timezones))]
for y in sorted(diccionario):
    print("{} ".format(y)+diccionario[y])
while True:
    valor = int(input("Ingresa el numero de la zona horaria a mostrar la hora: "))

    if valor > 0 and valor < 10:
        tzToDisplay=pytz.timezone(diccionario[valor])
        localTime=datetime.datetime.now(tz=tzToDisplay)
        print("{}: {}".format(diccionario[valor],localTime))
        print("{}: {}".format(diccionario[valor],datetime.datetime.utcnow()))

    elif valor == 0:
        print("El programa se ha terminado")
        break
    else:
        print("Ingrese un numero valido")
