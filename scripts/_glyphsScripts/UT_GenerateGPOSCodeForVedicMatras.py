#MenuTitle: UT-NotoBengali: Generate GPOS code for Vedic matras.
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
from math import ceil
import collections
__doc__="""
For selected set of 'composed', non-exporting glyphs in the Noto Sans Bengali source.
Evaluate their parts to determine anchor center positions and output feature code.
"""
Glyphs.clearLog()

this_font = Glyphs.font

def get_base_anchor_position(reference_base, anchor_name):
    """
    Get the x position of the anchor from the base glyph layer
    """
    anchor_position = 0
    if reference_base.anchors[anchor_name]:
        anchor_position = int(reference_base.anchors[anchor_name].x)
    return anchor_position

def compile_values(ref_width, base_position, glyph_a, glyph_b, ref_glyph, class_label="VEDIC_", mark_class=None):
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
        value = (adjustment_value, glyph_a, glyph_b, f"{class_label}{ref_glyph.name.split('-')[0]}", mark_class)
        #database[selected_glyph.name] = dictionary_value
        #print(selected_glyph.name, dictionary_value)
    if value:
        return value

def _compile_values(ref_width, base_position, glyph_a, glyph_b, ref_glyph, class_label="VEDIC_", mark_class=None):
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
        value = (adjustment_value, glyph_a, [glyph_b], f"{class_label}{ref_glyph.name.split('-')[0]}", mark_class)
        #database[selected_glyph.name] = dictionary_value
        #print(selected_glyph.name, dictionary_value)
    if value:
        return value

def check_coverage(data, glyph_selection, count_a, count_b):
    """
    Check if all selected glyphs have been represented in the processing
    """
    output = ""
    if count_a != count_b:
        print(f"Total selected: {count_a}\nTotal processed: {count_b}")
        for glyphs in glyph_selection:
            if glyphs not in data:
                output += glyphs + "\n"
            else:
                pass
    else:
        pass
    if output != "":
        print("\nGlyphs not processed:")
        print(output)
    else:
        print("All selected glyphs processed successfully!")

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
    value_check = []
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
                            check_val = (dictionary_value[0], dictionary_value[1], dictionary_value[2])
                            if check_val not in value_check:
                                value_check.append(check_val)
                                database[selected_glyph.name] = dictionary_value
                            #print(selected_glyph.name, dictionary_value)
                    else:
                        base_anchor_pos_x = get_base_anchor_position(shape_b_parent.layers[layer_name], anchor_label)
                        dictionary_value = compile_values(reference_glyph_width_center, base_anchor_pos_x, shape_a.name, shape_b.name, selected_glyph, class_label="VEDIC_")
                        if len(dictionary_value) > 0:
                            check_val = (dictionary_value[0], dictionary_value[1], dictionary_value[2])
                            if check_val not in value_check:
                                value_check.append(check_val)
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
                        dictionary_value = compile_values(reference_glyph_width_center, base_anchor_pos_x, shape_a.name, shape_b.name, selected_glyph, class_label="VEDIC_", mark_class=mark_glyphs)
                        if len(dictionary_value) > 0:
                            check_val = (dictionary_value[0], dictionary_value[1], dictionary_value[2])
                            if check_val not in value_check:
                                value_check.append(check_val)
                                database[selected_glyph.name] = dictionary_value
                    else:
                        # Check if the remaining components have a BASE glyph
                        # with the target anchor
                        # -----
                        if len(glyph_layer.shapes[1:-1]) == 1:
                            base = glyph_layer.shapes[1:-1][0]
                            base_anchor_pos_x = get_base_anchor_position(font[base.name].layers[layer_name], anchor_label)
                            dictionary_value = compile_values(reference_glyph_width_center, base_anchor_pos_x, shape_a.name, base.name, selected_glyph, class_label="VEDIC_")
                            if len(dictionary_value) > 0:
                                check_val = (dictionary_value[0], dictionary_value[1], dictionary_value[2])
                                if check_val not in value_check:
                                    value_check.append(check_val)
                                    database[selected_glyph.name] = dictionary_value
                                #print(selected_glyph.name, dictionary_value)
                        else:
                            count = len(glyph_layer.shapes[1:-1]) - 1
                            while count >= 0:
                                base = glyph_layer.shapes[1:-1][count]
                                # Check from the back if any of the components have
                                # a BASE or MARK glyph with the target anchor
                                # -----
                                if font[base.name].layers[layer_name].anchors[anchor_label] != None:
                                    base_anchor_pos_x = get_base_anchor_position(font[base.name].layers[layer_name], anchor_label)
                                    dictionary_value = compile_values(reference_glyph_width_center, base_anchor_pos_x, shape_a.name, base.name, selected_glyph, class_label="VEDIC_")
                                    if len(dictionary_value) > 0:
                                        check_val = (dictionary_value[0], dictionary_value[1], dictionary_value[2])
                                        if check_val not in value_check:
                                            value_check.append(check_val)
                                            database[selected_glyph.name] = dictionary_value
                                        #print(selected_glyph.name, dictionary_value)
                                    break
                                else:
                                    pass
                                count -= 1
            elif len(glyph_layer.shapes) == 2:
                shape_a = glyph_layer.shapes[0] # Component object at index 0
                shape_a_parent = font[shape_a.name] # Selected layer object of the shape_a component
                shape_b = glyph_layer.shapes[-1] # Component object at index -1
                shape_b_parent = font[shape_b.name] # Selected layer object of the shape_b component
                # Check if the 1st and last component in the shape order
                # are BASE (spacing) glyphs
                # -----
                if shape_a_parent.category == "Letter" and shape_b_parent.category == "Letter":
                    base_anchor_pos_x = get_base_anchor_position(shape_b_parent.layers[layer_name], anchor_label)
                    dictionary_value = compile_values(reference_glyph_width_center, base_anchor_pos_x, shape_a.name, shape_b.name, selected_glyph, class_label="VEDIC_")
                    if len(dictionary_value) > 0:
                        check_val = (dictionary_value[0], dictionary_value[1], dictionary_value[2])
                        if check_val not in value_check:
                            value_check.append(check_val)
                            database[selected_glyph.name] = dictionary_value
                        #print(selected_glyph.name, dictionary_value)
    #print(value_check)
    return (database, len(total_selected), len(database), total_selected)

