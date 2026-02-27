# agents/__init__.py
from agents.requirement_agent import parse_requirements
from agents.component_agent import select_components
from agents.validation_agent import validate_components

def generate_design(user_input: str):
    # 1️⃣ Parse requirements
    requirements = parse_requirements(user_input)

    # 2️⃣ Select components
    selected_components = select_components(requirements)

    # 3️⃣ Validate components
    validation = validate_components(requirements, selected_components)

    # 4️⃣ Layout recommendations (hackathon: simple placeholders)
    layout_recommendations = [
        "Place regulator near input capacitor",
        "Keep output capacitor close to load",
        "Diode before input"
    ]

    # 5️⃣ Generate BOM
    bom = []
    reg = selected_components.get("regulator")
    if reg:
        bom.append({
            "component_name": reg["name"],
            "specification": f"{reg['output_voltage']}V {reg['max_current']}A {reg['type']}",
            "quantity": 1
        })
    for cap in selected_components.get("capacitors", []):
        bom.append({
            "component_name": cap["name"],
            "specification": f"{cap['value']} {cap['voltage_rating']}V {cap['type']}",
            "quantity": 1
        })
    diode = selected_components.get("diode")
    if diode:
        bom.append({
            "component_name": diode["name"],
            "specification": f"{diode['type']} {diode['max_current']}A {diode['max_voltage']}V",
            "quantity": 1
        })

    # 6️⃣ Return full structure
    return {
        "requirements": requirements,
        "selected_components": selected_components,
        "validation": validation,
        "layout_recommendations": layout_recommendations,
        "bom": bom
    }