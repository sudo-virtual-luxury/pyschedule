# -*- coding: utf-8 -*-

import time

horaActual = time.strftime("%H")
#horaActual = 17
siguienteHora = int(horaActual) + 1
diaActual = time.strftime("%A")
#diaActual = "Saturday"

horario = {"Sunday":{"":""},"Saturday":{"":""},"Monday":{"14":"De.Sus","15":"De.Sus","16":"Inv.Opera","17":"Inv.Opera","18":"Fis.Gen","19":"Fis.Gen"},"Tuesday":{"14":"Estr.Dat","15":"Estr.Dat","16":"Inv.Opera","17":"Inv.Opera","18":"Cult.Emp","19":"Fis.Gen"},"Wednesday":{"15":"Estr.Dat","16":"Estr.Dat","17":"Estr.Dat","18":"Calc.Vect","19":"Calc.Vect"},"Thursday":{"14":"De.Sus","15":"De.Sus","16":"De.Sus","17":"Calc.Vect","18":"Fis.Gen","19":"Fis.Gen"},"Friday":{"15":"Cult.Emp","16":"Cult.Emp","17":"Cult.Emp","18":"Calc.Vect","19":"Calc.Vect"}}

dia = horario.get(diaActual, "--")
clase = dia.get(str(horaActual), "--")
nextclase = dia.get(str(siguienteHora), "--")


if int(horaActual) > 12:
	hora12 = str(int(horaActual)-12) + " PM"
else:
	hora12 = str(horaActual) + " AM"

#datos = "[", diaActual, ":", str(hora12), ": ", clase, ", Next: ", nextclase, "]"
datos = "[" + diaActual + ", " + str(hora12) + ": " + clase + ", Next: " + nextclase + "]"
print datos
archivo = open("data.txt","w")
archivo.write(datos)
archivo.close()
