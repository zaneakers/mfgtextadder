# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-85-gdf26f269)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class mfgtextadder
###########################################################################

class mfgtextadder ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Manufacturing Data editor"), pos = wx.DefaultPosition, size = wx.Size( 1050,780 ), style = wx.DEFAULT_DIALOG_STYLE|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        overallsizer = wx.BoxSizer( wx.VERTICAL )

        mainsizer = wx.FlexGridSizer( 13, 4, 0, 0 )
        mainsizer.AddGrowableRow( 0 )
        mainsizer.SetFlexibleDirection( wx.BOTH )
        mainsizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

        mainsizer.SetMinSize( wx.Size( 900,630 ) )
        sizer_names = wx.GridSizer( 12, 1, 0, 0 )

        sizer_names.SetMinSize( wx.Size( 270,648 ) )
        self.drill_plot_show = wx.CheckBox( self, wx.ID_ANY, _(u"Drill Plot Shows Finished Hole Sizes"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer_names.Add( self.drill_plot_show, 0, wx.ALL, 5 )

        self.copper_count = wx.CheckBox( self, wx.ID_ANY, _(u"Copper Layer Count"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer_names.Add( self.copper_count, 0, wx.ALL, 5 )

        self.front_copperweight = wx.CheckBox( self, wx.ID_ANY, _(u"Front Copper Weight"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer_names.Add( self.front_copperweight, 0, wx.ALL, 5 )

        self.back_copperweight = wx.CheckBox( self, wx.ID_ANY, _(u"Back Copper Weight"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer_names.Add( self.back_copperweight, 0, wx.ALL, 5 )

        self.mask_color = wx.CheckBox( self, wx.ID_ANY, _(u"Solder Mask Color"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer_names.Add( self.mask_color, 0, wx.ALL, 5 )

        self.silkscreen_color = wx.CheckBox( self, wx.ID_ANY, _(u"Silkscreen Color"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer_names.Add( self.silkscreen_color, 0, wx.ALL, 5 )

        self.board_thickness = wx.CheckBox( self, wx.ID_ANY, _(u"Total Board Thickness"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer_names.Add( self.board_thickness, 0, wx.ALL, 5 )

        self.copper_srf_overall = wx.CheckBox( self, wx.ID_ANY, _(u"Copper Surface Finish/Thickness"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer_names.Add( self.copper_srf_overall, 0, wx.ALL, 5 )

        self.trackwidth_spacing = wx.CheckBox( self, wx.ID_ANY, _(u"Min. Track width/spacing"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer_names.Add( self.trackwidth_spacing, 0, wx.ALL, 5 )

        self.min_hole_diameter = wx.CheckBox( self, wx.ID_ANY, _(u"Min. Hole Diameter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer_names.Add( self.min_hole_diameter, 0, wx.ALL, 5 )

        self.imped_ctrl = wx.CheckBox( self, wx.ID_ANY, _(u"Impedance Control"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer_names.Add( self.imped_ctrl, 0, wx.ALL, 5 )

        self.dimensions = wx.CheckBox( self, wx.ID_ANY, _(u"Dimensions (width/height)"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer_names.Add( self.dimensions, 0, wx.ALL, 5 )


        mainsizer.Add( sizer_names, 1, wx.ALL, 5 )

        sizer1_values = wx.GridSizer( 12, 1, 0, 0 )

        sizer1_values.SetMinSize( wx.Size( 200,647 ) )
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        sizer1_values.Add( self.m_staticText2, 0, 0, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        sizer1_values.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.frontcu_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer1_values.Add( self.frontcu_value, 0, wx.ALL, 5 )

        self.backcu_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer1_values.Add( self.backcu_value, 0, wx.ALL, 5 )

        mask_valueChoices = [ _(u"Green"), _(u"Purple"), _(u"Red"), _(u"Yellow"), _(u"Blue"), _(u"White"), _(u"Black") ]
        self.mask_value = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mask_valueChoices, 0 )
        self.mask_value.SetSelection( 0 )
        sizer1_values.Add( self.mask_value, 0, wx.ALL, 5 )

        silkscreen_valueChoices = [ _(u"White"), _(u"Black") ]
        self.silkscreen_value = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, silkscreen_valueChoices, 0 )
        self.silkscreen_value.SetSelection( 0 )
        sizer1_values.Add( self.silkscreen_value, 0, wx.ALL, 5 )

        self.thickness_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer1_values.Add( self.thickness_value, 0, wx.ALL, 5 )

        cu_finish_valueChoices = [ _(u"Immersion Gold (ENIG)"), _(u"Immersion Silver (Ag)"), _(u"HASL Lead-Free"), _(u"HASL Leaded"), _(u"OSP (copper core boards only)") ]
        self.cu_finish_value = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cu_finish_valueChoices, 0 )
        self.cu_finish_value.SetSelection( 0 )
        sizer1_values.Add( self.cu_finish_value, 0, wx.ALL, 5 )

        self.track_width_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer1_values.Add( self.track_width_value, 0, wx.ALL, 5 )

        self.hole_diameter_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer1_values.Add( self.hole_diameter_value, 0, wx.ALL, 5 )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        sizer1_values.Add( self.m_staticText13, 0, wx.ALL, 5 )

        self.dimension_width_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer1_values.Add( self.dimension_width_value, 0, wx.ALL, 5 )


        mainsizer.Add( sizer1_values, 1, wx.ALL, 5 )

        sizer_values = wx.GridSizer( 12, 1, 0, 0 )

        sizer_values.SetMinSize( wx.Size( 100,647 ) )
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        sizer_values.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        sizer_values.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        sizer_values.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        sizer_values.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        sizer_values.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        sizer_values.Add( self.m_staticText9, 0, wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        sizer_values.Add( self.m_staticText10, 0, wx.ALL, 5 )

        self.copper_thick_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer_values.Add( self.copper_thick_value, 0, wx.ALL, 5 )

        self.track_spacing_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer_values.Add( self.track_spacing_value, 0, wx.ALL, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        sizer_values.Add( self.m_staticText11, 0, wx.ALL, 5 )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        sizer_values.Add( self.m_staticText12, 0, wx.ALL, 5 )

        self.dimension_height_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        sizer_values.Add( self.dimension_height_value, 0, wx.ALL, 5 )


        mainsizer.Add( sizer_values, 1, wx.ALL, 5 )

        addtopluginsizer = wx.FlexGridSizer( 0, 2, 0, 0 )
        addtopluginsizer.SetFlexibleDirection( wx.BOTH )
        addtopluginsizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_checkBox17 = wx.CheckBox( self, wx.ID_ANY, _(u"Check Me!"), wx.DefaultPosition, wx.DefaultSize, 0 )
        addtopluginsizer.Add( self.m_checkBox17, 0, wx.ALL, 5 )

        self.removebutton = wx.ToggleButton( self, wx.ID_ANY, _(u"remove"), wx.DefaultPosition, wx.DefaultSize, 0 )
        addtopluginsizer.Add( self.removebutton, 0, wx.ALL, 5 )
        self.title_here = wx.CheckBox(self, wx.ID_ANY, "title_here", wx.DefaultPosition, wx.DefaultSize, 0)
        addtopluginsizer.Add(self.title_here, 0, wx.ALL, 5)
        self.title_here_removebutton = wx.ToggleButton( self, wx.ID_ANY, "title_here_removebutton", wx.DefaultPosition, wx.DefaultSize, 0 )
        addtopluginsizer.Add(self.title_here_removebutton, 0, wx.ALL, 5)
        self.title_here = wx.CheckBox(self, wx.ID_ANY, "title_here", wx.DefaultPosition, wx.DefaultSize, 0)
        addtopluginsizer.Add(self.title_here, 0, wx.ALL, 5)
        self.title_here_removebutton = wx.ToggleButton( self, wx.ID_ANY, "title_here_removebutton", wx.DefaultPosition, wx.DefaultSize, 0 )
        addtopluginsizer.Add(self.title_here_removebutton, 0, wx.ALL, 5)

        mainsizer.Add( addtopluginsizer, 1, wx.EXPAND, 2 )


        overallsizer.Add( mainsizer, 1, wx.EXPAND, 5 )

        editortextoverallsizer = wx.FlexGridSizer( 2, 4, 0, 0 )
        editortextoverallsizer.SetFlexibleDirection( wx.BOTH )
        editortextoverallsizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        plugintitlesizer = wx.BoxSizer( wx.VERTICAL )

        self.titleinput = wx.TextCtrl( self, wx.ID_ANY, _(u"title here"), wx.DefaultPosition, wx.DefaultSize, 0 )
        plugintitlesizer.Add( self.titleinput, 0, wx.ALL, 5 )


        editortextoverallsizer.Add( plugintitlesizer, 1, wx.EXPAND, 5 )

        editortextsizer = wx.FlexGridSizer( 2, 1, 0, 0 )
        editortextsizer.SetFlexibleDirection( wx.BOTH )
        editortextsizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.editortext = wx.TextCtrl( self, wx.ID_ANY, _(u"this very professional text box is so you can add your own text to the pcb"), wx.DefaultPosition, wx.Size( 700,50 ), wx.TE_MULTILINE )
        editortextsizer.Add( self.editortext, 0, wx.ALL, 5 )


        editortextoverallsizer.Add( editortextsizer, 1, wx.EXPAND, 5 )

        editortextbuttonsizer = wx.FlexGridSizer( 2, 1, 0, 0 )
        editortextbuttonsizer.SetFlexibleDirection( wx.BOTH )
        editortextbuttonsizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.applyonce = wx.RadioButton( self, wx.ID_ANY, _(u"Apply once"), wx.DefaultPosition, wx.DefaultSize, 0 )
        editortextbuttonsizer.Add( self.applyonce, 0, wx.ALL, 5 )

        self.addtoplugin = wx.RadioButton( self, wx.ID_ANY, _(u"Add to Plugin"), wx.DefaultPosition, wx.DefaultSize, 0 )
        editortextbuttonsizer.Add( self.addtoplugin, 0, wx.ALL, 5 )


        editortextoverallsizer.Add( editortextbuttonsizer, 1, wx.EXPAND, 5 )

        self.Run = wx.Button( self, wx.ID_ANY, _(u"Run"), wx.DefaultPosition, wx.DefaultSize, 0 )
        editortextoverallsizer.Add( self.Run, 0, wx.ALIGN_BOTTOM|wx.ALL|wx.BOTTOM, 5 )


        overallsizer.Add( editortextoverallsizer, 1, wx.EXPAND|wx.TOP, 5 )


        self.SetSizer( overallsizer )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


