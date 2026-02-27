from agents import generate_design
import json

design = generate_design("Design 5V 2A regulated power supply")
print(json.dumps(design, indent=4))