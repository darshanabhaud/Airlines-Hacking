from collections import defaultdict
from geopy.distance import geodesic

# Load ADS-B simulated data
with open("icao_clone_data.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

aircraft_data = defaultdict(list)

# Parse the file
for line in lines:
    icao, lat, lon, speed = line.split(",")
    lat, lon = float(lat), float(lon)
    aircraft_data[icao].append((lat, lon))

print("\n=== ICAO Code Cloning Detection ===")
for icao, positions in aircraft_data.items():
    flagged = False
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            loc1 = positions[i]
            loc2 = positions[j]
            dist = geodesic(loc1, loc2).km
            if dist > 500:  # 500 km is suspicious if within same time window
                print(f"[CLONE DETECTED] ICAO {icao} appears in multiple locations:")
                print(f"  - Location 1: {loc1}")
                print(f"  - Location 2: {loc2}")
                print(f"  - Distance apart: {dist:.1f} km\n")
                flagged = True
                break
        if flagged:
            break
