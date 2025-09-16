from pyproj import Transformer

# Definir el sistema de coordenadas de origen (UTM zona 18 Sur, ajusta si es necesario)
transformer = Transformer.from_crs("EPSG:32718", "EPSG:4326", always_xy=True)

# Coordenadas UTM en metros
x, y = 422597.9314, 8445400.7212

# Convertir a lat/lon
lon, lat = transformer.transform(x, y)

print(f"Latitud: {lat}, Longitud: {lon}")
