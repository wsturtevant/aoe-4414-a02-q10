# llh_to_ececf.py
#
# Usage: py llh_to_ecef.py lat_deg lon_deg hae_km
#  Converts latitute, geight above ellipsoid to radisu and z-height
#
# Parameters:
#  lat_deg: latitude in degrees
#  lon_deg: longitude in degrees
#  hae_km: height above the ellipse in km
# Output:
#  Print the radius in km for the x, y, and z directions
#
# Written by Wheat Sturtevant
#

# import Python modules
# e.g., import math # math module
import sys # argv
import math #argv

# "constants"
R_E_KM = 6378.137
E_E = 0.081819221456

# helper functions

## calc denom
def calc_denom(ecc, lat_rad):
   return math.sqrt(1.0-ecc**2.0 * math.sin(lat_rad)**2.0)

# initialize script arguments
lat_deg = float('nan') # llh latitude in deg
lon_deg = float('nan') # llh longitude in deg
hae_km = float('nan') # height above the ellipse in km

# parse script arguments
if len(sys.argv)==4:
    lat_deg = float(sys.argv[1])
    lon_deg = float(sys.argv[2])
    hae_km = float(sys.argv[3])
else:
    print(\
        'Usage: '\
        'python3 llh_to_ecef.py lat_deg lon_deg hae_km'\
    )
    exit()

# write script below this line

# initialize lat_rad, lon_rad 
lat_rad = lat_deg*(math.pi/180)
lon_rad = lon_deg*(math.pi/180)

# foumulas from Slides
denom = calc_denom(E_E, lat_rad)
c_e = R_E_KM/denom
s_e = (R_E_KM)*(1-E_E**2)/denom

# calculate r_x_km r_y_km r_z_km
r_x_km = (c_e+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km = (c_e+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km = (s_e+hae_km)*math.sin(lat_rad)

# print outputs
print('r_x_km: '+str(r_x_km))
print('r_y_km: '+str(r_y_km))
print('r_z_km: '+str(r_z_km))

# Test Usage: 
# py llh_to_ecef.py 37.228863 -76.386573 0.63