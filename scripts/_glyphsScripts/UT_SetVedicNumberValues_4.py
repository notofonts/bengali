#MenuTitle: UT-NotoBengali: Set vedic number values.
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
from math import ceil
import collections
__doc__="""
Sets number values automatically in masters.
"""
Glyphs.clearLog()

this_font = Glyphs.font

def gather_data(font, mark_glyphs, anchor_label='top_vedic'):
    """
    Collect glyph structure data in the following format:

    dictionary = {
        <glyph_name>: (<anchor_shift_value>, <base_glyph_a>, [<base_glyph_b> or <mark_glyph_b>], <number_value_label>),
        'ng_gh_ra-beng': (-285, 'ng-beng.half', 'gh-beng.half', 'VEDIC_ng_gh_ra'),
        ...
    }
    """
    # The current layer's name
    layer_name = font.selectedFontMaster.name
    total_selected = [selected_glyph.name for selected_glyph in font.selection]

    # Data dictionary
    database = {}

    for selected_glyph in font.selection:
        glyph_layer = selected_glyph.layers[layer_name]
        # Check if selected glyph is only made up of components
        # -----
        if len(glyph_layer.components) > 0 and len(glyph_layer.paths) == 0:
            reference_glyph_width = int(selected_glyph.layers[layer_name].width)
            reference_glyph_width_center = ceil(reference_glyph_width / 2)
            # Check if selected glyph is composed more than 2 components
            # -----
            if len(glyph_layer.shapes) > 2:
                shape_a = glyph_layer.shapes[0] # Component object at index 0
                shape_a_parent = font[shape_a.name] # Selected layer object of the shape_a component
                shape_b = glyph_layer.shapes[-1] # Component object at index -1
                shape_b_parent = font[shape_b.name] # Selected layer object of the shape_b component
                # Check if the 1st and last component in the shape order
                # are BASE (spacing) glyphs
                # -----
                if shape_a_parent.category == "Letter" and shape_b_parent.category == "Letter":
                    # Check if the last base is itself a component. If it is, find the
                    # parent of the component to get anchor information
                    # -----
                    base_anchor_pos_x = 0
                    if len(shape_b_parent.layers[layer_name].components) > 1:
                        parent_name = shape_b_parent.layers[layer_name].shapes[0].name
                        parent_base = font[parent_name].layers[layer_name]
                        base_anchor_pos_x = get_base_anchor_position(parent_base, anchor_label)
                        dictionary_value = compile_values(reference_glyph_width_center, base_anchor_pos_x, shape_a.name, parent_name, selected_glyph, class_label="VEDIC_")
                        if len(dictionary_value) > 0:
                            database[selected_glyph.name] = dictionary_value
                        #print(selected_glyph.name, dictionary_value)
                        """
                        # Check if the anchored base glyph of this combination has
                        # anchor in the same position as the reference layer
                        # -----
                        if reference_glyph_width_center == base_anchor_pos_x:
                            print(f"{selected_glyph.name}: anchors are fine for this combination, no adjustment needed")
                        else:
                            adjustment_value = -int(reference_glyph_width_center - base_anchor_pos_x)
                            dictionary_value = (adjustment_value, shape_a.name, [parent_name], f"VEDIC_{selected_glyph.name.split('-')[0]}")
                            database[selected_glyph.name] = dictionary_value
                            #print(selected_glyph.name, dictionary_value)
                        """
                    else:
                        base_anchor_pos_x = get_base_anchor_position(shape_b_parent.layers[layer_name], anchor_label)
                        # Check if the anchored base glyph of this combination has
                        # anchor in the same position as the reference layer
                        # -----
                        if reference_glyph_width_center == base_anchor_pos_x:
                            print(f"{selected_glyph.name}: anchors are fine for this combination, no adjustment needed")
                        else:
                            adjustment_value = -int(reference_glyph_width_center - base_anchor_pos_x)
                            dictionary_value = (adjustment_value, shape_a.name, [shape_b.name], f"VEDIC_{selected_glyph.name.split('-')[0]}")
                            database[selected_glyph.name] = dictionary_value
                            #print(selected_glyph.name, dictionary_value)
                # Check if last component is a mark glyph but has the
                # target anchor for mark-to-mark positioning.
                # -----
                elif shape_a_parent.category == "Letter" and shape_b_parent.category != "Letter":
                    # Check if the final glyph is included in the 
                    # shortlisted 'mark_glyphs' positional argument
                    # -----
                    if shape_b.name in mark_glyphs:
                        base_anchor_pos_x = get_base_anchor_position(shape_b_parent.layers[layer_name], anchor_label)
                        # Check if the anchored base glyph of this combination has
                        # anchor in the same position as the reference layer
                        # -----
                        if reference_glyph_width_center == base_anchor_pos_x:
                            print(f"{selected_glyph.name}: anchors are fine for this combination, no adjustment needed")
                        else:
                            adjustment_value = -int(reference_glyph_width_center - base_anchor_pos_x)
                            # ! Add the 'mark_glyphs' positional argument to the
                            # ! tuple collection.
                            # -----
                            dictionary_value = (adjustment_value, shape_a.name, [shape_b.name], f"VEDIC_{selected_glyph.name.split('-')[0]}")
                            database[selected_glyph.name] = dictionary_value
                            #print(selected_glyph.name, dictionary_value)
                    else:
                        # Check if the remaining components have a BASE glyph
                        # with the target anchor
                        # -----
                        if len(glyph_layer.shapes[1:-1]) == 1:
                            base = glyph_layer.shapes[1:-1][0]
                            base_anchor_pos_x = get_base_anchor_position(font[base.name].layers[layer_name], anchor_label)
                            # Check if the anchored base glyph of this combination has
                            # anchor in the same position as the reference layer
                            # -----
                            if reference_glyph_width_center == base_anchor_pos_x:
                                print(f"{selected_glyph.name}: anchors are fine for this combination, no adjustment needed")
                            else:
                                adjustment_value = -int(reference_glyph_width_center - base_anchor_pos_x)
                                dictionary_value = (adjustment_value, shape_a.name, [shape_b.name], f"VEDIC_{selected_glyph.name.split('-')[0]}")
                                database[selected_glyph.name] = dictionary_value
                                #print(selected_glyph.name, dictionary_value)
                        else:
                            count = len(glyph_layer.shapes[1:-1]) - 1
                            while count > 0:
                                base = glyph_layer.shapes[1:-1][count]
                                # Check if the calculate offset is not 0
                                # -----
                                if get_base_anchor_position(font[base.name].layers[layer_name], anchor_label) != 0:
                                    base_anchor_pos_x = get_base_anchor_position(font[base.name].layers[layer_name], anchor_label)
                                    # Check if the anchored base glyph of this combination has
                                    # anchor in the same position as the reference layer
                                    # -----
                                    if reference_glyph_width_center == base_anchor_pos_x:
                                        print(f"{selected_glyph.name}: anchors are fine for this combination, no adjustment needed")
                                    else:
                                        adjustment_value = -int(reference_glyph_width_center - base_anchor_pos_x)
                                        dictionary_value = (adjustment_value, shape_a.name, [shape_b.name], f"VEDIC_{selected_glyph.name.split('-')[0]}")
                                        database[selected_glyph.name] = dictionary_value
                                        #print(selected_glyph.name, dictionary_value)
                                    break
                                # ! Test this if the tally is not tallying!
                                # -----
                                #else:
                                #    print("no", count, base)
                                count -= 1
            elif len(glyph_layer.shapes) == 2:
                shape_a = glyph_layer.shapes[0] # Component object at index 0
                shape_a_parent = font[shape_a.name] # Selected layer object of the shape_a component
                shape_b = glyph_layer.shapes[-1] # Component object at index -1
                shape_b_parent = font[shape_b.name] # Selected layer object of the shape_b component



                            
                            


        else:
            print(f"{selected_glyph.name}: this glyph has outlines.")
    
    return (database, len(total_selected), len(database))