def output_sorted_collection(data):
    """
    Compress data to match 
    """
    lookup_data_a = {}
    lookup_data_b = {}
    # If the source data exists, apply the function
    # -----
    data_count = 0
    process_count = 0
    if data:
        data_count = len(data.keys())
        for k in data:
            # Check the GDEF type of the final BASE by checking
            # if the tuple in the data values includes a list
            # of mark glyphs.
            # -----
            if len(data[k]) == 5 and data[k][-1] == None:
                number_value = data[k][0]
                base_pos_1 = data[k][1]
                base_pos_2 = data[k][2]
                label_name = data[k][3]
                key = number_value
                value = (base_pos_2, label_name)
                # If the offset value is not in the dictionary add it 
                # with the corresponding substitution context data.
                # -----
                if key not in lookup_data_a:
                    process_count += 1
                    #print("Novel", key, base_pos_1, value)
                    lookup_data_a[key] = {base_pos_1: value}
                else:
                    # If the offset value IS in the dictionary and the 
                    # 1st input base IS in the dictionary, add the 2nd
                    # input base to the existing list.
                    # -----
                    if key in lookup_data_a and base_pos_1 in lookup_data_a[key]:
                        process_count += 1
                        #print("Repeat 1", key, base_pos_1, value)
                        lookup_data_a[key][base_pos_1][0].append(base_pos_2[0])
                    # If the offset value IS in the dictionary but the 
                    # 1st input base is not the same, add a new key:value
                    # pair to the 2nd level dictionary.
                    # -----
                    elif key in lookup_data_a and base_pos_1 not in lookup_data_a[key]:
                        process_count += 1
                        #print("Repeat 2", key, base_pos_1, value)
                        lookup_data_a[key][base_pos_1] = value
                    else:
                        pass
                        #print("Repeat 3", key, base_pos_1, value)
            else:
                mark_class = data[k][4]
                # Adds a key:value pair containing a reference glyph class
                # for the substitution contexts
                # -----
                lookup_data_b["glyphClass"] = mark_class
                number_value = data[k][0]
                base_pos_1 = data[k][1]
                base_pos_2 = data[k][2]
                label_name = data[k][3]
                key = number_value
                value = (base_pos_2, label_name)
                if key not in lookup_data_b:
                    process_count += 1
                    #print("Novel", key, base_pos_1, value)
                    lookup_data_b[key] = {base_pos_1: value}
                else:
                    if key in lookup_data_b and base_pos_1 in lookup_data_b[key]:
                        process_count += 1
                        #print("Repeat 1", key, base_pos_1, value)
                        lookup_data_b[key][base_pos_1][0].append(base_pos_2[0])
                    elif key in lookup_data_b and base_pos_1 not in lookup_data_b[key]:
                        process_count += 1
                        #print("Repeat 2", key, base_pos_1, value)
                        lookup_data_b[key][base_pos_1] = value
                    else:
                        pass
                        #print("Repeat 3", key, base_pos_1, value)
    # Uncomment the below print function to debug this function
    # -----
    #print((data_count, process_count))
    if lookup_data_a == {} and lookup_data_b == {}:
        raise Exception("No data collected for lookups!")
    else:
        return (lookup_data_a, lookup_data_b)

