# 📊 Gráfico de Demanda Máxima con Flask

![Python](https://img.shields.io/badge/Lenguaje-Python-blue?style=flat&logo=python)
![HTML](https://img.shields.io/badge/Frontend-HTML5-orange?style=flat&logo=html5)
![Flask](https://img.shields.io/badge/Framework-Flask-black?style=flat&logo=flask)
![Gráfico](https://img.shields.io/badge/Visualización-Matplotlib-lightblue?style=flat&logo=plotly)
![Formato](https://img.shields.io/badge/Formato-Excel(.xlsx)-green?style=flat&logo=microsoft-excel)
![Deploy](https://img.shields.io/badge/Despliegue-Render-purple?style=flat)
![Licencia](https://img.shields.io/badge/Licencia-Personal-red)

---

## 📌 Descripción

Esta aplicación web permite cargar un archivo Excel con datos energéticos, seleccionar un rango de fechas y generar un **gráfico de distribución de despacho Diésel** en las horas de **máxima demanda**. Fue desarrollada con **Flask**, usando `pandas` para el procesamiento y `matplotlib` para la visualización.

🔗 **Prueba la app aquí:**  
👉 [https://grafico-de-demanda-maxima.onrender.com](https://grafico-de-demanda-maxima.onrender.com)

---

## 🎯 Objetivos

- Leer archivos Excel con datos energéticos.
- Filtrar por rango de fechas personalizado.
- Identificar el tipo de combustible (Diésel o Residual).
- Graficar las horas de máxima demanda diaria con diferenciación visual.
- Permitir descarga directa del gráfico generado.

---

## 💻 Requisitos

- Python 3.9+
- Navegador web moderno

### 📦 Librerías usadas

- `Flask`
- `pandas`
- `matplotlib`
- `openpyxl`
- `gunicorn` *(para despliegue en Render)*

---

## 🧠 Características

### Interfaz Web
- Carga de archivos Excel `.xlsx`
- Selección de fecha de inicio y fin
- Descarga automática del gráfico generado

### Procesamiento de Datos
- Conversión de fechas y horas
- Filtrado por rango
- Clasificación de tipo de combustible
- Agrupación por día con máxima demanda

### Visualización
- Gráfico de dispersión con codificación por color
- Sombreado por horas laborales
- Líneas guías de referencia horaria y mensual

---

## ▶️ Instrucciones de Uso

### Localmente

1. Clona el repositorio:
```bash
git clone https://github.com/Joanna20Carrion/Grafico-de-Demanda-Maxima.git
cd Grafico-de-Demanda-Maxima
```

2. Instala las dependencias:
```bash
git clone https://github.com/Joanna20Carrion/Grafico-de-Demanda-Maxima.git
cd Grafico-de-Demanda-Maxima
```

3. Ejecuta la app:
```bash
python app.py
```

4. Abre tu navegador en: http://localhost:5000