def get_base_anchor_position(reference_base, anchor_name):
    """
    Get the x position of the anchor from the base glyph layer
    """
    anchor_position = 0
    if reference_base.anchors[anchor_name]:
        anchor_position = int(reference_base.anchors[anchor_name].x)
    return anchor_position

def compile_values(ref_width, base_position, glyph_a, glyph_b, ref_glyph, class_label="VEDIC_"):
    """
    Check if the anchored base glyph of this combination has
    anchor in the same position as the reference layer
    """
    value = ()
    if ref_width == base_position:
        print(f"{ref_glyph.name}: anchors are fine for this combination, no adjustment needed")
        pass
    else:
        adjustment_value = -int(ref_width - base_position)
        value = (adjustment_value, glyph_a, [glyph_b], f"{class_label}{ref_glyph.name.split('-')[0]}")
        #database[selected_glyph.name] = dictionary_value
        #print(selected_glyph.name, dictionary_value)
    if value:
        return value

# Run Program

mark_glyphs_with_anchor = ["headline-beng.130", "headline-beng.200", "headline-beng.250", "aaMatra-beng.side2", "ka-beng.arm", "ka-beng.arm1", "headline-beng.ba"]

dataset_1, selection_count_1, selection_count_2 = gather_data(this_font, mark_glyphs_with_anchor, anchor_label='top_vedic')
print(dataset_1)
print(f"Total selected: {selection_count_1}\nTotal processed: {selection_count_2}")
