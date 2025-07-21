
## This file is part of the mfgtextadder project.
## It is used to add manufacturing information to KiCad PCB files.

####wxframework imports####
import os
import wx
import time
from copy import deepcopy
from typing import Set
import re

from plugins.mfgtextadderbase import mfgtextadder

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

        self.add_textonce(" Number of Copper Layers: " + str(coppercounter), False, False)

    def add_heading_text(self):
        # Create and add heading text
        
        heading = BoardText()
        heading.value = "FABRICATION NOTES"
        heading.position = Vector2.from_xy_mm(220.310997, self.spacing)
        self.spacing += 6
        txtatt = TextAttributes()
        txtatt.size = Vector2.from_xy_mm(3, 3)
        txtatt.horizontal_alignment = 1 #left alignment
        txtatt.stroke_width = 150000  # nanometers (7 mm thickness equivalent)
        heading.attributes = txtatt
        heading.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        
        self.board.create_items(heading)

    def run(self, event):
        self.alphabet = ["A.  ", "B.  ", "C.  ", "D.  ", "E.  ", "F.  ", "G.  ", "H.  ", "I.  ", "J.  ", "K.  ", "L.  ", "M.  "]
        self.index = 0
        self.spacing = 19.946399
        self.horizontal = 220.310997
        self.add_heading_text()

        for i in self.getremovebuttonslist():
            button = i.replace("self.", "")
            self.removebuttonheyo = getattr(self, button, None)
            print("removebutton", self.removebuttonheyo)
            if self.removebuttonheyo.GetValue() is True:
                self.buttontoremove = i
                print(f"Going to remove plugin: {button}")
                self.removeplugin()

        
        for plugin in self.getusermadepluginslist():
            checkbox = plugin.replace("self.", "")
            self.originalcheckbox = getattr(self, checkbox, None) #get original button variable in mfgtextadder
            print("user made checkbox", self.originalcheckbox)
            if self.originalcheckbox.GetValue() is True:
                self.userpluginchecked = plugin
                print(f"Going to initiate: {checkbox}")
                self.usermadepluginbackend(checkbox)


        # default text additions
        if self.copper_count.IsChecked():
            self.horizontal = 220.310997
            self.add_textonce(self.alphabet[self.index], False, True)
            self.index += 1
            self.number_copperlayers()
            

        if self.drill_plot_show.IsChecked():
            print("Drill Plot checkbox checked.")
            self.horizontal = 220.310997
            self.add_textonce(self.alphabet[self.index], False, True)
            self.index += 1
            self.add_drillplot()
           

        # Add text based on checkbox selections
        if self.silkscreen_color.IsChecked():
            print("Silkscreen checkbox checked.")
            self.horizontal = 220.310997
            self.add_textonce(self.alphabet[self.index], False, True)
            self.index += 1
            self.add_silkscreen()
            

        if self.front_copperweight.IsChecked():
            print("Front Copper checkbox checked.")
            self.horizontal = 220.310997
            self.add_textonce(self.alphabet[self.index], False, True)
            self.index += 1
            self.add_frontcopper()
            


        if self.back_copperweight.IsChecked():
            print("Back Copper checkbox checked.")
            self.horizontal = 220.310997
            self.add_textonce(self.alphabet[self.index], False, True)
            self.index += 1
            self.add_backcopper()
            
        
        if self.mask_color.IsChecked():
            print("Soldermask checkbox checked.")
            self.horizontal = 220.310997
            self.add_textonce(self.alphabet[self.index], False, True)
            self.index += 1
            self.add_soldercolor()
   
        if self.board_thickness.IsChecked():
            print("Board Thickness checkbox checked.")
            self.horizontal = 220.310997
            self.add_textonce(self.alphabet[self.index], False, True)
            self.index += 1
            self.add_boardthickness()
     
        if self.copper_srf_overall.IsChecked():
            print("Copper Surface Finish checkbox checked.")
            self.horizontal = 220.310997
            self.add_textonce(self.alphabet[self.index], False, True)
            self.index += 1
            self.add_copper_surface()
        

        if self.trackwidth_spacing.IsChecked():
            print("Track Width and Spacing checkbox checked.")
            self.horizontal = 220.310997
            self.add_textonce(self.alphabet[self.index], False, True)
            self.index += 1
            self.add_trackwidth_spacing()
           
        

