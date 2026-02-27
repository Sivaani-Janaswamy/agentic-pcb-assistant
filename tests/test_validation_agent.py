from agents.requirement_agent import parse_requirements
from agents.component_agent import select_components
from agents.validation_agent import validate_components

test_input = "Design 5V 2A regulated power supply"
reqs = parse_requirements(test_input)
components = select_components(reqs)
validation = validate_components(reqs, components)

print(validation)