# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# data_table_catcon.py
# Created on: 2018-12-05
#   Parts of code were generated via tool help in ArcGIS for Destop
# Usage: data_table_catcon <Input_Excel_File> <Field_Name> <Expression> <Field_Name__2_> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
v2018_AlaPine_TM_test_shp = "C:\\Projects\\Python\\fwarcmap\\2018AlaPine\\Test\\2018_AlaPine_TM_test.shp"
v2018_AlaPine_TM_test_shp__3_ = v2018_AlaPine_TM_test_shp
v2018_AlaPine_TM_test_shp__2_ = v2018_AlaPine_TM_test_shp__3_
v2018_AlaPine_TM_test_shp__4_ = v2018_AlaPine_TM_test_shp__2_
v2018_Timber_Marking_xlsx = "C:\\Projects\\Python\\fwarcmap\\Export\\2018_Timber_Marking.xlsx"
Timber_Marking_2018_dbf = "C:\\Projects\\Python\\fwarcmap\\Export\\Timber_Marking_2018.dbf"
Timber_Marking_2018_dbf__5_ = Timber_Marking_2018_dbf
Timber_Marking_2018_dbf__6_ = Timber_Marking_2018_dbf__5_
Timber_Marking_2018_dbf__2_ = Timber_Marking_2018_dbf__6_
Timber_Marking_2018_dbf__7_ = Timber_Marking_2018_dbf__2_
Timber_Marking_2018_dbf__4_ = Timber_Marking_2018_dbf__7_
Timber_Marking_2018_dbf__8_ = Timber_Marking_2018_dbf__4_
Timber_Marking_2018_dbf__9_ = Timber_Marking_2018_dbf__8_
Timber_Marking_2018_dbf__10_ = Timber_Marking_2018_dbf__9_
v2018_AlaPine_TM_shp__5_ = v2018_AlaPine_TM_test_shp__4_
v2018_AlaPine_TM_shp__6_ = v2018_AlaPine_TM_test_shp__4_
v2018_AlaPine_TM_shp__7_ = v2018_AlaPine_TM_test_shp__4_
v2018_AlaPine_TM_shp__8_ = v2018_AlaPine_TM_test_shp__4_
v2018_AlaPine_TM_shp__9_ = v2018_AlaPine_TM_test_shp__4_
v2018_AlaPine_TM_test_shp__5_ = v2018_AlaPine_TM_shp__9_

# Process: Add Field (2)
arcpy.AddField_management(v2018_AlaPine_TM_test_shp, "lacost", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (2)
arcpy.CalculateField_management(v2018_AlaPine_TM_test_shp__3_, "lacost", "[Landowner] + [Comp] + [Stand]", "VB", "")

# Process: Excel To Table
arcpy.ExcelToTable_conversion(v2018_Timber_Marking_xlsx, Timber_Marking_2018_dbf, "Sheet1")

# Process: Add Field (3)
arcpy.AddField_management(Timber_Marking_2018_dbf, "la", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (3)
arcpy.CalculateField_management(Timber_Marking_2018_dbf__5_, "la", "[Landowner]", "VB", "")

# Process: Add Field (4)
arcpy.AddField_management(Timber_Marking_2018_dbf__6_, "co", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (4)
arcpy.CalculateField_management(Timber_Marking_2018_dbf__2_, "co", "[Comp]", "VB", "")

# Process: Add Field (5)
arcpy.AddField_management(Timber_Marking_2018_dbf__7_, "st", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (5)
arcpy.CalculateField_management(Timber_Marking_2018_dbf__4_, "st", "[Column2]", "VB", "")

# Process: Add Field
arcpy.AddField_management(Timber_Marking_2018_dbf__8_, "lacost", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(Timber_Marking_2018_dbf__9_, "lacost", "[la]+ [co]+ [st]", "VB", "")

# Process: Join Field
arcpy.JoinField_management(v2018_AlaPine_TM_test_shp__2_, "lacost", Timber_Marking_2018_dbf__10_, "lacost", "Family;LO_Name;Stand_Acre;Crew;Thin")

# Process: Calculate Field Acres
arcpy.CalculateField_management(v2018_AlaPine_TM_test_shp__4_, "Acres", "[Stand_Acre]", "VB", "")

# Process: Calculate Field Crew
arcpy.CalculateField_management(v2018_AlaPine_TM_test_shp__4_, "Crew", "[Crew_1]", "VB", "")

# Process: Calculate Field Family
arcpy.CalculateField_management(v2018_AlaPine_TM_test_shp__4_, "Family", "[Family_1]", "VB", "")

# Process: Calculate Field Thin
arcpy.CalculateField_management(v2018_AlaPine_TM_test_shp__4_, "TYPE_CUT", "[Thin]", "VB", "")

# Process: Calculate Field LO Name
arcpy.CalculateField_management(v2018_AlaPine_TM_test_shp__4_, "CommentsFo", "[LO_Name]", "VB", "")

# Process: Delete Field
arcpy.DeleteField_management(v2018_AlaPine_TM_shp__9_, "Family_1;LO_Name;Crew_1;Thin;Family_12;LO_Name_1;Stand_Acre;Crew_12;Thin_1")