def output_feature_code_collection(feature_data, mark_class="@BNG_VEDIC_ALL", lookup_flag="UseMarkFilteringSet"):
    collected_data = {}
    if feature_data == None:
        raise Exception("No feature code data defined!")
    else:
        if "glyphClass" not in feature_data:
            print(feature_data)
            if lookup_flag != None and mark_class != None:
                collected_data["lookupFlag"] = f"lookupflag {lookup_flag} {mark_class};"
                collected_data["positioningRules"] = []
                sorted_data = collections.OrderedDict(sorted(feature_data.items()))
                for key in sorted_data:
                    print(sorted_data[key])
                    for glyph_base_1, glyph_bases_2 in sorted_data[key].items():
                        number_value_name = glyph_bases_2[1]
                        consolidated_bases_2 = list( dict.fromkeys(glyph_bases_2[0]) )
                        context_class = ""
                        glyph_a = glyph_base_1
                        context_class = " ".join(consolidated_bases_2)
                        #print(f"\tpos {glyph_a} [{context_class}] @BNG_VEDIC_ALL' <${number_value_name} 0 0 0>;")
                        #print(f"\tpos {glyph_a} [{context_class}] @BNG_VEDIC_ALL' <{key} 0 0 0>;")
                        #substitution_code = f"\n\tpos {glyph_a} [{context_class}] {mark_class}' <${number_value_name} 0 0 0>;"
                        substitution_code = f"\n\tpos {glyph_a} [{context_class}] {mark_class}' <{key} 0 0 0>;"
                        if substitution_code not in collected_data["positioningRules"]:
                            collected_data["positioningRules"].append(substitution_code)
                        else:
                            print("Duplicated substitution rules!")
        else:
            new_collection = {}
            for key in feature_data:
                    if type(key) == int:
                        new_collection[key] = feature_data[key]
            skip_marks = " ".join(feature_data["glyphClass"])
            if lookup_flag != None and mark_class != None:
                collected_data["lookupFlag"] = f"lookupflag {lookup_flag} [{mark_class} {skip_marks}];"
                collected_data["positioningRules"] = []
            if new_collection:
                sorted_data = collections.OrderedDict(sorted(new_collection.items()))
                for key in sorted_data:
                    for glyph_base_1, glyph_bases_2 in sorted_data[key].items():
                        number_value_name = glyph_bases_2[1]
                        consolidated_bases_2 = list( dict.fromkeys(glyph_bases_2[0]) )
                        context_class = ""
                        glyph_a = glyph_base_1
                        context_class = " ".join(consolidated_bases_2)
                    #   print(f"\tpos {glyph_a} [{context_class}] @BNG_VEDIC_ALL' <${number_value_name} 0 0 0>;")
                    #   print(f"\tpos {glyph_a} [{context_class}] @BNG_VEDIC_ALL' <{key} 0 0 0>;")
                        #substitution_code = f"\n\tpos {glyph_a} [{context_class}] {mark_class}' <${number_value_name} 0 0 0>;"
                        substitution_code = f"\n\tpos {glyph_a} [{context_class}] {mark_class}' <{key} 0 0 0>;"
                        if substitution_code not in collected_data["positioningRules"]:
                            collected_data["positioningRules"].append(substitution_code)
                        else:
                            print("Duplicated substitution rules!")
    if collected_data:
        return collected_data
    else:
        return None

