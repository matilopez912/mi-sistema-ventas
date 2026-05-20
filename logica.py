# logica.py

def calcular_comision(ventas):
    total_comision = 0
    total_ventas = len(ventas)

    if total_ventas <= 10:
        total_comision = total_ventas * 30000
    elif total_ventas >= 11:
        ventas_extra = ventas[11:]
        for venta in ventas_extra:
            if venta == 300:
                total_comision += 30000
            elif venta == 600:
                total_comision += 32000
            elif venta == 1000:
                total_comision += 34000
    return total_comision


def calcular_cluster(cluster):
    total_cluster = 0
    for zona in cluster:
        if zona == "A":
            total_cluster += 10000
        elif zona == "B":
            total_cluster += 0
        elif zona == "C":
            total_cluster -= 5000
    return total_cluster


def basico(total_ventas):
    return 500000 if total_ventas >= 11 else 0


def premio(total_ventas):
    if total_ventas >= 40:
        return 200000
    elif total_ventas >= 30:
        return 150000
    elif total_ventas >= 20:
        return 100000
    else:
        return 0
