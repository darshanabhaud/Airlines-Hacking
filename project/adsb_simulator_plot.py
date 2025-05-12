import matplotlib.pyplot as plt
from collections import defaultdict

# Load simulated ADS-B data with format: ICAO,LAT,LON,SPEED
with open("simulated_adsb_data.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

# Data structure to store aircraft paths
aircraft_paths = defaultdict(list)

# Parse the lines and store positions
for line in lines:
    try:
        icao, lat, lon, speed = line.split(",")
        lat = float(lat)
        lon = float(lon)
        speed = int(speed)
        aircraft_paths[icao].append((lat, lon, speed))
        print(f"[+] {icao} - Lat: {lat}, Lon: {lon}, Speed: {speed} kt")
    except ValueError as e:
        print(f"[!] Skipping line due to error: {e}")

# Plotting
plt.figure(figsize=(10, 6))
for icao, positions in aircraft_paths.items():
    lats = [pos[0] for pos in positions]
    lons = [pos[1] for pos in positions]
    plt.plot(lons, lats, marker='o', label=f"ICAO: {icao}")

plt.title("Simulated Aircraft Flight Paths")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.grid(True)
plt.show()
