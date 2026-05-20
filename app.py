from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import logica

app = Flask(__name__)

# Conexión a MySQL (ajustá con tus credenciales reales)
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TU_CONSTRASEÑA",
    database="mi_base"
)
cursor = conexion.cursor()

# ------------------ PÁGINA PRINCIPAL ------------------
@app.route("/")
def menu():
    return render_template("menu.html")

# ------------------ CÁLCULO DE SUELDO ------------------
@app.route("/calculo")
def calculo():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    ventas_300 = int(request.form["ventas_300"])
    ventas_600 = int(request.form["ventas_600"])
    ventas_1000 = int(request.form["ventas_1000"])
    zona_a = int(request.form["zona_a"])
    zona_b = int(request.form["zona_b"])
    zona_c = int(request.form["zona_c"])

    tarjeta = int(request.form["tarjeta"])
    portabilidad = int(request.form["portabilidad"])
    faltas = request.form["faltas"]

    ventas = [300]*ventas_300 + [600]*ventas_600 + [1000]*ventas_1000
    total_ventas = len(ventas)

    total_clusters = zona_a + zona_b + zona_c
    if total_clusters > total_ventas:
        return "Error: no puede haber más zonas que ventas"

    cluster = ["A"]*zona_a + ["B"]*zona_b + ["C"]*zona_c

    comisiones = logica.calcular_comision(ventas)
    cluster_total = logica.calcular_cluster(cluster)
    sueldo_basico = logica.basico(total_ventas)
    premio_extra = logica.premio(total_ventas)

    credito = tarjeta * 10000
    portabilidad_total = portabilidad * 17000
    viatico = 100000 if faltas == "no" else 0

    total = (comisiones + cluster_total + sueldo_basico + premio_extra +
             credito + portabilidad_total + viatico)
    total_neto = (total / 100) * 79

    return render_template("resultado.html",
                           ventas=total_ventas,
                           comisiones=comisiones,
                           cluster_total=cluster_total,
                           sueldo_basico=sueldo_basico,
                           premio_extra=premio_extra,
                           credito=credito,
                           portabilidad=portabilidad_total,
                           viatico=viatico,
                           total=total,
                           total_neto=total_neto)

# ------------------ NUEVA VENTA ------------------
@app.route("/nueva_venta")
def nueva_venta():
    return render_template("nueva_venta.html")

@app.route("/guardar_venta", methods=["POST"])
def guardar_venta():
    datos = (
        request.form["fecha_venta"],
        request.form["nombre"],
        request.form["apellido"],
        request.form["dni"],
        request.form["calle"],
        request.form["altura"],
        request.form["entre_calle1"],
        request.form["entre_calle2"],
        request.form["entre_calle3"],
        request.form["localidad"],
        request.form["cp"],
        request.form["mail"],
        request.form["telefono"],
        request.form["metodo_pago"],
        request.form["observaciones"],
        request.form["estado"],
        request.form["fecha_cumplida"] if request.form["estado"] == "cumplida" else None
    )

    cursor.execute("""
        INSERT INTO ventas (
            fecha_venta, nombre, apellido, dni, calle, altura,
            entre_calle1, entre_calle2, entre_calle3, localidad, cp,
            mail, telefono, metodo_pago, observaciones, estado, fecha_cumplida
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, datos)
    conexion.commit()

    return redirect(url_for("nueva_venta"))

# ------------------ BUSCAR VENTAS ------------------
@app.route("/buscar_ventas")
def buscar_ventas():
    return render_template("buscar_ventas.html")

@app.route("/resultado_busqueda", methods=["GET"])
def resultado_busqueda():
    filtro = request.args
    query = "SELECT * FROM ventas WHERE 1=1"
    valores = []

    if filtro.get("nombre"):
        query += " AND nombre LIKE %s"
        valores.append("%" + filtro["nombre"] + "%")
    if filtro.get("apellido"):
        query += " AND apellido LIKE %s"
        valores.append("%" + filtro["apellido"] + "%")
    if filtro.get("dni"):
        query += " AND dni = %s"
        valores.append(filtro["dni"])
    if filtro.get("estado"):
        query += " AND estado = %s"
        valores.append(filtro["estado"])
    if filtro.get("fecha_venta"):
        query += " AND fecha_venta = %s"
        valores.append(filtro["fecha_venta"])

    cursor.execute(query, valores)
    resultados = cursor.fetchall()

    return render_template("resultado_busqueda.html", ventas=resultados)

# ------------------ MAIN ------------------
if __name__ == "__main__":
    app.run(debug=True)
