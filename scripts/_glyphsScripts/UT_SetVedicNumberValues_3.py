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

anchors_name = "top_vedic"
mark_glyphs_with_anchor = ["headline-beng.130", "headline-beng.200", "headline-beng.250", "aaMatra-beng.side2", "ka-beng.arm", "ka-beng.arm1", "headline-beng.ba"]

internal_database_1 = {}
internal_database_2 = {}

def create_glyphdata_dict(data, value, base_glyphs, ref_data):
    original_base_A, original_base_B = base_glyphs
    #print(value, ref_data, base_glyphs)
    new_group = []
    for k in data[value]:
        print(data[value])
        if data[value][k][0][0] == original_base_A:
            #print(value, k, data[value][k], original_base_B)
            group = data[value][k][0][1]
            if original_base_B not in group:
                group+=original_base_B
            new_group = group
        else:
            #print(ref_data, data[value][k][0][0], data[value][k][0][0], value)
            print(ref_data)
            #data[value][ref_data] : 
    new_group = list( dict.fromkeys(new_group) )
    new_dict = {ref_data: [(original_base_A, new_group)]}
    #print("Repeat", ref_data, original_base_A, new_group, value)
    if new_dict:
        return new_dict
    else:
        return None
    
    #print(new_bases)
    #if original_base_A == data:

