import ezdxf
import geojson
from shapely.geometry import Polygon, LineString, Point, mapping
from pyproj import Transformer

# Transformer: UTM zone 18S -> WGS84
transformer = Transformer.from_crs("EPSG:32718", "EPSG:4326", always_xy=True)

doc = ezdxf.readfile("catastro-basico.dxf")
msp = doc.modelspace()

features = []

# 🔹 Closed polylines -> Polygon
for e in msp.query("LWPOLYLINE"):
    coords = [transformer.transform(p[0], p[1]) for p in e]
    if e.closed:
        poly = Polygon(coords)
        features.append(geojson.Feature(geometry=mapping(poly), properties={"layer": e.dxf.layer}))
    else:
        line = LineString(coords)
        features.append(geojson.Feature(geometry=mapping(line), properties={"layer": e.dxf.layer}))

# 🔹 Lines -> LineString
# for e in msp.query("LINE"):
#     start = transformer.transform(e.dxf.start[0], e.dxf.start[1])
#     end = transformer.transform(e.dxf.end[0], e.dxf.end[1])
#     line = LineString([start, end])
#     features.append(geojson.Feature(geometry=mapping(line), properties={"layer": e.dxf.layer}))

# 🔹 Circles -> Polygon (approximate)
# for e in msp.query("CIRCLE"):
#     center = transformer.transform(e.dxf.center[0], e.dxf.center[1])
#     circle = Point(center).buffer(e.dxf.radius, resolution=32)  # buffer = approximate circle
#     features.append(geojson.Feature(geometry=mapping(circle), properties={"layer": e.dxf.layer}))

# 🔹 Text -> Point with label
# for e in msp.query("TEXT"):
#     pos = transformer.transform(e.dxf.insert[0], e.dxf.insert[1])
#     features.append(geojson.Feature(
#         geometry=mapping(Point(pos)),
#         properties={"layer": e.dxf.layer, "text": e.dxf.text}
#     ))

# 🔹 MText (multi-line text)
# for e in msp.query("MTEXT"):
#     pos = transformer.transform(e.dxf.insert[0], e.dxf.insert[1])
#     features.append(geojson.Feature(
#         geometry=mapping(Point(pos)),
#         properties={"layer": e.dxf.layer, "text": e.text}
#     ))

# Save to GeoJSON
fc = geojson.FeatureCollection(features)

with open("CATASTRO_ICA.geojson", "w") as f:
    geojson.dump(fc, f, ensure_ascii=False, indent=2)
