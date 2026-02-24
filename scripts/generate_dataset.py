import os
import random
import json
from datetime import datetime, timedelta

NUM_INCIDENTS = 100000
BATCH_SIZE = 50

OUTPUT_DIR = os.path.join("data", "raw")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "industrial_incidents.json")

EQUIPMENT_TYPES = {
    "Turbine": ["Temperature Spike", "Over Vibration"],
    "Pump": ["Pressure Drop", "Flow Blockage"],
    "Compressor": ["Overheating", "Pressure Spike"],
    "Boiler": ["Steam Leak", "Temperature Drift"],
    "Generator": ["Power Fluctuation", "Voltage Instability"]
}

SEVERITY = ["Low", "Medium", "High"]

ROOT_CAUSES = {
    "Temperature Spike": "Cooling system obstruction",
    "Over Vibration": "Bearing wear",
    "Pressure Drop": "Valve leakage",
    "Flow Blockage": "Pipe obstruction",
    "Overheating": "Lubrication failure",
    "Pressure Spike": "Control system malfunction",
    "Steam Leak": "Seal degradation",
    "Temperature Drift": "Sensor calibration drift",
    "Power Fluctuation": "Electrical instability",
    "Voltage Instability": "Generator regulator fault"
}

RESOLUTIONS = {
    "Temperature Spike": "Cooling system cleaned and recalibrated",
    "Over Vibration": "Bearings replaced",
    "Pressure Drop": "Valve replaced",
    "Flow Blockage": "Pipe cleared",
    "Overheating": "Lubrication system repaired",
    "Pressure Spike": "Control software updated",
    "Steam Leak": "Seal replaced",
    "Temperature Drift": "Sensor recalibrated",
    "Power Fluctuation": "Electrical system stabilized",
    "Voltage Instability": "Regulator replaced"
}

def generate_sensor_series(base_value: float, anomaly: bool = False):
    values = [round(base_value + random.uniform(-2, 2), 2) for _ in range(15)]
    if anomaly:
        values[-3:] = [round(base_value * random.uniform(1.5, 2.0), 2) for _ in range(3)]
    return values

def generate_incident(i: int):
    equipment_type = random.choice(list(EQUIPMENT_TYPES.keys()))
    error_type = random.choice(EQUIPMENT_TYPES[equipment_type])
    return {
        "incident_id": f"INC_{i:06}",
        "timestamp": (datetime.utcnow() - timedelta(days=random.randint(0, 365))).isoformat(),
        "equipment": f"{equipment_type}_{random.randint(1,5)}",
        "equipment_type": equipment_type,
        "severity": random.choice(SEVERITY),
        "location": f"Plant_{random.choice(['A','B','C'])}",
        "error_type": error_type,
        "sensor_data": {
            "temperature": generate_sensor_series(70, anomaly=True),
            "pressure": generate_sensor_series(30, anomaly=True),
            "vibration": generate_sensor_series(0.5, anomaly=True)
        },
        "root_cause": ROOT_CAUSES[error_type],
        "resolution": RESOLUTIONS[error_type],
        "downtime_minutes": random.randint(10, 180)
    }

def main():
    print("Generating synthetic industrial incidents dataset...")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(OUTPUT_FILE, "w") as f:
        f.write("[\n")
        for i in range(1, NUM_INCIDENTS + 1):
            incident = generate_incident(i)
            f.write(json.dumps(incident))
            if i != NUM_INCIDENTS:
                f.write(",\n")
            if i % BATCH_SIZE == 0:
                print(f"{i} incidents generated...")
        f.write("\n]")

    print(f"Dataset successfully generated at: {OUTPUT_FILE}")
    print(f"Total incidents: {NUM_INCIDENTS}")

if __name__ == "__main__":
    main()