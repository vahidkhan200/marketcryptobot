import json
from datetime import datetime

def save_signal(signal):
    try:
        with open("signals.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    signal['timestamp'] = datetime.utcnow().isoformat()
    data.insert(0, signal)

    with open("signals.json", "w") as f:
        json.dump(data[:100], f, indent=2)
