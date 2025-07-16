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


if __name__=='__main__':
    kicad = KiCad()
    board = kicad.get_board()
    ###heading####
    text_box = BoardText()
    text_box.value = "FABRICATION NOTES"
    text_box.position = Vector2.from_xy_mm(233.310997, 19.946399) 

    txtatt = TextAttributes()
    txtatt.size = Vector2.from_xy_mm(3, 3) 
    txtatt.stroke_width = 150000 # = 7 mm thickness, so value is in nanometers
    text_box.attributes = txtatt
    text_box.layer = BoardLayer.BL_F_Fab  # Set to front fabrication layer
    
    board.create_items(text_box)

####body text#####
    text_box = BoardText()
    text_box.value = "A. Drill Plot Shows Finished Hole Sizes \n test"
    text_box.position = Vector2.from_xy_mm(232.294992, 23.756402) 

    txtatt = TextAttributes()
    txtatt.size = Vector2.from_xy_mm(1, 1) 
    txtatt.stroke_width = 150000 # = 7 mm thickness, so value is in nanometers
    txtatt.multiline = True
    txtatt.line_spacing = 2

    text_box.attributes = txtatt
    text_box.layer = BoardLayer.BL_F_Fab  # Set to front fabrication layer
    
    board.create_items(text_box)
    
    # copper layer counter
    stackup = board.get_stackup()
        
        # Assuming the BoardStackup exposes copper_layers, iterate over them.
    #print(stackup)
    coppercounter = 0
    for i in stackup.layers:
        print(f"Layer {i}: {board_layer.canonical_name(i)}")
        if i.material_name == "copper":
            coppercounter += 1
            print(f"copper layer {coppercounter} found: {board_layer.canonical_name(i)}")

