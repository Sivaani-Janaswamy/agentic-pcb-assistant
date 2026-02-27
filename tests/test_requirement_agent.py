from agents.requirement_agent import parse_requirements

test_input = "Design 5V 2A regulated power supply"
result = parse_requirements(test_input)

print(result)