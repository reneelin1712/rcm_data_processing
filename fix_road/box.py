import json

# Original coordinates
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

# Find the min and max latitudes and longitudes
min_lon = min(coord[0] for coord in coords)
max_lon = max(coord[0] for coord in coords)
min_lat = min(coord[1] for coord in coords)
max_lat = max(coord[1] for coord in coords)

# Expand the bounding box slightly (e.g., by 0.001 degrees)
expand_by = 0.001
min_lon -= expand_by
max_lon += expand_by
min_lat -= expand_by
max_lat += expand_by

# Create the expanded bounding box
expanded_coords = [
    [min_lon, min_lat], [max_lon, min_lat],
    [max_lon, max_lat], [min_lon, max_lat],
    [min_lon, min_lat]
]

# Create the GeoJSON structure
geojson = {
    "type": "FeatureCollection",
    "features": [{
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [expanded_coords]
        }
    }]
}

# Save to a GeoJSON file
with open('expanded_athens_polygon.geojson', 'w') as f:
    json.dump(geojson, f)

print(f"Expanded bounding box coordinates: {expanded_coords}")
