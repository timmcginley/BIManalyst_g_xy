from dataclasses import dataclass

import ifcopenshell
import ifcopenshell.util.selector

@dataclass
class DoorCountOverview:
    count_external: int # Number of external doors
    count_internal: int # Number of internal doors
    count_external_unknown: int  # Number of doors with unknown external/internal status


def count_doors(model: ifcopenshell.file) -> DoorCountOverview:
    doors = model.by_type('IfcDoor')

    count_external = 0  # Counter for external doors
    count_internal = 0  # Counter for internal doors

    external_doors = ifcopenshell.util.selector.filter_elements(model, "IfcDoor, Pset_DoorCommon.IsExternal=TRUE")
    internal_doors = ifcopenshell.util.selector.filter_elements(model, "IfcDoor, Pset_DoorCommon.IsExternal=FALSE")
    unknown_doors = set(doors) - set(external_doors) - set(internal_doors)

    count_external = len(external_doors)
    count_internal = len(internal_doors)
    count_external_unknown = len(unknown_doors)

    return DoorCountOverview(
        count_external=count_external,
        count_internal=count_internal,
        count_external_unknown=count_external_unknown
    )

def createDoorReport(door_overview: DoorCountOverview) -> str:
    """Generates a markdown report summarizing the door counts."""
    report_md = (
        f"# Door Count Overview:\n"
        f"- External Doors: {door_overview.count_external}\n"
        f"- Internal Doors: {door_overview.count_internal}\n"
        f"- Doors with Unknown External/Internal Status: {door_overview.count_external_unknown}\n"
    )
    return report_md