for g in this_font.selection:
    layer_name = this_font.selectedFontMaster.name
    #print(g.layers[layer_name].compo)
    if g.layers[layer_name].components:
        #print(len(g.layers[layer_name].components))
        #print(g.name, int(g.layers[layer_name].width), int(g.layers[layer_name].width/2))
        ref_glyph_width = int(g.layers[layer_name].width)
        ref_glyph_width_center = ceil(ref_glyph_width/2)
        if len(g.layers[layer_name].shapes) > 2:
            first_comp = g.layers[layer_name].shapes[0]
            last_comp = g.layers[layer_name].shapes[-1]
            #print(first_comp, last_comp)
            if this_font[first_comp.name].category == "Letter" and this_font[last_comp.name].category == "Letter":
                base_anchor_pos_x = 0
                if this_font[last_comp.name].layers[layer_name].anchors[anchors_name]:
                    base_anchor_pos_x = int(this_font[last_comp.name].layers[layer_name].anchors[anchors_name].x)
                    base_glyph_width = int(this_font[last_comp.name].layers[layer_name].width)
                    if ref_glyph_width_center == base_anchor_pos_x:
                        print(f"Multi; Remove from list: {g.name}")
                    else:
                        new_value = -int(ref_glyph_width_center - base_anchor_pos_x)
                        bases = (first_comp.name, [last_comp.name])
                        references = (g.name, f"VEDIC_{g.name.split('-')[0]}")
                        if new_value not in internal_database_1:
                            internal_database_1[new_value] = {references: [bases]}
                            print("Novel", references, bases, new_value)
                        else:
                            print("Repeat", references, bases, new_value)
                            new_struct = create_glyphdata_dict(internal_database_1, new_value, bases, references)
                            if new_struct:
                                #print(new_struct, new_value)
                                #print("TEST 1 Repeat", new_struct[0], new_struct[1], new_value)
                                internal_database_1[new_value] = new_struct

                elif this_font[last_comp.name].layers[layer_name].components:
                    first_comp_glyph = this_font[last_comp.name].layers[layer_name].shapes[0]
                    if this_font[first_comp_glyph.name].layers[layer_name].anchors[anchors_name]:
                        base_anchor_pos_x = int(this_font[first_comp_glyph.name].layers[layer_name].anchors[anchors_name].x)
                        base_glyph_width = int(this_font[first_comp_glyph.name].layers[layer_name].width)
                        if ref_glyph_width_center == base_anchor_pos_x:
                            print(f"Multi; Remove from list: {g.name}")
                        else:
                            new_value = -int(ref_glyph_width_center - base_anchor_pos_x)
                            bases = (first_comp.name, [first_comp_glyph.name])
                            references = (g.name, f"VEDIC_{g.name.split('-')[0]}")
                            if new_value not in internal_database_1:
                                internal_database_1[new_value] = {references: [bases]}
                                print("Novel", references, bases, new_value)
                            else:
                                print("Repeat", references, bases, new_value)
                                new_struct = create_glyphdata_dict(internal_database_1, new_value, bases, references)
                                if new_struct:
                                    #print(new_struct, new_value)
                                    #print("TEST 1 Repeat", new_struct[0], new_struct[1], new_value)
                                    internal_database_1[new_value] = new_struct


            elif this_font[first_comp.name].category == "Letter" and this_font[last_comp.name].category != "Letter":
                if last_comp.name in mark_glyphs_with_anchor:
                    base_anchor_pos_x = 0
                    if this_font[last_comp.name].layers[layer_name].anchors[anchors_name]:
                        base_anchor_pos_x = int(this_font[last_comp.name].layers[layer_name].anchors[anchors_name].x)
                        new_value = -int(ref_glyph_width_center - base_anchor_pos_x)
                        bases = (first_comp.name, [last_comp.name])
                        references = (g.name, f"VEDIC_{g.name.split('-')[0]}")
                        if new_value not in internal_database_2:
                            internal_database_2[new_value] = {references: bases}
                        #elif new_value in internal_database_2 and data_struct[0] not in internal_database_2[new_value]:
                        #    internal_database_2[new_value][data_struct[0]] = data_struct[1]
                        else:
                            new_struct = create_glyphdata_dict(internal_database_2, new_value, bases, references)
                            if new_struct:
                                #print(new_struct, new_value)
                                #print("TEST 1 Repeat", new_struct[0], new_struct[1], new_value)
                                internal_database_2[new_value] = new_struct
                else:
                    for c in g.layers[layer_name].shapes[1:-1]:
                        if this_font[c.name].category == "Letter":
                            base_anchor_pos_x = 0
                            if this_font[c.name].layers[layer_name].anchors[anchors_name]:
                                base_anchor_pos_x = int(this_font[c.name].layers[layer_name].anchors[anchors_name].x)
                                base_glyph_width = int(this_font[c.name].layers[layer_name].width)
                                if ref_glyph_width_center == base_anchor_pos_x:
                                    print(f"Multi; Remove from list: {g.name}")
                                else:
                                    new_value = -int(ref_glyph_width_center - base_anchor_pos_x)
                                    bases = (first_comp.name, [c.name]) 
                                    references = (g.name, f"VEDIC_{g.name.split('-')[0]}")
                                    if new_value not in internal_database_1:
                                        internal_database_1[new_value] = {references: [bases]}
                                        print("Novel", references, bases, new_value)
                                    else:
                                        print("Repeat", references, bases, new_value)
                                        new_struct = create_glyphdata_dict(internal_database_1, new_value, bases, references)
                                        if new_struct:
                                            #print(new_struct, new_value)
                                            #print("Repeat", new_struct[0], new_struct[1], new_value)
                                            internal_database_1[new_value] = new_struct
                            else:
                                print("! Multi comp: Untested 2")
                                print(g.name, last_comp)


        elif len(g.layers[layer_name].shapes) == 2:
            first_comp = g.layers[layer_name].shapes[0]
            last_comp = g.layers[layer_name].shapes[-1]
            if this_font[first_comp.name].category == "Letter" and this_font[last_comp.name].category == "Letter":
                base_anchor_pos_x = 0
                if this_font[last_comp.name].layers[layer_name].anchors[anchors_name]:
                    base_anchor_pos_x = int(this_font[last_comp.name].layers[layer_name].anchors[anchors_name].x)
                    base_glyph_width = int(this_font[last_comp.name].layers[layer_name].width)
                    if ref_glyph_width_center == base_anchor_pos_x:
                        print(f"Single; Remove from list: {g.name}")
                    else:
                        new_value = -int(ref_glyph_width_center - base_anchor_pos_x)
                        bases = (first_comp.name, [last_comp.name])
                        references = (g.name, f"VEDIC_{g.name.split('-')[0]}")
                        if new_value not in internal_database_1:
                            internal_database_1[new_value] = {references: [bases]}
                            print("Novel", references, bases, new_value)
                        else:
                            print("Repeat", references, bases, new_value)
                            new_struct = create_glyphdata_dict(internal_database_1, new_value, bases, references)
                            if new_struct:
                                #print(new_struct, new_value)
                                #print("Repeat", new_struct[0], new_struct[1], new_value)
                                internal_database_1[new_value] = new_struct

                else:
                    print("! Single comp: Untested")
                    print(g.name, ref_glyph_width_center)
            elif this_font[first_comp.name].category == "Letter" and this_font[last_comp.name].category != "Letter":
                base_anchor_pos_x = int(this_font[first_comp.name].layers[layer_name].anchors[anchors_name].x)
                if ref_glyph_width_center == base_anchor_pos_x:
                    print(f"Single; Remove from list: {g.name}")
                else:
                    print(f"Single; Letter and Mark; Remove from list: {g.name}")

#print(lookups)

