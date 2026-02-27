def generate_design(user_input):
    return {
        "requirements": {
            "output_voltage": 5,
            "output_current": 2,
            "circuit_type": "Linear Regulator"
        },
        "selected_components": {
            "regulator": {
                "name": "LM7805",
                "type": "Linear",
                "output_voltage": 5,
                "max_current": 1,
                "input_voltage_min": 7,
                "input_voltage_max": 25,
                "package": "TO-220"
            },
            "capacitors": [],
            "diode": None
        },
        "validation": {
            "status": "WARNING",
            "issues": ["Current close to regulator limit"]
        },
        "layout_recommendations": ["Place regulator centrally"],
        "bom": []
    }