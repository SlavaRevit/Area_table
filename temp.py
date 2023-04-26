from Autodesk.Revit.DB import *
import clr

clr.AddReference("RevitAPI")
clr.AddReference("System")
from System.Collections.Generic import List
doc = __revit__.ActiveUIDocument.Document



floors_collector = FilteredElementCollector(doc). \
    OfCategory(BuiltInCategory.OST_Floors). \
    WhereElementIsNotElementType(). \
    ToElementIds()

levels_collector = FilteredElementCollector(doc).\
    OfCategory(BuiltInCategory.OST_Levels).\
    WhereElementIsNotElementType().\
    ToElementIds()


Elevators = {}
Regulars = {}
Stairs = {}

count = 0

for el in floors_collector:
    floor_element = doc.GetElement(el)
    floor_type = floor_element.FloorType
    floor_type_comments = floor_type.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_COMMENTS).AsString()
    floor_duplicationTypeMark = floor_type.LookupParameter("Duplication Type Mark").AsString()
    level_id = floor_element.LevelId
    level = doc.GetElement(level_id)
    level_name = level.Name
    if floor_duplicationTypeMark == "Air Stairs":
        floor_area = floor_element.LookupParameter("Area").AsDouble() * 0.092903
        Stairs[level_name] = {level_name : floor_area }
        # if floor_duplicationTypeMark == "Air Stairs":
        #
        #     floor_area = floor_element.LookupParameter("Area").AsDouble() * 0.092903
        #     Stairs[floor_duplicationTypeMark] = {"Area" : floor_area}
        # else:
        #     floor_area = floor_element.LookupParameter("Area").AsDouble() * 0.092903
        #     Stairs[floor_duplicationTypeMark] += floor_area




# for el in levels_collector:
#     print(el.Name)