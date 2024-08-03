import json
from shapely.geometry import Polygon

coords = [
    [23.724023443717012, 37.989214749626427], [23.727989595441151, 37.988666794454019],
    [23.728250526475634, 37.989945356522981], [23.728981133372187, 37.993024342729882],
    [23.736887343717015, 37.992345922040222], [23.736078457510118, 37.989032097902289],
    [23.732112305785982, 37.989658332385048], [23.731355605785982, 37.98694464962643],
    [23.732294957510117, 37.985483435833324], [23.733547426475635, 37.986083577212639],
    [23.74001851613081, 37.977629411695396], [23.736522040268738, 37.97507228755746],
    [23.734408498889429, 37.975046194454016], [23.728120060958393, 37.9828741254885],
    [23.727258988544602, 37.982665380660912], [23.725797774751495, 37.982482728936773],
    [23.722797067854945, 37.986683718591948], [23.724023443717012, 37.989214749626427]
]

poly = Polygon(coords)

geojson = {
    "type": "FeatureCollection",
    "features": [{
        "type": "Feature",
        "properties": {},
        "geometry": json.loads(json.dumps(poly.__geo_interface__))
    }]
}

with open('athens_polygon.geojson', 'w') as f:
    json.dump(geojson, f)


# osmium extract -p athens_polygon.geojson europe-latest.osm.pbf -o athens_extract.osm.pbf