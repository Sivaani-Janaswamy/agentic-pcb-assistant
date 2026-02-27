import json

def load_db():
    with open("./data/component_db.json", "r") as f:
        db = json.load(f)
    return db
def find_regulator(voltage, current):
    db = load_db()
    for reg in db["regulators"]:
        if reg["output_voltage"] == voltage and reg["max_current"] >= current:
            return reg
    return None

db = load_db()

print("Loaded successfully!")
print("Regulators:", len(db["regulators"]))
print("Capacitors:", len(db["capacitors"]))
print("Diodes:", len(db["diodes"]))

test_cases = [
    (5, 1),
    (5, 2),
    (5, 3)
]

for voltage, current in test_cases:
    result = find_regulator(voltage, current)
    if result:
        print(f"Found regulator for {voltage}V {current}A → {result['name']}")
    else:
        print(f"No regulator found for {voltage}V {current}A")