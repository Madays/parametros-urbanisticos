import json

# 📌 Diccionario con los parámetros urbanísticos (extraídos del DOC)
parametros_urbanisticos = {
    # 🔹 Zonas Residenciales
    "R5": {
        "zona": "Residencial de Alta Densidad (880 hab/ha)",
        "densidad_neta_max_hab_ha": 880,
        "area_minima_lote_m2": 72,
        "frente_minimo_ml": 6,
        "coeficiente_edificacion": 4.0,
        "area_libre_pct": 20,
        "altura_maxima_pisos": 10,
        "estacionamiento": "0.5 por vivienda"
    },
    "R4": {
        "zona": "Residencial de Alta Densidad (500 hab/ha)",
        "densidad_neta_max_hab_ha": 500,
        "area_minima_lote_m2": 72,
        "frente_minimo_ml": 6,
        "coeficiente_edificacion": 3.0,
        "area_libre_pct": 30,
        "altura_maxima_pisos": 5,
        "estacionamiento": "0.5 por vivienda"
    },
    "R3": {
        "zona": "Residencial de Media Densidad (330 hab/ha)",
        "densidad_neta_max_hab_ha": 330,
        "area_minima_lote_m2": 72,
        "frente_minimo_ml": 6,
        "coeficiente_edificacion": 1.8,
        "area_libre_pct": 30,
        "altura_maxima_pisos": 3,
        "estacionamiento": "0.5 por vivienda"
    },
    "R2": {
        "zona": "Residencial de Baja Densidad (200 hab/ha)",
        "densidad_neta_max_hab_ha": 200,
        "area_minima_lote_m2": 120,
        "frente_minimo_ml": 8,
        "coeficiente_edificacion": 1.2,
        "area_libre_pct": 40,
        "altura_maxima_pisos": 2,
        "estacionamiento": "1 por vivienda"
    },
    "R1": {
        "zona": "Residencial de Baja Densidad (110 hab/ha)",
        "densidad_neta_max_hab_ha": 110,
        "area_minima_lote_m2": 200,
        "frente_minimo_ml": 10,
        "coeficiente_edificacion": 1.0,
        "area_libre_pct": 50,
        "altura_maxima_pisos": 2,
        "estacionamiento": "1 por vivienda"
    },
    "R1-S": {
        "zona": "Residencial Agro Urbano (70 hab/ha)",
        "densidad_neta_max_hab_ha": 70,
        "area_minima_lote_m2": 1000,
        "frente_minimo_ml": 20,
        "coeficiente_edificacion": 0.3,
        "area_libre_pct": 70,
        "altura_maxima_pisos": 2,
        "estacionamiento": "1 por vivienda"
    },
    "RVI": {
        "zona": "Residencial Vulnerable por Inundación",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": None,
        "frente_minimo_ml": None,
        "coeficiente_edificacion": None,
        "area_libre_pct": None,
        "altura_maxima_pisos": None,
        "estacionamiento": "No aplica"
    },
    "EVS": {
        "zona": "Residencial Vulnerable por Sismos",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": None,
        "frente_minimo_ml": None,
        "coeficiente_edificacion": None,
        "area_libre_pct": None,
        "altura_maxima_pisos": None,
        "estacionamiento": "No aplica"
    },

    # 🔹 Zonas Comerciales
    "C9": {
        "zona": "Zona Comercial Metropolitana",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": 120,
        "frente_minimo_ml": 8,
        "coeficiente_edificacion": 2.5,
        "area_libre_pct": 20,
        "altura_maxima_pisos": 5,
        "estacionamiento": "1 por cada 100 m² de área techada"
    },
    "CS": {
        "zona": "Comercio Sectorial (Abastos)",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": 200,
        "frente_minimo_ml": 10,
        "coeficiente_edificacion": 2.0,
        "area_libre_pct": 30,
        "altura_maxima_pisos": 4,
        "estacionamiento": "1 por cada 50 m² de área techada"
    },
    "CE": {
        "zona": "Comercio Especializado",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": 200,
        "frente_minimo_ml": 10,
        "coeficiente_edificacion": 3.0,
        "area_libre_pct": 20,
        "altura_maxima_pisos": 6,
        "estacionamiento": "1 por cada 50 m² de área techada"
    },
    "CI": {
        "zona": "Comercio Intensivo (Mayorista)",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": 500,
        "frente_minimo_ml": 15,
        "coeficiente_edificacion": 2.0,
        "area_libre_pct": 30,
        "altura_maxima_pisos": 3,
        "estacionamiento": "1 por cada 100 m² de área techada"
    },
    "CI2": {
        "zona": "Comercio Industrial",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": 500,
        "frente_minimo_ml": 15,
        "coeficiente_edificacion": 1.5,
        "area_libre_pct": 40,
        "altura_maxima_pisos": 2,
        "estacionamiento": "1 por cada 100 m² de área techada"
    },
    "CV": {
        "zona": "Comercio Vecinal",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": 120,
        "frente_minimo_ml": 8,
        "coeficiente_edificacion": 1.5,
        "area_libre_pct": 30,
        "altura_maxima_pisos": 2,
        "estacionamiento": "1 por cada 50 m² de área techada"
    },

    # 🔹 Industria
    "I3": {
        "zona": "Gran Industria",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": 2000,
        "frente_minimo_ml": 30,
        "coeficiente_edificacion": 1.0,
        "area_libre_pct": 50,
        "altura_maxima_pisos": 3,
        "estacionamiento": "Según reglamento industrial"
    },
    "I2": {
        "zona": "Industria Liviana",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": 1000,
        "frente_minimo_ml": 20,
        "coeficiente_edificacion": 1.2,
        "area_libre_pct": 40,
        "altura_maxima_pisos": 3,
        "estacionamiento": "Según reglamento industrial"
    },
    "IR": {
        "zona": "Pequeña Industria (I3G, Vivienda Productiva)",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": 500,
        "frente_minimo_ml": 15,
        "coeficiente_edificacion": 1.5,
        "area_libre_pct": 30,
        "altura_maxima_pisos": 2,
        "estacionamiento": "Según reglamento industrial"
    },

    # 🔹 Equipamiento urbano
    "E": {
        "zona": "Educación (Primaria, Secundaria, Superior)",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": None,
        "frente_minimo_ml": None,
        "coeficiente_edificacion": None,
        "area_libre_pct": 30,
        "altura_maxima_pisos": 3,
        "estacionamiento": "Según reglamento específico"
    },
    "S": {
        "zona": "Salud (Hospitales y Centros de Salud)",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": None,
        "frente_minimo_ml": None,
        "coeficiente_edificacion": None,
        "area_libre_pct": 30,
        "altura_maxima_pisos": 3,
        "estacionamiento": "Según reglamento específico"
    },

    # 🔹 Recreación y protección ambiental
    "ZRP": {
        "zona": "Recreación y Parques Sectoriales",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": None,
        "frente_minimo_ml": None,
        "coeficiente_edificacion": None,
        "area_libre_pct": 60,
        "altura_maxima_pisos": 2,
        "estacionamiento": "Según reglamento específico"
    },
    "ZREF": {
        "zona": "Zonas de Recuperación Ecológica Forestal",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": None,
        "frente_minimo_ml": None,
        "coeficiente_edificacion": None,
        "area_libre_pct": 80,
        "altura_maxima_pisos": None,
        "estacionamiento": "No aplica"
    },
    "ZRPA": {
        "zona": "Zona de Reserva Paisajista y Ambiental",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": None,
        "frente_minimo_ml": None,
        "coeficiente_edificacion": None,
        "area_libre_pct": 80,
        "altura_maxima_pisos": None,
        "estacionamiento": "No aplica"
    },

    # 🔹 Tratamientos especiales
    "ZTE-I": {
        "zona": "Zona de Tratamiento Especial Tipo I",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": None,
        "frente_minimo_ml": None,
        "coeficiente_edificacion": None,
        "area_libre_pct": None,
        "altura_maxima_pisos": None,
        "estacionamiento": "Según proyecto específico"
    },
    "ZTE-II": {
        "zona": "Zona de Tratamiento Especial Tipo II",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": None,
        "frente_minimo_ml": None,
        "coeficiente_edificacion": None,
        "area_libre_pct": None,
        "altura_maxima_pisos": None,
        "estacionamiento": "Según proyecto específico"
    },

    # 🔹 Otros usos
    "OU": {
        "zona": "Otros Usos",
        "densidad_neta_max_hab_ha": None,
        "area_minima_lote_m2": None,
        "frente_minimo_ml": None,
        "coeficiente_edificacion": None,
        "area_libre_pct": None,
        "altura_maxima_pisos": None,
        "estacionamiento": "Según proyecto específico"
    }
}


# 📌 Rutas de archivo
input_geojson = "process_geojson/CATASTRO_ICA_normalizado.geojson"
output_geojson = "process_geojson/CATASTRO_ICA_enriquecido.geojson"

# 📌 Cargar el GeoJSON original
with open(input_geojson, "r", encoding="utf-8") as f:
    data = json.load(f)

# 📌 Enriquecer cada feature con sus parámetros urbanísticos
for feature in data["features"]:
    layer = feature["properties"].get("layer")
    if layer and layer in parametros_urbanisticos:
        # Añadir los parámetros al properties
        feature["properties"].update(parametros_urbanisticos[layer])

# 📌 Guardar el nuevo GeoJSON enriquecido
with open(output_geojson, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Archivo exportado:", output_geojson)
