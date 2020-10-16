if opcion == 9:
    hoy = date.today()
    nacimiento = date(1997,9,1)

    diferencia = (hoy.year-nacimiento.year) * 12 + hoy.month - nacimiento.month
    print(f"han pasado {diferencia} meses desde {nacimiento} hasta hoy")