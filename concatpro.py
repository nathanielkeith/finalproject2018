# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# data_table_catcon.py
# Created on: 2018-12-05 18:30:30.00000
#   Parts of code were generated via tool help in ArcGIS for Destop
# Usage: data_table_catcon <Input_Excel_File> <Field_Name> <Expression> <Field_Name__2_> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Input_Excel_File = arcpy.GetParameterAsText(0)

Field_Name = arcpy.GetParameterAsText(1)

Expression = arcpy.GetParameterAsText(2)

Field_Name__2_ = arcpy.GetParameterAsText(3)

# Local variables:
Output_Table = ""
Output_Feature_Class = Output_Table
Output_Feature_Class__2_ = Output_Feature_Class

# Process: Excel To Table
arcpy.ExcelToTable_conversion(Input_Excel_File, Output_Table, "")

# Process: Add Field
arcpy.AddField_management(Output_Table, Field_Name, "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(Output_Feature_Class, Field_Name__2_, Expression, "VB", "")

