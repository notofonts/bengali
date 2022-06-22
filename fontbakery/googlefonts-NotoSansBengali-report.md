## Fontbakery report

Fontbakery version: 0.8.9

<details><summary><b>[4] Family checks</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking all files are in the same directory. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/single_directory">com.google.fonts/check/family/single_directory</a>)</summary><div>


* 🔥 **FAIL** Not all fonts passed in the command line are in the same directory. This may lead to bad results as the tool will interpret all font files as belonging to a single font family. The detected directories are: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf', 'fonts/NotoSansBengali/googlefonts/ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf'] [code: single-directory]
</div></details><details><summary>🔥 <b>FAIL:</b> Each font in a family must have the same set of vertical metrics values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/vertical_metrics">com.google.fonts/check/family/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** sTypoAscender is not the same across the family:
Noto Sans Bengali Regular: 917
Noto Sans Bengali Black: 917
Noto Sans Bengali Bold: 917
Noto Sans Bengali ExtraBold: 917
Noto Sans Bengali ExtraLight: 917
Noto Sans Bengali Light: 917
Noto Sans Bengali Medium: 917
Noto Sans Bengali SemiBold: 917
Noto Sans Bengali Thin: 917
Noto Sans Bengali UI Black: 1069
Noto Sans Bengali UI Bold: 1069
Noto Sans Bengali UI ExtraBold: 1069
Noto Sans Bengali UI ExtraLight: 1069
Noto Sans Bengali UI Light: 1069
Noto Sans Bengali UI Medium: 1069
Noto Sans Bengali UI Regular: 1069
Noto Sans Bengali UI SemiBold: 1069
Noto Sans Bengali UI Thin: 1069 [code: sTypoAscender-mismatch]
* 🔥 **FAIL** sTypoDescender is not the same across the family:
Noto Sans Bengali Regular: -408
Noto Sans Bengali Black: -408
Noto Sans Bengali Bold: -408
Noto Sans Bengali ExtraBold: -408
Noto Sans Bengali ExtraLight: -408
Noto Sans Bengali Light: -408
Noto Sans Bengali Medium: -408
Noto Sans Bengali SemiBold: -408
Noto Sans Bengali Thin: -408
Noto Sans Bengali UI Black: -293
Noto Sans Bengali UI Bold: -293
Noto Sans Bengali UI ExtraBold: -293
Noto Sans Bengali UI ExtraLight: -293
Noto Sans Bengali UI Light: -293
Noto Sans Bengali UI Medium: -293
Noto Sans Bengali UI Regular: -293
Noto Sans Bengali UI SemiBold: -293
Noto Sans Bengali UI Thin: -293 [code: sTypoDescender-mismatch]
* 🔥 **FAIL** usWinAscent is not the same across the family:
Noto Sans Bengali Regular: 917
Noto Sans Bengali Black: 917
Noto Sans Bengali Bold: 917
Noto Sans Bengali ExtraBold: 917
Noto Sans Bengali ExtraLight: 917
Noto Sans Bengali Light: 917
Noto Sans Bengali Medium: 917
Noto Sans Bengali SemiBold: 917
Noto Sans Bengali Thin: 917
Noto Sans Bengali UI Black: 1069
Noto Sans Bengali UI Bold: 1069
Noto Sans Bengali UI ExtraBold: 1069
Noto Sans Bengali UI ExtraLight: 1069
Noto Sans Bengali UI Light: 1069
Noto Sans Bengali UI Medium: 1069
Noto Sans Bengali UI Regular: 1069
Noto Sans Bengali UI SemiBold: 1069
Noto Sans Bengali UI Thin: 1069 [code: usWinAscent-mismatch]
* 🔥 **FAIL** usWinDescent is not the same across the family:
Noto Sans Bengali Regular: 408
Noto Sans Bengali Black: 408
Noto Sans Bengali Bold: 408
Noto Sans Bengali ExtraBold: 408
Noto Sans Bengali ExtraLight: 408
Noto Sans Bengali Light: 408
Noto Sans Bengali Medium: 408
Noto Sans Bengali SemiBold: 408
Noto Sans Bengali Thin: 408
Noto Sans Bengali UI Black: 293
Noto Sans Bengali UI Bold: 293
Noto Sans Bengali UI ExtraBold: 293
Noto Sans Bengali UI ExtraLight: 293
Noto Sans Bengali UI Light: 293
Noto Sans Bengali UI Medium: 293
Noto Sans Bengali UI Regular: 293
Noto Sans Bengali UI SemiBold: 293
Noto Sans Bengali UI Thin: 293 [code: usWinDescent-mismatch]
* 🔥 **FAIL** ascent is not the same across the family:
Noto Sans Bengali Regular: 917
Noto Sans Bengali Black: 917
Noto Sans Bengali Bold: 917
Noto Sans Bengali ExtraBold: 917
Noto Sans Bengali ExtraLight: 917
Noto Sans Bengali Light: 917
Noto Sans Bengali Medium: 917
Noto Sans Bengali SemiBold: 917
Noto Sans Bengali Thin: 917
Noto Sans Bengali UI Black: 1069
Noto Sans Bengali UI Bold: 1069
Noto Sans Bengali UI ExtraBold: 1069
Noto Sans Bengali UI ExtraLight: 1069
Noto Sans Bengali UI Light: 1069
Noto Sans Bengali UI Medium: 1069
Noto Sans Bengali UI Regular: 1069
Noto Sans Bengali UI SemiBold: 1069
Noto Sans Bengali UI Thin: 1069 [code: ascent-mismatch]
* 🔥 **FAIL** descent is not the same across the family:
Noto Sans Bengali Regular: -408
Noto Sans Bengali Black: -408
Noto Sans Bengali Bold: -408
Noto Sans Bengali ExtraBold: -408
Noto Sans Bengali ExtraLight: -408
Noto Sans Bengali Light: -408
Noto Sans Bengali Medium: -408
Noto Sans Bengali SemiBold: -408
Noto Sans Bengali Thin: -408
Noto Sans Bengali UI Black: -293
Noto Sans Bengali UI Bold: -293
Noto Sans Bengali UI ExtraBold: -293
Noto Sans Bengali UI ExtraLight: -293
Noto Sans Bengali UI Light: -293
Noto Sans Bengali UI Medium: -293
Noto Sans Bengali UI Regular: -293
Noto Sans Bengali UI SemiBold: -293
Noto Sans Bengali UI Thin: -293 [code: descent-mismatch]
</div></details><details><summary>🔥 <b>FAIL:</b> Fonts have consistent PANOSE proportion? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/family/panose_proportion">com.google.fonts/check/family/panose_proportion</a>)</summary><div>


* 🔥 **FAIL** PANOSE proportion is not the same across this family. In order to fix this, please make sure that the panose.bProportion value is the same in the OS/2 table of all of this family font files. [code: inconsistency]
</div></details><details><summary>🔥 <b>FAIL:</b> Fonts have consistent PANOSE family type? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/family/panose_familytype">com.google.fonts/check/family/panose_familytype</a>)</summary><div>


* 🔥 **FAIL** PANOSE family type is not the same across this family. In order to fix this, please make sure that the panose.bFamilyType value is the same in the OS/2 table of all of this family font files. [code: inconsistency]
</div></details><br></div></details><details><summary><b>[17] NotoSansBengali[wght].ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** The file 'NotoSansBengali[wght].ttf' must be renamed to 'NotoSansBengali[wdth,wght].ttf' according to the Google Fonts naming policy for variable fonts. [code: bad-varfont-filename]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x00AF (MACRON)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp">com.google.fonts/check/gasp</a>)</summary><div>


* 🔥 **FAIL** Font is missing the 'gasp' table. Try exporting the font with autohinting enabled.
If you are dealing with an unhinted font, it can be fixed by running the fonts through the command 'gftools fix-nonhinting'
GFTools is available at https://pypi.org/project/gftools/ [code: lacks-gasp]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> Font enables smart dropout control in "prep" table instructions? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/smart_dropout">com.google.fonts/check/smart_dropout</a>)</summary><div>


* 🔥 **FAIL** The 'prep' table does not contain TrueType instructions enabling smart dropout control. To fix, export the font with autohinting enabled, or run ttfautohint on the font, or run the `gftools fix-nonhinting` script. [code: lacks-smart-dropout]
</div></details><details><summary>🔥 <b>FAIL:</b> Check variable font instances don't have duplicate names (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_duplicate_instance_names">com.google.fonts/check/varfont_duplicate_instance_names</a>)</summary><div>


* 🔥 **FAIL** Following instances names are duplicate: 
	- ExtraLight
	- Light
	- Regular
	- Medium
	- SemiBold
	- Bold
 [code: duplicate-instance-names]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 995, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CED

	- uuvowelsignbeng

	- rrvocalicvowelsignbeng

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD5

	- uni1CD6

	- uni1CD8

	- uni0952 

	- And 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>🔥 <b>FAIL:</b> Validates that when an instance record is included for the default instance, its subfamilyNameID value is set to either 2 or 17, and its postScriptNameID value is set to 6. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/valid_default_instance_nameids">com.adobe.fonts/check/varfont/valid_default_instance_nameids</a>)</summary><div>


* 🔥 **FAIL** 'Regular' instance has the same coordinates as the default instance; its subfamilyNameID should be either 2 or 17, instead of 261. [code: invalid-default-instance-subfamily-nameid:261]
* 🔥 **FAIL** 'Regular' instance has the same coordinates as the default instance; its postScriptNameID should be 6, instead of 270. [code: invalid-default-instance-postscript-nameid:270]
* 🔥 **FAIL** 'Regular' instance has the same coordinates as the default instance; its subfamilyNameID should be either 2 or 17, instead of 261. [code: invalid-default-instance-subfamily-nameid:261]
* 🔥 **FAIL** 'Regular' instance has the same coordinates as the default instance; its postScriptNameID should be 6, instead of 279. [code: invalid-default-instance-postscript-nameid:279]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- ra1nuktahalfbeng

	- dhahalfbeng

	- uuvowelsignvattuUIbeng

	- dhanuktahalfbeng

	- one

	- kanuktahalfbeng

	- canuktahalfbeng

	- shanuktahalfbeng

	- asciitilde

	- phanuktahalfbeng 

	- And 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1), uni1CE1.UI (unencoded) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 acutecomb (U+0301), gravecomb (U+0300), tildecomb (U+0303), uni0302 (U+0302), uni0304 (U+0304), uni0306 (U+0306), uni0307 (U+0307), uni0308 (U+0308), uni030A (U+030A), uni030B (U+030B) and 5 more.

