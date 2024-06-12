from datetime import datetime
from datetime import date

fecha=datetime.now().isoformat()
print(fecha)
f=list(fecha.split("-"))
año=int(f[0])
mes=int(f[1])
dia=int(f[2][0]+f[2][1])

fecha=date(año,mes,dia)

print(fecha)