def lookup_labels(substitution_data, lookup_flag=("0", ""), lookup_name_prefix="BNG_dflt_", feature_tag="abvm_", lookup_name_desc="None"):
    subs = output_feature_code(substitution_data)
    if subs:
        print(f"lookup {lookup_name_prefix}{feature_tag}{lookup_name_desc}" + " {")
        if lookup_flag[1] != "" and type(lookup_flag[1]) == str:
            print(f"lookupflag {lookup_flag[0]} {lookup_flag[1]};")
        elif type(lookup_flag[1]) == list:
            glyphs = ""
            for g in lookup_flag[1]:
                glyphs += g,
            print(f"lookupflag {lookup_flag[0]} {glyphs};")
        for rules in subs:
            print(rules)
        print("} " + f"{lookup_name_prefix}{feature_tag}{lookup_name_desc};")

def output_feature_code(feature_data):
    collected_data = []
    if feature_data:
        sorted_data = collections.OrderedDict(sorted(feature_data.items()))
        for key in sorted_data:
            for k, v in sorted_data[key].items():
                #print(k, v)
                number_value_name = k[1]
                group = ""
                glyph_a = v[0]
                if type(v[1]) == list:
                    if len(v[1]) > 1:
                        group = " ".join(v[1])
                        #for g in v[1]:
                        #    groups += g + " "
                        #print(f"\tpos {glyph_a} {glyph_b} @BNG_VEDIC_ALL' <${number_value_name} 0 0 0>;")
                        #print(f"\tpos {glyph_a} {glyph_b} @BNG_VEDIC_ALL' <-{key} 0 0 0>;")
                        substitution_code = f"\tpos {glyph_a} [{group}] @BNG_VEDIC_ALL' <${number_value_name} 0 0 0>;"
                        if substitution_code not in collected_data:
                            collected_data.append(substitution_code)
                        else:
                            print("Duplicated substitution rules!")
                    else:
                        glyph_b = v[1][0]
                        substitution_code = f"\tpos {glyph_a} {glyph_b} @BNG_VEDIC_ALL' <${number_value_name} 0 0 0>;"
                        if substitution_code not in collected_data:
                            collected_data.append(substitution_code)
                        else:
                            print("Duplicated substitution rules!")
                else:
                    glyph_b = v[1]
                    substitution_code = f"\tpos {glyph_a} {glyph_b} @BNG_VEDIC_ALL' <${number_value_name} 0 0 0>;"
                    if substitution_code not in collected_data:
                        collected_data.append(substitution_code)
                    else:
                        print("Duplicated substitution rules!")

    if collected_data:
        return collected_data
    else:
        return None

def collect_number_values(data):
    vals = {}
    if data:
        for k in collections.OrderedDict(sorted(data.items())):
            #print(k)
            for keys in data[k].items():
                #print(keys[0][1], k)
                vals[keys[0][1]] = k
    if vals:
        return vals

def update_number_values(font, user_data):
    """
    Update values in the glyphs source

    font.selectedFontMaster.numbers[user_data[g.name]] = deduct_half_width(l.width)
    """
    layer_name = font.selectedFontMaster.name
    for data in user_data:
        #print(data, user_data[data])
        if data not in font.selectedFontMaster.numbers:
            #print(data)
            font.selectedFontMaster.numbers[data] = user_data[data]
        else:
            font.selectedFontMaster.numbers[data] = user_data[data]

# -----------
# Run program
# -----------

num_vals_1 = collect_number_values(internal_database_1)
num_vals_2 = collect_number_values(internal_database_2)
mark_glyphs = " ".join(mark_glyphs_with_anchor)
vedic_marks = ["uni0951", "uni1CD0", "uni1CD2", "uni1CF5.stack", "uni1CF6.stack", "uni0952", "uni1CD5", "uni1CD6", "uni1CD8", "uni1CED"]
mark_class_name = "@BNG_VEDIC_ALL"

print(internal_database_1)

#print("abvm;")
#print("# Automatic Code End")
#print(f"{mark_class_name} = [" + " ".join(vedic_marks) + "];")
#lookup_labels(internal_database_1, lookup_flag=("UseMarkFilteringSet", f"{mark_class_name}"), lookup_name_prefix="BNG_dflt_", feature_tag="abvm_", lookup_name_desc="vedic_mark_shift_1")
#lookup_labels(internal_database_2, lookup_flag=("UseMarkFilteringSet", f"[{mark_class_name} {mark_glyphs}]"), lookup_name_prefix="BNG_dflt_", feature_tag="abvm_", lookup_name_desc="vedic_mark_shift_2")

#update_number_values(this_font, num_vals_1)
#update_number_values(this_font, num_vals_2)
