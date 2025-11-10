import ifcopenshell

from rules import windowRule
from rules import doorRule

model = ifcopenshell.open("path/to/ifcfile.ifc")

windowResult = windowRule.checkRule(model)

door_overview = doorRule.count_doors(model)
door_report = doorRule.createDoorReport(door_overview)

print("Window result:", windowResult)

# Optionally write markdown to a file
print("Markdown report:\n", door_report)
