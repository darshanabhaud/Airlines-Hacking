# airlines_hacking_simulator.py
# Author: [Your Name]
# Digisuraksha Internship 2025

import csv
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Simulated ADS-B Data Generator
def generate_adsb_data():
    icao_list = ['A1B2C3', 'D4E5F6', 'G7H8I9']
    for _ in range(100):
        icao = random.choice(icao_list)
        lat = round(random.uniform(10.0, 50.0), 4)
        lon = round(random.uniform(-120.0, -70.0), 4)
        speed = round(random.uniform(200, 1100), 1)
        yield {'icao': icao, 'lat': lat, 'lon': lon, 'speed': speed}

colors = {'A1B2C3': 'blue', 'D4E5F6': 'green', 'G7H8I9': 'red'}
positions = {k: [] for k in colors}
fig, ax = plt.subplots()
scatters = {icao: ax.plot([], [], color=clr, label=icao)[0] for icao, clr in colors.items()}

# 2. Suspicious Activity Detection
def is_suspicious(data):
    if data['speed'] > 1000:
        return 'High Speed'
    if len(positions[data['icao']]) >= 2 and positions[data['icao']][-1] == positions[data['icao']][-2]:
        return 'Repeated Coordinates'
    return None

# 3. CSV Logging
log_file = open('flight_log.csv', mode='w', newline='')
csv_writer = csv.writer(log_file)
csv_writer.writerow(['ICAO', 'Latitude', 'Longitude', 'Speed', 'Suspicious'])

data_gen = generate_adsb_data()

def update(frame):
    try:
        data = next(data_gen)
    except StopIteration:
        return
    icao = data['icao']
    lat, lon, speed = data['lat'], data['lon'], data['speed']
    positions[icao].append((lon, lat))
    xs, ys = zip(*positions[icao])
    scatters[icao].set_data(xs, ys)
    reason = is_suspicious(data)
    csv_writer.writerow([icao, lat, lon, speed, reason if reason else ''])
    ax.set_xlim(-130, -60)
    ax.set_ylim(0, 60)
    ax.set_title("Flight Path Visualization")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.legend()

ani = FuncAnimation(fig, update, interval=500, cache_frame_data=False)

plt.show()
log_file.close()