#MenuTitle: [UT] Rename Glyphs from DataBase
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
from bangla_glyph_names import glyph_names as name_dict
__doc__="""
Does what it says on the tin!

The script takes a dictionary of before/after glyph-names and renames glyphs if they're found in the font.

TODO:

- Update prefixes
- Update classes
- Update features
- [DONE] Update glyphOrder

"""
Glyphs.clearLog()

this_font = Glyphs.font

def renameGlyphs(font, data):
    """docstring for renameGlyphs"""
    for names in data:
        if names in font.glyphs:
            font.glyphs[names].name = data[names]
        else:
            print("Glyph \'{}\' not found in source!".format(names))

def updateGlyphOrder(font, data):
    if font.customParameters["glyphOrder"]:
        for names in data.keys():
            if names in font.customParameters["glyphOrder"]:
#                print(font.glyphOrder().index(n))
                glyph_index = font.customParameters["glyphOrder"].index(names)
                font.customParameters["glyphOrder"][glyph_index] = data[names]

# update prefixes
#if len(this_font.featurePrefixes) > 1:
#    # Do stuff
#    print(this_font.featurePrefixes)
#else:
#    pass

# update classes
#if len(this_font.classes) > 0:
#    # Do stuff
#    print(this_font.classes)
#else:
#    pass

# update features


#if len(this_font.features) > 0:
#    # Do stuff
#    print(this_font.features[0].code)
#else:
#    pass

this_font.disableUpdateInterface()
glyph_name_data = name_dict
renameGlyphs(this_font, glyph_name_data)
updateGlyphOrder(this_font, glyph_name_data)
this_font.enableUpdateInterface()
