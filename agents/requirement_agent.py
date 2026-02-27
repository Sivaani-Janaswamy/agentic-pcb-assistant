# agents/requirement_agent.py

import re
from transformers import pipeline


# Use small local model
generator = pipeline(
    "text-generation",
    model="google/flan-t5-small"
)

def parse_requirements(user_input: str):
    prompt = f"""
Extract voltage and current from:
{user_input}
"""

    result = generator(prompt, max_length=50)[0]["generated_text"]

    print("MODEL OUTPUT:", result)

    voltage_match = re.search(r'(\d+\.?\d*)\s*(V|volt|volts)', result, re.IGNORECASE)
    current_match = re.search(r'(\d+\.?\d*)\s*(A|amp|amps|ampere)', result, re.IGNORECASE)

    output_voltage = float(voltage_match.group(1)) if voltage_match else None
    output_current = float(current_match.group(1)) if current_match else None

    return {
        "output_voltage": output_voltage,
        "output_current": output_current,
        "circuit_type": user_input
    }

if __name__ == "__main__":
    print("New File LOADED")
    def test():
        from .requirement_agent import parse_requirements
        return parse_requirements("Design 5V 2A regulated power supply")
    
    print(test())