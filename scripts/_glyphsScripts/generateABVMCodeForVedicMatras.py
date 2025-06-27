#MenuTitle: Noto Sans Bengali: Generate ABVM feature code for select Vedic matras.
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
from math import ceil
import collections
__doc__="""
For selected set of 'composed', non-exporting glyphs in the Noto Sans Bengali source.
Evaluate their parts to determine anchor center positions and output feature code.

Note: The feature code needs to be manually added to the source under the ABVM feature
in the Thin master and under the Replace Feature custom parameter of other masters.
"""
Glyphs.clearLog()

this_font = Glyphs.font

def collect_structure(font, mark_glyphs=None):
    """
    """
    data = {}
    layer_name = font.selectedFontMaster.name
    for selected_glyph in font.selection:
        glyph_layer = selected_glyph.layers[layer_name]
        if selected_glyph.layers[layer_name].components:
            # Check if the selected conjunct has more than 2 components
            if len(selected_glyph.layers[layer_name].shapes) > 2:
                start_glyph = selected_glyph.layers[layer_name].shapes[0]
                end_glyph = selected_glyph.layers[layer_name].shapes[-1]
                # Check BASE-BASE combinations:
                if font[end_glyph.name].category == "Letter":
                    count = len(glyph_layer.shapes[1:-1]) - 1
                    while count >= 0:
                        # Check if the intermediate glyphs are 
                        # categorised as BASEs. If not only output
                        # the first and last glyphs.
                        if font[glyph_layer.shapes[1:-1][count].name].category == "Letter":
                            middle_glyph = glyph_layer.shapes[1:-1][count]
                            #print(start_glyph.name, middle_glyph.name, end_glyph.name, selected_glyph.name)
                            if selected_glyph.name not in data:
                                data[selected_glyph.name] = (start_glyph.name, middle_glyph.name, end_glyph.name)
                        else:
                            #print(start_glyph.name, end_glyph.name, selected_glyph.name)
                            if selected_glyph.name not in data:
                                data[selected_glyph.name] = (start_glyph.name, end_glyph.name)
                        count -= 1
                if font[end_glyph.name].category == "Mark":
                    if end_glyph.name in mark_glyphs:
                        count = len(glyph_layer.shapes[1:-1]) - 1
                        while count >= 0:
                            if font[glyph_layer.shapes[1:-1][count].name].category == "Letter":
                                middle_glyph = glyph_layer.shapes[1:-1][count]
                                #print(start_glyph.name, middle_glyph.name, end_glyph.name, selected_glyph.name)
                                if selected_glyph.name not in data:
                                    data[selected_glyph.name] = (start_glyph.name, middle_glyph.name, end_glyph.name)
                            else:
                                #print(start_glyph.name, end_glyph.name, selected_glyph.name)
                                if selected_glyph.name not in data:
                                    data[selected_glyph.name] = (start_glyph.name, end_glyph.name)
                            count -= 1
                    else:
                        count = len(glyph_layer.shapes[1:-1]) - 1
                        while count >= 0:
                            if font[glyph_layer.shapes[1:-1][count].name].category == "Letter":
                                middle_glyph = glyph_layer.shapes[1:-1][count]
                                #print(start_glyph.name, middle_glyph.name, selected_glyph.name)
                                if selected_glyph.name not in data:
                                    data[selected_glyph.name] = (start_glyph.name, middle_glyph.name)
                            elif font[glyph_layer.shapes[1:-1][count].name].category == "Mark":
                                if glyph_layer.shapes[1:-1][count].name in mark_glyphs:
                                    middle_glyph = glyph_layer.shapes[1:-1][count]
                                    #print(start_glyph.name, middle_glyph.name, selected_glyph.name)
                                    if selected_glyph.name not in data:
                                        data[selected_glyph.name] = (start_glyph.name, middle_glyph.name)
                            count -= 1
            elif len(selected_glyph.layers[layer_name].shapes) == 2:
                start_glyph = selected_glyph.layers[layer_name].shapes[0]
                end_glyph = selected_glyph.layers[layer_name].shapes[-1]
                # Check BASE-BASE combinations:
                if font[end_glyph.name].category == "Letter":
                    #print(start_glyph.name, end_glyph.name, selected_glyph.name)
                    if selected_glyph.name not in data:
                        data[selected_glyph.name] = (start_glyph.name, end_glyph.name)
    if data:
        return data

def get_base_anchor_position(reference_base, anchor_name):
    """
    Get the x position of the anchor from the base glyph layer
    """
    anchor_position = 0
    if reference_base.anchors[anchor_name]:
        anchor_position = int(reference_base.anchors[anchor_name].x)
    return anchor_position

def compile_values(ref_width, base_position, glyph_a, glyph_b, mark_class=None):
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
        value = (adjustment_value, glyph_a, glyph_b, mark_class)

    if value:
        return value

