
## This file is part of the mfgtextadder project.
## It is used to add manufacturing information to KiCad PCB files.

####wxframework imports####
import os
import wx
import time
from copy import deepcopy
from typing import Set
import re

from mfgtextadderbase import mfgtextadder

###kipy imports####
from kipy import KiCad
from kipy.board_types import (
    BoardLayer,
    Zone,
    BoardText
)
from kipy.board import BoardStackup
from kipy.geometry import Vector2
from kipy.util import (from_mm, board_layer)
from kipy.common_types import TextAttributes

class MfgInfoAction(mfgtextadder):
    """
    Action to add manufacturing information to a KiCad PCB file.
    This class extends the mfgtextadder base class and implements the action logic.
    """
    
    
    def __init__(self):
        super(MfgInfoAction, self).__init__(None)
        self.kicad=KiCad()
        self.board = self.kicad.get_board()
        #self.silkscreen_color.Bind(wx.EVT_CHECKBOX, self.on_silkscreen_checkbox)
        self.Run.Bind(wx.EVT_BUTTON, self.run)
        
#######default functions########

    def number_copperlayers(self):
        stackup = self.board.get_stackup()
        coppercounter = 0
        for layer in stackup.layers:
            if layer.material_name == "copper":
                coppercounter += 1
                #print(f"copper layers {coppercounter}")
        #return coppercounter
        body = BoardText()
        body.value = " Number of Copper Layers: " + str(coppercounter)
        body.position = Vector2.from_xy_mm(232.294992, self.spacing)
        self.spacing += 4
        txtatt = TextAttributes()
        txtatt.size = Vector2.from_xy_mm(1, 1)
        txtatt.stroke_width = 150000  # nanometers
        body.attributes = txtatt
        body.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        
        self.board.create_items(body)
    
    def add_heading_text(self):
        # Create and add heading text
        heading = BoardText()
        heading.value = "FABRICATION NOTES"
        heading.position = Vector2.from_xy_mm(233.310997, self.spacing)
        self.spacing += 6
        txtatt = TextAttributes()
        txtatt.size = Vector2.from_xy_mm(3, 3)
        txtatt.stroke_width = 150000  # nanometers (7 mm thickness equivalent)
        heading.attributes = txtatt
        heading.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        
        self.board.create_items(heading)

    def run(self, event):
        
        self.spacing = 19.946399
        self.add_heading_text()

        for i in self.getremovebuttons():
            button = i.replace("self.", "")
            self.removebuttonheyo = getattr(self, button, None)
            print("removebutton", self.removebuttonheyo)
            if self.removebuttonheyo.GetValue() is True:
                self.buttontoremove = i
                print(f"Going to remove plugin: {button}")
                self.removeplugin()

        # default text additions
        if self.copper_count.IsChecked():
            self.number_copperlayers()

        if self.drill_plot_show.IsChecked():
            print("Drill Plot checkbox checked.")
            self.add_drillplot()

        # Add text based on checkbox selections
        if self.silkscreen_color.IsChecked():
            print("Silkscreen checkbox checked.")
            self.add_silkscreen()

        if self.front_copperweight.IsChecked():
            print("Front Copper checkbox checked.")
            self.add_frontcopper()

        if self.back_copperweight.IsChecked():
            print("Back Copper checkbox checked.")
            self.add_backcopper()

        if self.mask_color.IsChecked():
            print("Soldermask checkbox checked.")
            self.add_soldercolor()

        if self.board_thickness.IsChecked():
            print("Board Thickness checkbox checked.")
            self.add_boardthickness()

        if self.copper_srf_overall.IsChecked():
            print("Copper Surface Finish checkbox checked.")
            self.add_copper_surface()
        
        if self.trackwidth_spacing.IsChecked():
            print("Track Width and Spacing checkbox checked.")
            self.add_trackwidth_spacing()
        
        if self.min_hole_diameter.IsChecked():
            print("Minimum Hole Diameter checkbox checked.")
            self.add_holediameter()

        if self.imped_ctrl.IsChecked():
            print("Impedance Control checkbox checked.")
            self.add_impedctrl()

        if self.dimensions.IsChecked():
            print("Dimensions checkbox checked.")
            self.add_dimensions()

        if self.applyonce.GetValue():
            self.add_textonce()

        if self.addtoplugin.GetValue():
            # create function
            self.addtopluginfn()

        for i in self.
        

  ###########add text functions############
    def add_drillplot(self):
        # Create and add body text
        body = BoardText()
        body.value = " Drill Plot Shows Finished Hole Sizes"
        body.position = Vector2.from_xy_mm(232.294992, self.spacing)
        self.spacing += 4
        txtatt = TextAttributes()
        txtatt.size = Vector2.from_xy_mm(1, 1)
        txtatt.stroke_width = 150000  # nanometers
        body.attributes = txtatt
        body.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        self.board.create_items(body)

    def add_silkscreen(self):
        # Create and add body text
        body = BoardText()
        if self.silkscreen_value.GetStringSelection() == "White":
            body.value = " Silkscreen color: White"
        elif self.silkscreen_value.GetStringSelection() == "Black":
            body.value = " Silkscreen color: Black"
        body.position = Vector2.from_xy_mm(232.294992, self.spacing)
        self.spacing += 4
        txtatt = TextAttributes()
        txtatt.size = Vector2.from_xy_mm(1, 1)
        txtatt.stroke_width = 150000  # nanometers
        body.attributes = txtatt
        body.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        self.board.create_items(body)

    def add_frontcopper(self):
        # Create and add body text
        body = BoardText()
        body.value = " Front Copper weight: " + self.frontcu_value.GetValue() + " oz"
        body.position = Vector2.from_xy_mm(232.294992, self.spacing)
        self.spacing += 4
        txtatt = TextAttributes()
        txtatt.size = Vector2.from_xy_mm(1, 1)
        txtatt.stroke_width = 150000  # nanometers
        body.attributes = txtatt
        body.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        self.board.create_items(body)

    def add_backcopper(self):
        # Create and add body text
        body = BoardText()
        body.value = " Back Copper weight: " + self.backcu_value.GetValue() + " oz"
        body.position = Vector2.from_xy_mm(232.294992, self.spacing)
        self.spacing += 4
        txtatt = TextAttributes()
        txtatt.size = Vector2.from_xy_mm(1, 1)
        txtatt.stroke_width = 150000  # nanometers
        body.attributes = txtatt
        body.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        self.board.create_items(body)

    def add_soldercolor(self):
        # Create and add body text
        body = BoardText()
        if self.mask_value.GetStringSelection() == "Green":
            body.value = " Soldermask color: Green"
        elif self.mask_value.GetStringSelection() == "Red":
            body.value = " Soldermask color: Red"
        elif self.mask_value.GetStringSelection() == "Blue":
            body.value = " Soldermask color: Blue"
        elif self.mask_value.GetStringSelection() == "Yellow":
            body.value = " Soldermask color: Yellow"
        elif self.mask_value.GetStringSelection() == "White":
            body.value = " Soldermask color: White"
        elif self.mask_value.GetStringSelection() == "Purple":
            body.value = " Soldermask color: Purple"
        elif self.mask_value.GetStringSelection() == "Black":
            body.value = " Soldermask color: Black"
        body.position = Vector2.from_xy_mm(232.294992, self.spacing)
        self.spacing += 4
        txtatt = TextAttributes()
        txtatt.size = Vector2.from_xy_mm(1, 1)
        txtatt.stroke_width = 150000  # nanometers
        body.attributes = txtatt
        body.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        
        self.board.create_items(body)

    def add_boardthickness(self):
        # Create and add body text
        body = BoardText()
        body.value = " Board thickness: " + self.thickness_value.GetValue() + " mm"
        body.position = Vector2.from_xy_mm(232.294992, self.spacing)
        self.spacing += 5
        txtatt = TextAttributes()
        txtatt.size = Vector2.from_xy_mm(1, 1)
        txtatt.stroke_width = 150000  # nanometers
        body.attributes = txtatt
        body.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        self.board.create_items(body)
    
    def add_copper_surface(self):
        # Create and add body text
        body = BoardText()
        
        if self.cu_finish_value.GetStringSelection() == "Immersion Gold (ENIG)":
            body.value = " Copper finish color: Immersion Gold (ENIG)"
        elif self.cu_finish_value.GetStringSelection() == "Immersion Silver (Ag)":
            body.value = " Copper finish color: Immersion Silver (Ag)"
        elif self.cu_finish_value.GetStringSelection() == "HASL Lead-Free":
            body.value = " Copper finish color: HASL Lead-Free"
        elif self.cu_finish_value.GetStringSelection() == "HASL Leaded":
            body.value = " Copper finish color: HASL Leaded"
        elif self.cu_finish_value.GetStringSelection() == "OSP (copper core boards only)":
            body.value = " Copper finish color: OSP (copper core boards only)"
        else :
            print("No copper finish selected.")
        body.value += "\n Copper thickness: " + self.copper_thick_value.GetValue() + " µm"

        body.position = Vector2.from_xy_mm(232.294992, self.spacing)
        self.spacing += 6
        txtatt = TextAttributes()
        txtatt.line_spacing = 2
        txtatt.multiline = True
        txtatt.size = Vector2.from_xy_mm(1, 1)
        txtatt.stroke_width = 150000  # nanometers
        body.attributes = txtatt
        body.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        self.board.create_items(body)

    def add_trackwidth_spacing(self):
        # Create and add body text
        body = BoardText()
        body.value = " Track width: " + self.track_width_value.GetValue() + " mm"
        body.value += "\n Track spacing: " + self.track_spacing_value.GetValue() + " mm"
        body.position = Vector2.from_xy_mm(232.294992, self.spacing)
        self.spacing += 4
        txtatt = TextAttributes()
        txtatt.line_spacing = 2
        txtatt.multiline = True
        txtatt.size = Vector2.from_xy_mm(1, 1)
        txtatt.stroke_width = 150000  # nanometers
        body.attributes = txtatt
        body.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        self.board.create_items(body)

    def add_holediameter(self):
        # Create and add body text
        body = BoardText()
        body.value = " Hole diameter: " + self.hole_diameter_value.GetValue() + " mm"
        body.position = Vector2.from_xy_mm(232.294992, self.spacing)
        self.spacing += 4
        txtatt = TextAttributes()
        txtatt.size = Vector2.from_xy_mm(1, 1)
        txtatt.stroke_width = 150000  # nanometers
        body.attributes = txtatt
        body.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        self.board.create_items(body)

    def add_impedctrl(self):
        # Create and add body text
        body = BoardText()
        body.value = " Impedance control: Yes"
        body.position = Vector2.from_xy_mm(232.294992, self.spacing)
        self.spacing += 4
        txtatt = TextAttributes()
        txtatt.size = Vector2.from_xy_mm(1, 1)
        txtatt.stroke_width = 150000  # nanometers
        body.attributes = txtatt
        body.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        self.board.create_items(body)
    
    def add_dimensions(self):
        # Create and add body text
        body = BoardText()
        body.value = " Dimensions- width: " + self.dimension_width_value.GetValue() + " mm"
        body.value += "\n height: " + self.dimension_height_value.GetValue() + " mm"
        body.position = Vector2.from_xy_mm(232.294992, self.spacing)
        self.spacing += 4
        txtatt = TextAttributes()
        txtatt.line_spacing = 2
        txtatt.multiline = True
        txtatt.size = Vector2.from_xy_mm(1, 1)
        txtatt.stroke_width = 150000  # nanometers
        body.attributes = txtatt
        body.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        self.board.create_items(body)

    def add_textonce(self):
        # Create and add body text
        body = BoardText()
        body.value = " idk man " + self.editortext.GetValue() + " balls"
        body.position = Vector2.from_xy_mm(232.294992, self.spacing)
        self.spacing += 4
        txtatt = TextAttributes()
        txtatt.size = Vector2.from_xy_mm(1, 1)
        txtatt.stroke_width = 150000  # nanometers
        body.attributes = txtatt
        body.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        self.board.create_items(body)

    def addtopluginfn(self):
        
        self.add_textonce()
        ###get user input regarding plugin title and name of remove button
        plugin_title = self.titleinput.GetValue().strip().replace(" ", "_")
        if not plugin_title:
            plugin_title = "myballs"
        removetitle = plugin_title + "_removebutton"

        markeradd = "        addtopluginsizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )"
        filename = "/home/zane-akers/python_scripts/kicadpython/mfgtextadder/mfgtextadderbase.py"
        with open(filename, "r") as file:
            lines = file.readlines()
        newlines = []
        for index, line in enumerate(lines):
            newlines.append(line)
            if markeradd in line:
                newlines.insert(index+1, f"        \nself.{plugin_title} = wx.CheckBox(self, wx.ID_ANY, \"{plugin_title}\", wx.DefaultPosition, wx.DefaultSize, 0)\n")
                newlines.append(f"        addtopluginsizer.Add(self.{plugin_title}, 0, wx.ALL, 5)\n\n")
                newlines.append(f"        self.{removetitle} = wx.ToggleButton( self, wx.ID_ANY, \"{removetitle}\", wx.DefaultPosition, wx.DefaultSize, 0 )\n")
                newlines.append(f"        addtopluginsizer.Add(self.{removetitle}, 0, wx.ALL, 5)\n\n")
        with open(filename, "w") as file:
            file.writelines(newlines)
        
        
    def removeplugin(self):
        marker1 = self.buttontoremove
        marker2 = self.buttontoremove.replace("_removebutton", "")
        print("buttontoremove", self.buttontoremove)
        filename = "/home/zane-akers/python_scripts/kicadpython/mfgtextadder/mfgtextadderbase.py"
        with open(filename, "r") as file:
            lines = file.readlines()
        newlines = []
        indexesto_delete = []
        for index, line in enumerate(lines):
            newlines.append(line)
            if marker1 in line or marker2 in line:
                indexesto_delete.append(index)
        for idx in reversed(indexesto_delete):
            del newlines[idx]
        with open(filename, "w") as file:
            file.writelines(newlines)

        self.Layout()

    def getremovebuttons(self):
        marker = "_removebutton"
        filename = "/home/zane-akers/python_scripts/kicadpython/mfgtextadder/mfgtextadderbase.py"
        buttonlist = []
        with open(filename, "r") as file:
            lines = file.readlines()
       #newlines = []
        for index, line in enumerate(lines):
           # newlines.append(line)
            if marker in line:
                buttonlist.append(line)
        print("buttonsfound", buttonlist)
        var_names = []
        for line in buttonlist:
            match = re.search(r'self\.\w+', line)
            if match:
                var_names.append(match.group(0))

        print(var_names)
        return var_names
    
    def getplugins(self):
        markercheck = "wx.CheckBox"
        filename = "/home/zane-akers/python_scripts/kicadpython/mfgtextadder/mfgtextadderbase.py"
        checkboxlist = []
        with open(filename, "r") as file:
            lines = file.readlines()
        for index, line in enumerate(lines):
            if markercheck in line:
                checkboxlist.append(line)
        print("buttonsfound", checkboxlist)
        var_names = []
        for line in checkboxlist:
            match = re.search(r'self\.\w+', line)
            if match:
                var_names.append(match.group(0))

        print(var_names)
        return var_names
            

if __name__ == "__main__":
    app = wx.App()
    rt = MfgInfoAction()
    rt.ShowModal()
    rt.Destroy()