def lookup_labels(substitution_data, lookup_flag=("0", ""), lookup_name_prefix="BNG_dflt_", feature_tag="abvm_", lookup_name_desc="None"):
    subs = output_feature_code_collection(substitution_data)
    output = ""
    # Substitution data can have two keys: 'lookupFlag' &
    # 'positioningRules'. Query the data to find these keys
    # and format output.
    # -----
    if subs == None:
        raise Exception("Data object is empty!")
    else:
        output += f"lookup {lookup_name_prefix}{feature_tag}{lookup_name_desc}" + " {\n"
        if 'lookupFlag' in subs:
            output += f"{subs['lookupFlag']}"
        if 'positioningRules' in subs:
            for values in subs["positioningRules"]:
                #print(values)
                output += values
        output += "\n} " + f"{lookup_name_prefix}{feature_tag}{lookup_name_desc};"
    if output != "":
        print(output)
    else:
        raise Exception("No output collected")

def opentype_code(data, mark_class="@BNG_VEDIC_ALL", lookup_flag="UseMarkFilteringSet"):
    count = 1
    for key in data:
        if data[key][-1] != None:
            marks = " ".join(data[key][-1])
            print(f"lookup BNG_dflt_abvm_vedicMatraShift_{count}" + " {")
            print(f"lookupflag {lookup_flag} [{mark_class} {marks}];")
            #print(data[key])
            print(f"\tpos {data[key][1]} {data[key][2]} {mark_class}' <{data[key][0]} 0 0 0>;")
            print("} " + f"BNG_dflt_abvm_vedicMatraShift_{count};\n")
            count += 1
        else:
            print(f"lookup BNG_dflt_abvm_vedicMatraShift_{count}" + " {")
            print(f"lookupflag {lookup_flag} {mark_class};")
            #print(data[key])
            print(f"\tpos {data[key][1]} {data[key][2]} {mark_class}' <{data[key][0]} 0 0 0>;")
            print("} " + f"BNG_dflt_abvm_vedicMatraShift_{count};\n")
            count += 1

# -----------
# Run Program
# -----------

master_layer_name = this_font.selectedFontMaster.name
mark_class_name = "@BNG_VEDIC_ALL"
vedic_marks = ["uni0951", "uni1CD0", "uni1CD2", "uni1CF5.stack", "uni1CF6.stack", "uni0952", "uni1CD5", "uni1CD6", "uni1CD8", "uni1CED"]
mark_glyphs_with_anchor = ["headline-beng.130", "headline-beng.200", "headline-beng.250", "aaMatra-beng.float", "aaMatra-beng.side2", "ka-beng.arm", "ka-beng.arm1", "headline-beng.ba"]

dataset_1, selection_count_1, selection_count_2, all_selected = gather_data(this_font, mark_glyphs_with_anchor, anchor_label='top_vedic')

# Output feature code for selected master
# -----

print("# Automatic Code End\n")
print(f"# {master_layer_name}\n")
print(f"{mark_class_name} = [" + " ".join(vedic_marks) + "];\n")
opentype_code(dataset_1)