def calculate_distances(font, data, current_layer, mark_glyphs=None, anchor_label='top_vedic'):
    """
    """
    collection = {}
    value_check = []
    if data:
        for bases in data:
            reference_glyph_width = int(font[bases].layers[current_layer].width)
            reference_glyph_width_center = ceil(reference_glyph_width / 2)
            reference_base = font[data[bases][-1]].layers[current_layer]
            anchor_name = anchor_label
            base_anchor_pos_x = get_base_anchor_position(reference_base, anchor_name)
            if len(data[bases]) == 2:
                entry_glyph = data[bases][0]
                exit_glyph = data[bases][-1]
                if mark_glyphs is not None:
                    if exit_glyph in mark_glyphs:
                        value, glyph_a, glyph_b, marks = compile_values(reference_glyph_width_center, base_anchor_pos_x, entry_glyph, exit_glyph, mark_glyphs)
                        if bases not in collection:
                            collection[bases] = (value, glyph_a, glyph_b, marks)
                    else:
                        value, glyph_a, glyph_b, marks = compile_values(reference_glyph_width_center, base_anchor_pos_x, entry_glyph, exit_glyph, mark_glyphs)
                        if bases not in collection:
                            collection[bases] = (value, glyph_a, glyph_b)
            elif len(data[bases]) == 3:
                entry_glyph = data[bases][0]
                middle_glyph = data[bases][1]
                exit_glyph = data[bases][-1]
                if mark_glyphs is not None:
                    if exit_glyph in mark_glyphs:
                        value, glyph_a, glyph_b, marks = compile_values(reference_glyph_width_center, base_anchor_pos_x, entry_glyph, exit_glyph, mark_glyphs)
                        if bases not in collection:
                            collection[bases] = (value, glyph_a, middle_glyph, glyph_b, marks)
                    else:
                        value, glyph_a, glyph_b, marks = compile_values(reference_glyph_width_center, base_anchor_pos_x, entry_glyph, exit_glyph, mark_glyphs)
                        if bases not in collection:
                            collection[bases] = (value, glyph_a, middle_glyph, glyph_b)
    return collection

def opentype_code(data, mark_class="@BNG_VEDIC_ALL", lookup_flag="UseMarkFilteringSet", lookup_flag_marks=None):
    """
    """
    count = 1
    group_a = []
    group_b = []
    group_c = []
    marks = " ".join(lookup_flag_marks)
    for key in data:
        if len(data[key]) == 4:
            if type(data[key][-1]) != list:
                group_a.append(f"\tpos {data[key][1]} {data[key][2]} {data[key][3]} {mark_class}' <{data[key][0]} 0 0 0>;")
            elif type(data[key][-1]) == list:
                marks = " ".join(data[key][-1])
                group_b.append(f"\tpos {data[key][1]} {data[key][2]} {mark_class}' <{data[key][0]} 0 0 0>;")
        elif len(data[key]) == 3:
            group_c.append(f"\tpos {data[key][1]} {data[key][2]} {mark_class}' <{data[key][0]} 0 0 0>;")

    consolidated_group_a = list( dict.fromkeys(group_a) )
    consolidated_group_b = list( dict.fromkeys(group_b) )
    consolidated_group_c = list( dict.fromkeys(group_c) )
    for items in consolidated_group_a:
        print(f"lookup BNG_dflt_abvm_vedicMatraShift_{count}" + " {")
        print(f"lookupflag {lookup_flag} {mark_class};")
        print(items)
        print("} " + f"BNG_dflt_abvm_vedicMatraShift_{count};\n")
        count += 1

    for items in consolidated_group_b:
        print(f"lookup BNG_dflt_abvm_vedicMatraShift_{count}" + " {")
        print(f"lookupflag {lookup_flag} [{mark_class} {marks}];")
        print(items)
        print("} " + f"BNG_dflt_abvm_vedicMatraShift_{count};\n")
        count += 1
    
    for items in consolidated_group_c:
        print(f"lookup BNG_dflt_abvm_vedicMatraShift_{count}" + " {")
        print(f"lookupflag {lookup_flag} {mark_class};")
        print(items)
        print("} " + f"BNG_dflt_abvm_vedicMatraShift_{count};\n")
        count += 1

# Program
# -------

master_layer_name = this_font.selectedFontMaster.name
mark_class_name = "@BNG_VEDIC_ALL"
vedic_marks = ["uni0951", "uni1CD0", "uni1CD2", "uni1CF5.stack", "uni1CF6.stack", "uni0952", "uni1CD5", "uni1CD6", "uni1CD8", "uni1CED"]
mark_glyphs_with_anchor = ["headline-beng.130", "headline-beng.200", "headline-beng.250", "aaMatra-beng.float", "aaMatra-beng.side2", "ka-beng.arm", "ka-beng.arm1", "headline-beng.ba"]
data_collection = collect_structure(this_font, mark_glyphs=mark_glyphs_with_anchor)
second_collection = calculate_distances(this_font, data_collection, this_font.selectedFontMaster.name, mark_glyphs=mark_glyphs_with_anchor)
#print(len(this_font.selection), len(data_collection))

print("# Automatic Code End\n")
print(f"# {master_layer_name}\n")
print(f"{mark_class_name} = [" + " ".join(vedic_marks) + "];\n")
opentype_code(second_collection, lookup_flag_marks=mark_glyphs_with_anchor)
