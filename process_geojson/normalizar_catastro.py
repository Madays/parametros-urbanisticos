import json
import os

# 📌 Diccionario de equivalencias entre los nombres originales y los códigos normalizados
map_layer = {
    "UR3-RESID-MEDIA": "R3",
    "UR4-RESID-ALTA": "R4",
    "UR5-RESID-ALTA": "R5",
    "UR2-RESID-BAJA": "R2",
    "UR1-RESID-BAJA": "R1",
    "UR1S-RESID-AGRO": "R1-S",
    "URVI-RESID-VULN-INUND": "RVI",
    "UEVS-RESID-VULN-SISMOS": "EVS",
    "UOU-OTROSUSOS": "OU",
    "UE-EDUCACION": "E",
    "US-SALUD": "S",
    "UC9-COMMETROP": "C9",
    "UCS-SECTORIAL": "CS",
    "UCE-ESPECIALIZADO": "CE",
    "UCI-COMINTENSIVO": "CI",
    "UCI2-COMINDUSTRIAL": "CI2",
    "UCV-COMVECINAL": "CV",
    "UI3-GRANINDUSTRIA": "I3",
    "UI2-INDULIVIANA": "I2",
    "UIR-INDUPRODUCTIVA": "IR",
    "UZRP-RECREAC-PUBLICA": "ZRP",
    "UZREF-ZONA-REC-FOREST": "ZREF",
    "UZRPA-RESERVA-AMBIENTAL": "ZRPA",
    "UZTEI-TRAT-ESP-I": "ZTE-I",
    "UZTEII-TRAT-ESP-II": "ZTE-II"
}

# 📌 Rutas de archivo
input_geojson = "process_geojson/CATASTRO_ICA.geojson"
output_geojson = "process_geojson/CATASTRO_ICA_normalizado.geojson"

# 📌 Debug logs
print("Current working directory:", os.getcwd())
print("Absolute path to input file:", os.path.abspath(input_geojson))
print("File exists:", os.path.exists(input_geojson))

# 📌 Cargar el archivo original
with open(input_geojson, "r", encoding="utf-8") as f:
    data = json.load(f)

# 📌 Reemplazar los nombres de layer
for feature in data["features"]:
    old_layer = feature["properties"].get("layer")
    if old_layer in map_layer:
        feature["properties"]["layer"] = map_layer[old_layer]

# 📌 Guardar el nuevo archivo
with open(output_geojson, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Archivo normalizado exportado:", output_geojson)
