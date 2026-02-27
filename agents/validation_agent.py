def validate_components(requirements: dict, components: dict):
    issues = []

    voltage_req = requirements["output_voltage"]
    current_req = requirements["output_current"]

    regulator = components["regulator"]

    # Check if regulator exists
    if not regulator:
        issues.append("No suitable regulator found.")
    else:
        # Check voltage
        if regulator["output_voltage"] != voltage_req:
            issues.append(f"Regulator voltage mismatch: required {voltage_req}V, found {regulator['output_voltage']}V")
        # Check current
        if regulator["max_current"] < current_req:
            issues.append(f"Regulator current too low: required {current_req}A, max {regulator['max_current']}A")

    # Add more checks if needed (thermal, diode, etc.)
    # For now simple pass/fail
    status = "PASS" if not issues else "WARNING"

    return {
        "status": status,
        "issues": issues
    }