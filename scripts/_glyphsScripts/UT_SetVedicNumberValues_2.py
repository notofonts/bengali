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
                        pass
                    else:
                        new_value = int(ref_glyph_width_center - base_anchor_pos_x)
                        #print("Multi comp: last letter")
                        #print(g.name, ref_glyph_width_center)
                        #print(f"\t{first_comp.name}, {last_comp.name}, {new_value}")
                        data_struct = [(first_comp.name, last_comp.name), (g.name, f"VEDIC_{g.name.split('-')[0]}")]
                        #print(g.name, data_struct[0], new_value)
                        if new_value not in internal_database_1:
                            internal_database_1[new_value] = {data_struct[0]: data_struct[1]}
                        elif new_value in internal_database_1 and data_struct[0] not in internal_database_1[new_value]:
                            internal_database_1[new_value][data_struct[0]] = data_struct[1]
                        
                elif this_font[last_comp.name].layers[layer_name].components:
                    first_comp_glyph = this_font[last_comp.name].layers[layer_name].shapes[0]
                    if this_font[first_comp_glyph.name].layers[layer_name].anchors[anchors_name]:
                        base_anchor_pos_x = int(this_font[first_comp_glyph.name].layers[layer_name].anchors[anchors_name].x)
                        base_glyph_width = int(this_font[first_comp_glyph.name].layers[layer_name].width)
                        if ref_glyph_width_center == base_anchor_pos_x:
                            print(f"Multi; Remove from list: {g.name}")
                            pass
                        else:
                            new_value = int(ref_glyph_width_center - base_anchor_pos_x)
                            data_struct = [(first_comp.name, first_comp_glyph.name), (g.name, f"VEDIC_{g.name.split('-')[0]}")]
                            #print("! Multi comp: nested components")
                            #print(g.name, data_struct[0], new_value)
                            #base_anchor_pos_x = int(this_font[first_comp.name].layers[layer_name].anchors[anchors_name].x)
                            if new_value not in internal_database_1:
                                internal_database_1[new_value] = {data_struct[0]: data_struct[1]}
                            elif new_value in internal_database_1 and data_struct[0] not in internal_database_1[new_value]:
                                internal_database_1[new_value][data_struct[0]] = data_struct[1]


            elif this_font[first_comp.name].category == "Letter" and this_font[last_comp.name].category != "Letter":
                if last_comp.name in mark_glyphs_with_anchor:
                    base_anchor_pos_x = 0
                    if this_font[last_comp.name].layers[layer_name].anchors[anchors_name]:
                        base_anchor_pos_x = int(this_font[last_comp.name].layers[layer_name].anchors[anchors_name].x)
                        new_value = int(ref_glyph_width_center - base_anchor_pos_x)
                        #print("Multi comp: last mark")
                        #print(g.name, ref_glyph_width_center)
                        #print(f"\t{first_comp.name}, {last_comp.name}, {new_value}")
                        data_struct = [(first_comp.name, last_comp.name), (g.name, f"VEDIC_{g.name.split('-')[0]}")]
                        #print(g.name, data_struct[0], new_value)
                        if new_value not in internal_database_2:
                            internal_database_2[new_value] = {data_struct[0]: data_struct[1]}
                        elif new_value in internal_database_2 and data_struct[0] not in internal_database_2[new_value]:
                            internal_database_2[new_value][data_struct[0]] = data_struct[1]
                else:
                    for c in g.layers[layer_name].shapes[1:-1]:
                        if this_font[c.name].category == "Letter":
                            base_anchor_pos_x = 0
                            if this_font[c.name].layers[layer_name].anchors[anchors_name]:
                                base_anchor_pos_x = int(this_font[c.name].layers[layer_name].anchors[anchors_name].x)
                                base_glyph_width = int(this_font[c.name].layers[layer_name].width)
                                if ref_glyph_width_center == base_anchor_pos_x:
                                    print(f"Multi; Remove from list: {g.name}")
                                    pass
                                else:
                                    new_value = int(ref_glyph_width_center - base_anchor_pos_x)
                                    #print("Multi comp: last mark")
                                    #print(g.name, ref_glyph_width_center)
                                    #print(f"\t{first_comp.name}, {c.name}, {new_value}")
                                    data_struct = [(first_comp.name, c.name), (g.name, f"VEDIC_{g.name.split('-')[0]}")]
                                    #print(g.name, data_struct[0], c.name, new_value)
                                    if new_value not in internal_database_1:
                                        internal_database_1[new_value] = {data_struct[0]: data_struct[1]}
                                    elif new_value in internal_database_1 and data_struct[0] not in internal_database_1[new_value]:
                                        internal_database_1[new_value][data_struct[0]] = data_struct[1]
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
                        pass
                    else:
                        new_value = int(ref_glyph_width_center - base_anchor_pos_x)
                        #print("Single comp: 2 in 2")
                        #print(g.name, ref_glyph_width_center)
                        #print(f"\t{first_comp.name}, {last_comp.name}, {new_value}")
                        data_struct = [(first_comp.name, last_comp.name), (g.name, f"VEDIC_{g.name.split('-')[0]}")]
                        
                        if new_value not in internal_database_1:
                            internal_database_1[new_value] = {data_struct[0]: data_struct[1]}
                        elif new_value in internal_database_1 and data_struct[0] not in internal_database_1[new_value]:
                            internal_database_1[new_value][data_struct[0]] = data_struct[1]
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
        for key, val in sorted_data.items():
            if len(val) < 2:
                for k, v in val.items():
                    #print(k, v)
                    glyph_a = k[0]
                    glyph_b = k[1]
                    number_value_name = v[1]
                    #print(f"\tpos {glyph_a} {glyph_b} @BNG_VEDIC_ALL' <${number_value_name} 0 0 0>;")
                    #print(f"\tpos {glyph_a} {glyph_b} @BNG_VEDIC_ALL' <-{key} 0 0 0>;")
                    substitution_code = f"\tpos {glyph_a} {glyph_b} @BNG_VEDIC_ALL' <${number_value_name} 0 0 0>;"
                    if substitution_code not in collected_data:
                        collected_data.append(substitution_code)
                    else:
                        print("Duplicated substitution rules!")
                    
            else:
                for k, v in val.items():
                    #print(k, v)
                    glyph_a = k[0]
                    glyph_b = k[1]
                    number_value_name = v[1]
                    #print(f"\tpos {glyph_a} {glyph_b} @BNG_VEDIC_ALL' <${number_value_name} 0 0 0>;")
                    #print(f"\tpos {glyph_a} {glyph_b} @BNG_VEDIC_ALL' <-{key} 0 0 0>;")
                    substitution_code = f"\tpos {glyph_a} {glyph_b} @BNG_VEDIC_ALL' <${number_value_name} 0 0 0>;"
                    if substitution_code not in collected_data:
                        collected_data.append(substitution_code)
                    else:
                        print("Duplicated substitution rules!")
    
    if collected_data:
        return collected_data
    else:
        return None

lookup_labels(internal_database_1, lookup_flag=("UseMarkFilteringSet", "@BNG_VEDIC_ALL"), lookup_name_prefix="BNG_dflt_", feature_tag="abvm_", lookup_name_desc="vedic_mark_shift_1")
lookup_labels(internal_database_2, lookup_flag=("UseMarkFilteringSet", "[@BNG_VEDIC_ALL ]"), lookup_name_prefix="BNG_dflt_", feature_tag="abvm_", lookup_name_desc="vedic_mark_shift_2")

#output_feature_code(internal_database_2, )

#"vedic_mark_shift_2"
