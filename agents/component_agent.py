import json

def load_components():
    with open("data/component_db.json") as f:
        return json.load(f)

def select_components(requirements: dict):
    db = load_components()
    voltage = requirements["output_voltage"]
    current = requirements["output_current"]

    # Select regulator
    regulator = None
    for reg in db["regulators"]:
        if reg["output_voltage"] == voltage and reg["max_current"] >= current:
            regulator = reg
            break

    # Pick all capacitors
    capacitors = db["capacitors"]

    # Pick first diode
    diode = db["diodes"][0] if db["diodes"] else None

    return {
        "regulator": regulator,
        "capacitors": capacitors,
        "diode": diode
    }