#MenuTitle: UT-NotoBengali: Set vedic number values.
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
__doc__="""
Sets number values automatically in masters.
"""
Glyphs.clearLog()

this_font = Glyphs.font

vedic_value_info = {"g-beng.half": "VEDIC_gHalf",
"g-beng.half2": "VEDIC_gHalf2",
"ng-beng.half": "VEDIC_ng",
"ng-beng.half2": "VEDIC_ngHalf2",
"c-beng.half": "VEDIC_cHalf",
"j-beng.half": "VEDIC_jHalf",
"dd-beng.half1": "VEDIC_ddHalf1",
"dd-beng.half": "VEDIC_ddHalf",
"ddh-beng.half": "VEDIC_ddhHalf",
"nn-beng.half": "VEDIC_nnHalf",
"nn-beng.half3": "VEDIC_nnHalf3",
"t-beng.half": "VEDIC_tHalf",
"k_ta-beng": "VEDIC_kTa",
"t_ta-beng": "VEDIC_kTaHalf",
"k_ra-beng": "VEDIC_kRa",
"th-beng.half": "VEDIC_thHalf",
"d-beng.half": "VEDIC_dHalf",
"d-beng.half2": "VEDIC_dHalf2",
"d-beng.half3": "VEDIC_dHalf3",
"n-beng.headline": "VEDIC_nHeadline",
"d-beng.half4": "VEDIC_dHalf4",
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
"m_ba-beng": "VEDIC_mBa",
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
"ss_ba-beng": "VEDIC_ssBa",
"s_k_ra-beng": "VEDIC_sKRa",
"s_ra_uMatra-beng": "VEDIC_sRU",
"ha_rVocalicMatra-beng": "VEDIC_hRvoc",
"h_na-beng": "VEDIC_hNa",
"ddha-beng.side": "VEDIC_ddhaSide",
"ddh-beng.side": "VEDIC_ddhaHalfSide"
}


def test_user_data(font, data):
    """Test if glyph names in user data are the active master"""
    print("Testing user glyph data against active master...")
    collection = [g.name for g in data if g not in font.glyphs]
    if len(collection) > 0:
        return collection
    else:
        return None

def deduct_half_width(value):
    """
       1. Find width of the base glyph and divide it by half: width / 2
       2. Return a negative value
    """
    if value != 0:
        new_value = int(-value/2)
        return new_value

def output_vedic_values(font, user_data, layer_name):
    """docstring for output_number_values"""
    data = ""
    print("\nProcessing...\n")
    for f in font.glyphs:
        for l in f.layers:
            if l.name == layer_name:
                if l.parent.name in user_data:
                    #print("{")
                    data += "{\n"
                    #print("name= {};".format(user_data[l.parent.name]))
                    data += "name= {};\n".format(user_data[l.parent.name])
                    #print("value= {};".format(deduct_half_width(l.width)))
                    data += "value= {};\n".format(deduct_half_width(l.width))
                    #print("},")
                    data += "},\n"
    if data:
        return data

def output_kern_values(font, user_data, layer_name):
    """docstring for output_number_values"""
    data = ""
    print("\nProcessing...\n")
    for f in font.glyphs:
        for l in f.layers:
            if l.name == layer_name:
                if l.parent.name in user_data:
                    #print("{")
                    data += "{\n"
                    #print("name= {};".format(user_data[l.parent.name]))
                    data += "name= {};\n".format(user_data[l.parent.name])
                    #print("value= {};".format(deduct_half_width(l.width)))
                    data += "value= {};\n".format(deduct_half_width(l.width))
                    #print("},")
                    data += "},\n"
    if data:
        return data

def update_number_values(font, user_data):
    """Update values in the glyphs source"""
    layer_name = font.selectedFontMaster.name
    for g in font.glyphs:
        for l in g.layers:
            if l.name == layer_name:
                if g.name in user_data:
                    print(deduct_half_width(l.width), user_data[l.parent.name])
                    font.selectedFontMaster.numbers[user_data[l.parent.name]] = deduct_half_width(l.width)
                    
# -----
# TESTS
# -----
test_user_data(this_font, vedic_value_info)

# Vedic Data
# ----------
#vedic_data = output_vedic_values(this_font, number_value_info, "Thin")
#print(vedic_data)

# -------------
# Apply changes
# -------------
update_number_values(this_font, vedic_value_info)