Use -F or --full-lists to disable shortening of long lists. [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><br></div></details><details><summary><b>[18] NotoSansBengali-Black.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali Black [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 995, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CED

	- uuvowelsignbeng

	- rrvocalicvowelsignbeng

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD5

	- uni1CD6

	- uni1CD8

	- uni0952 

	- And 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* tathabeng
	* shabeng
	* sharabeng
	* gadhabeng
	* ngakarabeng
	* ttarabeng
	* kababeng
	* nadabeng
	* dadhabeng
	* babhabeng and 411 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali Black' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dhanuktahalfbeng

	- kanuktahalfbeng

	- canuktahalfbeng 

	- And 22 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 717 but it should be 776 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* bracketleft.beng (U+005B): X=283.0,Y=-1.0 (should be at baseline 0?)

	* bracketleft.beng (U+005B): X=380.0,Y=-1.0 (should be at baseline 0?)

	* bracketright.beng (U+005D): X=71.0,Y=-1.0 (should be at baseline 0?)

	* bracketright.beng (U+005D): X=168.0,Y=-1.0 (should be at baseline 0?)

	* braceright.beng (U+007D): X=322.0,Y=624.0 (should be at cap-height 622?)

	* uni0951 (U+0951): X=-200.0,Y=623.0 (should be at cap-height 622?)

	* uni0951 (U+0951): X=-310.0,Y=623.0 (should be at cap-height 622?)

	* ibeng (U+0987): X=0.0,Y=915.0 (should be at ascender 917?)

	* iibeng (U+0988): X=44.0,Y=915.0 (should be at ascender 917?)

	* ubeng (U+0989): X=74.0,Y=915.0 (should be at ascender 917?) 

	* And 19 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* aabeng (U+0986): B<<1058.5,609.0>-<1078.0,596.0>-<1089.0,566.0>>/B<<1089.0,566.0>-<1087.0,580.0>-<1086.0,598.5>> = 12.006201074092134

	* aavowelsignbeng (U+09BE): B<<48.5,609.0>-<68.0,596.0>-<79.0,566.0>>/B<<79.0,566.0>-<77.0,580.0>-<76.0,598.5>> = 12.006201074092134 

	* And ovowelsignbeng (U+09CB): B<<740.5,609.0>-<760.0,596.0>-<771.0,566.0>>/B<<771.0,566.0>-<769.0,580.0>-<768.0,598.5>> = 12.006201074092134 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[17] NotoSansBengali-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 995, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CED

	- uuvowelsignbeng

	- rrvocalicvowelsignbeng

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD5

	- uni1CD6

	- uni1CD8

	- uni0952 

	- And 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* shabeng
	* sharabeng
	* gadhabeng
	* ngakarabeng
	* ttarabeng
	* kababeng
	* nadabeng
	* dadhabeng
	* babhabeng
	* jhahalfbeng and 367 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dhanuktahalfbeng

	- kanuktahalfbeng

	- canuktahalfbeng 

	- And 22 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 687 but it should be 740 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* five.beng (U+0035): X=127.0,Y=-0.5 (should be at baseline 0?)

	* uni0951 (U+0951): X=-205.0,Y=623.0 (should be at cap-height 622?)

	* uni0951 (U+0951): X=-305.0,Y=623.0 (should be at cap-height 622?)

	* uni0980 (U+0980): X=445.0,Y=621.0 (should be at cap-height 622?)

	* ngabeng (U+0999): X=210.0,Y=623.0 (should be at cap-height 622?)

	* dhabeng (U+09A7): X=299.0,Y=624.0 (should be at cap-height 622?)

	* shabeng (U+09B6): X=-12.0,Y=620.0 (should be at cap-height 622?)

	* evowelsignbeng (U+09C7): X=353.0,Y=1.5 (should be at baseline 0?)

	* aivowelsignbeng (U+09C8): X=353.0,Y=1.5 (should be at baseline 0?)

	* ovowelsignbeng (U+09CB): X=353.0,Y=1.5 (should be at baseline 0?) 

	* And 4 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* aabeng (U+0986): B<<1014.5,608.0>-<1034.0,594.0>-<1050.0,559.0>>/B<<1050.0,559.0>-<1049.0,564.0>-<1047.5,582.0>> = 13.257238846581073

	* aavowelsignbeng (U+09BE): B<<53.0,610.0>-<73.0,598.0>-<90.0,559.0>>/B<<90.0,559.0>-<89.0,564.0>-<87.5,582.0>> = 12.242331198874426 

	* And ovowelsignbeng (U+09CB): B<<745.0,610.0>-<765.0,598.0>-<782.0,559.0>>/B<<782.0,559.0>-<781.0,564.0>-<779.5,582.0>> = 12.242331198874426 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[19] NotoSansBengali-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali ExtraBold [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 995, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CED

	- uuvowelsignbeng

	- rrvocalicvowelsignbeng

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD5

	- uni1CD6

	- uni1CD8

	- uni0952 

	- And 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* shabeng
	* sharabeng
	* gadhabeng
	* ngakarabeng
	* ttarabeng
	* kababeng
	* nadabeng
	* dadhabeng
	* babhabeng
	* tatabeng and 391 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali ExtraBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dhanuktahalfbeng

	- kanuktahalfbeng

	- canuktahalfbeng 

	- And 22 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 701 but it should be 757 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* five.beng (U+0035): X=131.0,Y=-0.5 (should be at baseline 0?)

	* braceleft.beng (U+007B): X=430.0,Y=-2.0 (should be at baseline 0?)

	* uni0951 (U+0951): X=-203.0,Y=623.0 (should be at cap-height 622?)

	* uni0951 (U+0951): X=-307.0,Y=623.0 (should be at cap-height 622?)

	* aabeng (U+0986): X=1064.0,Y=621.0 (should be at cap-height 622?)

	* ngabeng (U+0999): X=452.0,Y=2.0 (should be at baseline 0?)

	* ngabeng (U+0999): X=228.0,Y=623.0 (should be at cap-height 622?)

	* ngabeng (U+0999): X=452.0,Y=2.0 (should be at baseline 0?)

	* dhabeng (U+09A7): X=306.0,Y=624.0 (should be at cap-height 622?)

	* rabeng (U+09B0): X=112.0,Y=0.5 (should be at baseline 0?) 

	* And 11 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* two.beng (U+0032) contains a short segment L<<249.0,147.0>--<249.0,141.0>>

	* aabeng (U+0986) contains a short segment B<<469.0,356.0>-<451.0,356.0>-<440.5,346.0>>

	* aabeng (U+0986) contains a short segment B<<440.5,346.0>-<430.0,336.0>-<430.0,321.0>>

	* aabeng (U+0986) contains a short segment B<<430.0,321.0>-<430.0,307.0>-<436.0,289.0>>

	* aabeng (U+0986) contains a short segment B<<285.5,310.0>-<281.0,330.0>-<281.0,345.0>>

	* aabeng (U+0986) contains a short segment B<<1068.0,562.0>-<1066.0,571.0>-<1065.0,589.5>>

	* aabeng (U+0986) contains a short segment B<<1065.0,589.5>-<1064.0,608.0>-<1064.0,621.0>>

	* ibeng (U+0987) contains a short segment B<<212.0,317.0>-<212.0,304.0>-<218.0,293.0>>

	* ibeng (U+0987) contains a short segment B<<142.0,904.0>-<141.0,895.0>-<140.0,888.0>>

	* ibeng (U+0987) contains a short segment B<<140.0,888.0>-<139.0,881.0>-<139.0,876.0>> 

	* And 80 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* aabeng (U+0986): B<<1034.5,608.5>-<1054.0,595.0>-<1068.0,562.0>>/B<<1068.0,562.0>-<1066.0,571.0>-<1065.0,589.5>> = 10.459909092929111

	* aavowelsignbeng (U+09BE): B<<50.5,609.5>-<70.0,597.0>-<85.0,562.0>>/B<<85.0,562.0>-<83.0,571.0>-<82.0,589.5>> = 10.66978280449666 

	* And ovowelsignbeng (U+09CB): B<<742.5,609.5>-<762.0,597.0>-<777.0,562.0>>/B<<777.0,562.0>-<775.0,571.0>-<774.0,589.5>> = 10.66978280449666 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[20] NotoSansBengali-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali ExtraLight [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 995, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CED

	- uuvowelsignbeng

	- rrvocalicvowelsignbeng

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD5

	- uni1CD6

	- uni1CD8

	- uni0952 

	- And 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* cacabeng
	* ssamabeng
	* badabeng
	* kassannabeng
	* ssakabeng
	* cachababeng
	* maparabeng
	* badarabeng
	* cacharabeng
	* ssakarabeng and 7 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dhanuktahalfbeng

	- kanuktahalfbeng

	- canuktahalfbeng 

	- And 22 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 614 but it should be 661 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* exclam.beng (U+0021): X=210.5,Y=1.5 (should be at baseline 0?)

	* exclam.beng (U+0021): X=158.5,Y=1.5 (should be at baseline 0?)

	* period.beng (U+002E): X=136.0,Y=1.5 (should be at baseline 0?)

	* period.beng (U+002E): X=84.5,Y=1.5 (should be at baseline 0?)

	* two.beng (U+0032): X=91.0,Y=623.0 (should be at cap-height 622?)

	* three.beng (U+0033): X=129.0,Y=-1.5 (should be at baseline 0?)

	* five.beng (U+0035): X=152.5,Y=1.5 (should be at baseline 0?)

	* nine.beng (U+0039): X=107.0,Y=-2.0 (should be at baseline 0?)

	* colon.beng (U+003A): X=97.5,Y=1.5 (should be at baseline 0?)

	* colon.beng (U+003A): X=149.0,Y=1.5 (should be at baseline 0?) 

	* And 17 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* two.beng (U+0032) contains a short segment L<<102.0,39.0>--<102.0,37.0>>

	* abeng (U+0985) contains a short segment B<<311.0,398.0>-<311.0,385.0>-<313.0,371.0>>

	* aabeng (U+0986) contains a short segment B<<311.0,398.0>-<311.0,385.0>-<313.0,371.0>>

	* aabeng (U+0986) contains a short segment B<<313.0,371.0>-<315.0,357.0>-<323.0,341.0>>

	* aabeng (U+0986) contains a short segment B<<287.0,332.0>-<280.0,349.0>-<276.5,367.5>>

	* aabeng (U+0986) contains a short segment B<<276.5,367.5>-<273.0,386.0>-<273.0,402.0>>

	* aabeng (U+0986) contains a short segment L<<-10.0,587.0>--<-10.0,622.0>>

	* aabeng (U+0986) contains a short segment L<<858.0,622.0>--<858.0,622.0>>

	* aabeng (U+0986) contains a short segment B<<954.0,549.0>-<953.0,559.0>-<952.5,577.0>>

	* aabeng (U+0986) contains a short segment B<<952.5,577.0>-<952.0,595.0>-<952.0,613.0>> 

	* And 60 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<858.0,622.0>> -> L<<858.0,622.0>--<858.0,622.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* chabeng (U+099B): B<<514.0,177.5>-<450.0,123.0>-<343.0,114.0>>/B<<343.0,114.0>-<493.0,89.0>-<651.0,1.0>> = 14.27027617105606

	* mabeng (U+09AE): L<<449.0,587.0>--<64.0,587.0>>/B<<64.0,587.0>-<143.0,574.0>-<185.0,541.5>> = 9.344671902099696 

	* And sabeng (U+09B8): L<<516.0,587.0>--<57.0,587.0>>/B<<57.0,587.0>-<145.0,570.0>-<197.5,544.5>> = 10.933816785755795 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[20] NotoSansBengali-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali Light [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 995, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CED

	- uuvowelsignbeng

	- rrvocalicvowelsignbeng

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD5

	- uni1CD6

	- uni1CD8

	- uni0952 

	- And 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* ngakarabeng
	* cacabeng
	* ssamabeng
	* mababeng
	* badabeng
	* papabeng
	* yarephiivowelsignbeng
	* kakabeng
	* kassababeng
	* ssattabeng and 48 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali Light' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dhanuktahalfbeng

	- kanuktahalfbeng

	- canuktahalfbeng 

	- And 22 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 627 but it should be 675 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* three.beng (U+0033): X=129.0,Y=-1.5 (should be at baseline 0?)

	* five.beng (U+0035): X=148.5,Y=0.5 (should be at baseline 0?)

	* nine.beng (U+0039): X=107.0,Y=-1.0 (should be at baseline 0?)

	* braceleft.beng (U+007B): X=180.0,Y=2.0 (should be at baseline 0?)

	* ngabeng (U+0999): X=162.0,Y=623.0 (should be at cap-height 622?)

	* shabeng (U+09B6): X=-7.0,Y=620.0 (should be at cap-height 622?)

	* evowelsignbeng (U+09C7): X=312.5,Y=1.0 (should be at baseline 0?)

	* aivowelsignbeng (U+09C8): X=312.5,Y=1.0 (should be at baseline 0?)

	* ovowelsignbeng (U+09CB): X=312.5,Y=1.0 (should be at baseline 0?)

	* auvowelsignbeng (U+09CC): X=312.5,Y=1.0 (should be at baseline 0?) 

	* And 4 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* two.beng (U+0032) contains a short segment L<<122.0,56.0>--<122.0,54.0>>

	* abeng (U+0985) contains a short segment B<<327.0,389.0>-<327.0,377.0>-<329.0,364.0>>

	* aabeng (U+0986) contains a short segment B<<327.0,389.0>-<327.0,377.0>-<329.0,364.0>>

	* aabeng (U+0986) contains a short segment B<<329.0,364.0>-<331.0,351.0>-<337.0,337.0>>

	* aabeng (U+0986) contains a short segment L<<873.0,622.0>--<873.0,622.0>>

	* aabeng (U+0986) contains a short segment B<<968.0,553.0>-<966.0,561.0>-<965.5,579.0>>

	* aabeng (U+0986) contains a short segment B<<965.5,579.0>-<965.0,597.0>-<965.0,613.0>>

	* aabeng (U+0986) contains a short segment L<<965.0,682.0>--<1001.0,682.0>>

	* ibeng (U+0987) contains a short segment B<<48.0,909.0>-<46.0,896.0>-<45.0,885.5>>

	* ibeng (U+0987) contains a short segment B<<45.0,885.5>-<44.0,875.0>-<44.0,866.0>> 

	* And 38 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<873.0,622.0>> -> L<<873.0,622.0>--<873.0,622.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* mabeng (U+09AE): L<<450.0,574.0>--<82.0,574.0>>/B<<82.0,574.0>-<187.0,558.0>-<229.5,500.0>> = 8.664135433108044 

	* And sabeng (U+09B8): L<<514.0,574.0>--<75.0,574.0>>/B<<75.0,574.0>-<159.0,558.0>-<208.0,534.0>> = 10.784297867562596 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[19] NotoSansBengali-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali Medium [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 995, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CED

	- uuvowelsignbeng

	- rrvocalicvowelsignbeng

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD5

	- uni1CD6

	- uni1CD8

	- uni0952 

	- And 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* sharabeng
	* gadhabeng
	* ngakarabeng
	* kababeng
	* babhabeng
	* ra1nuktahalfbeng
	* yarasquishbeng
	* cacabeng
	* charabeng
	* satarabeng and 261 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali Medium' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dhanuktahalfbeng

	- kanuktahalfbeng

	- canuktahalfbeng 

	- And 22 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 659 but it should be 710 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* three.beng (U+0033): X=127.0,Y=-1.0 (should be at baseline 0?)

	* five.beng (U+0035): X=138.0,Y=-0.5 (should be at baseline 0?)

	* nine.beng (U+0039): X=99.0,Y=-2.0 (should be at baseline 0?)

	* question.beng (U+003F): X=178.5,Y=620.5 (should be at cap-height 622?)

	* lvocalicbeng (U+098C): X=164.5,Y=620.0 (should be at cap-height 622?)

	* ngabeng (U+0999): X=188.0,Y=623.0 (should be at cap-height 622?)

	* dhabeng (U+09A7): X=295.0,Y=624.0 (should be at cap-height 622?)

	* shabeng (U+09B6): X=-10.0,Y=620.0 (should be at cap-height 622?)

	* llvocalicbeng (U+09E1): X=164.5,Y=620.0 (should be at cap-height 622?)

	* llvocalicbeng (U+09E1): X=209.0,Y=-2.0 (should be at baseline 0?) 

	* And 5 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* two.beng (U+0032) contains a short segment L<<177.0,99.0>--<177.0,95.0>>

	* aabeng (U+0986) contains a short segment B<<276.5,345.0>-<273.0,363.0>-<273.0,378.0>>

	* aabeng (U+0986) contains a short segment B<<1008.0,559.0>-<1006.0,564.0>-<1005.0,582.0>>

	* aabeng (U+0986) contains a short segment B<<1005.0,582.0>-<1004.0,600.0>-<1004.0,613.0>>

	* ibeng (U+0987) contains a short segment B<<-9.0,858.0>-<-9.0,871.0>-<-8.0,884.0>>

	* ibeng (U+0987) contains a short segment B<<-8.0,884.0>-<-7.0,897.0>-<-4.0,912.0>>

	* ibeng (U+0987) contains a short segment B<<162.0,360.0>-<162.0,352.0>-<164.0,344.0>>

	* ibeng (U+0987) contains a short segment B<<164.0,344.0>-<166.0,336.0>-<168.0,330.0>>

	* iibeng (U+0988) contains a short segment B<<60.5,351.0>-<57.0,370.0>-<57.0,385.0>>

	* iibeng (U+0988) contains a short segment B<<44.0,858.0>-<44.0,871.0>-<45.5,884.0>> 

	* And 56 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* aabeng (U+0986): B<<968.5,607.0>-<991.0,592.0>-<1008.0,559.0>>/B<<1008.0,559.0>-<1006.0,564.0>-<1005.0,582.0>> = 5.453918888591197

	* mabeng (U+09AE): L<<443.0,539.0>--<157.0,539.0>>/B<<157.0,539.0>-<228.0,521.0>-<265.0,472.0>> = 14.22596389875178 

	* And sabeng (U+09B8): L<<504.0,539.0>--<143.0,539.0>>/B<<143.0,539.0>-<204.0,527.0>-<240.0,506.5>> = 11.129189289611167 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[20] NotoSansBengali-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 995, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CED

	- uuvowelsignbeng

	- rrvocalicvowelsignbeng

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD5

	- uni1CD6

	- uni1CD8

	- uni0952 

	- And 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>🔥 <b>FAIL:</b> Check that texts shape as per expectation (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/shaping/regression">com.google.fonts/check/shaping/regression</a>)</summary><div>


* 🔥 **FAIL** qa/shaping_tests/bengali.json: Expected and actual shaping not matching
<div class="shaping">


<style type="text/css">
    @font-face {font-family: "TestFont"; src: url(../../fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf);}
    .tf { font-family: "TestFont"; }
    .shaping pre { font-size: 1.2rem; }
    .shaping li {
        font-size: 1.2rem;
        border-top: 1px solid #ddd;
        padding: 12px;
        margin-top: 12px;
    }
    .shaping-svg {
        height: 100px;
        margin: 10px;
        transform: matrix(1, 0, 0, -1, 0, 0);
    }
</style>

<h4>qa/shaping_tests/bengali.json: Expected and actual shaping not matching</h4>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ৗ᳐᳷ৈ৮꣱ৗ᳖ৎঞ</span> (Added by SIESTA)</li>


<pre>Expected: uni25CC=0+510|aulengthmarkbeng=0+266|uni1CD0=0@-214,323+0|uni1CF7=0+526|aivowelsignbeng=0+346|uni25CC=0+510|eightbeng=4+592|uniA8F1=4@0,323+0|uni25CC=4+510|aulengthmarkbeng=4+266|uni1CD6=4@-214,-319+0|khandatabeng=8+507|nyabeng=9+1019</pre>



<pre>Got     : uni25CC=0+510|aulengthmarkbeng=0+266|uni1CD0=0@-214,323+0|uni1CF7=0+456|aivowelsignbeng=0+346|uni25CC=0+510|eightbeng=4+592|uniA8F1=4@0,323+0|uni25CC=4+510|aulengthmarkbeng=4+266|uni1CD6=4@-214,-319+0|khandatabeng=8+525|nyabeng=9+1019</pre>



<pre>                                                                              ^^                                                                                                                                                   ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5000 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z"  transform="translate(0, 908)"/>
<path d="M171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L99.0,622.0Q98.0,663.0 79.5,681.0Q61.0,699.0 20.0,699.0L-149.0,699.0Q-214.0,699.0 -249.5,708.0Q-285.0,717.0 -310.0,736.0Q-364.0,777.0 -364.0,859.0Q-364.0,872.0 -362.5,885.0Q-361.0,898.0 -359.0,912.0L-285.0,907.0Q-287.0,895.0 -288.0,886.0Q-289.0,877.0 -289.0,869.0Q-289.0,847.0 -284.5,830.0Q-280.0,813.0 -270.0,802.0Q-256.0,786.0 -230.0,778.5Q-204.0,771.0 -154.0,771.0L-2.0,771.0Q51.0,771.0 82.0,763.0Q113.0,755.0 135.0,734.0Q168.0,702.0 171.0,622.0L276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0Z"  transform="translate(510, 908)"/>
<path d="M-430.0,661.0L-289.0,910.0L-228.0,910.0L-77.0,663.0L-131.0,636.0L-255.0,849.0L-371.0,636.0L-430.0,661.0Z"  transform="translate(562, 1231)"/>
<path d="M469.0,795.0Q438.0,818.0 406.0,831.0Q374.0,844.0 341.0,844.0Q305.0,844.0 274.5,831.5Q244.0,819.0 225.5,780.5Q207.0,742.0 207.0,664.0Q207.0,544.0 213.0,433.5Q219.0,323.0 227.0,213.0Q235.0,103.0 241.0,-15.5Q247.0,-134.0 247.0,-271.0L167.0,-271.0Q167.0,-134.0 161.0,-14.0Q155.0,106.0 146.5,217.5Q138.0,329.0 132.0,439.5Q126.0,550.0 126.0,668.0Q126.0,764.0 155.5,818.5Q185.0,873.0 232.0,895.0Q279.0,917.0 332.0,917.0Q388.0,917.0 433.5,899.0Q479.0,881.0 516.0,854.0L469.0,795.0Z"  transform="translate(776, 908)"/>
<path d="M283.0,622.0Q282.0,661.0 264.5,680.0Q247.0,699.0 203.0,699.0L183.0,699.0Q118.0,699.0 82.5,708.0Q47.0,717.0 22.0,736.0Q-32.0,777.0 -32.0,859.0Q-32.0,872.0 -30.5,884.5Q-29.0,897.0 -27.0,912.0L47.0,907.0Q43.0,887.0 43.0,869.0Q43.0,847.0 47.5,830.0Q52.0,813.0 62.0,802.0Q76.0,786.0 102.0,778.5Q128.0,771.0 178.0,771.0L182.0,771.0Q235.0,771.0 266.0,763.0Q297.0,755.0 319.0,734.0Q352.0,702.0 355.0,622.0L356.0,622.0L356.0,551.0L336.0,551.0Q305.0,544.0 269.0,520.5Q233.0,497.0 201.0,459.5Q169.0,422.0 148.5,372.0Q128.0,322.0 128.0,262.0Q128.0,190.0 149.5,147.5Q171.0,105.0 203.0,87.0Q235.0,69.0 267.0,69.0Q292.0,69.0 309.0,74.0Q326.0,79.0 348.0,92.0L383.0,31.0Q357.0,11.0 326.0,3.0Q295.0,-5.0 264.0,-5.0Q201.0,-5.0 152.5,28.0Q104.0,61.0 76.5,120.5Q49.0,180.0 49.0,260.0Q49.0,359.0 93.5,435.0Q138.0,511.0 208.0,554.0Q191.0,552.0 172.0,551.5Q153.0,551.0 130.0,551.0L-10.0,551.0L-10.0,622.0L283.0,622.0Z"  transform="translate(1232, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z"  transform="translate(1578, 908)"/>
<path d="M237.0,0.0Q198.0,0.0 172.5,11.0Q147.0,22.0 132.0,38.0Q114.0,56.0 102.5,83.0Q91.0,110.0 91.0,164.0L91.0,481.0Q91.0,518.0 78.5,532.0Q66.0,546.0 22.0,547.0L31.0,624.0Q106.0,621.0 136.0,595.0Q153.0,580.0 160.0,556.5Q167.0,533.0 167.0,501.0L167.0,355.0Q198.0,366.0 225.5,370.5Q253.0,375.0 269.0,375.0Q280.0,375.0 294.0,373.5Q308.0,372.0 318.0,370.0Q347.0,363.0 366.5,361.5Q386.0,360.0 408.0,360.0Q446.0,360.0 470.5,371.0Q495.0,382.0 514.0,418.0L586.0,383.0Q567.0,333.0 528.0,312.5Q489.0,292.0 442.0,292.0Q436.0,292.0 430.0,292.0Q448.0,257.0 448.0,213.0Q448.0,147.0 419.5,99.0Q391.0,51.0 343.5,25.5Q296.0,0.0 237.0,0.0ZM238.0,71.0Q282.0,71.0 311.0,92.5Q340.0,114.0 354.5,146.5Q369.0,179.0 369.0,212.0Q369.0,249.0 354.5,269.0Q340.0,289.0 318.5,296.5Q297.0,304.0 274.0,304.0Q241.0,304.0 215.5,298.0Q190.0,292.0 167.0,281.0L167.0,168.0Q167.0,135.0 172.0,117.5Q177.0,100.0 184.0,92.0Q192.0,84.0 203.5,77.5Q215.0,71.0 238.0,71.0Z"  transform="translate(2088, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z"  transform="translate(2680, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z"  transform="translate(2680, 908)"/>
<path d="M171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L99.0,622.0Q98.0,663.0 79.5,681.0Q61.0,699.0 20.0,699.0L-149.0,699.0Q-214.0,699.0 -249.5,708.0Q-285.0,717.0 -310.0,736.0Q-364.0,777.0 -364.0,859.0Q-364.0,872.0 -362.5,885.0Q-361.0,898.0 -359.0,912.0L-285.0,907.0Q-287.0,895.0 -288.0,886.0Q-289.0,877.0 -289.0,869.0Q-289.0,847.0 -284.5,830.0Q-280.0,813.0 -270.0,802.0Q-256.0,786.0 -230.0,778.5Q-204.0,771.0 -154.0,771.0L-2.0,771.0Q51.0,771.0 82.0,763.0Q113.0,755.0 135.0,734.0Q168.0,702.0 171.0,622.0L276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0Z"  transform="translate(3190, 908)"/>
<path d="M-426.0,-94.0L-348.0,-94.0L-348.0,-202.0L-78.0,-202.0L-78.0,-271.0L-426.0,-271.0L-426.0,-94.0Z"  transform="translate(3242, 589)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z"  transform="translate(3456, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z"  transform="translate(3981, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5052 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z"  transform="translate(0, 908)"/>
<path d="M171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L99.0,622.0Q98.0,663.0 79.5,681.0Q61.0,699.0 20.0,699.0L-149.0,699.0Q-214.0,699.0 -249.5,708.0Q-285.0,717.0 -310.0,736.0Q-364.0,777.0 -364.0,859.0Q-364.0,872.0 -362.5,885.0Q-361.0,898.0 -359.0,912.0L-285.0,907.0Q-287.0,895.0 -288.0,886.0Q-289.0,877.0 -289.0,869.0Q-289.0,847.0 -284.5,830.0Q-280.0,813.0 -270.0,802.0Q-256.0,786.0 -230.0,778.5Q-204.0,771.0 -154.0,771.0L-2.0,771.0Q51.0,771.0 82.0,763.0Q113.0,755.0 135.0,734.0Q168.0,702.0 171.0,622.0L276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0Z"  transform="translate(510, 908)"/>
<path d="M-430.0,661.0L-289.0,910.0L-228.0,910.0L-77.0,663.0L-131.0,636.0L-255.0,849.0L-371.0,636.0L-430.0,661.0Z"  transform="translate(562, 1231)"/>
<path d="M469.0,795.0Q438.0,818.0 406.0,831.0Q374.0,844.0 341.0,844.0Q305.0,844.0 274.5,831.5Q244.0,819.0 225.5,780.5Q207.0,742.0 207.0,664.0Q207.0,544.0 213.0,433.5Q219.0,323.0 227.0,213.0Q235.0,103.0 241.0,-15.5Q247.0,-134.0 247.0,-271.0L167.0,-271.0Q167.0,-134.0 161.0,-14.0Q155.0,106.0 146.5,217.5Q138.0,329.0 132.0,439.5Q126.0,550.0 126.0,668.0Q126.0,764.0 155.5,818.5Q185.0,873.0 232.0,895.0Q279.0,917.0 332.0,917.0Q388.0,917.0 433.5,899.0Q479.0,881.0 516.0,854.0L469.0,795.0Z"  transform="translate(776, 908)"/>
<path d="M283.0,622.0Q282.0,661.0 264.5,680.0Q247.0,699.0 203.0,699.0L183.0,699.0Q118.0,699.0 82.5,708.0Q47.0,717.0 22.0,736.0Q-32.0,777.0 -32.0,859.0Q-32.0,872.0 -30.5,884.5Q-29.0,897.0 -27.0,912.0L47.0,907.0Q43.0,887.0 43.0,869.0Q43.0,847.0 47.5,830.0Q52.0,813.0 62.0,802.0Q76.0,786.0 102.0,778.5Q128.0,771.0 178.0,771.0L182.0,771.0Q235.0,771.0 266.0,763.0Q297.0,755.0 319.0,734.0Q352.0,702.0 355.0,622.0L356.0,622.0L356.0,551.0L336.0,551.0Q305.0,544.0 269.0,520.5Q233.0,497.0 201.0,459.5Q169.0,422.0 148.5,372.0Q128.0,322.0 128.0,262.0Q128.0,190.0 149.5,147.5Q171.0,105.0 203.0,87.0Q235.0,69.0 267.0,69.0Q292.0,69.0 309.0,74.0Q326.0,79.0 348.0,92.0L383.0,31.0Q357.0,11.0 326.0,3.0Q295.0,-5.0 264.0,-5.0Q201.0,-5.0 152.5,28.0Q104.0,61.0 76.5,120.5Q49.0,180.0 49.0,260.0Q49.0,359.0 93.5,435.0Q138.0,511.0 208.0,554.0Q191.0,552.0 172.0,551.5Q153.0,551.0 130.0,551.0L-10.0,551.0L-10.0,622.0L283.0,622.0Z"  transform="translate(1302, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z"  transform="translate(1648, 908)"/>
<path d="M237.0,0.0Q198.0,0.0 172.5,11.0Q147.0,22.0 132.0,38.0Q114.0,56.0 102.5,83.0Q91.0,110.0 91.0,164.0L91.0,481.0Q91.0,518.0 78.5,532.0Q66.0,546.0 22.0,547.0L31.0,624.0Q106.0,621.0 136.0,595.0Q153.0,580.0 160.0,556.5Q167.0,533.0 167.0,501.0L167.0,355.0Q198.0,366.0 225.5,370.5Q253.0,375.0 269.0,375.0Q280.0,375.0 294.0,373.5Q308.0,372.0 318.0,370.0Q347.0,363.0 366.5,361.5Q386.0,360.0 408.0,360.0Q446.0,360.0 470.5,371.0Q495.0,382.0 514.0,418.0L586.0,383.0Q567.0,333.0 528.0,312.5Q489.0,292.0 442.0,292.0Q436.0,292.0 430.0,292.0Q448.0,257.0 448.0,213.0Q448.0,147.0 419.5,99.0Q391.0,51.0 343.5,25.5Q296.0,0.0 237.0,0.0ZM238.0,71.0Q282.0,71.0 311.0,92.5Q340.0,114.0 354.5,146.5Q369.0,179.0 369.0,212.0Q369.0,249.0 354.5,269.0Q340.0,289.0 318.5,296.5Q297.0,304.0 274.0,304.0Q241.0,304.0 215.5,298.0Q190.0,292.0 167.0,281.0L167.0,168.0Q167.0,135.0 172.0,117.5Q177.0,100.0 184.0,92.0Q192.0,84.0 203.5,77.5Q215.0,71.0 238.0,71.0Z"  transform="translate(2158, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z"  transform="translate(2750, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z"  transform="translate(2750, 908)"/>
<path d="M171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L99.0,622.0Q98.0,663.0 79.5,681.0Q61.0,699.0 20.0,699.0L-149.0,699.0Q-214.0,699.0 -249.5,708.0Q-285.0,717.0 -310.0,736.0Q-364.0,777.0 -364.0,859.0Q-364.0,872.0 -362.5,885.0Q-361.0,898.0 -359.0,912.0L-285.0,907.0Q-287.0,895.0 -288.0,886.0Q-289.0,877.0 -289.0,869.0Q-289.0,847.0 -284.5,830.0Q-280.0,813.0 -270.0,802.0Q-256.0,786.0 -230.0,778.5Q-204.0,771.0 -154.0,771.0L-2.0,771.0Q51.0,771.0 82.0,763.0Q113.0,755.0 135.0,734.0Q168.0,702.0 171.0,622.0L276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0Z"  transform="translate(3260, 908)"/>
<path d="M-426.0,-94.0L-348.0,-94.0L-348.0,-202.0L-78.0,-202.0L-78.0,-271.0L-426.0,-271.0L-426.0,-94.0Z"  transform="translate(3312, 589)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z"  transform="translate(3526, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z"  transform="translate(4033, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">জ়ঞগএগ+꣱ং᳒</span> (Added by SIESTA)</li>


<pre>Expected: januktabeng=0+917|nyabeng=2+1001|gabeng=3+656|ebeng=4+740|gabeng=5+656|plus.beng=6+592|uni25CC=6+510|uniA8F1=6+0|uni25CC=6+510|anusvarabeng=6+438|uni1CD2=6@-386,323+0</pre>



<pre>Got     : januktabeng=0+917|nyabeng=2+1019|gabeng=3+656|ebeng=4+758|gabeng=5+656|plus.beng=6+592|uni25CC=6+510|uniA8F1=6+0|uni25CC=6+510|anusvarabeng=6+438|uni1CD2=6@-386,323+0</pre>



<pre>                                        +                        ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 6056 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(917, 908)"/>
<path d=""  transform="translate(1936, 908)"/>
<path d=""  transform="translate(2592, 908)"/>
<path d=""  transform="translate(3350, 908)"/>
<path d=""  transform="translate(4006, 908)"/>
<path d=""  transform="translate(4598, 908)"/>
<path d=""  transform="translate(5108, 908)"/>
<path d=""  transform="translate(5108, 908)"/>
<path d=""  transform="translate(5618, 908)"/>
<path d=""  transform="translate(5670, 1231)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 6020 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(917, 908)"/>
<path d=""  transform="translate(1918, 908)"/>
<path d=""  transform="translate(2574, 908)"/>
<path d=""  transform="translate(3314, 908)"/>
<path d=""  transform="translate(3970, 908)"/>
<path d=""  transform="translate(4562, 908)"/>
<path d=""  transform="translate(5072, 908)"/>
<path d=""  transform="translate(5072, 908)"/>
<path d=""  transform="translate(5582, 908)"/>
<path d=""  transform="translate(5634, 1231)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">িআংএঠ᳘</span> (Added by SIESTA)</li>


<pre>Expected: ivowelsignbeng=0+266|uni25CC=0+510|aabeng=1+1158|anusvarabeng=1+403|ebeng=3+758|tthabeng=4+591|uni1CD8=4@-41,-351+0</pre>



<pre>Got     : ivowelsignbeng=0+266|uni25CC=0+510|aabeng=1+1158|anusvarabeng=1+438|ebeng=3+758|tthabeng=4+591|uni1CD8=4@-41,-351+0</pre>



<pre>                                                                           +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3721 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(266, 908)"/>
<path d=""  transform="translate(776, 908)"/>
<path d=""  transform="translate(1934, 908)"/>
<path d=""  transform="translate(2372, 908)"/>
<path d=""  transform="translate(3130, 908)"/>
<path d=""  transform="translate(3680, 557)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3686 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(266, 908)"/>
<path d=""  transform="translate(776, 908)"/>
<path d=""  transform="translate(1934, 908)"/>
<path d=""  transform="translate(2337, 908)"/>
<path d=""  transform="translate(3095, 908)"/>
<path d=""  transform="translate(3645, 557)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঙওদ়ষ᳒ট॒</span> (Added by SIESTA)</li>


<pre>Expected: ngabeng=0+705|obeng=1+738|danuktabeng=2+603|ssabeng=4+633|uni1CD2=4@-62,323+0|ttabeng=6+567|uni0952=6@-29,-313+0</pre>



<pre>Got     : ngabeng=0+723|obeng=1+738|danuktabeng=2+603|ssabeng=4+633|uni1CD2=4@-62,323+0|ttabeng=6+567|uni0952=6@-29,-313+0</pre>



<pre>                     ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3264 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(723, 908)"/>
<path d=""  transform="translate(1461, 908)"/>
<path d=""  transform="translate(2064, 908)"/>
<path d=""  transform="translate(2635, 1231)"/>
<path d=""  transform="translate(2697, 908)"/>
<path d=""  transform="translate(3235, 595)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3246 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(705, 908)"/>
<path d=""  transform="translate(1443, 908)"/>
<path d=""  transform="translate(2046, 908)"/>
<path d=""  transform="translate(2617, 1231)"/>
<path d=""  transform="translate(2679, 908)"/>
<path d=""  transform="translate(3217, 595)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঞও়্꣱৾ফ্ল</span> (Added by SIESTA)</li>


<pre>Expected: nyabeng=0+1001|obeng=1+738|nuktabeng=1+0|viramabeng=1+0|uniA8F1=1@0,323+0|uni25CC=1+510|uni09FE=1+0|phalabeng=6+824</pre>



<pre>Got     : nyabeng=0+1019|obeng=1+738|nuktabeng=1+0|viramabeng=1+0|uniA8F1=1@0,323+0|uni25CC=1+510|uni09FE=1+0|phalabeng=6+824</pre>



<pre>                      +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3091 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(1019, 908)"/>
<path d=""  transform="translate(1757, 908)"/>
<path d=""  transform="translate(1757, 908)"/>
<path d=""  transform="translate(1757, 1231)"/>
<path d=""  transform="translate(1757, 908)"/>
<path d=""  transform="translate(2267, 908)"/>
<path d=""  transform="translate(2267, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3073 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(1001, 908)"/>
<path d=""  transform="translate(1739, 908)"/>
<path d=""  transform="translate(1739, 908)"/>
<path d=""  transform="translate(1739, 1231)"/>
<path d=""  transform="translate(1739, 908)"/>
<path d=""  transform="translate(2249, 908)"/>
<path d=""  transform="translate(2249, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ন়ঝৣঞ়টৃঁৎপ</span> (Added by SIESTA)</li>


<pre>Expected: nanuktabeng=0+604|jhabeng=2+794|llvocalicvowelsignbeng=2@-207,0+0|nyanuktabeng=4+1019|ttabeng=6+567|rvocalicvowelsignbeng=6@-83,0+0|candrabindualtbeng=6+0|khandatabeng=9+507|pabeng=10+716</pre>



<pre>Got     : nanuktabeng=0+604|jhabeng=2+794|llvocalicvowelsignbeng=2@-207,0+0|nyanuktabeng=4+1019|ttabeng=6+567|rvocalicvowelsignbeng=6@-83,0+0|candrabindualtbeng=6+0|khandatabeng=9+525|pabeng=10+716</pre>



<pre>                                                                                                                                                                                     ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4225 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(604, 908)"/>
<path d=""  transform="translate(1191, 908)"/>
<path d=""  transform="translate(1398, 908)"/>
<path d=""  transform="translate(2417, 908)"/>
<path d=""  transform="translate(2901, 908)"/>
<path d=""  transform="translate(2984, 908)"/>
<path d=""  transform="translate(2984, 908)"/>
<path d=""  transform="translate(3509, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4207 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(604, 908)"/>
<path d=""  transform="translate(1191, 908)"/>
<path d=""  transform="translate(1398, 908)"/>
<path d=""  transform="translate(2417, 908)"/>
<path d=""  transform="translate(2901, 908)"/>
<path d=""  transform="translate(2984, 908)"/>
<path d=""  transform="translate(2984, 908)"/>
<path d=""  transform="translate(3491, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ৄ৾শ‍ুৎৎ</span> (Added by SIESTA)</li>


<pre>Expected: uni25CC=0+510|rrvocalicvowelsignbeng=0+0|uni09FE=0@0,323+0|shubeng=2+807|khandatabeng=5+507|khandatabeng=6+525</pre>



<pre>Got     : uni25CC=0+510|rrvocalicvowelsignbeng=0+0|uni09FE=0@0,323+0|shubeng=2+825|khandatabeng=5+525|khandatabeng=6+525</pre>



<pre>                                                                                ^^                 ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2385 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(510, 908)"/>
<path d=""  transform="translate(510, 1231)"/>
<path d=""  transform="translate(510, 908)"/>
<path d=""  transform="translate(1335, 908)"/>
<path d=""  transform="translate(1860, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2349 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(510, 908)"/>
<path d=""  transform="translate(510, 1231)"/>
<path d=""  transform="translate(510, 908)"/>
<path d=""  transform="translate(1317, 908)"/>
<path d=""  transform="translate(1824, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ফ়ৡগপৣ</span> (Added by SIESTA)</li>


<pre>Expected: phanuktabeng=0+838|llvocalicbeng=2+621|gabeng=3+656|pabeng=4+716|llvocalicvowelsignbeng=4+0</pre>



<pre>Got     : phanuktabeng=0+838|llvocalicbeng=2+639|gabeng=3+656|pabeng=4+716|llvocalicvowelsignbeng=4+0</pre>



<pre>                                              ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2849 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(838, 908)"/>
<path d=""  transform="translate(1477, 908)"/>
<path d=""  transform="translate(2133, 908)"/>
<path d=""  transform="translate(2849, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2831 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(838, 908)"/>
<path d=""  transform="translate(1459, 908)"/>
<path d=""  transform="translate(2115, 908)"/>
<path d=""  transform="translate(2831, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঌঔত্ম‌꣱</span> (Added by SIESTA)</li>


<pre>Expected: lvocalicbeng=0+621|aubeng=1+874|tamabeng=2+901|space=5+0|uni25CC=5+510|uniA8F1=5+0</pre>



<pre>Got     : lvocalicbeng=0+639|aubeng=1+874|tamabeng=2+901|space=5+0|uni25CC=5+510|uniA8F1=5+0</pre>



<pre>                          ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2924 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(639, 908)"/>
<path d=""  transform="translate(1513, 908)"/>
<path d=""  transform="translate(2414, 908)"/>
<path d=""  transform="translate(2414, 908)"/>
<path d=""  transform="translate(2924, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2906 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(621, 908)"/>
<path d=""  transform="translate(1495, 908)"/>
<path d=""  transform="translate(2396, 908)"/>
<path d=""  transform="translate(2396, 908)"/>
<path d=""  transform="translate(2906, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ফৄঋঙল্দূ9৾</span> (Added by SIESTA)</li>


<pre>Expected: phabeng=0+838|rrvocalicvowelsignbeng=0@-221,0+0|rvocalicbeng=2+835|ngabeng=3+723|ladabeng=4+1021|uuvowelsignbeng=4@11,0+0|nine.beng=8+551|uni09FE=8@0,323+0</pre>



<pre>Got     : phabeng=0+838|rrvocalicvowelsignbeng=0@-221,0+0|rvocalicbeng=2+853|ngabeng=3+723|ladabeng=4+1021|uuvowelsignbeng=4@11,0+0|nine.beng=8+551|uni09FE=8@0,323+0</pre>



<pre>                                                                          +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3986 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(617, 908)"/>
<path d=""  transform="translate(838, 908)"/>
<path d=""  transform="translate(1691, 908)"/>
<path d=""  transform="translate(2414, 908)"/>
<path d=""  transform="translate(3446, 908)"/>
<path d=""  transform="translate(3435, 908)"/>
<path d=""  transform="translate(3986, 1231)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3968 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(617, 908)"/>
<path d=""  transform="translate(838, 908)"/>
<path d=""  transform="translate(1673, 908)"/>
<path d=""  transform="translate(2396, 908)"/>
<path d=""  transform="translate(3428, 908)"/>
<path d=""  transform="translate(3417, 908)"/>
<path d=""  transform="translate(3968, 1231)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ৠএঢ়᳐দ᳖িঊঌ॒</span> (Added by SIESTA)</li>


<pre>Expected: rrvocalicbeng=0+835|ebeng=1+758|rhabeng=2+567|uni1CD0=2@-29,323+0|dabeng=4+603|uni1CD6=4@-47,-319+0|ivowelsignbeng=4+266|uni25CC=4+510|uubeng=7+853|lvocalicbeng=8+639|uni0952=8@-65,-313+0</pre>



<pre>Got     : rrvocalicbeng=0+853|ebeng=1+758|rhabeng=2+567|uni1CD0=2@-29,323+0|dabeng=4+603|uni1CD6=4@-47,-319+0|ivowelsignbeng=4+266|uni25CC=4+510|uubeng=7+853|lvocalicbeng=8+639|uni0952=8@-65,-313+0</pre>



<pre>                           +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5049 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(853, 908)"/>
<path d=""  transform="translate(1611, 908)"/>
<path d=""  transform="translate(2149, 1231)"/>
<path d=""  transform="translate(2178, 908)"/>
<path d=""  transform="translate(2734, 589)"/>
<path d=""  transform="translate(2781, 908)"/>
<path d=""  transform="translate(3047, 908)"/>
<path d=""  transform="translate(3557, 908)"/>
<path d=""  transform="translate(4410, 908)"/>
<path d=""  transform="translate(4984, 595)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5031 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(835, 908)"/>
<path d=""  transform="translate(1593, 908)"/>
<path d=""  transform="translate(2131, 1231)"/>
<path d=""  transform="translate(2160, 908)"/>
<path d=""  transform="translate(2716, 589)"/>
<path d=""  transform="translate(2763, 908)"/>
<path d=""  transform="translate(3029, 908)"/>
<path d=""  transform="translate(3539, 908)"/>
<path d=""  transform="translate(4392, 908)"/>
<path d=""  transform="translate(4966, 595)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঙূঃ᳐ল্ৡৠএঋ</span> (Added by SIESTA)</li>


<pre>Expected: ngabeng=0+723|uuvowelsignlongbeng=0@-107,0+0|visargabeng=0+438|uni1CD0=0@-386,323+0|labeng=4+731|viramabeng=4+0|llvocalicbeng=6+621|rrvocalicbeng=7+835|ebeng=8+740|rvocalicbeng=9+853</pre>



<pre>Got     : ngabeng=0+723|uuvowelsignlongbeng=0@-107,0+0|visargabeng=0+438|uni1CD0=0@-386,323+0|labeng=4+731|viramabeng=4+0|llvocalicbeng=6+639|rrvocalicbeng=7+853|ebeng=8+758|rvocalicbeng=9+853</pre>



<pre>                                                                                                                                           ^^                  +           ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4995 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(616, 908)"/>
<path d=""  transform="translate(723, 908)"/>
<path d=""  transform="translate(775, 1231)"/>
<path d=""  transform="translate(1161, 908)"/>
<path d=""  transform="translate(1892, 908)"/>
<path d=""  transform="translate(1892, 908)"/>
<path d=""  transform="translate(2531, 908)"/>
<path d=""  transform="translate(3384, 908)"/>
<path d=""  transform="translate(4142, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4941 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(616, 908)"/>
<path d=""  transform="translate(723, 908)"/>
<path d=""  transform="translate(775, 1231)"/>
<path d=""  transform="translate(1161, 908)"/>
<path d=""  transform="translate(1892, 908)"/>
<path d=""  transform="translate(1892, 908)"/>
<path d=""  transform="translate(2513, 908)"/>
<path d=""  transform="translate(3348, 908)"/>
<path d=""  transform="translate(4088, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঞ্জওওᳪ</span> (Added by SIESTA)</li>


<pre>Expected: nyajabeng=0+842|obeng=3+720|obeng=4+738|uni1CEA=5+748</pre>



<pre>Got     : nyajabeng=0+860|obeng=3+738|obeng=4+738|uni1CEA=5+748</pre>



<pre>                       ^^          ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3084 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(860, 908)"/>
<path d=""  transform="translate(1598, 908)"/>
<path d=""  transform="translate(2336, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3048 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(842, 908)"/>
<path d=""  transform="translate(1562, 908)"/>
<path d=""  transform="translate(2300, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">চৢল্ডূৎঙঢৣ</span> (Added by SIESTA)</li>


<pre>Expected: cabeng=0+567|lvocalicvowelsignbeng=0@-83,0+0|laddabeng=2+933|uuvowelsignbeng=2@-106,0+0|khandatabeng=6+507|ngabeng=7+723|ddhabeng=8+567|llvocalicvowelsignbeng=8@-83,0+0</pre>



<pre>Got     : cabeng=0+567|lvocalicvowelsignbeng=0@-83,0+0|laddabeng=2+933|uuvowelsignbeng=2@-106,0+0|khandatabeng=6+525|ngabeng=7+723|ddhabeng=8+567|llvocalicvowelsignbeng=8@-83,0+0</pre>



<pre>                                                                                                                  ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3315 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(484, 908)"/>
<path d=""  transform="translate(567, 908)"/>
<path d=""  transform="translate(1394, 908)"/>
<path d=""  transform="translate(1500, 908)"/>
<path d=""  transform="translate(2025, 908)"/>
<path d=""  transform="translate(2748, 908)"/>
<path d=""  transform="translate(3232, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3297 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(484, 908)"/>
<path d=""  transform="translate(567, 908)"/>
<path d=""  transform="translate(1394, 908)"/>
<path d=""  transform="translate(1500, 908)"/>
<path d=""  transform="translate(2007, 908)"/>
<path d=""  transform="translate(2730, 908)"/>
<path d=""  transform="translate(3214, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">মৢথ্ᳶিফংঐচ॑</span> (Added by SIESTA)</li>


<pre>Expected: mabeng=0+622|lvocalicvowelsignbeng=0+0|thabeng=2+645|viramabeng=2+0|ivowelsignbeng=4+266|uni1CF6=4+628|phabeng=6+838|anusvarabeng=6+403|aibeng=8+873|cabeng=9+567|uni0951=9@-29,323+0</pre>



<pre>Got     : mabeng=0+622|lvocalicvowelsignbeng=0+0|thabeng=2+645|viramabeng=2+0|ivowelsignbeng=4+266|uni1CF6=4+628|phabeng=6+838|anusvarabeng=6+438|aibeng=8+873|cabeng=9+567|uni0951=9@-29,323+0</pre>



<pre>                                                                                                                                               +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4877 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(622, 908)"/>
<path d=""  transform="translate(622, 908)"/>
<path d=""  transform="translate(1267, 908)"/>
<path d=""  transform="translate(1267, 908)"/>
<path d=""  transform="translate(1533, 908)"/>
<path d=""  transform="translate(2161, 908)"/>
<path d=""  transform="translate(2999, 908)"/>
<path d=""  transform="translate(3437, 908)"/>
<path d=""  transform="translate(4310, 908)"/>
<path d=""  transform="translate(4848, 1231)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4842 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(622, 908)"/>
<path d=""  transform="translate(622, 908)"/>
<path d=""  transform="translate(1267, 908)"/>
<path d=""  transform="translate(1267, 908)"/>
<path d=""  transform="translate(1533, 908)"/>
<path d=""  transform="translate(2161, 908)"/>
<path d=""  transform="translate(2999, 908)"/>
<path d=""  transform="translate(3402, 908)"/>
<path d=""  transform="translate(4275, 908)"/>
<path d=""  transform="translate(4813, 1231)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঋৎ৲৾ঠীগ॑ণ্</span> (Added by SIESTA)</li>


<pre>Expected: rvocalicbeng=0+835|khandatabeng=1+525|rupeemarkbeng=2+589|uni25CC=2+510|uni09FE=2+0|tthabeng=4+591|iivowelsignshortbeng=4+266|gabeng=6+656|uni0951=6@-73,323+0|nnabeng=8+620|viramabeng=8+0</pre>



<pre>Got     : rvocalicbeng=0+853|khandatabeng=1+525|rupeemarkbeng=2+589|uni25CC=2+510|uni09FE=2+0|tthabeng=4+591|iivowelsignshortbeng=4+266|gabeng=6+656|uni0951=6@-73,323+0|nnabeng=8+620|viramabeng=8+0</pre>



<pre>                          +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4610 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(853, 908)"/>
<path d=""  transform="translate(1378, 908)"/>
<path d=""  transform="translate(1967, 908)"/>
<path d=""  transform="translate(2477, 908)"/>
<path d=""  transform="translate(2477, 908)"/>
<path d=""  transform="translate(3068, 908)"/>
<path d=""  transform="translate(3334, 908)"/>
<path d=""  transform="translate(3917, 1231)"/>
<path d=""  transform="translate(3990, 908)"/>
<path d=""  transform="translate(4610, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4592 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(835, 908)"/>
<path d=""  transform="translate(1360, 908)"/>
<path d=""  transform="translate(1949, 908)"/>
<path d=""  transform="translate(2459, 908)"/>
<path d=""  transform="translate(2459, 908)"/>
<path d=""  transform="translate(3050, 908)"/>
<path d=""  transform="translate(3316, 908)"/>
<path d=""  transform="translate(3899, 1231)"/>
<path d=""  transform="translate(3972, 908)"/>
<path d=""  transform="translate(4592, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঙ্ক᳭ৠঌঠ</span> (Added by SIESTA)</li>


<pre>Expected: ngakabeng=0+679|uni1CED=0@-85,-363+0|rrvocalicbeng=4+835|lvocalicbeng=5+639|tthabeng=6+591</pre>



<pre>Got     : ngakabeng=0+679|uni1CED=0@-85,-363+0|rrvocalicbeng=4+853|lvocalicbeng=5+639|tthabeng=6+591</pre>



<pre>                                                                +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2762 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(594, 545)"/>
<path d=""  transform="translate(679, 908)"/>
<path d=""  transform="translate(1532, 908)"/>
<path d=""  transform="translate(2171, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2744 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(594, 545)"/>
<path d=""  transform="translate(679, 908)"/>
<path d=""  transform="translate(1514, 908)"/>
<path d=""  transform="translate(2153, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">িপঁআঁংণঠ॒</span> (Added by SIESTA)</li>


<pre>Expected: ivowelsignbeng=0+266|uni25CC=0+510|pabeng=1+716|candrabindubeng=1@-61,0+0|aabeng=3+1158|candrabindubeng=3@-61,0+0|anusvarabeng=3+399|nnabeng=6+620|tthabeng=7+591|uni0952=7@-41,-313+0</pre>



<pre>Got     : ivowelsignbeng=0+266|uni25CC=0+510|pabeng=1+716|candrabindubeng=1@-61,0+0|aabeng=3+1158|candrabindubeng=3@-61,0+0|anusvarabeng=3+438|nnabeng=6+620|tthabeng=7+591|uni0952=7@-41,-313+0</pre>



<pre>                                                                                                                                            ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4299 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(266, 908)"/>
<path d=""  transform="translate(776, 908)"/>
<path d=""  transform="translate(1431, 908)"/>
<path d=""  transform="translate(1492, 908)"/>
<path d=""  transform="translate(2589, 908)"/>
<path d=""  transform="translate(2650, 908)"/>
<path d=""  transform="translate(3088, 908)"/>
<path d=""  transform="translate(3708, 908)"/>
<path d=""  transform="translate(4258, 595)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4260 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(266, 908)"/>
<path d=""  transform="translate(776, 908)"/>
<path d=""  transform="translate(1431, 908)"/>
<path d=""  transform="translate(1492, 908)"/>
<path d=""  transform="translate(2589, 908)"/>
<path d=""  transform="translate(2650, 908)"/>
<path d=""  transform="translate(3049, 908)"/>
<path d=""  transform="translate(3669, 908)"/>
<path d=""  transform="translate(4219, 595)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">০৾ৰ্এ॑গ᳭ঞ্ছ</span> (Added by SIESTA)</li>


<pre>Expected: zerobeng=0+592|uni09FE=0@0,323+0|ebeng=2+740|rephbeng=2@-93,0+0|uni0951=2@-106,323+0|gabeng=6+656|uni1CED=6@-73,-363+0|nyachabeng=8+744</pre>



<pre>Got     : zerobeng=0+592|uni09FE=0@0,323+0|ebeng=2+758|rephbeng=2@-111,0+0|uni0951=2@-124,323+0|gabeng=6+656|uni1CED=6@-73,-363+0|nyachabeng=8+744</pre>



<pre>                                                    ^^             ^^                 ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2750 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(592, 1231)"/>
<path d=""  transform="translate(592, 908)"/>
<path d=""  transform="translate(1239, 908)"/>
<path d=""  transform="translate(1226, 1231)"/>
<path d=""  transform="translate(1350, 908)"/>
<path d=""  transform="translate(1933, 545)"/>
<path d=""  transform="translate(2006, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2732 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(592, 1231)"/>
<path d=""  transform="translate(592, 908)"/>
<path d=""  transform="translate(1239, 908)"/>
<path d=""  transform="translate(1226, 1231)"/>
<path d=""  transform="translate(1332, 908)"/>
<path d=""  transform="translate(1915, 545)"/>
<path d=""  transform="translate(1988, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">য়৾তৢংশঃ᳭×</span> (Added by SIESTA)</li>


<pre>Expected: yyabeng=0+626|uni09FE=0@0,323+0|tabeng=2+707|lvocalicvowelsignbeng=2@-108,0+0|anusvarabeng=2+426|shabeng=5+677|visargabeng=5+438|uni1CED=5@-386,-363+0|multiply.beng=8+592</pre>



<pre>Got     : yyabeng=0+626|uni09FE=0@0,323+0|tabeng=2+707|lvocalicvowelsignbeng=2@-108,0+0|anusvarabeng=2+438|shabeng=5+677|visargabeng=5+438|uni1CED=5@-386,-363+0|multiply.beng=8+592</pre>



<pre>                                                                                                        ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3478 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(626, 1231)"/>
<path d=""  transform="translate(626, 908)"/>
<path d=""  transform="translate(1225, 908)"/>
<path d=""  transform="translate(1333, 908)"/>
<path d=""  transform="translate(1771, 908)"/>
<path d=""  transform="translate(2448, 908)"/>
<path d=""  transform="translate(2500, 545)"/>
<path d=""  transform="translate(2886, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3466 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(626, 1231)"/>
<path d=""  transform="translate(626, 908)"/>
<path d=""  transform="translate(1225, 908)"/>
<path d=""  transform="translate(1333, 908)"/>
<path d=""  transform="translate(1759, 908)"/>
<path d=""  transform="translate(2436, 908)"/>
<path d=""  transform="translate(2488, 545)"/>
<path d=""  transform="translate(2874, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">এ꣱ংখ০॒থ᳖ৈ</span> (Added by SIESTA)</li>


<pre>Expected: ebeng=0+758|uniA8F1=0@0,323+0|uni25CC=0+510|anusvarabeng=0+389|khabeng=3+696|zerobeng=4+592|uni0952=4@-41,-313+0|thabeng=6+645|uni1CD6=6@-68,-319+0|aivowelsignbeng=6+346|uni25CC=6+510</pre>



<pre>Got     : ebeng=0+758|uniA8F1=0@0,323+0|uni25CC=0+510|anusvarabeng=0+438|khabeng=3+696|zerobeng=4+592|uni0952=4@-41,-313+0|thabeng=6+645|uni1CD6=6@-68,-319+0|aivowelsignbeng=6+346|uni25CC=6+510</pre>



<pre>                                                                       +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4495 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(758, 1231)"/>
<path d=""  transform="translate(758, 908)"/>
<path d=""  transform="translate(1268, 908)"/>
<path d=""  transform="translate(1706, 908)"/>
<path d=""  transform="translate(2402, 908)"/>
<path d=""  transform="translate(2953, 595)"/>
<path d=""  transform="translate(2994, 908)"/>
<path d=""  transform="translate(3571, 589)"/>
<path d=""  transform="translate(3639, 908)"/>
<path d=""  transform="translate(3985, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4446 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(758, 1231)"/>
<path d=""  transform="translate(758, 908)"/>
<path d=""  transform="translate(1268, 908)"/>
<path d=""  transform="translate(1657, 908)"/>
<path d=""  transform="translate(2353, 908)"/>
<path d=""  transform="translate(2904, 595)"/>
<path d=""  transform="translate(2945, 908)"/>
<path d=""  transform="translate(3522, 589)"/>
<path d=""  transform="translate(3590, 908)"/>
<path d=""  transform="translate(3936, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">েঊ꣱ড্ঞ᳒প᳒</span> (Added by SIESTA)</li>


<pre>Expected: evowelsigninibeng=0+346|uni25CC=0+510|uubeng=1+853|uniA8F1=1@0,323+0|ddahalfbeng=3+615|nyabeng=5+1001|uni1CD2=5@-237,323+0|pabeng=7+716|uni1CD2=7@-103,323+0</pre>



<pre>Got     : evowelsigninibeng=0+346|uni25CC=0+510|uubeng=1+853|uniA8F1=1@0,323+0|ddahalfbeng=3+615|nyabeng=5+1019|uni1CD2=5@-255,323+0|pabeng=7+716|uni1CD2=7@-103,323+0</pre>



<pre>                                                                                                             +              ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4059 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(346, 908)"/>
<path d=""  transform="translate(856, 908)"/>
<path d=""  transform="translate(1709, 1231)"/>
<path d=""  transform="translate(1709, 908)"/>
<path d=""  transform="translate(2324, 908)"/>
<path d=""  transform="translate(3088, 1231)"/>
<path d=""  transform="translate(3343, 908)"/>
<path d=""  transform="translate(3956, 1231)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4041 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(346, 908)"/>
<path d=""  transform="translate(856, 908)"/>
<path d=""  transform="translate(1709, 1231)"/>
<path d=""  transform="translate(1709, 908)"/>
<path d=""  transform="translate(2324, 908)"/>
<path d=""  transform="translate(3088, 1231)"/>
<path d=""  transform="translate(3325, 908)"/>
<path d=""  transform="translate(3938, 1231)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঘ॑ঞ্চওএৱ্ৡৠ</span> (Added by SIESTA)</li>


<pre>Expected: ghabeng=0+631|uni0951=0@-61,323+0|nyacabeng=2+829|obeng=5+720|ebeng=6+758|wabeng=7+596|viramabeng=7+0|llvocalicbeng=9+621|rrvocalicbeng=10+853</pre>



<pre>Got     : ghabeng=0+631|uni0951=0@-61,323+0|nyacabeng=2+847|obeng=5+738|ebeng=6+758|wabeng=7+596|viramabeng=7+0|llvocalicbeng=9+639|rrvocalicbeng=10+853</pre>



<pre>                                                         ^^          ^^                                                          ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5062 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(570, 1231)"/>
<path d=""  transform="translate(631, 908)"/>
<path d=""  transform="translate(1478, 908)"/>
<path d=""  transform="translate(2216, 908)"/>
<path d=""  transform="translate(2974, 908)"/>
<path d=""  transform="translate(3570, 908)"/>
<path d=""  transform="translate(3570, 908)"/>
<path d=""  transform="translate(4209, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5008 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(570, 1231)"/>
<path d=""  transform="translate(631, 908)"/>
<path d=""  transform="translate(1460, 908)"/>
<path d=""  transform="translate(2180, 908)"/>
<path d=""  transform="translate(2938, 908)"/>
<path d=""  transform="translate(3534, 908)"/>
<path d=""  transform="translate(3534, 908)"/>
<path d=""  transform="translate(4155, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ৠথফূংঞডুিঅ</span> (Added by SIESTA)</li>


<pre>Expected: rrvocalicbeng=0+835|thabeng=1+645|phabeng=2+838|uuvowelsignbeng=2@-221,0+0|anusvarabeng=2+403|nyabeng=5+1019|ivowelsignbeng=6+266|ddabeng=6+712|uvowelsignlongbeng=6@-106,0+0|abeng=9+893</pre>



<pre>Got     : rrvocalicbeng=0+853|thabeng=1+645|phabeng=2+838|uuvowelsignbeng=2@-221,0+0|anusvarabeng=2+438|nyabeng=5+1019|ivowelsignbeng=6+266|ddabeng=6+712|uvowelsignlongbeng=6@-106,0+0|abeng=9+893</pre>



<pre>                           +                                                                         +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5664 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(853, 908)"/>
<path d=""  transform="translate(1498, 908)"/>
<path d=""  transform="translate(2115, 908)"/>
<path d=""  transform="translate(2336, 908)"/>
<path d=""  transform="translate(2774, 908)"/>
<path d=""  transform="translate(3793, 908)"/>
<path d=""  transform="translate(4059, 908)"/>
<path d=""  transform="translate(4665, 908)"/>
<path d=""  transform="translate(4771, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5611 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(835, 908)"/>
<path d=""  transform="translate(1480, 908)"/>
<path d=""  transform="translate(2097, 908)"/>
<path d=""  transform="translate(2318, 908)"/>
<path d=""  transform="translate(2721, 908)"/>
<path d=""  transform="translate(3740, 908)"/>
<path d=""  transform="translate(4006, 908)"/>
<path d=""  transform="translate(4612, 908)"/>
<path d=""  transform="translate(4718, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">প্ঞপফ᳒ভ꣱</span> (Added by SIESTA)</li>


<pre>Expected: pahalfbeng=0+554|nyabeng=2+1001|pabeng=3+716|phabeng=4+838|uni1CD2=4@-164,323+0|bhabeng=6+721|uniA8F1=6@0,323+0</pre>



<pre>Got     : pahalfbeng=0+554|nyabeng=2+1019|pabeng=3+716|phabeng=4+838|uni1CD2=4@-164,323+0|bhabeng=6+721|uniA8F1=6@0,323+0</pre>



<pre>                                       +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3848 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(554, 908)"/>
<path d=""  transform="translate(1573, 908)"/>
<path d=""  transform="translate(2289, 908)"/>
<path d=""  transform="translate(2963, 1231)"/>
<path d=""  transform="translate(3127, 908)"/>
<path d=""  transform="translate(3848, 1231)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3830 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(554, 908)"/>
<path d=""  transform="translate(1555, 908)"/>
<path d=""  transform="translate(2271, 908)"/>
<path d=""  transform="translate(2945, 1231)"/>
<path d=""  transform="translate(3109, 908)"/>
<path d=""  transform="translate(3830, 1231)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">4৾ঀ৾ঢ্ংগঌখ</span> (Added by SIESTA)</li>


<pre>Expected: four.beng=0+551|uni09FE=0@0,323+0|uni0980=2+540|uni09FE=2@0,323+0|ddhabeng=4+567|viramabeng=4@-83,0+0|anusvarabeng=4+408|gabeng=7+656|lvocalicbeng=8+621|khabeng=9+696</pre>



<pre>Got     : four.beng=0+551|uni09FE=0@0,323+0|uni0980=2+540|uni09FE=2@0,323+0|ddhabeng=4+567|viramabeng=4@-83,0+0|anusvarabeng=4+438|gabeng=7+656|lvocalicbeng=8+639|khabeng=9+696</pre>



<pre>                                                                                                                                ^                               ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4087 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(551, 1231)"/>
<path d=""  transform="translate(551, 908)"/>
<path d=""  transform="translate(1091, 1231)"/>
<path d=""  transform="translate(1091, 908)"/>
<path d=""  transform="translate(1575, 908)"/>
<path d=""  transform="translate(1658, 908)"/>
<path d=""  transform="translate(2096, 908)"/>
<path d=""  transform="translate(2752, 908)"/>
<path d=""  transform="translate(3391, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4039 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(551, 1231)"/>
<path d=""  transform="translate(551, 908)"/>
<path d=""  transform="translate(1091, 1231)"/>
<path d=""  transform="translate(1091, 908)"/>
<path d=""  transform="translate(1575, 908)"/>
<path d=""  transform="translate(1658, 908)"/>
<path d=""  transform="translate(2066, 908)"/>
<path d=""  transform="translate(2722, 908)"/>
<path d=""  transform="translate(3343, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ড্ফ্টথ৾ৡঐ</span> (Added by SIESTA)</li>


<pre>Expected: ddahalfbeng=0+615|phattabeng=2+842|thabeng=5+645|uni09FE=5@0,323+0|llvocalicbeng=7+621|aibeng=8+873</pre>



<pre>Got     : ddahalfbeng=0+615|phattabeng=2+842|thabeng=5+645|uni09FE=5@0,323+0|llvocalicbeng=7+639|aibeng=8+873</pre>



<pre>                                                                                              ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3614 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(615, 908)"/>
<path d=""  transform="translate(1457, 908)"/>
<path d=""  transform="translate(2102, 1231)"/>
<path d=""  transform="translate(2102, 908)"/>
<path d=""  transform="translate(2741, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3596 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(615, 908)"/>
<path d=""  transform="translate(1457, 908)"/>
<path d=""  transform="translate(2102, 1231)"/>
<path d=""  transform="translate(2102, 908)"/>
<path d=""  transform="translate(2723, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঝ॑ঊ॑শ্ঞঐ</span> (Added by SIESTA)</li>


<pre>Expected: jhabeng=0+794|uni0951=0@-86,323+0|uubeng=2+853|uni0951=2@-172,323+0|shahalfbeng=4+528|nyabeng=6+1001|aibeng=7+873</pre>



<pre>Got     : jhabeng=0+794|uni0951=0@-86,323+0|uubeng=2+853|uni0951=2@-172,323+0|shahalfbeng=4+528|nyabeng=6+1019|aibeng=7+873</pre>



<pre>                                                                                                            +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4067 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(708, 1231)"/>
<path d=""  transform="translate(794, 908)"/>
<path d=""  transform="translate(1475, 1231)"/>
<path d=""  transform="translate(1647, 908)"/>
<path d=""  transform="translate(2175, 908)"/>
<path d=""  transform="translate(3194, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4049 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(708, 1231)"/>
<path d=""  transform="translate(794, 908)"/>
<path d=""  transform="translate(1475, 1231)"/>
<path d=""  transform="translate(1647, 908)"/>
<path d=""  transform="translate(2175, 908)"/>
<path d=""  transform="translate(3176, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ৠখঞ্ঝশুণ্ধৢ</span> (Added by SIESTA)</li>


<pre>Expected: rrvocalicbeng=0+835|khabeng=1+696|nyajhabeng=2+956|shubeng=5+807|nnahalfbeng=7+413|dhabeng=9+596|lvocalicvowelsignbeng=9+0</pre>



<pre>Got     : rrvocalicbeng=0+853|khabeng=1+696|nyajhabeng=2+974|shubeng=5+825|nnahalfbeng=7+413|dhabeng=9+596|lvocalicvowelsignbeng=9+0</pre>



<pre>                           +                              ^^            ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4357 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(853, 908)"/>
<path d=""  transform="translate(1549, 908)"/>
<path d=""  transform="translate(2523, 908)"/>
<path d=""  transform="translate(3348, 908)"/>
<path d=""  transform="translate(3761, 908)"/>
<path d=""  transform="translate(4357, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4303 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(835, 908)"/>
<path d=""  transform="translate(1531, 908)"/>
<path d=""  transform="translate(2487, 908)"/>
<path d=""  transform="translate(3294, 908)"/>
<path d=""  transform="translate(3707, 908)"/>
<path d=""  transform="translate(4303, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ট্এ॒ংৠ</span> (Added by SIESTA)</li>


<pre>Expected: ttabeng=0+567|viramabeng=0@-83,0+0|ebeng=2+758|uni0952=2@-124,-313+0|uni25CC=2+510|anusvarabeng=2+389|rrvocalicbeng=5+853</pre>



<pre>Got     : ttabeng=0+567|viramabeng=0@-83,0+0|ebeng=2+758|uni0952=2@-124,-313+0|uni25CC=2+510|anusvarabeng=2+438|rrvocalicbeng=5+853</pre>



<pre>                                                                                                              +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3126 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(484, 908)"/>
<path d=""  transform="translate(567, 908)"/>
<path d=""  transform="translate(1201, 595)"/>
<path d=""  transform="translate(1325, 908)"/>
<path d=""  transform="translate(1835, 908)"/>
<path d=""  transform="translate(2273, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3077 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(484, 908)"/>
<path d=""  transform="translate(567, 908)"/>
<path d=""  transform="translate(1201, 595)"/>
<path d=""  transform="translate(1325, 908)"/>
<path d=""  transform="translate(1835, 908)"/>
<path d=""  transform="translate(2224, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঘ্নঁ꣱ঞঌদৢ</span> (Added by SIESTA)</li>


<pre>Expected: ghanabeng=0+617|candrabindubeng=0+0|uniA8F1=0@0,323+0|nyabeng=5+1001|lvocalicbeng=6+639|dabeng=7+603|lvocalicvowelsignbeng=7@12,0+0</pre>



<pre>Got     : ghanabeng=0+617|candrabindubeng=0+0|uniA8F1=0@0,323+0|nyabeng=5+1019|lvocalicbeng=6+639|dabeng=7+603|lvocalicvowelsignbeng=7@12,0+0</pre>



<pre>                                                                            +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2878 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(617, 908)"/>
<path d=""  transform="translate(617, 1231)"/>
<path d=""  transform="translate(617, 908)"/>
<path d=""  transform="translate(1636, 908)"/>
<path d=""  transform="translate(2275, 908)"/>
<path d=""  transform="translate(2890, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2860 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(617, 908)"/>
<path d=""  transform="translate(617, 1231)"/>
<path d=""  transform="translate(617, 908)"/>
<path d=""  transform="translate(1618, 908)"/>
<path d=""  transform="translate(2257, 908)"/>
<path d=""  transform="translate(2872, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঢৄিভঁখ়ভ꣱ৎখ</span> (Added by SIESTA)</li>


<pre>Expected: ivowelsignbeng=0+266|ddhabeng=0+567|rrvocalicvowelsignbeng=0@-83,0+0|bhabeng=3+721|candrabindubeng=3@-165,0+0|khanuktabeng=5+696|bhabeng=7+721|uniA8F1=7@0,323+0|khandatabeng=9+507|khabeng=10+696</pre>



<pre>Got     : ivowelsignbeng=0+266|ddhabeng=0+567|rrvocalicvowelsignbeng=0@-83,0+0|bhabeng=3+721|candrabindubeng=3@-165,0+0|khanuktabeng=5+696|bhabeng=7+721|uniA8F1=7@0,323+0|khandatabeng=9+525|khabeng=10+696</pre>



<pre>                                                                                                                                                                                           ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4192 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(266, 908)"/>
<path d=""  transform="translate(750, 908)"/>
<path d=""  transform="translate(833, 908)"/>
<path d=""  transform="translate(1389, 908)"/>
<path d=""  transform="translate(1554, 908)"/>
<path d=""  transform="translate(2250, 908)"/>
<path d=""  transform="translate(2971, 1231)"/>
<path d=""  transform="translate(2971, 908)"/>
<path d=""  transform="translate(3496, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4174 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(266, 908)"/>
<path d=""  transform="translate(750, 908)"/>
<path d=""  transform="translate(833, 908)"/>
<path d=""  transform="translate(1389, 908)"/>
<path d=""  transform="translate(1554, 908)"/>
<path d=""  transform="translate(2250, 908)"/>
<path d=""  transform="translate(2971, 1231)"/>
<path d=""  transform="translate(2971, 908)"/>
<path d=""  transform="translate(3478, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ৠ᳐ৰ‍ূঋগখ꣱ত্ল</span> (Added by SIESTA)</li>


<pre>Expected: rrvocalicbeng=0+853|uni1CD0=0@-172,323+0|ruu1beng=2+769|rvocalicbeng=5+835|gabeng=6+656|khabeng=7+696|uniA8F1=7@0,323+0|talabeng=9+673</pre>



<pre>Got     : rrvocalicbeng=0+853|uni1CD0=0@-172,323+0|ruu1beng=2+769|rvocalicbeng=5+853|gabeng=6+656|khabeng=7+696|uniA8F1=7@0,323+0|talabeng=9+673</pre>



<pre>                                                                                  +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4500 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(681, 1231)"/>
<path d=""  transform="translate(853, 908)"/>
<path d=""  transform="translate(1622, 908)"/>
<path d=""  transform="translate(2475, 908)"/>
<path d=""  transform="translate(3131, 908)"/>
<path d=""  transform="translate(3827, 1231)"/>
<path d=""  transform="translate(3827, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4482 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(681, 1231)"/>
<path d=""  transform="translate(853, 908)"/>
<path d=""  transform="translate(1622, 908)"/>
<path d=""  transform="translate(2457, 908)"/>
<path d=""  transform="translate(3113, 908)"/>
<path d=""  transform="translate(3809, 1231)"/>
<path d=""  transform="translate(3809, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঙঙষ॑ংঋ</span> (Added by SIESTA)</li>


<pre>Expected: ngabeng=0+705|ngabeng=1+723|ssabeng=2+633|uni0951=2@-62,323+0|uni25CC=2+510|anusvarabeng=2+389|rvocalicbeng=5+853</pre>



<pre>Got     : ngabeng=0+723|ngabeng=1+723|ssabeng=2+633|uni0951=2@-62,323+0|uni25CC=2+510|anusvarabeng=2+438|rvocalicbeng=5+853</pre>



<pre>                     ^^                                                                                +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3880 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(723, 908)"/>
<path d=""  transform="translate(1446, 908)"/>
<path d=""  transform="translate(2017, 1231)"/>
<path d=""  transform="translate(2079, 908)"/>
<path d=""  transform="translate(2589, 908)"/>
<path d=""  transform="translate(3027, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3813 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(705, 908)"/>
<path d=""  transform="translate(1428, 908)"/>
<path d=""  transform="translate(1999, 1231)"/>
<path d=""  transform="translate(2061, 908)"/>
<path d=""  transform="translate(2571, 908)"/>
<path d=""  transform="translate(2960, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ৎঋ‘ড়ু</span> (Added by SIESTA)</li>


<pre>Expected: khandatabeng=0+507|rvocalicbeng=1+853|quoteleft.beng=2+312|rrubeng=3+712</pre>



<pre>Got     : khandatabeng=0+525|rvocalicbeng=1+853|quoteleft.beng=2+312|rrubeng=3+712</pre>



<pre>                          ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2402 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(525, 908)"/>
<path d=""  transform="translate(1378, 908)"/>
<path d=""  transform="translate(1690, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2384 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(507, 908)"/>
<path d=""  transform="translate(1360, 908)"/>
<path d=""  transform="translate(1672, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">০৾ষ্খ॑ৠঋ</span> (Added by SIESTA)</li>


<pre>Expected: zerobeng=0+592|uni09FE=0@0,323+0|ssahalfbeng=2+505|khabeng=4+696|uni0951=4@-93,323+0|rrvocalicbeng=6+835|rvocalicbeng=7+853</pre>



<pre>Got     : zerobeng=0+592|uni09FE=0@0,323+0|ssahalfbeng=2+505|khabeng=4+696|uni0951=4@-93,323+0|rrvocalicbeng=6+853|rvocalicbeng=7+853</pre>



<pre>                                                                                                                +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3499 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(592, 1231)"/>
<path d=""  transform="translate(592, 908)"/>
<path d=""  transform="translate(1097, 908)"/>
<path d=""  transform="translate(1700, 1231)"/>
<path d=""  transform="translate(1793, 908)"/>
<path d=""  transform="translate(2646, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3481 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(592, 1231)"/>
<path d=""  transform="translate(592, 908)"/>
<path d=""  transform="translate(1097, 908)"/>
<path d=""  transform="translate(1700, 1231)"/>
<path d=""  transform="translate(1793, 908)"/>
<path d=""  transform="translate(2628, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">উ᳘গ্ধুঞঌ</span> (Added by SIESTA)</li>


<pre>Expected: ubeng=0+712|uni1CD8=0@-101,-351+0|gadhabeng=2+819|uvowelsignvattubeng=2@-163,0+0|nyabeng=6+1001|lvocalicbeng=7+639</pre>



<pre>Got     : ubeng=0+712|uni1CD8=0@-101,-351+0|gadhabeng=2+819|uvowelsignvattubeng=2@-163,0+0|nyabeng=6+1019|lvocalicbeng=7+639</pre>



<pre>                                                                                                       +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3189 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(611, 557)"/>
<path d=""  transform="translate(712, 908)"/>
<path d=""  transform="translate(1368, 908)"/>
<path d=""  transform="translate(1531, 908)"/>
<path d=""  transform="translate(2550, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3171 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(611, 557)"/>
<path d=""  transform="translate(712, 908)"/>
<path d=""  transform="translate(1368, 908)"/>
<path d=""  transform="translate(1531, 908)"/>
<path d=""  transform="translate(2532, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ংথভূᳶ꣱ফ্ৰু</span> (Added by SIESTA)</li>


<pre>Expected: uni25CC=0+510|anusvarabeng=0+406|thabeng=1+645|bhabeng=2+721|uuvowelsigntallbeng=2@-115,0+0|uni1CF6=4+628|uniA8F1=4@0,323+0|pharabeng=6+899|uvowelsignlowbeng=6@-221,0+0</pre>



<pre>Got     : uni25CC=0+510|anusvarabeng=0+438|thabeng=1+645|bhabeng=2+721|uuvowelsigntallbeng=2@-115,0+0|uni1CF6=4+628|uniA8F1=4@0,323+0|pharabeng=6+899|uvowelsignlowbeng=6@-221,0+0</pre>



<pre>                                        ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3841 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(510, 908)"/>
<path d=""  transform="translate(948, 908)"/>
<path d=""  transform="translate(1593, 908)"/>
<path d=""  transform="translate(2199, 908)"/>
<path d=""  transform="translate(2314, 908)"/>
<path d=""  transform="translate(2942, 1231)"/>
<path d=""  transform="translate(2942, 908)"/>
<path d=""  transform="translate(3620, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3809 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(510, 908)"/>
<path d=""  transform="translate(916, 908)"/>
<path d=""  transform="translate(1561, 908)"/>
<path d=""  transform="translate(2167, 908)"/>
<path d=""  transform="translate(2282, 908)"/>
<path d=""  transform="translate(2910, 1231)"/>
<path d=""  transform="translate(2910, 908)"/>
<path d=""  transform="translate(3588, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ংপগৄ</span> (Added by SIESTA)</li>


<pre>Expected: uni25CC=0+510|anusvarabeng=0+406|pabeng=1+716|gabeng=2+656|rrvocalicvowelsignbeng=2+0</pre>



<pre>Got     : uni25CC=0+510|anusvarabeng=0+438|pabeng=1+716|gabeng=2+656|rrvocalicvowelsignbeng=2+0</pre>



<pre>                                        ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2320 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(510, 908)"/>
<path d=""  transform="translate(948, 908)"/>
<path d=""  transform="translate(1664, 908)"/>
<path d=""  transform="translate(2320, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2288 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(510, 908)"/>
<path d=""  transform="translate(916, 908)"/>
<path d=""  transform="translate(1632, 908)"/>
<path d=""  transform="translate(2288, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">এঋর‍ূ</span> (Added by SIESTA)</li>


<pre>Expected: ebeng=0+740|rvocalicbeng=1+853|ruubeng=2+769</pre>



<pre>Got     : ebeng=0+758|rvocalicbeng=1+853|ruubeng=2+769</pre>



<pre>                   ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2380 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(758, 908)"/>
<path d=""  transform="translate(1611, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2362 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(740, 908)"/>
<path d=""  transform="translate(1593, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ফ্অ꣱ংধএ᳘</span> (Added by SIESTA)</li>


<pre>Expected: phabeng=0+838|viramabeng=0@-221,0+0|abeng=2+893|uniA8F1=2@0,323+0|uni25CC=2+510|anusvarabeng=2+394|dhabeng=5+596|ebeng=6+758|uni1CD8=6@-124,-351+0</pre>



<pre>Got     : phabeng=0+838|viramabeng=0@-221,0+0|abeng=2+893|uniA8F1=2@0,323+0|uni25CC=2+510|anusvarabeng=2+438|dhabeng=5+596|ebeng=6+758|uni1CD8=6@-124,-351+0</pre>



<pre>                                                                                                         ++
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4033 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(617, 908)"/>
<path d=""  transform="translate(838, 908)"/>
<path d=""  transform="translate(1731, 1231)"/>
<path d=""  transform="translate(1731, 908)"/>
<path d=""  transform="translate(2241, 908)"/>
<path d=""  transform="translate(2679, 908)"/>
<path d=""  transform="translate(3275, 908)"/>
<path d=""  transform="translate(3909, 557)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3989 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(617, 908)"/>
<path d=""  transform="translate(838, 908)"/>
<path d=""  transform="translate(1731, 1231)"/>
<path d=""  transform="translate(1731, 908)"/>
<path d=""  transform="translate(2241, 908)"/>
<path d=""  transform="translate(2635, 908)"/>
<path d=""  transform="translate(3231, 908)"/>
<path d=""  transform="translate(3865, 557)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">৬᳖ঙ্মৢৢ꣱ক</span> (Added by SIESTA)</li>


<pre>Expected: sixbeng=0+592|uni1CD6=0@-41,-319+0|ngamabeng=2+918|lvocalicvowelsignbeng=2@225,0+0|lvocalicvowelsignbeng=2+0|uniA8F1=2@0,323+0|kabeng=8+807</pre>



<pre>Got     : sixbeng=0+592|uni1CD6=0@-41,-319+0|ngamabeng=2+918|lvocalicvowelsignbeng=2+0|lvocalicvowelsignbeng=2+0|uniA8F1=2@0,323+0|kabeng=8+807</pre>



<pre>                                                                                    ++++++
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2317 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(551, 589)"/>
<path d=""  transform="translate(592, 908)"/>
<path d=""  transform="translate(1510, 908)"/>
<path d=""  transform="translate(1510, 908)"/>
<path d=""  transform="translate(1510, 1231)"/>
<path d=""  transform="translate(1510, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2317 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(551, 589)"/>
<path d=""  transform="translate(592, 908)"/>
<path d=""  transform="translate(1735, 908)"/>
<path d=""  transform="translate(1510, 908)"/>
<path d=""  transform="translate(1510, 1231)"/>
<path d=""  transform="translate(1510, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ক্ষ/৾ঙএ</span> (Added by SIESTA)</li>


<pre>Expected: kassabeng=0+919|slash.beng=3+449|uni25CC=3+510|uni09FE=3+0|ngabeng=5+705|ebeng=6+758</pre>



<pre>Got     : kassabeng=0+919|slash.beng=3+449|uni25CC=3+510|uni09FE=3+0|ngabeng=5+723|ebeng=6+758</pre>



<pre>                                                                                ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3359 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(919, 908)"/>
<path d=""  transform="translate(1368, 908)"/>
<path d=""  transform="translate(1878, 908)"/>
<path d=""  transform="translate(1878, 908)"/>
<path d=""  transform="translate(2601, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3341 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(919, 908)"/>
<path d=""  transform="translate(1368, 908)"/>
<path d=""  transform="translate(1878, 908)"/>
<path d=""  transform="translate(1878, 908)"/>
<path d=""  transform="translate(2583, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ᳶৈফেঙ᳒২꣱এৠ</span> (Added by SIESTA)</li>


<pre>Expected: aivowelsigninibeng=0+346|uni1CF6=0+628|evowelsignbeng=2+346|phabeng=2+838|ngabeng=4+723|uni1CD2=4@-107,323+0|twobeng=6+592|uniA8F1=6@0,323+0|ebeng=8+740|rrvocalicbeng=9+853</pre>



<pre>Got     : aivowelsigninibeng=0+346|uni1CF6=0+628|evowelsignbeng=2+346|phabeng=2+838|ngabeng=4+723|uni1CD2=4@-107,323+0|twobeng=6+592|uniA8F1=6@0,323+0|ebeng=8+758|rrvocalicbeng=9+853</pre>



<pre>                                                                                                                                                                ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5084 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(346, 908)"/>
<path d=""  transform="translate(974, 908)"/>
<path d=""  transform="translate(1320, 908)"/>
<path d=""  transform="translate(2158, 908)"/>
<path d=""  transform="translate(2774, 1231)"/>
<path d=""  transform="translate(2881, 908)"/>
<path d=""  transform="translate(3473, 1231)"/>
<path d=""  transform="translate(3473, 908)"/>
<path d=""  transform="translate(4231, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5066 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(346, 908)"/>
<path d=""  transform="translate(974, 908)"/>
<path d=""  transform="translate(1320, 908)"/>
<path d=""  transform="translate(2158, 908)"/>
<path d=""  transform="translate(2774, 1231)"/>
<path d=""  transform="translate(2881, 908)"/>
<path d=""  transform="translate(3473, 1231)"/>
<path d=""  transform="translate(3473, 908)"/>
<path d=""  transform="translate(4213, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ক্ক᳭ূঌপয্</span> (Added by SIESTA)</li>


<pre>Expected: kakabeng=0+766|uni1CED=0@-94,-363+0|uni25CC=0+510|uuvowelsignbeng=0+0|lvocalicbeng=5+621|pabeng=6+716|yabeng=7+626|viramabeng=7+0</pre>



<pre>Got     : kakabeng=0+766|uni1CED=0@-94,-363+0|uni25CC=0+510|uuvowelsignbeng=0+0|lvocalicbeng=5+639|pabeng=6+716|yabeng=7+626|viramabeng=7+0</pre>



<pre>                                                                                                ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3257 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(672, 545)"/>
<path d=""  transform="translate(766, 908)"/>
<path d=""  transform="translate(1276, 908)"/>
<path d=""  transform="translate(1276, 908)"/>
<path d=""  transform="translate(1915, 908)"/>
<path d=""  transform="translate(2631, 908)"/>
<path d=""  transform="translate(3257, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3239 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(672, 545)"/>
<path d=""  transform="translate(766, 908)"/>
<path d=""  transform="translate(1276, 908)"/>
<path d=""  transform="translate(1276, 908)"/>
<path d=""  transform="translate(1897, 908)"/>
<path d=""  transform="translate(2613, 908)"/>
<path d=""  transform="translate(3239, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">7৾ল্তৣ৫ু꣱</span> (Added by SIESTA)</li>


<pre>Expected: seven.beng=0+551|uni09FE=0@0,323+0|latasquishbeng=2+724|llvocalicvowelsignbeng=2@104,0+0|fivebeng=6+592|uvowelsignbeng=6+0|uniA8F1=6@0,323+0</pre>



<pre>Got     : seven.beng=0+551|uni09FE=0@0,323+0|latasquishbeng=2+724|llvocalicvowelsignbeng=2@-33,0+0|fivebeng=6+592|uvowelsignbeng=6+0|uniA8F1=6@0,323+0</pre>



<pre>                                                                                           ^^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1867 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(551, 1231)"/>
<path d=""  transform="translate(551, 908)"/>
<path d=""  transform="translate(1242, 908)"/>
<path d=""  transform="translate(1275, 908)"/>
<path d=""  transform="translate(1867, 908)"/>
<path d=""  transform="translate(1867, 1231)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1867 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(551, 1231)"/>
<path d=""  transform="translate(551, 908)"/>
<path d=""  transform="translate(1379, 908)"/>
<path d=""  transform="translate(1275, 908)"/>
<path d=""  transform="translate(1867, 908)"/>
<path d=""  transform="translate(1867, 1231)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঞওহ᳭ণ্ন্</span> (Added by SIESTA)</li>


<pre>Expected: nyabeng=0+1001|obeng=1+738|habeng=2+530|uni1CED=2@-10,-363+0|nnanabeng=4+603|viramabeng=4+0</pre>



<pre>Got     : nyabeng=0+1019|obeng=1+738|habeng=2+530|uni1CED=2@-10,-363+0|nnanabeng=4+603|viramabeng=4+0</pre>



<pre>                      +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2890 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(1019, 908)"/>
<path d=""  transform="translate(1757, 908)"/>
<path d=""  transform="translate(2277, 545)"/>
<path d=""  transform="translate(2287, 908)"/>
<path d=""  transform="translate(2890, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2872 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(1001, 908)"/>
<path d=""  transform="translate(1739, 908)"/>
<path d=""  transform="translate(2259, 545)"/>
<path d=""  transform="translate(2269, 908)"/>
<path d=""  transform="translate(2872, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">উ᳕ঞথহ্ন</span> (Added by SIESTA)</li>


<pre>Expected: ubeng=0+712|uni1CD5=0@-101,-313+0|nyabeng=2+1001|thabeng=3+645|hanabeng=4+751</pre>



<pre>Got     : ubeng=0+712|uni1CD5=0@-101,-313+0|nyabeng=2+1019|thabeng=3+645|hanabeng=4+751</pre>



<pre>                                                        +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3127 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(611, 595)"/>
<path d=""  transform="translate(712, 908)"/>
<path d=""  transform="translate(1731, 908)"/>
<path d=""  transform="translate(2376, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3109 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(611, 595)"/>
<path d=""  transform="translate(712, 908)"/>
<path d=""  transform="translate(1713, 908)"/>
<path d=""  transform="translate(2358, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">টীঋৎ</span> (Added by SIESTA)</li>


<pre>Expected: ttiibeng=0+833|rvocalicbeng=2+835|khandatabeng=3+525</pre>



<pre>Got     : ttiibeng=0+833|rvocalicbeng=2+853|khandatabeng=3+525</pre>



<pre>                                         +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2211 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(833, 908)"/>
<path d=""  transform="translate(1686, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2193 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(833, 908)"/>
<path d=""  transform="translate(1668, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">এধষ্টৃঁম়১॑</span> (Added by SIESTA)</li>


<pre>Expected: ebeng=0+740|dhabeng=1+596|ssattabeng=2+565|rvocalicvowelsignbeng=2@-58,0+0|candrabindualtbeng=2+0|manuktabeng=7+622|onebeng=9+592|uni0951=9@-41,323+0</pre>



<pre>Got     : ebeng=0+758|dhabeng=1+596|ssattabeng=2+565|rvocalicvowelsignbeng=2@-58,0+0|candrabindualtbeng=2+0|manuktabeng=7+622|onebeng=9+592|uni0951=9@-41,323+0</pre>



<pre>                   ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3133 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(758, 908)"/>
<path d=""  transform="translate(1354, 908)"/>
<path d=""  transform="translate(1861, 908)"/>
<path d=""  transform="translate(1919, 908)"/>
<path d=""  transform="translate(1919, 908)"/>
<path d=""  transform="translate(2541, 908)"/>
<path d=""  transform="translate(3092, 1231)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3115 2325" transform="matrix(1 0 0 -1 0 0)">
<path d=""  transform="translate(0, 908)"/>
<path d=""  transform="translate(740, 908)"/>
<path d=""  transform="translate(1336, 908)"/>
<path d=""  transform="translate(1843, 908)"/>
<path d=""  transform="translate(1901, 908)"/>
<path d=""  transform="translate(1901, 908)"/>
<path d=""  transform="translate(2523, 908)"/>
<path d=""  transform="translate(3074, 1231)"/>
</svg>


</div> [code: shaping-regression]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* sharabeng
	* gadhabeng
	* ngakarabeng
	* kababeng
	* ra1nuktahalfbeng
	* cacabeng
	* satarabeng
	* ssamabeng
	* marasquishbeng
	* mababeng and 194 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dhanuktahalfbeng

	- kanuktahalfbeng

	- canuktahalfbeng 

	- And 22 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 648 but it should be 697 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* exclam.beng (U+0021): X=252.5,Y=2.0 (should be at baseline 0?)

	* exclam.beng (U+0021): X=165.0,Y=2.0 (should be at baseline 0?)

	* comma.beng (U+002C): X=73.5,Y=2.0 (should be at baseline 0?)

	* period.beng (U+002E): X=177.5,Y=2.0 (should be at baseline 0?)

	* period.beng (U+002E): X=90.0,Y=2.0 (should be at baseline 0?)

	* three.beng (U+0033): X=128.5,Y=-1.5 (should be at baseline 0?)

	* three.beng (U+0033): X=344.5,Y=620.5 (should be at cap-height 622?)

	* five.beng (U+0035): X=142.0,Y=-0.5 (should be at baseline 0?)

	* nine.beng (U+0039): X=106.0,Y=-1.0 (should be at baseline 0?)

	* nine.beng (U+0039): X=349.5,Y=621.5 (should be at cap-height 622?) 

	* And 20 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* two.beng (U+0032) contains a short segment L<<156.0,85.0>--<156.0,81.0>>

	* abeng (U+0985) contains a short segment B<<353.0,372.0>-<353.0,365.0>-<355.0,353.0>>

	* abeng (U+0985) contains a short segment B<<355.0,353.0>-<357.0,341.0>-<361.0,331.0>>

	* aabeng (U+0986) contains a short segment B<<353.0,372.0>-<353.0,365.0>-<355.0,353.0>>

	* aabeng (U+0986) contains a short segment B<<355.0,353.0>-<357.0,341.0>-<361.0,331.0>>

	* aabeng (U+0986) contains a short segment B<<274.5,354.5>-<271.0,372.0>-<271.0,388.0>>

	* aabeng (U+0986) contains a short segment L<<898.0,622.0>--<898.0,622.0>>

	* aabeng (U+0986) contains a short segment B<<990.0,559.0>-<989.0,564.0>-<987.5,582.0>>

	* aabeng (U+0986) contains a short segment B<<987.5,582.0>-<986.0,600.0>-<986.0,613.0>>

	* ibeng (U+0987) contains a short segment B<<-10.0,859.0>-<-10.0,872.0>-<-8.5,885.0>> 

	* And 68 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<898.0,622.0>> -> L<<898.0,622.0>--<898.0,622.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* mabeng (U+09AE): L<<450.0,551.0>--<116.0,551.0>>/B<<116.0,551.0>-<199.0,540.0>-<246.5,489.5>> = 7.549421768263246 

	* And sabeng (U+09B8): L<<510.0,551.0>--<107.0,551.0>>/B<<107.0,551.0>-<183.0,540.0>-<226.5,518.0>> = 8.235619324209488 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[19] NotoSansBengali-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali SemiBold [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 995, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CED

	- uuvowelsignbeng

	- rrvocalicvowelsignbeng

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD5

	- uni1CD6

	- uni1CD8

	- uni0952 

	- And 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* shabeng
	* sharabeng
	* gadhabeng
	* ngakarabeng
	* kababeng
	* dadhabeng
	* babhabeng
	* jhahalfbeng
	* uni1CF6
	* ra1nuktahalfbeng and 316 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dhanuktahalfbeng

	- kanuktahalfbeng

	- canuktahalfbeng 

	- And 22 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 672 but it should be 724 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* comma.beng (U+002C): X=185.5,Y=1.0 (should be at baseline 0?)

	* zero.beng (U+0030): X=275.0,Y=620.0 (should be at cap-height 622?)

	* three.beng (U+0033): X=125.0,Y=-0.5 (should be at baseline 0?)

	* three.beng (U+0033): X=249.0,Y=620.0 (should be at cap-height 622?)

	* five.beng (U+0035): X=132.5,Y=-0.5 (should be at baseline 0?)

	* nine.beng (U+0039): X=90.0,Y=-2.0 (should be at baseline 0?)

	* semicolon.beng (U+003B): X=188.5,Y=1.0 (should be at baseline 0?)

	* question.beng (U+003F): X=259.0,Y=620.0 (should be at cap-height 622?)

	* uni0951 (U+0951): X=-210.0,Y=624.0 (should be at cap-height 622?)

	* uni0951 (U+0951): X=-299.0,Y=624.0 (should be at cap-height 622?) 

	* And 11 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* two.beng (U+0032) contains a short segment L<<201.0,116.0>--<201.0,110.0>>

	* aabeng (U+0986) contains a short segment B<<279.0,334.5>-<275.0,352.0>-<275.0,367.0>>

	* aabeng (U+0986) contains a short segment B<<1027.0,559.0>-<1026.0,564.0>-<1024.5,582.0>>

	* aabeng (U+0986) contains a short segment B<<1024.5,582.0>-<1023.0,600.0>-<1023.0,613.0>>

	* ibeng (U+0987) contains a short segment B<<177.0,348.0>-<177.0,342.0>-<179.0,334.5>>

	* ibeng (U+0987) contains a short segment B<<179.0,334.5>-<181.0,327.0>-<183.0,321.0>>

	* iibeng (U+0988) contains a short segment B<<179.0,187.5>-<193.0,176.0>-<211.0,176.0>>

	* iibeng (U+0988) contains a short segment B<<173.5,387.0>-<161.0,375.0>-<161.0,357.0>>

	* iibeng (U+0988) contains a short segment B<<153.0,905.0>-<150.0,884.0>-<150.0,873.0>>

	* iibeng (U+0988) contains a short segment B<<154.5,834.5>-<159.0,818.0>-<170.0,807.0>> 

	* And 70 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* aabeng (U+0986): B<<990.0,607.5>-<1011.0,593.0>-<1027.0,559.0>>/B<<1027.0,559.0>-<1026.0,564.0>-<1024.5,582.0>> = 13.891191171454844

	* aavowelsignbeng (U+09BE): B<<54.0,608.5>-<76.0,595.0>-<93.0,559.0>>/B<<93.0,559.0>-<91.0,564.0>-<90.0,582.0>> = 3.4763127492009898 

	* And ovowelsignbeng (U+09CB): B<<744.0,608.5>-<766.0,595.0>-<783.0,559.0>>/B<<783.0,559.0>-<781.0,564.0>-<780.0,582.0>> = 3.4763127492009898 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[20] NotoSansBengali-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali Thin [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 995, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CED

	- uuvowelsignbeng

	- rrvocalicvowelsignbeng

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD5

	- uni1CD6

	- uni1CD8

	- uni0952 

	- And 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* cacabeng
	* cachababeng
	* cacharabeng and cachabeng
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali Thin' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dhanuktahalfbeng

	- kanuktahalfbeng

	- canuktahalfbeng 

	- And 22 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 606 but it should be 652 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* exclam.beng (U+0021): X=199.5,Y=1.0 (should be at baseline 0?)

	* exclam.beng (U+0021): X=157.0,Y=1.0 (should be at baseline 0?)

	* period.beng (U+002E): X=125.5,Y=1.0 (should be at baseline 0?)

	* period.beng (U+002E): X=83.0,Y=1.0 (should be at baseline 0?)

	* three.beng (U+0033): X=129.5,Y=-1.0 (should be at baseline 0?)

	* five.beng (U+0035): X=155.5,Y=2.0 (should be at baseline 0?)

	* nine.beng (U+0039): X=107.0,Y=-2.0 (should be at baseline 0?)

	* colon.beng (U+003A): X=96.0,Y=1.0 (should be at baseline 0?)

	* colon.beng (U+003A): X=138.5,Y=1.0 (should be at baseline 0?)

	* question.beng (U+003F): X=171.0,Y=1.0 (should be at baseline 0?) 

	* And 30 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<848.0,622.0>> -> L<<848.0,622.0>--<848.0,622.0>>

	* rrvocalicbeng (U+09E0): L<<484.0,676.0>--<489.0,622.0>> -> L<<489.0,622.0>--<489.0,318.0>>

	* rrvocalicbeng (U+09E0): L<<677.0,676.0>--<682.0,622.0>> -> L<<682.0,622.0>--<682.0,72.0>>

	* rvocalicbeng (U+098B): L<<484.0,676.0>--<489.0,622.0>> -> L<<489.0,622.0>--<489.0,318.0>> 

	* And rvocalicbeng (U+098B): L<<677.0,676.0>--<682.0,622.0>> -> L<<682.0,622.0>--<682.0,72.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* chabeng (U+099B): B<<500.5,178.5>-<433.0,122.0>-<312.0,117.0>>/B<<312.0,117.0>-<473.0,95.0>-<642.0,-1.0>> = 10.147294214439293

	* ghabeng (U+0998): B<<164.5,329.0>-<209.0,363.0>-<255.0,389.0>>/B<<255.0,389.0>-<243.0,384.0>-<230.5,381.5>> = 6.856024055205275

	* mabeng (U+09AE): L<<449.0,596.0>--<51.0,596.0>>/B<<51.0,596.0>-<136.0,582.0>-<179.0,547.5>> = 9.352979250093227

	* sabeng (U+09B8): L<<517.0,596.0>--<44.0,596.0>>/B<<44.0,596.0>-<113.0,582.0>-<160.5,564.0>> = 11.469530332866904 

	* And twobeng (U+09E8): B<<252.0,187.0>-<242.0,187.0>-<233.0,188.0>>/B<<233.0,188.0>-<313.0,158.0>-<390.0,105.5>> = 14.21585347367354 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* exclam.beng (U+0021): L<<167.0,174.0>--<165.0,714.0>> 

	* And exclam.beng (U+0021): L<<193.0,714.0>--<191.0,174.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[18] NotoSansBengaliUI-Black.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali UI Black [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CD6

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD8

	- uni0952

	- uni1CED

	- uuvowelsignbeng

	- viramabeng

	- uni0951 

	- And 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali UI Black' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- uvowelsignvattuUIbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dabasquishbeng

	- uuvowelsignvattuUIbeng 

	- And 34 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 717 but it should be 776 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 llvocalicvowelsignUIbeng (U+09E3), lvocalicvowelsignUIbeng (U+09E2) and rrvocalicvowelsignUIbeng (U+09C4) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* bracketleft.beng (U+005B): X=283.0,Y=-1.0 (should be at baseline 0?)

	* bracketleft.beng (U+005B): X=380.0,Y=-1.0 (should be at baseline 0?)

	* bracketright.beng (U+005D): X=71.0,Y=-1.0 (should be at baseline 0?)

	* bracketright.beng (U+005D): X=168.0,Y=-1.0 (should be at baseline 0?)

	* braceright.beng (U+007D): X=322.0,Y=624.0 (should be at cap-height 622?)

	* uni0951 (U+0951): X=-200.0,Y=623.0 (should be at cap-height 622?)

	* uni0951 (U+0951): X=-310.0,Y=623.0 (should be at cap-height 622?)

	* ngabeng (U+0999): X=249.0,Y=623.0 (should be at cap-height 622?)

	* nyabeng (U+099E): X=916.0,Y=620.0 (should be at cap-height 622?)

	* dhabeng (U+09A7): X=314.0,Y=623.0 (should be at cap-height 622?) 

	* And 10 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* aabeng (U+0986): B<<1058.5,609.0>-<1078.0,596.0>-<1089.0,566.0>>/B<<1089.0,566.0>-<1087.0,580.0>-<1086.0,598.5>> = 12.006201074092134

	* aavowelsignbeng (U+09BE): B<<48.5,609.0>-<68.0,596.0>-<79.0,566.0>>/B<<79.0,566.0>-<77.0,580.0>-<76.0,598.5>> = 12.006201074092134 

	* And ovowelsignbeng (U+09CB): B<<740.5,609.0>-<760.0,596.0>-<771.0,566.0>>/B<<771.0,566.0>-<769.0,580.0>-<768.0,598.5>> = 12.006201074092134 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[17] NotoSansBengaliUI-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali UI [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CD6

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD8

	- uni0952

	- uni1CED

	- uuvowelsignbeng

	- viramabeng

	- uni0951 

	- And 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- uvowelsignvattuUIbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dabasquishbeng

	- uuvowelsignvattuUIbeng 

	- And 34 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 687 but it should be 741 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 llvocalicvowelsignUIbeng (U+09E3), lvocalicvowelsignUIbeng (U+09E2) and rrvocalicvowelsignUIbeng (U+09C4) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* five.beng (U+0035): X=127.0,Y=-0.5 (should be at baseline 0?)

	* uni0951 (U+0951): X=-205.0,Y=623.0 (should be at cap-height 622?)

	* uni0951 (U+0951): X=-305.0,Y=623.0 (should be at cap-height 622?)

	* uni0980 (U+0980): X=445.0,Y=621.0 (should be at cap-height 622?)

	* ngabeng (U+0999): X=210.0,Y=623.0 (should be at cap-height 622?)

	* dhabeng (U+09A7): X=299.0,Y=624.0 (should be at cap-height 622?)

	* shabeng (U+09B6): X=-12.0,Y=620.0 (should be at cap-height 622?)

	* evowelsignbeng (U+09C7): X=353.0,Y=1.5 (should be at baseline 0?)

	* aivowelsignbeng (U+09C8): X=353.0,Y=1.5 (should be at baseline 0?)

	* ovowelsignbeng (U+09CB): X=353.0,Y=1.5 (should be at baseline 0?) 

	* And 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* aabeng (U+0986): B<<1014.5,608.0>-<1034.0,594.0>-<1050.0,559.0>>/B<<1050.0,559.0>-<1049.0,564.0>-<1047.5,582.0>> = 13.257238846581073

	* aavowelsignbeng (U+09BE): B<<53.0,610.0>-<73.0,598.0>-<90.0,559.0>>/B<<90.0,559.0>-<89.0,564.0>-<87.5,582.0>> = 12.242331198874426 

	* And ovowelsignbeng (U+09CB): B<<745.0,610.0>-<765.0,598.0>-<782.0,559.0>>/B<<782.0,559.0>-<781.0,564.0>-<779.5,582.0>> = 12.242331198874426 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[19] NotoSansBengaliUI-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali UI ExtraBold [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CD6

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD8

	- uni0952

	- uni1CED

	- uuvowelsignbeng

	- viramabeng

	- uni0951 

	- And 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali UI ExtraBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- uvowelsignvattuUIbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dabasquishbeng

	- uuvowelsignvattuUIbeng 

	- And 34 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 701 but it should be 757 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 llvocalicvowelsignUIbeng (U+09E3), lvocalicvowelsignUIbeng (U+09E2) and rrvocalicvowelsignUIbeng (U+09C4) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* five.beng (U+0035): X=131.0,Y=-0.5 (should be at baseline 0?)

	* braceleft.beng (U+007B): X=430.0,Y=-2.0 (should be at baseline 0?)

	* uni0951 (U+0951): X=-203.0,Y=623.0 (should be at cap-height 622?)

	* uni0951 (U+0951): X=-307.0,Y=623.0 (should be at cap-height 622?)

	* aabeng (U+0986): X=1064.0,Y=621.0 (should be at cap-height 622?)

	* ngabeng (U+0999): X=452.0,Y=2.0 (should be at baseline 0?)

	* ngabeng (U+0999): X=228.0,Y=623.0 (should be at cap-height 622?)

	* ngabeng (U+0999): X=452.0,Y=2.0 (should be at baseline 0?)

	* dhabeng (U+09A7): X=306.0,Y=624.0 (should be at cap-height 622?)

	* rabeng (U+09B0): X=112.0,Y=0.5 (should be at baseline 0?) 

	* And 10 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* two.beng (U+0032) contains a short segment L<<249.0,147.0>--<249.0,141.0>>

	* aabeng (U+0986) contains a short segment B<<469.0,356.0>-<451.0,356.0>-<440.5,346.0>>

	* aabeng (U+0986) contains a short segment B<<440.5,346.0>-<430.0,336.0>-<430.0,321.0>>

	* aabeng (U+0986) contains a short segment B<<430.0,321.0>-<430.0,307.0>-<436.0,289.0>>

	* aabeng (U+0986) contains a short segment B<<285.5,310.0>-<281.0,330.0>-<281.0,345.0>>

	* aabeng (U+0986) contains a short segment B<<1068.0,562.0>-<1066.0,571.0>-<1065.0,589.5>>

	* aabeng (U+0986) contains a short segment B<<1065.0,589.5>-<1064.0,608.0>-<1064.0,621.0>>

	* ibeng (U+0987) contains a short segment B<<212.0,317.0>-<212.0,304.0>-<218.0,293.0>>

	* ibeng (U+0987) contains a short segment B<<142.0,904.0>-<141.0,895.0>-<140.0,888.0>>

	* ibeng (U+0987) contains a short segment B<<140.0,888.0>-<139.0,881.0>-<139.0,876.0>> 

	* And 88 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* aabeng (U+0986): B<<1034.5,608.5>-<1054.0,595.0>-<1068.0,562.0>>/B<<1068.0,562.0>-<1066.0,571.0>-<1065.0,589.5>> = 10.459909092929111

	* aavowelsignbeng (U+09BE): B<<50.5,609.5>-<70.0,597.0>-<85.0,562.0>>/B<<85.0,562.0>-<83.0,571.0>-<82.0,589.5>> = 10.66978280449666 

	* And ovowelsignbeng (U+09CB): B<<742.5,609.5>-<762.0,597.0>-<777.0,562.0>>/B<<777.0,562.0>-<775.0,571.0>-<774.0,589.5>> = 10.66978280449666 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[20] NotoSansBengaliUI-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali UI ExtraLight [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CD6

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD8

	- uni0952

	- uni1CED

	- uuvowelsignbeng

	- viramabeng

	- uni0951 

	- And 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali UI ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- uvowelsignvattuUIbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dabasquishbeng

	- uuvowelsignvattuUIbeng 

	- And 34 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 614 but it should be 661 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 llvocalicvowelsignUIbeng (U+09E3), lvocalicvowelsignUIbeng (U+09E2) and rrvocalicvowelsignUIbeng (U+09C4) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* exclam.beng (U+0021): X=210.5,Y=1.5 (should be at baseline 0?)

	* exclam.beng (U+0021): X=158.5,Y=1.5 (should be at baseline 0?)

	* period.beng (U+002E): X=136.0,Y=1.5 (should be at baseline 0?)

	* period.beng (U+002E): X=84.5,Y=1.5 (should be at baseline 0?)

	* two.beng (U+0032): X=91.0,Y=623.0 (should be at cap-height 622?)

	* three.beng (U+0033): X=129.0,Y=-1.5 (should be at baseline 0?)

	* five.beng (U+0035): X=152.5,Y=1.5 (should be at baseline 0?)

	* nine.beng (U+0039): X=107.0,Y=-2.0 (should be at baseline 0?)

	* colon.beng (U+003A): X=97.5,Y=1.5 (should be at baseline 0?)

	* colon.beng (U+003A): X=149.0,Y=1.5 (should be at baseline 0?) 

	* And 14 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* two.beng (U+0032) contains a short segment L<<102.0,39.0>--<102.0,37.0>>

	* abeng (U+0985) contains a short segment B<<311.0,398.0>-<311.0,385.0>-<313.0,371.0>>

	* aabeng (U+0986) contains a short segment B<<311.0,398.0>-<311.0,385.0>-<313.0,371.0>>

	* aabeng (U+0986) contains a short segment B<<313.0,371.0>-<315.0,357.0>-<323.0,341.0>>

	* aabeng (U+0986) contains a short segment B<<287.0,332.0>-<280.0,349.0>-<276.5,367.5>>

	* aabeng (U+0986) contains a short segment B<<276.5,367.5>-<273.0,386.0>-<273.0,402.0>>

	* aabeng (U+0986) contains a short segment L<<-10.0,587.0>--<-10.0,622.0>>

	* aabeng (U+0986) contains a short segment L<<858.0,622.0>--<858.0,622.0>>

	* aabeng (U+0986) contains a short segment B<<954.0,549.0>-<953.0,559.0>-<952.5,577.0>>

	* aabeng (U+0986) contains a short segment B<<952.5,577.0>-<952.0,595.0>-<952.0,613.0>> 

	* And 66 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<858.0,622.0>> -> L<<858.0,622.0>--<858.0,622.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* chabeng (U+099B): B<<514.0,177.5>-<450.0,123.0>-<343.0,114.0>>/B<<343.0,114.0>-<493.0,89.0>-<651.0,1.0>> = 14.27027617105606

	* mabeng (U+09AE): L<<449.0,587.0>--<64.0,587.0>>/B<<64.0,587.0>-<143.0,574.0>-<185.0,541.5>> = 9.344671902099696 

	* And sabeng (U+09B8): L<<516.0,587.0>--<57.0,587.0>>/B<<57.0,587.0>-<145.0,570.0>-<197.5,544.5>> = 10.933816785755795 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[20] NotoSansBengaliUI-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali UI Light [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CD6

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD8

	- uni0952

	- uni1CED

	- uuvowelsignbeng

	- viramabeng

	- uni0951 

	- And 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali UI Light' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- uvowelsignvattuUIbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dabasquishbeng

	- uuvowelsignvattuUIbeng 

	- And 34 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 627 but it should be 675 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 llvocalicvowelsignUIbeng (U+09E3), lvocalicvowelsignUIbeng (U+09E2) and rrvocalicvowelsignUIbeng (U+09C4) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* three.beng (U+0033): X=129.0,Y=-1.5 (should be at baseline 0?)

	* five.beng (U+0035): X=148.5,Y=0.5 (should be at baseline 0?)

	* nine.beng (U+0039): X=107.0,Y=-1.0 (should be at baseline 0?)

	* braceleft.beng (U+007B): X=180.0,Y=2.0 (should be at baseline 0?)

	* ngabeng (U+0999): X=162.0,Y=623.0 (should be at cap-height 622?)

	* shabeng (U+09B6): X=-7.0,Y=620.0 (should be at cap-height 622?)

	* evowelsignbeng (U+09C7): X=312.5,Y=1.0 (should be at baseline 0?)

	* aivowelsignbeng (U+09C8): X=312.5,Y=1.0 (should be at baseline 0?)

	* ovowelsignbeng (U+09CB): X=312.5,Y=1.0 (should be at baseline 0?)

	* auvowelsignbeng (U+09CC): X=312.5,Y=1.0 (should be at baseline 0?) 

	* And 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* two.beng (U+0032) contains a short segment L<<122.0,56.0>--<122.0,54.0>>

	* abeng (U+0985) contains a short segment B<<327.0,389.0>-<327.0,377.0>-<329.0,364.0>>

	* aabeng (U+0986) contains a short segment B<<327.0,389.0>-<327.0,377.0>-<329.0,364.0>>

	* aabeng (U+0986) contains a short segment B<<329.0,364.0>-<331.0,351.0>-<337.0,337.0>>

	* aabeng (U+0986) contains a short segment L<<873.0,622.0>--<873.0,622.0>>

	* aabeng (U+0986) contains a short segment B<<968.0,553.0>-<966.0,561.0>-<965.5,579.0>>

	* aabeng (U+0986) contains a short segment B<<965.5,579.0>-<965.0,597.0>-<965.0,613.0>>

	* aabeng (U+0986) contains a short segment L<<965.0,682.0>--<1001.0,682.0>>

	* ibeng (U+0987) contains a short segment B<<48.0,909.0>-<46.0,896.0>-<45.0,885.5>>

	* ibeng (U+0987) contains a short segment B<<45.0,885.5>-<44.0,875.0>-<44.0,866.0>> 

	* And 42 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<873.0,622.0>> -> L<<873.0,622.0>--<873.0,622.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* mabeng (U+09AE): L<<450.0,574.0>--<82.0,574.0>>/B<<82.0,574.0>-<187.0,558.0>-<229.5,500.0>> = 8.664135433108044 

	* And sabeng (U+09B8): L<<514.0,574.0>--<75.0,574.0>>/B<<75.0,574.0>-<159.0,558.0>-<208.0,534.0>> = 10.784297867562596 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[19] NotoSansBengaliUI-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali UI Medium [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CD6

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD8

	- uni0952

	- uni1CED

	- uuvowelsignbeng

	- viramabeng

	- uni0951 

	- And 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali UI Medium' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- uvowelsignvattuUIbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dabasquishbeng

	- uuvowelsignvattuUIbeng 

	- And 34 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 659 but it should be 710 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 llvocalicvowelsignUIbeng (U+09E3), lvocalicvowelsignUIbeng (U+09E2) and rrvocalicvowelsignUIbeng (U+09C4) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* three.beng (U+0033): X=127.0,Y=-1.0 (should be at baseline 0?)

	* five.beng (U+0035): X=138.0,Y=-0.5 (should be at baseline 0?)

	* nine.beng (U+0039): X=99.0,Y=-2.0 (should be at baseline 0?)

	* question.beng (U+003F): X=178.5,Y=620.5 (should be at cap-height 622?)

	* lvocalicbeng (U+098C): X=164.5,Y=620.0 (should be at cap-height 622?)

	* ngabeng (U+0999): X=188.0,Y=623.0 (should be at cap-height 622?)

	* dhabeng (U+09A7): X=295.0,Y=624.0 (should be at cap-height 622?)

	* shabeng (U+09B6): X=-10.0,Y=620.0 (should be at cap-height 622?)

	* llvocalicUIbeng (U+09E1): X=164.5,Y=620.0 (should be at cap-height 622?)

	* eightbeng (U+09EE): X=35.0,Y=623.0 (should be at cap-height 622?) 

	* And 4 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* two.beng (U+0032) contains a short segment L<<177.0,99.0>--<177.0,95.0>>

	* aabeng (U+0986) contains a short segment B<<276.5,345.0>-<273.0,363.0>-<273.0,378.0>>

	* aabeng (U+0986) contains a short segment B<<1008.0,559.0>-<1006.0,564.0>-<1005.0,582.0>>

	* aabeng (U+0986) contains a short segment B<<1005.0,582.0>-<1004.0,600.0>-<1004.0,613.0>>

	* ibeng (U+0987) contains a short segment B<<-9.0,858.0>-<-9.0,871.0>-<-8.0,884.0>>

	* ibeng (U+0987) contains a short segment B<<-8.0,884.0>-<-7.0,897.0>-<-4.0,912.0>>

	* ibeng (U+0987) contains a short segment B<<162.0,360.0>-<162.0,352.0>-<164.0,344.0>>

	* ibeng (U+0987) contains a short segment B<<164.0,344.0>-<166.0,336.0>-<168.0,330.0>>

	* iibeng (U+0988) contains a short segment B<<60.5,351.0>-<57.0,370.0>-<57.0,385.0>>

	* iibeng (U+0988) contains a short segment B<<44.0,858.0>-<44.0,871.0>-<45.5,884.0>> 

	* And 62 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* aabeng (U+0986): B<<968.5,607.0>-<991.0,592.0>-<1008.0,559.0>>/B<<1008.0,559.0>-<1006.0,564.0>-<1005.0,582.0>> = 5.453918888591197

	* mabeng (U+09AE): L<<443.0,539.0>--<157.0,539.0>>/B<<157.0,539.0>-<228.0,521.0>-<265.0,472.0>> = 14.22596389875178 

	* And sabeng (U+09B8): L<<504.0,539.0>--<143.0,539.0>>/B<<143.0,539.0>-<204.0,527.0>-<240.0,506.5>> = 11.129189289611167 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[19] NotoSansBengaliUI-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali UI [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CD6

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD8

	- uni0952

	- uni1CED

	- uuvowelsignbeng

	- viramabeng

	- uni0951 

	- And 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- uvowelsignvattuUIbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dabasquishbeng

	- uuvowelsignvattuUIbeng 

	- And 34 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 648 but it should be 697 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 llvocalicvowelsignUIbeng (U+09E3), lvocalicvowelsignUIbeng (U+09E2) and rrvocalicvowelsignUIbeng (U+09C4) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* exclam.beng (U+0021): X=252.5,Y=2.0 (should be at baseline 0?)

	* exclam.beng (U+0021): X=165.0,Y=2.0 (should be at baseline 0?)

	* comma.beng (U+002C): X=73.5,Y=2.0 (should be at baseline 0?)

	* period.beng (U+002E): X=177.5,Y=2.0 (should be at baseline 0?)

	* period.beng (U+002E): X=90.0,Y=2.0 (should be at baseline 0?)

	* three.beng (U+0033): X=128.5,Y=-1.5 (should be at baseline 0?)

	* three.beng (U+0033): X=344.5,Y=620.5 (should be at cap-height 622?)

	* five.beng (U+0035): X=142.0,Y=-0.5 (should be at baseline 0?)

	* nine.beng (U+0039): X=106.0,Y=-1.0 (should be at baseline 0?)

	* nine.beng (U+0039): X=349.5,Y=621.5 (should be at cap-height 622?) 

	* And 21 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* two.beng (U+0032) contains a short segment L<<156.0,85.0>--<156.0,81.0>>

	* abeng (U+0985) contains a short segment B<<353.0,372.0>-<353.0,365.0>-<355.0,353.0>>

	* abeng (U+0985) contains a short segment B<<355.0,353.0>-<357.0,341.0>-<361.0,331.0>>

	* aabeng (U+0986) contains a short segment B<<353.0,372.0>-<353.0,365.0>-<355.0,353.0>>

	* aabeng (U+0986) contains a short segment B<<355.0,353.0>-<357.0,341.0>-<361.0,331.0>>

	* aabeng (U+0986) contains a short segment B<<274.5,354.5>-<271.0,372.0>-<271.0,388.0>>

	* aabeng (U+0986) contains a short segment L<<898.0,622.0>--<898.0,622.0>>

	* aabeng (U+0986) contains a short segment B<<990.0,559.0>-<989.0,564.0>-<987.5,582.0>>

	* aabeng (U+0986) contains a short segment B<<987.5,582.0>-<986.0,600.0>-<986.0,613.0>>

	* ibeng (U+0987) contains a short segment B<<-10.0,859.0>-<-10.0,872.0>-<-8.5,885.0>> 

	* And 74 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<898.0,622.0>> -> L<<898.0,622.0>--<898.0,622.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* mabeng (U+09AE): L<<450.0,551.0>--<116.0,551.0>>/B<<116.0,551.0>-<199.0,540.0>-<246.5,489.5>> = 7.549421768263246 

	* And sabeng (U+09B8): L<<510.0,551.0>--<107.0,551.0>>/B<<107.0,551.0>-<183.0,540.0>-<226.5,518.0>> = 8.235619324209488 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[19] NotoSansBengaliUI-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali UI SemiBold [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CD6

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD8

	- uni0952

	- uni1CED

	- uuvowelsignbeng

	- viramabeng

	- uni0951 

	- And 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali UI SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- uvowelsignvattuUIbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dabasquishbeng

	- uuvowelsignvattuUIbeng 

	- And 34 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 672 but it should be 724 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 llvocalicvowelsignUIbeng (U+09E3), lvocalicvowelsignUIbeng (U+09E2) and rrvocalicvowelsignUIbeng (U+09C4) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* comma.beng (U+002C): X=185.5,Y=1.0 (should be at baseline 0?)

	* zero.beng (U+0030): X=275.0,Y=620.0 (should be at cap-height 622?)

	* three.beng (U+0033): X=125.0,Y=-0.5 (should be at baseline 0?)

	* three.beng (U+0033): X=249.0,Y=620.0 (should be at cap-height 622?)

	* five.beng (U+0035): X=132.5,Y=-0.5 (should be at baseline 0?)

	* nine.beng (U+0039): X=90.0,Y=-2.0 (should be at baseline 0?)

	* semicolon.beng (U+003B): X=188.5,Y=1.0 (should be at baseline 0?)

	* question.beng (U+003F): X=259.0,Y=620.0 (should be at cap-height 622?)

	* uni0951 (U+0951): X=-210.0,Y=624.0 (should be at cap-height 622?)

	* uni0951 (U+0951): X=-299.0,Y=624.0 (should be at cap-height 622?) 

	* And 11 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* two.beng (U+0032) contains a short segment L<<201.0,116.0>--<201.0,110.0>>

	* aabeng (U+0986) contains a short segment B<<279.0,334.5>-<275.0,352.0>-<275.0,367.0>>

	* aabeng (U+0986) contains a short segment B<<1027.0,559.0>-<1026.0,564.0>-<1024.5,582.0>>

	* aabeng (U+0986) contains a short segment B<<1024.5,582.0>-<1023.0,600.0>-<1023.0,613.0>>

	* ibeng (U+0987) contains a short segment B<<177.0,348.0>-<177.0,342.0>-<179.0,334.5>>

	* ibeng (U+0987) contains a short segment B<<179.0,334.5>-<181.0,327.0>-<183.0,321.0>>

	* iibeng (U+0988) contains a short segment B<<179.0,187.5>-<193.0,176.0>-<211.0,176.0>>

	* iibeng (U+0988) contains a short segment B<<173.5,387.0>-<161.0,375.0>-<161.0,357.0>>

	* iibeng (U+0988) contains a short segment B<<153.0,905.0>-<150.0,884.0>-<150.0,873.0>>

	* iibeng (U+0988) contains a short segment B<<154.5,834.5>-<159.0,818.0>-<170.0,807.0>> 

	* And 76 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* aabeng (U+0986): B<<990.0,607.5>-<1011.0,593.0>-<1027.0,559.0>>/B<<1027.0,559.0>-<1026.0,564.0>-<1024.5,582.0>> = 13.891191171454844

	* aavowelsignbeng (U+09BE): B<<54.0,608.5>-<76.0,595.0>-<93.0,559.0>>/B<<93.0,559.0>-<91.0,564.0>-<90.0,582.0>> = 3.4763127492009898 

	* And ovowelsignbeng (U+09CB): B<<744.0,608.5>-<766.0,595.0>-<783.0,559.0>>/B<<783.0,559.0>-<781.0,564.0>-<780.0,582.0>> = 3.4763127492009898 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[20] NotoSansBengaliUI-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0030 (DIGIT ZERO)


	- 0x0031 (DIGIT ONE)


	- 0x0032 (DIGIT TWO)


	- 0x0033 (DIGIT THREE)


	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0038 (DIGIT EIGHT)


	- 0x0039 (DIGIT NINE)
 

	- And 321 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font can render its own name. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/render_own_name">com.google.fonts/check/render_own_name</a>)</summary><div>


* 🔥 **FAIL** .notdef glyphs were found when attempting to render Noto Sans Bengali UI Thin [code: render-own-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CD6

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD8

	- uni0952

	- uni1CED

	- uuvowelsignbeng

	- viramabeng

	- uni0951 

	- And 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali UI Thin' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- danuktahalfbeng

	- nyanuktahalfbeng

	- uvowelsignvattuUIbeng

	- chanuktahalfbeng

	- nganuktahalfbeng

	- ra1nuktahalfbeng

	- dhahalfbeng

	- jhanuktahalfbeng

	- dabasquishbeng

	- uuvowelsignvattuUIbeng 

	- And 34 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- And Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 606 but it should be 652 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 llvocalicvowelsignUIbeng (U+09E3), lvocalicvowelsignUIbeng (U+09E2) and rrvocalicvowelsignUIbeng (U+09C4) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* exclam.beng (U+0021): X=199.5,Y=1.0 (should be at baseline 0?)

	* exclam.beng (U+0021): X=157.0,Y=1.0 (should be at baseline 0?)

	* period.beng (U+002E): X=125.5,Y=1.0 (should be at baseline 0?)

	* period.beng (U+002E): X=83.0,Y=1.0 (should be at baseline 0?)

	* three.beng (U+0033): X=129.5,Y=-1.0 (should be at baseline 0?)

	* five.beng (U+0035): X=155.5,Y=2.0 (should be at baseline 0?)

	* nine.beng (U+0039): X=107.0,Y=-2.0 (should be at baseline 0?)

	* colon.beng (U+003A): X=96.0,Y=1.0 (should be at baseline 0?)

	* colon.beng (U+003A): X=138.5,Y=1.0 (should be at baseline 0?)

	* question.beng (U+003F): X=171.0,Y=1.0 (should be at baseline 0?) 

	* And 27 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<848.0,622.0>> -> L<<848.0,622.0>--<848.0,622.0>>

	* llvocalicvowelsignUIbeng (U+09E3): L<<-161.0,-164.0>--<-161.0,-164.0>> -> L<<-161.0,-164.0>--<-161.0,-164.0>>

	* rrvocalicbeng (U+09E0): L<<484.0,676.0>--<489.0,622.0>> -> L<<489.0,622.0>--<489.0,318.0>>

	* rrvocalicbeng (U+09E0): L<<677.0,676.0>--<682.0,622.0>> -> L<<682.0,622.0>--<682.0,72.0>>

	* rvocalicbeng (U+098B): L<<484.0,676.0>--<489.0,622.0>> -> L<<489.0,622.0>--<489.0,318.0>> 

	* And rvocalicbeng (U+098B): L<<677.0,676.0>--<682.0,622.0>> -> L<<682.0,622.0>--<682.0,72.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* chabeng (U+099B): B<<500.5,178.5>-<433.0,122.0>-<312.0,117.0>>/B<<312.0,117.0>-<473.0,95.0>-<642.0,-1.0>> = 10.147294214439293

	* ghabeng (U+0998): B<<164.5,329.0>-<209.0,363.0>-<255.0,389.0>>/B<<255.0,389.0>-<243.0,384.0>-<230.5,381.5>> = 6.856024055205275

	* mabeng (U+09AE): L<<449.0,596.0>--<51.0,596.0>>/B<<51.0,596.0>-<136.0,582.0>-<179.0,547.5>> = 9.352979250093227

	* sabeng (U+09B8): L<<517.0,596.0>--<44.0,596.0>>/B<<44.0,596.0>-<113.0,582.0>-<160.5,564.0>> = 11.469530332866904 

	* And twobeng (U+09E8): B<<252.0,187.0>-<242.0,187.0>-<233.0,188.0>>/B<<233.0,188.0>-<313.0,158.0>-<390.0,105.5>> = 14.21585347367354 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* exclam.beng (U+0021): L<<167.0,174.0>--<165.0,714.0>> 

	* And exclam.beng (U+0021): L<<193.0,714.0>--<191.0,174.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[13] NotoSansBengali[wdth,wght].ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x00AF (MACRON)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
</div></details><details><summary>🔥 <b>FAIL:</b> Copyright notices match canonical pattern in fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright">com.google.fonts/check/font_copyright</a>)</summary><div>


* 🔥 **FAIL** Name Table entry: Copyright notices should match a pattern similar to: "Copyright 2019 The Familyname Project Authors (git url)"
But instead we have got:
"Copyright 2017-2022 Google Inc. All Rights Reserved." [code: bad-notice-format]
</div></details><details><summary>🔥 <b>FAIL:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics">com.google.fonts/check/os2/use_typo_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/NotoSansBengali/googlefonts/slim-variable-ttf/NotoSansBengali[wght].ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengali-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Black.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Bold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-ExtraLight.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Light.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Medium.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Regular.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-SemiBold.ttf', 'fonts/NotoSansBengali/googlefonts/ttf/NotoSansBengaliUI-Thin.ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf/NotoSansBengali[wdth,wght].ttf']. [code: missing-os2-fsselection-bit7]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 995, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- uni1CED

	- uuvowelsignbeng

	- rrvocalicvowelsignbeng

	- uni1CD0

	- uni1CD2

	- rvocalicvowelsignbeng

	- uni1CD5

	- uni1CD6

	- uni1CD8

	- uni0952 

	- And 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: unattached-dotted-circle-marks]
</div></details><details><summary>🔥 <b>FAIL:</b> Validates that when an instance record is included for the default instance, its subfamilyNameID value is set to either 2 or 17, and its postScriptNameID value is set to 6. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/valid_default_instance_nameids">com.adobe.fonts/check/varfont/valid_default_instance_nameids</a>)</summary><div>


* 🔥 **FAIL** 'Regular' instance has the same coordinates as the default instance; its subfamilyNameID should be either 2 or 17, instead of 292. [code: invalid-default-instance-subfamily-nameid:292]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- ra1nuktahalfbeng

	- dhahalfbeng

	- uuvowelsignvattuUIbeng

	- dhanuktahalfbeng

	- one

	- kanuktahalfbeng

	- canuktahalfbeng

	- shanuktahalfbeng

	- asciitilde

	- phanuktahalfbeng 

	- And 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1), uni1CE1.UI (unencoded) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 acutecomb (U+0301), gravecomb (U+0300), tildecomb (U+0303), uni0302 (U+0302), uni0304 (U+0304), uni0306 (U+0306), uni0307 (U+0307), uni0308 (U+0308), uni030A (U+030A), uni030B (U+030B) and 5 more.

Use -F or --full-lists to disable shortening of long lists. [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 169 | 208 | 2265 | 140 | 1633 | 0 |
| 0% | 4% | 5% | 51% | 3% | 37% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
