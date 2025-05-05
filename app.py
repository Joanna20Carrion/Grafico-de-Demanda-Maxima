from flask import Flask, render_template, request, send_file
import pandas as pd
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Obtener archivo cargado
    file = request.files['file']
    start_date = request.form['start_date']
    end_date = request.form['end_date']

    # Leer el archivo Excel
    df = pd.read_excel(file, sheet_name="Hoja1")

    # Convertir la columna 'Fecha' a tipo datetime
    df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
    df["Fecha"] = df["Fecha"].dt.floor("30min")
    df["Día"] = df["Fecha"].dt.strftime("%Y-%m-%d")
    df["Hora"] = df["Fecha"].dt.time

    # Filtrar los datos según el rango de fechas
    df_filtrado = df.loc[(df["Día"] >= start_date) & (df["Día"] <= end_date)].copy()

    # Determinar si es Residual (0) o Diésel (>0)
    df_filtrado.loc[:, "Tipo"] = df_filtrado["Residual y Diésel"].apply(lambda x: "Diésel" if x > 0 else "Residual")

    # Encontrar la hora de máxima demanda por día
    max_demand_per_day = df_filtrado.loc[df_filtrado.groupby("Día")["Demanda"].idxmax()]
    colores = max_demand_per_day["Tipo"].map({"Diésel": "red", "Residual": "blue"})
    max_demand_per_day["Hora_num"] = max_demand_per_day["Hora"].apply(lambda x: x.hour * 60 + x.minute)

    # Crear el gráfico
    plt.figure(figsize=(20, 10))
    plt.axhspan(10 * 60, 16 * 60, color="yellow", alpha=0.3, zorder=0)  # Sombreado amarillo

    # Agregar puntos (scatter plot)
    plt.scatter(max_demand_per_day["Día"], max_demand_per_day["Hora_num"], c=colores, s=8, alpha=0.7, zorder=5)

    # Agregar líneas punteadas verdes el primer día de cada mes
    primeros_de_mes = pd.date_range(start_date, end_date, freq="MS").strftime("%Y-%m-%d")
    for fecha in primeros_de_mes:
        plt.axvline(x=fecha, color="green", linestyle="dotted", alpha=0.7, zorder=2)

    # Líneas punteadas rojas horizontales a las 12:30 y 14:30
    plt.axhline(y=12.5 * 60, color="red", linestyle="dotted", alpha=0.7, zorder=2)
    plt.axhline(y=14.5 * 60, color="red", linestyle="dotted", alpha=0.7, zorder=2)

    # Configurar etiquetas y título
    plt.xlabel("Día", fontsize=10)
    plt.ylabel("Hora", fontsize=10)
    plt.title("Distribución de Despacho Diésel en Horas de Máxima Demanda", fontsize=12)

    # Configuración del eje X
    fechas_disponibles = pd.date_range(start_date, end_date, freq="5D").strftime("%Y-%m-%d")
    plt.xticks(fechas_disponibles, rotation=60, fontsize=2)

    # Configuración del eje Y con etiquetas de tiempo legibles
    horas_disponibles = pd.date_range("00:00", "23:30", freq="30min").time
    horas_numericas = [h.hour * 60 + h.minute for h in horas_disponibles]
    plt.yticks(horas_numericas, [h.strftime("%H:%M") for h in horas_disponibles], fontsize=6)

    plt.grid(True, zorder=1)

    # Guardar el gráfico en memoria
    img = io.BytesIO()
    plt.savefig(img, format='png', dpi=300, bbox_inches='tight')
    img.seek(0)

    return send_file(img, mimetype='image/png', as_attachment=True, download_name='grafico_despacho_diesel.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
