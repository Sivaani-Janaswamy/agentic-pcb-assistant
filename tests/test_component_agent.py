from agents.component_agent import select_components
from agents.requirement_agent import parse_requirements

test_input = "Design 5V 2A regulated power supply"
reqs = parse_requirements(test_input)
selected = select_components(reqs)

print(selected)