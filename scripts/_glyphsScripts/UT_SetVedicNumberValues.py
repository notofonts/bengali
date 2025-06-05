#MenuTitle: UT-NotoBengali: Set vedic number values.
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
__doc__="""
Sets number values automatically in masters.
"""
Glyphs.clearLog()

this_font = Glyphs.font

test_value = {
    # Value Number Label: ((<comp-glyph-1>, <comp-glyph-2>), <ref-glyph>)
    "VEDIC_kTa": [("t_ta-beng", "headline-beng.200"), "k_ta-beng"],
    "VEDIC_nnHalf": [("nn-beng.half", "ddha-beng.side"), "nn_ddha-beng"],
    "VEDIC_kRa": [("t_ra-beng", "headline-beng.200"), "k_ra-beng"],
    "VEDIC_ddHalf": [("dd-beng.half", "headline-beng.200"), "dd_ba-beng"],
    "VEDIC_dHalf3": [("d-beng.half3", "headline-beng.130"), "d_dh_wa-beng"],
    "VEDIC_dHalf4": [("d-beng.half4", "gha-beng"), "d_gha-beng"],
    "VEDIC_nHeadline": [("n-beng.headline", "ddha-beng.side"), "n_tta-beng"],
    "VEDIC_ddhaSide": [("p-beng.half3", "ddha-beng.side"), "p_ddha-beng"],
    "VEDIC_dhHalf": [("dh-beng.half", "ma-beng.side3"), "dh_ma-beng"],
    "VEDIC_nDda": [("n-beng.headline", "dda-beng.side"), "n_dda-beng"],
    "VEDIC_mBa": [("m-beng.half", "headline-beng.200"), "m_ba-beng"],
    "VEDIC_mSa": [("m-beng.half", "sa-beng"), "m_sa-beng"],
    "VEDIC_sKRa": [("s-beng.half2", ""), "s_k_ra-beng"],
    "VEDIC_ssBa": [("ss-beng.half4", ""), "ss_ba-beng"],
    # testing:
    "VEDIC_lGa": [("l-beng.half3", "aaMatra-beng.part2"), "l_ga-beng"],
    "VEDIC_sPa": [("s-beng.half", "pa-beng"), "s_pa-beng"],
    "VEDIC_mPa": [("m-beng.half", "pa-beng"), "m_pa-beng"],
    "VEDIC_ssPa": [("ss-beng.half4", "pa-beng"), "ss_pa-beng"]
}

vedic_value_info = {
"g-beng.half": "VEDIC_gHalf",
"g-beng.half2": "VEDIC_gHalf2",
"ng-beng.half": "VEDIC_ng",
"ng-beng.half2": "VEDIC_ngHalf2",
"c-beng.half": "VEDIC_cHalf",
"j-beng.half": "VEDIC_jHalf",
"dd-beng.half1": "VEDIC_ddHalf1",
"ddh-beng.half": "VEDIC_ddhHalf",
"nn-beng.half3": "VEDIC_nnHalf3",
"t-beng.half": "VEDIC_tHalf",
"th-beng.half": "VEDIC_thHalf",
"d-beng.half": "VEDIC_dHalf",
"d-beng.half2": "VEDIC_dHalf2",
"n-beng.headline": "VEDIC_nHeadline",
"n_s-beng.half": "VEDIC_nSHalf",
"n_k_ta-beng": "VEDIC_nKTa",
"p-beng.half": "VEDIC_pHalf",
"p-beng.half3": "VEDIC_pHalf3",
"b-beng.half": "VEDIC_bHalf",
"b-beng.half2": "VEDIC_bHalf2",
"bh-beng.half": "VEDIC_bhHalf",
"m-beng.half": "VEDIC_mHalf",
"ra-beng": "VEDIC_ra",
"l-beng.half3": "VEDIC_lHalf3",
"sh-beng.half": "VEDIC_shHalf",
"sh-beng.half2": "VEDIC_shHalf2",
"ss-beng.half3": "VEDIC_ssHalf3",
"ss-beng.half4": "VEDIC_ssHalf4",
"s-beng.half": "VEDIC_sHalf",
"s-beng.half4": "VEDIC_sHalf4",
"s-beng.half2": "VEDIC_sHalf2",
"ramiddlediagonal-beng": "VEDIC_ramiddlediagonal",
"s_ka-beng": "VEDIC_sKa",
"s_ba-beng": "VEDIC_sBa",
"n_da-beng": "VEDIC_nDa",
"n_dha-beng": "VEDIC_nDha",
"n_ma-beng": "VEDIC_nMa",
"b_dha-beng": "VEDIC_bDha",
"bh_ra_uuMatra-beng": "VEDIC_bhRUu",
"l_ka-beng": "VEDIC_lKa",
"l_ma-beng": "VEDIC_lMa",
"ss_ka-beng": "VEDIC_ssKa",
"s_k_ra-beng": "VEDIC_sKRa",
"s_ra_uMatra-beng": "VEDIC_sRU",
"ha_rVocalicMatra-beng": "VEDIC_hRvoc",
"h_na-beng": "VEDIC_hNa",
"ddh-beng.side": "VEDIC_ddhaHalfSide"
}


