import rasterio
from rasterio.features import shapes
import json

# Open the GeoTIFF file
with rasterio.open('create_JSON/file.tif') as src:
    # Read the raster data
    image = src.read(1)  # You may need to adjust the band index (e.g., read(1), read(2), etc.)

    # Get the transform
    transform = src.transform

    # Convert raster data to GeoJSON-like features
    geoms = list(shapes(image, transform=transform))

# Create a GeoJSON-like dictionary
geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": geom[0]['type'],
                "coordinates": geom[0]['coordinates']
            },
            "properties": {}
        }
        for geom in geoms
    ]
}

# Write the GeoJSON to a file
with open('output.geojson', 'w') as output_file:
    json.dump(geojson, output_file)