# add new line before hole diamter, print hole diameter, add text on next line and a space on next line
        if self.min_hole_diameter.IsChecked():
            print("Minimum Hole Diameter checkbox checked.")
         
            self.horizontal = 220.310997
            self.add_textonce(self.alphabet[self.index], False, True)
            self.add_holediameter()
            
            self.index += 1

        if self.imped_ctrl.IsChecked():
            print("Impedance Control checkbox checked.")
            self.horizontal = 220.310997
            self.add_textonce(self.alphabet[self.index], False, True)
            self.add_impedctrl()
            self.index += 1

        if self.dimensions.IsChecked():
            print("Dimensions checkbox checked.")
            self.horizontal = 220.310997
            self.add_textonce(self.alphabet[self.index], False, True)
            self.index += 1

            self.add_dimensions()
           
            

        if self.applyonce.GetValue():
            self.horizontal = 220.310997
            self.add_textonce(self.alphabet[self.index], False, True)
            self.index += 1
            self.add_textonce(self.editortext.GetValue(), False, False)

        if self.addtoplugin.GetValue():
            # create function
            self.createusermadeplugin()

        
        

  ###########add text functions############
    def add_drillplot(self):
        # Create and add body text
        self.add_textonce(" Drill Plot Shows Finished Hole Sizes", False, False)
       
    def add_silkscreen(self):
        # Create and add body text
        if self.silkscreen_value.GetStringSelection() == "White":
            self.add_textonce(" Silkscreen color: White", False, False)
        elif self.silkscreen_value.GetStringSelection() == "Black":
            self.add_textonce(" Silkscreen color: Black", False, False)

    def add_frontcopper(self):
        # Create and add body text
        self.add_textonce(" Front Copper weight: " + self.frontcu_value.GetValue() + " oz", False, False)
       

    def add_backcopper(self):
        # Create and add body text
        self.add_textonce(" Back Copper weight: " + self.backcu_value.GetValue() + " oz", False, False)
       

    def add_soldercolor(self):
        # Create and add body text
        body = BoardText()
        if self.mask_value.GetStringSelection() == "Green":
            self.add_textonce(" Soldermask color: Green", False, False)
        elif self.mask_value.GetStringSelection() == "Red":
            self.add_textonce(" Soldermask color: Red", False, False)
        elif self.mask_value.GetStringSelection() == "Blue":
            self.add_textonce(" Soldermask color: Blue", False, False)
        elif self.mask_value.GetStringSelection() == "Yellow":
            self.add_textonce(" Soldermask color: Yellow", False, False)
        elif self.mask_value.GetStringSelection() == "White":
            self.add_textonce(" Soldermask color: White", False, False)
        elif self.mask_value.GetStringSelection() == "Purple":
            self.add_textonce(" Soldermask color: Purple", False, False)
        elif self.mask_value.GetStringSelection() == "Black":
            self.add_textonce(" Soldermask color: Black", False, False)

    def add_boardthickness(self):
        # Create and add body text
        self.add_textonce(" Board thickness: " + self.thickness_value.GetValue() + " mm", False, False)
        
    
    def add_copper_surface(self):
        # Create and add body text
        
        if self.cu_finish_value.GetStringSelection() == "Immersion Gold (ENIG)":
            self.add_textonce(" Copper finish color: Immersion Gold (ENIG)", False, False)
        elif self.cu_finish_value.GetStringSelection() == "Immersion Silver (Ag)":
            self.add_textonce(" Copper finish color: Immersion Silver (Ag)", False, False)
        elif self.cu_finish_value.GetStringSelection() == "HASL Lead-Free":
            self.add_textonce(" Copper finish color: HASL Lead-Free", False, False)
        elif self.cu_finish_value.GetStringSelection() == "HASL Leaded":
            self.add_textonce(" Copper finish color: HASL Leaded", False, False)
        elif self.cu_finish_value.GetStringSelection() == "OSP (copper core boards only)":
            self.add_textonce(" Copper finish color: OSP (copper core boards only)", False, False)
        else :
            print("No copper finish selected.")
            self.add_textonce("\n Copper finish color: None", False, False)

        self.add_textonce("\n Copper thickness: " + self.copper_thick_value.GetValue() + " µm", False, False)


    def add_trackwidth_spacing(self):
        # Create and add body text
        self.add_textonce(" Track width: " + self.track_width_value.GetValue() + " mm", False, False)
        self.add_textonce(" Track spacing: " + self.track_spacing_value.GetValue() + " mm", False, False)

    def add_holediameter(self):
        # Create and add body text
        self.add_textonce(" Hole diameter: " + self.hole_diameter_value.GetValue() + " mm", False, False)

    def add_impedctrl(self):
        # Create and add body text
        self.add_textonce(" Impedance control: Yes", False, False)

    def add_dimensions(self):
        # Create and add body text
        self.add_textonce(" Dimensions- width: ", False, True)
        self.add_textonce(self.dimension_width_value.GetValue(), True, True)
        self.add_textonce(" mm\n", False, False)
        
        self.horizontal = 220.310997
        self.add_textonce("    ", False, True)
        self.add_textonce(" Dimensions- height: ", False, True)
        self.add_textonce(self.dimension_height_value.GetValue(), True, True)
        self.add_textonce("mm\n", False, True)
        self.add_textonce(" ", False, False)
        #self.add_textonce(" Dimensions- height: " + self.dimension_height_value.GetValue() + " mm")

    def add_textonce(self, inputtext, underline, sameline):
        # Create and add body text
        body = BoardText()
        body.value =  inputtext
        
        if sameline:
            #self.horizontal += 8
            
            body.position = Vector2.from_xy_mm(self.horizontal, self.spacing)
            self.horizontal += len(inputtext)+2

        else:
            # self.spacing += 4
            body.position = Vector2.from_xy_mm(self.horizontal, self.spacing)
            self.spacing += 4
        txtatt = TextAttributes()
        txtatt.size = Vector2.from_xy_mm(1, 1)
        txtatt.horizontal_alignment = 1 #left alignment
        txtatt.stroke_width = 150000  # nanometers
        if underline:
            txtatt.underlined = True  # Underline the text
        body.attributes = txtatt
        body.layer = BoardLayer.BL_F_Fab  # Front fabrication layer
        self.board.create_items(body)

    def createusermadeplugin(self):
        
        
        ###get user input regarding plugin title and name of remove button
        plugin_title = self.titleinput.GetValue().strip().replace(" ", "_")
        if not plugin_title:
            plugin_title = "ur supposed to give this a title nimrod"
        removetitle = plugin_title + "_removebutton"
        self.horizontal = 220.310997
        self.add_textonce(self.alphabet[self.index], False, True)
        self.index += 1
        self.add_textonce(self.editortext.GetValue(), False, False)


        markeradd = "        addtopluginsizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )"
        filename = "/home/zane-akers/python_scripts/kicadpython/mfgtextadder/plugins/mfgtextadderbase.py"
        with open(filename, "r") as file:
            lines = file.readlines()
        newlines = []
        for i, line in enumerate(lines):
            newlines.append(line)
            if markeradd in line:
                newlines.insert(i+1, f"\n        self.{plugin_title} = wx.CheckBox(self, wx.ID_ANY, \"{plugin_title}\", wx.DefaultPosition, wx.DefaultSize, 0)\n")
                newlines.append(f"        addtopluginsizer.Add(self.{plugin_title}, 0, wx.ALL, 5)\n\n")
                newlines.append(f"#text that {plugin_title} spits out into the pcb: {self.editortext.GetValue()}\n")
                newlines.append(f"        self.{removetitle} = wx.ToggleButton( self, wx.ID_ANY, \"{removetitle}\", wx.DefaultPosition, wx.DefaultSize, 0 )\n")
                newlines.append(f"        addtopluginsizer.Add(self.{removetitle}, 0, wx.ALL, 5)\n\n")
        with open(filename, "w") as file:
            file.writelines(newlines)
        
        
    def removeplugin(self):
        marker1 = self.buttontoremove
        marker2 = self.buttontoremove.replace("_removebutton", "")
        print("buttontoremove", self.buttontoremove)
        filename = "/home/zane-akers/python_scripts/kicadpython/mfgtextadder/plugins/mfgtextadderbase.py"
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

    def getremovebuttonslist(self):
        marker = "_removebutton"
        filename = "/home/zane-akers/python_scripts/kicadpython/mfgtextadder/plugins/mfgtextadderbase.py"
        buttonlist = []
        with open(filename, "r") as file:
            lines = file.readlines()
       #newlines = []
        for index, line in enumerate(lines):
           # newlines.append(line)
            if marker in line:
                buttonlist.append(line)
       # print("buttonsfound", buttonlist)
        var_names = []
        for line in buttonlist:
            match = re.search(r'self\.\w+', line)
            if match:
                var_names.append(match.group(0))

        #print(var_names)
        return var_names
    
    def getusermadepluginslist(self):
        standardcheckbox = ['self.drill_plot_show', 'self.copper_count', 
                            'self.front_copperweight', 'self.back_copperweight', 
                            'self.mask_color', 'self.silkscreen_color', 'self.board_thickness', 
                            'self.copper_srf_overall', 'self.trackwidth_spacing', 
                            'self.min_hole_diameter', 'self.imped_ctrl', 'self.dimensions']
        markercheck = "wx.CheckBox"
        filename = "/home/zane-akers/python_scripts/kicadpython/mfgtextadder/plugins/mfgtextadderbase.py"
        checkboxlist = []
        with open(filename, "r") as file:
            lines = file.readlines()
        for index, line in enumerate(lines):
            if markercheck in line:
                checkboxlist.append(line)
        #print("check boxes found", checkboxlist)
        plugin_names = []
        for line in checkboxlist:
            match = re.search(r'self\.\w+', line)
            if match and match.group(0) not in standardcheckbox:
                plugin_names.append(match.group(0))

        print(plugin_names)
        return plugin_names
            

    def usermadepluginbackend(self, plugin_title):
        marker = f"#text that {plugin_title} spits out into the pcb: "
        filename = "/home/zane-akers/python_scripts/kicadpython/mfgtextadder/plugins/mfgtextadderbase.py"

        with open(filename, "r") as file:
            lines = file.readlines()

        usermadeplugintext = ""
        for line in lines:
            if marker in line:
                # Keep only the part after the marker
                usermadeplugintext += line.split(marker)[1] + "\n"

        print(usermadeplugintext)
        self.horizontal = 220.310997
        self.add_textonce(self.alphabet[self.index], False, True)
        self.index += 1
        self.add_textonce(usermadeplugintext, False, False)
        

if __name__ == "__main__":
    app = wx.App()
    rt = MfgInfoAction()
    rt.ShowModal()
    rt.Destroy()
