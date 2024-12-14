import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree
import rasterio
from rasterio.transform import from_origin

# Load your data
data = pd.read_csv(r'/content/random_points_piezometric.csv')

# Extract x, y, z columns
x_coords = data['X'].values
y_coords = data['Y'].values
z_values = data['Z (Piezometric Level)'].values

# Define a grid for interpolation
grid_resolution = 100  # Adjust resolution
xi = np.linspace(min(x_coords), max(x_coords), grid_resolution)
yi = np.linspace(min(y_coords), max(y_coords), grid_resolution)
xi, yi = np.meshgrid(xi, yi)

# IDW interpolation function
def idw(x, y, z, xi, yi, power=2):
    dist = np.sqrt((xi - x[:, None, None])**2 + (yi - y[:, None, None])**2)
    weights = 1 / (dist**power)
    weights[dist == 0] = 1e12  # Prevent division by zero
    z_idw = np.sum(weights * z[:, None, None], axis=0) / np.sum(weights, axis=0)
    return z_idw

# Perform IDW interpolation
zi = idw(x_coords, y_coords, z_values, xi, yi)

# Plot the results
plt.contourf(xi, yi, zi, levels=100, cmap='viridis')
plt.colorbar(label='Interpolated Z values')
plt.scatter(x_coords, y_coords, c=z_values, s=10, cmap='viridis', edgecolor='black')
plt.title('IDW Interpolation of Z values')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Exporting the grid as a GeoTIFF raster
output_raster = r"/content/output_idw.tif"
transform = from_origin(min(xi.flatten()), max(yi.flatten()), (xi[1, 0] - xi[0, 0]), (yi[0, 1] - yi[0, 0]))

# Create a new raster dataset
#  with rasterio.open(
#      output_raster, 'w',
#      driver='GTiff',
 #     height=zi.shape[0],
  #    width=zi.shape[1],
   #   count=1,
    #  dtype=zi.dtype,
     # crs='EPSG:4326',  # Coordinate Reference System, modify if needed
     # transform=transform) as dst:

     # dst.write(zi, 1)

 # print(f"Raster saved as {output_raster}")
