import os
import json
from pathlib import Path
from datetime import datetime

RAW_PATH = Path("data/raw/industrial_incidents.json")
PROCESSED_DIR = Path("data/processed")
PROCESSED_FILE = PROCESSED_DIR / "incidents_for_ingestion.json"

os.makedirs(PROCESSED_DIR, exist_ok=True)

# -----------------------------
# Helper function to convert incident to text
# -----------------------------
def incident_to_text(inc):
    return f"""
Incident ID: {inc['incident_id']}
Timestamp: {inc['timestamp']}
Equipment: {inc['equipment']} ({inc['equipment_type']})
Location: {inc['location']}
Severity: {inc['severity']}
Error Type: {inc['error_type']}
Root Cause: {inc['root_cause']}
Resolution: {inc['resolution']}
Downtime: {inc['downtime_minutes']} minutes
"""

# -----------------------------
# Additional fields for processed data
# -----------------------------
def compute_additional_fields(inc):
    # Example: severity score (Low=1, Medium=2, High=3)
    severity_map = {"Low": 1, "Medium": 2, "High": 3}
    severity_score = severity_map.get(inc["severity"], 0)

    # Example: detect sensor anomalies
    sensor_data = inc.get("sensor_data", {})
    temp_anomaly = any(t > 100 for t in sensor_data.get("temperature", []))
    pressure_anomaly = any(p > 50 for p in sensor_data.get("pressure", []))
    vibration_anomaly = any(v > 2 for v in sensor_data.get("vibration", []))

    # Example: parse timestamp to datetime object
    timestamp_dt = datetime.fromisoformat(inc["timestamp"])

    return {
        "severity_score": severity_score,
        "temp_anomaly": temp_anomaly,
        "pressure_anomaly": pressure_anomaly,
        "vibration_anomaly": vibration_anomaly,
        "timestamp_dt": timestamp_dt.isoformat()
    }

# -----------------------------
# Load raw incidents
# -----------------------------
with open(RAW_PATH) as f:
    raw_incidents = json.load(f)

# -----------------------------
# Process incidents
# -----------------------------
processed_incidents = []
for inc in raw_incidents:
    processed = {
        "incident_id": inc["incident_id"],
        "text": incident_to_text(inc),
        "error_type": inc["error_type"],
        "equipment": inc["equipment"],
        **compute_additional_fields(inc)  # add computed fields
    }
    processed_incidents.append(processed)

# -----------------------------
# Save processed dataset
# -----------------------------
with open(PROCESSED_FILE, "w") as f:
    json.dump(processed_incidents, f, indent=2)

print(f"✅ Processed {len(processed_incidents)} incidents to {PROCESSED_FILE}")