def test_user_data(font, data):
    """
    Test if glyph names in user data are the active master.
    """
    print("Testing user glyph data against active master...")
    collection = [g.name for g in data if g not in font.glyphs]
    if len(collection) > 0:
        for names in collection:
            print(names)
    else:
        print("...No errors found!")

def deduct_half_width(value):
    """
       1. Find width of the base glyph and divide it by half: width / 2
       2. Return a negative value
    """
    if value != 0:
        new_value = int(-value/2)
        return new_value

def subtract_values(value_1, value_2, reference_glyph):
    """
    Calculate the true width of an on-the-fly combination
    """
    result = value_1 - value_2
    if result == reference_glyph.width:
        return result
    else:
        return None

def update_vedic_values(font, user_data, anchor_name="top_vedic"):
    """docstring for output_number_values"""
    layer_name = font.selectedFontMaster.name
    for i, k in enumerate(user_data):
        #print(user_data[k])
        vals = user_data[k]
        if len(vals) > 1:
            ref_glyph = vals[1]
            ref_glyph_width = int(font[ref_glyph].layers[layer_name].width)
            base_glyph = ""
            if vals[0][1] != "":
                base_glyph = vals[0][1]
                base_anchor_position = int(font[base_glyph].layers[layer_name].anchors[anchor_name].x)
                base_glyph_width = int(font[base_glyph].layers[layer_name].width)
                #print(base_glyph_width, base_anchor_position, ref_glyph_width, ref_glyph_width/2)
                new_value = -(int(ref_glyph_width/2) - (base_glyph_width - base_anchor_position))
                print(f"{k}: {new_value}")
                #print(f"BASE: {base_glyph} Anchor Pos. X: {base_anchor_position}\n\tRef. BASE: {ref_glyph} Ref. BASE width: {ref_glyph_width}\n\tRef. BASE half width: {int(ref_glyph_width/2)} Difference: {new_value}")
                #font.selectedFontMaster.numbers[k] = new_value
                
            else:
                base_glyph = vals[0][0]
                base_anchor_position = int(font[base_glyph].layers[layer_name].anchors[anchor_name].x)
                if int(ref_glyph_width/2) > base_anchor_position:
                    new_value = int(ref_glyph_width/2) - base_anchor_position
                    #new_value = base_anchor_position + difference
                    print(f"{k}: {new_value}")
                    #print(f"BASE: {base_glyph} Anchor Pos. X: {base_anchor_position}\n\tRef. BASE: {ref_glyph} Ref. BASE width: {ref_glyph_width}\n\tRef. BASE half width: {int(ref_glyph_width/2)} Difference: {new_value}")
                    #font.selectedFontMaster.numbers[k] = new_value
                else:
                    new_value = -(base_anchor_position - int(ref_glyph_width/2))
                    print(f"{k}: {new_value}")
                    #print(f"BASE: {base_glyph} Anchor Pos. X: {base_anchor_position}\n\tRef. BASE: {ref_glyph} Ref. BASE width: {ref_glyph_width}\n\tRef. BASE half width: {int(ref_glyph_width/2)} Difference: {new_value}")
                    #font.selectedFontMaster.numbers[k] = new_value

def update_number_values(font, user_data):
    """Update values in the glyphs source"""
    layer_name = font.selectedFontMaster.name
    for g in font.glyphs:
        for l in g.layers:
            if l.name == layer_name:
                # Need to also add a check to make sure that the number value 
                # labels are valid.
                if g.name in user_data:
                    font.selectedFontMaster.numbers[user_data[g.name]] = deduct_half_width(l.width)
                    
# -----
# TESTS
# -----

# Test to ensure that the data in the dictionary is valid. If there
# are issues in the glyphs list, it'll output invalid glyph names.

#test_user_data(this_font, test_value)

# To preview data as text output uncomment lines 134

vedic_data = update_vedic_values(this_font, test_value)
#print(vedic_data)

# -------------
# Apply changes
# -------------

#update_number_values(this_font, vedic_value_info)
