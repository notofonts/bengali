## Fontbakery report

Fontbakery version: 0.8.11

<details><summary><b>[5] Family checks</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking all files are in the same directory. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/single_directory">com.google.fonts/check/family/single_directory</a>)</summary><div>


* 🔥 **FAIL** Not all fonts passed in the command line are in the same directory. This may lead to bad results as the tool will interpret all font files as belonging to a single font family. The detected directories are: ['fonts/NotoSansBengali/googlefonts/ttf', 'fonts/NotoSansBengali/googlefonts/variable-ttf'] [code: single-directory]
</div></details><details><summary>🔥 <b>FAIL:</b> Each font in a family must have the same set of vertical metrics values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/vertical_metrics">com.google.fonts/check/family/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** sTypoAscender is not the same across the family:
Noto Sans Bengali Black: 917
Noto Sans Bengali Bold: 917
Noto Sans Bengali ExtraBold: 917
Noto Sans Bengali ExtraLight: 917
Noto Sans Bengali Light: 917
Noto Sans Bengali Medium: 917
Noto Sans Bengali: 917
Noto Sans Bengali SemiBold: 917
Noto Sans Bengali Thin: 917
Noto Sans Bengali UI Black: 1069
Noto Sans Bengali UI Bold: 1069
Noto Sans Bengali UI ExtraBold: 1069
Noto Sans Bengali UI ExtraLight: 1069
Noto Sans Bengali UI Light: 1069
Noto Sans Bengali UI Medium: 1069
Noto Sans Bengali UI: 1069
Noto Sans Bengali UI SemiBold: 1069
Noto Sans Bengali UI Thin: 1069 [code: sTypoAscender-mismatch]
* 🔥 **FAIL** sTypoDescender is not the same across the family:
Noto Sans Bengali Black: -408
Noto Sans Bengali Bold: -408
Noto Sans Bengali ExtraBold: -408
Noto Sans Bengali ExtraLight: -408
Noto Sans Bengali Light: -408
Noto Sans Bengali Medium: -408
Noto Sans Bengali: -408
Noto Sans Bengali SemiBold: -408
Noto Sans Bengali Thin: -408
Noto Sans Bengali UI Black: -293
Noto Sans Bengali UI Bold: -293
Noto Sans Bengali UI ExtraBold: -293
Noto Sans Bengali UI ExtraLight: -293
Noto Sans Bengali UI Light: -293
Noto Sans Bengali UI Medium: -293
Noto Sans Bengali UI: -293
Noto Sans Bengali UI SemiBold: -293
Noto Sans Bengali UI Thin: -293 [code: sTypoDescender-mismatch]
* 🔥 **FAIL** usWinAscent is not the same across the family:
Noto Sans Bengali Black: 917
Noto Sans Bengali Bold: 917
Noto Sans Bengali ExtraBold: 917
Noto Sans Bengali ExtraLight: 917
Noto Sans Bengali Light: 917
Noto Sans Bengali Medium: 917
Noto Sans Bengali: 917
Noto Sans Bengali SemiBold: 917
Noto Sans Bengali Thin: 917
Noto Sans Bengali UI Black: 1069
Noto Sans Bengali UI Bold: 1069
Noto Sans Bengali UI ExtraBold: 1069
Noto Sans Bengali UI ExtraLight: 1069
Noto Sans Bengali UI Light: 1069
Noto Sans Bengali UI Medium: 1069
Noto Sans Bengali UI: 1069
Noto Sans Bengali UI SemiBold: 1069
Noto Sans Bengali UI Thin: 1069 [code: usWinAscent-mismatch]
* 🔥 **FAIL** usWinDescent is not the same across the family:
Noto Sans Bengali Black: 408
Noto Sans Bengali Bold: 408
Noto Sans Bengali ExtraBold: 408
Noto Sans Bengali ExtraLight: 408
Noto Sans Bengali Light: 408
Noto Sans Bengali Medium: 408
Noto Sans Bengali: 408
Noto Sans Bengali SemiBold: 408
Noto Sans Bengali Thin: 408
Noto Sans Bengali UI Black: 293
Noto Sans Bengali UI Bold: 293
Noto Sans Bengali UI ExtraBold: 293
Noto Sans Bengali UI ExtraLight: 293
Noto Sans Bengali UI Light: 293
Noto Sans Bengali UI Medium: 293
Noto Sans Bengali UI: 293
Noto Sans Bengali UI SemiBold: 293
Noto Sans Bengali UI Thin: 293 [code: usWinDescent-mismatch]
* 🔥 **FAIL** ascent is not the same across the family:
Noto Sans Bengali Black: 917
Noto Sans Bengali Bold: 917
Noto Sans Bengali ExtraBold: 917
Noto Sans Bengali ExtraLight: 917
Noto Sans Bengali Light: 917
Noto Sans Bengali Medium: 917
Noto Sans Bengali: 917
Noto Sans Bengali SemiBold: 917
Noto Sans Bengali Thin: 917
Noto Sans Bengali UI Black: 1069
Noto Sans Bengali UI Bold: 1069
Noto Sans Bengali UI ExtraBold: 1069
Noto Sans Bengali UI ExtraLight: 1069
Noto Sans Bengali UI Light: 1069
Noto Sans Bengali UI Medium: 1069
Noto Sans Bengali UI: 1069
Noto Sans Bengali UI SemiBold: 1069
Noto Sans Bengali UI Thin: 1069 [code: ascent-mismatch]
* 🔥 **FAIL** descent is not the same across the family:
Noto Sans Bengali Black: -408
Noto Sans Bengali Bold: -408
Noto Sans Bengali ExtraBold: -408
Noto Sans Bengali ExtraLight: -408
Noto Sans Bengali Light: -408
Noto Sans Bengali Medium: -408
Noto Sans Bengali: -408
Noto Sans Bengali SemiBold: -408
Noto Sans Bengali Thin: -408
Noto Sans Bengali UI Black: -293
Noto Sans Bengali UI Bold: -293
Noto Sans Bengali UI ExtraBold: -293
Noto Sans Bengali UI ExtraLight: -293
Noto Sans Bengali UI Light: -293
Noto Sans Bengali UI Medium: -293
Noto Sans Bengali UI: -293
Noto Sans Bengali UI SemiBold: -293
Noto Sans Bengali UI Thin: -293 [code: descent-mismatch]
</div></details><details><summary>🔥 <b>FAIL:</b> Fonts have consistent PANOSE proportion? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/family/panose_proportion">com.google.fonts/check/family/panose_proportion</a>)</summary><div>


* 🔥 **FAIL** PANOSE proportion is not the same across this family. In order to fix this, please make sure that the panose.bProportion value is the same in the OS/2 table of all of this family font files. [code: inconsistency]
</div></details><details><summary>🔥 <b>FAIL:</b> Fonts have consistent PANOSE family type? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/family/panose_familytype">com.google.fonts/check/family/panose_familytype</a>)</summary><div>


* 🔥 **FAIL** PANOSE family type is not the same across this family. In order to fix this, please make sure that the panose.bFamilyType value is the same in the OS/2 table of all of this family font files. [code: inconsistency]
</div></details><details><summary>🔥 <b>FAIL:</b> Check that OS/2.fsSelection bold & italic settings are unique for each NameID1 (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.adobe.fonts/check/family/bold_italic_unique_for_nameid1">com.adobe.fonts/check/family/bold_italic_unique_for_nameid1</a>)</summary><div>


* 🔥 **FAIL** Family 'Noto Sans Bengali' has 2 fonts (should be no more than 1) with the same OS/2.fsSelection bold & italic settings: Bold=False, Italic=False [code: unique-fsselection]
</div></details><br></div></details><details><summary><b>[14] NotoSansBengali-Black.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1012, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* aabeng
	* abeng
	* aibeng
	* aubeng
	* auvowelwavebeng
	* bababeng
	* babhabeng
	* badabeng
	* badarabeng
	* badhabeng and 393 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali Black' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1), uni1CE1.UI (unencoded) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* V (U+0056): B<<339.5,236.0>-<346.0,204.0>-<347.0,184.0>>/B<<347.0,184.0>-<349.0,204.0>-<354.5,235.5>> = 8.57299836361137

	* W (U+0057): B<<308.0,211.5>-<313.0,185.0>-<315.0,167.0>>/B<<315.0,167.0>-<319.0,197.0>-<325.5,236.0>> = 13.934835114501363

	* W (U+0057): B<<527.0,442.0>-<523.0,468.0>-<521.0,486.0>>/B<<521.0,486.0>-<519.0,468.0>-<514.5,442.0>> = 12.680383491819825

	* W (U+0057): B<<714.0,235.0>-<721.0,196.0>-<724.0,167.0>>/B<<724.0,167.0>-<727.0,192.0>-<734.0,229.0>> = 12.748914526401432

	* Wacute (U+1E82): B<<308.0,211.5>-<313.0,185.0>-<315.0,167.0>>/B<<315.0,167.0>-<319.0,197.0>-<325.5,236.0>> = 13.934835114501363

	* Wacute (U+1E82): B<<527.0,442.0>-<523.0,468.0>-<521.0,486.0>>/B<<521.0,486.0>-<519.0,468.0>-<514.5,442.0>> = 12.680383491819825

	* Wacute (U+1E82): B<<714.0,235.0>-<721.0,196.0>-<724.0,167.0>>/B<<724.0,167.0>-<727.0,192.0>-<734.0,229.0>> = 12.748914526401432

	* Wcircumflex (U+0174): B<<308.0,211.5>-<313.0,185.0>-<315.0,167.0>>/B<<315.0,167.0>-<319.0,197.0>-<325.5,236.0>> = 13.934835114501363

	* Wcircumflex (U+0174): B<<527.0,442.0>-<523.0,468.0>-<521.0,486.0>>/B<<521.0,486.0>-<519.0,468.0>-<514.5,442.0>> = 12.680383491819825

	* Wcircumflex (U+0174): B<<714.0,235.0>-<721.0,196.0>-<724.0,167.0>>/B<<724.0,167.0>-<727.0,192.0>-<734.0,229.0>> = 12.748914526401432 

	* 9 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[14] NotoSansBengali-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1012, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* aabeng
	* abeng
	* aibeng
	* aubeng
	* auvowelwavebeng
	* bababeng
	* babhabeng
	* badabeng
	* badarabeng
	* badhabeng and 352 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1), uni1CE1.UI (unencoded) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* five.beng (U+0035): X=127.0,Y=-0.5 (should be at baseline 0?)

	* C (U+0043): X=482.0,Y=-1.0 (should be at baseline 0?)

	* G (U+0047): X=527.5,Y=1.0 (should be at baseline 0?)

	* c (U+0063): X=394.5,Y=-0.5 (should be at baseline 0?)

	* e (U+0065): X=432.5,Y=-0.5 (should be at baseline 0?)

	* g (U+0067): X=555.0,Y=-1.0 (should be at baseline 0?)

	* h (U+0068): X=295.0,Y=537.0 (should be at x-height 536?)

	* m (U+006D): X=288.5,Y=537.0 (should be at x-height 536?)

	* m (U+006D): X=481.0,Y=536.5 (should be at x-height 536?)

	* m (U+006D): X=627.5,Y=537.0 (should be at x-height 536?) 

	* 60 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* W (U+0057): B<<266.0,196.0>-<272.0,161.0>-<275.0,137.0>>/B<<275.0,137.0>-<278.0,162.0>-<284.0,196.5>> = 13.967789761532726

	* W (U+0057): B<<489.0,505.5>-<485.0,529.0>-<483.0,542.0>>/B<<483.0,542.0>-<482.0,529.0>-<477.5,505.5>> = 13.144867617550734

	* W (U+0057): B<<683.0,196.0>-<689.0,161.0>-<692.0,137.0>>/B<<692.0,137.0>-<695.0,162.0>-<701.0,196.5>> = 13.967789761532726

	* Wacute (U+1E82): B<<266.0,196.0>-<272.0,161.0>-<275.0,137.0>>/B<<275.0,137.0>-<278.0,162.0>-<284.0,196.5>> = 13.967789761532726

	* Wacute (U+1E82): B<<489.0,505.5>-<485.0,529.0>-<483.0,542.0>>/B<<483.0,542.0>-<482.0,529.0>-<477.5,505.5>> = 13.144867617550734

	* Wacute (U+1E82): B<<683.0,196.0>-<689.0,161.0>-<692.0,137.0>>/B<<692.0,137.0>-<695.0,162.0>-<701.0,196.5>> = 13.967789761532726

	* Wcircumflex (U+0174): B<<266.0,196.0>-<272.0,161.0>-<275.0,137.0>>/B<<275.0,137.0>-<278.0,162.0>-<284.0,196.5>> = 13.967789761532726

	* Wcircumflex (U+0174): B<<489.0,505.5>-<485.0,529.0>-<483.0,542.0>>/B<<483.0,542.0>-<482.0,529.0>-<477.5,505.5>> = 13.144867617550734

	* Wcircumflex (U+0174): B<<683.0,196.0>-<689.0,161.0>-<692.0,137.0>>/B<<692.0,137.0>-<695.0,162.0>-<701.0,196.5>> = 13.967789761532726

	* Wdieresis (U+1E84): B<<266.0,196.0>-<272.0,161.0>-<275.0,137.0>>/B<<275.0,137.0>-<278.0,162.0>-<284.0,196.5>> = 13.967789761532726 

	* 8 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[14] NotoSansBengali-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1012, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* aabeng
	* abeng
	* aibeng
	* aubeng
	* auvowelwavebeng
	* bababeng
	* babhabeng
	* badabeng
	* badarabeng
	* badhabeng and 375 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali ExtraBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1), uni1CE1.UI (unencoded) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* V (U+0056): B<<326.0,209.5>-<333.0,177.0>-<335.0,156.0>>/B<<335.0,156.0>-<338.0,177.0>-<344.5,209.0>> = 13.570434385161475

	* W (U+0057): B<<283.5,211.5>-<290.0,175.0>-<293.0,151.0>>/B<<293.0,151.0>-<297.0,183.0>-<305.0,226.5>> = 14.25003269780357

	* W (U+0057): B<<506.5,475.5>-<502.0,500.0>-<501.0,516.0>>/B<<501.0,516.0>-<499.0,500.0>-<494.5,475.5>> = 10.701350723899111

	* Wacute (U+1E82): B<<283.5,211.5>-<290.0,175.0>-<293.0,151.0>>/B<<293.0,151.0>-<297.0,183.0>-<305.0,226.5>> = 14.25003269780357

	* Wacute (U+1E82): B<<506.5,475.5>-<502.0,500.0>-<501.0,516.0>>/B<<501.0,516.0>-<499.0,500.0>-<494.5,475.5>> = 10.701350723899111

	* Wcircumflex (U+0174): B<<283.5,211.5>-<290.0,175.0>-<293.0,151.0>>/B<<293.0,151.0>-<297.0,183.0>-<305.0,226.5>> = 14.25003269780357

	* Wcircumflex (U+0174): B<<506.5,475.5>-<502.0,500.0>-<501.0,516.0>>/B<<501.0,516.0>-<499.0,500.0>-<494.5,475.5>> = 10.701350723899111

	* Wdieresis (U+1E84): B<<283.5,211.5>-<290.0,175.0>-<293.0,151.0>>/B<<293.0,151.0>-<297.0,183.0>-<305.0,226.5>> = 14.25003269780357

	* Wdieresis (U+1E84): B<<506.5,475.5>-<502.0,500.0>-<501.0,516.0>>/B<<501.0,516.0>-<499.0,500.0>-<494.5,475.5>> = 10.701350723899111

	* Wgrave (U+1E80): B<<283.5,211.5>-<290.0,175.0>-<293.0,151.0>>/B<<293.0,151.0>-<297.0,183.0>-<305.0,226.5>> = 14.25003269780357 

	* 4 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[16] NotoSansBengali-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1012, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* badabeng
	* badarabeng
	* cacabeng
	* cachababeng
	* cachabeng
	* cacharabeng
	* hababeng
	* kassamabeng
	* kassannabeng
	* kassarabeng and 7 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1), uni1CE1.UI (unencoded) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
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

	* 79 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<858.0,622.0>> -> L<<858.0,622.0>--<858.0,622.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* chabeng (U+099B): B<<514.0,177.5>-<450.0,123.0>-<343.0,114.0>>/B<<343.0,114.0>-<493.0,89.0>-<651.0,1.0>> = 14.27027617105606

	* mabeng (U+09AE): L<<449.0,587.0>--<64.0,587.0>>/B<<64.0,587.0>-<143.0,574.0>-<185.0,541.5>> = 9.344671902099696 

	* sabeng (U+09B8): L<<516.0,587.0>--<57.0,587.0>>/B<<57.0,587.0>-<145.0,570.0>-<197.5,544.5>> = 10.933816785755795 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[16] NotoSansBengali-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1012, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* badabeng
	* badarabeng
	* cacabeng
	* cachababeng
	* cachabeng
	* cacharabeng
	* canyabeng
	* dhamabeng
	* hababeng
	* hamabeng and 48 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali Light' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1), uni1CE1.UI (unencoded) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* three.beng (U+0033): X=129.0,Y=-1.5 (should be at baseline 0?)

	* five.beng (U+0035): X=148.5,Y=0.5 (should be at baseline 0?)

	* nine.beng (U+0039): X=107.0,Y=-1.0 (should be at baseline 0?)

	* C (U+0043): X=491.0,Y=-2.0 (should be at baseline 0?)

	* N (U+004E): X=153.0,Y=624.0 (should be at cap-height 622?)

	* N (U+004E): X=150.0,Y=624.0 (should be at cap-height 622?)

	* Q (U+0051): X=478.0,Y=2.0 (should be at baseline 0?)

	* S (U+0053): X=136.0,Y=-1.0 (should be at baseline 0?)

	* c (U+0063): X=385.0,Y=535.0 (should be at x-height 536?)

	* e (U+0065): X=395.0,Y=-2.0 (should be at baseline 0?) 

	* 57 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<873.0,622.0>> -> L<<873.0,622.0>--<873.0,622.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* mabeng (U+09AE): L<<450.0,574.0>--<82.0,574.0>>/B<<82.0,574.0>-<187.0,558.0>-<229.5,500.0>> = 8.664135433108044 

	* sabeng (U+09B8): L<<514.0,574.0>--<75.0,574.0>>/B<<75.0,574.0>-<159.0,558.0>-<208.0,534.0>> = 10.784297867562596 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[14] NotoSansBengali-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1012, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* aabeng
	* abeng
	* bababeng
	* babhabeng
	* badabeng
	* badarabeng
	* badhabeng
	* barabeng
	* barasquishbeng
	* barubeng and 256 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali Medium' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1), uni1CE1.UI (unencoded) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* aabeng (U+0986): B<<968.5,607.0>-<991.0,592.0>-<1008.0,559.0>>/B<<1008.0,559.0>-<1006.0,564.0>-<1005.0,582.0>> = 5.453918888591197

	* mabeng (U+09AE): L<<443.0,539.0>--<157.0,539.0>>/B<<157.0,539.0>-<228.0,521.0>-<265.0,472.0>> = 14.22596389875178 

	* sabeng (U+09B8): L<<504.0,539.0>--<143.0,539.0>>/B<<143.0,539.0>-<204.0,527.0>-<240.0,506.5>> = 11.129189289611167 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[15] NotoSansBengali-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1012, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
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

<li>Shaping did not match: <span class="tf">ত্ত্র</span> (Issue #6)</li>


<pre>Expected: ttarabeng=0+675</pre>



<pre>Got     : tatarabeng=0+723</pre>



<pre>                      + ^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 723 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M733.0,622.0L733.0,551.0L-10.0,551.0L-10.0,622.0L733.0,622.0ZM620.0,-231.0L545.0,-231.0Q532.0,-190.0 504.0,-167.0Q476.0,-144.0 438.0,-144.0Q386.0,-144.0 342.0,-152.5Q298.0,-161.0 249.0,-161.0Q205.0,-161.0 161.5,-144.5Q118.0,-128.0 89.5,-87.0Q61.0,-46.0 61.0,26.0Q61.0,54.0 65.0,79.5Q69.0,105.0 73.0,118.0L150.0,108.0Q146.0,89.0 142.5,69.0Q139.0,49.0 139.0,24.0Q139.0,-40.0 169.5,-64.5Q200.0,-89.0 248.0,-89.0Q292.0,-89.0 333.5,-80.5Q375.0,-72.0 430.0,-72.0Q459.0,-72.0 487.0,-83.5Q515.0,-95.0 543.0,-127.0L543.0,-15.0Q543.0,-7.0 543.0,1.5Q543.0,10.0 543.0,18.0Q495.0,0.0 432.0,0.0Q344.0,0.0 267.5,39.5Q191.0,79.0 130.5,170.5Q70.0,262.0 28.0,417.0L104.0,440.0Q140.0,311.0 185.5,231.0Q231.0,151.0 291.5,113.5Q352.0,76.0 433.0,76.0Q494.0,76.0 533.5,99.0Q573.0,122.0 573.0,172.0Q573.0,194.0 562.0,212.0Q551.0,230.0 531.0,244.0Q499.0,227.0 457.0,212.0L427.0,282.0Q492.0,303.0 528.0,327.0Q564.0,351.0 564.0,393.0Q564.0,457.0 483.0,457.0Q438.0,457.0 399.5,440.0Q361.0,423.0 337.5,400.0Q314.0,377.0 314.0,358.0Q314.0,345.0 323.5,336.0Q333.0,327.0 364.0,322.0L344.0,248.0Q235.0,267.0 235.0,350.0Q235.0,383.0 255.5,414.5Q276.0,446.0 311.0,472.0Q346.0,498.0 391.5,513.0Q437.0,528.0 486.0,528.0Q562.0,528.0 603.0,493.0Q644.0,458.0 644.0,396.0Q644.0,363.0 630.5,335.5Q617.0,308.0 592.0,286.0Q654.0,240.0 654.0,170.0Q654.0,111.0 620.0,70.0L620.0,-231.0Z" transform="translate(0, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 675 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M576.0,-190.0L501.0,-190.0Q488.0,-149.0 460.0,-126.5Q432.0,-104.0 398.0,-104.0Q353.0,-104.0 310.0,-112.5Q267.0,-121.0 223.0,-121.0Q180.0,-121.0 138.0,-105.0Q96.0,-89.0 68.5,-49.0Q41.0,-9.0 41.0,64.0Q41.0,93.0 45.0,119.0Q49.0,145.0 53.0,158.0L130.0,148.0Q126.0,129.0 122.5,107.5Q119.0,86.0 119.0,64.0Q119.0,0.0 147.0,-24.5Q175.0,-49.0 221.0,-49.0Q260.0,-49.0 303.0,-40.5Q346.0,-32.0 388.0,-32.0Q416.0,-32.0 443.5,-43.0Q471.0,-54.0 499.0,-86.0L499.0,35.0Q499.0,45.0 499.5,60.0Q500.0,75.0 501.0,93.0Q467.0,68.0 429.0,53.5Q391.0,39.0 346.0,39.0Q309.0,39.0 282.5,50.0Q256.0,61.0 239.0,78.0Q223.0,97.0 212.5,124.0Q202.0,151.0 202.0,206.0L202.0,551.0L-10.0,551.0L-10.0,622.0L502.0,622.0Q501.0,663.0 482.5,681.0Q464.0,699.0 422.0,699.0L328.0,699.0Q263.0,699.0 227.5,708.0Q192.0,717.0 167.0,736.0Q113.0,777.0 113.0,859.0Q113.0,872.0 114.5,884.5Q116.0,897.0 118.0,912.0L192.0,907.0Q188.0,887.0 188.0,869.0Q188.0,847.0 192.5,830.0Q197.0,813.0 207.0,802.0Q221.0,786.0 247.5,778.5Q274.0,771.0 323.0,771.0L401.0,771.0Q454.0,771.0 485.0,763.0Q516.0,755.0 538.0,734.0Q571.0,702.0 574.0,622.0L685.0,622.0L685.0,551.0L279.0,551.0L279.0,220.0Q279.0,176.0 284.0,158.0Q289.0,140.0 296.0,132.0Q314.0,111.0 351.0,111.0Q390.0,111.0 425.0,130.0Q460.0,149.0 486.0,177.0Q515.0,208.0 530.5,243.0Q546.0,278.0 546.0,314.0Q546.0,346.0 530.0,362.5Q514.0,379.0 477.0,379.0Q465.0,379.0 450.5,377.0Q436.0,375.0 424.0,372.0L413.0,443.0Q432.0,448.0 452.5,451.0Q473.0,454.0 496.0,454.0Q552.0,454.0 588.0,421.5Q624.0,389.0 624.0,318.0Q624.0,279.0 611.0,241.5Q598.0,204.0 576.0,172.0L576.0,-190.0Z" transform="translate(0, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ৗ᳐᳷ৈ৮꣱ৗ᳖ৎঞ</span> (Added by SIESTA)</li>


<pre>Expected: uni25CC=0+510|aulengthmarkbeng=0+266|uni1CD0=0@-214,323+0|uni1CF7=0+526|aivowelsignbeng=0+346|uni25CC=0+510|eightbeng=4+592|uniA8F1=4@0,323+0|uni25CC=4+510|aulengthmarkbeng=4+266|uni1CD6=4@-214,-319+0|khandatabeng=8+507|nyabeng=9+1019</pre>



<pre>Got     : uni25CC=0+510|aulengthmarkbeng=0+266|uni1CD0=0@-214,323+0|uni1CF7=0+456|aivowelsignbeng=0+346|uni25CC=0+510|eightbeng=4+592|uniA8F1=4@0,323+0|uni25CC=4+510|aulengthmarkbeng=4+266|uni1CD6=4@-214,-319+0|khandatabeng=8+525|nyabeng=9+1019</pre>



<pre>                                                                              ^^                                                                                                                                                   ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5000 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(0, 908)"/>
<path d="M171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L99.0,622.0Q98.0,663.0 79.5,681.0Q61.0,699.0 20.0,699.0L-149.0,699.0Q-214.0,699.0 -249.5,708.0Q-285.0,717.0 -310.0,736.0Q-364.0,777.0 -364.0,859.0Q-364.0,872.0 -362.5,885.0Q-361.0,898.0 -359.0,912.0L-285.0,907.0Q-287.0,895.0 -288.0,886.0Q-289.0,877.0 -289.0,869.0Q-289.0,847.0 -284.5,830.0Q-280.0,813.0 -270.0,802.0Q-256.0,786.0 -230.0,778.5Q-204.0,771.0 -154.0,771.0L-2.0,771.0Q51.0,771.0 82.0,763.0Q113.0,755.0 135.0,734.0Q168.0,702.0 171.0,622.0L276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0Z" transform="translate(510, 908)"/>
<path d="M-430.0,661.0L-289.0,910.0L-228.0,910.0L-77.0,663.0L-131.0,636.0L-255.0,849.0L-371.0,636.0L-430.0,661.0Z" transform="translate(562, 1231)"/>
<path d="M469.0,795.0Q438.0,818.0 406.0,831.0Q374.0,844.0 341.0,844.0Q305.0,844.0 274.5,831.5Q244.0,819.0 225.5,780.5Q207.0,742.0 207.0,664.0Q207.0,544.0 213.0,433.5Q219.0,323.0 227.0,213.0Q235.0,103.0 241.0,-15.5Q247.0,-134.0 247.0,-271.0L167.0,-271.0Q167.0,-134.0 161.0,-14.0Q155.0,106.0 146.5,217.5Q138.0,329.0 132.0,439.5Q126.0,550.0 126.0,668.0Q126.0,764.0 155.5,818.5Q185.0,873.0 232.0,895.0Q279.0,917.0 332.0,917.0Q388.0,917.0 433.5,899.0Q479.0,881.0 516.0,854.0L469.0,795.0Z" transform="translate(776, 908)"/>
<path d="M283.0,622.0Q282.0,661.0 264.5,680.0Q247.0,699.0 203.0,699.0L183.0,699.0Q118.0,699.0 82.5,708.0Q47.0,717.0 22.0,736.0Q-32.0,777.0 -32.0,859.0Q-32.0,872.0 -30.5,884.5Q-29.0,897.0 -27.0,912.0L47.0,907.0Q43.0,887.0 43.0,869.0Q43.0,847.0 47.5,830.0Q52.0,813.0 62.0,802.0Q76.0,786.0 102.0,778.5Q128.0,771.0 178.0,771.0L182.0,771.0Q235.0,771.0 266.0,763.0Q297.0,755.0 319.0,734.0Q352.0,702.0 355.0,622.0L356.0,622.0L356.0,551.0L336.0,551.0Q305.0,544.0 269.0,520.5Q233.0,497.0 201.0,459.5Q169.0,422.0 148.5,372.0Q128.0,322.0 128.0,262.0Q128.0,190.0 149.5,147.5Q171.0,105.0 203.0,87.0Q235.0,69.0 267.0,69.0Q292.0,69.0 309.0,74.0Q326.0,79.0 348.0,92.0L383.0,31.0Q357.0,11.0 326.0,3.0Q295.0,-5.0 264.0,-5.0Q201.0,-5.0 152.5,28.0Q104.0,61.0 76.5,120.5Q49.0,180.0 49.0,260.0Q49.0,359.0 93.5,435.0Q138.0,511.0 208.0,554.0Q191.0,552.0 172.0,551.5Q153.0,551.0 130.0,551.0L-10.0,551.0L-10.0,622.0L283.0,622.0Z" transform="translate(1232, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1578, 908)"/>
<path d="M237.0,0.0Q198.0,0.0 172.5,11.0Q147.0,22.0 132.0,38.0Q114.0,56.0 102.5,83.0Q91.0,110.0 91.0,164.0L91.0,481.0Q91.0,518.0 78.5,532.0Q66.0,546.0 22.0,547.0L31.0,624.0Q106.0,621.0 136.0,595.0Q153.0,580.0 160.0,556.5Q167.0,533.0 167.0,501.0L167.0,355.0Q198.0,366.0 225.5,370.5Q253.0,375.0 269.0,375.0Q280.0,375.0 294.0,373.5Q308.0,372.0 318.0,370.0Q347.0,363.0 366.5,361.5Q386.0,360.0 408.0,360.0Q446.0,360.0 470.5,371.0Q495.0,382.0 514.0,418.0L586.0,383.0Q567.0,333.0 528.0,312.5Q489.0,292.0 442.0,292.0Q436.0,292.0 430.0,292.0Q448.0,257.0 448.0,213.0Q448.0,147.0 419.5,99.0Q391.0,51.0 343.5,25.5Q296.0,0.0 237.0,0.0ZM238.0,71.0Q282.0,71.0 311.0,92.5Q340.0,114.0 354.5,146.5Q369.0,179.0 369.0,212.0Q369.0,249.0 354.5,269.0Q340.0,289.0 318.5,296.5Q297.0,304.0 274.0,304.0Q241.0,304.0 215.5,298.0Q190.0,292.0 167.0,281.0L167.0,168.0Q167.0,135.0 172.0,117.5Q177.0,100.0 184.0,92.0Q192.0,84.0 203.5,77.5Q215.0,71.0 238.0,71.0Z" transform="translate(2088, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(2680, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(2680, 908)"/>
<path d="M171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L99.0,622.0Q98.0,663.0 79.5,681.0Q61.0,699.0 20.0,699.0L-149.0,699.0Q-214.0,699.0 -249.5,708.0Q-285.0,717.0 -310.0,736.0Q-364.0,777.0 -364.0,859.0Q-364.0,872.0 -362.5,885.0Q-361.0,898.0 -359.0,912.0L-285.0,907.0Q-287.0,895.0 -288.0,886.0Q-289.0,877.0 -289.0,869.0Q-289.0,847.0 -284.5,830.0Q-280.0,813.0 -270.0,802.0Q-256.0,786.0 -230.0,778.5Q-204.0,771.0 -154.0,771.0L-2.0,771.0Q51.0,771.0 82.0,763.0Q113.0,755.0 135.0,734.0Q168.0,702.0 171.0,622.0L276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0Z" transform="translate(3190, 908)"/>
<path d="M-426.0,-94.0L-348.0,-94.0L-348.0,-202.0L-78.0,-202.0L-78.0,-271.0L-426.0,-271.0L-426.0,-94.0Z" transform="translate(3242, 589)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(3456, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(3981, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5052 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(0, 908)"/>
<path d="M171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L99.0,622.0Q98.0,663.0 79.5,681.0Q61.0,699.0 20.0,699.0L-149.0,699.0Q-214.0,699.0 -249.5,708.0Q-285.0,717.0 -310.0,736.0Q-364.0,777.0 -364.0,859.0Q-364.0,872.0 -362.5,885.0Q-361.0,898.0 -359.0,912.0L-285.0,907.0Q-287.0,895.0 -288.0,886.0Q-289.0,877.0 -289.0,869.0Q-289.0,847.0 -284.5,830.0Q-280.0,813.0 -270.0,802.0Q-256.0,786.0 -230.0,778.5Q-204.0,771.0 -154.0,771.0L-2.0,771.0Q51.0,771.0 82.0,763.0Q113.0,755.0 135.0,734.0Q168.0,702.0 171.0,622.0L276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0Z" transform="translate(510, 908)"/>
<path d="M-430.0,661.0L-289.0,910.0L-228.0,910.0L-77.0,663.0L-131.0,636.0L-255.0,849.0L-371.0,636.0L-430.0,661.0Z" transform="translate(562, 1231)"/>
<path d="M469.0,795.0Q438.0,818.0 406.0,831.0Q374.0,844.0 341.0,844.0Q305.0,844.0 274.5,831.5Q244.0,819.0 225.5,780.5Q207.0,742.0 207.0,664.0Q207.0,544.0 213.0,433.5Q219.0,323.0 227.0,213.0Q235.0,103.0 241.0,-15.5Q247.0,-134.0 247.0,-271.0L167.0,-271.0Q167.0,-134.0 161.0,-14.0Q155.0,106.0 146.5,217.5Q138.0,329.0 132.0,439.5Q126.0,550.0 126.0,668.0Q126.0,764.0 155.5,818.5Q185.0,873.0 232.0,895.0Q279.0,917.0 332.0,917.0Q388.0,917.0 433.5,899.0Q479.0,881.0 516.0,854.0L469.0,795.0Z" transform="translate(776, 908)"/>
<path d="M283.0,622.0Q282.0,661.0 264.5,680.0Q247.0,699.0 203.0,699.0L183.0,699.0Q118.0,699.0 82.5,708.0Q47.0,717.0 22.0,736.0Q-32.0,777.0 -32.0,859.0Q-32.0,872.0 -30.5,884.5Q-29.0,897.0 -27.0,912.0L47.0,907.0Q43.0,887.0 43.0,869.0Q43.0,847.0 47.5,830.0Q52.0,813.0 62.0,802.0Q76.0,786.0 102.0,778.5Q128.0,771.0 178.0,771.0L182.0,771.0Q235.0,771.0 266.0,763.0Q297.0,755.0 319.0,734.0Q352.0,702.0 355.0,622.0L356.0,622.0L356.0,551.0L336.0,551.0Q305.0,544.0 269.0,520.5Q233.0,497.0 201.0,459.5Q169.0,422.0 148.5,372.0Q128.0,322.0 128.0,262.0Q128.0,190.0 149.5,147.5Q171.0,105.0 203.0,87.0Q235.0,69.0 267.0,69.0Q292.0,69.0 309.0,74.0Q326.0,79.0 348.0,92.0L383.0,31.0Q357.0,11.0 326.0,3.0Q295.0,-5.0 264.0,-5.0Q201.0,-5.0 152.5,28.0Q104.0,61.0 76.5,120.5Q49.0,180.0 49.0,260.0Q49.0,359.0 93.5,435.0Q138.0,511.0 208.0,554.0Q191.0,552.0 172.0,551.5Q153.0,551.0 130.0,551.0L-10.0,551.0L-10.0,622.0L283.0,622.0Z" transform="translate(1302, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1648, 908)"/>
<path d="M237.0,0.0Q198.0,0.0 172.5,11.0Q147.0,22.0 132.0,38.0Q114.0,56.0 102.5,83.0Q91.0,110.0 91.0,164.0L91.0,481.0Q91.0,518.0 78.5,532.0Q66.0,546.0 22.0,547.0L31.0,624.0Q106.0,621.0 136.0,595.0Q153.0,580.0 160.0,556.5Q167.0,533.0 167.0,501.0L167.0,355.0Q198.0,366.0 225.5,370.5Q253.0,375.0 269.0,375.0Q280.0,375.0 294.0,373.5Q308.0,372.0 318.0,370.0Q347.0,363.0 366.5,361.5Q386.0,360.0 408.0,360.0Q446.0,360.0 470.5,371.0Q495.0,382.0 514.0,418.0L586.0,383.0Q567.0,333.0 528.0,312.5Q489.0,292.0 442.0,292.0Q436.0,292.0 430.0,292.0Q448.0,257.0 448.0,213.0Q448.0,147.0 419.5,99.0Q391.0,51.0 343.5,25.5Q296.0,0.0 237.0,0.0ZM238.0,71.0Q282.0,71.0 311.0,92.5Q340.0,114.0 354.5,146.5Q369.0,179.0 369.0,212.0Q369.0,249.0 354.5,269.0Q340.0,289.0 318.5,296.5Q297.0,304.0 274.0,304.0Q241.0,304.0 215.5,298.0Q190.0,292.0 167.0,281.0L167.0,168.0Q167.0,135.0 172.0,117.5Q177.0,100.0 184.0,92.0Q192.0,84.0 203.5,77.5Q215.0,71.0 238.0,71.0Z" transform="translate(2158, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(2750, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(2750, 908)"/>
<path d="M171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L99.0,622.0Q98.0,663.0 79.5,681.0Q61.0,699.0 20.0,699.0L-149.0,699.0Q-214.0,699.0 -249.5,708.0Q-285.0,717.0 -310.0,736.0Q-364.0,777.0 -364.0,859.0Q-364.0,872.0 -362.5,885.0Q-361.0,898.0 -359.0,912.0L-285.0,907.0Q-287.0,895.0 -288.0,886.0Q-289.0,877.0 -289.0,869.0Q-289.0,847.0 -284.5,830.0Q-280.0,813.0 -270.0,802.0Q-256.0,786.0 -230.0,778.5Q-204.0,771.0 -154.0,771.0L-2.0,771.0Q51.0,771.0 82.0,763.0Q113.0,755.0 135.0,734.0Q168.0,702.0 171.0,622.0L276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0Z" transform="translate(3260, 908)"/>
<path d="M-426.0,-94.0L-348.0,-94.0L-348.0,-202.0L-78.0,-202.0L-78.0,-271.0L-426.0,-271.0L-426.0,-94.0Z" transform="translate(3312, 589)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(3526, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(4033, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">জ়ঞগএগ+꣱ং᳒</span> (Added by SIESTA)</li>


<pre>Expected: januktabeng=0+917|nyabeng=2+1001|gabeng=3+656|ebeng=4+740|gabeng=5+656|plus.beng=6+592|uni25CC=6+510|uniA8F1=6+0|uni25CC=6+510|anusvarabeng=6+438|uni1CD2=6@-386,323+0</pre>



<pre>Got     : januktabeng=0+917|nyabeng=2+1019|gabeng=3+656|ebeng=4+758|gabeng=5+656|plus.beng=6+592|uni25CC=6+510|uniA8F1=6+0|uni25CC=6+510|anusvarabeng=6+438|uni1CD2=6@-386,323+0</pre>



<pre>                                        +                        ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 6056 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M401.0,63.0Q323.0,63.0 253.5,101.0Q184.0,139.0 127.0,227.0Q70.0,315.0 29.0,465.0L105.0,485.0Q139.0,362.0 181.0,285.5Q223.0,209.0 278.0,174.0Q333.0,139.0 404.0,139.0Q554.0,139.0 554.0,268.0Q554.0,282.0 552.0,294.5Q550.0,307.0 547.0,318.0Q513.0,290.0 475.0,273.5Q437.0,257.0 391.0,257.0Q332.0,257.0 295.0,290.0Q258.0,323.0 258.0,384.0Q258.0,428.0 289.0,473.5Q320.0,519.0 394.0,553.0Q374.0,552.0 348.5,551.5Q323.0,551.0 298.0,551.0L-10.0,551.0L-10.0,622.0L927.0,622.0L927.0,551.0L614.0,551.0Q597.0,551.0 582.0,551.5Q567.0,552.0 554.0,553.0Q578.0,512.0 623.0,485.5Q668.0,459.0 751.0,459.0Q776.0,459.0 806.0,462.0L845.0,392.0Q821.0,347.0 811.0,304.0Q801.0,261.0 801.0,205.0Q801.0,156.0 809.0,111.0Q817.0,66.0 836.0,10.0L761.0,-7.0Q743.0,51.0 733.0,106.5Q723.0,162.0 723.0,222.0Q723.0,275.0 732.5,317.0Q742.0,359.0 755.0,388.0Q647.0,389.0 583.5,426.0Q520.0,463.0 483.0,529.0Q421.0,498.0 389.5,471.5Q358.0,445.0 346.5,422.5Q335.0,400.0 335.0,380.0Q335.0,352.0 351.0,340.0Q367.0,328.0 387.0,328.0Q425.0,328.0 455.0,345.5Q485.0,363.0 523.0,396.0L609.0,365.0Q618.0,345.0 624.0,315.5Q630.0,286.0 630.0,254.0Q630.0,204.0 607.5,160.5Q585.0,117.0 534.5,90.0Q484.0,63.0 401.0,63.0ZM458.0,-144.0Q433.0,-144.0 415.5,-128.0Q398.0,-112.0 398.0,-86.0Q398.0,-60.0 415.5,-43.0Q433.0,-26.0 458.0,-26.0Q483.0,-26.0 500.5,-43.0Q518.0,-60.0 518.0,-86.0Q518.0,-112.0 500.5,-128.0Q483.0,-144.0 458.0,-144.0Z" transform="translate(0, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(917, 908)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(1936, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(2592, 908)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(3350, 908)"/>
<path d="M259.0,286.0L70.0,286.0L70.0,359.0L259.0,359.0L259.0,548.0L332.0,548.0L332.0,359.0L521.0,359.0L521.0,286.0L332.0,286.0L332.0,97.0L259.0,97.0L259.0,286.0Z" transform="translate(4006, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(4598, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(5108, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(5108, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(5618, 908)"/>
<path d="M-418.0,789.0L-90.0,789.0L-90.0,722.0L-418.0,722.0L-418.0,789.0Z" transform="translate(5670, 1231)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 6020 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M401.0,63.0Q323.0,63.0 253.5,101.0Q184.0,139.0 127.0,227.0Q70.0,315.0 29.0,465.0L105.0,485.0Q139.0,362.0 181.0,285.5Q223.0,209.0 278.0,174.0Q333.0,139.0 404.0,139.0Q554.0,139.0 554.0,268.0Q554.0,282.0 552.0,294.5Q550.0,307.0 547.0,318.0Q513.0,290.0 475.0,273.5Q437.0,257.0 391.0,257.0Q332.0,257.0 295.0,290.0Q258.0,323.0 258.0,384.0Q258.0,428.0 289.0,473.5Q320.0,519.0 394.0,553.0Q374.0,552.0 348.5,551.5Q323.0,551.0 298.0,551.0L-10.0,551.0L-10.0,622.0L927.0,622.0L927.0,551.0L614.0,551.0Q597.0,551.0 582.0,551.5Q567.0,552.0 554.0,553.0Q578.0,512.0 623.0,485.5Q668.0,459.0 751.0,459.0Q776.0,459.0 806.0,462.0L845.0,392.0Q821.0,347.0 811.0,304.0Q801.0,261.0 801.0,205.0Q801.0,156.0 809.0,111.0Q817.0,66.0 836.0,10.0L761.0,-7.0Q743.0,51.0 733.0,106.5Q723.0,162.0 723.0,222.0Q723.0,275.0 732.5,317.0Q742.0,359.0 755.0,388.0Q647.0,389.0 583.5,426.0Q520.0,463.0 483.0,529.0Q421.0,498.0 389.5,471.5Q358.0,445.0 346.5,422.5Q335.0,400.0 335.0,380.0Q335.0,352.0 351.0,340.0Q367.0,328.0 387.0,328.0Q425.0,328.0 455.0,345.5Q485.0,363.0 523.0,396.0L609.0,365.0Q618.0,345.0 624.0,315.5Q630.0,286.0 630.0,254.0Q630.0,204.0 607.5,160.5Q585.0,117.0 534.5,90.0Q484.0,63.0 401.0,63.0ZM458.0,-144.0Q433.0,-144.0 415.5,-128.0Q398.0,-112.0 398.0,-86.0Q398.0,-60.0 415.5,-43.0Q433.0,-26.0 458.0,-26.0Q483.0,-26.0 500.5,-43.0Q518.0,-60.0 518.0,-86.0Q518.0,-112.0 500.5,-128.0Q483.0,-144.0 458.0,-144.0Z" transform="translate(0, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(917, 908)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(1918, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(2574, 908)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(3314, 908)"/>
<path d="M259.0,286.0L70.0,286.0L70.0,359.0L259.0,359.0L259.0,548.0L332.0,548.0L332.0,359.0L521.0,359.0L521.0,286.0L332.0,286.0L332.0,97.0L259.0,97.0L259.0,286.0Z" transform="translate(3970, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(4562, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(5072, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(5072, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(5582, 908)"/>
<path d="M-418.0,789.0L-90.0,789.0L-90.0,722.0L-418.0,722.0L-418.0,789.0Z" transform="translate(5634, 1231)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">িআংএঠ᳘</span> (Added by SIESTA)</li>


<pre>Expected: ivowelsignbeng=0+266|uni25CC=0+510|aabeng=1+1158|anusvarabeng=1+403|ebeng=3+758|tthabeng=4+591|uni1CD8=4@-41,-351+0</pre>



<pre>Got     : ivowelsignbeng=0+266|uni25CC=0+510|aabeng=1+1158|anusvarabeng=1+438|ebeng=3+758|tthabeng=4+591|uni1CD8=4@-41,-351+0</pre>



<pre>                                                                           +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3721 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L82.0,622.0Q66.0,641.0 49.5,662.0Q33.0,683.0 20.0,704.0Q54.0,763.0 93.0,811.5Q132.0,860.0 185.0,888.5Q238.0,917.0 313.0,917.0Q384.0,917.0 447.0,894.0Q510.0,871.0 573.0,829.5Q636.0,788.0 705.0,731.0L663.0,677.0Q594.0,733.0 538.5,770.0Q483.0,807.0 432.5,825.5Q382.0,844.0 325.0,844.0Q242.0,844.0 192.0,802.0Q142.0,760.0 106.0,693.0Q114.0,678.0 128.0,660.0Q142.0,642.0 160.0,622.0L276.0,622.0Z" transform="translate(0, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(266, 908)"/>
<path d="M376.0,91.0Q308.0,91.0 246.0,123.0Q184.0,155.0 129.5,231.5Q75.0,308.0 29.0,442.0L102.0,466.0Q155.0,309.0 219.5,238.0Q284.0,167.0 378.0,167.0Q461.0,167.0 495.5,205.0Q530.0,243.0 530.0,300.0Q530.0,358.0 498.5,394.0Q467.0,430.0 420.0,430.0Q353.0,430.0 353.0,372.0Q353.0,365.0 355.0,353.0Q357.0,341.0 361.0,331.0L285.0,316.0Q278.0,337.0 274.5,354.5Q271.0,372.0 271.0,388.0Q271.0,423.0 290.0,447.5Q309.0,472.0 339.0,485.0Q330.0,507.0 311.5,524.0Q293.0,541.0 262.0,551.0L-10.0,551.0L-10.0,622.0L898.0,622.0L898.0,622.0Q925.0,622.0 949.5,606.0Q974.0,590.0 990.0,559.0Q989.0,564.0 987.5,582.0Q986.0,600.0 986.0,613.0L986.0,688.0L1039.0,688.0L1062.0,622.0L1168.0,622.0L1168.0,551.0L1063.0,551.0L1063.0,0.0L986.0,0.0L986.0,479.0Q969.0,518.0 947.5,534.5Q926.0,551.0 897.0,551.0L798.0,551.0L798.0,0.0L721.0,0.0Q693.0,56.0 653.0,98.5Q613.0,141.0 568.0,173.0Q540.0,136.0 492.0,113.5Q444.0,91.0 376.0,91.0ZM606.0,294.0Q606.0,264.0 598.0,236.0Q634.0,213.0 669.5,178.5Q705.0,144.0 724.0,109.0Q723.0,131.0 722.0,150.5Q721.0,170.0 721.0,194.0L721.0,551.0L381.0,551.0Q406.0,530.0 416.0,500.0Q474.0,499.0 516.5,472.5Q559.0,446.0 582.5,400.0Q606.0,354.0 606.0,294.0Z" transform="translate(776, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(1934, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(2372, 908)"/>
<path d="M282.0,0.0Q192.0,0.0 128.0,47.0Q64.0,94.0 36.0,168.0L58.0,247.0Q140.0,255.0 184.0,283.0Q228.0,311.0 245.5,353.5Q263.0,396.0 263.0,448.0Q263.0,471.0 258.0,498.0Q253.0,525.0 242.0,551.0L-10.0,551.0L-10.0,622.0L200.0,622.0Q168.0,666.0 148.5,702.5Q129.0,739.0 129.0,776.0Q129.0,818.0 152.0,852.0Q175.0,886.0 218.0,917.0L269.0,861.0Q237.0,836.0 222.5,814.5Q208.0,793.0 208.0,764.0Q208.0,733.0 230.5,699.5Q253.0,666.0 291.0,622.0L601.0,622.0L601.0,551.0L427.0,551.0Q408.0,551.0 394.0,551.5Q380.0,552.0 365.0,553.0Q438.0,480.0 483.5,406.0Q529.0,332.0 529.0,240.0Q529.0,169.0 500.0,115.0Q471.0,61.0 416.0,30.5Q361.0,0.0 282.0,0.0ZM280.0,74.0Q338.0,74.0 375.0,98.0Q412.0,122.0 430.0,161.0Q448.0,200.0 448.0,244.0Q448.0,308.0 419.0,369.5Q390.0,431.0 316.0,512.0Q323.0,489.0 328.0,463.5Q333.0,438.0 333.0,406.0Q333.0,359.0 315.0,313.5Q297.0,268.0 250.0,232.0Q203.0,196.0 117.0,175.0Q141.0,123.0 186.0,98.5Q231.0,74.0 280.0,74.0Z" transform="translate(3130, 908)"/>
<path d="M-44.0,-88.0Q-67.0,-188.0 -120.5,-229.5Q-174.0,-271.0 -251.0,-271.0Q-323.0,-271.0 -377.0,-226.5Q-431.0,-182.0 -465.0,-88.0L-394.0,-64.0Q-368.0,-134.0 -334.5,-168.0Q-301.0,-202.0 -248.0,-202.0Q-191.0,-202.0 -163.5,-165.5Q-136.0,-129.0 -120.0,-62.0L-44.0,-88.0Z" transform="translate(3680, 557)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3686 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L82.0,622.0Q66.0,641.0 49.5,662.0Q33.0,683.0 20.0,704.0Q54.0,763.0 93.0,811.5Q132.0,860.0 185.0,888.5Q238.0,917.0 313.0,917.0Q384.0,917.0 447.0,894.0Q510.0,871.0 573.0,829.5Q636.0,788.0 705.0,731.0L663.0,677.0Q594.0,733.0 538.5,770.0Q483.0,807.0 432.5,825.5Q382.0,844.0 325.0,844.0Q242.0,844.0 192.0,802.0Q142.0,760.0 106.0,693.0Q114.0,678.0 128.0,660.0Q142.0,642.0 160.0,622.0L276.0,622.0Z" transform="translate(0, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(266, 908)"/>
<path d="M376.0,91.0Q308.0,91.0 246.0,123.0Q184.0,155.0 129.5,231.5Q75.0,308.0 29.0,442.0L102.0,466.0Q155.0,309.0 219.5,238.0Q284.0,167.0 378.0,167.0Q461.0,167.0 495.5,205.0Q530.0,243.0 530.0,300.0Q530.0,358.0 498.5,394.0Q467.0,430.0 420.0,430.0Q353.0,430.0 353.0,372.0Q353.0,365.0 355.0,353.0Q357.0,341.0 361.0,331.0L285.0,316.0Q278.0,337.0 274.5,354.5Q271.0,372.0 271.0,388.0Q271.0,423.0 290.0,447.5Q309.0,472.0 339.0,485.0Q330.0,507.0 311.5,524.0Q293.0,541.0 262.0,551.0L-10.0,551.0L-10.0,622.0L898.0,622.0L898.0,622.0Q925.0,622.0 949.5,606.0Q974.0,590.0 990.0,559.0Q989.0,564.0 987.5,582.0Q986.0,600.0 986.0,613.0L986.0,688.0L1039.0,688.0L1062.0,622.0L1168.0,622.0L1168.0,551.0L1063.0,551.0L1063.0,0.0L986.0,0.0L986.0,479.0Q969.0,518.0 947.5,534.5Q926.0,551.0 897.0,551.0L798.0,551.0L798.0,0.0L721.0,0.0Q693.0,56.0 653.0,98.5Q613.0,141.0 568.0,173.0Q540.0,136.0 492.0,113.5Q444.0,91.0 376.0,91.0ZM606.0,294.0Q606.0,264.0 598.0,236.0Q634.0,213.0 669.5,178.5Q705.0,144.0 724.0,109.0Q723.0,131.0 722.0,150.5Q721.0,170.0 721.0,194.0L721.0,551.0L381.0,551.0Q406.0,530.0 416.0,500.0Q474.0,499.0 516.5,472.5Q559.0,446.0 582.5,400.0Q606.0,354.0 606.0,294.0Z" transform="translate(776, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(1934, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(2337, 908)"/>
<path d="M282.0,0.0Q192.0,0.0 128.0,47.0Q64.0,94.0 36.0,168.0L58.0,247.0Q140.0,255.0 184.0,283.0Q228.0,311.0 245.5,353.5Q263.0,396.0 263.0,448.0Q263.0,471.0 258.0,498.0Q253.0,525.0 242.0,551.0L-10.0,551.0L-10.0,622.0L200.0,622.0Q168.0,666.0 148.5,702.5Q129.0,739.0 129.0,776.0Q129.0,818.0 152.0,852.0Q175.0,886.0 218.0,917.0L269.0,861.0Q237.0,836.0 222.5,814.5Q208.0,793.0 208.0,764.0Q208.0,733.0 230.5,699.5Q253.0,666.0 291.0,622.0L601.0,622.0L601.0,551.0L427.0,551.0Q408.0,551.0 394.0,551.5Q380.0,552.0 365.0,553.0Q438.0,480.0 483.5,406.0Q529.0,332.0 529.0,240.0Q529.0,169.0 500.0,115.0Q471.0,61.0 416.0,30.5Q361.0,0.0 282.0,0.0ZM280.0,74.0Q338.0,74.0 375.0,98.0Q412.0,122.0 430.0,161.0Q448.0,200.0 448.0,244.0Q448.0,308.0 419.0,369.5Q390.0,431.0 316.0,512.0Q323.0,489.0 328.0,463.5Q333.0,438.0 333.0,406.0Q333.0,359.0 315.0,313.5Q297.0,268.0 250.0,232.0Q203.0,196.0 117.0,175.0Q141.0,123.0 186.0,98.5Q231.0,74.0 280.0,74.0Z" transform="translate(3095, 908)"/>
<path d="M-44.0,-88.0Q-67.0,-188.0 -120.5,-229.5Q-174.0,-271.0 -251.0,-271.0Q-323.0,-271.0 -377.0,-226.5Q-431.0,-182.0 -465.0,-88.0L-394.0,-64.0Q-368.0,-134.0 -334.5,-168.0Q-301.0,-202.0 -248.0,-202.0Q-191.0,-202.0 -163.5,-165.5Q-136.0,-129.0 -120.0,-62.0L-44.0,-88.0Z" transform="translate(3645, 557)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঙওদ়ষ᳒ট॒</span> (Added by SIESTA)</li>


<pre>Expected: ngabeng=0+705|obeng=1+738|danuktabeng=2+603|ssabeng=4+633|uni1CD2=4@-62,323+0|ttabeng=6+567|uni0952=6@-29,-313+0</pre>



<pre>Got     : ngabeng=0+723|obeng=1+738|danuktabeng=2+603|ssabeng=4+633|uni1CD2=4@-62,323+0|ttabeng=6+567|uni0952=6@-29,-313+0</pre>



<pre>                     ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3264 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(0, 908)"/>
<path d="M681.0,225.0Q681.0,142.0 619.5,92.0Q558.0,42.0 453.0,42.0Q359.0,42.0 279.0,87.5Q199.0,133.0 136.0,235.5Q73.0,338.0 28.0,507.0L103.0,529.0Q143.0,386.0 192.5,295.0Q242.0,204.0 306.5,161.0Q371.0,118.0 455.0,118.0Q518.0,118.0 559.0,144.5Q600.0,171.0 600.0,228.0Q600.0,255.0 587.0,276.5Q574.0,298.0 552.0,314.0Q520.0,297.0 480.0,282.0L449.0,354.0Q516.0,376.0 553.5,405.5Q591.0,435.0 591.0,482.0Q591.0,558.0 509.0,558.0Q461.0,558.0 420.5,537.5Q380.0,517.0 355.5,489.5Q331.0,462.0 331.0,439.0Q331.0,423.0 341.0,411.5Q351.0,400.0 386.0,395.0L365.0,321.0Q308.0,332.0 279.5,360.0Q251.0,388.0 251.0,431.0Q251.0,465.0 271.5,499.5Q292.0,534.0 328.0,563.5Q364.0,593.0 410.5,611.0Q457.0,629.0 509.0,629.0Q586.0,629.0 628.5,590.0Q671.0,551.0 671.0,483.0Q671.0,445.0 655.5,414.0Q640.0,383.0 613.0,358.0Q681.0,308.0 681.0,225.0Z" transform="translate(723, 908)"/>
<path d="M613.0,622.0L613.0,551.0L159.0,551.0L159.0,288.0Q280.0,414.0 475.0,486.0L540.0,422.0Q512.0,370.0 499.5,320.0Q487.0,270.0 487.0,205.0Q487.0,156.0 495.0,111.0Q503.0,66.0 522.0,10.0L447.0,-7.0Q429.0,51.0 419.0,106.5Q409.0,162.0 409.0,222.0Q409.0,276.0 420.0,322.0Q431.0,368.0 445.0,397.0Q365.0,361.0 291.5,306.5Q218.0,252.0 141.0,175.0L82.0,215.0L82.0,551.0L-10.0,551.0L-10.0,622.0L613.0,622.0ZM264.0,-123.0Q239.0,-123.0 221.5,-107.0Q204.0,-91.0 204.0,-65.0Q204.0,-39.0 221.5,-22.0Q239.0,-5.0 264.0,-5.0Q289.0,-5.0 306.5,-22.0Q324.0,-39.0 324.0,-65.0Q324.0,-91.0 306.5,-107.0Q289.0,-123.0 264.0,-123.0Z" transform="translate(1461, 908)"/>
<path d="M643.0,622.0L643.0,551.0L538.0,551.0L538.0,0.0L461.0,0.0Q412.0,58.0 360.0,100.5Q308.0,143.0 242.0,171.0Q176.0,199.0 84.0,212.0L48.0,303.0Q95.0,333.0 150.0,362.5Q205.0,392.0 265.0,418.0Q211.0,448.0 155.5,469.5Q100.0,491.0 48.0,502.0L69.0,551.0L-10.0,551.0L-10.0,622.0L643.0,622.0ZM461.0,551.0L132.0,551.0Q190.0,533.0 250.0,503.5Q310.0,474.0 365.0,437.0Q420.0,400.0 463.0,359.0Q462.0,378.0 461.5,397.0Q461.0,416.0 461.0,434.0L461.0,551.0ZM142.0,275.0Q252.0,254.0 327.5,207.5Q403.0,161.0 463.0,99.0Q463.0,116.0 462.0,134.0Q461.0,152.0 461.0,171.0L461.0,270.0Q435.0,298.0 403.5,324.5Q372.0,351.0 337.0,374.0Q288.0,352.0 235.0,326.5Q182.0,301.0 142.0,275.0Z" transform="translate(2064, 908)"/>
<path d="M-418.0,789.0L-90.0,789.0L-90.0,722.0L-418.0,722.0L-418.0,789.0Z" transform="translate(2635, 1231)"/>
<path d="M395.0,622.0Q394.0,663.0 375.5,681.0Q357.0,699.0 315.0,699.0L221.0,699.0Q156.0,699.0 120.5,708.0Q85.0,717.0 60.0,736.0Q6.0,777.0 6.0,859.0Q6.0,872.0 7.5,884.5Q9.0,897.0 11.0,912.0L85.0,907.0Q81.0,887.0 81.0,869.0Q81.0,847.0 85.5,830.0Q90.0,813.0 100.0,802.0Q114.0,786.0 140.5,778.5Q167.0,771.0 216.0,771.0L294.0,771.0Q347.0,771.0 378.0,763.0Q409.0,755.0 431.0,734.0Q464.0,702.0 467.0,622.0L577.0,622.0L577.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L395.0,622.0Z" transform="translate(2697, 908)"/>
<path d="M-443.0,-187.0L-443.0,-116.0L-67.0,-116.0L-67.0,-187.0L-443.0,-187.0Z" transform="translate(3235, 595)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3246 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(0, 908)"/>
<path d="M681.0,225.0Q681.0,142.0 619.5,92.0Q558.0,42.0 453.0,42.0Q359.0,42.0 279.0,87.5Q199.0,133.0 136.0,235.5Q73.0,338.0 28.0,507.0L103.0,529.0Q143.0,386.0 192.5,295.0Q242.0,204.0 306.5,161.0Q371.0,118.0 455.0,118.0Q518.0,118.0 559.0,144.5Q600.0,171.0 600.0,228.0Q600.0,255.0 587.0,276.5Q574.0,298.0 552.0,314.0Q520.0,297.0 480.0,282.0L449.0,354.0Q516.0,376.0 553.5,405.5Q591.0,435.0 591.0,482.0Q591.0,558.0 509.0,558.0Q461.0,558.0 420.5,537.5Q380.0,517.0 355.5,489.5Q331.0,462.0 331.0,439.0Q331.0,423.0 341.0,411.5Q351.0,400.0 386.0,395.0L365.0,321.0Q308.0,332.0 279.5,360.0Q251.0,388.0 251.0,431.0Q251.0,465.0 271.5,499.5Q292.0,534.0 328.0,563.5Q364.0,593.0 410.5,611.0Q457.0,629.0 509.0,629.0Q586.0,629.0 628.5,590.0Q671.0,551.0 671.0,483.0Q671.0,445.0 655.5,414.0Q640.0,383.0 613.0,358.0Q681.0,308.0 681.0,225.0Z" transform="translate(705, 908)"/>
<path d="M613.0,622.0L613.0,551.0L159.0,551.0L159.0,288.0Q280.0,414.0 475.0,486.0L540.0,422.0Q512.0,370.0 499.5,320.0Q487.0,270.0 487.0,205.0Q487.0,156.0 495.0,111.0Q503.0,66.0 522.0,10.0L447.0,-7.0Q429.0,51.0 419.0,106.5Q409.0,162.0 409.0,222.0Q409.0,276.0 420.0,322.0Q431.0,368.0 445.0,397.0Q365.0,361.0 291.5,306.5Q218.0,252.0 141.0,175.0L82.0,215.0L82.0,551.0L-10.0,551.0L-10.0,622.0L613.0,622.0ZM264.0,-123.0Q239.0,-123.0 221.5,-107.0Q204.0,-91.0 204.0,-65.0Q204.0,-39.0 221.5,-22.0Q239.0,-5.0 264.0,-5.0Q289.0,-5.0 306.5,-22.0Q324.0,-39.0 324.0,-65.0Q324.0,-91.0 306.5,-107.0Q289.0,-123.0 264.0,-123.0Z" transform="translate(1443, 908)"/>
<path d="M643.0,622.0L643.0,551.0L538.0,551.0L538.0,0.0L461.0,0.0Q412.0,58.0 360.0,100.5Q308.0,143.0 242.0,171.0Q176.0,199.0 84.0,212.0L48.0,303.0Q95.0,333.0 150.0,362.5Q205.0,392.0 265.0,418.0Q211.0,448.0 155.5,469.5Q100.0,491.0 48.0,502.0L69.0,551.0L-10.0,551.0L-10.0,622.0L643.0,622.0ZM461.0,551.0L132.0,551.0Q190.0,533.0 250.0,503.5Q310.0,474.0 365.0,437.0Q420.0,400.0 463.0,359.0Q462.0,378.0 461.5,397.0Q461.0,416.0 461.0,434.0L461.0,551.0ZM142.0,275.0Q252.0,254.0 327.5,207.5Q403.0,161.0 463.0,99.0Q463.0,116.0 462.0,134.0Q461.0,152.0 461.0,171.0L461.0,270.0Q435.0,298.0 403.5,324.5Q372.0,351.0 337.0,374.0Q288.0,352.0 235.0,326.5Q182.0,301.0 142.0,275.0Z" transform="translate(2046, 908)"/>
<path d="M-418.0,789.0L-90.0,789.0L-90.0,722.0L-418.0,722.0L-418.0,789.0Z" transform="translate(2617, 1231)"/>
<path d="M395.0,622.0Q394.0,663.0 375.5,681.0Q357.0,699.0 315.0,699.0L221.0,699.0Q156.0,699.0 120.5,708.0Q85.0,717.0 60.0,736.0Q6.0,777.0 6.0,859.0Q6.0,872.0 7.5,884.5Q9.0,897.0 11.0,912.0L85.0,907.0Q81.0,887.0 81.0,869.0Q81.0,847.0 85.5,830.0Q90.0,813.0 100.0,802.0Q114.0,786.0 140.5,778.5Q167.0,771.0 216.0,771.0L294.0,771.0Q347.0,771.0 378.0,763.0Q409.0,755.0 431.0,734.0Q464.0,702.0 467.0,622.0L577.0,622.0L577.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L395.0,622.0Z" transform="translate(2679, 908)"/>
<path d="M-443.0,-187.0L-443.0,-116.0L-67.0,-116.0L-67.0,-187.0L-443.0,-187.0Z" transform="translate(3217, 595)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঞও়্꣱৾ফ্ল</span> (Added by SIESTA)</li>


<pre>Expected: nyabeng=0+1001|obeng=1+738|nuktabeng=1+0|viramabeng=1+0|uniA8F1=1@0,323+0|uni25CC=1+510|uni09FE=1+0|phalabeng=6+824</pre>



<pre>Got     : nyabeng=0+1019|obeng=1+738|nuktabeng=1+0|viramabeng=1+0|uniA8F1=1@0,323+0|uni25CC=1+510|uni09FE=1+0|phalabeng=6+824</pre>



<pre>                      +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3091 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(0, 908)"/>
<path d="M681.0,225.0Q681.0,142.0 619.5,92.0Q558.0,42.0 453.0,42.0Q359.0,42.0 279.0,87.5Q199.0,133.0 136.0,235.5Q73.0,338.0 28.0,507.0L103.0,529.0Q143.0,386.0 192.5,295.0Q242.0,204.0 306.5,161.0Q371.0,118.0 455.0,118.0Q518.0,118.0 559.0,144.5Q600.0,171.0 600.0,228.0Q600.0,255.0 587.0,276.5Q574.0,298.0 552.0,314.0Q520.0,297.0 480.0,282.0L449.0,354.0Q516.0,376.0 553.5,405.5Q591.0,435.0 591.0,482.0Q591.0,558.0 509.0,558.0Q461.0,558.0 420.5,537.5Q380.0,517.0 355.5,489.5Q331.0,462.0 331.0,439.0Q331.0,423.0 341.0,411.5Q351.0,400.0 386.0,395.0L365.0,321.0Q308.0,332.0 279.5,360.0Q251.0,388.0 251.0,431.0Q251.0,465.0 271.5,499.5Q292.0,534.0 328.0,563.5Q364.0,593.0 410.5,611.0Q457.0,629.0 509.0,629.0Q586.0,629.0 628.5,590.0Q671.0,551.0 671.0,483.0Q671.0,445.0 655.5,414.0Q640.0,383.0 613.0,358.0Q681.0,308.0 681.0,225.0Z" transform="translate(1019, 908)"/>
<path d="M-255.0,-183.0Q-280.0,-183.0 -297.5,-167.0Q-315.0,-151.0 -315.0,-125.0Q-315.0,-99.0 -297.5,-82.0Q-280.0,-65.0 -255.0,-65.0Q-230.0,-65.0 -212.5,-82.0Q-195.0,-99.0 -195.0,-125.0Q-195.0,-151.0 -212.5,-167.0Q-230.0,-183.0 -255.0,-183.0Z" transform="translate(1757, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(1757, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(1757, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1757, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(2267, 908)"/>
<path d="M176.0,183.0Q223.0,183.0 254.5,162.0Q286.0,141.0 306.0,109.0Q317.0,132.0 334.5,142.5Q352.0,153.0 370.0,153.0Q388.0,153.0 403.5,144.5Q419.0,136.0 434.0,122.0L434.0,143.0Q376.0,191.0 299.0,223.0Q222.0,255.0 115.0,263.0L79.0,351.0Q110.0,370.0 135.0,384.5Q160.0,399.0 186.5,412.0Q213.0,425.0 247.0,441.0Q168.0,494.0 68.0,512.0L86.0,551.0L-10.0,551.0L-10.0,622.0L834.0,622.0L834.0,551.0L185.0,551.0Q229.0,533.0 265.5,508.5Q302.0,484.0 331.0,458.0L336.0,404.0Q290.0,385.0 248.5,365.0Q207.0,345.0 168.0,324.0Q247.0,318.0 314.0,290.5Q381.0,263.0 433.0,223.0Q432.0,240.0 431.5,258.0Q431.0,276.0 431.0,295.0L431.0,510.0L444.0,510.0Q526.0,510.0 600.0,488.5Q674.0,467.0 725.0,414.0Q749.0,389.0 763.5,357.5Q778.0,326.0 778.0,288.0Q778.0,255.0 764.5,225.5Q751.0,196.0 721.0,177.0Q691.0,158.0 641.0,158.0Q626.0,158.0 611.5,159.0Q597.0,160.0 583.0,163.0L588.0,234.0Q594.0,233.0 603.0,232.5Q612.0,232.0 622.0,232.0Q670.0,232.0 685.0,251.0Q700.0,270.0 700.0,296.0Q700.0,347.0 648.5,386.0Q597.0,425.0 508.0,434.0L508.0,-43.0L431.0,-43.0L431.0,62.0Q420.0,72.0 408.0,78.5Q396.0,85.0 383.0,85.0Q368.0,85.0 355.0,73.5Q342.0,62.0 342.0,29.0Q342.0,22.0 342.5,15.5Q343.0,9.0 344.0,3.0L283.0,0.0Q278.0,51.0 252.0,83.0Q226.0,115.0 182.0,115.0Q154.0,115.0 138.5,100.0Q123.0,85.0 123.0,64.0Q123.0,36.0 142.5,18.5Q162.0,1.0 207.0,-16.0L178.0,-84.0Q118.0,-62.0 81.5,-26.5Q45.0,9.0 45.0,68.0Q45.0,118.0 82.0,150.5Q119.0,183.0 176.0,183.0Z" transform="translate(2267, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3073 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(0, 908)"/>
<path d="M681.0,225.0Q681.0,142.0 619.5,92.0Q558.0,42.0 453.0,42.0Q359.0,42.0 279.0,87.5Q199.0,133.0 136.0,235.5Q73.0,338.0 28.0,507.0L103.0,529.0Q143.0,386.0 192.5,295.0Q242.0,204.0 306.5,161.0Q371.0,118.0 455.0,118.0Q518.0,118.0 559.0,144.5Q600.0,171.0 600.0,228.0Q600.0,255.0 587.0,276.5Q574.0,298.0 552.0,314.0Q520.0,297.0 480.0,282.0L449.0,354.0Q516.0,376.0 553.5,405.5Q591.0,435.0 591.0,482.0Q591.0,558.0 509.0,558.0Q461.0,558.0 420.5,537.5Q380.0,517.0 355.5,489.5Q331.0,462.0 331.0,439.0Q331.0,423.0 341.0,411.5Q351.0,400.0 386.0,395.0L365.0,321.0Q308.0,332.0 279.5,360.0Q251.0,388.0 251.0,431.0Q251.0,465.0 271.5,499.5Q292.0,534.0 328.0,563.5Q364.0,593.0 410.5,611.0Q457.0,629.0 509.0,629.0Q586.0,629.0 628.5,590.0Q671.0,551.0 671.0,483.0Q671.0,445.0 655.5,414.0Q640.0,383.0 613.0,358.0Q681.0,308.0 681.0,225.0Z" transform="translate(1001, 908)"/>
<path d="M-255.0,-183.0Q-280.0,-183.0 -297.5,-167.0Q-315.0,-151.0 -315.0,-125.0Q-315.0,-99.0 -297.5,-82.0Q-280.0,-65.0 -255.0,-65.0Q-230.0,-65.0 -212.5,-82.0Q-195.0,-99.0 -195.0,-125.0Q-195.0,-151.0 -212.5,-167.0Q-230.0,-183.0 -255.0,-183.0Z" transform="translate(1739, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(1739, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(1739, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1739, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(2249, 908)"/>
<path d="M176.0,183.0Q223.0,183.0 254.5,162.0Q286.0,141.0 306.0,109.0Q317.0,132.0 334.5,142.5Q352.0,153.0 370.0,153.0Q388.0,153.0 403.5,144.5Q419.0,136.0 434.0,122.0L434.0,143.0Q376.0,191.0 299.0,223.0Q222.0,255.0 115.0,263.0L79.0,351.0Q110.0,370.0 135.0,384.5Q160.0,399.0 186.5,412.0Q213.0,425.0 247.0,441.0Q168.0,494.0 68.0,512.0L86.0,551.0L-10.0,551.0L-10.0,622.0L834.0,622.0L834.0,551.0L185.0,551.0Q229.0,533.0 265.5,508.5Q302.0,484.0 331.0,458.0L336.0,404.0Q290.0,385.0 248.5,365.0Q207.0,345.0 168.0,324.0Q247.0,318.0 314.0,290.5Q381.0,263.0 433.0,223.0Q432.0,240.0 431.5,258.0Q431.0,276.0 431.0,295.0L431.0,510.0L444.0,510.0Q526.0,510.0 600.0,488.5Q674.0,467.0 725.0,414.0Q749.0,389.0 763.5,357.5Q778.0,326.0 778.0,288.0Q778.0,255.0 764.5,225.5Q751.0,196.0 721.0,177.0Q691.0,158.0 641.0,158.0Q626.0,158.0 611.5,159.0Q597.0,160.0 583.0,163.0L588.0,234.0Q594.0,233.0 603.0,232.5Q612.0,232.0 622.0,232.0Q670.0,232.0 685.0,251.0Q700.0,270.0 700.0,296.0Q700.0,347.0 648.5,386.0Q597.0,425.0 508.0,434.0L508.0,-43.0L431.0,-43.0L431.0,62.0Q420.0,72.0 408.0,78.5Q396.0,85.0 383.0,85.0Q368.0,85.0 355.0,73.5Q342.0,62.0 342.0,29.0Q342.0,22.0 342.5,15.5Q343.0,9.0 344.0,3.0L283.0,0.0Q278.0,51.0 252.0,83.0Q226.0,115.0 182.0,115.0Q154.0,115.0 138.5,100.0Q123.0,85.0 123.0,64.0Q123.0,36.0 142.5,18.5Q162.0,1.0 207.0,-16.0L178.0,-84.0Q118.0,-62.0 81.5,-26.5Q45.0,9.0 45.0,68.0Q45.0,118.0 82.0,150.5Q119.0,183.0 176.0,183.0Z" transform="translate(2249, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ন়ঝৣঞ়টৃঁৎপ</span> (Added by SIESTA)</li>


<pre>Expected: nanuktabeng=0+604|jhabeng=2+794|llvocalicvowelsignbeng=2@-207,0+0|nyanuktabeng=4+1019|ttabeng=6+567|rvocalicvowelsignbeng=6@-83,0+0|candrabindualtbeng=6+0|khandatabeng=9+507|pabeng=10+716</pre>



<pre>Got     : nanuktabeng=0+604|jhabeng=2+794|llvocalicvowelsignbeng=2@-207,0+0|nyanuktabeng=4+1019|ttabeng=6+567|rvocalicvowelsignbeng=6@-83,0+0|candrabindualtbeng=6+0|khandatabeng=9+525|pabeng=10+716</pre>



<pre>                                                                                                                                                                                     ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4225 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M614.0,622.0L614.0,551.0L509.0,551.0L509.0,0.0L432.0,0.0L432.0,208.0Q384.0,269.0 327.0,310.0Q270.0,351.0 216.0,351.0Q179.0,351.0 153.5,331.5Q128.0,312.0 128.0,274.0Q128.0,218.0 214.0,184.0L176.0,113.0Q115.0,138.0 80.5,180.5Q46.0,223.0 46.0,277.0Q46.0,326.0 69.5,358.5Q93.0,391.0 129.5,407.0Q166.0,423.0 204.0,423.0Q275.0,423.0 330.5,389.5Q386.0,356.0 435.0,303.0Q433.0,320.0 432.5,337.0Q432.0,354.0 432.0,371.0L432.0,551.0L-10.0,551.0L-10.0,622.0L614.0,622.0ZM225.0,-91.0Q200.0,-91.0 182.5,-75.0Q165.0,-59.0 165.0,-33.0Q165.0,-7.0 182.5,10.0Q200.0,27.0 225.0,27.0Q250.0,27.0 267.5,10.0Q285.0,-7.0 285.0,-33.0Q285.0,-59.0 267.5,-75.0Q250.0,-91.0 225.0,-91.0Z" transform="translate(0, 908)"/>
<path d="M492.0,622.0L492.0,313.0Q528.0,290.0 565.5,253.0Q603.0,216.0 624.0,179.0Q622.0,210.0 622.0,257.0L622.0,688.0L675.0,688.0L698.0,622.0L804.0,622.0L804.0,551.0L699.0,551.0L699.0,73.0L622.0,73.0Q597.0,122.0 564.0,161.0Q531.0,200.0 492.0,230.0L492.0,0.0L415.0,0.0Q386.0,59.0 334.0,111.0Q282.0,163.0 215.5,198.5Q149.0,234.0 76.0,243.0L37.0,339.0Q127.0,393.0 222.0,439.0Q317.0,485.0 415.0,517.0L415.0,551.0L-10.0,551.0L-10.0,622.0L492.0,622.0ZM130.0,304.0Q183.0,294.0 239.0,266.0Q295.0,238.0 342.5,197.5Q390.0,157.0 418.0,109.0Q417.0,126.0 416.0,145.0Q415.0,164.0 415.0,189.0L415.0,439.0Q345.0,415.0 271.0,380.0Q197.0,345.0 130.0,304.0Z" transform="translate(604, 908)"/>
<path d="M-449.0,-208.0Q-395.0,-208.0 -368.0,-231.0Q-341.0,-254.0 -341.0,-289.0Q-341.0,-301.0 -345.5,-314.0Q-350.0,-327.0 -363.0,-339.0Q-303.0,-331.0 -279.0,-313.5Q-255.0,-296.0 -255.0,-268.0Q-255.0,-251.0 -263.5,-238.0Q-272.0,-225.0 -296.5,-212.0Q-321.0,-199.0 -369.0,-185.0Q-420.0,-169.0 -447.0,-152.5Q-474.0,-136.0 -474.0,-103.0Q-474.0,-86.0 -464.0,-68.0L-408.0,-81.0Q-412.0,-89.0 -412.0,-97.0Q-412.0,-107.0 -397.5,-114.0Q-383.0,-121.0 -334.0,-136.0Q-274.0,-154.0 -242.0,-173.5Q-210.0,-193.0 -198.5,-216.0Q-187.0,-239.0 -187.0,-266.0Q-187.0,-313.0 -219.0,-341.5Q-251.0,-370.0 -302.5,-382.0Q-354.0,-394.0 -415.0,-394.0L-439.0,-394.0L-451.0,-345.0Q-424.0,-337.0 -412.0,-324.5Q-400.0,-312.0 -400.0,-295.0Q-400.0,-280.0 -411.0,-270.5Q-422.0,-261.0 -447.0,-261.0Q-487.0,-261.0 -487.0,-285.0Q-487.0,-294.0 -480.0,-308.0L-540.0,-319.0Q-551.0,-299.0 -551.0,-276.0Q-551.0,-247.0 -525.5,-227.5Q-500.0,-208.0 -449.0,-208.0ZM-142.0,-127.0Q-88.0,-127.0 -61.0,-150.0Q-34.0,-173.0 -34.0,-208.0Q-34.0,-220.0 -38.5,-233.0Q-43.0,-246.0 -56.0,-258.0Q4.0,-250.0 28.0,-232.5Q52.0,-215.0 52.0,-187.0Q52.0,-170.0 43.5,-157.0Q35.0,-144.0 10.5,-131.0Q-14.0,-118.0 -62.0,-104.0Q-113.0,-88.0 -140.0,-71.5Q-167.0,-55.0 -167.0,-22.0Q-167.0,-5.0 -157.0,13.0L-101.0,0.0Q-105.0,-8.0 -105.0,-16.0Q-105.0,-26.0 -90.5,-33.0Q-76.0,-40.0 -27.0,-55.0Q33.0,-73.0 65.0,-92.5Q97.0,-112.0 108.5,-135.0Q120.0,-158.0 120.0,-185.0Q120.0,-232.0 88.0,-260.5Q56.0,-289.0 4.5,-301.0Q-47.0,-313.0 -108.0,-313.0L-132.0,-313.0L-144.0,-264.0Q-117.0,-256.0 -105.0,-243.5Q-93.0,-231.0 -93.0,-214.0Q-93.0,-199.0 -104.0,-189.5Q-115.0,-180.0 -140.0,-180.0Q-180.0,-180.0 -180.0,-204.0Q-180.0,-213.0 -173.0,-227.0L-233.0,-238.0Q-244.0,-218.0 -244.0,-195.0Q-244.0,-166.0 -218.5,-146.5Q-193.0,-127.0 -142.0,-127.0Z" transform="translate(1191, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0ZM393.0,-144.0Q368.0,-144.0 350.5,-128.0Q333.0,-112.0 333.0,-86.0Q333.0,-60.0 350.5,-43.0Q368.0,-26.0 393.0,-26.0Q418.0,-26.0 435.5,-43.0Q453.0,-60.0 453.0,-86.0Q453.0,-112.0 435.5,-128.0Q418.0,-144.0 393.0,-144.0Z" transform="translate(1398, 908)"/>
<path d="M395.0,622.0Q394.0,663.0 375.5,681.0Q357.0,699.0 315.0,699.0L221.0,699.0Q156.0,699.0 120.5,708.0Q85.0,717.0 60.0,736.0Q6.0,777.0 6.0,859.0Q6.0,872.0 7.5,884.5Q9.0,897.0 11.0,912.0L85.0,907.0Q81.0,887.0 81.0,869.0Q81.0,847.0 85.5,830.0Q90.0,813.0 100.0,802.0Q114.0,786.0 140.5,778.5Q167.0,771.0 216.0,771.0L294.0,771.0Q347.0,771.0 378.0,763.0Q409.0,755.0 431.0,734.0Q464.0,702.0 467.0,622.0L577.0,622.0L577.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L395.0,622.0Z" transform="translate(2417, 908)"/>
<path d="M-355.0,-80.0Q-296.0,-51.0 -233.0,-24.5Q-170.0,2.0 -105.0,25.0L-79.0,-41.0Q-126.0,-56.0 -173.5,-72.0Q-221.0,-88.0 -259.0,-105.0Q-157.0,-118.0 -87.5,-149.0Q-18.0,-180.0 35.0,-214.0L-1.0,-271.0Q-79.0,-221.0 -154.0,-195.5Q-229.0,-170.0 -321.0,-160.0L-355.0,-80.0Z" transform="translate(2901, 908)"/>
<path d="M-109.0,874.0Q-109.0,854.0 -121.5,843.0Q-134.0,832.0 -153.0,832.0Q-175.0,832.0 -186.0,844.5Q-197.0,857.0 -197.0,877.0Q-197.0,893.0 -186.5,905.0Q-176.0,917.0 -154.0,917.0Q-109.0,917.0 -109.0,874.0ZM18.0,905.0Q11.0,831.0 -28.5,783.0Q-68.0,735.0 -150.0,735.0Q-232.0,735.0 -274.0,783.0Q-316.0,831.0 -324.0,904.0L-256.0,913.0Q-251.0,860.0 -228.0,829.5Q-205.0,799.0 -154.0,799.0Q-106.0,799.0 -81.0,828.5Q-56.0,858.0 -51.0,914.0L18.0,905.0Z" transform="translate(2984, 908)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(2984, 908)"/>
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(3509, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4207 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M614.0,622.0L614.0,551.0L509.0,551.0L509.0,0.0L432.0,0.0L432.0,208.0Q384.0,269.0 327.0,310.0Q270.0,351.0 216.0,351.0Q179.0,351.0 153.5,331.5Q128.0,312.0 128.0,274.0Q128.0,218.0 214.0,184.0L176.0,113.0Q115.0,138.0 80.5,180.5Q46.0,223.0 46.0,277.0Q46.0,326.0 69.5,358.5Q93.0,391.0 129.5,407.0Q166.0,423.0 204.0,423.0Q275.0,423.0 330.5,389.5Q386.0,356.0 435.0,303.0Q433.0,320.0 432.5,337.0Q432.0,354.0 432.0,371.0L432.0,551.0L-10.0,551.0L-10.0,622.0L614.0,622.0ZM225.0,-91.0Q200.0,-91.0 182.5,-75.0Q165.0,-59.0 165.0,-33.0Q165.0,-7.0 182.5,10.0Q200.0,27.0 225.0,27.0Q250.0,27.0 267.5,10.0Q285.0,-7.0 285.0,-33.0Q285.0,-59.0 267.5,-75.0Q250.0,-91.0 225.0,-91.0Z" transform="translate(0, 908)"/>
<path d="M492.0,622.0L492.0,313.0Q528.0,290.0 565.5,253.0Q603.0,216.0 624.0,179.0Q622.0,210.0 622.0,257.0L622.0,688.0L675.0,688.0L698.0,622.0L804.0,622.0L804.0,551.0L699.0,551.0L699.0,73.0L622.0,73.0Q597.0,122.0 564.0,161.0Q531.0,200.0 492.0,230.0L492.0,0.0L415.0,0.0Q386.0,59.0 334.0,111.0Q282.0,163.0 215.5,198.5Q149.0,234.0 76.0,243.0L37.0,339.0Q127.0,393.0 222.0,439.0Q317.0,485.0 415.0,517.0L415.0,551.0L-10.0,551.0L-10.0,622.0L492.0,622.0ZM130.0,304.0Q183.0,294.0 239.0,266.0Q295.0,238.0 342.5,197.5Q390.0,157.0 418.0,109.0Q417.0,126.0 416.0,145.0Q415.0,164.0 415.0,189.0L415.0,439.0Q345.0,415.0 271.0,380.0Q197.0,345.0 130.0,304.0Z" transform="translate(604, 908)"/>
<path d="M-449.0,-208.0Q-395.0,-208.0 -368.0,-231.0Q-341.0,-254.0 -341.0,-289.0Q-341.0,-301.0 -345.5,-314.0Q-350.0,-327.0 -363.0,-339.0Q-303.0,-331.0 -279.0,-313.5Q-255.0,-296.0 -255.0,-268.0Q-255.0,-251.0 -263.5,-238.0Q-272.0,-225.0 -296.5,-212.0Q-321.0,-199.0 -369.0,-185.0Q-420.0,-169.0 -447.0,-152.5Q-474.0,-136.0 -474.0,-103.0Q-474.0,-86.0 -464.0,-68.0L-408.0,-81.0Q-412.0,-89.0 -412.0,-97.0Q-412.0,-107.0 -397.5,-114.0Q-383.0,-121.0 -334.0,-136.0Q-274.0,-154.0 -242.0,-173.5Q-210.0,-193.0 -198.5,-216.0Q-187.0,-239.0 -187.0,-266.0Q-187.0,-313.0 -219.0,-341.5Q-251.0,-370.0 -302.5,-382.0Q-354.0,-394.0 -415.0,-394.0L-439.0,-394.0L-451.0,-345.0Q-424.0,-337.0 -412.0,-324.5Q-400.0,-312.0 -400.0,-295.0Q-400.0,-280.0 -411.0,-270.5Q-422.0,-261.0 -447.0,-261.0Q-487.0,-261.0 -487.0,-285.0Q-487.0,-294.0 -480.0,-308.0L-540.0,-319.0Q-551.0,-299.0 -551.0,-276.0Q-551.0,-247.0 -525.5,-227.5Q-500.0,-208.0 -449.0,-208.0ZM-142.0,-127.0Q-88.0,-127.0 -61.0,-150.0Q-34.0,-173.0 -34.0,-208.0Q-34.0,-220.0 -38.5,-233.0Q-43.0,-246.0 -56.0,-258.0Q4.0,-250.0 28.0,-232.5Q52.0,-215.0 52.0,-187.0Q52.0,-170.0 43.5,-157.0Q35.0,-144.0 10.5,-131.0Q-14.0,-118.0 -62.0,-104.0Q-113.0,-88.0 -140.0,-71.5Q-167.0,-55.0 -167.0,-22.0Q-167.0,-5.0 -157.0,13.0L-101.0,0.0Q-105.0,-8.0 -105.0,-16.0Q-105.0,-26.0 -90.5,-33.0Q-76.0,-40.0 -27.0,-55.0Q33.0,-73.0 65.0,-92.5Q97.0,-112.0 108.5,-135.0Q120.0,-158.0 120.0,-185.0Q120.0,-232.0 88.0,-260.5Q56.0,-289.0 4.5,-301.0Q-47.0,-313.0 -108.0,-313.0L-132.0,-313.0L-144.0,-264.0Q-117.0,-256.0 -105.0,-243.5Q-93.0,-231.0 -93.0,-214.0Q-93.0,-199.0 -104.0,-189.5Q-115.0,-180.0 -140.0,-180.0Q-180.0,-180.0 -180.0,-204.0Q-180.0,-213.0 -173.0,-227.0L-233.0,-238.0Q-244.0,-218.0 -244.0,-195.0Q-244.0,-166.0 -218.5,-146.5Q-193.0,-127.0 -142.0,-127.0Z" transform="translate(1191, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0ZM393.0,-144.0Q368.0,-144.0 350.5,-128.0Q333.0,-112.0 333.0,-86.0Q333.0,-60.0 350.5,-43.0Q368.0,-26.0 393.0,-26.0Q418.0,-26.0 435.5,-43.0Q453.0,-60.0 453.0,-86.0Q453.0,-112.0 435.5,-128.0Q418.0,-144.0 393.0,-144.0Z" transform="translate(1398, 908)"/>
<path d="M395.0,622.0Q394.0,663.0 375.5,681.0Q357.0,699.0 315.0,699.0L221.0,699.0Q156.0,699.0 120.5,708.0Q85.0,717.0 60.0,736.0Q6.0,777.0 6.0,859.0Q6.0,872.0 7.5,884.5Q9.0,897.0 11.0,912.0L85.0,907.0Q81.0,887.0 81.0,869.0Q81.0,847.0 85.5,830.0Q90.0,813.0 100.0,802.0Q114.0,786.0 140.5,778.5Q167.0,771.0 216.0,771.0L294.0,771.0Q347.0,771.0 378.0,763.0Q409.0,755.0 431.0,734.0Q464.0,702.0 467.0,622.0L577.0,622.0L577.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L395.0,622.0Z" transform="translate(2417, 908)"/>
<path d="M-355.0,-80.0Q-296.0,-51.0 -233.0,-24.5Q-170.0,2.0 -105.0,25.0L-79.0,-41.0Q-126.0,-56.0 -173.5,-72.0Q-221.0,-88.0 -259.0,-105.0Q-157.0,-118.0 -87.5,-149.0Q-18.0,-180.0 35.0,-214.0L-1.0,-271.0Q-79.0,-221.0 -154.0,-195.5Q-229.0,-170.0 -321.0,-160.0L-355.0,-80.0Z" transform="translate(2901, 908)"/>
<path d="M-109.0,874.0Q-109.0,854.0 -121.5,843.0Q-134.0,832.0 -153.0,832.0Q-175.0,832.0 -186.0,844.5Q-197.0,857.0 -197.0,877.0Q-197.0,893.0 -186.5,905.0Q-176.0,917.0 -154.0,917.0Q-109.0,917.0 -109.0,874.0ZM18.0,905.0Q11.0,831.0 -28.5,783.0Q-68.0,735.0 -150.0,735.0Q-232.0,735.0 -274.0,783.0Q-316.0,831.0 -324.0,904.0L-256.0,913.0Q-251.0,860.0 -228.0,829.5Q-205.0,799.0 -154.0,799.0Q-106.0,799.0 -81.0,828.5Q-56.0,858.0 -51.0,914.0L18.0,905.0Z" transform="translate(2984, 908)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(2984, 908)"/>
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(3491, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ৄ৾শ‍ুৎৎ</span> (Added by SIESTA)</li>


<pre>Expected: uni25CC=0+510|rrvocalicvowelsignbeng=0+0|uni09FE=0@0,323+0|shubeng=2+807|khandatabeng=5+507|khandatabeng=6+525</pre>



<pre>Got     : uni25CC=0+510|rrvocalicvowelsignbeng=0@19,3+0|uni09FE=0@0,323+0|shubeng=2+825|khandatabeng=5+525|khandatabeng=6+525</pre>



<pre>                                                                                ^^                 ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2385 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(0, 908)"/>
<path d="M-355.0,-80.0Q-296.0,-51.0 -233.0,-24.5Q-170.0,2.0 -105.0,25.0L-79.0,-41.0Q-124.0,-54.0 -175.5,-71.5Q-227.0,-89.0 -263.0,-106.0Q-175.0,-121.0 -103.0,-149.0Q-31.0,-177.0 28.0,-211.0L-3.0,-261.0Q-34.0,-244.0 -63.5,-230.5Q-93.0,-217.0 -121.0,-206.0Q-157.0,-218.0 -197.5,-233.5Q-238.0,-249.0 -263.0,-260.0Q-209.0,-268.0 -148.5,-288.0Q-88.0,-308.0 -32.0,-342.0L-63.0,-394.0Q-128.0,-356.0 -190.5,-339.0Q-253.0,-322.0 -323.0,-312.0L-355.0,-238.0Q-320.0,-222.0 -284.5,-206.5Q-249.0,-191.0 -207.0,-178.0Q-234.0,-171.0 -262.0,-167.0Q-290.0,-163.0 -321.0,-160.0L-355.0,-80.0Z" transform="translate(529, 911)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(510, 1231)"/>
<path d="M519.0,32.0Q410.0,32.0 315.5,75.0Q221.0,118.0 148.0,213.0Q75.0,308.0 28.0,464.0L102.0,487.0Q167.0,286.0 268.5,197.0Q370.0,108.0 517.0,108.0Q594.0,108.0 640.5,134.5Q687.0,161.0 687.0,218.0Q687.0,242.0 678.0,261.0Q669.0,280.0 653.0,295.0Q616.0,270.0 566.0,250.0L535.0,323.0Q602.0,348.0 641.5,381.5Q681.0,415.0 681.0,470.0Q681.0,490.0 674.0,509.0Q667.0,528.0 651.0,544.0L582.0,459.0L521.0,457.0Q512.0,509.0 491.5,532.5Q471.0,556.0 439.0,556.0Q411.0,556.0 392.5,539.5Q374.0,523.0 374.0,490.0Q374.0,458.0 398.0,438.0Q422.0,418.0 476.0,416.0L471.0,339.0Q418.0,342.0 384.0,361.5Q350.0,381.0 333.0,413.0Q317.0,380.0 283.5,358.5Q250.0,337.0 196.0,337.0L189.0,414.0Q247.0,415.0 268.0,438.0Q289.0,461.0 289.0,486.0Q289.0,519.0 267.5,537.5Q246.0,556.0 203.0,556.0Q185.0,556.0 171.5,553.0Q158.0,550.0 141.0,545.0L133.0,620.0Q154.0,625.0 171.0,627.0Q188.0,629.0 207.0,629.0Q243.0,629.0 276.5,613.0Q310.0,597.0 329.0,562.0Q345.0,596.0 375.0,612.5Q405.0,629.0 440.0,629.0Q480.0,629.0 508.5,610.0Q537.0,591.0 562.0,542.0L616.0,608.0L677.0,622.0Q709.0,597.0 733.0,559.5Q757.0,522.0 757.0,471.0Q757.0,433.0 744.0,401.0Q731.0,369.0 708.0,342.0Q768.0,293.0 768.0,212.0Q768.0,131.0 701.5,81.5Q635.0,32.0 519.0,32.0Z" transform="translate(510, 908)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(1335, 908)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(1860, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2349 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(0, 908)"/>
<path d="M-355.0,-80.0Q-296.0,-51.0 -233.0,-24.5Q-170.0,2.0 -105.0,25.0L-79.0,-41.0Q-124.0,-54.0 -175.5,-71.5Q-227.0,-89.0 -263.0,-106.0Q-175.0,-121.0 -103.0,-149.0Q-31.0,-177.0 28.0,-211.0L-3.0,-261.0Q-34.0,-244.0 -63.5,-230.5Q-93.0,-217.0 -121.0,-206.0Q-157.0,-218.0 -197.5,-233.5Q-238.0,-249.0 -263.0,-260.0Q-209.0,-268.0 -148.5,-288.0Q-88.0,-308.0 -32.0,-342.0L-63.0,-394.0Q-128.0,-356.0 -190.5,-339.0Q-253.0,-322.0 -323.0,-312.0L-355.0,-238.0Q-320.0,-222.0 -284.5,-206.5Q-249.0,-191.0 -207.0,-178.0Q-234.0,-171.0 -262.0,-167.0Q-290.0,-163.0 -321.0,-160.0L-355.0,-80.0Z" transform="translate(510, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(510, 1231)"/>
<path d="M519.0,32.0Q410.0,32.0 315.5,75.0Q221.0,118.0 148.0,213.0Q75.0,308.0 28.0,464.0L102.0,487.0Q167.0,286.0 268.5,197.0Q370.0,108.0 517.0,108.0Q594.0,108.0 640.5,134.5Q687.0,161.0 687.0,218.0Q687.0,242.0 678.0,261.0Q669.0,280.0 653.0,295.0Q616.0,270.0 566.0,250.0L535.0,323.0Q602.0,348.0 641.5,381.5Q681.0,415.0 681.0,470.0Q681.0,490.0 674.0,509.0Q667.0,528.0 651.0,544.0L582.0,459.0L521.0,457.0Q512.0,509.0 491.5,532.5Q471.0,556.0 439.0,556.0Q411.0,556.0 392.5,539.5Q374.0,523.0 374.0,490.0Q374.0,458.0 398.0,438.0Q422.0,418.0 476.0,416.0L471.0,339.0Q418.0,342.0 384.0,361.5Q350.0,381.0 333.0,413.0Q317.0,380.0 283.5,358.5Q250.0,337.0 196.0,337.0L189.0,414.0Q247.0,415.0 268.0,438.0Q289.0,461.0 289.0,486.0Q289.0,519.0 267.5,537.5Q246.0,556.0 203.0,556.0Q185.0,556.0 171.5,553.0Q158.0,550.0 141.0,545.0L133.0,620.0Q154.0,625.0 171.0,627.0Q188.0,629.0 207.0,629.0Q243.0,629.0 276.5,613.0Q310.0,597.0 329.0,562.0Q345.0,596.0 375.0,612.5Q405.0,629.0 440.0,629.0Q480.0,629.0 508.5,610.0Q537.0,591.0 562.0,542.0L616.0,608.0L677.0,622.0Q709.0,597.0 733.0,559.5Q757.0,522.0 757.0,471.0Q757.0,433.0 744.0,401.0Q731.0,369.0 708.0,342.0Q768.0,293.0 768.0,212.0Q768.0,131.0 701.5,81.5Q635.0,32.0 519.0,32.0Z" transform="translate(510, 908)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(1317, 908)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(1824, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ফ়ৡগপৣ</span> (Added by SIESTA)</li>


<pre>Expected: phanuktabeng=0+838|llvocalicbeng=2+621|gabeng=3+656|pabeng=4+716|llvocalicvowelsignbeng=4+0</pre>



<pre>Got     : phanuktabeng=0+838|llvocalicbeng=2+639|gabeng=3+656|pabeng=4+716|llvocalicvowelsignbeng=4+0</pre>



<pre>                                              ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2849 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M848.0,622.0L848.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.5,327.5Q184.0,301.0 142.0,276.0Q246.0,250.0 316.0,207.5Q386.0,165.0 447.0,99.0Q446.0,116.0 445.5,134.0Q445.0,152.0 445.0,171.0L445.0,510.0L458.0,510.0Q540.0,510.0 614.0,488.5Q688.0,467.0 739.0,414.0Q763.0,389.0 777.5,357.5Q792.0,326.0 792.0,288.0Q792.0,255.0 778.5,225.5Q765.0,196.0 735.0,177.0Q705.0,158.0 655.0,158.0Q640.0,158.0 625.5,159.0Q611.0,160.0 597.0,163.0L602.0,234.0Q608.0,233.0 617.0,232.5Q626.0,232.0 636.0,232.0Q685.0,232.0 699.5,251.0Q714.0,270.0 714.0,296.0Q714.0,347.0 662.5,386.0Q611.0,425.0 522.0,434.0L522.0,0.0L445.0,0.0Q404.0,56.0 354.5,98.0Q305.0,140.0 239.5,168.5Q174.0,197.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L848.0,622.0ZM180.0,-6.0Q155.0,-6.0 137.5,10.0Q120.0,26.0 120.0,52.0Q120.0,78.0 137.5,95.0Q155.0,112.0 180.0,112.0Q205.0,112.0 222.5,95.0Q240.0,78.0 240.0,52.0Q240.0,26.0 222.5,10.0Q205.0,-6.0 180.0,-6.0Z" transform="translate(0, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0ZM243.0,-107.0Q297.0,-107.0 324.0,-130.0Q351.0,-153.0 351.0,-188.0Q351.0,-200.0 346.5,-213.0Q342.0,-226.0 329.0,-238.0Q389.0,-230.0 413.0,-212.5Q437.0,-195.0 437.0,-167.0Q437.0,-150.0 428.5,-137.0Q420.0,-124.0 395.5,-111.0Q371.0,-98.0 323.0,-84.0Q272.0,-68.0 245.0,-51.5Q218.0,-35.0 218.0,-2.0Q218.0,15.0 228.0,33.0L284.0,20.0Q280.0,12.0 280.0,4.0Q280.0,-6.0 294.5,-13.0Q309.0,-20.0 358.0,-35.0Q418.0,-53.0 450.0,-72.5Q482.0,-92.0 493.5,-115.0Q505.0,-138.0 505.0,-165.0Q505.0,-212.0 473.0,-240.5Q441.0,-269.0 389.5,-281.0Q338.0,-293.0 277.0,-293.0L253.0,-293.0L241.0,-244.0Q268.0,-236.0 280.0,-223.5Q292.0,-211.0 292.0,-194.0Q292.0,-179.0 281.0,-169.5Q270.0,-160.0 245.0,-160.0Q205.0,-160.0 205.0,-184.0Q205.0,-193.0 212.0,-207.0L152.0,-218.0Q141.0,-198.0 141.0,-175.0Q141.0,-146.0 166.5,-126.5Q192.0,-107.0 243.0,-107.0Z" transform="translate(838, 908)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(1477, 908)"/>
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(2133, 908)"/>
<path d="M-449.0,-208.0Q-395.0,-208.0 -368.0,-231.0Q-341.0,-254.0 -341.0,-289.0Q-341.0,-301.0 -345.5,-314.0Q-350.0,-327.0 -363.0,-339.0Q-303.0,-331.0 -279.0,-313.5Q-255.0,-296.0 -255.0,-268.0Q-255.0,-251.0 -263.5,-238.0Q-272.0,-225.0 -296.5,-212.0Q-321.0,-199.0 -369.0,-185.0Q-420.0,-169.0 -447.0,-152.5Q-474.0,-136.0 -474.0,-103.0Q-474.0,-86.0 -464.0,-68.0L-408.0,-81.0Q-412.0,-89.0 -412.0,-97.0Q-412.0,-107.0 -397.5,-114.0Q-383.0,-121.0 -334.0,-136.0Q-274.0,-154.0 -242.0,-173.5Q-210.0,-193.0 -198.5,-216.0Q-187.0,-239.0 -187.0,-266.0Q-187.0,-313.0 -219.0,-341.5Q-251.0,-370.0 -302.5,-382.0Q-354.0,-394.0 -415.0,-394.0L-439.0,-394.0L-451.0,-345.0Q-424.0,-337.0 -412.0,-324.5Q-400.0,-312.0 -400.0,-295.0Q-400.0,-280.0 -411.0,-270.5Q-422.0,-261.0 -447.0,-261.0Q-487.0,-261.0 -487.0,-285.0Q-487.0,-294.0 -480.0,-308.0L-540.0,-319.0Q-551.0,-299.0 -551.0,-276.0Q-551.0,-247.0 -525.5,-227.5Q-500.0,-208.0 -449.0,-208.0ZM-142.0,-127.0Q-88.0,-127.0 -61.0,-150.0Q-34.0,-173.0 -34.0,-208.0Q-34.0,-220.0 -38.5,-233.0Q-43.0,-246.0 -56.0,-258.0Q4.0,-250.0 28.0,-232.5Q52.0,-215.0 52.0,-187.0Q52.0,-170.0 43.5,-157.0Q35.0,-144.0 10.5,-131.0Q-14.0,-118.0 -62.0,-104.0Q-113.0,-88.0 -140.0,-71.5Q-167.0,-55.0 -167.0,-22.0Q-167.0,-5.0 -157.0,13.0L-101.0,0.0Q-105.0,-8.0 -105.0,-16.0Q-105.0,-26.0 -90.5,-33.0Q-76.0,-40.0 -27.0,-55.0Q33.0,-73.0 65.0,-92.5Q97.0,-112.0 108.5,-135.0Q120.0,-158.0 120.0,-185.0Q120.0,-232.0 88.0,-260.5Q56.0,-289.0 4.5,-301.0Q-47.0,-313.0 -108.0,-313.0L-132.0,-313.0L-144.0,-264.0Q-117.0,-256.0 -105.0,-243.5Q-93.0,-231.0 -93.0,-214.0Q-93.0,-199.0 -104.0,-189.5Q-115.0,-180.0 -140.0,-180.0Q-180.0,-180.0 -180.0,-204.0Q-180.0,-213.0 -173.0,-227.0L-233.0,-238.0Q-244.0,-218.0 -244.0,-195.0Q-244.0,-166.0 -218.5,-146.5Q-193.0,-127.0 -142.0,-127.0Z" transform="translate(2849, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2831 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M848.0,622.0L848.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.5,327.5Q184.0,301.0 142.0,276.0Q246.0,250.0 316.0,207.5Q386.0,165.0 447.0,99.0Q446.0,116.0 445.5,134.0Q445.0,152.0 445.0,171.0L445.0,510.0L458.0,510.0Q540.0,510.0 614.0,488.5Q688.0,467.0 739.0,414.0Q763.0,389.0 777.5,357.5Q792.0,326.0 792.0,288.0Q792.0,255.0 778.5,225.5Q765.0,196.0 735.0,177.0Q705.0,158.0 655.0,158.0Q640.0,158.0 625.5,159.0Q611.0,160.0 597.0,163.0L602.0,234.0Q608.0,233.0 617.0,232.5Q626.0,232.0 636.0,232.0Q685.0,232.0 699.5,251.0Q714.0,270.0 714.0,296.0Q714.0,347.0 662.5,386.0Q611.0,425.0 522.0,434.0L522.0,0.0L445.0,0.0Q404.0,56.0 354.5,98.0Q305.0,140.0 239.5,168.5Q174.0,197.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L848.0,622.0ZM180.0,-6.0Q155.0,-6.0 137.5,10.0Q120.0,26.0 120.0,52.0Q120.0,78.0 137.5,95.0Q155.0,112.0 180.0,112.0Q205.0,112.0 222.5,95.0Q240.0,78.0 240.0,52.0Q240.0,26.0 222.5,10.0Q205.0,-6.0 180.0,-6.0Z" transform="translate(0, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0ZM243.0,-107.0Q297.0,-107.0 324.0,-130.0Q351.0,-153.0 351.0,-188.0Q351.0,-200.0 346.5,-213.0Q342.0,-226.0 329.0,-238.0Q389.0,-230.0 413.0,-212.5Q437.0,-195.0 437.0,-167.0Q437.0,-150.0 428.5,-137.0Q420.0,-124.0 395.5,-111.0Q371.0,-98.0 323.0,-84.0Q272.0,-68.0 245.0,-51.5Q218.0,-35.0 218.0,-2.0Q218.0,15.0 228.0,33.0L284.0,20.0Q280.0,12.0 280.0,4.0Q280.0,-6.0 294.5,-13.0Q309.0,-20.0 358.0,-35.0Q418.0,-53.0 450.0,-72.5Q482.0,-92.0 493.5,-115.0Q505.0,-138.0 505.0,-165.0Q505.0,-212.0 473.0,-240.5Q441.0,-269.0 389.5,-281.0Q338.0,-293.0 277.0,-293.0L253.0,-293.0L241.0,-244.0Q268.0,-236.0 280.0,-223.5Q292.0,-211.0 292.0,-194.0Q292.0,-179.0 281.0,-169.5Q270.0,-160.0 245.0,-160.0Q205.0,-160.0 205.0,-184.0Q205.0,-193.0 212.0,-207.0L152.0,-218.0Q141.0,-198.0 141.0,-175.0Q141.0,-146.0 166.5,-126.5Q192.0,-107.0 243.0,-107.0Z" transform="translate(838, 908)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(1459, 908)"/>
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(2115, 908)"/>
<path d="M-449.0,-208.0Q-395.0,-208.0 -368.0,-231.0Q-341.0,-254.0 -341.0,-289.0Q-341.0,-301.0 -345.5,-314.0Q-350.0,-327.0 -363.0,-339.0Q-303.0,-331.0 -279.0,-313.5Q-255.0,-296.0 -255.0,-268.0Q-255.0,-251.0 -263.5,-238.0Q-272.0,-225.0 -296.5,-212.0Q-321.0,-199.0 -369.0,-185.0Q-420.0,-169.0 -447.0,-152.5Q-474.0,-136.0 -474.0,-103.0Q-474.0,-86.0 -464.0,-68.0L-408.0,-81.0Q-412.0,-89.0 -412.0,-97.0Q-412.0,-107.0 -397.5,-114.0Q-383.0,-121.0 -334.0,-136.0Q-274.0,-154.0 -242.0,-173.5Q-210.0,-193.0 -198.5,-216.0Q-187.0,-239.0 -187.0,-266.0Q-187.0,-313.0 -219.0,-341.5Q-251.0,-370.0 -302.5,-382.0Q-354.0,-394.0 -415.0,-394.0L-439.0,-394.0L-451.0,-345.0Q-424.0,-337.0 -412.0,-324.5Q-400.0,-312.0 -400.0,-295.0Q-400.0,-280.0 -411.0,-270.5Q-422.0,-261.0 -447.0,-261.0Q-487.0,-261.0 -487.0,-285.0Q-487.0,-294.0 -480.0,-308.0L-540.0,-319.0Q-551.0,-299.0 -551.0,-276.0Q-551.0,-247.0 -525.5,-227.5Q-500.0,-208.0 -449.0,-208.0ZM-142.0,-127.0Q-88.0,-127.0 -61.0,-150.0Q-34.0,-173.0 -34.0,-208.0Q-34.0,-220.0 -38.5,-233.0Q-43.0,-246.0 -56.0,-258.0Q4.0,-250.0 28.0,-232.5Q52.0,-215.0 52.0,-187.0Q52.0,-170.0 43.5,-157.0Q35.0,-144.0 10.5,-131.0Q-14.0,-118.0 -62.0,-104.0Q-113.0,-88.0 -140.0,-71.5Q-167.0,-55.0 -167.0,-22.0Q-167.0,-5.0 -157.0,13.0L-101.0,0.0Q-105.0,-8.0 -105.0,-16.0Q-105.0,-26.0 -90.5,-33.0Q-76.0,-40.0 -27.0,-55.0Q33.0,-73.0 65.0,-92.5Q97.0,-112.0 108.5,-135.0Q120.0,-158.0 120.0,-185.0Q120.0,-232.0 88.0,-260.5Q56.0,-289.0 4.5,-301.0Q-47.0,-313.0 -108.0,-313.0L-132.0,-313.0L-144.0,-264.0Q-117.0,-256.0 -105.0,-243.5Q-93.0,-231.0 -93.0,-214.0Q-93.0,-199.0 -104.0,-189.5Q-115.0,-180.0 -140.0,-180.0Q-180.0,-180.0 -180.0,-204.0Q-180.0,-213.0 -173.0,-227.0L-233.0,-238.0Q-244.0,-218.0 -244.0,-195.0Q-244.0,-166.0 -218.5,-146.5Q-193.0,-127.0 -142.0,-127.0Z" transform="translate(2831, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঌঔত্ম‌꣱</span> (Added by SIESTA)</li>


<pre>Expected: lvocalicbeng=0+621|aubeng=1+874|tamabeng=2+901|space=5+0|uni25CC=5+510|uniA8F1=5+0</pre>



<pre>Got     : lvocalicbeng=0+639|aubeng=1+874|tamabeng=2+901|space=5+0|uni25CC=5+510|uniA8F1=5+0</pre>



<pre>                          ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2924 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0Z" transform="translate(0, 908)"/>
<path d="M681.0,225.0Q681.0,142.0 619.5,92.0Q558.0,42.0 453.0,42.0Q359.0,42.0 279.0,87.5Q199.0,133.0 136.0,235.5Q73.0,338.0 28.0,507.0L103.0,529.0Q143.0,386.0 192.5,295.0Q242.0,204.0 306.5,161.0Q371.0,118.0 455.0,118.0Q518.0,118.0 559.0,144.5Q600.0,171.0 600.0,228.0Q600.0,255.0 587.0,276.5Q574.0,298.0 551.0,314.0Q535.0,305.0 517.0,297.0Q499.0,289.0 480.0,282.0L449.0,354.0Q516.0,376.0 553.5,405.5Q591.0,435.0 591.0,482.0Q591.0,558.0 509.0,558.0Q461.0,558.0 420.5,537.5Q380.0,517.0 355.5,489.5Q331.0,462.0 331.0,439.0Q331.0,423.0 341.0,411.5Q351.0,400.0 386.0,395.0L365.0,321.0Q308.0,332.0 279.5,360.0Q251.0,388.0 251.0,431.0Q251.0,465.0 271.5,499.5Q292.0,534.0 328.0,563.5Q364.0,593.0 410.5,611.0Q457.0,629.0 509.0,629.0Q586.0,629.0 628.0,590.5Q670.0,552.0 670.0,488.0Q670.0,466.0 659.0,443.0Q697.0,464.0 725.5,495.0Q754.0,526.0 754.0,570.0Q754.0,596.0 746.0,614.0Q738.0,632.0 724.0,646.0Q706.0,664.0 675.0,674.5Q644.0,685.0 600.0,691.0L482.0,707.0Q387.0,721.0 346.0,760.0Q305.0,799.0 305.0,875.0Q305.0,883.0 306.5,895.0Q308.0,907.0 309.0,917.0L383.0,913.0Q380.0,895.0 380.0,878.0Q380.0,838.0 400.0,814.0Q411.0,802.0 429.5,794.0Q448.0,786.0 484.0,781.0L625.0,762.0Q677.0,755.0 711.5,742.5Q746.0,730.0 771.0,710.0Q832.0,663.0 832.0,577.0Q832.0,522.0 805.5,481.5Q779.0,441.0 731.5,410.0Q684.0,379.0 620.0,352.0Q681.0,303.0 681.0,225.0Z" transform="translate(639, 908)"/>
<path d="M358.0,185.0Q287.0,185.0 225.0,215.0Q163.0,245.0 113.5,312.5Q64.0,380.0 29.0,492.0L102.0,513.0Q143.0,382.0 200.5,320.0Q258.0,258.0 354.0,258.0Q409.0,258.0 440.5,272.5Q472.0,287.0 485.0,311.0Q498.0,335.0 498.0,364.0Q498.0,405.0 471.0,432.5Q444.0,460.0 397.0,460.0Q363.0,460.0 347.0,444.5Q331.0,429.0 331.0,406.0Q331.0,399.0 332.5,389.5Q334.0,380.0 337.0,372.0L264.0,358.0Q258.0,373.0 255.5,390.0Q253.0,407.0 253.0,419.0Q253.0,472.0 294.5,499.5Q336.0,527.0 392.0,527.0Q451.0,527.0 491.0,503.5Q531.0,480.0 552.0,442.5Q573.0,405.0 573.0,361.0Q573.0,301.0 541.0,258.0Q560.0,243.0 576.0,218.5Q592.0,194.0 592.0,154.0Q631.0,141.0 665.0,115.5Q699.0,90.0 730.0,55.0Q729.0,75.0 729.0,95.0Q729.0,115.0 729.0,136.0L729.0,551.0L-10.0,551.0L-10.0,622.0L911.0,622.0L911.0,551.0L806.0,551.0L806.0,-72.0L729.0,-72.0L729.0,-42.0Q685.0,16.0 636.5,55.0Q588.0,94.0 531.0,94.0Q509.0,94.0 496.0,83.5Q483.0,73.0 483.0,56.0Q483.0,36.0 497.0,24.5Q511.0,13.0 538.0,3.0L503.0,-66.0Q457.0,-48.0 430.0,-17.0Q403.0,14.0 403.0,56.0Q403.0,107.0 436.5,134.5Q470.0,162.0 516.0,164.0Q513.0,180.0 505.0,192.0Q497.0,204.0 486.0,213.0Q462.0,199.0 429.5,192.0Q397.0,185.0 358.0,185.0Z" transform="translate(1513, 908)"/>
<path d="" transform="translate(2414, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(2414, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(2924, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2906 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0Z" transform="translate(0, 908)"/>
<path d="M681.0,225.0Q681.0,142.0 619.5,92.0Q558.0,42.0 453.0,42.0Q359.0,42.0 279.0,87.5Q199.0,133.0 136.0,235.5Q73.0,338.0 28.0,507.0L103.0,529.0Q143.0,386.0 192.5,295.0Q242.0,204.0 306.5,161.0Q371.0,118.0 455.0,118.0Q518.0,118.0 559.0,144.5Q600.0,171.0 600.0,228.0Q600.0,255.0 587.0,276.5Q574.0,298.0 551.0,314.0Q535.0,305.0 517.0,297.0Q499.0,289.0 480.0,282.0L449.0,354.0Q516.0,376.0 553.5,405.5Q591.0,435.0 591.0,482.0Q591.0,558.0 509.0,558.0Q461.0,558.0 420.5,537.5Q380.0,517.0 355.5,489.5Q331.0,462.0 331.0,439.0Q331.0,423.0 341.0,411.5Q351.0,400.0 386.0,395.0L365.0,321.0Q308.0,332.0 279.5,360.0Q251.0,388.0 251.0,431.0Q251.0,465.0 271.5,499.5Q292.0,534.0 328.0,563.5Q364.0,593.0 410.5,611.0Q457.0,629.0 509.0,629.0Q586.0,629.0 628.0,590.5Q670.0,552.0 670.0,488.0Q670.0,466.0 659.0,443.0Q697.0,464.0 725.5,495.0Q754.0,526.0 754.0,570.0Q754.0,596.0 746.0,614.0Q738.0,632.0 724.0,646.0Q706.0,664.0 675.0,674.5Q644.0,685.0 600.0,691.0L482.0,707.0Q387.0,721.0 346.0,760.0Q305.0,799.0 305.0,875.0Q305.0,883.0 306.5,895.0Q308.0,907.0 309.0,917.0L383.0,913.0Q380.0,895.0 380.0,878.0Q380.0,838.0 400.0,814.0Q411.0,802.0 429.5,794.0Q448.0,786.0 484.0,781.0L625.0,762.0Q677.0,755.0 711.5,742.5Q746.0,730.0 771.0,710.0Q832.0,663.0 832.0,577.0Q832.0,522.0 805.5,481.5Q779.0,441.0 731.5,410.0Q684.0,379.0 620.0,352.0Q681.0,303.0 681.0,225.0Z" transform="translate(621, 908)"/>
<path d="M358.0,185.0Q287.0,185.0 225.0,215.0Q163.0,245.0 113.5,312.5Q64.0,380.0 29.0,492.0L102.0,513.0Q143.0,382.0 200.5,320.0Q258.0,258.0 354.0,258.0Q409.0,258.0 440.5,272.5Q472.0,287.0 485.0,311.0Q498.0,335.0 498.0,364.0Q498.0,405.0 471.0,432.5Q444.0,460.0 397.0,460.0Q363.0,460.0 347.0,444.5Q331.0,429.0 331.0,406.0Q331.0,399.0 332.5,389.5Q334.0,380.0 337.0,372.0L264.0,358.0Q258.0,373.0 255.5,390.0Q253.0,407.0 253.0,419.0Q253.0,472.0 294.5,499.5Q336.0,527.0 392.0,527.0Q451.0,527.0 491.0,503.5Q531.0,480.0 552.0,442.5Q573.0,405.0 573.0,361.0Q573.0,301.0 541.0,258.0Q560.0,243.0 576.0,218.5Q592.0,194.0 592.0,154.0Q631.0,141.0 665.0,115.5Q699.0,90.0 730.0,55.0Q729.0,75.0 729.0,95.0Q729.0,115.0 729.0,136.0L729.0,551.0L-10.0,551.0L-10.0,622.0L911.0,622.0L911.0,551.0L806.0,551.0L806.0,-72.0L729.0,-72.0L729.0,-42.0Q685.0,16.0 636.5,55.0Q588.0,94.0 531.0,94.0Q509.0,94.0 496.0,83.5Q483.0,73.0 483.0,56.0Q483.0,36.0 497.0,24.5Q511.0,13.0 538.0,3.0L503.0,-66.0Q457.0,-48.0 430.0,-17.0Q403.0,14.0 403.0,56.0Q403.0,107.0 436.5,134.5Q470.0,162.0 516.0,164.0Q513.0,180.0 505.0,192.0Q497.0,204.0 486.0,213.0Q462.0,199.0 429.5,192.0Q397.0,185.0 358.0,185.0Z" transform="translate(1495, 908)"/>
<path d="" transform="translate(2396, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(2396, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(2906, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ফৄঋঙল্দূ9৾</span> (Added by SIESTA)</li>


<pre>Expected: phabeng=0+838|rrvocalicvowelsignbeng=0@-221,0+0|rvocalicbeng=2+835|ngabeng=3+723|ladabeng=4+1021|uuvowelsignbeng=4@11,0+0|nine.beng=8+551|uni09FE=8@0,323+0</pre>



<pre>Got     : phabeng=0+838|rrvocalicvowelsignbeng=0@-221,0+0|rvocalicbeng=2+853|ngabeng=3+723|ladabeng=4+1021|uuvowelsignbeng=4@11,0+0|nine.beng=8+551|uni09FE=8@0,323+0</pre>



<pre>                                                                          +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3986 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M848.0,622.0L848.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.5,327.5Q184.0,301.0 142.0,276.0Q246.0,250.0 316.0,207.5Q386.0,165.0 447.0,99.0Q446.0,116.0 445.5,134.0Q445.0,152.0 445.0,171.0L445.0,510.0L458.0,510.0Q540.0,510.0 614.0,488.5Q688.0,467.0 739.0,414.0Q763.0,389.0 777.5,357.5Q792.0,326.0 792.0,288.0Q792.0,255.0 778.5,225.5Q765.0,196.0 735.0,177.0Q705.0,158.0 655.0,158.0Q640.0,158.0 625.5,159.0Q611.0,160.0 597.0,163.0L602.0,234.0Q608.0,233.0 617.0,232.5Q626.0,232.0 636.0,232.0Q685.0,232.0 699.5,251.0Q714.0,270.0 714.0,296.0Q714.0,347.0 662.5,386.0Q611.0,425.0 522.0,434.0L522.0,0.0L445.0,0.0Q404.0,56.0 354.5,98.0Q305.0,140.0 239.5,168.5Q174.0,197.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L848.0,622.0Z" transform="translate(0, 908)"/>
<path d="M-355.0,-80.0Q-296.0,-51.0 -233.0,-24.5Q-170.0,2.0 -105.0,25.0L-79.0,-41.0Q-124.0,-54.0 -175.5,-71.5Q-227.0,-89.0 -263.0,-106.0Q-175.0,-121.0 -103.0,-149.0Q-31.0,-177.0 28.0,-211.0L-3.0,-261.0Q-34.0,-244.0 -63.5,-230.5Q-93.0,-217.0 -121.0,-206.0Q-157.0,-218.0 -197.5,-233.5Q-238.0,-249.0 -263.0,-260.0Q-209.0,-268.0 -148.5,-288.0Q-88.0,-308.0 -32.0,-342.0L-63.0,-394.0Q-128.0,-356.0 -190.5,-339.0Q-253.0,-322.0 -323.0,-312.0L-355.0,-238.0Q-320.0,-222.0 -284.5,-206.5Q-249.0,-191.0 -207.0,-178.0Q-234.0,-171.0 -262.0,-167.0Q-290.0,-163.0 -321.0,-160.0L-355.0,-80.0Z" transform="translate(617, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(838, 908)"/>
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(1691, 908)"/>
<path d="M200.0,486.0Q243.0,486.0 278.0,469.5Q313.0,453.0 342.0,417.0Q355.0,443.0 379.5,457.0Q404.0,471.0 432.0,471.0Q452.0,471.0 468.5,464.5Q485.0,458.0 501.0,447.0Q500.0,459.0 500.0,471.0Q500.0,483.0 500.0,495.0L500.0,551.0L-10.0,551.0L-10.0,622.0L1031.0,622.0L1031.0,551.0L577.0,551.0L577.0,288.0Q698.0,414.0 893.0,486.0L958.0,422.0Q930.0,370.0 917.5,320.0Q905.0,270.0 905.0,205.0Q905.0,156.0 913.0,111.0Q921.0,66.0 940.0,10.0L865.0,-7.0Q847.0,51.0 837.0,106.5Q827.0,162.0 827.0,222.0Q827.0,276.0 838.0,322.0Q849.0,368.0 863.0,397.0Q783.0,361.0 709.5,306.5Q636.0,252.0 559.0,175.0L500.0,215.0L500.0,372.0Q486.0,384.0 471.5,391.5Q457.0,399.0 440.0,399.0Q419.0,399.0 400.0,386.0Q381.0,373.0 381.0,338.0Q381.0,332.0 381.0,326.5Q381.0,321.0 382.0,314.0L318.0,311.0Q310.0,358.0 278.5,386.0Q247.0,414.0 207.0,414.0Q170.0,414.0 149.0,395.5Q128.0,377.0 128.0,347.0Q128.0,308.0 156.5,286.5Q185.0,265.0 234.0,248.0L207.0,174.0Q138.0,194.0 92.0,237.0Q46.0,280.0 46.0,353.0Q46.0,392.0 66.5,422.0Q87.0,452.0 122.0,469.0Q157.0,486.0 200.0,486.0Z" transform="translate(2414, 908)"/>
<path d="M-177.0,-241.0Q-207.0,-241.0 -237.5,-230.5Q-268.0,-220.0 -288.0,-197.0Q-308.0,-174.0 -308.0,-137.0Q-308.0,-87.0 -268.0,-62.0Q-228.0,-37.0 -172.0,-36.0L-172.0,8.0L-95.0,8.0L-95.0,-56.0L-128.0,-102.0Q-135.0,-101.0 -144.5,-100.5Q-154.0,-100.0 -165.0,-100.0Q-235.0,-100.0 -235.0,-140.0Q-235.0,-159.0 -219.0,-169.0Q-203.0,-179.0 -179.0,-179.0Q-137.0,-179.0 -103.0,-159.0Q-69.0,-139.0 -38.0,-102.0Q7.0,-122.0 62.5,-154.0Q118.0,-186.0 163.0,-218.0L121.0,-271.0Q84.0,-243.0 46.0,-220.0Q8.0,-197.0 -22.0,-183.0Q-53.0,-211.0 -91.5,-226.0Q-130.0,-241.0 -177.0,-241.0Z" transform="translate(3446, 908)"/>
<path d="M190.0,-10.0Q171.0,-10.0 147.0,-7.5Q123.0,-5.0 106.0,-1.0L106.0,75.0Q123.0,69.0 144.5,66.0Q166.0,63.0 187.0,63.0Q253.0,63.0 296.0,86.0Q339.0,109.0 363.0,148.5Q387.0,188.0 398.0,240.0Q409.0,292.0 411.0,350.0L405.0,350.0Q386.0,315.0 349.5,291.0Q313.0,267.0 255.0,267.0Q163.0,267.0 107.5,324.0Q52.0,381.0 52.0,484.0Q52.0,596.0 110.5,660.0Q169.0,724.0 269.0,724.0Q335.0,724.0 387.5,690.0Q440.0,656.0 471.0,586.0Q502.0,516.0 502.0,409.0Q502.0,348.0 494.5,287.5Q487.0,227.0 467.0,173.5Q447.0,120.0 412.0,78.5Q377.0,37.0 322.5,13.5Q268.0,-10.0 190.0,-10.0ZM267.0,337.0Q311.0,337.0 344.0,356.5Q377.0,376.0 395.0,406.0Q413.0,436.0 413.0,467.0Q413.0,511.0 397.0,552.5Q381.0,594.0 349.5,621.5Q318.0,649.0 270.0,649.0Q212.0,649.0 175.0,609.0Q138.0,569.0 138.0,484.0Q138.0,416.0 170.5,376.5Q203.0,337.0 267.0,337.0Z" transform="translate(3435, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(3986, 1231)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3968 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M848.0,622.0L848.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.5,327.5Q184.0,301.0 142.0,276.0Q246.0,250.0 316.0,207.5Q386.0,165.0 447.0,99.0Q446.0,116.0 445.5,134.0Q445.0,152.0 445.0,171.0L445.0,510.0L458.0,510.0Q540.0,510.0 614.0,488.5Q688.0,467.0 739.0,414.0Q763.0,389.0 777.5,357.5Q792.0,326.0 792.0,288.0Q792.0,255.0 778.5,225.5Q765.0,196.0 735.0,177.0Q705.0,158.0 655.0,158.0Q640.0,158.0 625.5,159.0Q611.0,160.0 597.0,163.0L602.0,234.0Q608.0,233.0 617.0,232.5Q626.0,232.0 636.0,232.0Q685.0,232.0 699.5,251.0Q714.0,270.0 714.0,296.0Q714.0,347.0 662.5,386.0Q611.0,425.0 522.0,434.0L522.0,0.0L445.0,0.0Q404.0,56.0 354.5,98.0Q305.0,140.0 239.5,168.5Q174.0,197.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L848.0,622.0Z" transform="translate(0, 908)"/>
<path d="M-355.0,-80.0Q-296.0,-51.0 -233.0,-24.5Q-170.0,2.0 -105.0,25.0L-79.0,-41.0Q-124.0,-54.0 -175.5,-71.5Q-227.0,-89.0 -263.0,-106.0Q-175.0,-121.0 -103.0,-149.0Q-31.0,-177.0 28.0,-211.0L-3.0,-261.0Q-34.0,-244.0 -63.5,-230.5Q-93.0,-217.0 -121.0,-206.0Q-157.0,-218.0 -197.5,-233.5Q-238.0,-249.0 -263.0,-260.0Q-209.0,-268.0 -148.5,-288.0Q-88.0,-308.0 -32.0,-342.0L-63.0,-394.0Q-128.0,-356.0 -190.5,-339.0Q-253.0,-322.0 -323.0,-312.0L-355.0,-238.0Q-320.0,-222.0 -284.5,-206.5Q-249.0,-191.0 -207.0,-178.0Q-234.0,-171.0 -262.0,-167.0Q-290.0,-163.0 -321.0,-160.0L-355.0,-80.0Z" transform="translate(617, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(838, 908)"/>
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(1673, 908)"/>
<path d="M200.0,486.0Q243.0,486.0 278.0,469.5Q313.0,453.0 342.0,417.0Q355.0,443.0 379.5,457.0Q404.0,471.0 432.0,471.0Q452.0,471.0 468.5,464.5Q485.0,458.0 501.0,447.0Q500.0,459.0 500.0,471.0Q500.0,483.0 500.0,495.0L500.0,551.0L-10.0,551.0L-10.0,622.0L1031.0,622.0L1031.0,551.0L577.0,551.0L577.0,288.0Q698.0,414.0 893.0,486.0L958.0,422.0Q930.0,370.0 917.5,320.0Q905.0,270.0 905.0,205.0Q905.0,156.0 913.0,111.0Q921.0,66.0 940.0,10.0L865.0,-7.0Q847.0,51.0 837.0,106.5Q827.0,162.0 827.0,222.0Q827.0,276.0 838.0,322.0Q849.0,368.0 863.0,397.0Q783.0,361.0 709.5,306.5Q636.0,252.0 559.0,175.0L500.0,215.0L500.0,372.0Q486.0,384.0 471.5,391.5Q457.0,399.0 440.0,399.0Q419.0,399.0 400.0,386.0Q381.0,373.0 381.0,338.0Q381.0,332.0 381.0,326.5Q381.0,321.0 382.0,314.0L318.0,311.0Q310.0,358.0 278.5,386.0Q247.0,414.0 207.0,414.0Q170.0,414.0 149.0,395.5Q128.0,377.0 128.0,347.0Q128.0,308.0 156.5,286.5Q185.0,265.0 234.0,248.0L207.0,174.0Q138.0,194.0 92.0,237.0Q46.0,280.0 46.0,353.0Q46.0,392.0 66.5,422.0Q87.0,452.0 122.0,469.0Q157.0,486.0 200.0,486.0Z" transform="translate(2396, 908)"/>
<path d="M-177.0,-241.0Q-207.0,-241.0 -237.5,-230.5Q-268.0,-220.0 -288.0,-197.0Q-308.0,-174.0 -308.0,-137.0Q-308.0,-87.0 -268.0,-62.0Q-228.0,-37.0 -172.0,-36.0L-172.0,8.0L-95.0,8.0L-95.0,-56.0L-128.0,-102.0Q-135.0,-101.0 -144.5,-100.5Q-154.0,-100.0 -165.0,-100.0Q-235.0,-100.0 -235.0,-140.0Q-235.0,-159.0 -219.0,-169.0Q-203.0,-179.0 -179.0,-179.0Q-137.0,-179.0 -103.0,-159.0Q-69.0,-139.0 -38.0,-102.0Q7.0,-122.0 62.5,-154.0Q118.0,-186.0 163.0,-218.0L121.0,-271.0Q84.0,-243.0 46.0,-220.0Q8.0,-197.0 -22.0,-183.0Q-53.0,-211.0 -91.5,-226.0Q-130.0,-241.0 -177.0,-241.0Z" transform="translate(3428, 908)"/>
<path d="M190.0,-10.0Q171.0,-10.0 147.0,-7.5Q123.0,-5.0 106.0,-1.0L106.0,75.0Q123.0,69.0 144.5,66.0Q166.0,63.0 187.0,63.0Q253.0,63.0 296.0,86.0Q339.0,109.0 363.0,148.5Q387.0,188.0 398.0,240.0Q409.0,292.0 411.0,350.0L405.0,350.0Q386.0,315.0 349.5,291.0Q313.0,267.0 255.0,267.0Q163.0,267.0 107.5,324.0Q52.0,381.0 52.0,484.0Q52.0,596.0 110.5,660.0Q169.0,724.0 269.0,724.0Q335.0,724.0 387.5,690.0Q440.0,656.0 471.0,586.0Q502.0,516.0 502.0,409.0Q502.0,348.0 494.5,287.5Q487.0,227.0 467.0,173.5Q447.0,120.0 412.0,78.5Q377.0,37.0 322.5,13.5Q268.0,-10.0 190.0,-10.0ZM267.0,337.0Q311.0,337.0 344.0,356.5Q377.0,376.0 395.0,406.0Q413.0,436.0 413.0,467.0Q413.0,511.0 397.0,552.5Q381.0,594.0 349.5,621.5Q318.0,649.0 270.0,649.0Q212.0,649.0 175.0,609.0Q138.0,569.0 138.0,484.0Q138.0,416.0 170.5,376.5Q203.0,337.0 267.0,337.0Z" transform="translate(3417, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(3968, 1231)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ৠএঢ়᳐দ᳖িঊঌ॒</span> (Added by SIESTA)</li>


<pre>Expected: rrvocalicbeng=0+835|ebeng=1+758|rhabeng=2+567|uni1CD0=2@-29,323+0|dabeng=4+603|uni1CD6=4@-47,-319+0|ivowelsignbeng=4+266|uni25CC=4+510|uubeng=7+853|lvocalicbeng=8+639|uni0952=8@-65,-313+0</pre>



<pre>Got     : rrvocalicbeng=0+853|ebeng=1+758|rhabeng=2+567|uni1CD0=2@-29,323+0|dabeng=4+603|uni1CD6=4@-47,-319+0|ivowelsignbeng=4+266|uni25CC=4+510|uubeng=7+853|lvocalicbeng=8+639|uni0952=8@-65,-313+0</pre>



<pre>                           +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5049 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(0, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(853, 908)"/>
<path d="M577.0,622.0L577.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L577.0,622.0ZM281.0,-152.0Q256.0,-152.0 238.5,-136.0Q221.0,-120.0 221.0,-94.0Q221.0,-68.0 238.5,-51.0Q256.0,-34.0 281.0,-34.0Q306.0,-34.0 323.5,-51.0Q341.0,-68.0 341.0,-94.0Q341.0,-120.0 323.5,-136.0Q306.0,-152.0 281.0,-152.0Z" transform="translate(1611, 908)"/>
<path d="M-430.0,661.0L-289.0,910.0L-228.0,910.0L-77.0,663.0L-131.0,636.0L-255.0,849.0L-371.0,636.0L-430.0,661.0Z" transform="translate(2149, 1231)"/>
<path d="M613.0,622.0L613.0,551.0L159.0,551.0L159.0,288.0Q280.0,414.0 475.0,486.0L540.0,422.0Q512.0,370.0 499.5,320.0Q487.0,270.0 487.0,205.0Q487.0,156.0 495.0,111.0Q503.0,66.0 522.0,10.0L447.0,-7.0Q429.0,51.0 419.0,106.5Q409.0,162.0 409.0,222.0Q409.0,276.0 420.0,322.0Q431.0,368.0 445.0,397.0Q365.0,361.0 291.5,306.5Q218.0,252.0 141.0,175.0L82.0,215.0L82.0,551.0L-10.0,551.0L-10.0,622.0L613.0,622.0Z" transform="translate(2178, 908)"/>
<path d="M-426.0,-94.0L-348.0,-94.0L-348.0,-202.0L-78.0,-202.0L-78.0,-271.0L-426.0,-271.0L-426.0,-94.0Z" transform="translate(2734, 589)"/>
<path d="M276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L82.0,622.0Q66.0,641.0 49.5,662.0Q33.0,683.0 20.0,704.0Q54.0,763.0 93.0,811.5Q132.0,860.0 185.0,888.5Q238.0,917.0 313.0,917.0Q384.0,917.0 447.0,894.0Q510.0,871.0 573.0,829.5Q636.0,788.0 705.0,731.0L663.0,677.0Q594.0,733.0 538.5,770.0Q483.0,807.0 432.5,825.5Q382.0,844.0 325.0,844.0Q242.0,844.0 192.0,802.0Q142.0,760.0 106.0,693.0Q114.0,678.0 128.0,660.0Q142.0,642.0 160.0,622.0L276.0,622.0Z" transform="translate(2781, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(3047, 908)"/>
<path d="M649.0,622.0Q648.0,663.0 629.5,681.0Q611.0,699.0 569.0,699.0L384.0,699.0Q318.0,699.0 282.5,708.0Q247.0,717.0 222.0,736.0Q168.0,777.0 168.0,859.0Q168.0,872.0 169.5,885.0Q171.0,898.0 173.0,912.0L247.0,907.0Q245.0,896.0 244.0,886.5Q243.0,877.0 243.0,869.0Q243.0,847.0 247.5,830.0Q252.0,813.0 262.0,802.0Q276.0,786.0 302.5,778.5Q329.0,771.0 378.0,771.0L548.0,771.0Q601.0,771.0 632.0,763.0Q663.0,755.0 685.0,734.0Q718.0,702.0 721.0,622.0L863.0,622.0L863.0,551.0L496.0,551.0L496.0,372.0Q496.0,316.0 533.0,316.0Q562.0,316.0 594.0,343.5Q626.0,371.0 669.0,433.0L729.0,442.0Q761.0,395.0 778.5,345.0Q796.0,295.0 796.0,245.0Q796.0,184.0 770.0,134.0Q744.0,84.0 689.0,54.0Q634.0,24.0 548.0,24.0Q439.0,24.0 343.5,61.0Q248.0,98.0 169.0,188.0Q90.0,278.0 29.0,435.0L104.0,458.0Q130.0,385.0 163.5,321.0Q197.0,257.0 246.5,203.0Q296.0,149.0 369.0,106.0L372.0,109.0Q331.0,147.0 298.0,200.5Q265.0,254.0 240.5,316.5Q216.0,379.0 199.0,440.0L274.0,461.0Q308.0,335.0 345.0,255.5Q382.0,176.0 432.5,138.0Q483.0,100.0 555.0,100.0Q612.0,100.0 648.5,120.0Q685.0,140.0 702.5,172.5Q720.0,205.0 720.0,244.0Q720.0,279.0 712.0,305.5Q704.0,332.0 693.0,349.0Q661.0,305.0 620.0,273.5Q579.0,242.0 534.0,242.0Q486.0,242.0 457.0,268.0Q441.0,282.0 430.0,307.5Q419.0,333.0 419.0,393.0L419.0,551.0L-10.0,551.0L-10.0,622.0L649.0,622.0Z" transform="translate(3557, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0Z" transform="translate(4410, 908)"/>
<path d="M-443.0,-187.0L-443.0,-116.0L-67.0,-116.0L-67.0,-187.0L-443.0,-187.0Z" transform="translate(4984, 595)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5031 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(0, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(835, 908)"/>
<path d="M577.0,622.0L577.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L577.0,622.0ZM281.0,-152.0Q256.0,-152.0 238.5,-136.0Q221.0,-120.0 221.0,-94.0Q221.0,-68.0 238.5,-51.0Q256.0,-34.0 281.0,-34.0Q306.0,-34.0 323.5,-51.0Q341.0,-68.0 341.0,-94.0Q341.0,-120.0 323.5,-136.0Q306.0,-152.0 281.0,-152.0Z" transform="translate(1593, 908)"/>
<path d="M-430.0,661.0L-289.0,910.0L-228.0,910.0L-77.0,663.0L-131.0,636.0L-255.0,849.0L-371.0,636.0L-430.0,661.0Z" transform="translate(2131, 1231)"/>
<path d="M613.0,622.0L613.0,551.0L159.0,551.0L159.0,288.0Q280.0,414.0 475.0,486.0L540.0,422.0Q512.0,370.0 499.5,320.0Q487.0,270.0 487.0,205.0Q487.0,156.0 495.0,111.0Q503.0,66.0 522.0,10.0L447.0,-7.0Q429.0,51.0 419.0,106.5Q409.0,162.0 409.0,222.0Q409.0,276.0 420.0,322.0Q431.0,368.0 445.0,397.0Q365.0,361.0 291.5,306.5Q218.0,252.0 141.0,175.0L82.0,215.0L82.0,551.0L-10.0,551.0L-10.0,622.0L613.0,622.0Z" transform="translate(2160, 908)"/>
<path d="M-426.0,-94.0L-348.0,-94.0L-348.0,-202.0L-78.0,-202.0L-78.0,-271.0L-426.0,-271.0L-426.0,-94.0Z" transform="translate(2716, 589)"/>
<path d="M276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L82.0,622.0Q66.0,641.0 49.5,662.0Q33.0,683.0 20.0,704.0Q54.0,763.0 93.0,811.5Q132.0,860.0 185.0,888.5Q238.0,917.0 313.0,917.0Q384.0,917.0 447.0,894.0Q510.0,871.0 573.0,829.5Q636.0,788.0 705.0,731.0L663.0,677.0Q594.0,733.0 538.5,770.0Q483.0,807.0 432.5,825.5Q382.0,844.0 325.0,844.0Q242.0,844.0 192.0,802.0Q142.0,760.0 106.0,693.0Q114.0,678.0 128.0,660.0Q142.0,642.0 160.0,622.0L276.0,622.0Z" transform="translate(2763, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(3029, 908)"/>
<path d="M649.0,622.0Q648.0,663.0 629.5,681.0Q611.0,699.0 569.0,699.0L384.0,699.0Q318.0,699.0 282.5,708.0Q247.0,717.0 222.0,736.0Q168.0,777.0 168.0,859.0Q168.0,872.0 169.5,885.0Q171.0,898.0 173.0,912.0L247.0,907.0Q245.0,896.0 244.0,886.5Q243.0,877.0 243.0,869.0Q243.0,847.0 247.5,830.0Q252.0,813.0 262.0,802.0Q276.0,786.0 302.5,778.5Q329.0,771.0 378.0,771.0L548.0,771.0Q601.0,771.0 632.0,763.0Q663.0,755.0 685.0,734.0Q718.0,702.0 721.0,622.0L863.0,622.0L863.0,551.0L496.0,551.0L496.0,372.0Q496.0,316.0 533.0,316.0Q562.0,316.0 594.0,343.5Q626.0,371.0 669.0,433.0L729.0,442.0Q761.0,395.0 778.5,345.0Q796.0,295.0 796.0,245.0Q796.0,184.0 770.0,134.0Q744.0,84.0 689.0,54.0Q634.0,24.0 548.0,24.0Q439.0,24.0 343.5,61.0Q248.0,98.0 169.0,188.0Q90.0,278.0 29.0,435.0L104.0,458.0Q130.0,385.0 163.5,321.0Q197.0,257.0 246.5,203.0Q296.0,149.0 369.0,106.0L372.0,109.0Q331.0,147.0 298.0,200.5Q265.0,254.0 240.5,316.5Q216.0,379.0 199.0,440.0L274.0,461.0Q308.0,335.0 345.0,255.5Q382.0,176.0 432.5,138.0Q483.0,100.0 555.0,100.0Q612.0,100.0 648.5,120.0Q685.0,140.0 702.5,172.5Q720.0,205.0 720.0,244.0Q720.0,279.0 712.0,305.5Q704.0,332.0 693.0,349.0Q661.0,305.0 620.0,273.5Q579.0,242.0 534.0,242.0Q486.0,242.0 457.0,268.0Q441.0,282.0 430.0,307.5Q419.0,333.0 419.0,393.0L419.0,551.0L-10.0,551.0L-10.0,622.0L649.0,622.0Z" transform="translate(3539, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0Z" transform="translate(4392, 908)"/>
<path d="M-443.0,-187.0L-443.0,-116.0L-67.0,-116.0L-67.0,-187.0L-443.0,-187.0Z" transform="translate(4966, 595)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঙূঃ᳐ল্ৡৠএঋ</span> (Added by SIESTA)</li>


<pre>Expected: ngabeng=0+723|uuvowelsignlongbeng=0@-107,0+0|visargabeng=0+438|uni1CD0=0@-386,323+0|labeng=4+731|viramabeng=4+0|llvocalicbeng=6+621|rrvocalicbeng=7+835|ebeng=8+740|rvocalicbeng=9+853</pre>



<pre>Got     : ngabeng=0+723|uuvowelsignlongbeng=0@-107,0+0|visargabeng=0+438|uni1CD0=0@-386,323+0|labeng=4+731|viramabeng=4+0|llvocalicbeng=6+639|rrvocalicbeng=7+853|ebeng=8+758|rvocalicbeng=9+853</pre>



<pre>                                                                                                                                           ^^                  +           ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4995 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(0, 908)"/>
<path d="M-177.0,-241.0Q-207.0,-241.0 -237.5,-230.5Q-268.0,-220.0 -288.0,-197.0Q-308.0,-174.0 -308.0,-137.0Q-308.0,-87.0 -268.0,-62.0Q-228.0,-37.0 -172.0,-36.0L-172.0,52.0L-101.0,52.0L-101.0,-65.0L-128.0,-102.0Q-135.0,-101.0 -144.5,-100.5Q-154.0,-100.0 -165.0,-100.0Q-235.0,-100.0 -235.0,-140.0Q-235.0,-159.0 -219.0,-169.0Q-203.0,-179.0 -179.0,-179.0Q-137.0,-179.0 -103.0,-159.0Q-69.0,-139.0 -38.0,-102.0Q7.0,-122.0 62.5,-154.0Q118.0,-186.0 163.0,-218.0L121.0,-271.0Q84.0,-243.0 46.0,-220.0Q8.0,-197.0 -22.0,-183.0Q-53.0,-211.0 -91.5,-226.0Q-130.0,-241.0 -177.0,-241.0Z" transform="translate(616, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,518.0 271.0,537.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM78.0,137.0Q78.0,199.0 118.5,236.0Q159.0,273.0 219.0,273.0Q279.0,273.0 319.5,236.0Q360.0,199.0 360.0,137.0Q360.0,75.0 319.5,37.5Q279.0,0.0 219.0,0.0Q159.0,0.0 118.5,37.5Q78.0,75.0 78.0,137.0ZM147.0,137.0Q147.0,104.0 167.5,84.5Q188.0,65.0 219.0,65.0Q251.0,65.0 271.0,84.5Q291.0,104.0 291.0,137.0Q291.0,170.0 271.0,189.0Q251.0,208.0 219.0,208.0Q188.0,208.0 167.5,188.5Q147.0,169.0 147.0,137.0Z" transform="translate(723, 908)"/>
<path d="M-430.0,661.0L-289.0,910.0L-228.0,910.0L-77.0,663.0L-131.0,636.0L-255.0,849.0L-371.0,636.0L-430.0,661.0Z" transform="translate(775, 1231)"/>
<path d="M741.0,622.0L741.0,551.0L636.0,551.0L636.0,0.0L559.0,0.0L559.0,317.0Q538.0,346.0 515.0,362.5Q492.0,379.0 465.0,379.0Q450.0,379.0 434.5,373.5Q419.0,368.0 408.5,353.0Q398.0,338.0 398.0,307.0Q398.0,296.0 398.5,287.5Q399.0,279.0 400.0,271.0L335.0,266.0Q329.0,327.0 293.0,360.5Q257.0,394.0 213.0,394.0Q173.0,394.0 150.5,371.5Q128.0,349.0 128.0,316.0Q128.0,276.0 157.5,248.0Q187.0,220.0 241.0,201.0L214.0,127.0Q142.0,150.0 94.0,197.5Q46.0,245.0 46.0,320.0Q46.0,365.0 68.0,397.5Q90.0,430.0 127.0,448.0Q164.0,466.0 208.0,466.0Q257.0,466.0 293.0,449.5Q329.0,433.0 359.0,396.0Q372.0,423.0 398.0,437.0Q424.0,451.0 452.0,451.0Q485.0,451.0 509.5,439.5Q534.0,428.0 561.0,406.0Q559.0,435.0 559.0,467.0L559.0,551.0L-10.0,551.0L-10.0,622.0L741.0,622.0Z" transform="translate(1161, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(1892, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0ZM243.0,-107.0Q297.0,-107.0 324.0,-130.0Q351.0,-153.0 351.0,-188.0Q351.0,-200.0 346.5,-213.0Q342.0,-226.0 329.0,-238.0Q389.0,-230.0 413.0,-212.5Q437.0,-195.0 437.0,-167.0Q437.0,-150.0 428.5,-137.0Q420.0,-124.0 395.5,-111.0Q371.0,-98.0 323.0,-84.0Q272.0,-68.0 245.0,-51.5Q218.0,-35.0 218.0,-2.0Q218.0,15.0 228.0,33.0L284.0,20.0Q280.0,12.0 280.0,4.0Q280.0,-6.0 294.5,-13.0Q309.0,-20.0 358.0,-35.0Q418.0,-53.0 450.0,-72.5Q482.0,-92.0 493.5,-115.0Q505.0,-138.0 505.0,-165.0Q505.0,-212.0 473.0,-240.5Q441.0,-269.0 389.5,-281.0Q338.0,-293.0 277.0,-293.0L253.0,-293.0L241.0,-244.0Q268.0,-236.0 280.0,-223.5Q292.0,-211.0 292.0,-194.0Q292.0,-179.0 281.0,-169.5Q270.0,-160.0 245.0,-160.0Q205.0,-160.0 205.0,-184.0Q205.0,-193.0 212.0,-207.0L152.0,-218.0Q141.0,-198.0 141.0,-175.0Q141.0,-146.0 166.5,-126.5Q192.0,-107.0 243.0,-107.0Z" transform="translate(1892, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(2531, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(3384, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(4142, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4941 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(0, 908)"/>
<path d="M-177.0,-241.0Q-207.0,-241.0 -237.5,-230.5Q-268.0,-220.0 -288.0,-197.0Q-308.0,-174.0 -308.0,-137.0Q-308.0,-87.0 -268.0,-62.0Q-228.0,-37.0 -172.0,-36.0L-172.0,52.0L-101.0,52.0L-101.0,-65.0L-128.0,-102.0Q-135.0,-101.0 -144.5,-100.5Q-154.0,-100.0 -165.0,-100.0Q-235.0,-100.0 -235.0,-140.0Q-235.0,-159.0 -219.0,-169.0Q-203.0,-179.0 -179.0,-179.0Q-137.0,-179.0 -103.0,-159.0Q-69.0,-139.0 -38.0,-102.0Q7.0,-122.0 62.5,-154.0Q118.0,-186.0 163.0,-218.0L121.0,-271.0Q84.0,-243.0 46.0,-220.0Q8.0,-197.0 -22.0,-183.0Q-53.0,-211.0 -91.5,-226.0Q-130.0,-241.0 -177.0,-241.0Z" transform="translate(616, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,518.0 271.0,537.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM78.0,137.0Q78.0,199.0 118.5,236.0Q159.0,273.0 219.0,273.0Q279.0,273.0 319.5,236.0Q360.0,199.0 360.0,137.0Q360.0,75.0 319.5,37.5Q279.0,0.0 219.0,0.0Q159.0,0.0 118.5,37.5Q78.0,75.0 78.0,137.0ZM147.0,137.0Q147.0,104.0 167.5,84.5Q188.0,65.0 219.0,65.0Q251.0,65.0 271.0,84.5Q291.0,104.0 291.0,137.0Q291.0,170.0 271.0,189.0Q251.0,208.0 219.0,208.0Q188.0,208.0 167.5,188.5Q147.0,169.0 147.0,137.0Z" transform="translate(723, 908)"/>
<path d="M-430.0,661.0L-289.0,910.0L-228.0,910.0L-77.0,663.0L-131.0,636.0L-255.0,849.0L-371.0,636.0L-430.0,661.0Z" transform="translate(775, 1231)"/>
<path d="M741.0,622.0L741.0,551.0L636.0,551.0L636.0,0.0L559.0,0.0L559.0,317.0Q538.0,346.0 515.0,362.5Q492.0,379.0 465.0,379.0Q450.0,379.0 434.5,373.5Q419.0,368.0 408.5,353.0Q398.0,338.0 398.0,307.0Q398.0,296.0 398.5,287.5Q399.0,279.0 400.0,271.0L335.0,266.0Q329.0,327.0 293.0,360.5Q257.0,394.0 213.0,394.0Q173.0,394.0 150.5,371.5Q128.0,349.0 128.0,316.0Q128.0,276.0 157.5,248.0Q187.0,220.0 241.0,201.0L214.0,127.0Q142.0,150.0 94.0,197.5Q46.0,245.0 46.0,320.0Q46.0,365.0 68.0,397.5Q90.0,430.0 127.0,448.0Q164.0,466.0 208.0,466.0Q257.0,466.0 293.0,449.5Q329.0,433.0 359.0,396.0Q372.0,423.0 398.0,437.0Q424.0,451.0 452.0,451.0Q485.0,451.0 509.5,439.5Q534.0,428.0 561.0,406.0Q559.0,435.0 559.0,467.0L559.0,551.0L-10.0,551.0L-10.0,622.0L741.0,622.0Z" transform="translate(1161, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(1892, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0ZM243.0,-107.0Q297.0,-107.0 324.0,-130.0Q351.0,-153.0 351.0,-188.0Q351.0,-200.0 346.5,-213.0Q342.0,-226.0 329.0,-238.0Q389.0,-230.0 413.0,-212.5Q437.0,-195.0 437.0,-167.0Q437.0,-150.0 428.5,-137.0Q420.0,-124.0 395.5,-111.0Q371.0,-98.0 323.0,-84.0Q272.0,-68.0 245.0,-51.5Q218.0,-35.0 218.0,-2.0Q218.0,15.0 228.0,33.0L284.0,20.0Q280.0,12.0 280.0,4.0Q280.0,-6.0 294.5,-13.0Q309.0,-20.0 358.0,-35.0Q418.0,-53.0 450.0,-72.5Q482.0,-92.0 493.5,-115.0Q505.0,-138.0 505.0,-165.0Q505.0,-212.0 473.0,-240.5Q441.0,-269.0 389.5,-281.0Q338.0,-293.0 277.0,-293.0L253.0,-293.0L241.0,-244.0Q268.0,-236.0 280.0,-223.5Q292.0,-211.0 292.0,-194.0Q292.0,-179.0 281.0,-169.5Q270.0,-160.0 245.0,-160.0Q205.0,-160.0 205.0,-184.0Q205.0,-193.0 212.0,-207.0L152.0,-218.0Q141.0,-198.0 141.0,-175.0Q141.0,-146.0 166.5,-126.5Q192.0,-107.0 243.0,-107.0Z" transform="translate(1892, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(2513, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(3348, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(4088, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঞ্জওওᳪ</span> (Added by SIESTA)</li>


<pre>Expected: nyajabeng=0+842|obeng=3+720|obeng=4+738|uni1CEA=5+748</pre>



<pre>Got     : nyajabeng=0+860|obeng=3+738|obeng=4+738|uni1CEA=5+748</pre>



<pre>                       ^^          ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3084 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M658.0,250.0Q610.0,250.0 573.0,271.5Q536.0,293.0 509.0,327.0Q482.0,361.0 463.0,400.0Q444.0,381.0 416.0,360.0Q386.0,338.0 365.5,319.0Q345.0,300.0 345.0,276.0Q345.0,234.0 389.0,234.0Q415.0,234.0 438.0,245.5Q461.0,257.0 489.0,282.0L565.0,255.0Q581.0,214.0 581.0,158.0Q581.0,88.0 530.0,44.0Q479.0,0.0 380.0,0.0Q333.0,0.0 284.0,15.0Q235.0,30.0 188.0,71.5Q141.0,113.0 100.0,191.0Q59.0,269.0 28.0,395.0L105.0,417.0Q131.0,308.0 162.5,240.5Q194.0,173.0 229.5,137.5Q265.0,102.0 303.0,89.0Q341.0,76.0 380.0,76.0Q438.0,76.0 471.5,100.0Q505.0,124.0 505.0,170.0Q505.0,184.0 502.0,199.0Q478.0,183.0 451.0,174.0Q424.0,165.0 390.0,165.0Q334.0,165.0 301.0,195.5Q268.0,226.0 268.0,272.0Q268.0,307.0 284.5,333.0Q301.0,359.0 325.5,379.5Q350.0,400.0 375.0,418.0Q404.0,439.0 425.5,460.0Q447.0,481.0 447.0,506.0Q447.0,515.0 442.5,526.5Q438.0,538.0 424.5,546.5Q411.0,555.0 384.0,555.0Q349.0,555.0 320.0,541.5Q291.0,528.0 274.0,509.0Q257.0,490.0 257.0,474.0Q257.0,460.0 266.0,449.0Q275.0,438.0 290.0,430.0L237.0,370.0Q202.0,390.0 188.5,417.0Q175.0,444.0 175.0,467.0Q175.0,494.0 192.0,522.0Q209.0,550.0 238.5,573.5Q268.0,597.0 305.5,611.5Q343.0,626.0 384.0,626.0Q433.0,626.0 467.0,607.0Q501.0,588.0 512.0,549.0Q548.0,587.0 587.0,607.0Q626.0,627.0 673.0,627.0Q732.0,627.0 765.0,598.0Q798.0,569.0 798.0,523.0Q798.0,504.0 789.5,484.0Q781.0,464.0 761.0,445.0Q779.0,431.0 791.5,410.0Q804.0,389.0 804.0,363.0Q804.0,318.0 772.0,288.0L787.0,272.0Q762.0,241.0 753.0,210.0Q744.0,179.0 744.0,144.0Q744.0,122.0 750.5,82.0Q757.0,42.0 770.0,9.0L699.0,-7.0Q685.0,37.0 677.0,81.0Q669.0,125.0 669.0,165.0Q669.0,190.0 673.0,211.5Q677.0,233.0 683.0,251.0Q671.0,250.0 658.0,250.0ZM669.0,559.0Q627.0,559.0 586.5,529.5Q546.0,500.0 516.0,454.0Q538.0,384.0 576.0,351.0Q614.0,318.0 666.0,318.0Q689.0,318.0 708.5,329.0Q728.0,340.0 728.0,370.0Q728.0,394.0 706.0,412.0Q683.0,403.0 655.0,396.0L639.0,460.0Q677.0,469.0 699.5,482.5Q722.0,496.0 722.0,521.0Q722.0,541.0 708.0,550.0Q694.0,559.0 669.0,559.0Z" transform="translate(0, 908)"/>
<path d="M681.0,225.0Q681.0,142.0 619.5,92.0Q558.0,42.0 453.0,42.0Q359.0,42.0 279.0,87.5Q199.0,133.0 136.0,235.5Q73.0,338.0 28.0,507.0L103.0,529.0Q143.0,386.0 192.5,295.0Q242.0,204.0 306.5,161.0Q371.0,118.0 455.0,118.0Q518.0,118.0 559.0,144.5Q600.0,171.0 600.0,228.0Q600.0,255.0 587.0,276.5Q574.0,298.0 552.0,314.0Q520.0,297.0 480.0,282.0L449.0,354.0Q516.0,376.0 553.5,405.5Q591.0,435.0 591.0,482.0Q591.0,558.0 509.0,558.0Q461.0,558.0 420.5,537.5Q380.0,517.0 355.5,489.5Q331.0,462.0 331.0,439.0Q331.0,423.0 341.0,411.5Q351.0,400.0 386.0,395.0L365.0,321.0Q308.0,332.0 279.5,360.0Q251.0,388.0 251.0,431.0Q251.0,465.0 271.5,499.5Q292.0,534.0 328.0,563.5Q364.0,593.0 410.5,611.0Q457.0,629.0 509.0,629.0Q586.0,629.0 628.5,590.0Q671.0,551.0 671.0,483.0Q671.0,445.0 655.5,414.0Q640.0,383.0 613.0,358.0Q681.0,308.0 681.0,225.0Z" transform="translate(860, 908)"/>
<path d="M681.0,225.0Q681.0,142.0 619.5,92.0Q558.0,42.0 453.0,42.0Q359.0,42.0 279.0,87.5Q199.0,133.0 136.0,235.5Q73.0,338.0 28.0,507.0L103.0,529.0Q143.0,386.0 192.5,295.0Q242.0,204.0 306.5,161.0Q371.0,118.0 455.0,118.0Q518.0,118.0 559.0,144.5Q600.0,171.0 600.0,228.0Q600.0,255.0 587.0,276.5Q574.0,298.0 552.0,314.0Q520.0,297.0 480.0,282.0L449.0,354.0Q516.0,376.0 553.5,405.5Q591.0,435.0 591.0,482.0Q591.0,558.0 509.0,558.0Q461.0,558.0 420.5,537.5Q380.0,517.0 355.5,489.5Q331.0,462.0 331.0,439.0Q331.0,423.0 341.0,411.5Q351.0,400.0 386.0,395.0L365.0,321.0Q308.0,332.0 279.5,360.0Q251.0,388.0 251.0,431.0Q251.0,465.0 271.5,499.5Q292.0,534.0 328.0,563.5Q364.0,593.0 410.5,611.0Q457.0,629.0 509.0,629.0Q586.0,629.0 628.5,590.0Q671.0,551.0 671.0,483.0Q671.0,445.0 655.5,414.0Q640.0,383.0 613.0,358.0Q681.0,308.0 681.0,225.0Z" transform="translate(1598, 908)"/>
<path d="M372.0,0.0Q277.0,0.0 216.5,26.0Q156.0,52.0 127.0,97.5Q98.0,143.0 98.0,199.0Q98.0,258.0 123.5,296.0Q149.0,334.0 191.0,375.0Q222.0,405.0 237.5,430.5Q253.0,456.0 253.0,493.0Q253.0,527.0 230.0,547.5Q207.0,568.0 175.0,568.0Q144.0,568.0 129.5,554.5Q115.0,541.0 115.0,518.0Q115.0,493.0 135.0,477.0Q155.0,461.0 199.0,458.0L189.0,389.0Q131.0,396.0 98.5,416.0Q66.0,436.0 53.0,464.0Q40.0,492.0 40.0,520.0Q40.0,570.0 76.0,601.0Q112.0,632.0 173.0,632.0Q235.0,632.0 269.0,608.5Q303.0,585.0 317.0,552.0Q331.0,519.0 331.0,489.0Q331.0,441.0 310.5,402.5Q290.0,364.0 241.0,317.0Q207.0,285.0 192.5,259.0Q178.0,233.0 178.0,197.0Q178.0,169.0 195.0,140.5Q212.0,112.0 254.0,93.0Q296.0,74.0 372.0,74.0Q451.0,74.0 494.0,95.0Q537.0,116.0 554.0,145.5Q571.0,175.0 571.0,200.0Q571.0,236.0 556.0,261.5Q541.0,287.0 502.0,324.0Q470.0,354.0 451.5,379.5Q433.0,405.0 425.5,433.0Q418.0,461.0 418.0,496.0Q418.0,527.0 433.5,558.0Q449.0,589.0 484.0,610.5Q519.0,632.0 578.0,632.0Q643.0,632.0 675.5,599.0Q708.0,566.0 708.0,514.0Q708.0,488.0 695.5,461.0Q683.0,434.0 651.0,414.0Q619.0,394.0 560.0,388.0L550.0,458.0Q594.0,461.0 614.0,477.0Q634.0,493.0 634.0,518.0Q634.0,541.0 622.0,554.5Q610.0,568.0 581.0,568.0Q545.0,568.0 520.5,546.5Q496.0,525.0 496.0,487.0Q496.0,455.0 511.0,429.0Q526.0,403.0 560.0,371.0Q593.0,340.0 622.0,297.0Q651.0,254.0 651.0,197.0Q651.0,142.0 622.5,97.0Q594.0,52.0 533.0,26.0Q472.0,0.0 372.0,0.0Z" transform="translate(2336, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3048 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M658.0,250.0Q610.0,250.0 573.0,271.5Q536.0,293.0 509.0,327.0Q482.0,361.0 463.0,400.0Q444.0,381.0 416.0,360.0Q386.0,338.0 365.5,319.0Q345.0,300.0 345.0,276.0Q345.0,234.0 389.0,234.0Q415.0,234.0 438.0,245.5Q461.0,257.0 489.0,282.0L565.0,255.0Q581.0,214.0 581.0,158.0Q581.0,88.0 530.0,44.0Q479.0,0.0 380.0,0.0Q333.0,0.0 284.0,15.0Q235.0,30.0 188.0,71.5Q141.0,113.0 100.0,191.0Q59.0,269.0 28.0,395.0L105.0,417.0Q131.0,308.0 162.5,240.5Q194.0,173.0 229.5,137.5Q265.0,102.0 303.0,89.0Q341.0,76.0 380.0,76.0Q438.0,76.0 471.5,100.0Q505.0,124.0 505.0,170.0Q505.0,184.0 502.0,199.0Q478.0,183.0 451.0,174.0Q424.0,165.0 390.0,165.0Q334.0,165.0 301.0,195.5Q268.0,226.0 268.0,272.0Q268.0,307.0 284.5,333.0Q301.0,359.0 325.5,379.5Q350.0,400.0 375.0,418.0Q404.0,439.0 425.5,460.0Q447.0,481.0 447.0,506.0Q447.0,515.0 442.5,526.5Q438.0,538.0 424.5,546.5Q411.0,555.0 384.0,555.0Q349.0,555.0 320.0,541.5Q291.0,528.0 274.0,509.0Q257.0,490.0 257.0,474.0Q257.0,460.0 266.0,449.0Q275.0,438.0 290.0,430.0L237.0,370.0Q202.0,390.0 188.5,417.0Q175.0,444.0 175.0,467.0Q175.0,494.0 192.0,522.0Q209.0,550.0 238.5,573.5Q268.0,597.0 305.5,611.5Q343.0,626.0 384.0,626.0Q433.0,626.0 467.0,607.0Q501.0,588.0 512.0,549.0Q548.0,587.0 587.0,607.0Q626.0,627.0 673.0,627.0Q732.0,627.0 765.0,598.0Q798.0,569.0 798.0,523.0Q798.0,504.0 789.5,484.0Q781.0,464.0 761.0,445.0Q779.0,431.0 791.5,410.0Q804.0,389.0 804.0,363.0Q804.0,318.0 772.0,288.0L787.0,272.0Q762.0,241.0 753.0,210.0Q744.0,179.0 744.0,144.0Q744.0,122.0 750.5,82.0Q757.0,42.0 770.0,9.0L699.0,-7.0Q685.0,37.0 677.0,81.0Q669.0,125.0 669.0,165.0Q669.0,190.0 673.0,211.5Q677.0,233.0 683.0,251.0Q671.0,250.0 658.0,250.0ZM669.0,559.0Q627.0,559.0 586.5,529.5Q546.0,500.0 516.0,454.0Q538.0,384.0 576.0,351.0Q614.0,318.0 666.0,318.0Q689.0,318.0 708.5,329.0Q728.0,340.0 728.0,370.0Q728.0,394.0 706.0,412.0Q683.0,403.0 655.0,396.0L639.0,460.0Q677.0,469.0 699.5,482.5Q722.0,496.0 722.0,521.0Q722.0,541.0 708.0,550.0Q694.0,559.0 669.0,559.0Z" transform="translate(0, 908)"/>
<path d="M681.0,225.0Q681.0,142.0 619.5,92.0Q558.0,42.0 453.0,42.0Q359.0,42.0 279.0,87.5Q199.0,133.0 136.0,235.5Q73.0,338.0 28.0,507.0L103.0,529.0Q143.0,386.0 192.5,295.0Q242.0,204.0 306.5,161.0Q371.0,118.0 455.0,118.0Q518.0,118.0 559.0,144.5Q600.0,171.0 600.0,228.0Q600.0,255.0 587.0,276.5Q574.0,298.0 552.0,314.0Q520.0,297.0 480.0,282.0L449.0,354.0Q516.0,376.0 553.5,405.5Q591.0,435.0 591.0,482.0Q591.0,558.0 509.0,558.0Q461.0,558.0 420.5,537.5Q380.0,517.0 355.5,489.5Q331.0,462.0 331.0,439.0Q331.0,423.0 341.0,411.5Q351.0,400.0 386.0,395.0L365.0,321.0Q308.0,332.0 279.5,360.0Q251.0,388.0 251.0,431.0Q251.0,465.0 271.5,499.5Q292.0,534.0 328.0,563.5Q364.0,593.0 410.5,611.0Q457.0,629.0 509.0,629.0Q586.0,629.0 628.5,590.0Q671.0,551.0 671.0,483.0Q671.0,445.0 655.5,414.0Q640.0,383.0 613.0,358.0Q681.0,308.0 681.0,225.0Z" transform="translate(842, 908)"/>
<path d="M681.0,225.0Q681.0,142.0 619.5,92.0Q558.0,42.0 453.0,42.0Q359.0,42.0 279.0,87.5Q199.0,133.0 136.0,235.5Q73.0,338.0 28.0,507.0L103.0,529.0Q143.0,386.0 192.5,295.0Q242.0,204.0 306.5,161.0Q371.0,118.0 455.0,118.0Q518.0,118.0 559.0,144.5Q600.0,171.0 600.0,228.0Q600.0,255.0 587.0,276.5Q574.0,298.0 552.0,314.0Q520.0,297.0 480.0,282.0L449.0,354.0Q516.0,376.0 553.5,405.5Q591.0,435.0 591.0,482.0Q591.0,558.0 509.0,558.0Q461.0,558.0 420.5,537.5Q380.0,517.0 355.5,489.5Q331.0,462.0 331.0,439.0Q331.0,423.0 341.0,411.5Q351.0,400.0 386.0,395.0L365.0,321.0Q308.0,332.0 279.5,360.0Q251.0,388.0 251.0,431.0Q251.0,465.0 271.5,499.5Q292.0,534.0 328.0,563.5Q364.0,593.0 410.5,611.0Q457.0,629.0 509.0,629.0Q586.0,629.0 628.5,590.0Q671.0,551.0 671.0,483.0Q671.0,445.0 655.5,414.0Q640.0,383.0 613.0,358.0Q681.0,308.0 681.0,225.0Z" transform="translate(1562, 908)"/>
<path d="M372.0,0.0Q277.0,0.0 216.5,26.0Q156.0,52.0 127.0,97.5Q98.0,143.0 98.0,199.0Q98.0,258.0 123.5,296.0Q149.0,334.0 191.0,375.0Q222.0,405.0 237.5,430.5Q253.0,456.0 253.0,493.0Q253.0,527.0 230.0,547.5Q207.0,568.0 175.0,568.0Q144.0,568.0 129.5,554.5Q115.0,541.0 115.0,518.0Q115.0,493.0 135.0,477.0Q155.0,461.0 199.0,458.0L189.0,389.0Q131.0,396.0 98.5,416.0Q66.0,436.0 53.0,464.0Q40.0,492.0 40.0,520.0Q40.0,570.0 76.0,601.0Q112.0,632.0 173.0,632.0Q235.0,632.0 269.0,608.5Q303.0,585.0 317.0,552.0Q331.0,519.0 331.0,489.0Q331.0,441.0 310.5,402.5Q290.0,364.0 241.0,317.0Q207.0,285.0 192.5,259.0Q178.0,233.0 178.0,197.0Q178.0,169.0 195.0,140.5Q212.0,112.0 254.0,93.0Q296.0,74.0 372.0,74.0Q451.0,74.0 494.0,95.0Q537.0,116.0 554.0,145.5Q571.0,175.0 571.0,200.0Q571.0,236.0 556.0,261.5Q541.0,287.0 502.0,324.0Q470.0,354.0 451.5,379.5Q433.0,405.0 425.5,433.0Q418.0,461.0 418.0,496.0Q418.0,527.0 433.5,558.0Q449.0,589.0 484.0,610.5Q519.0,632.0 578.0,632.0Q643.0,632.0 675.5,599.0Q708.0,566.0 708.0,514.0Q708.0,488.0 695.5,461.0Q683.0,434.0 651.0,414.0Q619.0,394.0 560.0,388.0L550.0,458.0Q594.0,461.0 614.0,477.0Q634.0,493.0 634.0,518.0Q634.0,541.0 622.0,554.5Q610.0,568.0 581.0,568.0Q545.0,568.0 520.5,546.5Q496.0,525.0 496.0,487.0Q496.0,455.0 511.0,429.0Q526.0,403.0 560.0,371.0Q593.0,340.0 622.0,297.0Q651.0,254.0 651.0,197.0Q651.0,142.0 622.5,97.0Q594.0,52.0 533.0,26.0Q472.0,0.0 372.0,0.0Z" transform="translate(2300, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">চৢল্ডূৎঙঢৣ</span> (Added by SIESTA)</li>


<pre>Expected: cabeng=0+567|lvocalicvowelsignbeng=0@-83,0+0|laddabeng=2+933|uuvowelsignbeng=2@-106,0+0|khandatabeng=6+507|ngabeng=7+723|ddhabeng=8+567|llvocalicvowelsignbeng=8@-83,0+0</pre>



<pre>Got     : cabeng=0+567|lvocalicvowelsignbeng=0@-83,0+0|laddabeng=2+933|uuvowelsignbeng=2@-106,0+0|khandatabeng=6+525|ngabeng=7+723|ddhabeng=8+567|llvocalicvowelsignbeng=8@-83,0+0</pre>



<pre>                                                                                                                  ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3315 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M577.0,622.0L577.0,551.0L172.0,551.0L172.0,532.0Q192.0,497.0 215.5,472.5Q239.0,448.0 273.0,435.5Q307.0,423.0 361.0,423.0L377.0,423.0Q415.0,423.0 435.5,418.0Q456.0,413.0 472.0,403.0Q517.0,375.0 517.0,306.0Q517.0,245.0 488.0,189.0Q459.0,133.0 415.0,95.0Q377.0,62.0 334.0,43.0Q291.0,24.0 238.0,24.0Q201.0,24.0 175.0,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L577.0,622.0ZM189.0,117.0Q207.0,96.0 244.0,96.0Q284.0,96.0 318.0,115.0Q352.0,134.0 379.0,162.0Q407.0,192.0 422.5,225.5Q438.0,259.0 438.0,296.0Q438.0,329.0 419.5,339.0Q401.0,349.0 368.0,349.0L363.0,349.0Q317.0,349.0 289.0,356.5Q261.0,364.0 235.0,377.0Q216.0,388.0 199.0,402.0Q182.0,416.0 170.0,433.0Q171.0,420.0 171.5,405.5Q172.0,391.0 172.0,378.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Z" transform="translate(0, 908)"/>
<path d="M-254.0,-127.0Q-200.0,-127.0 -173.0,-150.0Q-146.0,-173.0 -146.0,-208.0Q-146.0,-220.0 -150.5,-233.0Q-155.0,-246.0 -168.0,-258.0Q-108.0,-250.0 -84.0,-232.5Q-60.0,-215.0 -60.0,-187.0Q-60.0,-170.0 -68.5,-157.0Q-77.0,-144.0 -101.5,-131.0Q-126.0,-118.0 -174.0,-104.0Q-225.0,-88.0 -252.0,-71.5Q-279.0,-55.0 -279.0,-22.0Q-279.0,-5.0 -269.0,13.0L-213.0,0.0Q-217.0,-8.0 -217.0,-16.0Q-217.0,-26.0 -202.5,-33.0Q-188.0,-40.0 -139.0,-55.0Q-79.0,-73.0 -47.0,-92.5Q-15.0,-112.0 -3.5,-135.0Q8.0,-158.0 8.0,-185.0Q8.0,-232.0 -24.0,-260.5Q-56.0,-289.0 -107.5,-301.0Q-159.0,-313.0 -220.0,-313.0L-244.0,-313.0L-256.0,-264.0Q-229.0,-256.0 -217.0,-243.5Q-205.0,-231.0 -205.0,-214.0Q-205.0,-199.0 -216.0,-189.5Q-227.0,-180.0 -252.0,-180.0Q-292.0,-180.0 -292.0,-204.0Q-292.0,-213.0 -285.0,-227.0L-345.0,-238.0Q-356.0,-218.0 -356.0,-195.0Q-356.0,-166.0 -330.5,-146.5Q-305.0,-127.0 -254.0,-127.0Z" transform="translate(484, 908)"/>
<path d="M199.0,500.0Q286.0,500.0 342.0,431.0Q355.0,457.0 379.5,471.0Q404.0,485.0 432.0,485.0Q452.0,485.0 468.5,478.5Q485.0,472.0 501.0,460.0Q500.0,472.0 500.0,484.0Q500.0,496.0 500.0,509.0L500.0,551.0L-10.0,551.0L-10.0,622.0L943.0,622.0L943.0,551.0L577.0,551.0L577.0,353.0Q577.0,296.0 614.0,296.0Q643.0,296.0 675.0,323.5Q707.0,351.0 750.0,413.0L810.0,422.0Q842.0,375.0 859.5,325.0Q877.0,275.0 877.0,225.0Q877.0,160.0 848.5,110.0Q820.0,60.0 766.0,32.0Q712.0,4.0 637.0,4.0Q577.0,4.0 516.5,27.0Q456.0,50.0 403.0,103.5Q350.0,157.0 310.0,248.0L382.0,276.0Q422.0,185.0 481.5,132.5Q541.0,80.0 635.0,80.0Q713.0,80.0 757.0,120.0Q801.0,160.0 801.0,223.0Q801.0,257.0 794.0,283.5Q787.0,310.0 774.0,329.0Q735.0,275.0 694.0,248.5Q653.0,222.0 615.0,222.0Q567.0,222.0 538.0,248.0Q522.0,262.0 511.0,287.5Q500.0,313.0 500.0,373.0L500.0,386.0Q486.0,398.0 471.5,405.5Q457.0,413.0 440.0,413.0Q421.0,413.0 401.0,400.5Q381.0,388.0 381.0,352.0Q381.0,347.0 381.0,341.0Q381.0,335.0 382.0,328.0L318.0,325.0Q310.0,372.0 278.5,400.0Q247.0,428.0 207.0,428.0Q170.0,428.0 149.0,409.5Q128.0,391.0 128.0,361.0Q128.0,322.0 156.5,300.5Q185.0,279.0 234.0,262.0L207.0,188.0Q138.0,208.0 92.0,250.5Q46.0,293.0 46.0,366.0Q46.0,405.0 67.0,435.5Q88.0,466.0 122.5,483.0Q157.0,500.0 199.0,500.0Z" transform="translate(567, 908)"/>
<path d="M-177.0,-241.0Q-207.0,-241.0 -237.5,-230.5Q-268.0,-220.0 -288.0,-197.0Q-308.0,-174.0 -308.0,-137.0Q-308.0,-87.0 -268.0,-62.0Q-228.0,-37.0 -172.0,-36.0L-172.0,8.0L-95.0,8.0L-95.0,-56.0L-128.0,-102.0Q-135.0,-101.0 -144.5,-100.5Q-154.0,-100.0 -165.0,-100.0Q-235.0,-100.0 -235.0,-140.0Q-235.0,-159.0 -219.0,-169.0Q-203.0,-179.0 -179.0,-179.0Q-137.0,-179.0 -103.0,-159.0Q-69.0,-139.0 -38.0,-102.0Q7.0,-122.0 62.5,-154.0Q118.0,-186.0 163.0,-218.0L121.0,-271.0Q84.0,-243.0 46.0,-220.0Q8.0,-197.0 -22.0,-183.0Q-53.0,-211.0 -91.5,-226.0Q-130.0,-241.0 -177.0,-241.0Z" transform="translate(1394, 908)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(1500, 908)"/>
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(2025, 908)"/>
<path d="M577.0,622.0L577.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L577.0,622.0Z" transform="translate(2748, 908)"/>
<path d="M-449.0,-208.0Q-395.0,-208.0 -368.0,-231.0Q-341.0,-254.0 -341.0,-289.0Q-341.0,-301.0 -345.5,-314.0Q-350.0,-327.0 -363.0,-339.0Q-303.0,-331.0 -279.0,-313.5Q-255.0,-296.0 -255.0,-268.0Q-255.0,-251.0 -263.5,-238.0Q-272.0,-225.0 -296.5,-212.0Q-321.0,-199.0 -369.0,-185.0Q-420.0,-169.0 -447.0,-152.5Q-474.0,-136.0 -474.0,-103.0Q-474.0,-86.0 -464.0,-68.0L-408.0,-81.0Q-412.0,-89.0 -412.0,-97.0Q-412.0,-107.0 -397.5,-114.0Q-383.0,-121.0 -334.0,-136.0Q-274.0,-154.0 -242.0,-173.5Q-210.0,-193.0 -198.5,-216.0Q-187.0,-239.0 -187.0,-266.0Q-187.0,-313.0 -219.0,-341.5Q-251.0,-370.0 -302.5,-382.0Q-354.0,-394.0 -415.0,-394.0L-439.0,-394.0L-451.0,-345.0Q-424.0,-337.0 -412.0,-324.5Q-400.0,-312.0 -400.0,-295.0Q-400.0,-280.0 -411.0,-270.5Q-422.0,-261.0 -447.0,-261.0Q-487.0,-261.0 -487.0,-285.0Q-487.0,-294.0 -480.0,-308.0L-540.0,-319.0Q-551.0,-299.0 -551.0,-276.0Q-551.0,-247.0 -525.5,-227.5Q-500.0,-208.0 -449.0,-208.0ZM-142.0,-127.0Q-88.0,-127.0 -61.0,-150.0Q-34.0,-173.0 -34.0,-208.0Q-34.0,-220.0 -38.5,-233.0Q-43.0,-246.0 -56.0,-258.0Q4.0,-250.0 28.0,-232.5Q52.0,-215.0 52.0,-187.0Q52.0,-170.0 43.5,-157.0Q35.0,-144.0 10.5,-131.0Q-14.0,-118.0 -62.0,-104.0Q-113.0,-88.0 -140.0,-71.5Q-167.0,-55.0 -167.0,-22.0Q-167.0,-5.0 -157.0,13.0L-101.0,0.0Q-105.0,-8.0 -105.0,-16.0Q-105.0,-26.0 -90.5,-33.0Q-76.0,-40.0 -27.0,-55.0Q33.0,-73.0 65.0,-92.5Q97.0,-112.0 108.5,-135.0Q120.0,-158.0 120.0,-185.0Q120.0,-232.0 88.0,-260.5Q56.0,-289.0 4.5,-301.0Q-47.0,-313.0 -108.0,-313.0L-132.0,-313.0L-144.0,-264.0Q-117.0,-256.0 -105.0,-243.5Q-93.0,-231.0 -93.0,-214.0Q-93.0,-199.0 -104.0,-189.5Q-115.0,-180.0 -140.0,-180.0Q-180.0,-180.0 -180.0,-204.0Q-180.0,-213.0 -173.0,-227.0L-233.0,-238.0Q-244.0,-218.0 -244.0,-195.0Q-244.0,-166.0 -218.5,-146.5Q-193.0,-127.0 -142.0,-127.0Z" transform="translate(3232, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3297 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M577.0,622.0L577.0,551.0L172.0,551.0L172.0,532.0Q192.0,497.0 215.5,472.5Q239.0,448.0 273.0,435.5Q307.0,423.0 361.0,423.0L377.0,423.0Q415.0,423.0 435.5,418.0Q456.0,413.0 472.0,403.0Q517.0,375.0 517.0,306.0Q517.0,245.0 488.0,189.0Q459.0,133.0 415.0,95.0Q377.0,62.0 334.0,43.0Q291.0,24.0 238.0,24.0Q201.0,24.0 175.0,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L577.0,622.0ZM189.0,117.0Q207.0,96.0 244.0,96.0Q284.0,96.0 318.0,115.0Q352.0,134.0 379.0,162.0Q407.0,192.0 422.5,225.5Q438.0,259.0 438.0,296.0Q438.0,329.0 419.5,339.0Q401.0,349.0 368.0,349.0L363.0,349.0Q317.0,349.0 289.0,356.5Q261.0,364.0 235.0,377.0Q216.0,388.0 199.0,402.0Q182.0,416.0 170.0,433.0Q171.0,420.0 171.5,405.5Q172.0,391.0 172.0,378.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Z" transform="translate(0, 908)"/>
<path d="M-254.0,-127.0Q-200.0,-127.0 -173.0,-150.0Q-146.0,-173.0 -146.0,-208.0Q-146.0,-220.0 -150.5,-233.0Q-155.0,-246.0 -168.0,-258.0Q-108.0,-250.0 -84.0,-232.5Q-60.0,-215.0 -60.0,-187.0Q-60.0,-170.0 -68.5,-157.0Q-77.0,-144.0 -101.5,-131.0Q-126.0,-118.0 -174.0,-104.0Q-225.0,-88.0 -252.0,-71.5Q-279.0,-55.0 -279.0,-22.0Q-279.0,-5.0 -269.0,13.0L-213.0,0.0Q-217.0,-8.0 -217.0,-16.0Q-217.0,-26.0 -202.5,-33.0Q-188.0,-40.0 -139.0,-55.0Q-79.0,-73.0 -47.0,-92.5Q-15.0,-112.0 -3.5,-135.0Q8.0,-158.0 8.0,-185.0Q8.0,-232.0 -24.0,-260.5Q-56.0,-289.0 -107.5,-301.0Q-159.0,-313.0 -220.0,-313.0L-244.0,-313.0L-256.0,-264.0Q-229.0,-256.0 -217.0,-243.5Q-205.0,-231.0 -205.0,-214.0Q-205.0,-199.0 -216.0,-189.5Q-227.0,-180.0 -252.0,-180.0Q-292.0,-180.0 -292.0,-204.0Q-292.0,-213.0 -285.0,-227.0L-345.0,-238.0Q-356.0,-218.0 -356.0,-195.0Q-356.0,-166.0 -330.5,-146.5Q-305.0,-127.0 -254.0,-127.0Z" transform="translate(484, 908)"/>
<path d="M199.0,500.0Q286.0,500.0 342.0,431.0Q355.0,457.0 379.5,471.0Q404.0,485.0 432.0,485.0Q452.0,485.0 468.5,478.5Q485.0,472.0 501.0,460.0Q500.0,472.0 500.0,484.0Q500.0,496.0 500.0,509.0L500.0,551.0L-10.0,551.0L-10.0,622.0L943.0,622.0L943.0,551.0L577.0,551.0L577.0,353.0Q577.0,296.0 614.0,296.0Q643.0,296.0 675.0,323.5Q707.0,351.0 750.0,413.0L810.0,422.0Q842.0,375.0 859.5,325.0Q877.0,275.0 877.0,225.0Q877.0,160.0 848.5,110.0Q820.0,60.0 766.0,32.0Q712.0,4.0 637.0,4.0Q577.0,4.0 516.5,27.0Q456.0,50.0 403.0,103.5Q350.0,157.0 310.0,248.0L382.0,276.0Q422.0,185.0 481.5,132.5Q541.0,80.0 635.0,80.0Q713.0,80.0 757.0,120.0Q801.0,160.0 801.0,223.0Q801.0,257.0 794.0,283.5Q787.0,310.0 774.0,329.0Q735.0,275.0 694.0,248.5Q653.0,222.0 615.0,222.0Q567.0,222.0 538.0,248.0Q522.0,262.0 511.0,287.5Q500.0,313.0 500.0,373.0L500.0,386.0Q486.0,398.0 471.5,405.5Q457.0,413.0 440.0,413.0Q421.0,413.0 401.0,400.5Q381.0,388.0 381.0,352.0Q381.0,347.0 381.0,341.0Q381.0,335.0 382.0,328.0L318.0,325.0Q310.0,372.0 278.5,400.0Q247.0,428.0 207.0,428.0Q170.0,428.0 149.0,409.5Q128.0,391.0 128.0,361.0Q128.0,322.0 156.5,300.5Q185.0,279.0 234.0,262.0L207.0,188.0Q138.0,208.0 92.0,250.5Q46.0,293.0 46.0,366.0Q46.0,405.0 67.0,435.5Q88.0,466.0 122.5,483.0Q157.0,500.0 199.0,500.0Z" transform="translate(567, 908)"/>
<path d="M-177.0,-241.0Q-207.0,-241.0 -237.5,-230.5Q-268.0,-220.0 -288.0,-197.0Q-308.0,-174.0 -308.0,-137.0Q-308.0,-87.0 -268.0,-62.0Q-228.0,-37.0 -172.0,-36.0L-172.0,8.0L-95.0,8.0L-95.0,-56.0L-128.0,-102.0Q-135.0,-101.0 -144.5,-100.5Q-154.0,-100.0 -165.0,-100.0Q-235.0,-100.0 -235.0,-140.0Q-235.0,-159.0 -219.0,-169.0Q-203.0,-179.0 -179.0,-179.0Q-137.0,-179.0 -103.0,-159.0Q-69.0,-139.0 -38.0,-102.0Q7.0,-122.0 62.5,-154.0Q118.0,-186.0 163.0,-218.0L121.0,-271.0Q84.0,-243.0 46.0,-220.0Q8.0,-197.0 -22.0,-183.0Q-53.0,-211.0 -91.5,-226.0Q-130.0,-241.0 -177.0,-241.0Z" transform="translate(1394, 908)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(1500, 908)"/>
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(2007, 908)"/>
<path d="M577.0,622.0L577.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L577.0,622.0Z" transform="translate(2730, 908)"/>
<path d="M-449.0,-208.0Q-395.0,-208.0 -368.0,-231.0Q-341.0,-254.0 -341.0,-289.0Q-341.0,-301.0 -345.5,-314.0Q-350.0,-327.0 -363.0,-339.0Q-303.0,-331.0 -279.0,-313.5Q-255.0,-296.0 -255.0,-268.0Q-255.0,-251.0 -263.5,-238.0Q-272.0,-225.0 -296.5,-212.0Q-321.0,-199.0 -369.0,-185.0Q-420.0,-169.0 -447.0,-152.5Q-474.0,-136.0 -474.0,-103.0Q-474.0,-86.0 -464.0,-68.0L-408.0,-81.0Q-412.0,-89.0 -412.0,-97.0Q-412.0,-107.0 -397.5,-114.0Q-383.0,-121.0 -334.0,-136.0Q-274.0,-154.0 -242.0,-173.5Q-210.0,-193.0 -198.5,-216.0Q-187.0,-239.0 -187.0,-266.0Q-187.0,-313.0 -219.0,-341.5Q-251.0,-370.0 -302.5,-382.0Q-354.0,-394.0 -415.0,-394.0L-439.0,-394.0L-451.0,-345.0Q-424.0,-337.0 -412.0,-324.5Q-400.0,-312.0 -400.0,-295.0Q-400.0,-280.0 -411.0,-270.5Q-422.0,-261.0 -447.0,-261.0Q-487.0,-261.0 -487.0,-285.0Q-487.0,-294.0 -480.0,-308.0L-540.0,-319.0Q-551.0,-299.0 -551.0,-276.0Q-551.0,-247.0 -525.5,-227.5Q-500.0,-208.0 -449.0,-208.0ZM-142.0,-127.0Q-88.0,-127.0 -61.0,-150.0Q-34.0,-173.0 -34.0,-208.0Q-34.0,-220.0 -38.5,-233.0Q-43.0,-246.0 -56.0,-258.0Q4.0,-250.0 28.0,-232.5Q52.0,-215.0 52.0,-187.0Q52.0,-170.0 43.5,-157.0Q35.0,-144.0 10.5,-131.0Q-14.0,-118.0 -62.0,-104.0Q-113.0,-88.0 -140.0,-71.5Q-167.0,-55.0 -167.0,-22.0Q-167.0,-5.0 -157.0,13.0L-101.0,0.0Q-105.0,-8.0 -105.0,-16.0Q-105.0,-26.0 -90.5,-33.0Q-76.0,-40.0 -27.0,-55.0Q33.0,-73.0 65.0,-92.5Q97.0,-112.0 108.5,-135.0Q120.0,-158.0 120.0,-185.0Q120.0,-232.0 88.0,-260.5Q56.0,-289.0 4.5,-301.0Q-47.0,-313.0 -108.0,-313.0L-132.0,-313.0L-144.0,-264.0Q-117.0,-256.0 -105.0,-243.5Q-93.0,-231.0 -93.0,-214.0Q-93.0,-199.0 -104.0,-189.5Q-115.0,-180.0 -140.0,-180.0Q-180.0,-180.0 -180.0,-204.0Q-180.0,-213.0 -173.0,-227.0L-233.0,-238.0Q-244.0,-218.0 -244.0,-195.0Q-244.0,-166.0 -218.5,-146.5Q-193.0,-127.0 -142.0,-127.0Z" transform="translate(3214, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">মৢথ্ᳶিফংঐচ॑</span> (Added by SIESTA)</li>


<pre>Expected: mabeng=0+622|lvocalicvowelsignbeng=0+0|thabeng=2+645|viramabeng=2+0|ivowelsignbeng=4+266|uni1CF6=4+628|phabeng=6+838|anusvarabeng=6+403|aibeng=8+873|cabeng=9+567|uni0951=9@-29,323+0</pre>



<pre>Got     : mabeng=0+622|lvocalicvowelsignbeng=0+0|thabeng=2+645|viramabeng=2+0|ivowelsignbeng=4+266|uni1CF6=4+628|phabeng=6+838|anusvarabeng=6+438|aibeng=8+873|cabeng=9+567|uni0951=9@-29,323+0</pre>



<pre>                                                                                                                                               +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4877 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M632.0,622.0L632.0,551.0L527.0,551.0L527.0,0.0L450.0,0.0L450.0,109.0Q418.0,156.0 385.0,195.0Q352.0,234.0 315.5,257.5Q279.0,281.0 236.0,281.0Q199.0,281.0 173.5,262.0Q148.0,243.0 148.0,205.0Q148.0,172.0 172.0,149.5Q196.0,127.0 243.0,111.0L218.0,34.0Q137.0,63.0 101.5,108.5Q66.0,154.0 66.0,208.0Q66.0,256.0 89.5,288.0Q113.0,320.0 148.0,336.5Q183.0,353.0 218.0,353.0Q210.0,422.0 169.5,453.5Q129.0,485.0 38.0,494.0L48.0,551.0L-10.0,551.0L-10.0,622.0L632.0,622.0ZM450.0,551.0L116.0,551.0Q199.0,540.0 246.5,489.5Q294.0,439.0 299.0,342.0Q348.0,327.0 385.0,294.0Q422.0,261.0 452.0,219.0Q451.0,234.0 450.5,249.5Q450.0,265.0 450.0,281.0L450.0,551.0Z" transform="translate(0, 908)"/>
<path d="M-254.0,-127.0Q-200.0,-127.0 -173.0,-150.0Q-146.0,-173.0 -146.0,-208.0Q-146.0,-220.0 -150.5,-233.0Q-155.0,-246.0 -168.0,-258.0Q-108.0,-250.0 -84.0,-232.5Q-60.0,-215.0 -60.0,-187.0Q-60.0,-170.0 -68.5,-157.0Q-77.0,-144.0 -101.5,-131.0Q-126.0,-118.0 -174.0,-104.0Q-225.0,-88.0 -252.0,-71.5Q-279.0,-55.0 -279.0,-22.0Q-279.0,-5.0 -269.0,13.0L-213.0,0.0Q-217.0,-8.0 -217.0,-16.0Q-217.0,-26.0 -202.5,-33.0Q-188.0,-40.0 -139.0,-55.0Q-79.0,-73.0 -47.0,-92.5Q-15.0,-112.0 -3.5,-135.0Q8.0,-158.0 8.0,-185.0Q8.0,-232.0 -24.0,-260.5Q-56.0,-289.0 -107.5,-301.0Q-159.0,-313.0 -220.0,-313.0L-244.0,-313.0L-256.0,-264.0Q-229.0,-256.0 -217.0,-243.5Q-205.0,-231.0 -205.0,-214.0Q-205.0,-199.0 -216.0,-189.5Q-227.0,-180.0 -252.0,-180.0Q-292.0,-180.0 -292.0,-204.0Q-292.0,-213.0 -285.0,-227.0L-345.0,-238.0Q-356.0,-218.0 -356.0,-195.0Q-356.0,-166.0 -330.5,-146.5Q-305.0,-127.0 -254.0,-127.0Z" transform="translate(622, 908)"/>
<path d="M211.0,625.0Q306.0,625.0 353.0,578.5Q400.0,532.0 400.0,464.0Q400.0,394.0 348.0,347.0Q296.0,300.0 203.0,282.0Q303.0,253.0 370.5,202.0Q438.0,151.0 475.0,97.0Q474.0,120.0 473.5,143.0Q473.0,166.0 473.0,193.0L473.0,688.0L526.0,688.0L549.0,622.0L655.0,622.0L655.0,551.0L550.0,551.0L550.0,0.0L473.0,0.0Q435.0,55.0 383.0,103.5Q331.0,152.0 264.5,187.5Q198.0,223.0 115.0,238.0L92.0,331.0Q176.0,337.0 226.0,355.5Q276.0,374.0 297.5,402.5Q319.0,431.0 319.0,466.0Q319.0,509.0 291.0,532.0Q263.0,555.0 209.0,555.0Q159.0,555.0 137.5,535.5Q116.0,516.0 116.0,494.0Q116.0,480.0 123.5,468.0Q131.0,456.0 150.0,446.0L106.0,384.0Q78.0,403.0 58.0,430.0Q38.0,457.0 38.0,497.0Q38.0,550.0 83.0,587.5Q128.0,625.0 211.0,625.0Z" transform="translate(622, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(1267, 908)"/>
<path d="M276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L82.0,622.0Q66.0,641.0 49.5,662.0Q33.0,683.0 20.0,704.0Q54.0,763.0 93.0,811.5Q132.0,860.0 185.0,888.5Q238.0,917.0 313.0,917.0Q384.0,917.0 447.0,894.0Q510.0,871.0 573.0,829.5Q636.0,788.0 705.0,731.0L663.0,677.0Q594.0,733.0 538.5,770.0Q483.0,807.0 432.5,825.5Q382.0,844.0 325.0,844.0Q242.0,844.0 192.0,802.0Q142.0,760.0 106.0,693.0Q114.0,678.0 128.0,660.0Q142.0,642.0 160.0,622.0L276.0,622.0Z" transform="translate(1267, 908)"/>
<path d="M198.0,195.0Q153.0,195.0 120.5,214.0Q88.0,233.0 69.5,282.0Q51.0,331.0 47.0,422.0L126.0,427.0Q128.0,359.0 136.5,324.5Q145.0,290.0 161.5,278.0Q178.0,266.0 202.0,266.0Q245.0,266.0 259.5,300.5Q274.0,335.0 277.0,423.0L351.0,423.0Q354.0,335.0 370.0,300.5Q386.0,266.0 427.0,266.0Q449.0,266.0 465.0,278.5Q481.0,291.0 490.5,325.5Q500.0,360.0 502.0,427.0L581.0,422.0Q578.0,331.0 559.5,282.0Q541.0,233.0 508.5,214.0Q476.0,195.0 431.0,195.0Q387.0,195.0 359.5,214.0Q332.0,233.0 314.0,279.0Q296.0,233.0 268.5,214.0Q241.0,195.0 198.0,195.0Z" transform="translate(1533, 908)"/>
<path d="M848.0,622.0L848.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.5,327.5Q184.0,301.0 142.0,276.0Q246.0,250.0 316.0,207.5Q386.0,165.0 447.0,99.0Q446.0,116.0 445.5,134.0Q445.0,152.0 445.0,171.0L445.0,510.0L458.0,510.0Q540.0,510.0 614.0,488.5Q688.0,467.0 739.0,414.0Q763.0,389.0 777.5,357.5Q792.0,326.0 792.0,288.0Q792.0,255.0 778.5,225.5Q765.0,196.0 735.0,177.0Q705.0,158.0 655.0,158.0Q640.0,158.0 625.5,159.0Q611.0,160.0 597.0,163.0L602.0,234.0Q608.0,233.0 617.0,232.5Q626.0,232.0 636.0,232.0Q685.0,232.0 699.5,251.0Q714.0,270.0 714.0,296.0Q714.0,347.0 662.5,386.0Q611.0,425.0 522.0,434.0L522.0,0.0L445.0,0.0Q404.0,56.0 354.5,98.0Q305.0,140.0 239.5,168.5Q174.0,197.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L848.0,622.0Z" transform="translate(2161, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(2999, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,454.0Q700.0,470.0 726.5,498.0Q753.0,526.0 753.0,573.0Q753.0,598.0 744.5,616.5Q736.0,635.0 720.0,649.0Q701.0,665.0 670.5,675.5Q640.0,686.0 586.0,693.0L482.0,707.0Q389.0,720.0 347.0,759.5Q305.0,799.0 305.0,875.0Q305.0,884.0 306.5,896.0Q308.0,908.0 309.0,917.0L383.0,913.0Q382.0,906.0 381.0,896.0Q380.0,886.0 380.0,878.0Q380.0,838.0 400.0,814.0Q421.0,790.0 474.0,783.0L605.0,765.0Q671.0,756.0 712.0,741.0Q753.0,726.0 779.0,702.0Q804.0,679.0 817.5,646.5Q831.0,614.0 831.0,575.0Q831.0,523.0 808.5,485.5Q786.0,448.0 748.5,421.0Q711.0,394.0 667.0,374.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(3437, 908)"/>
<path d="M577.0,622.0L577.0,551.0L172.0,551.0L172.0,532.0Q192.0,497.0 215.5,472.5Q239.0,448.0 273.0,435.5Q307.0,423.0 361.0,423.0L377.0,423.0Q415.0,423.0 435.5,418.0Q456.0,413.0 472.0,403.0Q517.0,375.0 517.0,306.0Q517.0,245.0 488.0,189.0Q459.0,133.0 415.0,95.0Q377.0,62.0 334.0,43.0Q291.0,24.0 238.0,24.0Q201.0,24.0 175.0,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L577.0,622.0ZM189.0,117.0Q207.0,96.0 244.0,96.0Q284.0,96.0 318.0,115.0Q352.0,134.0 379.0,162.0Q407.0,192.0 422.5,225.5Q438.0,259.0 438.0,296.0Q438.0,329.0 419.5,339.0Q401.0,349.0 368.0,349.0L363.0,349.0Q317.0,349.0 289.0,356.5Q261.0,364.0 235.0,377.0Q216.0,388.0 199.0,402.0Q182.0,416.0 170.0,433.0Q171.0,420.0 171.5,405.5Q172.0,391.0 172.0,378.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Z" transform="translate(4310, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(4848, 1231)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4842 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M632.0,622.0L632.0,551.0L527.0,551.0L527.0,0.0L450.0,0.0L450.0,109.0Q418.0,156.0 385.0,195.0Q352.0,234.0 315.5,257.5Q279.0,281.0 236.0,281.0Q199.0,281.0 173.5,262.0Q148.0,243.0 148.0,205.0Q148.0,172.0 172.0,149.5Q196.0,127.0 243.0,111.0L218.0,34.0Q137.0,63.0 101.5,108.5Q66.0,154.0 66.0,208.0Q66.0,256.0 89.5,288.0Q113.0,320.0 148.0,336.5Q183.0,353.0 218.0,353.0Q210.0,422.0 169.5,453.5Q129.0,485.0 38.0,494.0L48.0,551.0L-10.0,551.0L-10.0,622.0L632.0,622.0ZM450.0,551.0L116.0,551.0Q199.0,540.0 246.5,489.5Q294.0,439.0 299.0,342.0Q348.0,327.0 385.0,294.0Q422.0,261.0 452.0,219.0Q451.0,234.0 450.5,249.5Q450.0,265.0 450.0,281.0L450.0,551.0Z" transform="translate(0, 908)"/>
<path d="M-254.0,-127.0Q-200.0,-127.0 -173.0,-150.0Q-146.0,-173.0 -146.0,-208.0Q-146.0,-220.0 -150.5,-233.0Q-155.0,-246.0 -168.0,-258.0Q-108.0,-250.0 -84.0,-232.5Q-60.0,-215.0 -60.0,-187.0Q-60.0,-170.0 -68.5,-157.0Q-77.0,-144.0 -101.5,-131.0Q-126.0,-118.0 -174.0,-104.0Q-225.0,-88.0 -252.0,-71.5Q-279.0,-55.0 -279.0,-22.0Q-279.0,-5.0 -269.0,13.0L-213.0,0.0Q-217.0,-8.0 -217.0,-16.0Q-217.0,-26.0 -202.5,-33.0Q-188.0,-40.0 -139.0,-55.0Q-79.0,-73.0 -47.0,-92.5Q-15.0,-112.0 -3.5,-135.0Q8.0,-158.0 8.0,-185.0Q8.0,-232.0 -24.0,-260.5Q-56.0,-289.0 -107.5,-301.0Q-159.0,-313.0 -220.0,-313.0L-244.0,-313.0L-256.0,-264.0Q-229.0,-256.0 -217.0,-243.5Q-205.0,-231.0 -205.0,-214.0Q-205.0,-199.0 -216.0,-189.5Q-227.0,-180.0 -252.0,-180.0Q-292.0,-180.0 -292.0,-204.0Q-292.0,-213.0 -285.0,-227.0L-345.0,-238.0Q-356.0,-218.0 -356.0,-195.0Q-356.0,-166.0 -330.5,-146.5Q-305.0,-127.0 -254.0,-127.0Z" transform="translate(622, 908)"/>
<path d="M211.0,625.0Q306.0,625.0 353.0,578.5Q400.0,532.0 400.0,464.0Q400.0,394.0 348.0,347.0Q296.0,300.0 203.0,282.0Q303.0,253.0 370.5,202.0Q438.0,151.0 475.0,97.0Q474.0,120.0 473.5,143.0Q473.0,166.0 473.0,193.0L473.0,688.0L526.0,688.0L549.0,622.0L655.0,622.0L655.0,551.0L550.0,551.0L550.0,0.0L473.0,0.0Q435.0,55.0 383.0,103.5Q331.0,152.0 264.5,187.5Q198.0,223.0 115.0,238.0L92.0,331.0Q176.0,337.0 226.0,355.5Q276.0,374.0 297.5,402.5Q319.0,431.0 319.0,466.0Q319.0,509.0 291.0,532.0Q263.0,555.0 209.0,555.0Q159.0,555.0 137.5,535.5Q116.0,516.0 116.0,494.0Q116.0,480.0 123.5,468.0Q131.0,456.0 150.0,446.0L106.0,384.0Q78.0,403.0 58.0,430.0Q38.0,457.0 38.0,497.0Q38.0,550.0 83.0,587.5Q128.0,625.0 211.0,625.0Z" transform="translate(622, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(1267, 908)"/>
<path d="M276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L82.0,622.0Q66.0,641.0 49.5,662.0Q33.0,683.0 20.0,704.0Q54.0,763.0 93.0,811.5Q132.0,860.0 185.0,888.5Q238.0,917.0 313.0,917.0Q384.0,917.0 447.0,894.0Q510.0,871.0 573.0,829.5Q636.0,788.0 705.0,731.0L663.0,677.0Q594.0,733.0 538.5,770.0Q483.0,807.0 432.5,825.5Q382.0,844.0 325.0,844.0Q242.0,844.0 192.0,802.0Q142.0,760.0 106.0,693.0Q114.0,678.0 128.0,660.0Q142.0,642.0 160.0,622.0L276.0,622.0Z" transform="translate(1267, 908)"/>
<path d="M198.0,195.0Q153.0,195.0 120.5,214.0Q88.0,233.0 69.5,282.0Q51.0,331.0 47.0,422.0L126.0,427.0Q128.0,359.0 136.5,324.5Q145.0,290.0 161.5,278.0Q178.0,266.0 202.0,266.0Q245.0,266.0 259.5,300.5Q274.0,335.0 277.0,423.0L351.0,423.0Q354.0,335.0 370.0,300.5Q386.0,266.0 427.0,266.0Q449.0,266.0 465.0,278.5Q481.0,291.0 490.5,325.5Q500.0,360.0 502.0,427.0L581.0,422.0Q578.0,331.0 559.5,282.0Q541.0,233.0 508.5,214.0Q476.0,195.0 431.0,195.0Q387.0,195.0 359.5,214.0Q332.0,233.0 314.0,279.0Q296.0,233.0 268.5,214.0Q241.0,195.0 198.0,195.0Z" transform="translate(1533, 908)"/>
<path d="M848.0,622.0L848.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.5,327.5Q184.0,301.0 142.0,276.0Q246.0,250.0 316.0,207.5Q386.0,165.0 447.0,99.0Q446.0,116.0 445.5,134.0Q445.0,152.0 445.0,171.0L445.0,510.0L458.0,510.0Q540.0,510.0 614.0,488.5Q688.0,467.0 739.0,414.0Q763.0,389.0 777.5,357.5Q792.0,326.0 792.0,288.0Q792.0,255.0 778.5,225.5Q765.0,196.0 735.0,177.0Q705.0,158.0 655.0,158.0Q640.0,158.0 625.5,159.0Q611.0,160.0 597.0,163.0L602.0,234.0Q608.0,233.0 617.0,232.5Q626.0,232.0 636.0,232.0Q685.0,232.0 699.5,251.0Q714.0,270.0 714.0,296.0Q714.0,347.0 662.5,386.0Q611.0,425.0 522.0,434.0L522.0,0.0L445.0,0.0Q404.0,56.0 354.5,98.0Q305.0,140.0 239.5,168.5Q174.0,197.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L848.0,622.0Z" transform="translate(2161, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(2999, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,454.0Q700.0,470.0 726.5,498.0Q753.0,526.0 753.0,573.0Q753.0,598.0 744.5,616.5Q736.0,635.0 720.0,649.0Q701.0,665.0 670.5,675.5Q640.0,686.0 586.0,693.0L482.0,707.0Q389.0,720.0 347.0,759.5Q305.0,799.0 305.0,875.0Q305.0,884.0 306.5,896.0Q308.0,908.0 309.0,917.0L383.0,913.0Q382.0,906.0 381.0,896.0Q380.0,886.0 380.0,878.0Q380.0,838.0 400.0,814.0Q421.0,790.0 474.0,783.0L605.0,765.0Q671.0,756.0 712.0,741.0Q753.0,726.0 779.0,702.0Q804.0,679.0 817.5,646.5Q831.0,614.0 831.0,575.0Q831.0,523.0 808.5,485.5Q786.0,448.0 748.5,421.0Q711.0,394.0 667.0,374.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(3402, 908)"/>
<path d="M577.0,622.0L577.0,551.0L172.0,551.0L172.0,532.0Q192.0,497.0 215.5,472.5Q239.0,448.0 273.0,435.5Q307.0,423.0 361.0,423.0L377.0,423.0Q415.0,423.0 435.5,418.0Q456.0,413.0 472.0,403.0Q517.0,375.0 517.0,306.0Q517.0,245.0 488.0,189.0Q459.0,133.0 415.0,95.0Q377.0,62.0 334.0,43.0Q291.0,24.0 238.0,24.0Q201.0,24.0 175.0,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L577.0,622.0ZM189.0,117.0Q207.0,96.0 244.0,96.0Q284.0,96.0 318.0,115.0Q352.0,134.0 379.0,162.0Q407.0,192.0 422.5,225.5Q438.0,259.0 438.0,296.0Q438.0,329.0 419.5,339.0Q401.0,349.0 368.0,349.0L363.0,349.0Q317.0,349.0 289.0,356.5Q261.0,364.0 235.0,377.0Q216.0,388.0 199.0,402.0Q182.0,416.0 170.0,433.0Q171.0,420.0 171.5,405.5Q172.0,391.0 172.0,378.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Z" transform="translate(4275, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(4813, 1231)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঋৎ৲৾ঠীগ॑ণ্</span> (Added by SIESTA)</li>


<pre>Expected: rvocalicbeng=0+835|khandatabeng=1+525|rupeemarkbeng=2+589|uni25CC=2+510|uni09FE=2+0|tthabeng=4+591|iivowelsignshortbeng=4+266|gabeng=6+656|uni0951=6@-73,323+0|nnabeng=8+620|viramabeng=8+0</pre>



<pre>Got     : rvocalicbeng=0+853|khandatabeng=1+525|rupeemarkbeng=2+589|uni25CC=2+510|uni09FE=2+0|tthabeng=4+591|iivowelsignshortbeng=4+266|gabeng=6+656|uni0951=6@-73,323+0|nnabeng=8+620|viramabeng=8+0</pre>



<pre>                          +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4610 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(0, 908)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(853, 908)"/>
<path d="M441.0,99.0Q399.0,194.0 350.0,258.5Q301.0,323.0 234.0,365.5Q167.0,408.0 71.0,435.0L102.0,516.0Q199.0,486.0 275.5,440.0Q352.0,394.0 412.0,318.5Q472.0,243.0 519.0,126.0L441.0,99.0Z" transform="translate(1378, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1967, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(2477, 908)"/>
<path d="M282.0,0.0Q192.0,0.0 128.0,47.0Q64.0,94.0 36.0,168.0L58.0,247.0Q140.0,255.0 184.0,283.0Q228.0,311.0 245.5,353.5Q263.0,396.0 263.0,448.0Q263.0,471.0 258.0,498.0Q253.0,525.0 242.0,551.0L-10.0,551.0L-10.0,622.0L200.0,622.0Q168.0,666.0 148.5,702.5Q129.0,739.0 129.0,776.0Q129.0,818.0 152.0,852.0Q175.0,886.0 218.0,917.0L269.0,861.0Q237.0,836.0 222.5,814.5Q208.0,793.0 208.0,764.0Q208.0,733.0 230.5,699.5Q253.0,666.0 291.0,622.0L601.0,622.0L601.0,551.0L427.0,551.0Q408.0,551.0 394.0,551.5Q380.0,552.0 365.0,553.0Q438.0,480.0 483.5,406.0Q529.0,332.0 529.0,240.0Q529.0,169.0 500.0,115.0Q471.0,61.0 416.0,30.5Q361.0,0.0 282.0,0.0ZM280.0,74.0Q338.0,74.0 375.0,98.0Q412.0,122.0 430.0,161.0Q448.0,200.0 448.0,244.0Q448.0,308.0 419.0,369.5Q390.0,431.0 316.0,512.0Q323.0,489.0 328.0,463.5Q333.0,438.0 333.0,406.0Q333.0,359.0 315.0,313.5Q297.0,268.0 250.0,232.0Q203.0,196.0 117.0,175.0Q141.0,123.0 186.0,98.5Q231.0,74.0 280.0,74.0Z" transform="translate(2477, 908)"/>
<path d="M276.0,551.0L171.0,551.0L171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L94.0,622.0Q90.0,687.0 61.5,731.0Q33.0,775.0 -12.0,800.5Q-57.0,826.0 -113.5,837.0Q-170.0,848.0 -231.0,848.0Q-287.0,848.0 -318.5,840.5Q-350.0,833.0 -362.5,820.5Q-375.0,808.0 -375.0,793.0Q-375.0,774.0 -355.0,768.5Q-335.0,763.0 -305.0,763.0L-264.0,763.0Q-211.0,763.0 -180.0,754.0Q-149.0,745.0 -130.0,725.0Q-95.0,690.0 -95.0,615.0L-162.0,615.0Q-163.0,662.0 -184.0,678.0Q-194.0,686.0 -208.5,689.0Q-223.0,692.0 -250.0,692.0L-285.0,692.0Q-325.0,692.0 -356.0,700.5Q-387.0,709.0 -407.0,719.0Q-432.0,733.0 -442.0,752.5Q-452.0,772.0 -452.0,790.0Q-452.0,843.0 -401.5,880.0Q-351.0,917.0 -237.0,917.0Q-50.0,917.0 57.0,845.5Q164.0,774.0 174.0,622.0L276.0,622.0L276.0,551.0Z" transform="translate(3068, 908)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(3334, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(3917, 1231)"/>
<path d="M630.0,622.0L630.0,551.0L525.0,551.0L525.0,0.0L448.0,0.0L448.0,391.0Q386.0,476.0 332.0,516.0Q278.0,556.0 222.0,556.0Q175.0,556.0 148.5,530.0Q122.0,504.0 122.0,463.0Q122.0,414.0 157.5,388.5Q193.0,363.0 275.0,355.0L269.0,272.0Q203.0,278.0 151.5,300.5Q100.0,323.0 70.0,363.5Q40.0,404.0 40.0,462.0Q40.0,516.0 64.0,553.5Q88.0,591.0 127.0,610.0Q166.0,629.0 211.0,629.0Q283.0,629.0 338.5,594.5Q394.0,560.0 452.0,494.0Q450.0,512.0 449.0,534.5Q448.0,557.0 448.0,576.0L448.0,688.0L501.0,688.0L524.0,622.0L630.0,622.0Z" transform="translate(3990, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(4610, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4592 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(0, 908)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(835, 908)"/>
<path d="M441.0,99.0Q399.0,194.0 350.0,258.5Q301.0,323.0 234.0,365.5Q167.0,408.0 71.0,435.0L102.0,516.0Q199.0,486.0 275.5,440.0Q352.0,394.0 412.0,318.5Q472.0,243.0 519.0,126.0L441.0,99.0Z" transform="translate(1360, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1949, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(2459, 908)"/>
<path d="M282.0,0.0Q192.0,0.0 128.0,47.0Q64.0,94.0 36.0,168.0L58.0,247.0Q140.0,255.0 184.0,283.0Q228.0,311.0 245.5,353.5Q263.0,396.0 263.0,448.0Q263.0,471.0 258.0,498.0Q253.0,525.0 242.0,551.0L-10.0,551.0L-10.0,622.0L200.0,622.0Q168.0,666.0 148.5,702.5Q129.0,739.0 129.0,776.0Q129.0,818.0 152.0,852.0Q175.0,886.0 218.0,917.0L269.0,861.0Q237.0,836.0 222.5,814.5Q208.0,793.0 208.0,764.0Q208.0,733.0 230.5,699.5Q253.0,666.0 291.0,622.0L601.0,622.0L601.0,551.0L427.0,551.0Q408.0,551.0 394.0,551.5Q380.0,552.0 365.0,553.0Q438.0,480.0 483.5,406.0Q529.0,332.0 529.0,240.0Q529.0,169.0 500.0,115.0Q471.0,61.0 416.0,30.5Q361.0,0.0 282.0,0.0ZM280.0,74.0Q338.0,74.0 375.0,98.0Q412.0,122.0 430.0,161.0Q448.0,200.0 448.0,244.0Q448.0,308.0 419.0,369.5Q390.0,431.0 316.0,512.0Q323.0,489.0 328.0,463.5Q333.0,438.0 333.0,406.0Q333.0,359.0 315.0,313.5Q297.0,268.0 250.0,232.0Q203.0,196.0 117.0,175.0Q141.0,123.0 186.0,98.5Q231.0,74.0 280.0,74.0Z" transform="translate(2459, 908)"/>
<path d="M276.0,551.0L171.0,551.0L171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L94.0,622.0Q90.0,687.0 61.5,731.0Q33.0,775.0 -12.0,800.5Q-57.0,826.0 -113.5,837.0Q-170.0,848.0 -231.0,848.0Q-287.0,848.0 -318.5,840.5Q-350.0,833.0 -362.5,820.5Q-375.0,808.0 -375.0,793.0Q-375.0,774.0 -355.0,768.5Q-335.0,763.0 -305.0,763.0L-264.0,763.0Q-211.0,763.0 -180.0,754.0Q-149.0,745.0 -130.0,725.0Q-95.0,690.0 -95.0,615.0L-162.0,615.0Q-163.0,662.0 -184.0,678.0Q-194.0,686.0 -208.5,689.0Q-223.0,692.0 -250.0,692.0L-285.0,692.0Q-325.0,692.0 -356.0,700.5Q-387.0,709.0 -407.0,719.0Q-432.0,733.0 -442.0,752.5Q-452.0,772.0 -452.0,790.0Q-452.0,843.0 -401.5,880.0Q-351.0,917.0 -237.0,917.0Q-50.0,917.0 57.0,845.5Q164.0,774.0 174.0,622.0L276.0,622.0L276.0,551.0Z" transform="translate(3050, 908)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(3316, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(3899, 1231)"/>
<path d="M630.0,622.0L630.0,551.0L525.0,551.0L525.0,0.0L448.0,0.0L448.0,391.0Q386.0,476.0 332.0,516.0Q278.0,556.0 222.0,556.0Q175.0,556.0 148.5,530.0Q122.0,504.0 122.0,463.0Q122.0,414.0 157.5,388.5Q193.0,363.0 275.0,355.0L269.0,272.0Q203.0,278.0 151.5,300.5Q100.0,323.0 70.0,363.5Q40.0,404.0 40.0,462.0Q40.0,516.0 64.0,553.5Q88.0,591.0 127.0,610.0Q166.0,629.0 211.0,629.0Q283.0,629.0 338.5,594.5Q394.0,560.0 452.0,494.0Q450.0,512.0 449.0,534.5Q448.0,557.0 448.0,576.0L448.0,688.0L501.0,688.0L524.0,622.0L630.0,622.0Z" transform="translate(3972, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(4592, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঙ্ক᳭ৠঌঠ</span> (Added by SIESTA)</li>


<pre>Expected: ngakabeng=0+679|uni1CED=0@-85,-363+0|rrvocalicbeng=4+835|lvocalicbeng=5+639|tthabeng=6+591</pre>



<pre>Got     : ngakabeng=0+679|uni1CED=0@-85,-363+0|rrvocalicbeng=4+853|lvocalicbeng=5+639|tthabeng=6+591</pre>



<pre>                                                                +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2762 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M522.0,49.0Q509.0,49.0 495.5,50.5Q482.0,52.0 470.0,54.0L474.0,124.0Q479.0,123.0 486.5,122.5Q494.0,122.0 503.0,122.0Q544.0,122.0 556.5,137.0Q569.0,152.0 569.0,172.0Q569.0,211.0 529.0,241.5Q489.0,272.0 412.0,285.0L412.0,-5.0L335.0,-5.0Q278.0,61.0 217.0,98.0Q156.0,135.0 73.0,146.0L37.0,234.0Q76.0,254.0 128.0,276.0Q180.0,298.0 234.0,317.5Q288.0,337.0 334.0,351.0Q327.0,383.0 300.0,404.5Q273.0,426.0 226.0,426.0Q196.0,426.0 179.0,414.0Q162.0,402.0 162.0,376.0Q162.0,369.0 163.5,360.5Q165.0,352.0 169.0,342.0L97.0,325.0Q89.0,344.0 86.0,361.5Q83.0,379.0 83.0,390.0Q83.0,426.0 105.0,451.5Q127.0,477.0 165.0,488.0Q156.0,509.0 137.0,525.0Q118.0,541.0 88.0,551.0L-10.0,551.0L-10.0,622.0L689.0,622.0L689.0,551.0L644.0,551.0L644.0,548.0Q644.0,489.0 604.0,460.0Q564.0,431.0 505.0,431.0Q442.0,431.0 396.5,462.5Q351.0,494.0 322.0,551.0L207.0,551.0Q236.0,528.0 245.0,494.0Q309.0,488.0 354.0,451.0Q399.0,414.0 409.0,357.0Q473.0,346.0 527.0,321.5Q581.0,297.0 613.5,257.5Q646.0,218.0 646.0,164.0Q646.0,116.0 615.0,82.5Q584.0,49.0 522.0,49.0ZM569.0,549.0Q569.0,552.0 569.0,551.0L409.0,551.0Q429.0,515.0 454.0,504.5Q479.0,494.0 501.0,494.0Q537.0,494.0 553.0,510.5Q569.0,527.0 569.0,549.0ZM335.0,151.0L335.0,277.0Q291.0,264.0 236.0,243.5Q181.0,223.0 137.0,203.0Q199.0,188.0 248.5,153.5Q298.0,119.0 338.0,77.0Q337.0,94.0 336.0,116.0Q335.0,138.0 335.0,151.0Z" transform="translate(0, 908)"/>
<path d="M-312.0,-106.0L-267.0,-46.0L-39.0,-211.0L-84.0,-271.0L-312.0,-106.0Z" transform="translate(594, 545)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(679, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0Z" transform="translate(1532, 908)"/>
<path d="M282.0,0.0Q192.0,0.0 128.0,47.0Q64.0,94.0 36.0,168.0L58.0,247.0Q140.0,255.0 184.0,283.0Q228.0,311.0 245.5,353.5Q263.0,396.0 263.0,448.0Q263.0,471.0 258.0,498.0Q253.0,525.0 242.0,551.0L-10.0,551.0L-10.0,622.0L200.0,622.0Q168.0,666.0 148.5,702.5Q129.0,739.0 129.0,776.0Q129.0,818.0 152.0,852.0Q175.0,886.0 218.0,917.0L269.0,861.0Q237.0,836.0 222.5,814.5Q208.0,793.0 208.0,764.0Q208.0,733.0 230.5,699.5Q253.0,666.0 291.0,622.0L601.0,622.0L601.0,551.0L427.0,551.0Q408.0,551.0 394.0,551.5Q380.0,552.0 365.0,553.0Q438.0,480.0 483.5,406.0Q529.0,332.0 529.0,240.0Q529.0,169.0 500.0,115.0Q471.0,61.0 416.0,30.5Q361.0,0.0 282.0,0.0ZM280.0,74.0Q338.0,74.0 375.0,98.0Q412.0,122.0 430.0,161.0Q448.0,200.0 448.0,244.0Q448.0,308.0 419.0,369.5Q390.0,431.0 316.0,512.0Q323.0,489.0 328.0,463.5Q333.0,438.0 333.0,406.0Q333.0,359.0 315.0,313.5Q297.0,268.0 250.0,232.0Q203.0,196.0 117.0,175.0Q141.0,123.0 186.0,98.5Q231.0,74.0 280.0,74.0Z" transform="translate(2171, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2744 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M522.0,49.0Q509.0,49.0 495.5,50.5Q482.0,52.0 470.0,54.0L474.0,124.0Q479.0,123.0 486.5,122.5Q494.0,122.0 503.0,122.0Q544.0,122.0 556.5,137.0Q569.0,152.0 569.0,172.0Q569.0,211.0 529.0,241.5Q489.0,272.0 412.0,285.0L412.0,-5.0L335.0,-5.0Q278.0,61.0 217.0,98.0Q156.0,135.0 73.0,146.0L37.0,234.0Q76.0,254.0 128.0,276.0Q180.0,298.0 234.0,317.5Q288.0,337.0 334.0,351.0Q327.0,383.0 300.0,404.5Q273.0,426.0 226.0,426.0Q196.0,426.0 179.0,414.0Q162.0,402.0 162.0,376.0Q162.0,369.0 163.5,360.5Q165.0,352.0 169.0,342.0L97.0,325.0Q89.0,344.0 86.0,361.5Q83.0,379.0 83.0,390.0Q83.0,426.0 105.0,451.5Q127.0,477.0 165.0,488.0Q156.0,509.0 137.0,525.0Q118.0,541.0 88.0,551.0L-10.0,551.0L-10.0,622.0L689.0,622.0L689.0,551.0L644.0,551.0L644.0,548.0Q644.0,489.0 604.0,460.0Q564.0,431.0 505.0,431.0Q442.0,431.0 396.5,462.5Q351.0,494.0 322.0,551.0L207.0,551.0Q236.0,528.0 245.0,494.0Q309.0,488.0 354.0,451.0Q399.0,414.0 409.0,357.0Q473.0,346.0 527.0,321.5Q581.0,297.0 613.5,257.5Q646.0,218.0 646.0,164.0Q646.0,116.0 615.0,82.5Q584.0,49.0 522.0,49.0ZM569.0,549.0Q569.0,552.0 569.0,551.0L409.0,551.0Q429.0,515.0 454.0,504.5Q479.0,494.0 501.0,494.0Q537.0,494.0 553.0,510.5Q569.0,527.0 569.0,549.0ZM335.0,151.0L335.0,277.0Q291.0,264.0 236.0,243.5Q181.0,223.0 137.0,203.0Q199.0,188.0 248.5,153.5Q298.0,119.0 338.0,77.0Q337.0,94.0 336.0,116.0Q335.0,138.0 335.0,151.0Z" transform="translate(0, 908)"/>
<path d="M-312.0,-106.0L-267.0,-46.0L-39.0,-211.0L-84.0,-271.0L-312.0,-106.0Z" transform="translate(594, 545)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(679, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0Z" transform="translate(1514, 908)"/>
<path d="M282.0,0.0Q192.0,0.0 128.0,47.0Q64.0,94.0 36.0,168.0L58.0,247.0Q140.0,255.0 184.0,283.0Q228.0,311.0 245.5,353.5Q263.0,396.0 263.0,448.0Q263.0,471.0 258.0,498.0Q253.0,525.0 242.0,551.0L-10.0,551.0L-10.0,622.0L200.0,622.0Q168.0,666.0 148.5,702.5Q129.0,739.0 129.0,776.0Q129.0,818.0 152.0,852.0Q175.0,886.0 218.0,917.0L269.0,861.0Q237.0,836.0 222.5,814.5Q208.0,793.0 208.0,764.0Q208.0,733.0 230.5,699.5Q253.0,666.0 291.0,622.0L601.0,622.0L601.0,551.0L427.0,551.0Q408.0,551.0 394.0,551.5Q380.0,552.0 365.0,553.0Q438.0,480.0 483.5,406.0Q529.0,332.0 529.0,240.0Q529.0,169.0 500.0,115.0Q471.0,61.0 416.0,30.5Q361.0,0.0 282.0,0.0ZM280.0,74.0Q338.0,74.0 375.0,98.0Q412.0,122.0 430.0,161.0Q448.0,200.0 448.0,244.0Q448.0,308.0 419.0,369.5Q390.0,431.0 316.0,512.0Q323.0,489.0 328.0,463.5Q333.0,438.0 333.0,406.0Q333.0,359.0 315.0,313.5Q297.0,268.0 250.0,232.0Q203.0,196.0 117.0,175.0Q141.0,123.0 186.0,98.5Q231.0,74.0 280.0,74.0Z" transform="translate(2153, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">িপঁআঁংণঠ॒</span> (Added by SIESTA)</li>


<pre>Expected: ivowelsignbeng=0+266|uni25CC=0+510|pabeng=1+716|candrabindubeng=1@-61,0+0|aabeng=3+1158|candrabindubeng=3@-61,0+0|anusvarabeng=3+399|nnabeng=6+620|tthabeng=7+591|uni0952=7@-41,-313+0</pre>



<pre>Got     : ivowelsignbeng=0+266|uni25CC=0+510|pabeng=1+716|candrabindubeng=1@-61,0+0|aabeng=3+1158|candrabindubeng=3@-61,0+0|anusvarabeng=3+438|nnabeng=6+620|tthabeng=7+591|uni0952=7@-41,-313+0</pre>



<pre>                                                                                                                                            ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4299 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L82.0,622.0Q66.0,641.0 49.5,662.0Q33.0,683.0 20.0,704.0Q54.0,763.0 93.0,811.5Q132.0,860.0 185.0,888.5Q238.0,917.0 313.0,917.0Q384.0,917.0 447.0,894.0Q510.0,871.0 573.0,829.5Q636.0,788.0 705.0,731.0L663.0,677.0Q594.0,733.0 538.5,770.0Q483.0,807.0 432.5,825.5Q382.0,844.0 325.0,844.0Q242.0,844.0 192.0,802.0Q142.0,760.0 106.0,693.0Q114.0,678.0 128.0,660.0Q142.0,642.0 160.0,622.0L276.0,622.0Z" transform="translate(0, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(266, 908)"/>
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(776, 908)"/>
<path d="M-90.0,830.0Q-90.0,810.0 -102.5,799.0Q-115.0,788.0 -134.0,788.0Q-156.0,788.0 -167.0,800.5Q-178.0,813.0 -178.0,833.0Q-178.0,849.0 -167.5,861.0Q-157.0,873.0 -135.0,873.0Q-90.0,873.0 -90.0,830.0ZM42.0,861.0Q35.0,785.0 -5.5,735.0Q-46.0,685.0 -131.0,685.0Q-218.0,685.0 -260.0,735.0Q-302.0,785.0 -310.0,860.0L-241.0,869.0Q-236.0,814.0 -212.0,782.5Q-188.0,751.0 -135.0,751.0Q-39.0,751.0 -28.0,870.0L42.0,861.0Z" transform="translate(1431, 908)"/>
<path d="M376.0,91.0Q308.0,91.0 246.0,123.0Q184.0,155.0 129.5,231.5Q75.0,308.0 29.0,442.0L102.0,466.0Q155.0,309.0 219.5,238.0Q284.0,167.0 378.0,167.0Q461.0,167.0 495.5,205.0Q530.0,243.0 530.0,300.0Q530.0,358.0 498.5,394.0Q467.0,430.0 420.0,430.0Q353.0,430.0 353.0,372.0Q353.0,365.0 355.0,353.0Q357.0,341.0 361.0,331.0L285.0,316.0Q278.0,337.0 274.5,354.5Q271.0,372.0 271.0,388.0Q271.0,423.0 290.0,447.5Q309.0,472.0 339.0,485.0Q330.0,507.0 311.5,524.0Q293.0,541.0 262.0,551.0L-10.0,551.0L-10.0,622.0L898.0,622.0L898.0,622.0Q925.0,622.0 949.5,606.0Q974.0,590.0 990.0,559.0Q989.0,564.0 987.5,582.0Q986.0,600.0 986.0,613.0L986.0,688.0L1039.0,688.0L1062.0,622.0L1168.0,622.0L1168.0,551.0L1063.0,551.0L1063.0,0.0L986.0,0.0L986.0,479.0Q969.0,518.0 947.5,534.5Q926.0,551.0 897.0,551.0L798.0,551.0L798.0,0.0L721.0,0.0Q693.0,56.0 653.0,98.5Q613.0,141.0 568.0,173.0Q540.0,136.0 492.0,113.5Q444.0,91.0 376.0,91.0ZM606.0,294.0Q606.0,264.0 598.0,236.0Q634.0,213.0 669.5,178.5Q705.0,144.0 724.0,109.0Q723.0,131.0 722.0,150.5Q721.0,170.0 721.0,194.0L721.0,551.0L381.0,551.0Q406.0,530.0 416.0,500.0Q474.0,499.0 516.5,472.5Q559.0,446.0 582.5,400.0Q606.0,354.0 606.0,294.0Z" transform="translate(1492, 908)"/>
<path d="M-90.0,830.0Q-90.0,810.0 -102.5,799.0Q-115.0,788.0 -134.0,788.0Q-156.0,788.0 -167.0,800.5Q-178.0,813.0 -178.0,833.0Q-178.0,849.0 -167.5,861.0Q-157.0,873.0 -135.0,873.0Q-90.0,873.0 -90.0,830.0ZM42.0,861.0Q35.0,785.0 -5.5,735.0Q-46.0,685.0 -131.0,685.0Q-218.0,685.0 -260.0,735.0Q-302.0,785.0 -310.0,860.0L-241.0,869.0Q-236.0,814.0 -212.0,782.5Q-188.0,751.0 -135.0,751.0Q-39.0,751.0 -28.0,870.0L42.0,861.0Z" transform="translate(2589, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(2650, 908)"/>
<path d="M630.0,622.0L630.0,551.0L525.0,551.0L525.0,0.0L448.0,0.0L448.0,391.0Q386.0,476.0 332.0,516.0Q278.0,556.0 222.0,556.0Q175.0,556.0 148.5,530.0Q122.0,504.0 122.0,463.0Q122.0,414.0 157.5,388.5Q193.0,363.0 275.0,355.0L269.0,272.0Q203.0,278.0 151.5,300.5Q100.0,323.0 70.0,363.5Q40.0,404.0 40.0,462.0Q40.0,516.0 64.0,553.5Q88.0,591.0 127.0,610.0Q166.0,629.0 211.0,629.0Q283.0,629.0 338.5,594.5Q394.0,560.0 452.0,494.0Q450.0,512.0 449.0,534.5Q448.0,557.0 448.0,576.0L448.0,688.0L501.0,688.0L524.0,622.0L630.0,622.0Z" transform="translate(3088, 908)"/>
<path d="M282.0,0.0Q192.0,0.0 128.0,47.0Q64.0,94.0 36.0,168.0L58.0,247.0Q140.0,255.0 184.0,283.0Q228.0,311.0 245.5,353.5Q263.0,396.0 263.0,448.0Q263.0,471.0 258.0,498.0Q253.0,525.0 242.0,551.0L-10.0,551.0L-10.0,622.0L200.0,622.0Q168.0,666.0 148.5,702.5Q129.0,739.0 129.0,776.0Q129.0,818.0 152.0,852.0Q175.0,886.0 218.0,917.0L269.0,861.0Q237.0,836.0 222.5,814.5Q208.0,793.0 208.0,764.0Q208.0,733.0 230.5,699.5Q253.0,666.0 291.0,622.0L601.0,622.0L601.0,551.0L427.0,551.0Q408.0,551.0 394.0,551.5Q380.0,552.0 365.0,553.0Q438.0,480.0 483.5,406.0Q529.0,332.0 529.0,240.0Q529.0,169.0 500.0,115.0Q471.0,61.0 416.0,30.5Q361.0,0.0 282.0,0.0ZM280.0,74.0Q338.0,74.0 375.0,98.0Q412.0,122.0 430.0,161.0Q448.0,200.0 448.0,244.0Q448.0,308.0 419.0,369.5Q390.0,431.0 316.0,512.0Q323.0,489.0 328.0,463.5Q333.0,438.0 333.0,406.0Q333.0,359.0 315.0,313.5Q297.0,268.0 250.0,232.0Q203.0,196.0 117.0,175.0Q141.0,123.0 186.0,98.5Q231.0,74.0 280.0,74.0Z" transform="translate(3708, 908)"/>
<path d="M-443.0,-187.0L-443.0,-116.0L-67.0,-116.0L-67.0,-187.0L-443.0,-187.0Z" transform="translate(4258, 595)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4260 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L82.0,622.0Q66.0,641.0 49.5,662.0Q33.0,683.0 20.0,704.0Q54.0,763.0 93.0,811.5Q132.0,860.0 185.0,888.5Q238.0,917.0 313.0,917.0Q384.0,917.0 447.0,894.0Q510.0,871.0 573.0,829.5Q636.0,788.0 705.0,731.0L663.0,677.0Q594.0,733.0 538.5,770.0Q483.0,807.0 432.5,825.5Q382.0,844.0 325.0,844.0Q242.0,844.0 192.0,802.0Q142.0,760.0 106.0,693.0Q114.0,678.0 128.0,660.0Q142.0,642.0 160.0,622.0L276.0,622.0Z" transform="translate(0, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(266, 908)"/>
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(776, 908)"/>
<path d="M-90.0,830.0Q-90.0,810.0 -102.5,799.0Q-115.0,788.0 -134.0,788.0Q-156.0,788.0 -167.0,800.5Q-178.0,813.0 -178.0,833.0Q-178.0,849.0 -167.5,861.0Q-157.0,873.0 -135.0,873.0Q-90.0,873.0 -90.0,830.0ZM42.0,861.0Q35.0,785.0 -5.5,735.0Q-46.0,685.0 -131.0,685.0Q-218.0,685.0 -260.0,735.0Q-302.0,785.0 -310.0,860.0L-241.0,869.0Q-236.0,814.0 -212.0,782.5Q-188.0,751.0 -135.0,751.0Q-39.0,751.0 -28.0,870.0L42.0,861.0Z" transform="translate(1431, 908)"/>
<path d="M376.0,91.0Q308.0,91.0 246.0,123.0Q184.0,155.0 129.5,231.5Q75.0,308.0 29.0,442.0L102.0,466.0Q155.0,309.0 219.5,238.0Q284.0,167.0 378.0,167.0Q461.0,167.0 495.5,205.0Q530.0,243.0 530.0,300.0Q530.0,358.0 498.5,394.0Q467.0,430.0 420.0,430.0Q353.0,430.0 353.0,372.0Q353.0,365.0 355.0,353.0Q357.0,341.0 361.0,331.0L285.0,316.0Q278.0,337.0 274.5,354.5Q271.0,372.0 271.0,388.0Q271.0,423.0 290.0,447.5Q309.0,472.0 339.0,485.0Q330.0,507.0 311.5,524.0Q293.0,541.0 262.0,551.0L-10.0,551.0L-10.0,622.0L898.0,622.0L898.0,622.0Q925.0,622.0 949.5,606.0Q974.0,590.0 990.0,559.0Q989.0,564.0 987.5,582.0Q986.0,600.0 986.0,613.0L986.0,688.0L1039.0,688.0L1062.0,622.0L1168.0,622.0L1168.0,551.0L1063.0,551.0L1063.0,0.0L986.0,0.0L986.0,479.0Q969.0,518.0 947.5,534.5Q926.0,551.0 897.0,551.0L798.0,551.0L798.0,0.0L721.0,0.0Q693.0,56.0 653.0,98.5Q613.0,141.0 568.0,173.0Q540.0,136.0 492.0,113.5Q444.0,91.0 376.0,91.0ZM606.0,294.0Q606.0,264.0 598.0,236.0Q634.0,213.0 669.5,178.5Q705.0,144.0 724.0,109.0Q723.0,131.0 722.0,150.5Q721.0,170.0 721.0,194.0L721.0,551.0L381.0,551.0Q406.0,530.0 416.0,500.0Q474.0,499.0 516.5,472.5Q559.0,446.0 582.5,400.0Q606.0,354.0 606.0,294.0Z" transform="translate(1492, 908)"/>
<path d="M-90.0,830.0Q-90.0,810.0 -102.5,799.0Q-115.0,788.0 -134.0,788.0Q-156.0,788.0 -167.0,800.5Q-178.0,813.0 -178.0,833.0Q-178.0,849.0 -167.5,861.0Q-157.0,873.0 -135.0,873.0Q-90.0,873.0 -90.0,830.0ZM42.0,861.0Q35.0,785.0 -5.5,735.0Q-46.0,685.0 -131.0,685.0Q-218.0,685.0 -260.0,735.0Q-302.0,785.0 -310.0,860.0L-241.0,869.0Q-236.0,814.0 -212.0,782.5Q-188.0,751.0 -135.0,751.0Q-39.0,751.0 -28.0,870.0L42.0,861.0Z" transform="translate(2589, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(2650, 908)"/>
<path d="M630.0,622.0L630.0,551.0L525.0,551.0L525.0,0.0L448.0,0.0L448.0,391.0Q386.0,476.0 332.0,516.0Q278.0,556.0 222.0,556.0Q175.0,556.0 148.5,530.0Q122.0,504.0 122.0,463.0Q122.0,414.0 157.5,388.5Q193.0,363.0 275.0,355.0L269.0,272.0Q203.0,278.0 151.5,300.5Q100.0,323.0 70.0,363.5Q40.0,404.0 40.0,462.0Q40.0,516.0 64.0,553.5Q88.0,591.0 127.0,610.0Q166.0,629.0 211.0,629.0Q283.0,629.0 338.5,594.5Q394.0,560.0 452.0,494.0Q450.0,512.0 449.0,534.5Q448.0,557.0 448.0,576.0L448.0,688.0L501.0,688.0L524.0,622.0L630.0,622.0Z" transform="translate(3049, 908)"/>
<path d="M282.0,0.0Q192.0,0.0 128.0,47.0Q64.0,94.0 36.0,168.0L58.0,247.0Q140.0,255.0 184.0,283.0Q228.0,311.0 245.5,353.5Q263.0,396.0 263.0,448.0Q263.0,471.0 258.0,498.0Q253.0,525.0 242.0,551.0L-10.0,551.0L-10.0,622.0L200.0,622.0Q168.0,666.0 148.5,702.5Q129.0,739.0 129.0,776.0Q129.0,818.0 152.0,852.0Q175.0,886.0 218.0,917.0L269.0,861.0Q237.0,836.0 222.5,814.5Q208.0,793.0 208.0,764.0Q208.0,733.0 230.5,699.5Q253.0,666.0 291.0,622.0L601.0,622.0L601.0,551.0L427.0,551.0Q408.0,551.0 394.0,551.5Q380.0,552.0 365.0,553.0Q438.0,480.0 483.5,406.0Q529.0,332.0 529.0,240.0Q529.0,169.0 500.0,115.0Q471.0,61.0 416.0,30.5Q361.0,0.0 282.0,0.0ZM280.0,74.0Q338.0,74.0 375.0,98.0Q412.0,122.0 430.0,161.0Q448.0,200.0 448.0,244.0Q448.0,308.0 419.0,369.5Q390.0,431.0 316.0,512.0Q323.0,489.0 328.0,463.5Q333.0,438.0 333.0,406.0Q333.0,359.0 315.0,313.5Q297.0,268.0 250.0,232.0Q203.0,196.0 117.0,175.0Q141.0,123.0 186.0,98.5Q231.0,74.0 280.0,74.0Z" transform="translate(3669, 908)"/>
<path d="M-443.0,-187.0L-443.0,-116.0L-67.0,-116.0L-67.0,-187.0L-443.0,-187.0Z" transform="translate(4219, 595)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">᳕৾৩᳐ৃড়্ছ৾</span> (Added by SIESTA)</li>


<pre>Expected: uni25CC=0+510|uni1CD5=0+0|uni25CC=0+510|uni09FE=0+0|threebeng=2+592|uni1CD0=2@-41,323+0|uni25CC=2+510|rvocalicvowelsignbeng=2+0|ddanuktahalfbeng=5+615|chabeng=7+687|uni09FE=7@0,323+0</pre>



<pre>Got     : uni25CC=0+510|uni1CD5=0@-21,-313+0|uni25CC=0+510|uni09FE=0+0|threebeng=2+592|uni1CD0=2@-41,323+0|uni25CC=2+510|rvocalicvowelsignbeng=2@19,3+0|ddanuktahalfbeng=5+615|chabeng=7+687|uni09FE=7@0,323+0</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3424 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(0, 908)"/>
<path d="M-221.0,-107.0Q-219.0,-159.0 -206.5,-181.5Q-194.0,-204.0 -167.0,-204.0Q-142.0,-204.0 -128.0,-184.5Q-114.0,-165.0 -113.0,-105.0L-38.0,-109.0Q-42.0,-201.0 -74.5,-236.0Q-107.0,-271.0 -160.0,-271.0Q-225.0,-271.0 -255.0,-211.0Q-285.0,-271.0 -350.0,-271.0Q-404.0,-271.0 -436.0,-236.0Q-468.0,-201.0 -472.0,-109.0L-398.0,-105.0Q-396.0,-165.0 -382.0,-184.5Q-368.0,-204.0 -343.0,-204.0Q-316.0,-204.0 -303.0,-181.5Q-290.0,-159.0 -289.0,-107.0L-221.0,-107.0Z" transform="translate(489, 595)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(510, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(1020, 908)"/>
<path d="M553.0,295.0Q553.0,223.0 532.5,165.0Q512.0,107.0 466.5,73.0Q421.0,39.0 347.0,39.0Q293.0,39.0 246.0,57.5Q199.0,76.0 159.5,124.5Q120.0,173.0 87.0,261.5Q54.0,350.0 29.0,490.0L105.0,510.0Q135.0,360.0 168.0,274.0Q201.0,188.0 243.5,151.5Q286.0,115.0 342.0,115.0Q393.0,115.0 422.0,139.0Q451.0,163.0 463.0,203.5Q475.0,244.0 475.0,295.0Q475.0,356.0 458.0,404.0Q441.0,452.0 412.0,480.0Q383.0,508.0 347.0,508.0Q292.0,508.0 292.0,458.0Q292.0,442.0 296.5,426.0Q301.0,410.0 311.0,390.0L231.0,369.0Q219.0,394.0 213.0,419.5Q207.0,445.0 207.0,467.0Q207.0,509.0 227.5,533.5Q248.0,558.0 278.5,568.5Q309.0,579.0 337.0,579.0Q407.0,579.0 455.0,540.5Q503.0,502.0 528.0,437.5Q553.0,373.0 553.0,295.0Z" transform="translate(1020, 908)"/>
<path d="M-430.0,661.0L-289.0,910.0L-228.0,910.0L-77.0,663.0L-131.0,636.0L-255.0,849.0L-371.0,636.0L-430.0,661.0Z" transform="translate(1571, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1612, 908)"/>
<path d="M-355.0,-80.0Q-296.0,-51.0 -233.0,-24.5Q-170.0,2.0 -105.0,25.0L-79.0,-41.0Q-126.0,-56.0 -173.5,-72.0Q-221.0,-88.0 -259.0,-105.0Q-157.0,-118.0 -87.5,-149.0Q-18.0,-180.0 35.0,-214.0L-1.0,-271.0Q-79.0,-221.0 -154.0,-195.5Q-229.0,-170.0 -321.0,-160.0L-355.0,-80.0Z" transform="translate(2141, 911)"/>
<path d="M625.0,622.0L625.0,551.0L320.0,551.0L320.0,425.0Q320.0,405.0 327.0,394.0Q334.0,383.0 351.0,383.0Q375.0,383.0 402.0,403.5Q429.0,424.0 467.0,478.0L524.0,487.0Q554.0,446.0 569.5,405.0Q585.0,364.0 585.0,320.0Q585.0,241.0 528.5,189.0Q472.0,137.0 367.0,137.0Q292.0,137.0 229.0,169.0Q166.0,201.0 116.0,275.0Q66.0,349.0 29.0,475.0L103.0,495.0Q145.0,341.0 208.5,276.0Q272.0,211.0 364.0,211.0Q434.0,211.0 471.5,240.5Q509.0,270.0 509.0,322.0Q509.0,364.0 491.0,398.0Q456.0,353.0 421.0,332.5Q386.0,312.0 347.0,312.0Q304.0,312.0 278.0,333.0Q264.0,345.0 253.5,367.5Q243.0,390.0 243.0,439.0L243.0,551.0L-10.0,551.0L-10.0,622.0L625.0,622.0ZM326.0,-42.0Q301.0,-42.0 283.5,-26.0Q266.0,-10.0 266.0,16.0Q266.0,42.0 283.5,59.0Q301.0,76.0 326.0,76.0Q351.0,76.0 368.5,59.0Q386.0,42.0 386.0,16.0Q386.0,-10.0 368.5,-26.0Q351.0,-42.0 326.0,-42.0Z" transform="translate(2122, 908)"/>
<path d="M227.0,217.0Q157.0,217.0 125.0,249.0Q110.0,264.0 100.5,288.0Q91.0,312.0 91.0,359.0L91.0,551.0L-10.0,551.0L-10.0,622.0L697.0,622.0L697.0,551.0L168.0,551.0L168.0,544.0Q185.0,525.0 204.0,510.5Q223.0,496.0 251.0,488.5Q279.0,481.0 323.0,481.0L372.0,481.0Q382.0,482.0 397.5,482.5Q413.0,483.0 423.0,483.0Q481.0,483.0 518.5,465.5Q556.0,448.0 577.0,421.0Q598.0,394.0 606.5,364.0Q615.0,334.0 615.0,310.0Q615.0,249.0 589.5,207.5Q564.0,166.0 522.5,141.5Q481.0,117.0 434.0,106.0Q495.0,92.0 555.5,69.5Q616.0,47.0 684.0,11.0L649.0,-49.0Q532.0,14.0 406.5,47.5Q281.0,81.0 143.0,94.0L152.0,166.0Q181.0,160.0 213.5,156.0Q246.0,152.0 290.0,152.0Q379.0,152.0 433.5,175.0Q488.0,198.0 513.0,234.5Q538.0,271.0 538.0,310.0Q538.0,355.0 513.5,382.0Q489.0,409.0 445.0,416.0Q450.0,403.0 450.0,388.0Q450.0,339.0 420.5,300.5Q391.0,262.0 340.5,239.5Q290.0,217.0 227.0,217.0ZM184.0,301.0Q199.0,286.0 233.0,286.0Q276.0,286.0 307.5,302.0Q339.0,318.0 356.5,340.5Q374.0,363.0 374.0,384.0Q374.0,403.0 360.0,408.0Q346.0,413.0 322.0,413.0L316.0,413.0Q269.0,413.0 231.0,428.0Q193.0,443.0 166.0,468.0Q167.0,458.0 167.5,446.0Q168.0,434.0 168.0,420.0L168.0,359.0Q168.0,333.0 172.5,321.0Q177.0,309.0 184.0,301.0Z" transform="translate(2737, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(3424, 1231)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3424 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(0, 908)"/>
<path d="M-221.0,-107.0Q-219.0,-159.0 -206.5,-181.5Q-194.0,-204.0 -167.0,-204.0Q-142.0,-204.0 -128.0,-184.5Q-114.0,-165.0 -113.0,-105.0L-38.0,-109.0Q-42.0,-201.0 -74.5,-236.0Q-107.0,-271.0 -160.0,-271.0Q-225.0,-271.0 -255.0,-211.0Q-285.0,-271.0 -350.0,-271.0Q-404.0,-271.0 -436.0,-236.0Q-468.0,-201.0 -472.0,-109.0L-398.0,-105.0Q-396.0,-165.0 -382.0,-184.5Q-368.0,-204.0 -343.0,-204.0Q-316.0,-204.0 -303.0,-181.5Q-290.0,-159.0 -289.0,-107.0L-221.0,-107.0Z" transform="translate(510, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(510, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(1020, 908)"/>
<path d="M553.0,295.0Q553.0,223.0 532.5,165.0Q512.0,107.0 466.5,73.0Q421.0,39.0 347.0,39.0Q293.0,39.0 246.0,57.5Q199.0,76.0 159.5,124.5Q120.0,173.0 87.0,261.5Q54.0,350.0 29.0,490.0L105.0,510.0Q135.0,360.0 168.0,274.0Q201.0,188.0 243.5,151.5Q286.0,115.0 342.0,115.0Q393.0,115.0 422.0,139.0Q451.0,163.0 463.0,203.5Q475.0,244.0 475.0,295.0Q475.0,356.0 458.0,404.0Q441.0,452.0 412.0,480.0Q383.0,508.0 347.0,508.0Q292.0,508.0 292.0,458.0Q292.0,442.0 296.5,426.0Q301.0,410.0 311.0,390.0L231.0,369.0Q219.0,394.0 213.0,419.5Q207.0,445.0 207.0,467.0Q207.0,509.0 227.5,533.5Q248.0,558.0 278.5,568.5Q309.0,579.0 337.0,579.0Q407.0,579.0 455.0,540.5Q503.0,502.0 528.0,437.5Q553.0,373.0 553.0,295.0Z" transform="translate(1020, 908)"/>
<path d="M-430.0,661.0L-289.0,910.0L-228.0,910.0L-77.0,663.0L-131.0,636.0L-255.0,849.0L-371.0,636.0L-430.0,661.0Z" transform="translate(1571, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1612, 908)"/>
<path d="M-355.0,-80.0Q-296.0,-51.0 -233.0,-24.5Q-170.0,2.0 -105.0,25.0L-79.0,-41.0Q-126.0,-56.0 -173.5,-72.0Q-221.0,-88.0 -259.0,-105.0Q-157.0,-118.0 -87.5,-149.0Q-18.0,-180.0 35.0,-214.0L-1.0,-271.0Q-79.0,-221.0 -154.0,-195.5Q-229.0,-170.0 -321.0,-160.0L-355.0,-80.0Z" transform="translate(2122, 908)"/>
<path d="M625.0,622.0L625.0,551.0L320.0,551.0L320.0,425.0Q320.0,405.0 327.0,394.0Q334.0,383.0 351.0,383.0Q375.0,383.0 402.0,403.5Q429.0,424.0 467.0,478.0L524.0,487.0Q554.0,446.0 569.5,405.0Q585.0,364.0 585.0,320.0Q585.0,241.0 528.5,189.0Q472.0,137.0 367.0,137.0Q292.0,137.0 229.0,169.0Q166.0,201.0 116.0,275.0Q66.0,349.0 29.0,475.0L103.0,495.0Q145.0,341.0 208.5,276.0Q272.0,211.0 364.0,211.0Q434.0,211.0 471.5,240.5Q509.0,270.0 509.0,322.0Q509.0,364.0 491.0,398.0Q456.0,353.0 421.0,332.5Q386.0,312.0 347.0,312.0Q304.0,312.0 278.0,333.0Q264.0,345.0 253.5,367.5Q243.0,390.0 243.0,439.0L243.0,551.0L-10.0,551.0L-10.0,622.0L625.0,622.0ZM326.0,-42.0Q301.0,-42.0 283.5,-26.0Q266.0,-10.0 266.0,16.0Q266.0,42.0 283.5,59.0Q301.0,76.0 326.0,76.0Q351.0,76.0 368.5,59.0Q386.0,42.0 386.0,16.0Q386.0,-10.0 368.5,-26.0Q351.0,-42.0 326.0,-42.0Z" transform="translate(2122, 908)"/>
<path d="M227.0,217.0Q157.0,217.0 125.0,249.0Q110.0,264.0 100.5,288.0Q91.0,312.0 91.0,359.0L91.0,551.0L-10.0,551.0L-10.0,622.0L697.0,622.0L697.0,551.0L168.0,551.0L168.0,544.0Q185.0,525.0 204.0,510.5Q223.0,496.0 251.0,488.5Q279.0,481.0 323.0,481.0L372.0,481.0Q382.0,482.0 397.5,482.5Q413.0,483.0 423.0,483.0Q481.0,483.0 518.5,465.5Q556.0,448.0 577.0,421.0Q598.0,394.0 606.5,364.0Q615.0,334.0 615.0,310.0Q615.0,249.0 589.5,207.5Q564.0,166.0 522.5,141.5Q481.0,117.0 434.0,106.0Q495.0,92.0 555.5,69.5Q616.0,47.0 684.0,11.0L649.0,-49.0Q532.0,14.0 406.5,47.5Q281.0,81.0 143.0,94.0L152.0,166.0Q181.0,160.0 213.5,156.0Q246.0,152.0 290.0,152.0Q379.0,152.0 433.5,175.0Q488.0,198.0 513.0,234.5Q538.0,271.0 538.0,310.0Q538.0,355.0 513.5,382.0Q489.0,409.0 445.0,416.0Q450.0,403.0 450.0,388.0Q450.0,339.0 420.5,300.5Q391.0,262.0 340.5,239.5Q290.0,217.0 227.0,217.0ZM184.0,301.0Q199.0,286.0 233.0,286.0Q276.0,286.0 307.5,302.0Q339.0,318.0 356.5,340.5Q374.0,363.0 374.0,384.0Q374.0,403.0 360.0,408.0Q346.0,413.0 322.0,413.0L316.0,413.0Q269.0,413.0 231.0,428.0Q193.0,443.0 166.0,468.0Q167.0,458.0 167.5,446.0Q168.0,434.0 168.0,420.0L168.0,359.0Q168.0,333.0 172.5,321.0Q177.0,309.0 184.0,301.0Z" transform="translate(2737, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(3424, 1231)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">০৾ৰ্এ॑গ᳭ঞ্ছ</span> (Added by SIESTA)</li>


<pre>Expected: zerobeng=0+592|uni09FE=0@0,323+0|ebeng=2+740|rephbeng=2@-93,0+0|uni0951=2@-106,323+0|gabeng=6+656|uni1CED=6@-73,-363+0|nyachabeng=8+744</pre>



<pre>Got     : zerobeng=0+592|uni09FE=0@0,323+0|ebeng=2+758|rephbeng=2@-111,0+0|uni0951=2@-124,323+0|gabeng=6+656|uni1CED=6@-73,-363+0|nyachabeng=8+744</pre>



<pre>                                                    ^^             ^^                 ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2750 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M290.0,91.0Q227.0,91.0 177.5,115.0Q128.0,139.0 100.0,188.5Q72.0,238.0 72.0,313.0Q72.0,372.0 96.0,424.5Q120.0,477.0 170.5,510.5Q221.0,544.0 300.0,544.0Q381.0,544.0 429.0,513.0Q477.0,482.0 498.5,431.5Q520.0,381.0 520.0,320.0Q520.0,261.0 495.5,208.5Q471.0,156.0 420.5,123.5Q370.0,91.0 290.0,91.0ZM301.0,473.0Q237.0,473.0 195.0,430.5Q153.0,388.0 153.0,311.0Q153.0,270.0 166.5,236.0Q180.0,202.0 210.5,182.0Q241.0,162.0 291.0,162.0Q359.0,162.0 399.0,206.5Q439.0,251.0 439.0,324.0Q439.0,393.0 404.5,433.0Q370.0,473.0 301.0,473.0Z" transform="translate(0, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(592, 1231)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(592, 908)"/>
<path d="M-254.0,707.0L72.0,917.0L110.0,860.0L-209.0,644.0L-254.0,707.0Z" transform="translate(1239, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(1226, 1231)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(1350, 908)"/>
<path d="M-312.0,-106.0L-267.0,-46.0L-39.0,-211.0L-84.0,-271.0L-312.0,-106.0Z" transform="translate(1933, 545)"/>
<path d="M490.0,145.0Q490.0,105.0 467.0,74.0Q444.0,43.0 395.0,27.0Q452.0,15.0 512.0,-6.5Q572.0,-28.0 626.0,-56.0L593.0,-115.0Q527.0,-80.0 444.5,-54.0Q362.0,-28.0 276.5,-11.5Q191.0,5.0 115.0,11.0L123.0,83.0Q155.0,76.0 187.0,72.5Q219.0,69.0 259.0,69.0Q416.0,69.0 416.0,148.0Q416.0,166.0 407.5,180.5Q399.0,195.0 385.0,207.0Q359.0,174.0 320.5,153.0Q282.0,132.0 234.0,132.0Q168.0,132.0 131.0,165.5Q94.0,199.0 94.0,248.0Q94.0,299.0 133.5,335.0Q173.0,371.0 246.0,408.0Q297.0,434.0 317.0,456.0Q337.0,478.0 337.0,506.0Q337.0,524.0 321.0,539.5Q305.0,555.0 261.0,555.0Q223.0,555.0 192.5,541.5Q162.0,528.0 144.5,509.0Q127.0,490.0 127.0,474.0Q127.0,460.0 136.0,449.0Q145.0,438.0 160.0,430.0L107.0,370.0Q72.0,390.0 58.5,417.0Q45.0,444.0 45.0,467.0Q45.0,502.0 73.0,539.0Q101.0,576.0 151.0,601.0Q201.0,626.0 268.0,626.0Q317.0,626.0 352.5,606.0Q388.0,586.0 400.0,549.0Q437.0,587.0 476.5,607.0Q516.0,627.0 562.0,627.0Q621.0,627.0 654.0,598.0Q687.0,569.0 687.0,523.0Q687.0,504.0 678.5,484.0Q670.0,464.0 650.0,445.0Q668.0,431.0 680.5,410.5Q693.0,390.0 693.0,363.0Q693.0,318.0 660.0,283.5Q627.0,249.0 559.0,249.0Q508.0,249.0 469.5,269.5Q431.0,290.0 402.5,324.5Q374.0,359.0 354.0,401.0Q344.0,391.0 333.0,383.0Q331.0,374.0 331.0,365.0Q331.0,343.0 351.5,323.0Q372.0,303.0 399.0,281.0Q421.0,264.0 441.5,243.5Q462.0,223.0 476.0,199.0Q490.0,175.0 490.0,145.0ZM558.0,559.0Q516.0,559.0 475.5,529.5Q435.0,500.0 405.0,454.0Q427.0,384.0 465.0,351.0Q503.0,318.0 555.0,318.0Q578.0,318.0 597.5,329.0Q617.0,340.0 617.0,370.0Q617.0,394.0 595.0,412.0Q572.0,403.0 544.0,396.0L528.0,460.0Q566.0,469.0 588.5,482.5Q611.0,496.0 611.0,521.0Q611.0,540.0 597.0,549.5Q583.0,559.0 558.0,559.0ZM171.0,253.0Q171.0,228.0 189.0,213.5Q207.0,199.0 236.0,199.0Q266.0,199.0 291.0,210.0Q316.0,221.0 336.0,247.0Q303.0,272.0 285.0,293.5Q267.0,315.0 267.0,344.0L267.0,345.0Q216.0,320.0 193.5,299.5Q171.0,279.0 171.0,253.0Z" transform="translate(2006, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2732 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M290.0,91.0Q227.0,91.0 177.5,115.0Q128.0,139.0 100.0,188.5Q72.0,238.0 72.0,313.0Q72.0,372.0 96.0,424.5Q120.0,477.0 170.5,510.5Q221.0,544.0 300.0,544.0Q381.0,544.0 429.0,513.0Q477.0,482.0 498.5,431.5Q520.0,381.0 520.0,320.0Q520.0,261.0 495.5,208.5Q471.0,156.0 420.5,123.5Q370.0,91.0 290.0,91.0ZM301.0,473.0Q237.0,473.0 195.0,430.5Q153.0,388.0 153.0,311.0Q153.0,270.0 166.5,236.0Q180.0,202.0 210.5,182.0Q241.0,162.0 291.0,162.0Q359.0,162.0 399.0,206.5Q439.0,251.0 439.0,324.0Q439.0,393.0 404.5,433.0Q370.0,473.0 301.0,473.0Z" transform="translate(0, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(592, 1231)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(592, 908)"/>
<path d="M-254.0,707.0L72.0,917.0L110.0,860.0L-209.0,644.0L-254.0,707.0Z" transform="translate(1239, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(1226, 1231)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(1332, 908)"/>
<path d="M-312.0,-106.0L-267.0,-46.0L-39.0,-211.0L-84.0,-271.0L-312.0,-106.0Z" transform="translate(1915, 545)"/>
<path d="M490.0,145.0Q490.0,105.0 467.0,74.0Q444.0,43.0 395.0,27.0Q452.0,15.0 512.0,-6.5Q572.0,-28.0 626.0,-56.0L593.0,-115.0Q527.0,-80.0 444.5,-54.0Q362.0,-28.0 276.5,-11.5Q191.0,5.0 115.0,11.0L123.0,83.0Q155.0,76.0 187.0,72.5Q219.0,69.0 259.0,69.0Q416.0,69.0 416.0,148.0Q416.0,166.0 407.5,180.5Q399.0,195.0 385.0,207.0Q359.0,174.0 320.5,153.0Q282.0,132.0 234.0,132.0Q168.0,132.0 131.0,165.5Q94.0,199.0 94.0,248.0Q94.0,299.0 133.5,335.0Q173.0,371.0 246.0,408.0Q297.0,434.0 317.0,456.0Q337.0,478.0 337.0,506.0Q337.0,524.0 321.0,539.5Q305.0,555.0 261.0,555.0Q223.0,555.0 192.5,541.5Q162.0,528.0 144.5,509.0Q127.0,490.0 127.0,474.0Q127.0,460.0 136.0,449.0Q145.0,438.0 160.0,430.0L107.0,370.0Q72.0,390.0 58.5,417.0Q45.0,444.0 45.0,467.0Q45.0,502.0 73.0,539.0Q101.0,576.0 151.0,601.0Q201.0,626.0 268.0,626.0Q317.0,626.0 352.5,606.0Q388.0,586.0 400.0,549.0Q437.0,587.0 476.5,607.0Q516.0,627.0 562.0,627.0Q621.0,627.0 654.0,598.0Q687.0,569.0 687.0,523.0Q687.0,504.0 678.5,484.0Q670.0,464.0 650.0,445.0Q668.0,431.0 680.5,410.5Q693.0,390.0 693.0,363.0Q693.0,318.0 660.0,283.5Q627.0,249.0 559.0,249.0Q508.0,249.0 469.5,269.5Q431.0,290.0 402.5,324.5Q374.0,359.0 354.0,401.0Q344.0,391.0 333.0,383.0Q331.0,374.0 331.0,365.0Q331.0,343.0 351.5,323.0Q372.0,303.0 399.0,281.0Q421.0,264.0 441.5,243.5Q462.0,223.0 476.0,199.0Q490.0,175.0 490.0,145.0ZM558.0,559.0Q516.0,559.0 475.5,529.5Q435.0,500.0 405.0,454.0Q427.0,384.0 465.0,351.0Q503.0,318.0 555.0,318.0Q578.0,318.0 597.5,329.0Q617.0,340.0 617.0,370.0Q617.0,394.0 595.0,412.0Q572.0,403.0 544.0,396.0L528.0,460.0Q566.0,469.0 588.5,482.5Q611.0,496.0 611.0,521.0Q611.0,540.0 597.0,549.5Q583.0,559.0 558.0,559.0ZM171.0,253.0Q171.0,228.0 189.0,213.5Q207.0,199.0 236.0,199.0Q266.0,199.0 291.0,210.0Q316.0,221.0 336.0,247.0Q303.0,272.0 285.0,293.5Q267.0,315.0 267.0,344.0L267.0,345.0Q216.0,320.0 193.5,299.5Q171.0,279.0 171.0,253.0Z" transform="translate(1988, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">য়৾তৢংশঃ᳭×</span> (Added by SIESTA)</li>


<pre>Expected: yyabeng=0+626|uni09FE=0@0,323+0|tabeng=2+707|lvocalicvowelsignbeng=2@-108,0+0|anusvarabeng=2+426|shabeng=5+677|visargabeng=5+438|uni1CED=5@-386,-363+0|multiply.beng=8+592</pre>



<pre>Got     : yyabeng=0+626|uni09FE=0@0,323+0|tabeng=2+707|lvocalicvowelsignbeng=2@-108,0+0|anusvarabeng=2+438|shabeng=5+677|visargabeng=5+438|uni1CED=5@-386,-363+0|multiply.beng=8+592</pre>



<pre>                                                                                                        ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3478 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M636.0,622.0L636.0,551.0L531.0,551.0L531.0,0.0L454.0,0.0Q412.0,56.0 361.0,98.5Q310.0,141.0 243.0,170.0Q176.0,199.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L636.0,622.0ZM454.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.0,327.5Q183.0,301.0 141.0,275.0Q250.0,255.0 324.0,209.0Q398.0,163.0 456.0,99.0Q454.0,134.0 454.0,171.0L454.0,551.0ZM180.0,-6.0Q155.0,-6.0 137.5,10.0Q120.0,26.0 120.0,52.0Q120.0,78.0 137.5,95.0Q155.0,112.0 180.0,112.0Q205.0,112.0 222.5,95.0Q240.0,78.0 240.0,52.0Q240.0,26.0 222.5,10.0Q205.0,-6.0 180.0,-6.0Z" transform="translate(0, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(626, 1231)"/>
<path d="M717.0,622.0L717.0,551.0L-10.0,551.0L-10.0,622.0L717.0,622.0ZM407.0,50.0Q325.0,50.0 254.0,90.5Q183.0,131.0 126.5,222.0Q70.0,313.0 29.0,466.0L105.0,486.0Q140.0,362.0 181.5,282.0Q223.0,202.0 277.5,164.0Q332.0,126.0 405.0,126.0Q467.0,126.0 504.0,146.5Q541.0,167.0 557.0,201.5Q573.0,236.0 573.0,278.0Q573.0,320.0 557.0,354.5Q541.0,389.0 512.0,409.0Q483.0,429.0 444.0,429.0Q404.0,429.0 386.5,412.0Q369.0,395.0 369.0,367.0Q369.0,357.0 371.0,346.0Q373.0,335.0 378.0,321.0L301.0,306.0Q295.0,325.0 291.5,343.0Q288.0,361.0 288.0,380.0Q288.0,438.0 330.5,469.0Q373.0,500.0 440.0,500.0Q502.0,500.0 549.0,471.5Q596.0,443.0 623.0,392.0Q650.0,341.0 650.0,274.0Q650.0,211.0 623.5,160.5Q597.0,110.0 543.0,80.0Q489.0,50.0 407.0,50.0Z" transform="translate(626, 908)"/>
<path d="M-254.0,-127.0Q-200.0,-127.0 -173.0,-150.0Q-146.0,-173.0 -146.0,-208.0Q-146.0,-220.0 -150.5,-233.0Q-155.0,-246.0 -168.0,-258.0Q-108.0,-250.0 -84.0,-232.5Q-60.0,-215.0 -60.0,-187.0Q-60.0,-170.0 -68.5,-157.0Q-77.0,-144.0 -101.5,-131.0Q-126.0,-118.0 -174.0,-104.0Q-225.0,-88.0 -252.0,-71.5Q-279.0,-55.0 -279.0,-22.0Q-279.0,-5.0 -269.0,13.0L-213.0,0.0Q-217.0,-8.0 -217.0,-16.0Q-217.0,-26.0 -202.5,-33.0Q-188.0,-40.0 -139.0,-55.0Q-79.0,-73.0 -47.0,-92.5Q-15.0,-112.0 -3.5,-135.0Q8.0,-158.0 8.0,-185.0Q8.0,-232.0 -24.0,-260.5Q-56.0,-289.0 -107.5,-301.0Q-159.0,-313.0 -220.0,-313.0L-244.0,-313.0L-256.0,-264.0Q-229.0,-256.0 -217.0,-243.5Q-205.0,-231.0 -205.0,-214.0Q-205.0,-199.0 -216.0,-189.5Q-227.0,-180.0 -252.0,-180.0Q-292.0,-180.0 -292.0,-204.0Q-292.0,-213.0 -285.0,-227.0L-345.0,-238.0Q-356.0,-218.0 -356.0,-195.0Q-356.0,-166.0 -330.5,-146.5Q-305.0,-127.0 -254.0,-127.0Z" transform="translate(1225, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(1333, 908)"/>
<path d="M77.0,629.0Q123.0,629.0 164.5,608.0Q206.0,587.0 226.0,541.0Q244.0,586.0 281.0,607.5Q318.0,629.0 361.0,629.0Q406.0,629.0 443.5,609.0Q481.0,589.0 507.0,554.0Q506.0,566.0 505.5,579.0Q505.0,592.0 505.0,607.0L505.0,688.0L558.0,688.0L582.0,622.0L687.0,622.0L687.0,551.0L582.0,551.0L582.0,0.0L505.0,0.0L505.0,454.0Q476.0,503.0 440.5,529.5Q405.0,556.0 363.0,556.0Q324.0,556.0 300.0,534.5Q276.0,513.0 276.0,471.0Q276.0,431.0 308.5,405.5Q341.0,380.0 413.0,377.0L406.0,300.0Q335.0,304.0 291.5,330.0Q248.0,356.0 230.0,398.0Q212.0,356.0 169.0,328.0Q126.0,300.0 54.0,300.0L48.0,377.0Q99.0,378.0 128.0,391.5Q157.0,405.0 169.0,426.0Q181.0,447.0 181.0,468.0Q181.0,509.0 155.0,532.5Q129.0,556.0 76.0,556.0Q43.0,556.0 -1.0,545.0L-9.0,620.0Q16.0,625.0 35.0,627.0Q54.0,629.0 77.0,629.0Z" transform="translate(1771, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,518.0 271.0,537.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM78.0,137.0Q78.0,199.0 118.5,236.0Q159.0,273.0 219.0,273.0Q279.0,273.0 319.5,236.0Q360.0,199.0 360.0,137.0Q360.0,75.0 319.5,37.5Q279.0,0.0 219.0,0.0Q159.0,0.0 118.5,37.5Q78.0,75.0 78.0,137.0ZM147.0,137.0Q147.0,104.0 167.5,84.5Q188.0,65.0 219.0,65.0Q251.0,65.0 271.0,84.5Q291.0,104.0 291.0,137.0Q291.0,170.0 271.0,189.0Q251.0,208.0 219.0,208.0Q188.0,208.0 167.5,188.5Q147.0,169.0 147.0,137.0Z" transform="translate(2448, 908)"/>
<path d="M-312.0,-106.0L-267.0,-46.0L-39.0,-211.0L-84.0,-271.0L-312.0,-106.0Z" transform="translate(2500, 545)"/>
<path d="M295.0,270.0L140.0,116.0L90.0,167.0L244.0,321.0L89.0,477.0L140.0,528.0L295.0,373.0L452.0,528.0L503.0,478.0L346.0,321.0L502.0,165.0L452.0,115.0L295.0,270.0Z" transform="translate(2886, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3466 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M636.0,622.0L636.0,551.0L531.0,551.0L531.0,0.0L454.0,0.0Q412.0,56.0 361.0,98.5Q310.0,141.0 243.0,170.0Q176.0,199.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L636.0,622.0ZM454.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.0,327.5Q183.0,301.0 141.0,275.0Q250.0,255.0 324.0,209.0Q398.0,163.0 456.0,99.0Q454.0,134.0 454.0,171.0L454.0,551.0ZM180.0,-6.0Q155.0,-6.0 137.5,10.0Q120.0,26.0 120.0,52.0Q120.0,78.0 137.5,95.0Q155.0,112.0 180.0,112.0Q205.0,112.0 222.5,95.0Q240.0,78.0 240.0,52.0Q240.0,26.0 222.5,10.0Q205.0,-6.0 180.0,-6.0Z" transform="translate(0, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(626, 1231)"/>
<path d="M717.0,622.0L717.0,551.0L-10.0,551.0L-10.0,622.0L717.0,622.0ZM407.0,50.0Q325.0,50.0 254.0,90.5Q183.0,131.0 126.5,222.0Q70.0,313.0 29.0,466.0L105.0,486.0Q140.0,362.0 181.5,282.0Q223.0,202.0 277.5,164.0Q332.0,126.0 405.0,126.0Q467.0,126.0 504.0,146.5Q541.0,167.0 557.0,201.5Q573.0,236.0 573.0,278.0Q573.0,320.0 557.0,354.5Q541.0,389.0 512.0,409.0Q483.0,429.0 444.0,429.0Q404.0,429.0 386.5,412.0Q369.0,395.0 369.0,367.0Q369.0,357.0 371.0,346.0Q373.0,335.0 378.0,321.0L301.0,306.0Q295.0,325.0 291.5,343.0Q288.0,361.0 288.0,380.0Q288.0,438.0 330.5,469.0Q373.0,500.0 440.0,500.0Q502.0,500.0 549.0,471.5Q596.0,443.0 623.0,392.0Q650.0,341.0 650.0,274.0Q650.0,211.0 623.5,160.5Q597.0,110.0 543.0,80.0Q489.0,50.0 407.0,50.0Z" transform="translate(626, 908)"/>
<path d="M-254.0,-127.0Q-200.0,-127.0 -173.0,-150.0Q-146.0,-173.0 -146.0,-208.0Q-146.0,-220.0 -150.5,-233.0Q-155.0,-246.0 -168.0,-258.0Q-108.0,-250.0 -84.0,-232.5Q-60.0,-215.0 -60.0,-187.0Q-60.0,-170.0 -68.5,-157.0Q-77.0,-144.0 -101.5,-131.0Q-126.0,-118.0 -174.0,-104.0Q-225.0,-88.0 -252.0,-71.5Q-279.0,-55.0 -279.0,-22.0Q-279.0,-5.0 -269.0,13.0L-213.0,0.0Q-217.0,-8.0 -217.0,-16.0Q-217.0,-26.0 -202.5,-33.0Q-188.0,-40.0 -139.0,-55.0Q-79.0,-73.0 -47.0,-92.5Q-15.0,-112.0 -3.5,-135.0Q8.0,-158.0 8.0,-185.0Q8.0,-232.0 -24.0,-260.5Q-56.0,-289.0 -107.5,-301.0Q-159.0,-313.0 -220.0,-313.0L-244.0,-313.0L-256.0,-264.0Q-229.0,-256.0 -217.0,-243.5Q-205.0,-231.0 -205.0,-214.0Q-205.0,-199.0 -216.0,-189.5Q-227.0,-180.0 -252.0,-180.0Q-292.0,-180.0 -292.0,-204.0Q-292.0,-213.0 -285.0,-227.0L-345.0,-238.0Q-356.0,-218.0 -356.0,-195.0Q-356.0,-166.0 -330.5,-146.5Q-305.0,-127.0 -254.0,-127.0Z" transform="translate(1225, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(1333, 908)"/>
<path d="M77.0,629.0Q123.0,629.0 164.5,608.0Q206.0,587.0 226.0,541.0Q244.0,586.0 281.0,607.5Q318.0,629.0 361.0,629.0Q406.0,629.0 443.5,609.0Q481.0,589.0 507.0,554.0Q506.0,566.0 505.5,579.0Q505.0,592.0 505.0,607.0L505.0,688.0L558.0,688.0L582.0,622.0L687.0,622.0L687.0,551.0L582.0,551.0L582.0,0.0L505.0,0.0L505.0,454.0Q476.0,503.0 440.5,529.5Q405.0,556.0 363.0,556.0Q324.0,556.0 300.0,534.5Q276.0,513.0 276.0,471.0Q276.0,431.0 308.5,405.5Q341.0,380.0 413.0,377.0L406.0,300.0Q335.0,304.0 291.5,330.0Q248.0,356.0 230.0,398.0Q212.0,356.0 169.0,328.0Q126.0,300.0 54.0,300.0L48.0,377.0Q99.0,378.0 128.0,391.5Q157.0,405.0 169.0,426.0Q181.0,447.0 181.0,468.0Q181.0,509.0 155.0,532.5Q129.0,556.0 76.0,556.0Q43.0,556.0 -1.0,545.0L-9.0,620.0Q16.0,625.0 35.0,627.0Q54.0,629.0 77.0,629.0Z" transform="translate(1759, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,518.0 271.0,537.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM78.0,137.0Q78.0,199.0 118.5,236.0Q159.0,273.0 219.0,273.0Q279.0,273.0 319.5,236.0Q360.0,199.0 360.0,137.0Q360.0,75.0 319.5,37.5Q279.0,0.0 219.0,0.0Q159.0,0.0 118.5,37.5Q78.0,75.0 78.0,137.0ZM147.0,137.0Q147.0,104.0 167.5,84.5Q188.0,65.0 219.0,65.0Q251.0,65.0 271.0,84.5Q291.0,104.0 291.0,137.0Q291.0,170.0 271.0,189.0Q251.0,208.0 219.0,208.0Q188.0,208.0 167.5,188.5Q147.0,169.0 147.0,137.0Z" transform="translate(2436, 908)"/>
<path d="M-312.0,-106.0L-267.0,-46.0L-39.0,-211.0L-84.0,-271.0L-312.0,-106.0Z" transform="translate(2488, 545)"/>
<path d="M295.0,270.0L140.0,116.0L90.0,167.0L244.0,321.0L89.0,477.0L140.0,528.0L295.0,373.0L452.0,528.0L503.0,478.0L346.0,321.0L502.0,165.0L452.0,115.0L295.0,270.0Z" transform="translate(2874, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">এ꣱ংখ০॒থ᳖ৈ</span> (Added by SIESTA)</li>


<pre>Expected: ebeng=0+758|uniA8F1=0@0,323+0|uni25CC=0+510|anusvarabeng=0+389|khabeng=3+696|zerobeng=4+592|uni0952=4@-41,-313+0|thabeng=6+645|uni1CD6=6@-68,-319+0|aivowelsignbeng=6+346|uni25CC=6+510</pre>



<pre>Got     : ebeng=0+758|uniA8F1=0@0,323+0|uni25CC=0+510|anusvarabeng=0+438|khabeng=3+696|zerobeng=4+592|uni0952=4@-41,-313+0|thabeng=6+645|uni1CD6=6@-68,-319+0|aivowelsignbeng=6+346|uni25CC=6+510</pre>



<pre>                                                                       +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4495 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(0, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(758, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(758, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(1268, 908)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0Z" transform="translate(1706, 908)"/>
<path d="M290.0,91.0Q227.0,91.0 177.5,115.0Q128.0,139.0 100.0,188.5Q72.0,238.0 72.0,313.0Q72.0,372.0 96.0,424.5Q120.0,477.0 170.5,510.5Q221.0,544.0 300.0,544.0Q381.0,544.0 429.0,513.0Q477.0,482.0 498.5,431.5Q520.0,381.0 520.0,320.0Q520.0,261.0 495.5,208.5Q471.0,156.0 420.5,123.5Q370.0,91.0 290.0,91.0ZM301.0,473.0Q237.0,473.0 195.0,430.5Q153.0,388.0 153.0,311.0Q153.0,270.0 166.5,236.0Q180.0,202.0 210.5,182.0Q241.0,162.0 291.0,162.0Q359.0,162.0 399.0,206.5Q439.0,251.0 439.0,324.0Q439.0,393.0 404.5,433.0Q370.0,473.0 301.0,473.0Z" transform="translate(2402, 908)"/>
<path d="M-443.0,-187.0L-443.0,-116.0L-67.0,-116.0L-67.0,-187.0L-443.0,-187.0Z" transform="translate(2953, 595)"/>
<path d="M211.0,625.0Q306.0,625.0 353.0,578.5Q400.0,532.0 400.0,464.0Q400.0,394.0 348.0,347.0Q296.0,300.0 203.0,282.0Q303.0,253.0 370.5,202.0Q438.0,151.0 475.0,97.0Q474.0,120.0 473.5,143.0Q473.0,166.0 473.0,193.0L473.0,688.0L526.0,688.0L549.0,622.0L655.0,622.0L655.0,551.0L550.0,551.0L550.0,0.0L473.0,0.0Q435.0,55.0 383.0,103.5Q331.0,152.0 264.5,187.5Q198.0,223.0 115.0,238.0L92.0,331.0Q176.0,337.0 226.0,355.5Q276.0,374.0 297.5,402.5Q319.0,431.0 319.0,466.0Q319.0,509.0 291.0,532.0Q263.0,555.0 209.0,555.0Q159.0,555.0 137.5,535.5Q116.0,516.0 116.0,494.0Q116.0,480.0 123.5,468.0Q131.0,456.0 150.0,446.0L106.0,384.0Q78.0,403.0 58.0,430.0Q38.0,457.0 38.0,497.0Q38.0,550.0 83.0,587.5Q128.0,625.0 211.0,625.0Z" transform="translate(2994, 908)"/>
<path d="M-426.0,-94.0L-348.0,-94.0L-348.0,-202.0L-78.0,-202.0L-78.0,-271.0L-426.0,-271.0L-426.0,-94.0Z" transform="translate(3571, 589)"/>
<path d="M283.0,622.0Q282.0,661.0 264.5,680.0Q247.0,699.0 203.0,699.0L183.0,699.0Q118.0,699.0 82.5,708.0Q47.0,717.0 22.0,736.0Q-32.0,777.0 -32.0,859.0Q-32.0,872.0 -30.5,884.5Q-29.0,897.0 -27.0,912.0L47.0,907.0Q43.0,887.0 43.0,869.0Q43.0,847.0 47.5,830.0Q52.0,813.0 62.0,802.0Q76.0,786.0 102.0,778.5Q128.0,771.0 178.0,771.0L182.0,771.0Q235.0,771.0 266.0,763.0Q297.0,755.0 319.0,734.0Q352.0,702.0 355.0,622.0L356.0,622.0L356.0,551.0L336.0,551.0Q305.0,544.0 269.0,520.5Q233.0,497.0 201.0,459.5Q169.0,422.0 148.5,372.0Q128.0,322.0 128.0,262.0Q128.0,190.0 149.5,147.5Q171.0,105.0 203.0,87.0Q235.0,69.0 267.0,69.0Q292.0,69.0 309.0,74.0Q326.0,79.0 348.0,92.0L383.0,31.0Q357.0,11.0 326.0,3.0Q295.0,-5.0 264.0,-5.0Q201.0,-5.0 152.5,28.0Q104.0,61.0 76.5,120.5Q49.0,180.0 49.0,260.0Q49.0,359.0 93.5,435.0Q138.0,511.0 208.0,554.0Q191.0,552.0 172.0,551.5Q153.0,551.0 130.0,551.0L-10.0,551.0L-10.0,622.0L283.0,622.0Z" transform="translate(3639, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(3985, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4446 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(0, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(758, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(758, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(1268, 908)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0Z" transform="translate(1657, 908)"/>
<path d="M290.0,91.0Q227.0,91.0 177.5,115.0Q128.0,139.0 100.0,188.5Q72.0,238.0 72.0,313.0Q72.0,372.0 96.0,424.5Q120.0,477.0 170.5,510.5Q221.0,544.0 300.0,544.0Q381.0,544.0 429.0,513.0Q477.0,482.0 498.5,431.5Q520.0,381.0 520.0,320.0Q520.0,261.0 495.5,208.5Q471.0,156.0 420.5,123.5Q370.0,91.0 290.0,91.0ZM301.0,473.0Q237.0,473.0 195.0,430.5Q153.0,388.0 153.0,311.0Q153.0,270.0 166.5,236.0Q180.0,202.0 210.5,182.0Q241.0,162.0 291.0,162.0Q359.0,162.0 399.0,206.5Q439.0,251.0 439.0,324.0Q439.0,393.0 404.5,433.0Q370.0,473.0 301.0,473.0Z" transform="translate(2353, 908)"/>
<path d="M-443.0,-187.0L-443.0,-116.0L-67.0,-116.0L-67.0,-187.0L-443.0,-187.0Z" transform="translate(2904, 595)"/>
<path d="M211.0,625.0Q306.0,625.0 353.0,578.5Q400.0,532.0 400.0,464.0Q400.0,394.0 348.0,347.0Q296.0,300.0 203.0,282.0Q303.0,253.0 370.5,202.0Q438.0,151.0 475.0,97.0Q474.0,120.0 473.5,143.0Q473.0,166.0 473.0,193.0L473.0,688.0L526.0,688.0L549.0,622.0L655.0,622.0L655.0,551.0L550.0,551.0L550.0,0.0L473.0,0.0Q435.0,55.0 383.0,103.5Q331.0,152.0 264.5,187.5Q198.0,223.0 115.0,238.0L92.0,331.0Q176.0,337.0 226.0,355.5Q276.0,374.0 297.5,402.5Q319.0,431.0 319.0,466.0Q319.0,509.0 291.0,532.0Q263.0,555.0 209.0,555.0Q159.0,555.0 137.5,535.5Q116.0,516.0 116.0,494.0Q116.0,480.0 123.5,468.0Q131.0,456.0 150.0,446.0L106.0,384.0Q78.0,403.0 58.0,430.0Q38.0,457.0 38.0,497.0Q38.0,550.0 83.0,587.5Q128.0,625.0 211.0,625.0Z" transform="translate(2945, 908)"/>
<path d="M-426.0,-94.0L-348.0,-94.0L-348.0,-202.0L-78.0,-202.0L-78.0,-271.0L-426.0,-271.0L-426.0,-94.0Z" transform="translate(3522, 589)"/>
<path d="M283.0,622.0Q282.0,661.0 264.5,680.0Q247.0,699.0 203.0,699.0L183.0,699.0Q118.0,699.0 82.5,708.0Q47.0,717.0 22.0,736.0Q-32.0,777.0 -32.0,859.0Q-32.0,872.0 -30.5,884.5Q-29.0,897.0 -27.0,912.0L47.0,907.0Q43.0,887.0 43.0,869.0Q43.0,847.0 47.5,830.0Q52.0,813.0 62.0,802.0Q76.0,786.0 102.0,778.5Q128.0,771.0 178.0,771.0L182.0,771.0Q235.0,771.0 266.0,763.0Q297.0,755.0 319.0,734.0Q352.0,702.0 355.0,622.0L356.0,622.0L356.0,551.0L336.0,551.0Q305.0,544.0 269.0,520.5Q233.0,497.0 201.0,459.5Q169.0,422.0 148.5,372.0Q128.0,322.0 128.0,262.0Q128.0,190.0 149.5,147.5Q171.0,105.0 203.0,87.0Q235.0,69.0 267.0,69.0Q292.0,69.0 309.0,74.0Q326.0,79.0 348.0,92.0L383.0,31.0Q357.0,11.0 326.0,3.0Q295.0,-5.0 264.0,-5.0Q201.0,-5.0 152.5,28.0Q104.0,61.0 76.5,120.5Q49.0,180.0 49.0,260.0Q49.0,359.0 93.5,435.0Q138.0,511.0 208.0,554.0Q191.0,552.0 172.0,551.5Q153.0,551.0 130.0,551.0L-10.0,551.0L-10.0,622.0L283.0,622.0Z" transform="translate(3590, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(3936, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">েঊ꣱ড্ঞ᳒প᳒</span> (Added by SIESTA)</li>


<pre>Expected: evowelsigninibeng=0+346|uni25CC=0+510|uubeng=1+853|uniA8F1=1@0,323+0|ddahalfbeng=3+615|nyabeng=5+1001|uni1CD2=5@-237,323+0|pabeng=7+716|uni1CD2=7@-103,323+0</pre>



<pre>Got     : evowelsigninibeng=0+346|uni25CC=0+510|uubeng=1+853|uniA8F1=1@0,323+0|ddahalfbeng=3+615|nyabeng=5+1019|uni1CD2=5@-255,323+0|pabeng=7+716|uni1CD2=7@-103,323+0</pre>



<pre>                                                                                                             +              ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4059 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M356.0,622.0L356.0,551.0L336.0,551.0Q305.0,544.0 269.0,520.5Q233.0,497.0 201.0,459.5Q169.0,422.0 148.5,372.0Q128.0,322.0 128.0,262.0Q128.0,190.0 149.5,147.5Q171.0,105.0 203.0,87.0Q235.0,69.0 267.0,69.0Q292.0,69.0 309.0,74.0Q326.0,79.0 348.0,92.0L383.0,31.0Q357.0,11.0 326.0,3.0Q295.0,-5.0 263.0,-5.0Q200.0,-5.0 152.0,28.0Q104.0,61.0 76.5,120.5Q49.0,180.0 49.0,260.0Q49.0,337.0 73.5,397.5Q98.0,458.0 137.5,503.0Q177.0,548.0 223.0,577.5Q269.0,607.0 312.0,622.0L356.0,622.0Z" transform="translate(0, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(346, 908)"/>
<path d="M649.0,622.0Q648.0,663.0 629.5,681.0Q611.0,699.0 569.0,699.0L384.0,699.0Q318.0,699.0 282.5,708.0Q247.0,717.0 222.0,736.0Q168.0,777.0 168.0,859.0Q168.0,872.0 169.5,885.0Q171.0,898.0 173.0,912.0L247.0,907.0Q245.0,896.0 244.0,886.5Q243.0,877.0 243.0,869.0Q243.0,847.0 247.5,830.0Q252.0,813.0 262.0,802.0Q276.0,786.0 302.5,778.5Q329.0,771.0 378.0,771.0L548.0,771.0Q601.0,771.0 632.0,763.0Q663.0,755.0 685.0,734.0Q718.0,702.0 721.0,622.0L863.0,622.0L863.0,551.0L496.0,551.0L496.0,372.0Q496.0,316.0 533.0,316.0Q562.0,316.0 594.0,343.5Q626.0,371.0 669.0,433.0L729.0,442.0Q761.0,395.0 778.5,345.0Q796.0,295.0 796.0,245.0Q796.0,184.0 770.0,134.0Q744.0,84.0 689.0,54.0Q634.0,24.0 548.0,24.0Q439.0,24.0 343.5,61.0Q248.0,98.0 169.0,188.0Q90.0,278.0 29.0,435.0L104.0,458.0Q130.0,385.0 163.5,321.0Q197.0,257.0 246.5,203.0Q296.0,149.0 369.0,106.0L372.0,109.0Q331.0,147.0 298.0,200.5Q265.0,254.0 240.5,316.5Q216.0,379.0 199.0,440.0L274.0,461.0Q308.0,335.0 345.0,255.5Q382.0,176.0 432.5,138.0Q483.0,100.0 555.0,100.0Q612.0,100.0 648.5,120.0Q685.0,140.0 702.5,172.5Q720.0,205.0 720.0,244.0Q720.0,279.0 712.0,305.5Q704.0,332.0 693.0,349.0Q661.0,305.0 620.0,273.5Q579.0,242.0 534.0,242.0Q486.0,242.0 457.0,268.0Q441.0,282.0 430.0,307.5Q419.0,333.0 419.0,393.0L419.0,551.0L-10.0,551.0L-10.0,622.0L649.0,622.0Z" transform="translate(856, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(1709, 1231)"/>
<path d="M625.0,622.0L625.0,551.0L320.0,551.0L320.0,425.0Q320.0,405.0 327.0,394.0Q334.0,383.0 351.0,383.0Q375.0,383.0 402.0,403.5Q429.0,424.0 467.0,478.0L524.0,487.0Q554.0,446.0 569.5,405.0Q585.0,364.0 585.0,320.0Q585.0,241.0 528.5,189.0Q472.0,137.0 367.0,137.0Q292.0,137.0 229.0,169.0Q166.0,201.0 116.0,275.0Q66.0,349.0 29.0,475.0L103.0,495.0Q145.0,341.0 208.5,276.0Q272.0,211.0 364.0,211.0Q434.0,211.0 471.5,240.5Q509.0,270.0 509.0,322.0Q509.0,364.0 491.0,398.0Q456.0,353.0 421.0,332.5Q386.0,312.0 347.0,312.0Q304.0,312.0 278.0,333.0Q264.0,345.0 253.5,367.5Q243.0,390.0 243.0,439.0L243.0,551.0L-10.0,551.0L-10.0,622.0L625.0,622.0Z" transform="translate(1709, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(2324, 908)"/>
<path d="M-418.0,789.0L-90.0,789.0L-90.0,722.0L-418.0,722.0L-418.0,789.0Z" transform="translate(3088, 1231)"/>
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(3343, 908)"/>
<path d="M-418.0,789.0L-90.0,789.0L-90.0,722.0L-418.0,722.0L-418.0,789.0Z" transform="translate(3956, 1231)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4041 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M356.0,622.0L356.0,551.0L336.0,551.0Q305.0,544.0 269.0,520.5Q233.0,497.0 201.0,459.5Q169.0,422.0 148.5,372.0Q128.0,322.0 128.0,262.0Q128.0,190.0 149.5,147.5Q171.0,105.0 203.0,87.0Q235.0,69.0 267.0,69.0Q292.0,69.0 309.0,74.0Q326.0,79.0 348.0,92.0L383.0,31.0Q357.0,11.0 326.0,3.0Q295.0,-5.0 263.0,-5.0Q200.0,-5.0 152.0,28.0Q104.0,61.0 76.5,120.5Q49.0,180.0 49.0,260.0Q49.0,337.0 73.5,397.5Q98.0,458.0 137.5,503.0Q177.0,548.0 223.0,577.5Q269.0,607.0 312.0,622.0L356.0,622.0Z" transform="translate(0, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(346, 908)"/>
<path d="M649.0,622.0Q648.0,663.0 629.5,681.0Q611.0,699.0 569.0,699.0L384.0,699.0Q318.0,699.0 282.5,708.0Q247.0,717.0 222.0,736.0Q168.0,777.0 168.0,859.0Q168.0,872.0 169.5,885.0Q171.0,898.0 173.0,912.0L247.0,907.0Q245.0,896.0 244.0,886.5Q243.0,877.0 243.0,869.0Q243.0,847.0 247.5,830.0Q252.0,813.0 262.0,802.0Q276.0,786.0 302.5,778.5Q329.0,771.0 378.0,771.0L548.0,771.0Q601.0,771.0 632.0,763.0Q663.0,755.0 685.0,734.0Q718.0,702.0 721.0,622.0L863.0,622.0L863.0,551.0L496.0,551.0L496.0,372.0Q496.0,316.0 533.0,316.0Q562.0,316.0 594.0,343.5Q626.0,371.0 669.0,433.0L729.0,442.0Q761.0,395.0 778.5,345.0Q796.0,295.0 796.0,245.0Q796.0,184.0 770.0,134.0Q744.0,84.0 689.0,54.0Q634.0,24.0 548.0,24.0Q439.0,24.0 343.5,61.0Q248.0,98.0 169.0,188.0Q90.0,278.0 29.0,435.0L104.0,458.0Q130.0,385.0 163.5,321.0Q197.0,257.0 246.5,203.0Q296.0,149.0 369.0,106.0L372.0,109.0Q331.0,147.0 298.0,200.5Q265.0,254.0 240.5,316.5Q216.0,379.0 199.0,440.0L274.0,461.0Q308.0,335.0 345.0,255.5Q382.0,176.0 432.5,138.0Q483.0,100.0 555.0,100.0Q612.0,100.0 648.5,120.0Q685.0,140.0 702.5,172.5Q720.0,205.0 720.0,244.0Q720.0,279.0 712.0,305.5Q704.0,332.0 693.0,349.0Q661.0,305.0 620.0,273.5Q579.0,242.0 534.0,242.0Q486.0,242.0 457.0,268.0Q441.0,282.0 430.0,307.5Q419.0,333.0 419.0,393.0L419.0,551.0L-10.0,551.0L-10.0,622.0L649.0,622.0Z" transform="translate(856, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(1709, 1231)"/>
<path d="M625.0,622.0L625.0,551.0L320.0,551.0L320.0,425.0Q320.0,405.0 327.0,394.0Q334.0,383.0 351.0,383.0Q375.0,383.0 402.0,403.5Q429.0,424.0 467.0,478.0L524.0,487.0Q554.0,446.0 569.5,405.0Q585.0,364.0 585.0,320.0Q585.0,241.0 528.5,189.0Q472.0,137.0 367.0,137.0Q292.0,137.0 229.0,169.0Q166.0,201.0 116.0,275.0Q66.0,349.0 29.0,475.0L103.0,495.0Q145.0,341.0 208.5,276.0Q272.0,211.0 364.0,211.0Q434.0,211.0 471.5,240.5Q509.0,270.0 509.0,322.0Q509.0,364.0 491.0,398.0Q456.0,353.0 421.0,332.5Q386.0,312.0 347.0,312.0Q304.0,312.0 278.0,333.0Q264.0,345.0 253.5,367.5Q243.0,390.0 243.0,439.0L243.0,551.0L-10.0,551.0L-10.0,622.0L625.0,622.0Z" transform="translate(1709, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(2324, 908)"/>
<path d="M-418.0,789.0L-90.0,789.0L-90.0,722.0L-418.0,722.0L-418.0,789.0Z" transform="translate(3088, 1231)"/>
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(3325, 908)"/>
<path d="M-418.0,789.0L-90.0,789.0L-90.0,722.0L-418.0,722.0L-418.0,789.0Z" transform="translate(3938, 1231)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঘ॑ঞ্চওএৱ্ৡৠ</span> (Added by SIESTA)</li>


<pre>Expected: ghabeng=0+631|uni0951=0@-61,323+0|nyacabeng=2+829|obeng=5+720|ebeng=6+758|wabeng=7+596|viramabeng=7+0|llvocalicbeng=9+621|rrvocalicbeng=10+853</pre>



<pre>Got     : ghabeng=0+631|uni0951=0@-61,323+0|nyacabeng=2+847|obeng=5+738|ebeng=6+758|wabeng=7+596|viramabeng=7+0|llvocalicbeng=9+639|rrvocalicbeng=10+853</pre>



<pre>                                                         ^^          ^^                                                          ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5062 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M641.0,622.0L641.0,551.0L536.0,551.0L536.0,0.0L459.0,0.0Q428.0,43.0 377.0,82.0Q326.0,121.0 260.0,147.5Q194.0,174.0 118.0,179.0L83.0,266.0Q111.0,288.0 139.0,307.0Q167.0,326.0 198.0,345.0Q129.0,352.0 92.5,384.0Q56.0,416.0 56.0,469.0Q56.0,514.0 88.0,551.0L-10.0,551.0L-10.0,622.0L641.0,622.0ZM374.0,381.0Q325.0,352.0 270.5,315.0Q216.0,278.0 173.0,246.0Q275.0,227.0 342.0,187.0Q409.0,147.0 461.0,92.0Q460.0,109.0 459.5,127.5Q459.0,146.0 459.0,165.0L459.0,551.0L184.0,551.0Q160.0,533.0 148.5,513.0Q137.0,493.0 137.0,472.0Q137.0,435.0 163.0,419.5Q189.0,404.0 224.0,404.0Q246.0,404.0 272.5,411.5Q299.0,419.0 331.0,441.0L374.0,381.0Z" transform="translate(0, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(570, 1231)"/>
<path d="M184.0,628.0Q248.0,628.0 308.0,594.5Q368.0,561.0 420.0,493.0Q419.0,510.0 418.5,529.0Q418.0,548.0 418.0,566.0L418.0,688.0L471.0,688.0L495.0,622.0L495.0,580.0Q495.0,567.0 494.5,554.0Q494.0,541.0 493.0,528.0Q526.0,566.0 564.5,586.5Q603.0,607.0 652.0,607.0Q714.0,607.0 750.5,575.0Q787.0,543.0 787.0,493.0Q787.0,470.0 778.0,442.5Q769.0,415.0 741.0,392.0Q762.0,376.0 777.5,351.5Q793.0,327.0 793.0,291.0Q793.0,242.0 757.0,204.5Q721.0,167.0 651.0,167.0Q593.0,167.0 555.5,191.5Q518.0,216.0 493.0,253.0Q494.0,238.0 494.5,221.5Q495.0,205.0 495.0,190.0L495.0,0.0L418.0,0.0Q390.0,53.0 341.5,100.0Q293.0,147.0 230.5,179.5Q168.0,212.0 96.0,223.0L57.0,318.0Q137.0,364.0 212.0,399.0Q287.0,434.0 357.0,457.0Q314.0,510.0 273.0,532.5Q232.0,555.0 191.0,555.0Q157.0,555.0 143.0,541.5Q129.0,528.0 129.0,510.0Q129.0,494.0 138.0,482.0Q147.0,470.0 163.0,460.0L113.0,400.0Q81.0,423.0 64.0,450.0Q47.0,477.0 47.0,514.0Q47.0,567.0 86.0,597.5Q125.0,628.0 184.0,628.0ZM647.0,538.0Q603.0,538.0 565.0,506.5Q527.0,475.0 495.0,423.0L495.0,383.0Q517.0,311.0 556.5,273.5Q596.0,236.0 648.0,236.0Q675.0,236.0 696.0,250.5Q717.0,265.0 717.0,294.0Q717.0,334.0 679.0,358.0Q657.0,350.0 630.0,344.0L613.0,412.0Q666.0,420.0 688.5,440.0Q711.0,460.0 711.0,485.0Q711.0,512.0 692.0,525.0Q673.0,538.0 647.0,538.0ZM150.0,284.0Q196.0,274.0 248.5,249.5Q301.0,225.0 347.0,189.0Q393.0,153.0 421.0,109.0Q420.0,126.0 419.0,144.5Q418.0,163.0 418.0,187.0L418.0,403.0Q353.0,381.0 282.5,350.0Q212.0,319.0 150.0,284.0Z" transform="translate(631, 908)"/>
<path d="M681.0,225.0Q681.0,142.0 619.5,92.0Q558.0,42.0 453.0,42.0Q359.0,42.0 279.0,87.5Q199.0,133.0 136.0,235.5Q73.0,338.0 28.0,507.0L103.0,529.0Q143.0,386.0 192.5,295.0Q242.0,204.0 306.5,161.0Q371.0,118.0 455.0,118.0Q518.0,118.0 559.0,144.5Q600.0,171.0 600.0,228.0Q600.0,255.0 587.0,276.5Q574.0,298.0 552.0,314.0Q520.0,297.0 480.0,282.0L449.0,354.0Q516.0,376.0 553.5,405.5Q591.0,435.0 591.0,482.0Q591.0,558.0 509.0,558.0Q461.0,558.0 420.5,537.5Q380.0,517.0 355.5,489.5Q331.0,462.0 331.0,439.0Q331.0,423.0 341.0,411.5Q351.0,400.0 386.0,395.0L365.0,321.0Q308.0,332.0 279.5,360.0Q251.0,388.0 251.0,431.0Q251.0,465.0 271.5,499.5Q292.0,534.0 328.0,563.5Q364.0,593.0 410.5,611.0Q457.0,629.0 509.0,629.0Q586.0,629.0 628.5,590.0Q671.0,551.0 671.0,483.0Q671.0,445.0 655.5,414.0Q640.0,383.0 613.0,358.0Q681.0,308.0 681.0,225.0Z" transform="translate(1478, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(2216, 908)"/>
<path d="M606.0,622.0L606.0,551.0L501.0,551.0L501.0,0.0L424.0,0.0Q394.0,60.0 341.5,110.5Q289.0,161.0 221.0,196.0Q153.0,231.0 76.0,243.0L37.0,339.0Q128.0,394.0 224.5,439.0Q321.0,484.0 424.0,517.0L424.0,551.0L-10.0,551.0L-10.0,622.0L606.0,622.0ZM130.0,304.0Q181.0,293.0 238.0,266.5Q295.0,240.0 345.5,200.0Q396.0,160.0 427.0,108.0Q426.0,126.0 425.0,145.0Q424.0,164.0 424.0,189.0L424.0,439.0Q352.0,414.0 274.0,379.5Q196.0,345.0 130.0,304.0ZM86.0,186.0Q173.0,170.0 235.0,127.5Q297.0,85.0 332.0,41.0L286.0,0.0Q244.0,44.0 191.0,72.5Q138.0,101.0 70.0,114.0L86.0,186.0Z" transform="translate(2974, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(3570, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0ZM243.0,-107.0Q297.0,-107.0 324.0,-130.0Q351.0,-153.0 351.0,-188.0Q351.0,-200.0 346.5,-213.0Q342.0,-226.0 329.0,-238.0Q389.0,-230.0 413.0,-212.5Q437.0,-195.0 437.0,-167.0Q437.0,-150.0 428.5,-137.0Q420.0,-124.0 395.5,-111.0Q371.0,-98.0 323.0,-84.0Q272.0,-68.0 245.0,-51.5Q218.0,-35.0 218.0,-2.0Q218.0,15.0 228.0,33.0L284.0,20.0Q280.0,12.0 280.0,4.0Q280.0,-6.0 294.5,-13.0Q309.0,-20.0 358.0,-35.0Q418.0,-53.0 450.0,-72.5Q482.0,-92.0 493.5,-115.0Q505.0,-138.0 505.0,-165.0Q505.0,-212.0 473.0,-240.5Q441.0,-269.0 389.5,-281.0Q338.0,-293.0 277.0,-293.0L253.0,-293.0L241.0,-244.0Q268.0,-236.0 280.0,-223.5Q292.0,-211.0 292.0,-194.0Q292.0,-179.0 281.0,-169.5Q270.0,-160.0 245.0,-160.0Q205.0,-160.0 205.0,-184.0Q205.0,-193.0 212.0,-207.0L152.0,-218.0Q141.0,-198.0 141.0,-175.0Q141.0,-146.0 166.5,-126.5Q192.0,-107.0 243.0,-107.0Z" transform="translate(3570, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(4209, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5008 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M641.0,622.0L641.0,551.0L536.0,551.0L536.0,0.0L459.0,0.0Q428.0,43.0 377.0,82.0Q326.0,121.0 260.0,147.5Q194.0,174.0 118.0,179.0L83.0,266.0Q111.0,288.0 139.0,307.0Q167.0,326.0 198.0,345.0Q129.0,352.0 92.5,384.0Q56.0,416.0 56.0,469.0Q56.0,514.0 88.0,551.0L-10.0,551.0L-10.0,622.0L641.0,622.0ZM374.0,381.0Q325.0,352.0 270.5,315.0Q216.0,278.0 173.0,246.0Q275.0,227.0 342.0,187.0Q409.0,147.0 461.0,92.0Q460.0,109.0 459.5,127.5Q459.0,146.0 459.0,165.0L459.0,551.0L184.0,551.0Q160.0,533.0 148.5,513.0Q137.0,493.0 137.0,472.0Q137.0,435.0 163.0,419.5Q189.0,404.0 224.0,404.0Q246.0,404.0 272.5,411.5Q299.0,419.0 331.0,441.0L374.0,381.0Z" transform="translate(0, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(570, 1231)"/>
<path d="M184.0,628.0Q248.0,628.0 308.0,594.5Q368.0,561.0 420.0,493.0Q419.0,510.0 418.5,529.0Q418.0,548.0 418.0,566.0L418.0,688.0L471.0,688.0L495.0,622.0L495.0,580.0Q495.0,567.0 494.5,554.0Q494.0,541.0 493.0,528.0Q526.0,566.0 564.5,586.5Q603.0,607.0 652.0,607.0Q714.0,607.0 750.5,575.0Q787.0,543.0 787.0,493.0Q787.0,470.0 778.0,442.5Q769.0,415.0 741.0,392.0Q762.0,376.0 777.5,351.5Q793.0,327.0 793.0,291.0Q793.0,242.0 757.0,204.5Q721.0,167.0 651.0,167.0Q593.0,167.0 555.5,191.5Q518.0,216.0 493.0,253.0Q494.0,238.0 494.5,221.5Q495.0,205.0 495.0,190.0L495.0,0.0L418.0,0.0Q390.0,53.0 341.5,100.0Q293.0,147.0 230.5,179.5Q168.0,212.0 96.0,223.0L57.0,318.0Q137.0,364.0 212.0,399.0Q287.0,434.0 357.0,457.0Q314.0,510.0 273.0,532.5Q232.0,555.0 191.0,555.0Q157.0,555.0 143.0,541.5Q129.0,528.0 129.0,510.0Q129.0,494.0 138.0,482.0Q147.0,470.0 163.0,460.0L113.0,400.0Q81.0,423.0 64.0,450.0Q47.0,477.0 47.0,514.0Q47.0,567.0 86.0,597.5Q125.0,628.0 184.0,628.0ZM647.0,538.0Q603.0,538.0 565.0,506.5Q527.0,475.0 495.0,423.0L495.0,383.0Q517.0,311.0 556.5,273.5Q596.0,236.0 648.0,236.0Q675.0,236.0 696.0,250.5Q717.0,265.0 717.0,294.0Q717.0,334.0 679.0,358.0Q657.0,350.0 630.0,344.0L613.0,412.0Q666.0,420.0 688.5,440.0Q711.0,460.0 711.0,485.0Q711.0,512.0 692.0,525.0Q673.0,538.0 647.0,538.0ZM150.0,284.0Q196.0,274.0 248.5,249.5Q301.0,225.0 347.0,189.0Q393.0,153.0 421.0,109.0Q420.0,126.0 419.0,144.5Q418.0,163.0 418.0,187.0L418.0,403.0Q353.0,381.0 282.5,350.0Q212.0,319.0 150.0,284.0Z" transform="translate(631, 908)"/>
<path d="M681.0,225.0Q681.0,142.0 619.5,92.0Q558.0,42.0 453.0,42.0Q359.0,42.0 279.0,87.5Q199.0,133.0 136.0,235.5Q73.0,338.0 28.0,507.0L103.0,529.0Q143.0,386.0 192.5,295.0Q242.0,204.0 306.5,161.0Q371.0,118.0 455.0,118.0Q518.0,118.0 559.0,144.5Q600.0,171.0 600.0,228.0Q600.0,255.0 587.0,276.5Q574.0,298.0 552.0,314.0Q520.0,297.0 480.0,282.0L449.0,354.0Q516.0,376.0 553.5,405.5Q591.0,435.0 591.0,482.0Q591.0,558.0 509.0,558.0Q461.0,558.0 420.5,537.5Q380.0,517.0 355.5,489.5Q331.0,462.0 331.0,439.0Q331.0,423.0 341.0,411.5Q351.0,400.0 386.0,395.0L365.0,321.0Q308.0,332.0 279.5,360.0Q251.0,388.0 251.0,431.0Q251.0,465.0 271.5,499.5Q292.0,534.0 328.0,563.5Q364.0,593.0 410.5,611.0Q457.0,629.0 509.0,629.0Q586.0,629.0 628.5,590.0Q671.0,551.0 671.0,483.0Q671.0,445.0 655.5,414.0Q640.0,383.0 613.0,358.0Q681.0,308.0 681.0,225.0Z" transform="translate(1460, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(2180, 908)"/>
<path d="M606.0,622.0L606.0,551.0L501.0,551.0L501.0,0.0L424.0,0.0Q394.0,60.0 341.5,110.5Q289.0,161.0 221.0,196.0Q153.0,231.0 76.0,243.0L37.0,339.0Q128.0,394.0 224.5,439.0Q321.0,484.0 424.0,517.0L424.0,551.0L-10.0,551.0L-10.0,622.0L606.0,622.0ZM130.0,304.0Q181.0,293.0 238.0,266.5Q295.0,240.0 345.5,200.0Q396.0,160.0 427.0,108.0Q426.0,126.0 425.0,145.0Q424.0,164.0 424.0,189.0L424.0,439.0Q352.0,414.0 274.0,379.5Q196.0,345.0 130.0,304.0ZM86.0,186.0Q173.0,170.0 235.0,127.5Q297.0,85.0 332.0,41.0L286.0,0.0Q244.0,44.0 191.0,72.5Q138.0,101.0 70.0,114.0L86.0,186.0Z" transform="translate(2938, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(3534, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0ZM243.0,-107.0Q297.0,-107.0 324.0,-130.0Q351.0,-153.0 351.0,-188.0Q351.0,-200.0 346.5,-213.0Q342.0,-226.0 329.0,-238.0Q389.0,-230.0 413.0,-212.5Q437.0,-195.0 437.0,-167.0Q437.0,-150.0 428.5,-137.0Q420.0,-124.0 395.5,-111.0Q371.0,-98.0 323.0,-84.0Q272.0,-68.0 245.0,-51.5Q218.0,-35.0 218.0,-2.0Q218.0,15.0 228.0,33.0L284.0,20.0Q280.0,12.0 280.0,4.0Q280.0,-6.0 294.5,-13.0Q309.0,-20.0 358.0,-35.0Q418.0,-53.0 450.0,-72.5Q482.0,-92.0 493.5,-115.0Q505.0,-138.0 505.0,-165.0Q505.0,-212.0 473.0,-240.5Q441.0,-269.0 389.5,-281.0Q338.0,-293.0 277.0,-293.0L253.0,-293.0L241.0,-244.0Q268.0,-236.0 280.0,-223.5Q292.0,-211.0 292.0,-194.0Q292.0,-179.0 281.0,-169.5Q270.0,-160.0 245.0,-160.0Q205.0,-160.0 205.0,-184.0Q205.0,-193.0 212.0,-207.0L152.0,-218.0Q141.0,-198.0 141.0,-175.0Q141.0,-146.0 166.5,-126.5Q192.0,-107.0 243.0,-107.0Z" transform="translate(3534, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(4155, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ৠথফূংঞডুিঅ</span> (Added by SIESTA)</li>


<pre>Expected: rrvocalicbeng=0+835|thabeng=1+645|phabeng=2+838|uuvowelsignbeng=2@-221,0+0|anusvarabeng=2+403|nyabeng=5+1019|ivowelsignbeng=6+266|ddabeng=6+712|uvowelsignlongbeng=6@-106,0+0|abeng=9+893</pre>



<pre>Got     : rrvocalicbeng=0+853|thabeng=1+645|phabeng=2+838|uuvowelsignbeng=2@-221,0+0|anusvarabeng=2+438|nyabeng=5+1019|ivowelsignbeng=6+266|ddabeng=6+712|uvowelsignlongbeng=6@-106,0+0|abeng=9+893</pre>



<pre>                           +                                                                         +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5664 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(0, 908)"/>
<path d="M211.0,625.0Q306.0,625.0 353.0,578.5Q400.0,532.0 400.0,464.0Q400.0,394.0 348.0,347.0Q296.0,300.0 203.0,282.0Q303.0,253.0 370.5,202.0Q438.0,151.0 475.0,97.0Q474.0,120.0 473.5,143.0Q473.0,166.0 473.0,193.0L473.0,688.0L526.0,688.0L549.0,622.0L655.0,622.0L655.0,551.0L550.0,551.0L550.0,0.0L473.0,0.0Q435.0,55.0 383.0,103.5Q331.0,152.0 264.5,187.5Q198.0,223.0 115.0,238.0L92.0,331.0Q176.0,337.0 226.0,355.5Q276.0,374.0 297.5,402.5Q319.0,431.0 319.0,466.0Q319.0,509.0 291.0,532.0Q263.0,555.0 209.0,555.0Q159.0,555.0 137.5,535.5Q116.0,516.0 116.0,494.0Q116.0,480.0 123.5,468.0Q131.0,456.0 150.0,446.0L106.0,384.0Q78.0,403.0 58.0,430.0Q38.0,457.0 38.0,497.0Q38.0,550.0 83.0,587.5Q128.0,625.0 211.0,625.0Z" transform="translate(853, 908)"/>
<path d="M848.0,622.0L848.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.5,327.5Q184.0,301.0 142.0,276.0Q246.0,250.0 316.0,207.5Q386.0,165.0 447.0,99.0Q446.0,116.0 445.5,134.0Q445.0,152.0 445.0,171.0L445.0,510.0L458.0,510.0Q540.0,510.0 614.0,488.5Q688.0,467.0 739.0,414.0Q763.0,389.0 777.5,357.5Q792.0,326.0 792.0,288.0Q792.0,255.0 778.5,225.5Q765.0,196.0 735.0,177.0Q705.0,158.0 655.0,158.0Q640.0,158.0 625.5,159.0Q611.0,160.0 597.0,163.0L602.0,234.0Q608.0,233.0 617.0,232.5Q626.0,232.0 636.0,232.0Q685.0,232.0 699.5,251.0Q714.0,270.0 714.0,296.0Q714.0,347.0 662.5,386.0Q611.0,425.0 522.0,434.0L522.0,0.0L445.0,0.0Q404.0,56.0 354.5,98.0Q305.0,140.0 239.5,168.5Q174.0,197.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L848.0,622.0Z" transform="translate(1498, 908)"/>
<path d="M-177.0,-241.0Q-207.0,-241.0 -237.5,-230.5Q-268.0,-220.0 -288.0,-197.0Q-308.0,-174.0 -308.0,-137.0Q-308.0,-87.0 -268.0,-62.0Q-228.0,-37.0 -172.0,-36.0L-172.0,8.0L-95.0,8.0L-95.0,-56.0L-128.0,-102.0Q-135.0,-101.0 -144.5,-100.5Q-154.0,-100.0 -165.0,-100.0Q-235.0,-100.0 -235.0,-140.0Q-235.0,-159.0 -219.0,-169.0Q-203.0,-179.0 -179.0,-179.0Q-137.0,-179.0 -103.0,-159.0Q-69.0,-139.0 -38.0,-102.0Q7.0,-122.0 62.5,-154.0Q118.0,-186.0 163.0,-218.0L121.0,-271.0Q84.0,-243.0 46.0,-220.0Q8.0,-197.0 -22.0,-183.0Q-53.0,-211.0 -91.5,-226.0Q-130.0,-241.0 -177.0,-241.0Z" transform="translate(2115, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(2336, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(2774, 908)"/>
<path d="M276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L82.0,622.0Q66.0,641.0 49.5,662.0Q33.0,683.0 20.0,704.0Q54.0,763.0 93.0,811.5Q132.0,860.0 185.0,888.5Q238.0,917.0 313.0,917.0Q384.0,917.0 447.0,894.0Q510.0,871.0 573.0,829.5Q636.0,788.0 705.0,731.0L663.0,677.0Q594.0,733.0 538.5,770.0Q483.0,807.0 432.5,825.5Q382.0,844.0 325.0,844.0Q242.0,844.0 192.0,802.0Q142.0,760.0 106.0,693.0Q114.0,678.0 128.0,660.0Q142.0,642.0 160.0,622.0L276.0,622.0Z" transform="translate(3793, 908)"/>
<path d="M722.0,622.0L722.0,551.0L356.0,551.0L356.0,372.0Q356.0,316.0 393.0,316.0Q422.0,316.0 454.0,343.5Q486.0,371.0 529.0,433.0L589.0,442.0Q621.0,395.0 638.5,345.0Q656.0,295.0 656.0,245.0Q656.0,182.0 628.5,132.0Q601.0,82.0 547.5,53.0Q494.0,24.0 417.0,24.0Q329.0,24.0 257.0,66.0Q185.0,108.0 128.5,205.0Q72.0,302.0 29.0,465.0L105.0,485.0Q141.0,346.0 184.5,261.5Q228.0,177.0 284.0,138.5Q340.0,100.0 413.0,100.0Q493.0,100.0 536.5,140.0Q580.0,180.0 580.0,243.0Q580.0,277.0 573.0,303.5Q566.0,330.0 553.0,349.0Q514.0,295.0 473.5,268.5Q433.0,242.0 394.0,242.0Q346.0,242.0 317.0,268.0Q301.0,282.0 290.0,307.5Q279.0,333.0 279.0,393.0L279.0,551.0L-10.0,551.0L-10.0,622.0L722.0,622.0Z" transform="translate(4059, 908)"/>
<path d="M-286.0,-266.0Q-313.0,-266.0 -345.0,-254.5Q-377.0,-243.0 -399.5,-218.0Q-422.0,-193.0 -422.0,-151.0Q-422.0,-100.0 -383.0,-69.5Q-344.0,-39.0 -274.0,-39.0Q-223.0,-39.0 -172.0,-56.0L-172.0,52.0L-100.0,52.0L-100.0,-47.0Q-100.0,-55.0 -100.5,-65.0Q-101.0,-75.0 -102.0,-85.0Q-57.0,-109.0 -10.0,-142.5Q37.0,-176.0 89.0,-217.0L44.0,-271.0Q-2.0,-233.0 -41.5,-203.5Q-81.0,-174.0 -117.0,-153.0Q-128.0,-183.0 -148.5,-208.5Q-169.0,-234.0 -202.5,-250.0Q-236.0,-266.0 -286.0,-266.0ZM-351.0,-153.0Q-351.0,-181.0 -331.5,-192.5Q-312.0,-204.0 -286.0,-204.0Q-238.0,-204.0 -214.0,-179.0Q-190.0,-154.0 -181.0,-122.0Q-231.0,-103.0 -279.0,-103.0Q-315.0,-103.0 -333.0,-117.0Q-351.0,-131.0 -351.0,-153.0Z" transform="translate(4665, 908)"/>
<path d="M376.0,91.0Q308.0,91.0 246.0,123.0Q184.0,155.0 129.5,231.5Q75.0,308.0 29.0,442.0L102.0,466.0Q155.0,309.0 219.5,238.0Q284.0,167.0 378.0,167.0Q461.0,167.0 495.5,205.5Q530.0,244.0 530.0,300.0Q530.0,358.0 498.5,394.0Q467.0,430.0 420.0,430.0Q353.0,430.0 353.0,372.0Q353.0,365.0 355.0,353.0Q357.0,341.0 361.0,331.0L285.0,316.0Q278.0,337.0 274.5,354.5Q271.0,372.0 271.0,388.0Q271.0,423.0 290.0,447.5Q309.0,472.0 339.0,485.0Q330.0,507.0 311.5,524.0Q293.0,541.0 262.0,551.0L-10.0,551.0L-10.0,622.0L903.0,622.0L903.0,551.0L798.0,551.0L798.0,0.0L721.0,0.0Q693.0,56.0 653.0,98.5Q613.0,141.0 568.0,173.0Q540.0,136.0 492.0,113.5Q444.0,91.0 376.0,91.0ZM606.0,294.0Q606.0,264.0 598.0,236.0Q634.0,213.0 669.5,178.5Q705.0,144.0 724.0,109.0Q723.0,131.0 722.0,150.5Q721.0,170.0 721.0,194.0L721.0,551.0L381.0,551.0Q406.0,530.0 416.0,500.0Q474.0,499.0 516.5,472.5Q559.0,446.0 582.5,400.0Q606.0,354.0 606.0,294.0Z" transform="translate(4771, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5611 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(0, 908)"/>
<path d="M211.0,625.0Q306.0,625.0 353.0,578.5Q400.0,532.0 400.0,464.0Q400.0,394.0 348.0,347.0Q296.0,300.0 203.0,282.0Q303.0,253.0 370.5,202.0Q438.0,151.0 475.0,97.0Q474.0,120.0 473.5,143.0Q473.0,166.0 473.0,193.0L473.0,688.0L526.0,688.0L549.0,622.0L655.0,622.0L655.0,551.0L550.0,551.0L550.0,0.0L473.0,0.0Q435.0,55.0 383.0,103.5Q331.0,152.0 264.5,187.5Q198.0,223.0 115.0,238.0L92.0,331.0Q176.0,337.0 226.0,355.5Q276.0,374.0 297.5,402.5Q319.0,431.0 319.0,466.0Q319.0,509.0 291.0,532.0Q263.0,555.0 209.0,555.0Q159.0,555.0 137.5,535.5Q116.0,516.0 116.0,494.0Q116.0,480.0 123.5,468.0Q131.0,456.0 150.0,446.0L106.0,384.0Q78.0,403.0 58.0,430.0Q38.0,457.0 38.0,497.0Q38.0,550.0 83.0,587.5Q128.0,625.0 211.0,625.0Z" transform="translate(835, 908)"/>
<path d="M848.0,622.0L848.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.5,327.5Q184.0,301.0 142.0,276.0Q246.0,250.0 316.0,207.5Q386.0,165.0 447.0,99.0Q446.0,116.0 445.5,134.0Q445.0,152.0 445.0,171.0L445.0,510.0L458.0,510.0Q540.0,510.0 614.0,488.5Q688.0,467.0 739.0,414.0Q763.0,389.0 777.5,357.5Q792.0,326.0 792.0,288.0Q792.0,255.0 778.5,225.5Q765.0,196.0 735.0,177.0Q705.0,158.0 655.0,158.0Q640.0,158.0 625.5,159.0Q611.0,160.0 597.0,163.0L602.0,234.0Q608.0,233.0 617.0,232.5Q626.0,232.0 636.0,232.0Q685.0,232.0 699.5,251.0Q714.0,270.0 714.0,296.0Q714.0,347.0 662.5,386.0Q611.0,425.0 522.0,434.0L522.0,0.0L445.0,0.0Q404.0,56.0 354.5,98.0Q305.0,140.0 239.5,168.5Q174.0,197.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L848.0,622.0Z" transform="translate(1480, 908)"/>
<path d="M-177.0,-241.0Q-207.0,-241.0 -237.5,-230.5Q-268.0,-220.0 -288.0,-197.0Q-308.0,-174.0 -308.0,-137.0Q-308.0,-87.0 -268.0,-62.0Q-228.0,-37.0 -172.0,-36.0L-172.0,8.0L-95.0,8.0L-95.0,-56.0L-128.0,-102.0Q-135.0,-101.0 -144.5,-100.5Q-154.0,-100.0 -165.0,-100.0Q-235.0,-100.0 -235.0,-140.0Q-235.0,-159.0 -219.0,-169.0Q-203.0,-179.0 -179.0,-179.0Q-137.0,-179.0 -103.0,-159.0Q-69.0,-139.0 -38.0,-102.0Q7.0,-122.0 62.5,-154.0Q118.0,-186.0 163.0,-218.0L121.0,-271.0Q84.0,-243.0 46.0,-220.0Q8.0,-197.0 -22.0,-183.0Q-53.0,-211.0 -91.5,-226.0Q-130.0,-241.0 -177.0,-241.0Z" transform="translate(2097, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(2318, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(2721, 908)"/>
<path d="M276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L82.0,622.0Q66.0,641.0 49.5,662.0Q33.0,683.0 20.0,704.0Q54.0,763.0 93.0,811.5Q132.0,860.0 185.0,888.5Q238.0,917.0 313.0,917.0Q384.0,917.0 447.0,894.0Q510.0,871.0 573.0,829.5Q636.0,788.0 705.0,731.0L663.0,677.0Q594.0,733.0 538.5,770.0Q483.0,807.0 432.5,825.5Q382.0,844.0 325.0,844.0Q242.0,844.0 192.0,802.0Q142.0,760.0 106.0,693.0Q114.0,678.0 128.0,660.0Q142.0,642.0 160.0,622.0L276.0,622.0Z" transform="translate(3740, 908)"/>
<path d="M722.0,622.0L722.0,551.0L356.0,551.0L356.0,372.0Q356.0,316.0 393.0,316.0Q422.0,316.0 454.0,343.5Q486.0,371.0 529.0,433.0L589.0,442.0Q621.0,395.0 638.5,345.0Q656.0,295.0 656.0,245.0Q656.0,182.0 628.5,132.0Q601.0,82.0 547.5,53.0Q494.0,24.0 417.0,24.0Q329.0,24.0 257.0,66.0Q185.0,108.0 128.5,205.0Q72.0,302.0 29.0,465.0L105.0,485.0Q141.0,346.0 184.5,261.5Q228.0,177.0 284.0,138.5Q340.0,100.0 413.0,100.0Q493.0,100.0 536.5,140.0Q580.0,180.0 580.0,243.0Q580.0,277.0 573.0,303.5Q566.0,330.0 553.0,349.0Q514.0,295.0 473.5,268.5Q433.0,242.0 394.0,242.0Q346.0,242.0 317.0,268.0Q301.0,282.0 290.0,307.5Q279.0,333.0 279.0,393.0L279.0,551.0L-10.0,551.0L-10.0,622.0L722.0,622.0Z" transform="translate(4006, 908)"/>
<path d="M-286.0,-266.0Q-313.0,-266.0 -345.0,-254.5Q-377.0,-243.0 -399.5,-218.0Q-422.0,-193.0 -422.0,-151.0Q-422.0,-100.0 -383.0,-69.5Q-344.0,-39.0 -274.0,-39.0Q-223.0,-39.0 -172.0,-56.0L-172.0,52.0L-100.0,52.0L-100.0,-47.0Q-100.0,-55.0 -100.5,-65.0Q-101.0,-75.0 -102.0,-85.0Q-57.0,-109.0 -10.0,-142.5Q37.0,-176.0 89.0,-217.0L44.0,-271.0Q-2.0,-233.0 -41.5,-203.5Q-81.0,-174.0 -117.0,-153.0Q-128.0,-183.0 -148.5,-208.5Q-169.0,-234.0 -202.5,-250.0Q-236.0,-266.0 -286.0,-266.0ZM-351.0,-153.0Q-351.0,-181.0 -331.5,-192.5Q-312.0,-204.0 -286.0,-204.0Q-238.0,-204.0 -214.0,-179.0Q-190.0,-154.0 -181.0,-122.0Q-231.0,-103.0 -279.0,-103.0Q-315.0,-103.0 -333.0,-117.0Q-351.0,-131.0 -351.0,-153.0Z" transform="translate(4612, 908)"/>
<path d="M376.0,91.0Q308.0,91.0 246.0,123.0Q184.0,155.0 129.5,231.5Q75.0,308.0 29.0,442.0L102.0,466.0Q155.0,309.0 219.5,238.0Q284.0,167.0 378.0,167.0Q461.0,167.0 495.5,205.5Q530.0,244.0 530.0,300.0Q530.0,358.0 498.5,394.0Q467.0,430.0 420.0,430.0Q353.0,430.0 353.0,372.0Q353.0,365.0 355.0,353.0Q357.0,341.0 361.0,331.0L285.0,316.0Q278.0,337.0 274.5,354.5Q271.0,372.0 271.0,388.0Q271.0,423.0 290.0,447.5Q309.0,472.0 339.0,485.0Q330.0,507.0 311.5,524.0Q293.0,541.0 262.0,551.0L-10.0,551.0L-10.0,622.0L903.0,622.0L903.0,551.0L798.0,551.0L798.0,0.0L721.0,0.0Q693.0,56.0 653.0,98.5Q613.0,141.0 568.0,173.0Q540.0,136.0 492.0,113.5Q444.0,91.0 376.0,91.0ZM606.0,294.0Q606.0,264.0 598.0,236.0Q634.0,213.0 669.5,178.5Q705.0,144.0 724.0,109.0Q723.0,131.0 722.0,150.5Q721.0,170.0 721.0,194.0L721.0,551.0L381.0,551.0Q406.0,530.0 416.0,500.0Q474.0,499.0 516.5,472.5Q559.0,446.0 582.5,400.0Q606.0,354.0 606.0,294.0Z" transform="translate(4718, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">প্ঞপফ᳒ভ꣱</span> (Added by SIESTA)</li>


<pre>Expected: pahalfbeng=0+554|nyabeng=2+1001|pabeng=3+716|phabeng=4+838|uni1CD2=4@-164,323+0|bhabeng=6+721|uniA8F1=6@0,323+0</pre>



<pre>Got     : pahalfbeng=0+554|nyabeng=2+1019|pabeng=3+716|phabeng=4+838|uni1CD2=4@-164,323+0|bhabeng=6+721|uniA8F1=6@0,323+0</pre>



<pre>                                       +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3848 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M291.0,629.0Q353.0,629.0 402.0,604.5Q451.0,580.0 499.0,531.0Q547.0,482.0 604.0,408.0L545.0,363.0Q526.0,390.0 508.5,413.0Q491.0,436.0 475.0,455.0L216.0,238.0L162.0,297.0L190.0,318.0Q202.0,331.0 209.0,346.5Q216.0,362.0 216.0,383.0Q216.0,401.0 203.0,417.5Q190.0,434.0 160.0,434.0Q144.0,434.0 127.5,428.5Q111.0,423.0 95.0,413.0L22.0,485.0Q82.0,549.0 147.0,589.0Q212.0,629.0 291.0,629.0ZM281.0,396.0Q281.0,390.0 281.0,383.0Q293.0,395.0 305.5,405.5Q318.0,416.0 333.0,428.0L426.0,505.0Q366.0,556.0 295.0,556.0Q242.0,556.0 199.0,534.5Q156.0,513.0 123.0,485.0Q135.0,491.0 150.0,494.0Q165.0,497.0 182.0,497.0Q235.0,497.0 258.0,466.5Q281.0,436.0 281.0,396.0Z" transform="translate(0, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(554, 908)"/>
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(1573, 908)"/>
<path d="M848.0,622.0L848.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.5,327.5Q184.0,301.0 142.0,276.0Q246.0,250.0 316.0,207.5Q386.0,165.0 447.0,99.0Q446.0,116.0 445.5,134.0Q445.0,152.0 445.0,171.0L445.0,510.0L458.0,510.0Q540.0,510.0 614.0,488.5Q688.0,467.0 739.0,414.0Q763.0,389.0 777.5,357.5Q792.0,326.0 792.0,288.0Q792.0,255.0 778.5,225.5Q765.0,196.0 735.0,177.0Q705.0,158.0 655.0,158.0Q640.0,158.0 625.5,159.0Q611.0,160.0 597.0,163.0L602.0,234.0Q608.0,233.0 617.0,232.5Q626.0,232.0 636.0,232.0Q685.0,232.0 699.5,251.0Q714.0,270.0 714.0,296.0Q714.0,347.0 662.5,386.0Q611.0,425.0 522.0,434.0L522.0,0.0L445.0,0.0Q404.0,56.0 354.5,98.0Q305.0,140.0 239.5,168.5Q174.0,197.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L848.0,622.0Z" transform="translate(2289, 908)"/>
<path d="M-418.0,789.0L-90.0,789.0L-90.0,722.0L-418.0,722.0L-418.0,789.0Z" transform="translate(2963, 1231)"/>
<path d="M731.0,622.0L731.0,551.0L-10.0,551.0L-10.0,622.0L731.0,622.0ZM422.0,43.0Q336.0,43.0 263.0,82.0Q190.0,121.0 131.5,213.0Q73.0,305.0 29.0,465.0L105.0,485.0Q141.0,353.0 186.5,272.5Q232.0,192.0 289.5,155.5Q347.0,119.0 420.0,119.0Q500.0,119.0 544.0,160.5Q588.0,202.0 588.0,267.0Q588.0,303.0 579.0,332.0Q570.0,361.0 555.0,381.0Q520.0,334.0 479.0,309.0Q438.0,284.0 384.0,284.0Q321.0,284.0 285.0,315.5Q249.0,347.0 249.0,402.0Q249.0,425.0 256.0,447.5Q263.0,470.0 271.0,486.0L351.0,462.0Q344.0,452.0 338.0,437.0Q332.0,422.0 332.0,406.0Q332.0,379.0 347.0,367.0Q362.0,355.0 386.0,355.0Q407.0,355.0 428.0,363.0Q449.0,371.0 473.5,394.5Q498.0,418.0 527.0,466.0L590.0,476.0Q664.0,366.0 664.0,266.0Q664.0,203.0 636.0,152.5Q608.0,102.0 554.5,72.5Q501.0,43.0 422.0,43.0Z" transform="translate(3127, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(3848, 1231)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3830 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M291.0,629.0Q353.0,629.0 402.0,604.5Q451.0,580.0 499.0,531.0Q547.0,482.0 604.0,408.0L545.0,363.0Q526.0,390.0 508.5,413.0Q491.0,436.0 475.0,455.0L216.0,238.0L162.0,297.0L190.0,318.0Q202.0,331.0 209.0,346.5Q216.0,362.0 216.0,383.0Q216.0,401.0 203.0,417.5Q190.0,434.0 160.0,434.0Q144.0,434.0 127.5,428.5Q111.0,423.0 95.0,413.0L22.0,485.0Q82.0,549.0 147.0,589.0Q212.0,629.0 291.0,629.0ZM281.0,396.0Q281.0,390.0 281.0,383.0Q293.0,395.0 305.5,405.5Q318.0,416.0 333.0,428.0L426.0,505.0Q366.0,556.0 295.0,556.0Q242.0,556.0 199.0,534.5Q156.0,513.0 123.0,485.0Q135.0,491.0 150.0,494.0Q165.0,497.0 182.0,497.0Q235.0,497.0 258.0,466.5Q281.0,436.0 281.0,396.0Z" transform="translate(0, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(554, 908)"/>
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(1555, 908)"/>
<path d="M848.0,622.0L848.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.5,327.5Q184.0,301.0 142.0,276.0Q246.0,250.0 316.0,207.5Q386.0,165.0 447.0,99.0Q446.0,116.0 445.5,134.0Q445.0,152.0 445.0,171.0L445.0,510.0L458.0,510.0Q540.0,510.0 614.0,488.5Q688.0,467.0 739.0,414.0Q763.0,389.0 777.5,357.5Q792.0,326.0 792.0,288.0Q792.0,255.0 778.5,225.5Q765.0,196.0 735.0,177.0Q705.0,158.0 655.0,158.0Q640.0,158.0 625.5,159.0Q611.0,160.0 597.0,163.0L602.0,234.0Q608.0,233.0 617.0,232.5Q626.0,232.0 636.0,232.0Q685.0,232.0 699.5,251.0Q714.0,270.0 714.0,296.0Q714.0,347.0 662.5,386.0Q611.0,425.0 522.0,434.0L522.0,0.0L445.0,0.0Q404.0,56.0 354.5,98.0Q305.0,140.0 239.5,168.5Q174.0,197.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L848.0,622.0Z" transform="translate(2271, 908)"/>
<path d="M-418.0,789.0L-90.0,789.0L-90.0,722.0L-418.0,722.0L-418.0,789.0Z" transform="translate(2945, 1231)"/>
<path d="M731.0,622.0L731.0,551.0L-10.0,551.0L-10.0,622.0L731.0,622.0ZM422.0,43.0Q336.0,43.0 263.0,82.0Q190.0,121.0 131.5,213.0Q73.0,305.0 29.0,465.0L105.0,485.0Q141.0,353.0 186.5,272.5Q232.0,192.0 289.5,155.5Q347.0,119.0 420.0,119.0Q500.0,119.0 544.0,160.5Q588.0,202.0 588.0,267.0Q588.0,303.0 579.0,332.0Q570.0,361.0 555.0,381.0Q520.0,334.0 479.0,309.0Q438.0,284.0 384.0,284.0Q321.0,284.0 285.0,315.5Q249.0,347.0 249.0,402.0Q249.0,425.0 256.0,447.5Q263.0,470.0 271.0,486.0L351.0,462.0Q344.0,452.0 338.0,437.0Q332.0,422.0 332.0,406.0Q332.0,379.0 347.0,367.0Q362.0,355.0 386.0,355.0Q407.0,355.0 428.0,363.0Q449.0,371.0 473.5,394.5Q498.0,418.0 527.0,466.0L590.0,476.0Q664.0,366.0 664.0,266.0Q664.0,203.0 636.0,152.5Q608.0,102.0 554.5,72.5Q501.0,43.0 422.0,43.0Z" transform="translate(3109, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(3830, 1231)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">4৾ঀ৾ঢ্ংগঌখ</span> (Added by SIESTA)</li>


<pre>Expected: four.beng=0+551|uni09FE=0@0,323+0|uni0980=2+540|uni09FE=2@0,323+0|ddhabeng=4+567|viramabeng=4@-83,0+0|anusvarabeng=4+408|gabeng=7+656|lvocalicbeng=8+621|khabeng=9+696</pre>



<pre>Got     : four.beng=0+551|uni09FE=0@0,323+0|uni0980=2+540|uni09FE=2@0,323+0|ddhabeng=4+567|viramabeng=4@-83,0+0|anusvarabeng=4+438|gabeng=7+656|lvocalicbeng=8+639|khabeng=9+696</pre>



<pre>                                                                                                                                ^                               ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4087 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M341.0,160.0L11.0,160.0L11.0,238.0L335.0,718.0L427.0,718.0L427.0,241.0L531.0,241.0L531.0,160.0L427.0,160.0L427.0,0.0L341.0,0.0L341.0,160.0ZM341.0,241.0L341.0,415.0Q341.0,452.0 342.5,492.5Q344.0,533.0 345.5,568.5Q347.0,604.0 347.0,626.0L343.0,626.0Q336.0,607.0 323.0,581.0Q310.0,555.0 299.0,538.0L98.0,241.0L341.0,241.0Z" transform="translate(0, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(551, 1231)"/>
<path d="M349.0,290.0Q297.0,275.0 246.0,275.0Q148.0,275.0 98.5,320.0Q49.0,365.0 49.0,444.0Q49.0,505.0 82.0,554.0Q115.0,603.0 168.0,631.5Q221.0,660.0 281.0,660.0Q317.0,660.0 347.0,651.5Q377.0,643.0 399.0,623.0Q420.0,604.0 432.0,576.5Q444.0,549.0 444.0,493.0L444.0,108.0Q444.0,72.0 450.5,55.5Q457.0,39.0 474.5,34.5Q492.0,30.0 526.0,29.0L519.0,-49.0Q452.0,-48.0 419.0,-32.0Q386.0,-16.0 375.5,16.5Q365.0,49.0 365.0,98.0L365.0,476.0Q365.0,513.0 361.5,533.5Q358.0,554.0 344.0,567.0Q325.0,588.0 280.0,588.0Q243.0,588.0 208.5,567.5Q174.0,547.0 152.5,513.0Q131.0,479.0 131.0,438.0Q131.0,389.0 164.5,369.5Q198.0,350.0 244.0,350.0Q293.0,350.0 331.0,363.0L349.0,290.0Z" transform="translate(551, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(1091, 1231)"/>
<path d="M577.0,622.0L577.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L577.0,622.0Z" transform="translate(1091, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(1575, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(1658, 908)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(2096, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0Z" transform="translate(2752, 908)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0Z" transform="translate(3391, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4039 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M341.0,160.0L11.0,160.0L11.0,238.0L335.0,718.0L427.0,718.0L427.0,241.0L531.0,241.0L531.0,160.0L427.0,160.0L427.0,0.0L341.0,0.0L341.0,160.0ZM341.0,241.0L341.0,415.0Q341.0,452.0 342.5,492.5Q344.0,533.0 345.5,568.5Q347.0,604.0 347.0,626.0L343.0,626.0Q336.0,607.0 323.0,581.0Q310.0,555.0 299.0,538.0L98.0,241.0L341.0,241.0Z" transform="translate(0, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(551, 1231)"/>
<path d="M349.0,290.0Q297.0,275.0 246.0,275.0Q148.0,275.0 98.5,320.0Q49.0,365.0 49.0,444.0Q49.0,505.0 82.0,554.0Q115.0,603.0 168.0,631.5Q221.0,660.0 281.0,660.0Q317.0,660.0 347.0,651.5Q377.0,643.0 399.0,623.0Q420.0,604.0 432.0,576.5Q444.0,549.0 444.0,493.0L444.0,108.0Q444.0,72.0 450.5,55.5Q457.0,39.0 474.5,34.5Q492.0,30.0 526.0,29.0L519.0,-49.0Q452.0,-48.0 419.0,-32.0Q386.0,-16.0 375.5,16.5Q365.0,49.0 365.0,98.0L365.0,476.0Q365.0,513.0 361.5,533.5Q358.0,554.0 344.0,567.0Q325.0,588.0 280.0,588.0Q243.0,588.0 208.5,567.5Q174.0,547.0 152.5,513.0Q131.0,479.0 131.0,438.0Q131.0,389.0 164.5,369.5Q198.0,350.0 244.0,350.0Q293.0,350.0 331.0,363.0L349.0,290.0Z" transform="translate(551, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(1091, 1231)"/>
<path d="M577.0,622.0L577.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L577.0,622.0Z" transform="translate(1091, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(1575, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(1658, 908)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(2066, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0Z" transform="translate(2722, 908)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0Z" transform="translate(3343, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ড্ফ্টথ৾ৡঐ</span> (Added by SIESTA)</li>


<pre>Expected: ddahalfbeng=0+615|phattabeng=2+842|thabeng=5+645|uni09FE=5@0,323+0|llvocalicbeng=7+621|aibeng=8+873</pre>



<pre>Got     : ddahalfbeng=0+615|phattabeng=2+842|thabeng=5+645|uni09FE=5@0,323+0|llvocalicbeng=7+639|aibeng=8+873</pre>



<pre>                                                                                              ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3614 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M625.0,622.0L625.0,551.0L320.0,551.0L320.0,425.0Q320.0,405.0 327.0,394.0Q334.0,383.0 351.0,383.0Q375.0,383.0 402.0,403.5Q429.0,424.0 467.0,478.0L524.0,487.0Q554.0,446.0 569.5,405.0Q585.0,364.0 585.0,320.0Q585.0,241.0 528.5,189.0Q472.0,137.0 367.0,137.0Q292.0,137.0 229.0,169.0Q166.0,201.0 116.0,275.0Q66.0,349.0 29.0,475.0L103.0,495.0Q145.0,341.0 208.5,276.0Q272.0,211.0 364.0,211.0Q434.0,211.0 471.5,240.5Q509.0,270.0 509.0,322.0Q509.0,364.0 491.0,398.0Q456.0,353.0 421.0,332.5Q386.0,312.0 347.0,312.0Q304.0,312.0 278.0,333.0Q264.0,345.0 253.5,367.5Q243.0,390.0 243.0,439.0L243.0,551.0L-10.0,551.0L-10.0,622.0L625.0,622.0Z" transform="translate(0, 908)"/>
<path d="M690.0,229.0Q738.0,229.0 767.5,202.5Q797.0,176.0 797.0,121.0Q797.0,73.0 769.5,29.0Q742.0,-15.0 701.0,-47.0Q667.0,-73.0 628.0,-88.5Q589.0,-104.0 540.0,-104.0Q503.0,-104.0 474.5,-93.0Q446.0,-82.0 432.0,-66.0Q418.0,-51.0 407.0,-24.5Q396.0,2.0 396.0,63.0L396.0,138.0Q339.0,189.0 263.5,221.0Q188.0,253.0 90.0,263.0L54.0,351.0Q85.0,370.0 110.0,384.5Q135.0,399.0 161.5,412.0Q188.0,425.0 222.0,441.0Q141.0,494.0 43.0,512.0L61.0,551.0L-10.0,551.0L-10.0,622.0L670.0,622.0Q669.0,663.0 650.5,681.0Q632.0,699.0 590.0,699.0L496.0,699.0Q431.0,699.0 395.5,708.0Q360.0,717.0 335.0,736.0Q281.0,777.0 281.0,859.0Q281.0,872.0 282.5,884.5Q284.0,897.0 286.0,912.0L360.0,907.0Q356.0,887.0 356.0,869.0Q356.0,847.0 360.5,830.0Q365.0,813.0 375.0,802.0Q389.0,786.0 415.5,778.5Q442.0,771.0 491.0,771.0L569.0,771.0Q622.0,771.0 653.0,763.0Q684.0,755.0 706.0,734.0Q739.0,702.0 742.0,622.0L852.0,622.0L852.0,551.0L160.0,551.0Q204.0,533.0 240.5,508.5Q277.0,484.0 306.0,458.0L311.0,404.0Q265.0,385.0 224.5,365.5Q184.0,346.0 145.0,325.0Q228.0,312.0 287.0,286.0Q346.0,260.0 398.0,216.0Q397.0,233.0 396.5,252.0Q396.0,271.0 396.0,288.0L396.0,510.0L411.0,510.0Q484.0,510.0 546.0,489.0Q608.0,468.0 646.0,428.0Q663.0,412.0 675.0,387.5Q687.0,363.0 687.0,332.0Q687.0,292.0 658.5,263.0Q630.0,234.0 577.0,234.0Q544.0,234.0 522.0,239.0L527.0,309.0Q532.0,308.0 540.5,307.5Q549.0,307.0 563.0,307.0Q595.0,307.0 604.0,317.5Q613.0,328.0 613.0,342.0Q613.0,375.0 575.5,401.0Q538.0,427.0 473.0,434.0L473.0,67.0Q473.0,27.0 478.0,11.0Q483.0,-5.0 489.0,-12.0Q497.0,-21.0 509.5,-27.0Q522.0,-33.0 544.0,-33.0Q577.0,-33.0 606.5,-20.0Q636.0,-7.0 661.0,13.0Q687.0,35.0 703.0,60.5Q719.0,86.0 719.0,111.0Q719.0,134.0 708.0,144.5Q697.0,155.0 671.0,155.0Q662.0,155.0 652.5,154.0Q643.0,153.0 634.0,151.0L622.0,221.0Q638.0,225.0 654.0,227.0Q670.0,229.0 690.0,229.0Z" transform="translate(615, 908)"/>
<path d="M211.0,625.0Q306.0,625.0 353.0,578.5Q400.0,532.0 400.0,464.0Q400.0,394.0 348.0,347.0Q296.0,300.0 203.0,282.0Q303.0,253.0 370.5,202.0Q438.0,151.0 475.0,97.0Q474.0,120.0 473.5,143.0Q473.0,166.0 473.0,193.0L473.0,688.0L526.0,688.0L549.0,622.0L655.0,622.0L655.0,551.0L550.0,551.0L550.0,0.0L473.0,0.0Q435.0,55.0 383.0,103.5Q331.0,152.0 264.5,187.5Q198.0,223.0 115.0,238.0L92.0,331.0Q176.0,337.0 226.0,355.5Q276.0,374.0 297.5,402.5Q319.0,431.0 319.0,466.0Q319.0,509.0 291.0,532.0Q263.0,555.0 209.0,555.0Q159.0,555.0 137.5,535.5Q116.0,516.0 116.0,494.0Q116.0,480.0 123.5,468.0Q131.0,456.0 150.0,446.0L106.0,384.0Q78.0,403.0 58.0,430.0Q38.0,457.0 38.0,497.0Q38.0,550.0 83.0,587.5Q128.0,625.0 211.0,625.0Z" transform="translate(1457, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(2102, 1231)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0ZM243.0,-107.0Q297.0,-107.0 324.0,-130.0Q351.0,-153.0 351.0,-188.0Q351.0,-200.0 346.5,-213.0Q342.0,-226.0 329.0,-238.0Q389.0,-230.0 413.0,-212.5Q437.0,-195.0 437.0,-167.0Q437.0,-150.0 428.5,-137.0Q420.0,-124.0 395.5,-111.0Q371.0,-98.0 323.0,-84.0Q272.0,-68.0 245.0,-51.5Q218.0,-35.0 218.0,-2.0Q218.0,15.0 228.0,33.0L284.0,20.0Q280.0,12.0 280.0,4.0Q280.0,-6.0 294.5,-13.0Q309.0,-20.0 358.0,-35.0Q418.0,-53.0 450.0,-72.5Q482.0,-92.0 493.5,-115.0Q505.0,-138.0 505.0,-165.0Q505.0,-212.0 473.0,-240.5Q441.0,-269.0 389.5,-281.0Q338.0,-293.0 277.0,-293.0L253.0,-293.0L241.0,-244.0Q268.0,-236.0 280.0,-223.5Q292.0,-211.0 292.0,-194.0Q292.0,-179.0 281.0,-169.5Q270.0,-160.0 245.0,-160.0Q205.0,-160.0 205.0,-184.0Q205.0,-193.0 212.0,-207.0L152.0,-218.0Q141.0,-198.0 141.0,-175.0Q141.0,-146.0 166.5,-126.5Q192.0,-107.0 243.0,-107.0Z" transform="translate(2102, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,454.0Q700.0,470.0 726.5,498.0Q753.0,526.0 753.0,573.0Q753.0,598.0 744.5,616.5Q736.0,635.0 720.0,649.0Q701.0,665.0 670.5,675.5Q640.0,686.0 586.0,693.0L482.0,707.0Q389.0,720.0 347.0,759.5Q305.0,799.0 305.0,875.0Q305.0,884.0 306.5,896.0Q308.0,908.0 309.0,917.0L383.0,913.0Q382.0,906.0 381.0,896.0Q380.0,886.0 380.0,878.0Q380.0,838.0 400.0,814.0Q421.0,790.0 474.0,783.0L605.0,765.0Q671.0,756.0 712.0,741.0Q753.0,726.0 779.0,702.0Q804.0,679.0 817.5,646.5Q831.0,614.0 831.0,575.0Q831.0,523.0 808.5,485.5Q786.0,448.0 748.5,421.0Q711.0,394.0 667.0,374.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(2741, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3596 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M625.0,622.0L625.0,551.0L320.0,551.0L320.0,425.0Q320.0,405.0 327.0,394.0Q334.0,383.0 351.0,383.0Q375.0,383.0 402.0,403.5Q429.0,424.0 467.0,478.0L524.0,487.0Q554.0,446.0 569.5,405.0Q585.0,364.0 585.0,320.0Q585.0,241.0 528.5,189.0Q472.0,137.0 367.0,137.0Q292.0,137.0 229.0,169.0Q166.0,201.0 116.0,275.0Q66.0,349.0 29.0,475.0L103.0,495.0Q145.0,341.0 208.5,276.0Q272.0,211.0 364.0,211.0Q434.0,211.0 471.5,240.5Q509.0,270.0 509.0,322.0Q509.0,364.0 491.0,398.0Q456.0,353.0 421.0,332.5Q386.0,312.0 347.0,312.0Q304.0,312.0 278.0,333.0Q264.0,345.0 253.5,367.5Q243.0,390.0 243.0,439.0L243.0,551.0L-10.0,551.0L-10.0,622.0L625.0,622.0Z" transform="translate(0, 908)"/>
<path d="M690.0,229.0Q738.0,229.0 767.5,202.5Q797.0,176.0 797.0,121.0Q797.0,73.0 769.5,29.0Q742.0,-15.0 701.0,-47.0Q667.0,-73.0 628.0,-88.5Q589.0,-104.0 540.0,-104.0Q503.0,-104.0 474.5,-93.0Q446.0,-82.0 432.0,-66.0Q418.0,-51.0 407.0,-24.5Q396.0,2.0 396.0,63.0L396.0,138.0Q339.0,189.0 263.5,221.0Q188.0,253.0 90.0,263.0L54.0,351.0Q85.0,370.0 110.0,384.5Q135.0,399.0 161.5,412.0Q188.0,425.0 222.0,441.0Q141.0,494.0 43.0,512.0L61.0,551.0L-10.0,551.0L-10.0,622.0L670.0,622.0Q669.0,663.0 650.5,681.0Q632.0,699.0 590.0,699.0L496.0,699.0Q431.0,699.0 395.5,708.0Q360.0,717.0 335.0,736.0Q281.0,777.0 281.0,859.0Q281.0,872.0 282.5,884.5Q284.0,897.0 286.0,912.0L360.0,907.0Q356.0,887.0 356.0,869.0Q356.0,847.0 360.5,830.0Q365.0,813.0 375.0,802.0Q389.0,786.0 415.5,778.5Q442.0,771.0 491.0,771.0L569.0,771.0Q622.0,771.0 653.0,763.0Q684.0,755.0 706.0,734.0Q739.0,702.0 742.0,622.0L852.0,622.0L852.0,551.0L160.0,551.0Q204.0,533.0 240.5,508.5Q277.0,484.0 306.0,458.0L311.0,404.0Q265.0,385.0 224.5,365.5Q184.0,346.0 145.0,325.0Q228.0,312.0 287.0,286.0Q346.0,260.0 398.0,216.0Q397.0,233.0 396.5,252.0Q396.0,271.0 396.0,288.0L396.0,510.0L411.0,510.0Q484.0,510.0 546.0,489.0Q608.0,468.0 646.0,428.0Q663.0,412.0 675.0,387.5Q687.0,363.0 687.0,332.0Q687.0,292.0 658.5,263.0Q630.0,234.0 577.0,234.0Q544.0,234.0 522.0,239.0L527.0,309.0Q532.0,308.0 540.5,307.5Q549.0,307.0 563.0,307.0Q595.0,307.0 604.0,317.5Q613.0,328.0 613.0,342.0Q613.0,375.0 575.5,401.0Q538.0,427.0 473.0,434.0L473.0,67.0Q473.0,27.0 478.0,11.0Q483.0,-5.0 489.0,-12.0Q497.0,-21.0 509.5,-27.0Q522.0,-33.0 544.0,-33.0Q577.0,-33.0 606.5,-20.0Q636.0,-7.0 661.0,13.0Q687.0,35.0 703.0,60.5Q719.0,86.0 719.0,111.0Q719.0,134.0 708.0,144.5Q697.0,155.0 671.0,155.0Q662.0,155.0 652.5,154.0Q643.0,153.0 634.0,151.0L622.0,221.0Q638.0,225.0 654.0,227.0Q670.0,229.0 690.0,229.0Z" transform="translate(615, 908)"/>
<path d="M211.0,625.0Q306.0,625.0 353.0,578.5Q400.0,532.0 400.0,464.0Q400.0,394.0 348.0,347.0Q296.0,300.0 203.0,282.0Q303.0,253.0 370.5,202.0Q438.0,151.0 475.0,97.0Q474.0,120.0 473.5,143.0Q473.0,166.0 473.0,193.0L473.0,688.0L526.0,688.0L549.0,622.0L655.0,622.0L655.0,551.0L550.0,551.0L550.0,0.0L473.0,0.0Q435.0,55.0 383.0,103.5Q331.0,152.0 264.5,187.5Q198.0,223.0 115.0,238.0L92.0,331.0Q176.0,337.0 226.0,355.5Q276.0,374.0 297.5,402.5Q319.0,431.0 319.0,466.0Q319.0,509.0 291.0,532.0Q263.0,555.0 209.0,555.0Q159.0,555.0 137.5,535.5Q116.0,516.0 116.0,494.0Q116.0,480.0 123.5,468.0Q131.0,456.0 150.0,446.0L106.0,384.0Q78.0,403.0 58.0,430.0Q38.0,457.0 38.0,497.0Q38.0,550.0 83.0,587.5Q128.0,625.0 211.0,625.0Z" transform="translate(1457, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(2102, 1231)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0ZM243.0,-107.0Q297.0,-107.0 324.0,-130.0Q351.0,-153.0 351.0,-188.0Q351.0,-200.0 346.5,-213.0Q342.0,-226.0 329.0,-238.0Q389.0,-230.0 413.0,-212.5Q437.0,-195.0 437.0,-167.0Q437.0,-150.0 428.5,-137.0Q420.0,-124.0 395.5,-111.0Q371.0,-98.0 323.0,-84.0Q272.0,-68.0 245.0,-51.5Q218.0,-35.0 218.0,-2.0Q218.0,15.0 228.0,33.0L284.0,20.0Q280.0,12.0 280.0,4.0Q280.0,-6.0 294.5,-13.0Q309.0,-20.0 358.0,-35.0Q418.0,-53.0 450.0,-72.5Q482.0,-92.0 493.5,-115.0Q505.0,-138.0 505.0,-165.0Q505.0,-212.0 473.0,-240.5Q441.0,-269.0 389.5,-281.0Q338.0,-293.0 277.0,-293.0L253.0,-293.0L241.0,-244.0Q268.0,-236.0 280.0,-223.5Q292.0,-211.0 292.0,-194.0Q292.0,-179.0 281.0,-169.5Q270.0,-160.0 245.0,-160.0Q205.0,-160.0 205.0,-184.0Q205.0,-193.0 212.0,-207.0L152.0,-218.0Q141.0,-198.0 141.0,-175.0Q141.0,-146.0 166.5,-126.5Q192.0,-107.0 243.0,-107.0Z" transform="translate(2102, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,454.0Q700.0,470.0 726.5,498.0Q753.0,526.0 753.0,573.0Q753.0,598.0 744.5,616.5Q736.0,635.0 720.0,649.0Q701.0,665.0 670.5,675.5Q640.0,686.0 586.0,693.0L482.0,707.0Q389.0,720.0 347.0,759.5Q305.0,799.0 305.0,875.0Q305.0,884.0 306.5,896.0Q308.0,908.0 309.0,917.0L383.0,913.0Q382.0,906.0 381.0,896.0Q380.0,886.0 380.0,878.0Q380.0,838.0 400.0,814.0Q421.0,790.0 474.0,783.0L605.0,765.0Q671.0,756.0 712.0,741.0Q753.0,726.0 779.0,702.0Q804.0,679.0 817.5,646.5Q831.0,614.0 831.0,575.0Q831.0,523.0 808.5,485.5Q786.0,448.0 748.5,421.0Q711.0,394.0 667.0,374.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(2723, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঝ॑ঊ॑শ্ঞঐ</span> (Added by SIESTA)</li>


<pre>Expected: jhabeng=0+794|uni0951=0@-86,323+0|uubeng=2+853|uni0951=2@-172,323+0|shahalfbeng=4+528|nyabeng=6+1001|aibeng=7+873</pre>



<pre>Got     : jhabeng=0+794|uni0951=0@-86,323+0|uubeng=2+853|uni0951=2@-172,323+0|shahalfbeng=4+528|nyabeng=6+1019|aibeng=7+873</pre>



<pre>                                                                                                            +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4067 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M492.0,622.0L492.0,313.0Q528.0,290.0 565.5,253.0Q603.0,216.0 624.0,179.0Q622.0,210.0 622.0,257.0L622.0,688.0L675.0,688.0L698.0,622.0L804.0,622.0L804.0,551.0L699.0,551.0L699.0,73.0L622.0,73.0Q597.0,122.0 564.0,161.0Q531.0,200.0 492.0,230.0L492.0,0.0L415.0,0.0Q386.0,59.0 334.0,111.0Q282.0,163.0 215.5,198.5Q149.0,234.0 76.0,243.0L37.0,339.0Q127.0,393.0 222.0,439.0Q317.0,485.0 415.0,517.0L415.0,551.0L-10.0,551.0L-10.0,622.0L492.0,622.0ZM130.0,304.0Q183.0,294.0 239.0,266.0Q295.0,238.0 342.5,197.5Q390.0,157.0 418.0,109.0Q417.0,126.0 416.0,145.0Q415.0,164.0 415.0,189.0L415.0,439.0Q345.0,415.0 271.0,380.0Q197.0,345.0 130.0,304.0Z" transform="translate(0, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(708, 1231)"/>
<path d="M649.0,622.0Q648.0,663.0 629.5,681.0Q611.0,699.0 569.0,699.0L384.0,699.0Q318.0,699.0 282.5,708.0Q247.0,717.0 222.0,736.0Q168.0,777.0 168.0,859.0Q168.0,872.0 169.5,885.0Q171.0,898.0 173.0,912.0L247.0,907.0Q245.0,896.0 244.0,886.5Q243.0,877.0 243.0,869.0Q243.0,847.0 247.5,830.0Q252.0,813.0 262.0,802.0Q276.0,786.0 302.5,778.5Q329.0,771.0 378.0,771.0L548.0,771.0Q601.0,771.0 632.0,763.0Q663.0,755.0 685.0,734.0Q718.0,702.0 721.0,622.0L863.0,622.0L863.0,551.0L496.0,551.0L496.0,372.0Q496.0,316.0 533.0,316.0Q562.0,316.0 594.0,343.5Q626.0,371.0 669.0,433.0L729.0,442.0Q761.0,395.0 778.5,345.0Q796.0,295.0 796.0,245.0Q796.0,184.0 770.0,134.0Q744.0,84.0 689.0,54.0Q634.0,24.0 548.0,24.0Q439.0,24.0 343.5,61.0Q248.0,98.0 169.0,188.0Q90.0,278.0 29.0,435.0L104.0,458.0Q130.0,385.0 163.5,321.0Q197.0,257.0 246.5,203.0Q296.0,149.0 369.0,106.0L372.0,109.0Q331.0,147.0 298.0,200.5Q265.0,254.0 240.5,316.5Q216.0,379.0 199.0,440.0L274.0,461.0Q308.0,335.0 345.0,255.5Q382.0,176.0 432.5,138.0Q483.0,100.0 555.0,100.0Q612.0,100.0 648.5,120.0Q685.0,140.0 702.5,172.5Q720.0,205.0 720.0,244.0Q720.0,279.0 712.0,305.5Q704.0,332.0 693.0,349.0Q661.0,305.0 620.0,273.5Q579.0,242.0 534.0,242.0Q486.0,242.0 457.0,268.0Q441.0,282.0 430.0,307.5Q419.0,333.0 419.0,393.0L419.0,551.0L-10.0,551.0L-10.0,622.0L649.0,622.0Z" transform="translate(794, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(1475, 1231)"/>
<path d="M77.0,629.0Q123.0,629.0 164.5,608.0Q206.0,587.0 226.0,541.0Q244.0,586.0 281.5,607.5Q319.0,629.0 364.0,629.0Q433.0,629.0 484.5,589.0Q536.0,549.0 589.0,473.0L530.0,427.0Q493.0,482.0 455.0,519.0Q417.0,556.0 363.0,556.0Q324.0,556.0 300.0,534.5Q276.0,513.0 276.0,471.0Q276.0,431.0 308.5,405.5Q341.0,380.0 413.0,377.0L406.0,300.0Q335.0,304.0 291.5,330.0Q248.0,356.0 230.0,398.0Q212.0,356.0 169.0,328.0Q126.0,300.0 54.0,300.0L48.0,377.0Q99.0,378.0 128.0,391.5Q157.0,405.0 169.0,426.0Q181.0,447.0 181.0,468.0Q181.0,509.0 155.0,532.5Q129.0,556.0 76.0,556.0Q43.0,556.0 -1.0,545.0L-9.0,620.0Q16.0,625.0 35.5,627.0Q55.0,629.0 77.0,629.0Z" transform="translate(1647, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(2175, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,454.0Q700.0,470.0 726.5,498.0Q753.0,526.0 753.0,573.0Q753.0,598.0 744.5,616.5Q736.0,635.0 720.0,649.0Q701.0,665.0 670.5,675.5Q640.0,686.0 586.0,693.0L482.0,707.0Q389.0,720.0 347.0,759.5Q305.0,799.0 305.0,875.0Q305.0,884.0 306.5,896.0Q308.0,908.0 309.0,917.0L383.0,913.0Q382.0,906.0 381.0,896.0Q380.0,886.0 380.0,878.0Q380.0,838.0 400.0,814.0Q421.0,790.0 474.0,783.0L605.0,765.0Q671.0,756.0 712.0,741.0Q753.0,726.0 779.0,702.0Q804.0,679.0 817.5,646.5Q831.0,614.0 831.0,575.0Q831.0,523.0 808.5,485.5Q786.0,448.0 748.5,421.0Q711.0,394.0 667.0,374.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(3194, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4049 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M492.0,622.0L492.0,313.0Q528.0,290.0 565.5,253.0Q603.0,216.0 624.0,179.0Q622.0,210.0 622.0,257.0L622.0,688.0L675.0,688.0L698.0,622.0L804.0,622.0L804.0,551.0L699.0,551.0L699.0,73.0L622.0,73.0Q597.0,122.0 564.0,161.0Q531.0,200.0 492.0,230.0L492.0,0.0L415.0,0.0Q386.0,59.0 334.0,111.0Q282.0,163.0 215.5,198.5Q149.0,234.0 76.0,243.0L37.0,339.0Q127.0,393.0 222.0,439.0Q317.0,485.0 415.0,517.0L415.0,551.0L-10.0,551.0L-10.0,622.0L492.0,622.0ZM130.0,304.0Q183.0,294.0 239.0,266.0Q295.0,238.0 342.5,197.5Q390.0,157.0 418.0,109.0Q417.0,126.0 416.0,145.0Q415.0,164.0 415.0,189.0L415.0,439.0Q345.0,415.0 271.0,380.0Q197.0,345.0 130.0,304.0Z" transform="translate(0, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(708, 1231)"/>
<path d="M649.0,622.0Q648.0,663.0 629.5,681.0Q611.0,699.0 569.0,699.0L384.0,699.0Q318.0,699.0 282.5,708.0Q247.0,717.0 222.0,736.0Q168.0,777.0 168.0,859.0Q168.0,872.0 169.5,885.0Q171.0,898.0 173.0,912.0L247.0,907.0Q245.0,896.0 244.0,886.5Q243.0,877.0 243.0,869.0Q243.0,847.0 247.5,830.0Q252.0,813.0 262.0,802.0Q276.0,786.0 302.5,778.5Q329.0,771.0 378.0,771.0L548.0,771.0Q601.0,771.0 632.0,763.0Q663.0,755.0 685.0,734.0Q718.0,702.0 721.0,622.0L863.0,622.0L863.0,551.0L496.0,551.0L496.0,372.0Q496.0,316.0 533.0,316.0Q562.0,316.0 594.0,343.5Q626.0,371.0 669.0,433.0L729.0,442.0Q761.0,395.0 778.5,345.0Q796.0,295.0 796.0,245.0Q796.0,184.0 770.0,134.0Q744.0,84.0 689.0,54.0Q634.0,24.0 548.0,24.0Q439.0,24.0 343.5,61.0Q248.0,98.0 169.0,188.0Q90.0,278.0 29.0,435.0L104.0,458.0Q130.0,385.0 163.5,321.0Q197.0,257.0 246.5,203.0Q296.0,149.0 369.0,106.0L372.0,109.0Q331.0,147.0 298.0,200.5Q265.0,254.0 240.5,316.5Q216.0,379.0 199.0,440.0L274.0,461.0Q308.0,335.0 345.0,255.5Q382.0,176.0 432.5,138.0Q483.0,100.0 555.0,100.0Q612.0,100.0 648.5,120.0Q685.0,140.0 702.5,172.5Q720.0,205.0 720.0,244.0Q720.0,279.0 712.0,305.5Q704.0,332.0 693.0,349.0Q661.0,305.0 620.0,273.5Q579.0,242.0 534.0,242.0Q486.0,242.0 457.0,268.0Q441.0,282.0 430.0,307.5Q419.0,333.0 419.0,393.0L419.0,551.0L-10.0,551.0L-10.0,622.0L649.0,622.0Z" transform="translate(794, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(1475, 1231)"/>
<path d="M77.0,629.0Q123.0,629.0 164.5,608.0Q206.0,587.0 226.0,541.0Q244.0,586.0 281.5,607.5Q319.0,629.0 364.0,629.0Q433.0,629.0 484.5,589.0Q536.0,549.0 589.0,473.0L530.0,427.0Q493.0,482.0 455.0,519.0Q417.0,556.0 363.0,556.0Q324.0,556.0 300.0,534.5Q276.0,513.0 276.0,471.0Q276.0,431.0 308.5,405.5Q341.0,380.0 413.0,377.0L406.0,300.0Q335.0,304.0 291.5,330.0Q248.0,356.0 230.0,398.0Q212.0,356.0 169.0,328.0Q126.0,300.0 54.0,300.0L48.0,377.0Q99.0,378.0 128.0,391.5Q157.0,405.0 169.0,426.0Q181.0,447.0 181.0,468.0Q181.0,509.0 155.0,532.5Q129.0,556.0 76.0,556.0Q43.0,556.0 -1.0,545.0L-9.0,620.0Q16.0,625.0 35.5,627.0Q55.0,629.0 77.0,629.0Z" transform="translate(1647, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(2175, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,454.0Q700.0,470.0 726.5,498.0Q753.0,526.0 753.0,573.0Q753.0,598.0 744.5,616.5Q736.0,635.0 720.0,649.0Q701.0,665.0 670.5,675.5Q640.0,686.0 586.0,693.0L482.0,707.0Q389.0,720.0 347.0,759.5Q305.0,799.0 305.0,875.0Q305.0,884.0 306.5,896.0Q308.0,908.0 309.0,917.0L383.0,913.0Q382.0,906.0 381.0,896.0Q380.0,886.0 380.0,878.0Q380.0,838.0 400.0,814.0Q421.0,790.0 474.0,783.0L605.0,765.0Q671.0,756.0 712.0,741.0Q753.0,726.0 779.0,702.0Q804.0,679.0 817.5,646.5Q831.0,614.0 831.0,575.0Q831.0,523.0 808.5,485.5Q786.0,448.0 748.5,421.0Q711.0,394.0 667.0,374.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(3176, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">+্৾বন৾খৣ</span> (Added by SIESTA)</li>


<pre>Expected: plus.beng=0+592|uni25CC=0+510|viramabeng=0+0|uni09FE=0@0,323+0|babeng=3+596|nabeng=4+604|uni09FE=4@0,323+0|khabeng=6+696|llvocalicvowelsignbeng=6+0</pre>



<pre>Got     : plus.beng=0+592|uni25CC=0+510|viramabeng=0@19,3+0|uni09FE=0@0,323+0|babeng=3+596|nabeng=4+604|uni09FE=4@0,323+0|khabeng=6+696|llvocalicvowelsignbeng=6+0</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2998 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M259.0,286.0L70.0,286.0L70.0,359.0L259.0,359.0L259.0,548.0L332.0,548.0L332.0,359.0L521.0,359.0L521.0,286.0L332.0,286.0L332.0,97.0L259.0,97.0L259.0,286.0Z" transform="translate(0, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(592, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(1121, 911)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(1102, 1231)"/>
<path d="M606.0,622.0L606.0,551.0L501.0,551.0L501.0,0.0L424.0,0.0Q394.0,60.0 341.5,110.5Q289.0,161.0 221.0,196.0Q153.0,231.0 76.0,243.0L37.0,339.0Q128.0,394.0 224.5,439.0Q321.0,484.0 424.0,517.0L424.0,551.0L-10.0,551.0L-10.0,622.0L606.0,622.0ZM130.0,304.0Q181.0,293.0 238.0,266.5Q295.0,240.0 345.5,200.0Q396.0,160.0 427.0,108.0Q426.0,126.0 425.0,145.0Q424.0,164.0 424.0,189.0L424.0,439.0Q352.0,414.0 274.0,379.5Q196.0,345.0 130.0,304.0Z" transform="translate(1102, 908)"/>
<path d="M614.0,622.0L614.0,551.0L509.0,551.0L509.0,0.0L432.0,0.0L432.0,208.0Q384.0,269.0 327.0,310.0Q270.0,351.0 216.0,351.0Q179.0,351.0 153.5,331.5Q128.0,312.0 128.0,274.0Q128.0,218.0 214.0,184.0L176.0,113.0Q115.0,138.0 80.5,180.5Q46.0,223.0 46.0,277.0Q46.0,326.0 69.5,358.5Q93.0,391.0 129.5,407.0Q166.0,423.0 204.0,423.0Q275.0,423.0 330.5,389.5Q386.0,356.0 435.0,303.0Q433.0,320.0 432.5,337.0Q432.0,354.0 432.0,371.0L432.0,551.0L-10.0,551.0L-10.0,622.0L614.0,622.0Z" transform="translate(1698, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(2302, 1231)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0Z" transform="translate(2302, 908)"/>
<path d="M-449.0,-208.0Q-395.0,-208.0 -368.0,-231.0Q-341.0,-254.0 -341.0,-289.0Q-341.0,-301.0 -345.5,-314.0Q-350.0,-327.0 -363.0,-339.0Q-303.0,-331.0 -279.0,-313.5Q-255.0,-296.0 -255.0,-268.0Q-255.0,-251.0 -263.5,-238.0Q-272.0,-225.0 -296.5,-212.0Q-321.0,-199.0 -369.0,-185.0Q-420.0,-169.0 -447.0,-152.5Q-474.0,-136.0 -474.0,-103.0Q-474.0,-86.0 -464.0,-68.0L-408.0,-81.0Q-412.0,-89.0 -412.0,-97.0Q-412.0,-107.0 -397.5,-114.0Q-383.0,-121.0 -334.0,-136.0Q-274.0,-154.0 -242.0,-173.5Q-210.0,-193.0 -198.5,-216.0Q-187.0,-239.0 -187.0,-266.0Q-187.0,-313.0 -219.0,-341.5Q-251.0,-370.0 -302.5,-382.0Q-354.0,-394.0 -415.0,-394.0L-439.0,-394.0L-451.0,-345.0Q-424.0,-337.0 -412.0,-324.5Q-400.0,-312.0 -400.0,-295.0Q-400.0,-280.0 -411.0,-270.5Q-422.0,-261.0 -447.0,-261.0Q-487.0,-261.0 -487.0,-285.0Q-487.0,-294.0 -480.0,-308.0L-540.0,-319.0Q-551.0,-299.0 -551.0,-276.0Q-551.0,-247.0 -525.5,-227.5Q-500.0,-208.0 -449.0,-208.0ZM-142.0,-127.0Q-88.0,-127.0 -61.0,-150.0Q-34.0,-173.0 -34.0,-208.0Q-34.0,-220.0 -38.5,-233.0Q-43.0,-246.0 -56.0,-258.0Q4.0,-250.0 28.0,-232.5Q52.0,-215.0 52.0,-187.0Q52.0,-170.0 43.5,-157.0Q35.0,-144.0 10.5,-131.0Q-14.0,-118.0 -62.0,-104.0Q-113.0,-88.0 -140.0,-71.5Q-167.0,-55.0 -167.0,-22.0Q-167.0,-5.0 -157.0,13.0L-101.0,0.0Q-105.0,-8.0 -105.0,-16.0Q-105.0,-26.0 -90.5,-33.0Q-76.0,-40.0 -27.0,-55.0Q33.0,-73.0 65.0,-92.5Q97.0,-112.0 108.5,-135.0Q120.0,-158.0 120.0,-185.0Q120.0,-232.0 88.0,-260.5Q56.0,-289.0 4.5,-301.0Q-47.0,-313.0 -108.0,-313.0L-132.0,-313.0L-144.0,-264.0Q-117.0,-256.0 -105.0,-243.5Q-93.0,-231.0 -93.0,-214.0Q-93.0,-199.0 -104.0,-189.5Q-115.0,-180.0 -140.0,-180.0Q-180.0,-180.0 -180.0,-204.0Q-180.0,-213.0 -173.0,-227.0L-233.0,-238.0Q-244.0,-218.0 -244.0,-195.0Q-244.0,-166.0 -218.5,-146.5Q-193.0,-127.0 -142.0,-127.0Z" transform="translate(2998, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2998 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M259.0,286.0L70.0,286.0L70.0,359.0L259.0,359.0L259.0,548.0L332.0,548.0L332.0,359.0L521.0,359.0L521.0,286.0L332.0,286.0L332.0,97.0L259.0,97.0L259.0,286.0Z" transform="translate(0, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(592, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(1102, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(1102, 1231)"/>
<path d="M606.0,622.0L606.0,551.0L501.0,551.0L501.0,0.0L424.0,0.0Q394.0,60.0 341.5,110.5Q289.0,161.0 221.0,196.0Q153.0,231.0 76.0,243.0L37.0,339.0Q128.0,394.0 224.5,439.0Q321.0,484.0 424.0,517.0L424.0,551.0L-10.0,551.0L-10.0,622.0L606.0,622.0ZM130.0,304.0Q181.0,293.0 238.0,266.5Q295.0,240.0 345.5,200.0Q396.0,160.0 427.0,108.0Q426.0,126.0 425.0,145.0Q424.0,164.0 424.0,189.0L424.0,439.0Q352.0,414.0 274.0,379.5Q196.0,345.0 130.0,304.0Z" transform="translate(1102, 908)"/>
<path d="M614.0,622.0L614.0,551.0L509.0,551.0L509.0,0.0L432.0,0.0L432.0,208.0Q384.0,269.0 327.0,310.0Q270.0,351.0 216.0,351.0Q179.0,351.0 153.5,331.5Q128.0,312.0 128.0,274.0Q128.0,218.0 214.0,184.0L176.0,113.0Q115.0,138.0 80.5,180.5Q46.0,223.0 46.0,277.0Q46.0,326.0 69.5,358.5Q93.0,391.0 129.5,407.0Q166.0,423.0 204.0,423.0Q275.0,423.0 330.5,389.5Q386.0,356.0 435.0,303.0Q433.0,320.0 432.5,337.0Q432.0,354.0 432.0,371.0L432.0,551.0L-10.0,551.0L-10.0,622.0L614.0,622.0Z" transform="translate(1698, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(2302, 1231)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0Z" transform="translate(2302, 908)"/>
<path d="M-449.0,-208.0Q-395.0,-208.0 -368.0,-231.0Q-341.0,-254.0 -341.0,-289.0Q-341.0,-301.0 -345.5,-314.0Q-350.0,-327.0 -363.0,-339.0Q-303.0,-331.0 -279.0,-313.5Q-255.0,-296.0 -255.0,-268.0Q-255.0,-251.0 -263.5,-238.0Q-272.0,-225.0 -296.5,-212.0Q-321.0,-199.0 -369.0,-185.0Q-420.0,-169.0 -447.0,-152.5Q-474.0,-136.0 -474.0,-103.0Q-474.0,-86.0 -464.0,-68.0L-408.0,-81.0Q-412.0,-89.0 -412.0,-97.0Q-412.0,-107.0 -397.5,-114.0Q-383.0,-121.0 -334.0,-136.0Q-274.0,-154.0 -242.0,-173.5Q-210.0,-193.0 -198.5,-216.0Q-187.0,-239.0 -187.0,-266.0Q-187.0,-313.0 -219.0,-341.5Q-251.0,-370.0 -302.5,-382.0Q-354.0,-394.0 -415.0,-394.0L-439.0,-394.0L-451.0,-345.0Q-424.0,-337.0 -412.0,-324.5Q-400.0,-312.0 -400.0,-295.0Q-400.0,-280.0 -411.0,-270.5Q-422.0,-261.0 -447.0,-261.0Q-487.0,-261.0 -487.0,-285.0Q-487.0,-294.0 -480.0,-308.0L-540.0,-319.0Q-551.0,-299.0 -551.0,-276.0Q-551.0,-247.0 -525.5,-227.5Q-500.0,-208.0 -449.0,-208.0ZM-142.0,-127.0Q-88.0,-127.0 -61.0,-150.0Q-34.0,-173.0 -34.0,-208.0Q-34.0,-220.0 -38.5,-233.0Q-43.0,-246.0 -56.0,-258.0Q4.0,-250.0 28.0,-232.5Q52.0,-215.0 52.0,-187.0Q52.0,-170.0 43.5,-157.0Q35.0,-144.0 10.5,-131.0Q-14.0,-118.0 -62.0,-104.0Q-113.0,-88.0 -140.0,-71.5Q-167.0,-55.0 -167.0,-22.0Q-167.0,-5.0 -157.0,13.0L-101.0,0.0Q-105.0,-8.0 -105.0,-16.0Q-105.0,-26.0 -90.5,-33.0Q-76.0,-40.0 -27.0,-55.0Q33.0,-73.0 65.0,-92.5Q97.0,-112.0 108.5,-135.0Q120.0,-158.0 120.0,-185.0Q120.0,-232.0 88.0,-260.5Q56.0,-289.0 4.5,-301.0Q-47.0,-313.0 -108.0,-313.0L-132.0,-313.0L-144.0,-264.0Q-117.0,-256.0 -105.0,-243.5Q-93.0,-231.0 -93.0,-214.0Q-93.0,-199.0 -104.0,-189.5Q-115.0,-180.0 -140.0,-180.0Q-180.0,-180.0 -180.0,-204.0Q-180.0,-213.0 -173.0,-227.0L-233.0,-238.0Q-244.0,-218.0 -244.0,-195.0Q-244.0,-166.0 -218.5,-146.5Q-193.0,-127.0 -142.0,-127.0Z" transform="translate(2998, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">য়॑9꣱ঁ৾ত্তছ॒</span> (Added by SIESTA)</li>


<pre>Expected: yyabeng=0+626|uni0951=0@-58,323+0|nine.beng=2+551|uniA8F1=2@0,323+0|uni25CC=2+510|candrabindubeng=2+0|uni09FE=2@0,323+0|tatabeng=6+723|chabeng=9+687|uni0952=9@-89,-313+0</pre>



<pre>Got     : yyabeng=0+626|uni0951=0@-58,323+0|nine.beng=2+551|uniA8F1=2@0,323+0|uni25CC=2+510|candrabindubeng=2@-40,0+0|uni09FE=2@0,323+0|tatabeng=6+723|chabeng=9+687|uni0952=9@-89,-313+0</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3097 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M636.0,622.0L636.0,551.0L531.0,551.0L531.0,0.0L454.0,0.0Q412.0,56.0 361.0,98.5Q310.0,141.0 243.0,170.0Q176.0,199.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L636.0,622.0ZM454.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.0,327.5Q183.0,301.0 141.0,275.0Q250.0,255.0 324.0,209.0Q398.0,163.0 456.0,99.0Q454.0,134.0 454.0,171.0L454.0,551.0ZM180.0,-6.0Q155.0,-6.0 137.5,10.0Q120.0,26.0 120.0,52.0Q120.0,78.0 137.5,95.0Q155.0,112.0 180.0,112.0Q205.0,112.0 222.5,95.0Q240.0,78.0 240.0,52.0Q240.0,26.0 222.5,10.0Q205.0,-6.0 180.0,-6.0Z" transform="translate(0, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(568, 1231)"/>
<path d="M190.0,-10.0Q171.0,-10.0 147.0,-7.5Q123.0,-5.0 106.0,-1.0L106.0,75.0Q123.0,69.0 144.5,66.0Q166.0,63.0 187.0,63.0Q253.0,63.0 296.0,86.0Q339.0,109.0 363.0,148.5Q387.0,188.0 398.0,240.0Q409.0,292.0 411.0,350.0L405.0,350.0Q386.0,315.0 349.5,291.0Q313.0,267.0 255.0,267.0Q163.0,267.0 107.5,324.0Q52.0,381.0 52.0,484.0Q52.0,596.0 110.5,660.0Q169.0,724.0 269.0,724.0Q335.0,724.0 387.5,690.0Q440.0,656.0 471.0,586.0Q502.0,516.0 502.0,409.0Q502.0,348.0 494.5,287.5Q487.0,227.0 467.0,173.5Q447.0,120.0 412.0,78.5Q377.0,37.0 322.5,13.5Q268.0,-10.0 190.0,-10.0ZM267.0,337.0Q311.0,337.0 344.0,356.5Q377.0,376.0 395.0,406.0Q413.0,436.0 413.0,467.0Q413.0,511.0 397.0,552.5Q381.0,594.0 349.5,621.5Q318.0,649.0 270.0,649.0Q212.0,649.0 175.0,609.0Q138.0,569.0 138.0,484.0Q138.0,416.0 170.5,376.5Q203.0,337.0 267.0,337.0Z" transform="translate(626, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(1177, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1177, 908)"/>
<path d="M-90.0,830.0Q-90.0,810.0 -102.5,799.0Q-115.0,788.0 -134.0,788.0Q-156.0,788.0 -167.0,800.5Q-178.0,813.0 -178.0,833.0Q-178.0,849.0 -167.5,861.0Q-157.0,873.0 -135.0,873.0Q-90.0,873.0 -90.0,830.0ZM42.0,861.0Q35.0,785.0 -5.5,735.0Q-46.0,685.0 -131.0,685.0Q-218.0,685.0 -260.0,735.0Q-302.0,785.0 -310.0,860.0L-241.0,869.0Q-236.0,814.0 -212.0,782.5Q-188.0,751.0 -135.0,751.0Q-39.0,751.0 -28.0,870.0L42.0,861.0Z" transform="translate(1647, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(1687, 1231)"/>
<path d="M733.0,622.0L733.0,551.0L-10.0,551.0L-10.0,622.0L733.0,622.0ZM654.0,170.0Q654.0,91.0 594.0,45.5Q534.0,0.0 432.0,0.0Q344.0,0.0 267.5,39.5Q191.0,79.0 130.5,170.5Q70.0,262.0 28.0,417.0L104.0,440.0Q140.0,311.0 185.5,231.0Q231.0,151.0 291.5,113.5Q352.0,76.0 433.0,76.0Q494.0,76.0 533.5,99.0Q573.0,122.0 573.0,172.0Q573.0,194.0 562.0,212.0Q551.0,230.0 531.0,244.0Q499.0,227.0 457.0,212.0L427.0,282.0Q492.0,303.0 528.0,327.0Q564.0,351.0 564.0,393.0Q564.0,457.0 483.0,457.0Q438.0,457.0 399.5,440.0Q361.0,423.0 337.5,400.0Q314.0,377.0 314.0,358.0Q314.0,345.0 323.5,336.0Q333.0,327.0 364.0,322.0L344.0,248.0Q235.0,267.0 235.0,350.0Q235.0,383.0 255.5,414.5Q276.0,446.0 311.0,472.0Q346.0,498.0 391.5,513.0Q437.0,528.0 486.0,528.0Q562.0,528.0 603.0,493.0Q644.0,458.0 644.0,396.0Q644.0,363.0 630.5,335.5Q617.0,308.0 592.0,286.0Q654.0,240.0 654.0,170.0Z" transform="translate(1687, 908)"/>
<path d="M227.0,217.0Q157.0,217.0 125.0,249.0Q110.0,264.0 100.5,288.0Q91.0,312.0 91.0,359.0L91.0,551.0L-10.0,551.0L-10.0,622.0L697.0,622.0L697.0,551.0L168.0,551.0L168.0,544.0Q185.0,525.0 204.0,510.5Q223.0,496.0 251.0,488.5Q279.0,481.0 323.0,481.0L372.0,481.0Q382.0,482.0 397.5,482.5Q413.0,483.0 423.0,483.0Q481.0,483.0 518.5,465.5Q556.0,448.0 577.0,421.0Q598.0,394.0 606.5,364.0Q615.0,334.0 615.0,310.0Q615.0,249.0 589.5,207.5Q564.0,166.0 522.5,141.5Q481.0,117.0 434.0,106.0Q495.0,92.0 555.5,69.5Q616.0,47.0 684.0,11.0L649.0,-49.0Q532.0,14.0 406.5,47.5Q281.0,81.0 143.0,94.0L152.0,166.0Q181.0,160.0 213.5,156.0Q246.0,152.0 290.0,152.0Q379.0,152.0 433.5,175.0Q488.0,198.0 513.0,234.5Q538.0,271.0 538.0,310.0Q538.0,355.0 513.5,382.0Q489.0,409.0 445.0,416.0Q450.0,403.0 450.0,388.0Q450.0,339.0 420.5,300.5Q391.0,262.0 340.5,239.5Q290.0,217.0 227.0,217.0ZM184.0,301.0Q199.0,286.0 233.0,286.0Q276.0,286.0 307.5,302.0Q339.0,318.0 356.5,340.5Q374.0,363.0 374.0,384.0Q374.0,403.0 360.0,408.0Q346.0,413.0 322.0,413.0L316.0,413.0Q269.0,413.0 231.0,428.0Q193.0,443.0 166.0,468.0Q167.0,458.0 167.5,446.0Q168.0,434.0 168.0,420.0L168.0,359.0Q168.0,333.0 172.5,321.0Q177.0,309.0 184.0,301.0Z" transform="translate(2410, 908)"/>
<path d="M-443.0,-187.0L-443.0,-116.0L-67.0,-116.0L-67.0,-187.0L-443.0,-187.0Z" transform="translate(3008, 595)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3097 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M636.0,622.0L636.0,551.0L531.0,551.0L531.0,0.0L454.0,0.0Q412.0,56.0 361.0,98.5Q310.0,141.0 243.0,170.0Q176.0,199.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L636.0,622.0ZM454.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.0,327.5Q183.0,301.0 141.0,275.0Q250.0,255.0 324.0,209.0Q398.0,163.0 456.0,99.0Q454.0,134.0 454.0,171.0L454.0,551.0ZM180.0,-6.0Q155.0,-6.0 137.5,10.0Q120.0,26.0 120.0,52.0Q120.0,78.0 137.5,95.0Q155.0,112.0 180.0,112.0Q205.0,112.0 222.5,95.0Q240.0,78.0 240.0,52.0Q240.0,26.0 222.5,10.0Q205.0,-6.0 180.0,-6.0Z" transform="translate(0, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(568, 1231)"/>
<path d="M190.0,-10.0Q171.0,-10.0 147.0,-7.5Q123.0,-5.0 106.0,-1.0L106.0,75.0Q123.0,69.0 144.5,66.0Q166.0,63.0 187.0,63.0Q253.0,63.0 296.0,86.0Q339.0,109.0 363.0,148.5Q387.0,188.0 398.0,240.0Q409.0,292.0 411.0,350.0L405.0,350.0Q386.0,315.0 349.5,291.0Q313.0,267.0 255.0,267.0Q163.0,267.0 107.5,324.0Q52.0,381.0 52.0,484.0Q52.0,596.0 110.5,660.0Q169.0,724.0 269.0,724.0Q335.0,724.0 387.5,690.0Q440.0,656.0 471.0,586.0Q502.0,516.0 502.0,409.0Q502.0,348.0 494.5,287.5Q487.0,227.0 467.0,173.5Q447.0,120.0 412.0,78.5Q377.0,37.0 322.5,13.5Q268.0,-10.0 190.0,-10.0ZM267.0,337.0Q311.0,337.0 344.0,356.5Q377.0,376.0 395.0,406.0Q413.0,436.0 413.0,467.0Q413.0,511.0 397.0,552.5Q381.0,594.0 349.5,621.5Q318.0,649.0 270.0,649.0Q212.0,649.0 175.0,609.0Q138.0,569.0 138.0,484.0Q138.0,416.0 170.5,376.5Q203.0,337.0 267.0,337.0Z" transform="translate(626, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(1177, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1177, 908)"/>
<path d="M-90.0,830.0Q-90.0,810.0 -102.5,799.0Q-115.0,788.0 -134.0,788.0Q-156.0,788.0 -167.0,800.5Q-178.0,813.0 -178.0,833.0Q-178.0,849.0 -167.5,861.0Q-157.0,873.0 -135.0,873.0Q-90.0,873.0 -90.0,830.0ZM42.0,861.0Q35.0,785.0 -5.5,735.0Q-46.0,685.0 -131.0,685.0Q-218.0,685.0 -260.0,735.0Q-302.0,785.0 -310.0,860.0L-241.0,869.0Q-236.0,814.0 -212.0,782.5Q-188.0,751.0 -135.0,751.0Q-39.0,751.0 -28.0,870.0L42.0,861.0Z" transform="translate(1687, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(1687, 1231)"/>
<path d="M733.0,622.0L733.0,551.0L-10.0,551.0L-10.0,622.0L733.0,622.0ZM654.0,170.0Q654.0,91.0 594.0,45.5Q534.0,0.0 432.0,0.0Q344.0,0.0 267.5,39.5Q191.0,79.0 130.5,170.5Q70.0,262.0 28.0,417.0L104.0,440.0Q140.0,311.0 185.5,231.0Q231.0,151.0 291.5,113.5Q352.0,76.0 433.0,76.0Q494.0,76.0 533.5,99.0Q573.0,122.0 573.0,172.0Q573.0,194.0 562.0,212.0Q551.0,230.0 531.0,244.0Q499.0,227.0 457.0,212.0L427.0,282.0Q492.0,303.0 528.0,327.0Q564.0,351.0 564.0,393.0Q564.0,457.0 483.0,457.0Q438.0,457.0 399.5,440.0Q361.0,423.0 337.5,400.0Q314.0,377.0 314.0,358.0Q314.0,345.0 323.5,336.0Q333.0,327.0 364.0,322.0L344.0,248.0Q235.0,267.0 235.0,350.0Q235.0,383.0 255.5,414.5Q276.0,446.0 311.0,472.0Q346.0,498.0 391.5,513.0Q437.0,528.0 486.0,528.0Q562.0,528.0 603.0,493.0Q644.0,458.0 644.0,396.0Q644.0,363.0 630.5,335.5Q617.0,308.0 592.0,286.0Q654.0,240.0 654.0,170.0Z" transform="translate(1687, 908)"/>
<path d="M227.0,217.0Q157.0,217.0 125.0,249.0Q110.0,264.0 100.5,288.0Q91.0,312.0 91.0,359.0L91.0,551.0L-10.0,551.0L-10.0,622.0L697.0,622.0L697.0,551.0L168.0,551.0L168.0,544.0Q185.0,525.0 204.0,510.5Q223.0,496.0 251.0,488.5Q279.0,481.0 323.0,481.0L372.0,481.0Q382.0,482.0 397.5,482.5Q413.0,483.0 423.0,483.0Q481.0,483.0 518.5,465.5Q556.0,448.0 577.0,421.0Q598.0,394.0 606.5,364.0Q615.0,334.0 615.0,310.0Q615.0,249.0 589.5,207.5Q564.0,166.0 522.5,141.5Q481.0,117.0 434.0,106.0Q495.0,92.0 555.5,69.5Q616.0,47.0 684.0,11.0L649.0,-49.0Q532.0,14.0 406.5,47.5Q281.0,81.0 143.0,94.0L152.0,166.0Q181.0,160.0 213.5,156.0Q246.0,152.0 290.0,152.0Q379.0,152.0 433.5,175.0Q488.0,198.0 513.0,234.5Q538.0,271.0 538.0,310.0Q538.0,355.0 513.5,382.0Q489.0,409.0 445.0,416.0Q450.0,403.0 450.0,388.0Q450.0,339.0 420.5,300.5Q391.0,262.0 340.5,239.5Q290.0,217.0 227.0,217.0ZM184.0,301.0Q199.0,286.0 233.0,286.0Q276.0,286.0 307.5,302.0Q339.0,318.0 356.5,340.5Q374.0,363.0 374.0,384.0Q374.0,403.0 360.0,408.0Q346.0,413.0 322.0,413.0L316.0,413.0Q269.0,413.0 231.0,428.0Q193.0,443.0 166.0,468.0Q167.0,458.0 167.5,446.0Q168.0,434.0 168.0,420.0L168.0,359.0Q168.0,333.0 172.5,321.0Q177.0,309.0 184.0,301.0Z" transform="translate(2410, 908)"/>
<path d="M-443.0,-187.0L-443.0,-116.0L-67.0,-116.0L-67.0,-187.0L-443.0,-187.0Z" transform="translate(3008, 595)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ৠখঞ্ঝশুণ্ধৢ</span> (Added by SIESTA)</li>


<pre>Expected: rrvocalicbeng=0+835|khabeng=1+696|nyajhabeng=2+956|shubeng=5+807|nnahalfbeng=7+413|dhabeng=9+596|lvocalicvowelsignbeng=9+0</pre>



<pre>Got     : rrvocalicbeng=0+853|khabeng=1+696|nyajhabeng=2+974|shubeng=5+825|nnahalfbeng=7+413|dhabeng=9+596|lvocalicvowelsignbeng=9+0</pre>



<pre>                           +                              ^^            ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4357 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(0, 908)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0Z" transform="translate(853, 908)"/>
<path d="M472.0,628.0Q509.0,628.0 535.0,619.0Q561.0,610.0 578.0,596.0Q609.0,571.0 616.0,527.0Q651.0,565.0 689.5,586.0Q728.0,607.0 778.0,607.0Q840.0,607.0 876.5,575.0Q913.0,543.0 913.0,493.0Q913.0,470.0 904.0,442.5Q895.0,415.0 867.0,392.0Q888.0,376.0 903.5,351.5Q919.0,327.0 919.0,291.0Q919.0,253.0 898.0,222.0Q877.0,191.0 834.0,177.0L834.0,-116.0L757.0,-116.0Q731.0,-65.0 696.0,-25.0Q661.0,15.0 621.0,46.0L621.0,-161.0L544.0,-161.0Q488.0,-103.0 427.0,-76.5Q366.0,-50.0 294.0,-38.0L258.0,42.0Q315.0,75.0 385.5,108.0Q456.0,141.0 519.0,163.0Q495.0,189.0 451.0,189.0Q417.0,189.0 388.0,185.0Q359.0,181.0 327.5,176.5Q296.0,172.0 253.0,172.0Q222.0,172.0 186.0,179.0Q150.0,186.0 118.5,205.5Q87.0,225.0 67.0,263.0Q47.0,301.0 47.0,364.0Q47.0,386.0 50.0,411.0Q53.0,436.0 57.0,455.0L134.0,443.0Q130.0,427.0 127.5,410.0Q125.0,393.0 125.0,367.0Q125.0,313.0 145.0,287.0Q165.0,261.0 194.5,253.5Q224.0,246.0 252.0,246.0Q289.0,246.0 318.0,250.0Q347.0,254.0 374.5,258.5Q402.0,263.0 433.0,263.0Q465.0,263.0 495.0,251.0Q525.0,239.0 544.0,208.0L544.0,467.0Q544.0,500.0 539.5,516.5Q535.0,533.0 524.0,542.0Q516.0,549.0 504.0,553.0Q492.0,557.0 472.0,557.0Q433.0,557.0 399.5,538.5Q366.0,520.0 345.5,494.0Q325.0,468.0 325.0,445.0Q325.0,429.0 335.0,418.5Q345.0,408.0 377.0,408.0Q391.0,408.0 401.5,409.0Q412.0,410.0 422.0,411.0L429.0,341.0Q419.0,337.0 402.5,335.0Q386.0,333.0 362.0,333.0Q317.0,333.0 282.0,358.0Q247.0,383.0 247.0,443.0Q247.0,475.0 264.0,507.5Q281.0,540.0 311.5,567.0Q342.0,594.0 383.0,611.0Q424.0,628.0 472.0,628.0ZM773.0,538.0Q729.0,538.0 690.5,506.5Q652.0,475.0 621.0,423.0L621.0,383.0Q644.0,312.0 683.0,274.0Q722.0,236.0 774.0,236.0Q802.0,236.0 822.5,250.5Q843.0,265.0 843.0,294.0Q843.0,334.0 805.0,358.0Q783.0,350.0 756.0,344.0L739.0,412.0Q792.0,420.0 814.5,440.0Q837.0,460.0 837.0,485.0Q837.0,512.0 818.0,525.0Q799.0,538.0 773.0,538.0ZM759.0,68.0L759.0,168.0Q711.0,172.0 677.0,194.5Q643.0,217.0 620.0,251.0Q620.0,240.0 620.5,228.5Q621.0,217.0 621.0,205.0L621.0,124.0Q647.0,109.0 674.0,86.0Q701.0,63.0 724.5,36.0Q748.0,9.0 762.0,-17.0Q759.0,17.0 759.0,68.0ZM544.0,102.0Q514.0,91.0 479.0,76.0Q444.0,61.0 410.0,45.0Q376.0,29.0 351.0,15.0Q406.0,2.0 454.5,-19.5Q503.0,-41.0 547.0,-80.0Q546.0,-63.0 545.0,-41.0Q544.0,-19.0 544.0,-6.0L544.0,102.0Z" transform="translate(1549, 908)"/>
<path d="M519.0,32.0Q410.0,32.0 315.5,75.0Q221.0,118.0 148.0,213.0Q75.0,308.0 28.0,464.0L102.0,487.0Q167.0,286.0 268.5,197.0Q370.0,108.0 517.0,108.0Q594.0,108.0 640.5,134.5Q687.0,161.0 687.0,218.0Q687.0,242.0 678.0,261.0Q669.0,280.0 653.0,295.0Q616.0,270.0 566.0,250.0L535.0,323.0Q602.0,348.0 641.5,381.5Q681.0,415.0 681.0,470.0Q681.0,490.0 674.0,509.0Q667.0,528.0 651.0,544.0L582.0,459.0L521.0,457.0Q512.0,509.0 491.5,532.5Q471.0,556.0 439.0,556.0Q411.0,556.0 392.5,539.5Q374.0,523.0 374.0,490.0Q374.0,458.0 398.0,438.0Q422.0,418.0 476.0,416.0L471.0,339.0Q418.0,342.0 384.0,361.5Q350.0,381.0 333.0,413.0Q317.0,380.0 283.5,358.5Q250.0,337.0 196.0,337.0L189.0,414.0Q247.0,415.0 268.0,438.0Q289.0,461.0 289.0,486.0Q289.0,519.0 267.5,537.5Q246.0,556.0 203.0,556.0Q185.0,556.0 171.5,553.0Q158.0,550.0 141.0,545.0L133.0,620.0Q154.0,625.0 171.0,627.0Q188.0,629.0 207.0,629.0Q243.0,629.0 276.5,613.0Q310.0,597.0 329.0,562.0Q345.0,596.0 375.0,612.5Q405.0,629.0 440.0,629.0Q480.0,629.0 508.5,610.0Q537.0,591.0 562.0,542.0L616.0,608.0L677.0,622.0Q709.0,597.0 733.0,559.5Q757.0,522.0 757.0,471.0Q757.0,433.0 744.0,401.0Q731.0,369.0 708.0,342.0Q768.0,293.0 768.0,212.0Q768.0,131.0 701.5,81.5Q635.0,32.0 519.0,32.0Z" transform="translate(2523, 908)"/>
<path d="M202.0,629.0Q254.0,629.0 296.5,610.5Q339.0,592.0 379.0,557.0Q419.0,522.0 465.0,474.0L409.0,423.0Q353.0,489.0 308.0,522.5Q263.0,556.0 213.0,556.0Q178.0,556.0 150.0,536.5Q122.0,517.0 122.0,470.0Q122.0,425.0 157.0,403.0Q192.0,381.0 261.0,373.0L255.0,290.0Q195.0,295.0 146.0,316.0Q97.0,337.0 68.5,375.5Q40.0,414.0 40.0,469.0Q40.0,525.0 63.5,560.0Q87.0,595.0 124.5,612.0Q162.0,629.0 202.0,629.0Z" transform="translate(3348, 908)"/>
<path d="M240.0,629.0Q252.0,629.0 266.0,627.5Q280.0,626.0 293.0,624.0L287.0,552.0Q281.0,553.0 272.5,553.5Q264.0,554.0 251.0,554.0Q221.0,554.0 204.5,541.5Q188.0,529.0 188.0,509.0Q188.0,490.0 199.5,475.5Q211.0,461.0 240.0,446.0Q285.0,466.0 331.0,484.0Q377.0,502.0 424.0,517.0L424.0,622.0L606.0,622.0L606.0,551.0L501.0,551.0L501.0,0.0L424.0,0.0Q394.0,60.0 341.5,110.5Q289.0,161.0 221.0,196.0Q153.0,231.0 76.0,243.0L37.0,339.0Q105.0,380.0 173.0,414.0Q143.0,436.0 126.0,463.0Q109.0,490.0 109.0,524.0Q109.0,565.0 141.0,597.0Q173.0,629.0 240.0,629.0ZM130.0,304.0Q181.0,293.0 238.0,266.5Q295.0,240.0 345.5,200.0Q396.0,160.0 427.0,108.0Q426.0,126.0 425.0,145.0Q424.0,164.0 424.0,189.0L424.0,439.0Q352.0,414.0 274.0,379.5Q196.0,345.0 130.0,304.0Z" transform="translate(3761, 908)"/>
<path d="M-254.0,-127.0Q-200.0,-127.0 -173.0,-150.0Q-146.0,-173.0 -146.0,-208.0Q-146.0,-220.0 -150.5,-233.0Q-155.0,-246.0 -168.0,-258.0Q-108.0,-250.0 -84.0,-232.5Q-60.0,-215.0 -60.0,-187.0Q-60.0,-170.0 -68.5,-157.0Q-77.0,-144.0 -101.5,-131.0Q-126.0,-118.0 -174.0,-104.0Q-225.0,-88.0 -252.0,-71.5Q-279.0,-55.0 -279.0,-22.0Q-279.0,-5.0 -269.0,13.0L-213.0,0.0Q-217.0,-8.0 -217.0,-16.0Q-217.0,-26.0 -202.5,-33.0Q-188.0,-40.0 -139.0,-55.0Q-79.0,-73.0 -47.0,-92.5Q-15.0,-112.0 -3.5,-135.0Q8.0,-158.0 8.0,-185.0Q8.0,-232.0 -24.0,-260.5Q-56.0,-289.0 -107.5,-301.0Q-159.0,-313.0 -220.0,-313.0L-244.0,-313.0L-256.0,-264.0Q-229.0,-256.0 -217.0,-243.5Q-205.0,-231.0 -205.0,-214.0Q-205.0,-199.0 -216.0,-189.5Q-227.0,-180.0 -252.0,-180.0Q-292.0,-180.0 -292.0,-204.0Q-292.0,-213.0 -285.0,-227.0L-345.0,-238.0Q-356.0,-218.0 -356.0,-195.0Q-356.0,-166.0 -330.5,-146.5Q-305.0,-127.0 -254.0,-127.0Z" transform="translate(4357, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4303 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(0, 908)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0Z" transform="translate(835, 908)"/>
<path d="M472.0,628.0Q509.0,628.0 535.0,619.0Q561.0,610.0 578.0,596.0Q609.0,571.0 616.0,527.0Q651.0,565.0 689.5,586.0Q728.0,607.0 778.0,607.0Q840.0,607.0 876.5,575.0Q913.0,543.0 913.0,493.0Q913.0,470.0 904.0,442.5Q895.0,415.0 867.0,392.0Q888.0,376.0 903.5,351.5Q919.0,327.0 919.0,291.0Q919.0,253.0 898.0,222.0Q877.0,191.0 834.0,177.0L834.0,-116.0L757.0,-116.0Q731.0,-65.0 696.0,-25.0Q661.0,15.0 621.0,46.0L621.0,-161.0L544.0,-161.0Q488.0,-103.0 427.0,-76.5Q366.0,-50.0 294.0,-38.0L258.0,42.0Q315.0,75.0 385.5,108.0Q456.0,141.0 519.0,163.0Q495.0,189.0 451.0,189.0Q417.0,189.0 388.0,185.0Q359.0,181.0 327.5,176.5Q296.0,172.0 253.0,172.0Q222.0,172.0 186.0,179.0Q150.0,186.0 118.5,205.5Q87.0,225.0 67.0,263.0Q47.0,301.0 47.0,364.0Q47.0,386.0 50.0,411.0Q53.0,436.0 57.0,455.0L134.0,443.0Q130.0,427.0 127.5,410.0Q125.0,393.0 125.0,367.0Q125.0,313.0 145.0,287.0Q165.0,261.0 194.5,253.5Q224.0,246.0 252.0,246.0Q289.0,246.0 318.0,250.0Q347.0,254.0 374.5,258.5Q402.0,263.0 433.0,263.0Q465.0,263.0 495.0,251.0Q525.0,239.0 544.0,208.0L544.0,467.0Q544.0,500.0 539.5,516.5Q535.0,533.0 524.0,542.0Q516.0,549.0 504.0,553.0Q492.0,557.0 472.0,557.0Q433.0,557.0 399.5,538.5Q366.0,520.0 345.5,494.0Q325.0,468.0 325.0,445.0Q325.0,429.0 335.0,418.5Q345.0,408.0 377.0,408.0Q391.0,408.0 401.5,409.0Q412.0,410.0 422.0,411.0L429.0,341.0Q419.0,337.0 402.5,335.0Q386.0,333.0 362.0,333.0Q317.0,333.0 282.0,358.0Q247.0,383.0 247.0,443.0Q247.0,475.0 264.0,507.5Q281.0,540.0 311.5,567.0Q342.0,594.0 383.0,611.0Q424.0,628.0 472.0,628.0ZM773.0,538.0Q729.0,538.0 690.5,506.5Q652.0,475.0 621.0,423.0L621.0,383.0Q644.0,312.0 683.0,274.0Q722.0,236.0 774.0,236.0Q802.0,236.0 822.5,250.5Q843.0,265.0 843.0,294.0Q843.0,334.0 805.0,358.0Q783.0,350.0 756.0,344.0L739.0,412.0Q792.0,420.0 814.5,440.0Q837.0,460.0 837.0,485.0Q837.0,512.0 818.0,525.0Q799.0,538.0 773.0,538.0ZM759.0,68.0L759.0,168.0Q711.0,172.0 677.0,194.5Q643.0,217.0 620.0,251.0Q620.0,240.0 620.5,228.5Q621.0,217.0 621.0,205.0L621.0,124.0Q647.0,109.0 674.0,86.0Q701.0,63.0 724.5,36.0Q748.0,9.0 762.0,-17.0Q759.0,17.0 759.0,68.0ZM544.0,102.0Q514.0,91.0 479.0,76.0Q444.0,61.0 410.0,45.0Q376.0,29.0 351.0,15.0Q406.0,2.0 454.5,-19.5Q503.0,-41.0 547.0,-80.0Q546.0,-63.0 545.0,-41.0Q544.0,-19.0 544.0,-6.0L544.0,102.0Z" transform="translate(1531, 908)"/>
<path d="M519.0,32.0Q410.0,32.0 315.5,75.0Q221.0,118.0 148.0,213.0Q75.0,308.0 28.0,464.0L102.0,487.0Q167.0,286.0 268.5,197.0Q370.0,108.0 517.0,108.0Q594.0,108.0 640.5,134.5Q687.0,161.0 687.0,218.0Q687.0,242.0 678.0,261.0Q669.0,280.0 653.0,295.0Q616.0,270.0 566.0,250.0L535.0,323.0Q602.0,348.0 641.5,381.5Q681.0,415.0 681.0,470.0Q681.0,490.0 674.0,509.0Q667.0,528.0 651.0,544.0L582.0,459.0L521.0,457.0Q512.0,509.0 491.5,532.5Q471.0,556.0 439.0,556.0Q411.0,556.0 392.5,539.5Q374.0,523.0 374.0,490.0Q374.0,458.0 398.0,438.0Q422.0,418.0 476.0,416.0L471.0,339.0Q418.0,342.0 384.0,361.5Q350.0,381.0 333.0,413.0Q317.0,380.0 283.5,358.5Q250.0,337.0 196.0,337.0L189.0,414.0Q247.0,415.0 268.0,438.0Q289.0,461.0 289.0,486.0Q289.0,519.0 267.5,537.5Q246.0,556.0 203.0,556.0Q185.0,556.0 171.5,553.0Q158.0,550.0 141.0,545.0L133.0,620.0Q154.0,625.0 171.0,627.0Q188.0,629.0 207.0,629.0Q243.0,629.0 276.5,613.0Q310.0,597.0 329.0,562.0Q345.0,596.0 375.0,612.5Q405.0,629.0 440.0,629.0Q480.0,629.0 508.5,610.0Q537.0,591.0 562.0,542.0L616.0,608.0L677.0,622.0Q709.0,597.0 733.0,559.5Q757.0,522.0 757.0,471.0Q757.0,433.0 744.0,401.0Q731.0,369.0 708.0,342.0Q768.0,293.0 768.0,212.0Q768.0,131.0 701.5,81.5Q635.0,32.0 519.0,32.0Z" transform="translate(2487, 908)"/>
<path d="M202.0,629.0Q254.0,629.0 296.5,610.5Q339.0,592.0 379.0,557.0Q419.0,522.0 465.0,474.0L409.0,423.0Q353.0,489.0 308.0,522.5Q263.0,556.0 213.0,556.0Q178.0,556.0 150.0,536.5Q122.0,517.0 122.0,470.0Q122.0,425.0 157.0,403.0Q192.0,381.0 261.0,373.0L255.0,290.0Q195.0,295.0 146.0,316.0Q97.0,337.0 68.5,375.5Q40.0,414.0 40.0,469.0Q40.0,525.0 63.5,560.0Q87.0,595.0 124.5,612.0Q162.0,629.0 202.0,629.0Z" transform="translate(3294, 908)"/>
<path d="M240.0,629.0Q252.0,629.0 266.0,627.5Q280.0,626.0 293.0,624.0L287.0,552.0Q281.0,553.0 272.5,553.5Q264.0,554.0 251.0,554.0Q221.0,554.0 204.5,541.5Q188.0,529.0 188.0,509.0Q188.0,490.0 199.5,475.5Q211.0,461.0 240.0,446.0Q285.0,466.0 331.0,484.0Q377.0,502.0 424.0,517.0L424.0,622.0L606.0,622.0L606.0,551.0L501.0,551.0L501.0,0.0L424.0,0.0Q394.0,60.0 341.5,110.5Q289.0,161.0 221.0,196.0Q153.0,231.0 76.0,243.0L37.0,339.0Q105.0,380.0 173.0,414.0Q143.0,436.0 126.0,463.0Q109.0,490.0 109.0,524.0Q109.0,565.0 141.0,597.0Q173.0,629.0 240.0,629.0ZM130.0,304.0Q181.0,293.0 238.0,266.5Q295.0,240.0 345.5,200.0Q396.0,160.0 427.0,108.0Q426.0,126.0 425.0,145.0Q424.0,164.0 424.0,189.0L424.0,439.0Q352.0,414.0 274.0,379.5Q196.0,345.0 130.0,304.0Z" transform="translate(3707, 908)"/>
<path d="M-254.0,-127.0Q-200.0,-127.0 -173.0,-150.0Q-146.0,-173.0 -146.0,-208.0Q-146.0,-220.0 -150.5,-233.0Q-155.0,-246.0 -168.0,-258.0Q-108.0,-250.0 -84.0,-232.5Q-60.0,-215.0 -60.0,-187.0Q-60.0,-170.0 -68.5,-157.0Q-77.0,-144.0 -101.5,-131.0Q-126.0,-118.0 -174.0,-104.0Q-225.0,-88.0 -252.0,-71.5Q-279.0,-55.0 -279.0,-22.0Q-279.0,-5.0 -269.0,13.0L-213.0,0.0Q-217.0,-8.0 -217.0,-16.0Q-217.0,-26.0 -202.5,-33.0Q-188.0,-40.0 -139.0,-55.0Q-79.0,-73.0 -47.0,-92.5Q-15.0,-112.0 -3.5,-135.0Q8.0,-158.0 8.0,-185.0Q8.0,-232.0 -24.0,-260.5Q-56.0,-289.0 -107.5,-301.0Q-159.0,-313.0 -220.0,-313.0L-244.0,-313.0L-256.0,-264.0Q-229.0,-256.0 -217.0,-243.5Q-205.0,-231.0 -205.0,-214.0Q-205.0,-199.0 -216.0,-189.5Q-227.0,-180.0 -252.0,-180.0Q-292.0,-180.0 -292.0,-204.0Q-292.0,-213.0 -285.0,-227.0L-345.0,-238.0Q-356.0,-218.0 -356.0,-195.0Q-356.0,-166.0 -330.5,-146.5Q-305.0,-127.0 -254.0,-127.0Z" transform="translate(4303, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ট্এ॒ংৠ</span> (Added by SIESTA)</li>


<pre>Expected: ttabeng=0+567|viramabeng=0@-83,0+0|ebeng=2+758|uni0952=2@-124,-313+0|uni25CC=2+510|anusvarabeng=2+389|rrvocalicbeng=5+853</pre>



<pre>Got     : ttabeng=0+567|viramabeng=0@-83,0+0|ebeng=2+758|uni0952=2@-124,-313+0|uni25CC=2+510|anusvarabeng=2+438|rrvocalicbeng=5+853</pre>



<pre>                                                                                                              +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3126 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M395.0,622.0Q394.0,663.0 375.5,681.0Q357.0,699.0 315.0,699.0L221.0,699.0Q156.0,699.0 120.5,708.0Q85.0,717.0 60.0,736.0Q6.0,777.0 6.0,859.0Q6.0,872.0 7.5,884.5Q9.0,897.0 11.0,912.0L85.0,907.0Q81.0,887.0 81.0,869.0Q81.0,847.0 85.5,830.0Q90.0,813.0 100.0,802.0Q114.0,786.0 140.5,778.5Q167.0,771.0 216.0,771.0L294.0,771.0Q347.0,771.0 378.0,763.0Q409.0,755.0 431.0,734.0Q464.0,702.0 467.0,622.0L577.0,622.0L577.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L395.0,622.0Z" transform="translate(0, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(484, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(567, 908)"/>
<path d="M-443.0,-187.0L-443.0,-116.0L-67.0,-116.0L-67.0,-187.0L-443.0,-187.0Z" transform="translate(1201, 595)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1325, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(1835, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(2273, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3077 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M395.0,622.0Q394.0,663.0 375.5,681.0Q357.0,699.0 315.0,699.0L221.0,699.0Q156.0,699.0 120.5,708.0Q85.0,717.0 60.0,736.0Q6.0,777.0 6.0,859.0Q6.0,872.0 7.5,884.5Q9.0,897.0 11.0,912.0L85.0,907.0Q81.0,887.0 81.0,869.0Q81.0,847.0 85.5,830.0Q90.0,813.0 100.0,802.0Q114.0,786.0 140.5,778.5Q167.0,771.0 216.0,771.0L294.0,771.0Q347.0,771.0 378.0,763.0Q409.0,755.0 431.0,734.0Q464.0,702.0 467.0,622.0L577.0,622.0L577.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L395.0,622.0Z" transform="translate(0, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(484, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(567, 908)"/>
<path d="M-443.0,-187.0L-443.0,-116.0L-67.0,-116.0L-67.0,-187.0L-443.0,-187.0Z" transform="translate(1201, 595)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1325, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(1835, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(2224, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ূছ়ফ্ল</span> (Added by SIESTA)</li>


<pre>Expected: uni25CC=0+510|uuvowelsignbeng=0+0|chanuktabeng=1+687|phalabeng=3+824</pre>



<pre>Got     : uni25CC=0+510|uuvowelsignbeng=0@19,3+0|chanuktabeng=1+687|phalabeng=3+824</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2021 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(0, 908)"/>
<path d="M-177.0,-241.0Q-207.0,-241.0 -237.5,-230.5Q-268.0,-220.0 -288.0,-197.0Q-308.0,-174.0 -308.0,-137.0Q-308.0,-87.0 -268.0,-62.0Q-228.0,-37.0 -172.0,-36.0L-172.0,8.0L-95.0,8.0L-95.0,-56.0L-128.0,-102.0Q-135.0,-101.0 -144.5,-100.5Q-154.0,-100.0 -165.0,-100.0Q-235.0,-100.0 -235.0,-140.0Q-235.0,-159.0 -219.0,-169.0Q-203.0,-179.0 -179.0,-179.0Q-137.0,-179.0 -103.0,-159.0Q-69.0,-139.0 -38.0,-102.0Q7.0,-122.0 62.5,-154.0Q118.0,-186.0 163.0,-218.0L121.0,-271.0Q84.0,-243.0 46.0,-220.0Q8.0,-197.0 -22.0,-183.0Q-53.0,-211.0 -91.5,-226.0Q-130.0,-241.0 -177.0,-241.0Z" transform="translate(529, 911)"/>
<path d="M227.0,217.0Q157.0,217.0 125.0,249.0Q110.0,264.0 100.5,288.0Q91.0,312.0 91.0,359.0L91.0,551.0L-10.0,551.0L-10.0,622.0L697.0,622.0L697.0,551.0L168.0,551.0L168.0,544.0Q185.0,525.0 204.0,510.5Q223.0,496.0 251.0,488.5Q279.0,481.0 323.0,481.0L372.0,481.0Q382.0,482.0 397.5,482.5Q413.0,483.0 423.0,483.0Q481.0,483.0 518.5,465.5Q556.0,448.0 577.0,421.0Q598.0,394.0 606.5,364.0Q615.0,334.0 615.0,310.0Q615.0,249.0 589.5,207.5Q564.0,166.0 522.5,141.5Q481.0,117.0 434.0,106.0Q495.0,92.0 555.5,69.5Q616.0,47.0 684.0,11.0L649.0,-49.0Q532.0,14.0 406.5,47.5Q281.0,81.0 143.0,94.0L152.0,166.0Q181.0,160.0 213.5,156.0Q246.0,152.0 290.0,152.0Q379.0,152.0 433.5,175.0Q488.0,198.0 513.0,234.5Q538.0,271.0 538.0,310.0Q538.0,355.0 513.5,382.0Q489.0,409.0 445.0,416.0Q450.0,403.0 450.0,388.0Q450.0,339.0 420.5,300.5Q391.0,262.0 340.5,239.5Q290.0,217.0 227.0,217.0ZM184.0,301.0Q199.0,286.0 233.0,286.0Q276.0,286.0 307.5,302.0Q339.0,318.0 356.5,340.5Q374.0,363.0 374.0,384.0Q374.0,403.0 360.0,408.0Q346.0,413.0 322.0,413.0L316.0,413.0Q269.0,413.0 231.0,428.0Q193.0,443.0 166.0,468.0Q167.0,458.0 167.5,446.0Q168.0,434.0 168.0,420.0L168.0,359.0Q168.0,333.0 172.5,321.0Q177.0,309.0 184.0,301.0ZM339.0,-148.0Q314.0,-148.0 296.5,-132.0Q279.0,-116.0 279.0,-90.0Q279.0,-64.0 296.5,-47.0Q314.0,-30.0 339.0,-30.0Q364.0,-30.0 381.5,-47.0Q399.0,-64.0 399.0,-90.0Q399.0,-116.0 381.5,-132.0Q364.0,-148.0 339.0,-148.0Z" transform="translate(510, 908)"/>
<path d="M176.0,183.0Q223.0,183.0 254.5,162.0Q286.0,141.0 306.0,109.0Q317.0,132.0 334.5,142.5Q352.0,153.0 370.0,153.0Q388.0,153.0 403.5,144.5Q419.0,136.0 434.0,122.0L434.0,143.0Q376.0,191.0 299.0,223.0Q222.0,255.0 115.0,263.0L79.0,351.0Q110.0,370.0 135.0,384.5Q160.0,399.0 186.5,412.0Q213.0,425.0 247.0,441.0Q168.0,494.0 68.0,512.0L86.0,551.0L-10.0,551.0L-10.0,622.0L834.0,622.0L834.0,551.0L185.0,551.0Q229.0,533.0 265.5,508.5Q302.0,484.0 331.0,458.0L336.0,404.0Q290.0,385.0 248.5,365.0Q207.0,345.0 168.0,324.0Q247.0,318.0 314.0,290.5Q381.0,263.0 433.0,223.0Q432.0,240.0 431.5,258.0Q431.0,276.0 431.0,295.0L431.0,510.0L444.0,510.0Q526.0,510.0 600.0,488.5Q674.0,467.0 725.0,414.0Q749.0,389.0 763.5,357.5Q778.0,326.0 778.0,288.0Q778.0,255.0 764.5,225.5Q751.0,196.0 721.0,177.0Q691.0,158.0 641.0,158.0Q626.0,158.0 611.5,159.0Q597.0,160.0 583.0,163.0L588.0,234.0Q594.0,233.0 603.0,232.5Q612.0,232.0 622.0,232.0Q670.0,232.0 685.0,251.0Q700.0,270.0 700.0,296.0Q700.0,347.0 648.5,386.0Q597.0,425.0 508.0,434.0L508.0,-43.0L431.0,-43.0L431.0,62.0Q420.0,72.0 408.0,78.5Q396.0,85.0 383.0,85.0Q368.0,85.0 355.0,73.5Q342.0,62.0 342.0,29.0Q342.0,22.0 342.5,15.5Q343.0,9.0 344.0,3.0L283.0,0.0Q278.0,51.0 252.0,83.0Q226.0,115.0 182.0,115.0Q154.0,115.0 138.5,100.0Q123.0,85.0 123.0,64.0Q123.0,36.0 142.5,18.5Q162.0,1.0 207.0,-16.0L178.0,-84.0Q118.0,-62.0 81.5,-26.5Q45.0,9.0 45.0,68.0Q45.0,118.0 82.0,150.5Q119.0,183.0 176.0,183.0Z" transform="translate(1197, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2021 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(0, 908)"/>
<path d="M-177.0,-241.0Q-207.0,-241.0 -237.5,-230.5Q-268.0,-220.0 -288.0,-197.0Q-308.0,-174.0 -308.0,-137.0Q-308.0,-87.0 -268.0,-62.0Q-228.0,-37.0 -172.0,-36.0L-172.0,8.0L-95.0,8.0L-95.0,-56.0L-128.0,-102.0Q-135.0,-101.0 -144.5,-100.5Q-154.0,-100.0 -165.0,-100.0Q-235.0,-100.0 -235.0,-140.0Q-235.0,-159.0 -219.0,-169.0Q-203.0,-179.0 -179.0,-179.0Q-137.0,-179.0 -103.0,-159.0Q-69.0,-139.0 -38.0,-102.0Q7.0,-122.0 62.5,-154.0Q118.0,-186.0 163.0,-218.0L121.0,-271.0Q84.0,-243.0 46.0,-220.0Q8.0,-197.0 -22.0,-183.0Q-53.0,-211.0 -91.5,-226.0Q-130.0,-241.0 -177.0,-241.0Z" transform="translate(510, 908)"/>
<path d="M227.0,217.0Q157.0,217.0 125.0,249.0Q110.0,264.0 100.5,288.0Q91.0,312.0 91.0,359.0L91.0,551.0L-10.0,551.0L-10.0,622.0L697.0,622.0L697.0,551.0L168.0,551.0L168.0,544.0Q185.0,525.0 204.0,510.5Q223.0,496.0 251.0,488.5Q279.0,481.0 323.0,481.0L372.0,481.0Q382.0,482.0 397.5,482.5Q413.0,483.0 423.0,483.0Q481.0,483.0 518.5,465.5Q556.0,448.0 577.0,421.0Q598.0,394.0 606.5,364.0Q615.0,334.0 615.0,310.0Q615.0,249.0 589.5,207.5Q564.0,166.0 522.5,141.5Q481.0,117.0 434.0,106.0Q495.0,92.0 555.5,69.5Q616.0,47.0 684.0,11.0L649.0,-49.0Q532.0,14.0 406.5,47.5Q281.0,81.0 143.0,94.0L152.0,166.0Q181.0,160.0 213.5,156.0Q246.0,152.0 290.0,152.0Q379.0,152.0 433.5,175.0Q488.0,198.0 513.0,234.5Q538.0,271.0 538.0,310.0Q538.0,355.0 513.5,382.0Q489.0,409.0 445.0,416.0Q450.0,403.0 450.0,388.0Q450.0,339.0 420.5,300.5Q391.0,262.0 340.5,239.5Q290.0,217.0 227.0,217.0ZM184.0,301.0Q199.0,286.0 233.0,286.0Q276.0,286.0 307.5,302.0Q339.0,318.0 356.5,340.5Q374.0,363.0 374.0,384.0Q374.0,403.0 360.0,408.0Q346.0,413.0 322.0,413.0L316.0,413.0Q269.0,413.0 231.0,428.0Q193.0,443.0 166.0,468.0Q167.0,458.0 167.5,446.0Q168.0,434.0 168.0,420.0L168.0,359.0Q168.0,333.0 172.5,321.0Q177.0,309.0 184.0,301.0ZM339.0,-148.0Q314.0,-148.0 296.5,-132.0Q279.0,-116.0 279.0,-90.0Q279.0,-64.0 296.5,-47.0Q314.0,-30.0 339.0,-30.0Q364.0,-30.0 381.5,-47.0Q399.0,-64.0 399.0,-90.0Q399.0,-116.0 381.5,-132.0Q364.0,-148.0 339.0,-148.0Z" transform="translate(510, 908)"/>
<path d="M176.0,183.0Q223.0,183.0 254.5,162.0Q286.0,141.0 306.0,109.0Q317.0,132.0 334.5,142.5Q352.0,153.0 370.0,153.0Q388.0,153.0 403.5,144.5Q419.0,136.0 434.0,122.0L434.0,143.0Q376.0,191.0 299.0,223.0Q222.0,255.0 115.0,263.0L79.0,351.0Q110.0,370.0 135.0,384.5Q160.0,399.0 186.5,412.0Q213.0,425.0 247.0,441.0Q168.0,494.0 68.0,512.0L86.0,551.0L-10.0,551.0L-10.0,622.0L834.0,622.0L834.0,551.0L185.0,551.0Q229.0,533.0 265.5,508.5Q302.0,484.0 331.0,458.0L336.0,404.0Q290.0,385.0 248.5,365.0Q207.0,345.0 168.0,324.0Q247.0,318.0 314.0,290.5Q381.0,263.0 433.0,223.0Q432.0,240.0 431.5,258.0Q431.0,276.0 431.0,295.0L431.0,510.0L444.0,510.0Q526.0,510.0 600.0,488.5Q674.0,467.0 725.0,414.0Q749.0,389.0 763.5,357.5Q778.0,326.0 778.0,288.0Q778.0,255.0 764.5,225.5Q751.0,196.0 721.0,177.0Q691.0,158.0 641.0,158.0Q626.0,158.0 611.5,159.0Q597.0,160.0 583.0,163.0L588.0,234.0Q594.0,233.0 603.0,232.5Q612.0,232.0 622.0,232.0Q670.0,232.0 685.0,251.0Q700.0,270.0 700.0,296.0Q700.0,347.0 648.5,386.0Q597.0,425.0 508.0,434.0L508.0,-43.0L431.0,-43.0L431.0,62.0Q420.0,72.0 408.0,78.5Q396.0,85.0 383.0,85.0Q368.0,85.0 355.0,73.5Q342.0,62.0 342.0,29.0Q342.0,22.0 342.5,15.5Q343.0,9.0 344.0,3.0L283.0,0.0Q278.0,51.0 252.0,83.0Q226.0,115.0 182.0,115.0Q154.0,115.0 138.5,100.0Q123.0,85.0 123.0,64.0Q123.0,36.0 142.5,18.5Q162.0,1.0 207.0,-16.0L178.0,-84.0Q118.0,-62.0 81.5,-26.5Q45.0,9.0 45.0,68.0Q45.0,118.0 82.0,150.5Q119.0,183.0 176.0,183.0Z" transform="translate(1197, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঘ্নঁ꣱ঞঌদৢ</span> (Added by SIESTA)</li>


<pre>Expected: ghanabeng=0+617|candrabindubeng=0+0|uniA8F1=0@0,323+0|nyabeng=5+1001|lvocalicbeng=6+639|dabeng=7+603|lvocalicvowelsignbeng=7@12,0+0</pre>



<pre>Got     : ghanabeng=0+617|candrabindubeng=0+0|uniA8F1=0@0,323+0|nyabeng=5+1019|lvocalicbeng=6+639|dabeng=7+603|lvocalicvowelsignbeng=7@12,0+0</pre>



<pre>                                                                            +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2878 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M236.0,166.0Q300.0,166.0 349.5,139.0Q399.0,112.0 447.0,67.0L447.0,126.0Q401.0,166.0 353.5,193.5Q306.0,221.0 249.0,236.5Q192.0,252.0 117.0,255.0L86.0,333.0Q127.0,360.0 174.0,384.0Q115.0,390.0 84.0,420.0Q53.0,450.0 53.0,492.0Q53.0,524.0 75.0,551.0L-10.0,551.0L-10.0,622.0L627.0,622.0L627.0,551.0L522.0,551.0L522.0,-43.0L445.0,-43.0L445.0,-20.0Q398.0,33.0 347.0,64.0Q296.0,95.0 245.0,95.0Q184.0,95.0 184.0,47.0Q184.0,28.0 199.5,14.5Q215.0,1.0 248.0,-11.0L213.0,-80.0Q164.0,-62.0 133.5,-27.5Q103.0,7.0 103.0,48.0Q103.0,104.0 142.5,135.0Q182.0,166.0 236.0,166.0ZM365.0,421.0Q318.0,397.0 272.5,371.5Q227.0,346.0 189.0,321.0Q269.0,310.0 332.0,282.0Q395.0,254.0 447.0,207.0Q446.0,223.0 445.5,241.0Q445.0,259.0 445.0,281.0L445.0,551.0L164.0,551.0Q133.0,527.0 133.0,494.0Q133.0,464.0 157.0,452.5Q181.0,441.0 212.0,441.0Q236.0,441.0 264.0,450.5Q292.0,460.0 327.0,482.0L365.0,421.0Z" transform="translate(0, 908)"/>
<path d="M-90.0,830.0Q-90.0,810.0 -102.5,799.0Q-115.0,788.0 -134.0,788.0Q-156.0,788.0 -167.0,800.5Q-178.0,813.0 -178.0,833.0Q-178.0,849.0 -167.5,861.0Q-157.0,873.0 -135.0,873.0Q-90.0,873.0 -90.0,830.0ZM42.0,861.0Q35.0,785.0 -5.5,735.0Q-46.0,685.0 -131.0,685.0Q-218.0,685.0 -260.0,735.0Q-302.0,785.0 -310.0,860.0L-241.0,869.0Q-236.0,814.0 -212.0,782.5Q-188.0,751.0 -135.0,751.0Q-39.0,751.0 -28.0,870.0L42.0,861.0Z" transform="translate(617, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(617, 1231)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(617, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0Z" transform="translate(1636, 908)"/>
<path d="M613.0,622.0L613.0,551.0L159.0,551.0L159.0,288.0Q280.0,414.0 475.0,486.0L540.0,422.0Q512.0,370.0 499.5,320.0Q487.0,270.0 487.0,205.0Q487.0,156.0 495.0,111.0Q503.0,66.0 522.0,10.0L447.0,-7.0Q429.0,51.0 419.0,106.5Q409.0,162.0 409.0,222.0Q409.0,276.0 420.0,322.0Q431.0,368.0 445.0,397.0Q365.0,361.0 291.5,306.5Q218.0,252.0 141.0,175.0L82.0,215.0L82.0,551.0L-10.0,551.0L-10.0,622.0L613.0,622.0Z" transform="translate(2275, 908)"/>
<path d="M-254.0,-127.0Q-200.0,-127.0 -173.0,-150.0Q-146.0,-173.0 -146.0,-208.0Q-146.0,-220.0 -150.5,-233.0Q-155.0,-246.0 -168.0,-258.0Q-108.0,-250.0 -84.0,-232.5Q-60.0,-215.0 -60.0,-187.0Q-60.0,-170.0 -68.5,-157.0Q-77.0,-144.0 -101.5,-131.0Q-126.0,-118.0 -174.0,-104.0Q-225.0,-88.0 -252.0,-71.5Q-279.0,-55.0 -279.0,-22.0Q-279.0,-5.0 -269.0,13.0L-213.0,0.0Q-217.0,-8.0 -217.0,-16.0Q-217.0,-26.0 -202.5,-33.0Q-188.0,-40.0 -139.0,-55.0Q-79.0,-73.0 -47.0,-92.5Q-15.0,-112.0 -3.5,-135.0Q8.0,-158.0 8.0,-185.0Q8.0,-232.0 -24.0,-260.5Q-56.0,-289.0 -107.5,-301.0Q-159.0,-313.0 -220.0,-313.0L-244.0,-313.0L-256.0,-264.0Q-229.0,-256.0 -217.0,-243.5Q-205.0,-231.0 -205.0,-214.0Q-205.0,-199.0 -216.0,-189.5Q-227.0,-180.0 -252.0,-180.0Q-292.0,-180.0 -292.0,-204.0Q-292.0,-213.0 -285.0,-227.0L-345.0,-238.0Q-356.0,-218.0 -356.0,-195.0Q-356.0,-166.0 -330.5,-146.5Q-305.0,-127.0 -254.0,-127.0Z" transform="translate(2890, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2860 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M236.0,166.0Q300.0,166.0 349.5,139.0Q399.0,112.0 447.0,67.0L447.0,126.0Q401.0,166.0 353.5,193.5Q306.0,221.0 249.0,236.5Q192.0,252.0 117.0,255.0L86.0,333.0Q127.0,360.0 174.0,384.0Q115.0,390.0 84.0,420.0Q53.0,450.0 53.0,492.0Q53.0,524.0 75.0,551.0L-10.0,551.0L-10.0,622.0L627.0,622.0L627.0,551.0L522.0,551.0L522.0,-43.0L445.0,-43.0L445.0,-20.0Q398.0,33.0 347.0,64.0Q296.0,95.0 245.0,95.0Q184.0,95.0 184.0,47.0Q184.0,28.0 199.5,14.5Q215.0,1.0 248.0,-11.0L213.0,-80.0Q164.0,-62.0 133.5,-27.5Q103.0,7.0 103.0,48.0Q103.0,104.0 142.5,135.0Q182.0,166.0 236.0,166.0ZM365.0,421.0Q318.0,397.0 272.5,371.5Q227.0,346.0 189.0,321.0Q269.0,310.0 332.0,282.0Q395.0,254.0 447.0,207.0Q446.0,223.0 445.5,241.0Q445.0,259.0 445.0,281.0L445.0,551.0L164.0,551.0Q133.0,527.0 133.0,494.0Q133.0,464.0 157.0,452.5Q181.0,441.0 212.0,441.0Q236.0,441.0 264.0,450.5Q292.0,460.0 327.0,482.0L365.0,421.0Z" transform="translate(0, 908)"/>
<path d="M-90.0,830.0Q-90.0,810.0 -102.5,799.0Q-115.0,788.0 -134.0,788.0Q-156.0,788.0 -167.0,800.5Q-178.0,813.0 -178.0,833.0Q-178.0,849.0 -167.5,861.0Q-157.0,873.0 -135.0,873.0Q-90.0,873.0 -90.0,830.0ZM42.0,861.0Q35.0,785.0 -5.5,735.0Q-46.0,685.0 -131.0,685.0Q-218.0,685.0 -260.0,735.0Q-302.0,785.0 -310.0,860.0L-241.0,869.0Q-236.0,814.0 -212.0,782.5Q-188.0,751.0 -135.0,751.0Q-39.0,751.0 -28.0,870.0L42.0,861.0Z" transform="translate(617, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(617, 1231)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(617, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0Z" transform="translate(1618, 908)"/>
<path d="M613.0,622.0L613.0,551.0L159.0,551.0L159.0,288.0Q280.0,414.0 475.0,486.0L540.0,422.0Q512.0,370.0 499.5,320.0Q487.0,270.0 487.0,205.0Q487.0,156.0 495.0,111.0Q503.0,66.0 522.0,10.0L447.0,-7.0Q429.0,51.0 419.0,106.5Q409.0,162.0 409.0,222.0Q409.0,276.0 420.0,322.0Q431.0,368.0 445.0,397.0Q365.0,361.0 291.5,306.5Q218.0,252.0 141.0,175.0L82.0,215.0L82.0,551.0L-10.0,551.0L-10.0,622.0L613.0,622.0Z" transform="translate(2257, 908)"/>
<path d="M-254.0,-127.0Q-200.0,-127.0 -173.0,-150.0Q-146.0,-173.0 -146.0,-208.0Q-146.0,-220.0 -150.5,-233.0Q-155.0,-246.0 -168.0,-258.0Q-108.0,-250.0 -84.0,-232.5Q-60.0,-215.0 -60.0,-187.0Q-60.0,-170.0 -68.5,-157.0Q-77.0,-144.0 -101.5,-131.0Q-126.0,-118.0 -174.0,-104.0Q-225.0,-88.0 -252.0,-71.5Q-279.0,-55.0 -279.0,-22.0Q-279.0,-5.0 -269.0,13.0L-213.0,0.0Q-217.0,-8.0 -217.0,-16.0Q-217.0,-26.0 -202.5,-33.0Q-188.0,-40.0 -139.0,-55.0Q-79.0,-73.0 -47.0,-92.5Q-15.0,-112.0 -3.5,-135.0Q8.0,-158.0 8.0,-185.0Q8.0,-232.0 -24.0,-260.5Q-56.0,-289.0 -107.5,-301.0Q-159.0,-313.0 -220.0,-313.0L-244.0,-313.0L-256.0,-264.0Q-229.0,-256.0 -217.0,-243.5Q-205.0,-231.0 -205.0,-214.0Q-205.0,-199.0 -216.0,-189.5Q-227.0,-180.0 -252.0,-180.0Q-292.0,-180.0 -292.0,-204.0Q-292.0,-213.0 -285.0,-227.0L-345.0,-238.0Q-356.0,-218.0 -356.0,-195.0Q-356.0,-166.0 -330.5,-146.5Q-305.0,-127.0 -254.0,-127.0Z" transform="translate(2872, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঢৄিভঁখ়ভ꣱ৎখ</span> (Added by SIESTA)</li>


<pre>Expected: ivowelsignbeng=0+266|ddhabeng=0+567|rrvocalicvowelsignbeng=0@-83,0+0|bhabeng=3+721|candrabindubeng=3@-165,0+0|khanuktabeng=5+696|bhabeng=7+721|uniA8F1=7@0,323+0|khandatabeng=9+507|khabeng=10+696</pre>



<pre>Got     : ivowelsignbeng=0+266|ddhabeng=0+567|rrvocalicvowelsignbeng=0@-83,0+0|bhabeng=3+721|candrabindubeng=3@-165,0+0|khanuktabeng=5+696|bhabeng=7+721|uniA8F1=7@0,323+0|khandatabeng=9+525|khabeng=10+696</pre>



<pre>                                                                                                                                                                                           ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4192 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L82.0,622.0Q66.0,641.0 49.5,662.0Q33.0,683.0 20.0,704.0Q54.0,763.0 93.0,811.5Q132.0,860.0 185.0,888.5Q238.0,917.0 313.0,917.0Q384.0,917.0 447.0,894.0Q510.0,871.0 573.0,829.5Q636.0,788.0 705.0,731.0L663.0,677.0Q594.0,733.0 538.5,770.0Q483.0,807.0 432.5,825.5Q382.0,844.0 325.0,844.0Q242.0,844.0 192.0,802.0Q142.0,760.0 106.0,693.0Q114.0,678.0 128.0,660.0Q142.0,642.0 160.0,622.0L276.0,622.0Z" transform="translate(0, 908)"/>
<path d="M577.0,622.0L577.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L577.0,622.0Z" transform="translate(266, 908)"/>
<path d="M-355.0,-80.0Q-296.0,-51.0 -233.0,-24.5Q-170.0,2.0 -105.0,25.0L-79.0,-41.0Q-124.0,-54.0 -175.5,-71.5Q-227.0,-89.0 -263.0,-106.0Q-175.0,-121.0 -103.0,-149.0Q-31.0,-177.0 28.0,-211.0L-3.0,-261.0Q-34.0,-244.0 -63.5,-230.5Q-93.0,-217.0 -121.0,-206.0Q-157.0,-218.0 -197.5,-233.5Q-238.0,-249.0 -263.0,-260.0Q-209.0,-268.0 -148.5,-288.0Q-88.0,-308.0 -32.0,-342.0L-63.0,-394.0Q-128.0,-356.0 -190.5,-339.0Q-253.0,-322.0 -323.0,-312.0L-355.0,-238.0Q-320.0,-222.0 -284.5,-206.5Q-249.0,-191.0 -207.0,-178.0Q-234.0,-171.0 -262.0,-167.0Q-290.0,-163.0 -321.0,-160.0L-355.0,-80.0Z" transform="translate(750, 908)"/>
<path d="M731.0,622.0L731.0,551.0L-10.0,551.0L-10.0,622.0L731.0,622.0ZM422.0,43.0Q336.0,43.0 263.0,82.0Q190.0,121.0 131.5,213.0Q73.0,305.0 29.0,465.0L105.0,485.0Q141.0,353.0 186.5,272.5Q232.0,192.0 289.5,155.5Q347.0,119.0 420.0,119.0Q500.0,119.0 544.0,160.5Q588.0,202.0 588.0,267.0Q588.0,303.0 579.0,332.0Q570.0,361.0 555.0,381.0Q520.0,334.0 479.0,309.0Q438.0,284.0 384.0,284.0Q321.0,284.0 285.0,315.5Q249.0,347.0 249.0,402.0Q249.0,425.0 256.0,447.5Q263.0,470.0 271.0,486.0L351.0,462.0Q344.0,452.0 338.0,437.0Q332.0,422.0 332.0,406.0Q332.0,379.0 347.0,367.0Q362.0,355.0 386.0,355.0Q407.0,355.0 428.0,363.0Q449.0,371.0 473.5,394.5Q498.0,418.0 527.0,466.0L590.0,476.0Q664.0,366.0 664.0,266.0Q664.0,203.0 636.0,152.5Q608.0,102.0 554.5,72.5Q501.0,43.0 422.0,43.0Z" transform="translate(833, 908)"/>
<path d="M-90.0,830.0Q-90.0,810.0 -102.5,799.0Q-115.0,788.0 -134.0,788.0Q-156.0,788.0 -167.0,800.5Q-178.0,813.0 -178.0,833.0Q-178.0,849.0 -167.5,861.0Q-157.0,873.0 -135.0,873.0Q-90.0,873.0 -90.0,830.0ZM42.0,861.0Q35.0,785.0 -5.5,735.0Q-46.0,685.0 -131.0,685.0Q-218.0,685.0 -260.0,735.0Q-302.0,785.0 -310.0,860.0L-241.0,869.0Q-236.0,814.0 -212.0,782.5Q-188.0,751.0 -135.0,751.0Q-39.0,751.0 -28.0,870.0L42.0,861.0Z" transform="translate(1389, 908)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0ZM256.0,-6.0Q231.0,-6.0 213.5,10.0Q196.0,26.0 196.0,52.0Q196.0,78.0 213.5,95.0Q231.0,112.0 256.0,112.0Q281.0,112.0 298.5,95.0Q316.0,78.0 316.0,52.0Q316.0,26.0 298.5,10.0Q281.0,-6.0 256.0,-6.0Z" transform="translate(1554, 908)"/>
<path d="M731.0,622.0L731.0,551.0L-10.0,551.0L-10.0,622.0L731.0,622.0ZM422.0,43.0Q336.0,43.0 263.0,82.0Q190.0,121.0 131.5,213.0Q73.0,305.0 29.0,465.0L105.0,485.0Q141.0,353.0 186.5,272.5Q232.0,192.0 289.5,155.5Q347.0,119.0 420.0,119.0Q500.0,119.0 544.0,160.5Q588.0,202.0 588.0,267.0Q588.0,303.0 579.0,332.0Q570.0,361.0 555.0,381.0Q520.0,334.0 479.0,309.0Q438.0,284.0 384.0,284.0Q321.0,284.0 285.0,315.5Q249.0,347.0 249.0,402.0Q249.0,425.0 256.0,447.5Q263.0,470.0 271.0,486.0L351.0,462.0Q344.0,452.0 338.0,437.0Q332.0,422.0 332.0,406.0Q332.0,379.0 347.0,367.0Q362.0,355.0 386.0,355.0Q407.0,355.0 428.0,363.0Q449.0,371.0 473.5,394.5Q498.0,418.0 527.0,466.0L590.0,476.0Q664.0,366.0 664.0,266.0Q664.0,203.0 636.0,152.5Q608.0,102.0 554.5,72.5Q501.0,43.0 422.0,43.0Z" transform="translate(2250, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(2971, 1231)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(2971, 908)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0Z" transform="translate(3496, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4174 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M276.0,622.0L276.0,551.0L171.0,551.0L171.0,0.0L94.0,0.0L94.0,551.0L-10.0,551.0L-10.0,622.0L82.0,622.0Q66.0,641.0 49.5,662.0Q33.0,683.0 20.0,704.0Q54.0,763.0 93.0,811.5Q132.0,860.0 185.0,888.5Q238.0,917.0 313.0,917.0Q384.0,917.0 447.0,894.0Q510.0,871.0 573.0,829.5Q636.0,788.0 705.0,731.0L663.0,677.0Q594.0,733.0 538.5,770.0Q483.0,807.0 432.5,825.5Q382.0,844.0 325.0,844.0Q242.0,844.0 192.0,802.0Q142.0,760.0 106.0,693.0Q114.0,678.0 128.0,660.0Q142.0,642.0 160.0,622.0L276.0,622.0Z" transform="translate(0, 908)"/>
<path d="M577.0,622.0L577.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L577.0,622.0Z" transform="translate(266, 908)"/>
<path d="M-355.0,-80.0Q-296.0,-51.0 -233.0,-24.5Q-170.0,2.0 -105.0,25.0L-79.0,-41.0Q-124.0,-54.0 -175.5,-71.5Q-227.0,-89.0 -263.0,-106.0Q-175.0,-121.0 -103.0,-149.0Q-31.0,-177.0 28.0,-211.0L-3.0,-261.0Q-34.0,-244.0 -63.5,-230.5Q-93.0,-217.0 -121.0,-206.0Q-157.0,-218.0 -197.5,-233.5Q-238.0,-249.0 -263.0,-260.0Q-209.0,-268.0 -148.5,-288.0Q-88.0,-308.0 -32.0,-342.0L-63.0,-394.0Q-128.0,-356.0 -190.5,-339.0Q-253.0,-322.0 -323.0,-312.0L-355.0,-238.0Q-320.0,-222.0 -284.5,-206.5Q-249.0,-191.0 -207.0,-178.0Q-234.0,-171.0 -262.0,-167.0Q-290.0,-163.0 -321.0,-160.0L-355.0,-80.0Z" transform="translate(750, 908)"/>
<path d="M731.0,622.0L731.0,551.0L-10.0,551.0L-10.0,622.0L731.0,622.0ZM422.0,43.0Q336.0,43.0 263.0,82.0Q190.0,121.0 131.5,213.0Q73.0,305.0 29.0,465.0L105.0,485.0Q141.0,353.0 186.5,272.5Q232.0,192.0 289.5,155.5Q347.0,119.0 420.0,119.0Q500.0,119.0 544.0,160.5Q588.0,202.0 588.0,267.0Q588.0,303.0 579.0,332.0Q570.0,361.0 555.0,381.0Q520.0,334.0 479.0,309.0Q438.0,284.0 384.0,284.0Q321.0,284.0 285.0,315.5Q249.0,347.0 249.0,402.0Q249.0,425.0 256.0,447.5Q263.0,470.0 271.0,486.0L351.0,462.0Q344.0,452.0 338.0,437.0Q332.0,422.0 332.0,406.0Q332.0,379.0 347.0,367.0Q362.0,355.0 386.0,355.0Q407.0,355.0 428.0,363.0Q449.0,371.0 473.5,394.5Q498.0,418.0 527.0,466.0L590.0,476.0Q664.0,366.0 664.0,266.0Q664.0,203.0 636.0,152.5Q608.0,102.0 554.5,72.5Q501.0,43.0 422.0,43.0Z" transform="translate(833, 908)"/>
<path d="M-90.0,830.0Q-90.0,810.0 -102.5,799.0Q-115.0,788.0 -134.0,788.0Q-156.0,788.0 -167.0,800.5Q-178.0,813.0 -178.0,833.0Q-178.0,849.0 -167.5,861.0Q-157.0,873.0 -135.0,873.0Q-90.0,873.0 -90.0,830.0ZM42.0,861.0Q35.0,785.0 -5.5,735.0Q-46.0,685.0 -131.0,685.0Q-218.0,685.0 -260.0,735.0Q-302.0,785.0 -310.0,860.0L-241.0,869.0Q-236.0,814.0 -212.0,782.5Q-188.0,751.0 -135.0,751.0Q-39.0,751.0 -28.0,870.0L42.0,861.0Z" transform="translate(1389, 908)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0ZM256.0,-6.0Q231.0,-6.0 213.5,10.0Q196.0,26.0 196.0,52.0Q196.0,78.0 213.5,95.0Q231.0,112.0 256.0,112.0Q281.0,112.0 298.5,95.0Q316.0,78.0 316.0,52.0Q316.0,26.0 298.5,10.0Q281.0,-6.0 256.0,-6.0Z" transform="translate(1554, 908)"/>
<path d="M731.0,622.0L731.0,551.0L-10.0,551.0L-10.0,622.0L731.0,622.0ZM422.0,43.0Q336.0,43.0 263.0,82.0Q190.0,121.0 131.5,213.0Q73.0,305.0 29.0,465.0L105.0,485.0Q141.0,353.0 186.5,272.5Q232.0,192.0 289.5,155.5Q347.0,119.0 420.0,119.0Q500.0,119.0 544.0,160.5Q588.0,202.0 588.0,267.0Q588.0,303.0 579.0,332.0Q570.0,361.0 555.0,381.0Q520.0,334.0 479.0,309.0Q438.0,284.0 384.0,284.0Q321.0,284.0 285.0,315.5Q249.0,347.0 249.0,402.0Q249.0,425.0 256.0,447.5Q263.0,470.0 271.0,486.0L351.0,462.0Q344.0,452.0 338.0,437.0Q332.0,422.0 332.0,406.0Q332.0,379.0 347.0,367.0Q362.0,355.0 386.0,355.0Q407.0,355.0 428.0,363.0Q449.0,371.0 473.5,394.5Q498.0,418.0 527.0,466.0L590.0,476.0Q664.0,366.0 664.0,266.0Q664.0,203.0 636.0,152.5Q608.0,102.0 554.5,72.5Q501.0,43.0 422.0,43.0Z" transform="translate(2250, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(2971, 1231)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(2971, 908)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0Z" transform="translate(3478, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ৠ᳐ৰ‍ূঋগখ꣱ত্ল</span> (Added by SIESTA)</li>


<pre>Expected: rrvocalicbeng=0+853|uni1CD0=0@-172,323+0|ruu1beng=2+769|rvocalicbeng=5+835|gabeng=6+656|khabeng=7+696|uniA8F1=7@0,323+0|talabeng=9+673</pre>



<pre>Got     : rrvocalicbeng=0+853|uni1CD0=0@-172,323+0|ruu1beng=2+769|rvocalicbeng=5+853|gabeng=6+656|khabeng=7+696|uniA8F1=7@0,323+0|talabeng=9+673</pre>



<pre>                                                                                  +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4500 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(0, 908)"/>
<path d="M-430.0,661.0L-289.0,910.0L-228.0,910.0L-77.0,663.0L-131.0,636.0L-255.0,849.0L-371.0,636.0L-430.0,661.0Z" transform="translate(681, 1231)"/>
<path d="M689.0,221.0Q689.0,188.0 695.5,148.5Q702.0,109.0 716.0,68.0L646.0,52.0Q631.0,96.0 623.0,141.5Q615.0,187.0 615.0,224.0Q615.0,256.0 619.5,290.5Q624.0,325.0 635.0,354.0Q604.0,344.0 565.5,328.0Q527.0,312.0 501.0,301.0L501.0,0.0L424.0,0.0Q393.0,60.0 340.5,110.5Q288.0,161.0 220.5,196.0Q153.0,231.0 76.0,243.0L37.0,339.0Q128.0,394.0 224.5,439.0Q321.0,484.0 424.0,517.0L424.0,551.0L-10.0,551.0L-10.0,622.0L779.0,622.0L779.0,551.0L501.0,551.0L501.0,377.0Q536.0,392.0 582.5,409.5Q629.0,427.0 670.0,440.0L728.0,382.0Q705.0,343.0 697.0,301.0Q689.0,259.0 689.0,221.0ZM280.0,383.0Q318.0,370.0 355.0,349.5Q392.0,329.0 424.0,299.0L424.0,440.0Q389.0,428.0 352.5,414.0Q316.0,400.0 280.0,383.0ZM128.0,304.0Q179.0,292.0 236.5,266.0Q294.0,240.0 345.0,200.0Q396.0,160.0 427.0,108.0Q425.0,128.0 424.5,148.5Q424.0,169.0 424.0,190.0L424.0,219.0Q382.0,264.0 327.5,297.0Q273.0,330.0 209.0,349.0Q167.0,327.0 128.0,304.0Z" transform="translate(853, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(1622, 908)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(2475, 908)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0Z" transform="translate(3131, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(3827, 1231)"/>
<path d="M683.0,622.0L683.0,551.0L-10.0,551.0L-10.0,622.0L683.0,622.0ZM214.0,148.0Q255.0,148.0 289.5,131.5Q324.0,115.0 343.0,84.0Q365.0,128.0 416.0,128.0Q436.0,128.0 453.5,121.5Q471.0,115.0 488.0,103.0L488.0,152.0Q488.0,164.0 488.0,177.0Q488.0,190.0 489.0,203.0Q442.0,185.0 379.0,185.0Q301.0,185.0 235.0,215.0Q169.0,245.0 117.5,312.5Q66.0,380.0 29.0,492.0L102.0,513.0Q132.0,426.0 168.0,369.5Q204.0,313.0 255.0,285.5Q306.0,258.0 378.0,258.0Q463.0,258.0 495.5,288.0Q528.0,318.0 528.0,364.0Q528.0,405.0 500.0,432.5Q472.0,460.0 422.0,460.0Q385.0,460.0 368.5,444.5Q352.0,429.0 352.0,406.0Q352.0,399.0 353.5,388.0Q355.0,377.0 358.0,369.0L285.0,355.0Q279.0,372.0 276.5,389.5Q274.0,407.0 274.0,417.0Q274.0,454.0 293.5,478.5Q313.0,503.0 346.0,515.0Q379.0,527.0 417.0,527.0Q477.0,527.0 518.5,503.5Q560.0,480.0 581.5,442.5Q603.0,405.0 603.0,361.0Q603.0,297.0 564.0,253.0L564.0,-77.0L487.0,-77.0L487.0,32.0Q472.0,45.0 458.0,52.5Q444.0,60.0 428.0,60.0Q407.0,60.0 393.0,47.5Q379.0,35.0 379.0,6.0Q379.0,-3.0 379.5,-11.0Q380.0,-19.0 381.0,-26.0L320.0,-29.0Q313.0,23.0 286.5,51.5Q260.0,80.0 221.0,80.0Q192.0,80.0 176.5,65.5Q161.0,51.0 161.0,29.0Q161.0,1.0 180.5,-16.5Q200.0,-34.0 245.0,-51.0L216.0,-119.0Q156.0,-97.0 119.5,-61.5Q83.0,-26.0 83.0,33.0Q83.0,82.0 120.0,115.0Q157.0,148.0 214.0,148.0Z" transform="translate(3827, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4482 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(0, 908)"/>
<path d="M-430.0,661.0L-289.0,910.0L-228.0,910.0L-77.0,663.0L-131.0,636.0L-255.0,849.0L-371.0,636.0L-430.0,661.0Z" transform="translate(681, 1231)"/>
<path d="M689.0,221.0Q689.0,188.0 695.5,148.5Q702.0,109.0 716.0,68.0L646.0,52.0Q631.0,96.0 623.0,141.5Q615.0,187.0 615.0,224.0Q615.0,256.0 619.5,290.5Q624.0,325.0 635.0,354.0Q604.0,344.0 565.5,328.0Q527.0,312.0 501.0,301.0L501.0,0.0L424.0,0.0Q393.0,60.0 340.5,110.5Q288.0,161.0 220.5,196.0Q153.0,231.0 76.0,243.0L37.0,339.0Q128.0,394.0 224.5,439.0Q321.0,484.0 424.0,517.0L424.0,551.0L-10.0,551.0L-10.0,622.0L779.0,622.0L779.0,551.0L501.0,551.0L501.0,377.0Q536.0,392.0 582.5,409.5Q629.0,427.0 670.0,440.0L728.0,382.0Q705.0,343.0 697.0,301.0Q689.0,259.0 689.0,221.0ZM280.0,383.0Q318.0,370.0 355.0,349.5Q392.0,329.0 424.0,299.0L424.0,440.0Q389.0,428.0 352.5,414.0Q316.0,400.0 280.0,383.0ZM128.0,304.0Q179.0,292.0 236.5,266.0Q294.0,240.0 345.0,200.0Q396.0,160.0 427.0,108.0Q425.0,128.0 424.5,148.5Q424.0,169.0 424.0,190.0L424.0,219.0Q382.0,264.0 327.5,297.0Q273.0,330.0 209.0,349.0Q167.0,327.0 128.0,304.0Z" transform="translate(853, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(1622, 908)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(2457, 908)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0Z" transform="translate(3113, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(3809, 1231)"/>
<path d="M683.0,622.0L683.0,551.0L-10.0,551.0L-10.0,622.0L683.0,622.0ZM214.0,148.0Q255.0,148.0 289.5,131.5Q324.0,115.0 343.0,84.0Q365.0,128.0 416.0,128.0Q436.0,128.0 453.5,121.5Q471.0,115.0 488.0,103.0L488.0,152.0Q488.0,164.0 488.0,177.0Q488.0,190.0 489.0,203.0Q442.0,185.0 379.0,185.0Q301.0,185.0 235.0,215.0Q169.0,245.0 117.5,312.5Q66.0,380.0 29.0,492.0L102.0,513.0Q132.0,426.0 168.0,369.5Q204.0,313.0 255.0,285.5Q306.0,258.0 378.0,258.0Q463.0,258.0 495.5,288.0Q528.0,318.0 528.0,364.0Q528.0,405.0 500.0,432.5Q472.0,460.0 422.0,460.0Q385.0,460.0 368.5,444.5Q352.0,429.0 352.0,406.0Q352.0,399.0 353.5,388.0Q355.0,377.0 358.0,369.0L285.0,355.0Q279.0,372.0 276.5,389.5Q274.0,407.0 274.0,417.0Q274.0,454.0 293.5,478.5Q313.0,503.0 346.0,515.0Q379.0,527.0 417.0,527.0Q477.0,527.0 518.5,503.5Q560.0,480.0 581.5,442.5Q603.0,405.0 603.0,361.0Q603.0,297.0 564.0,253.0L564.0,-77.0L487.0,-77.0L487.0,32.0Q472.0,45.0 458.0,52.5Q444.0,60.0 428.0,60.0Q407.0,60.0 393.0,47.5Q379.0,35.0 379.0,6.0Q379.0,-3.0 379.5,-11.0Q380.0,-19.0 381.0,-26.0L320.0,-29.0Q313.0,23.0 286.5,51.5Q260.0,80.0 221.0,80.0Q192.0,80.0 176.5,65.5Q161.0,51.0 161.0,29.0Q161.0,1.0 180.5,-16.5Q200.0,-34.0 245.0,-51.0L216.0,-119.0Q156.0,-97.0 119.5,-61.5Q83.0,-26.0 83.0,33.0Q83.0,82.0 120.0,115.0Q157.0,148.0 214.0,148.0Z" transform="translate(3809, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঙঙষ॑ংঋ</span> (Added by SIESTA)</li>


<pre>Expected: ngabeng=0+705|ngabeng=1+723|ssabeng=2+633|uni0951=2@-62,323+0|uni25CC=2+510|anusvarabeng=2+389|rvocalicbeng=5+853</pre>



<pre>Got     : ngabeng=0+723|ngabeng=1+723|ssabeng=2+633|uni0951=2@-62,323+0|uni25CC=2+510|anusvarabeng=2+438|rvocalicbeng=5+853</pre>



<pre>                     ^^                                                                                +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3880 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(0, 908)"/>
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(723, 908)"/>
<path d="M643.0,622.0L643.0,551.0L538.0,551.0L538.0,0.0L461.0,0.0Q412.0,58.0 360.0,100.5Q308.0,143.0 242.0,171.0Q176.0,199.0 84.0,212.0L48.0,303.0Q95.0,333.0 150.0,362.5Q205.0,392.0 265.0,418.0Q211.0,448.0 155.5,469.5Q100.0,491.0 48.0,502.0L69.0,551.0L-10.0,551.0L-10.0,622.0L643.0,622.0ZM461.0,551.0L132.0,551.0Q190.0,533.0 250.0,503.5Q310.0,474.0 365.0,437.0Q420.0,400.0 463.0,359.0Q462.0,378.0 461.5,397.0Q461.0,416.0 461.0,434.0L461.0,551.0ZM142.0,275.0Q252.0,254.0 327.5,207.5Q403.0,161.0 463.0,99.0Q463.0,116.0 462.0,134.0Q461.0,152.0 461.0,171.0L461.0,270.0Q435.0,298.0 403.5,324.5Q372.0,351.0 337.0,374.0Q288.0,352.0 235.0,326.5Q182.0,301.0 142.0,275.0Z" transform="translate(1446, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(2017, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(2079, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(2589, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(3027, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3813 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(0, 908)"/>
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(705, 908)"/>
<path d="M643.0,622.0L643.0,551.0L538.0,551.0L538.0,0.0L461.0,0.0Q412.0,58.0 360.0,100.5Q308.0,143.0 242.0,171.0Q176.0,199.0 84.0,212.0L48.0,303.0Q95.0,333.0 150.0,362.5Q205.0,392.0 265.0,418.0Q211.0,448.0 155.5,469.5Q100.0,491.0 48.0,502.0L69.0,551.0L-10.0,551.0L-10.0,622.0L643.0,622.0ZM461.0,551.0L132.0,551.0Q190.0,533.0 250.0,503.5Q310.0,474.0 365.0,437.0Q420.0,400.0 463.0,359.0Q462.0,378.0 461.5,397.0Q461.0,416.0 461.0,434.0L461.0,551.0ZM142.0,275.0Q252.0,254.0 327.5,207.5Q403.0,161.0 463.0,99.0Q463.0,116.0 462.0,134.0Q461.0,152.0 461.0,171.0L461.0,270.0Q435.0,298.0 403.5,324.5Q372.0,351.0 337.0,374.0Q288.0,352.0 235.0,326.5Q182.0,301.0 142.0,275.0Z" transform="translate(1428, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(1999, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(2061, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(2571, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(2960, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ৎঋ‘ড়ু</span> (Added by SIESTA)</li>


<pre>Expected: khandatabeng=0+507|rvocalicbeng=1+853|quoteleft.beng=2+312|rrubeng=3+712</pre>



<pre>Got     : khandatabeng=0+525|rvocalicbeng=1+853|quoteleft.beng=2+312|rrubeng=3+712</pre>



<pre>                          ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2402 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(0, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(525, 908)"/>
<path d="M89.0,484.0L82.0,495.0Q96.0,548.0 119.5,611.0Q143.0,674.0 168.0,729.0L235.0,729.0Q220.0,669.0 207.0,602.5Q194.0,536.0 186.0,484.0L89.0,484.0Z" transform="translate(1378, 908)"/>
<path d="M722.0,622.0L722.0,551.0L356.0,551.0L356.0,372.0Q356.0,316.0 393.0,316.0Q422.0,316.0 454.0,343.5Q486.0,371.0 529.0,433.0L589.0,442.0Q621.0,395.0 638.5,345.0Q656.0,295.0 656.0,245.0Q656.0,182.0 628.5,132.0Q601.0,82.0 547.5,53.0Q494.0,24.0 417.0,24.0Q329.0,24.0 257.0,66.0Q185.0,108.0 128.5,205.0Q72.0,302.0 29.0,465.0L105.0,485.0Q141.0,346.0 184.5,261.5Q228.0,177.0 284.0,138.5Q340.0,100.0 413.0,100.0Q493.0,100.0 536.5,140.0Q580.0,180.0 580.0,243.0Q580.0,277.0 573.0,303.5Q566.0,330.0 553.0,349.0Q514.0,295.0 473.5,268.5Q433.0,242.0 394.0,242.0Q346.0,242.0 317.0,268.0Q301.0,282.0 290.0,307.5Q279.0,333.0 279.0,393.0L279.0,551.0L-10.0,551.0L-10.0,622.0L722.0,622.0ZM414.0,-266.0Q387.0,-266.0 355.0,-254.5Q323.0,-243.0 300.5,-218.0Q278.0,-193.0 278.0,-151.0Q278.0,-100.0 317.0,-69.5Q356.0,-39.0 426.0,-39.0Q477.0,-39.0 528.0,-56.0L528.0,8.0L605.0,8.0L605.0,-45.0Q605.0,-54.0 604.5,-65.0Q604.0,-76.0 602.0,-88.0Q647.0,-111.0 692.5,-144.0Q738.0,-177.0 789.0,-217.0L744.0,-271.0Q699.0,-234.0 660.0,-205.0Q621.0,-176.0 586.0,-155.0Q568.0,-199.0 528.5,-232.5Q489.0,-266.0 414.0,-266.0ZM349.0,-153.0Q349.0,-181.0 368.5,-192.5Q388.0,-204.0 414.0,-204.0Q462.0,-204.0 486.0,-179.0Q510.0,-154.0 519.0,-122.0Q469.0,-103.0 421.0,-103.0Q385.0,-103.0 367.0,-117.0Q349.0,-131.0 349.0,-153.0ZM182.0,-92.0Q157.0,-92.0 139.5,-76.0Q122.0,-60.0 122.0,-34.0Q122.0,-8.0 139.5,9.0Q157.0,26.0 182.0,26.0Q207.0,26.0 224.5,9.0Q242.0,-8.0 242.0,-34.0Q242.0,-60.0 224.5,-76.0Q207.0,-92.0 182.0,-92.0Z" transform="translate(1690, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2384 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(0, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(507, 908)"/>
<path d="M89.0,484.0L82.0,495.0Q96.0,548.0 119.5,611.0Q143.0,674.0 168.0,729.0L235.0,729.0Q220.0,669.0 207.0,602.5Q194.0,536.0 186.0,484.0L89.0,484.0Z" transform="translate(1360, 908)"/>
<path d="M722.0,622.0L722.0,551.0L356.0,551.0L356.0,372.0Q356.0,316.0 393.0,316.0Q422.0,316.0 454.0,343.5Q486.0,371.0 529.0,433.0L589.0,442.0Q621.0,395.0 638.5,345.0Q656.0,295.0 656.0,245.0Q656.0,182.0 628.5,132.0Q601.0,82.0 547.5,53.0Q494.0,24.0 417.0,24.0Q329.0,24.0 257.0,66.0Q185.0,108.0 128.5,205.0Q72.0,302.0 29.0,465.0L105.0,485.0Q141.0,346.0 184.5,261.5Q228.0,177.0 284.0,138.5Q340.0,100.0 413.0,100.0Q493.0,100.0 536.5,140.0Q580.0,180.0 580.0,243.0Q580.0,277.0 573.0,303.5Q566.0,330.0 553.0,349.0Q514.0,295.0 473.5,268.5Q433.0,242.0 394.0,242.0Q346.0,242.0 317.0,268.0Q301.0,282.0 290.0,307.5Q279.0,333.0 279.0,393.0L279.0,551.0L-10.0,551.0L-10.0,622.0L722.0,622.0ZM414.0,-266.0Q387.0,-266.0 355.0,-254.5Q323.0,-243.0 300.5,-218.0Q278.0,-193.0 278.0,-151.0Q278.0,-100.0 317.0,-69.5Q356.0,-39.0 426.0,-39.0Q477.0,-39.0 528.0,-56.0L528.0,8.0L605.0,8.0L605.0,-45.0Q605.0,-54.0 604.5,-65.0Q604.0,-76.0 602.0,-88.0Q647.0,-111.0 692.5,-144.0Q738.0,-177.0 789.0,-217.0L744.0,-271.0Q699.0,-234.0 660.0,-205.0Q621.0,-176.0 586.0,-155.0Q568.0,-199.0 528.5,-232.5Q489.0,-266.0 414.0,-266.0ZM349.0,-153.0Q349.0,-181.0 368.5,-192.5Q388.0,-204.0 414.0,-204.0Q462.0,-204.0 486.0,-179.0Q510.0,-154.0 519.0,-122.0Q469.0,-103.0 421.0,-103.0Q385.0,-103.0 367.0,-117.0Q349.0,-131.0 349.0,-153.0ZM182.0,-92.0Q157.0,-92.0 139.5,-76.0Q122.0,-60.0 122.0,-34.0Q122.0,-8.0 139.5,9.0Q157.0,26.0 182.0,26.0Q207.0,26.0 224.5,9.0Q242.0,-8.0 242.0,-34.0Q242.0,-60.0 224.5,-76.0Q207.0,-92.0 182.0,-92.0Z" transform="translate(1672, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">০৾ষ্খ॑ৠঋ</span> (Added by SIESTA)</li>


<pre>Expected: zerobeng=0+592|uni09FE=0@0,323+0|ssahalfbeng=2+505|khabeng=4+696|uni0951=4@-93,323+0|rrvocalicbeng=6+835|rvocalicbeng=7+853</pre>



<pre>Got     : zerobeng=0+592|uni09FE=0@0,323+0|ssahalfbeng=2+505|khabeng=4+696|uni0951=4@-93,323+0|rrvocalicbeng=6+853|rvocalicbeng=7+853</pre>



<pre>                                                                                                                +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3499 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M290.0,91.0Q227.0,91.0 177.5,115.0Q128.0,139.0 100.0,188.5Q72.0,238.0 72.0,313.0Q72.0,372.0 96.0,424.5Q120.0,477.0 170.5,510.5Q221.0,544.0 300.0,544.0Q381.0,544.0 429.0,513.0Q477.0,482.0 498.5,431.5Q520.0,381.0 520.0,320.0Q520.0,261.0 495.5,208.5Q471.0,156.0 420.5,123.5Q370.0,91.0 290.0,91.0ZM301.0,473.0Q237.0,473.0 195.0,430.5Q153.0,388.0 153.0,311.0Q153.0,270.0 166.5,236.0Q180.0,202.0 210.5,182.0Q241.0,162.0 291.0,162.0Q359.0,162.0 399.0,206.5Q439.0,251.0 439.0,324.0Q439.0,393.0 404.5,433.0Q370.0,473.0 301.0,473.0Z" transform="translate(0, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(592, 1231)"/>
<path d="M515.0,622.0L515.0,551.0L445.0,551.0Q476.0,512.0 476.0,453.0Q476.0,390.0 442.0,348.0Q408.0,306.0 354.5,285.0Q301.0,264.0 242.0,264.0Q187.0,264.0 142.5,284.0Q98.0,304.0 72.0,342.5Q46.0,381.0 46.0,436.0Q46.0,472.0 59.0,501.0Q72.0,530.0 94.0,552.0Q80.0,551.0 65.5,551.0Q51.0,551.0 37.0,551.0L-10.0,551.0L-10.0,622.0L515.0,622.0ZM274.0,554.0Q216.0,554.0 176.0,530.0Q293.0,480.0 386.0,403.0Q400.0,427.0 400.0,457.0Q400.0,504.0 368.0,529.0Q336.0,554.0 274.0,554.0ZM122.0,436.0Q122.0,390.0 155.0,362.5Q188.0,335.0 248.0,335.0Q299.0,335.0 338.0,357.0Q243.0,432.0 131.0,480.0Q122.0,460.0 122.0,436.0Z" transform="translate(592, 908)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0Z" transform="translate(1097, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(1700, 1231)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(1793, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(2646, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3481 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M290.0,91.0Q227.0,91.0 177.5,115.0Q128.0,139.0 100.0,188.5Q72.0,238.0 72.0,313.0Q72.0,372.0 96.0,424.5Q120.0,477.0 170.5,510.5Q221.0,544.0 300.0,544.0Q381.0,544.0 429.0,513.0Q477.0,482.0 498.5,431.5Q520.0,381.0 520.0,320.0Q520.0,261.0 495.5,208.5Q471.0,156.0 420.5,123.5Q370.0,91.0 290.0,91.0ZM301.0,473.0Q237.0,473.0 195.0,430.5Q153.0,388.0 153.0,311.0Q153.0,270.0 166.5,236.0Q180.0,202.0 210.5,182.0Q241.0,162.0 291.0,162.0Q359.0,162.0 399.0,206.5Q439.0,251.0 439.0,324.0Q439.0,393.0 404.5,433.0Q370.0,473.0 301.0,473.0Z" transform="translate(0, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(592, 1231)"/>
<path d="M515.0,622.0L515.0,551.0L445.0,551.0Q476.0,512.0 476.0,453.0Q476.0,390.0 442.0,348.0Q408.0,306.0 354.5,285.0Q301.0,264.0 242.0,264.0Q187.0,264.0 142.5,284.0Q98.0,304.0 72.0,342.5Q46.0,381.0 46.0,436.0Q46.0,472.0 59.0,501.0Q72.0,530.0 94.0,552.0Q80.0,551.0 65.5,551.0Q51.0,551.0 37.0,551.0L-10.0,551.0L-10.0,622.0L515.0,622.0ZM274.0,554.0Q216.0,554.0 176.0,530.0Q293.0,480.0 386.0,403.0Q400.0,427.0 400.0,457.0Q400.0,504.0 368.0,529.0Q336.0,554.0 274.0,554.0ZM122.0,436.0Q122.0,390.0 155.0,362.5Q188.0,335.0 248.0,335.0Q299.0,335.0 338.0,357.0Q243.0,432.0 131.0,480.0Q122.0,460.0 122.0,436.0Z" transform="translate(592, 908)"/>
<path d="M182.0,430.0Q121.0,430.0 85.0,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L371.0,625.0Q405.0,594.0 427.5,554.5Q450.0,515.0 450.0,470.0Q450.0,391.0 394.0,345.5Q338.0,300.0 251.0,283.0Q324.0,263.0 376.5,232.0Q429.0,201.0 465.5,166.0Q502.0,131.0 526.0,97.0Q525.0,120.0 524.5,143.0Q524.0,166.0 524.0,193.0L524.0,688.0L577.0,688.0L600.0,622.0L706.0,622.0L706.0,551.0L601.0,551.0L601.0,0.0L524.0,0.0Q486.0,55.0 435.0,103.5Q384.0,152.0 317.5,187.5Q251.0,223.0 166.0,238.0L142.0,331.0Q263.0,340.0 319.0,375.0Q375.0,410.0 375.0,466.0Q375.0,505.0 352.0,535.0Q322.0,487.0 279.5,458.5Q237.0,430.0 182.0,430.0Z" transform="translate(1097, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(1700, 1231)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(1793, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(2628, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">উ᳘গ্ধুঞঌ</span> (Added by SIESTA)</li>


<pre>Expected: ubeng=0+712|uni1CD8=0@-101,-351+0|gadhabeng=2+819|uvowelsignvattubeng=2@-163,0+0|nyabeng=6+1001|lvocalicbeng=7+639</pre>



<pre>Got     : ubeng=0+712|uni1CD8=0@-101,-351+0|gadhabeng=2+819|uvowelsignvattubeng=2@-163,0+0|nyabeng=6+1019|lvocalicbeng=7+639</pre>



<pre>                                                                                                       +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3189 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M508.0,622.0Q507.0,663.0 488.5,681.0Q470.0,699.0 428.0,699.0L288.0,699.0Q223.0,699.0 187.5,708.0Q152.0,717.0 127.0,736.0Q73.0,777.0 73.0,859.0Q73.0,872.0 74.5,885.0Q76.0,898.0 78.0,912.0L152.0,907.0Q150.0,895.0 149.0,886.0Q148.0,877.0 148.0,869.0Q148.0,847.0 152.5,830.0Q157.0,813.0 167.0,802.0Q181.0,786.0 207.0,778.5Q233.0,771.0 283.0,771.0L407.0,771.0Q460.0,771.0 491.0,763.0Q522.0,755.0 544.0,734.0Q577.0,702.0 580.0,622.0L722.0,622.0L722.0,551.0L356.0,551.0L356.0,372.0Q356.0,316.0 393.0,316.0Q422.0,316.0 454.0,343.5Q486.0,371.0 529.0,433.0L589.0,442.0Q621.0,395.0 638.5,345.0Q656.0,295.0 656.0,245.0Q656.0,182.0 628.5,132.0Q601.0,82.0 547.5,53.0Q494.0,24.0 417.0,24.0Q329.0,24.0 257.0,66.0Q185.0,108.0 128.5,205.0Q72.0,302.0 29.0,465.0L105.0,485.0Q141.0,346.0 184.5,261.5Q228.0,177.0 284.0,138.5Q340.0,100.0 413.0,100.0Q493.0,100.0 536.5,140.0Q580.0,180.0 580.0,243.0Q580.0,277.0 573.0,303.5Q566.0,330.0 553.0,349.0Q514.0,295.0 473.5,268.5Q433.0,242.0 394.0,242.0Q346.0,242.0 317.0,268.0Q301.0,282.0 290.0,307.5Q279.0,333.0 279.0,393.0L279.0,551.0L-10.0,551.0L-10.0,622.0L508.0,622.0Z" transform="translate(0, 908)"/>
<path d="M-44.0,-88.0Q-67.0,-188.0 -120.5,-229.5Q-174.0,-271.0 -251.0,-271.0Q-323.0,-271.0 -377.0,-226.5Q-431.0,-182.0 -465.0,-88.0L-394.0,-64.0Q-368.0,-134.0 -334.5,-168.0Q-301.0,-202.0 -248.0,-202.0Q-191.0,-202.0 -163.5,-165.5Q-136.0,-129.0 -120.0,-62.0L-44.0,-88.0Z" transform="translate(611, 557)"/>
<path d="M829.0,622.0L829.0,551.0L561.0,551.0L561.0,317.0Q602.0,332.0 643.0,344.5Q684.0,357.0 720.0,366.0L774.0,311.0Q756.0,268.0 749.0,225.0Q742.0,182.0 742.0,143.0Q742.0,106.0 748.0,70.5Q754.0,35.0 767.0,-7.0L697.0,-24.0Q684.0,21.0 676.0,65.0Q668.0,109.0 668.0,149.0Q668.0,184.0 672.0,216.0Q676.0,248.0 686.0,285.0Q657.0,277.0 624.0,266.0Q591.0,255.0 561.0,244.0L561.0,-43.0L484.0,-43.0Q428.0,15.0 367.0,41.5Q306.0,68.0 234.0,80.0L198.0,159.0Q258.0,195.0 331.0,228.5Q404.0,262.0 484.0,291.0L484.0,391.0Q422.0,476.0 372.5,516.0Q323.0,556.0 260.0,556.0Q213.0,556.0 183.5,537.5Q154.0,519.0 130.0,494.0Q144.0,499.0 162.5,503.0Q181.0,507.0 203.0,507.0Q247.0,507.0 273.0,491.0Q299.0,475.0 311.0,451.5Q323.0,428.0 323.0,404.0Q323.0,355.0 289.5,315.5Q256.0,276.0 168.0,229.0L123.0,299.0Q181.0,325.0 212.0,348.0Q243.0,371.0 243.0,400.0Q243.0,440.0 190.0,440.0Q164.0,440.0 141.5,434.0Q119.0,428.0 93.0,416.0L22.0,473.0Q69.0,544.0 126.5,586.5Q184.0,629.0 255.0,629.0Q323.0,629.0 377.5,596.0Q432.0,563.0 487.0,497.0Q486.0,511.0 485.0,535.5Q484.0,560.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L829.0,622.0ZM484.0,111.0L484.0,219.0Q429.0,198.0 380.0,176.0Q331.0,154.0 291.0,133.0Q346.0,120.0 394.5,98.5Q443.0,77.0 487.0,38.0Q486.0,55.0 485.0,76.5Q484.0,98.0 484.0,111.0Z" transform="translate(712, 908)"/>
<path d="M-286.0,-309.0Q-313.0,-309.0 -345.0,-297.5Q-377.0,-286.0 -399.5,-261.0Q-422.0,-236.0 -422.0,-194.0Q-422.0,-143.0 -383.0,-112.5Q-344.0,-82.0 -274.0,-82.0Q-223.0,-82.0 -172.0,-99.0L-172.0,-35.0L-95.0,-35.0L-95.0,-88.0Q-95.0,-97.0 -95.5,-108.0Q-96.0,-119.0 -98.0,-131.0Q-53.0,-154.0 -7.5,-187.0Q38.0,-220.0 89.0,-260.0L44.0,-314.0Q-1.0,-277.0 -40.0,-248.0Q-79.0,-219.0 -114.0,-198.0Q-132.0,-242.0 -171.5,-275.5Q-211.0,-309.0 -286.0,-309.0ZM-351.0,-196.0Q-351.0,-224.0 -331.5,-235.5Q-312.0,-247.0 -286.0,-247.0Q-238.0,-247.0 -214.0,-222.0Q-190.0,-197.0 -181.0,-165.0Q-231.0,-146.0 -279.0,-146.0Q-315.0,-146.0 -333.0,-160.0Q-351.0,-174.0 -351.0,-196.0Z" transform="translate(1368, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(1531, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0Z" transform="translate(2550, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3171 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M508.0,622.0Q507.0,663.0 488.5,681.0Q470.0,699.0 428.0,699.0L288.0,699.0Q223.0,699.0 187.5,708.0Q152.0,717.0 127.0,736.0Q73.0,777.0 73.0,859.0Q73.0,872.0 74.5,885.0Q76.0,898.0 78.0,912.0L152.0,907.0Q150.0,895.0 149.0,886.0Q148.0,877.0 148.0,869.0Q148.0,847.0 152.5,830.0Q157.0,813.0 167.0,802.0Q181.0,786.0 207.0,778.5Q233.0,771.0 283.0,771.0L407.0,771.0Q460.0,771.0 491.0,763.0Q522.0,755.0 544.0,734.0Q577.0,702.0 580.0,622.0L722.0,622.0L722.0,551.0L356.0,551.0L356.0,372.0Q356.0,316.0 393.0,316.0Q422.0,316.0 454.0,343.5Q486.0,371.0 529.0,433.0L589.0,442.0Q621.0,395.0 638.5,345.0Q656.0,295.0 656.0,245.0Q656.0,182.0 628.5,132.0Q601.0,82.0 547.5,53.0Q494.0,24.0 417.0,24.0Q329.0,24.0 257.0,66.0Q185.0,108.0 128.5,205.0Q72.0,302.0 29.0,465.0L105.0,485.0Q141.0,346.0 184.5,261.5Q228.0,177.0 284.0,138.5Q340.0,100.0 413.0,100.0Q493.0,100.0 536.5,140.0Q580.0,180.0 580.0,243.0Q580.0,277.0 573.0,303.5Q566.0,330.0 553.0,349.0Q514.0,295.0 473.5,268.5Q433.0,242.0 394.0,242.0Q346.0,242.0 317.0,268.0Q301.0,282.0 290.0,307.5Q279.0,333.0 279.0,393.0L279.0,551.0L-10.0,551.0L-10.0,622.0L508.0,622.0Z" transform="translate(0, 908)"/>
<path d="M-44.0,-88.0Q-67.0,-188.0 -120.5,-229.5Q-174.0,-271.0 -251.0,-271.0Q-323.0,-271.0 -377.0,-226.5Q-431.0,-182.0 -465.0,-88.0L-394.0,-64.0Q-368.0,-134.0 -334.5,-168.0Q-301.0,-202.0 -248.0,-202.0Q-191.0,-202.0 -163.5,-165.5Q-136.0,-129.0 -120.0,-62.0L-44.0,-88.0Z" transform="translate(611, 557)"/>
<path d="M829.0,622.0L829.0,551.0L561.0,551.0L561.0,317.0Q602.0,332.0 643.0,344.5Q684.0,357.0 720.0,366.0L774.0,311.0Q756.0,268.0 749.0,225.0Q742.0,182.0 742.0,143.0Q742.0,106.0 748.0,70.5Q754.0,35.0 767.0,-7.0L697.0,-24.0Q684.0,21.0 676.0,65.0Q668.0,109.0 668.0,149.0Q668.0,184.0 672.0,216.0Q676.0,248.0 686.0,285.0Q657.0,277.0 624.0,266.0Q591.0,255.0 561.0,244.0L561.0,-43.0L484.0,-43.0Q428.0,15.0 367.0,41.5Q306.0,68.0 234.0,80.0L198.0,159.0Q258.0,195.0 331.0,228.5Q404.0,262.0 484.0,291.0L484.0,391.0Q422.0,476.0 372.5,516.0Q323.0,556.0 260.0,556.0Q213.0,556.0 183.5,537.5Q154.0,519.0 130.0,494.0Q144.0,499.0 162.5,503.0Q181.0,507.0 203.0,507.0Q247.0,507.0 273.0,491.0Q299.0,475.0 311.0,451.5Q323.0,428.0 323.0,404.0Q323.0,355.0 289.5,315.5Q256.0,276.0 168.0,229.0L123.0,299.0Q181.0,325.0 212.0,348.0Q243.0,371.0 243.0,400.0Q243.0,440.0 190.0,440.0Q164.0,440.0 141.5,434.0Q119.0,428.0 93.0,416.0L22.0,473.0Q69.0,544.0 126.5,586.5Q184.0,629.0 255.0,629.0Q323.0,629.0 377.5,596.0Q432.0,563.0 487.0,497.0Q486.0,511.0 485.0,535.5Q484.0,560.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L829.0,622.0ZM484.0,111.0L484.0,219.0Q429.0,198.0 380.0,176.0Q331.0,154.0 291.0,133.0Q346.0,120.0 394.5,98.5Q443.0,77.0 487.0,38.0Q486.0,55.0 485.0,76.5Q484.0,98.0 484.0,111.0Z" transform="translate(712, 908)"/>
<path d="M-286.0,-309.0Q-313.0,-309.0 -345.0,-297.5Q-377.0,-286.0 -399.5,-261.0Q-422.0,-236.0 -422.0,-194.0Q-422.0,-143.0 -383.0,-112.5Q-344.0,-82.0 -274.0,-82.0Q-223.0,-82.0 -172.0,-99.0L-172.0,-35.0L-95.0,-35.0L-95.0,-88.0Q-95.0,-97.0 -95.5,-108.0Q-96.0,-119.0 -98.0,-131.0Q-53.0,-154.0 -7.5,-187.0Q38.0,-220.0 89.0,-260.0L44.0,-314.0Q-1.0,-277.0 -40.0,-248.0Q-79.0,-219.0 -114.0,-198.0Q-132.0,-242.0 -171.5,-275.5Q-211.0,-309.0 -286.0,-309.0ZM-351.0,-196.0Q-351.0,-224.0 -331.5,-235.5Q-312.0,-247.0 -286.0,-247.0Q-238.0,-247.0 -214.0,-222.0Q-190.0,-197.0 -181.0,-165.0Q-231.0,-146.0 -279.0,-146.0Q-315.0,-146.0 -333.0,-160.0Q-351.0,-174.0 -351.0,-196.0Z" transform="translate(1368, 908)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(1531, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0Z" transform="translate(2532, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ংথভূᳶ꣱ফ্ৰু</span> (Added by SIESTA)</li>


<pre>Expected: uni25CC=0+510|anusvarabeng=0+406|thabeng=1+645|bhabeng=2+721|uuvowelsigntallbeng=2@-115,0+0|uni1CF6=4+628|uniA8F1=4@0,323+0|pharabeng=6+899|uvowelsignlowbeng=6@-221,0+0</pre>



<pre>Got     : uni25CC=0+510|anusvarabeng=0+438|thabeng=1+645|bhabeng=2+721|uuvowelsigntallbeng=2@-115,0+0|uni1CF6=4+628|uniA8F1=4@0,323+0|pharabeng=6+899|uvowelsignlowbeng=6@-221,0+0</pre>



<pre>                                        ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3841 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(0, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(510, 908)"/>
<path d="M211.0,625.0Q306.0,625.0 353.0,578.5Q400.0,532.0 400.0,464.0Q400.0,394.0 348.0,347.0Q296.0,300.0 203.0,282.0Q303.0,253.0 370.5,202.0Q438.0,151.0 475.0,97.0Q474.0,120.0 473.5,143.0Q473.0,166.0 473.0,193.0L473.0,688.0L526.0,688.0L549.0,622.0L655.0,622.0L655.0,551.0L550.0,551.0L550.0,0.0L473.0,0.0Q435.0,55.0 383.0,103.5Q331.0,152.0 264.5,187.5Q198.0,223.0 115.0,238.0L92.0,331.0Q176.0,337.0 226.0,355.5Q276.0,374.0 297.5,402.5Q319.0,431.0 319.0,466.0Q319.0,509.0 291.0,532.0Q263.0,555.0 209.0,555.0Q159.0,555.0 137.5,535.5Q116.0,516.0 116.0,494.0Q116.0,480.0 123.5,468.0Q131.0,456.0 150.0,446.0L106.0,384.0Q78.0,403.0 58.0,430.0Q38.0,457.0 38.0,497.0Q38.0,550.0 83.0,587.5Q128.0,625.0 211.0,625.0Z" transform="translate(948, 908)"/>
<path d="M731.0,622.0L731.0,551.0L-10.0,551.0L-10.0,622.0L731.0,622.0ZM422.0,43.0Q336.0,43.0 263.0,82.0Q190.0,121.0 131.5,213.0Q73.0,305.0 29.0,465.0L105.0,485.0Q141.0,353.0 186.5,272.5Q232.0,192.0 289.5,155.5Q347.0,119.0 420.0,119.0Q500.0,119.0 544.0,160.5Q588.0,202.0 588.0,267.0Q588.0,303.0 579.0,332.0Q570.0,361.0 555.0,381.0Q520.0,334.0 479.0,309.0Q438.0,284.0 384.0,284.0Q321.0,284.0 285.0,315.5Q249.0,347.0 249.0,402.0Q249.0,425.0 256.0,447.5Q263.0,470.0 271.0,486.0L351.0,462.0Q344.0,452.0 338.0,437.0Q332.0,422.0 332.0,406.0Q332.0,379.0 347.0,367.0Q362.0,355.0 386.0,355.0Q407.0,355.0 428.0,363.0Q449.0,371.0 473.5,394.5Q498.0,418.0 527.0,466.0L590.0,476.0Q664.0,366.0 664.0,266.0Q664.0,203.0 636.0,152.5Q608.0,102.0 554.5,72.5Q501.0,43.0 422.0,43.0Z" transform="translate(1593, 908)"/>
<path d="M-177.0,-241.0Q-207.0,-241.0 -237.5,-230.5Q-268.0,-220.0 -288.0,-197.0Q-308.0,-174.0 -308.0,-137.0Q-308.0,-87.0 -268.0,-62.0Q-228.0,-37.0 -172.0,-36.0L-172.0,81.0L-101.0,81.0L-101.0,-64.0L-128.0,-102.0Q-135.0,-101.0 -144.5,-100.5Q-154.0,-100.0 -165.0,-100.0Q-235.0,-100.0 -235.0,-140.0Q-235.0,-159.0 -219.0,-169.0Q-203.0,-179.0 -179.0,-179.0Q-137.0,-179.0 -103.0,-159.0Q-69.0,-139.0 -38.0,-102.0Q7.0,-122.0 62.5,-154.0Q118.0,-186.0 163.0,-218.0L121.0,-271.0Q84.0,-243.0 46.0,-220.0Q8.0,-197.0 -22.0,-183.0Q-53.0,-211.0 -91.5,-226.0Q-130.0,-241.0 -177.0,-241.0Z" transform="translate(2199, 908)"/>
<path d="M198.0,195.0Q153.0,195.0 120.5,214.0Q88.0,233.0 69.5,282.0Q51.0,331.0 47.0,422.0L126.0,427.0Q128.0,359.0 136.5,324.5Q145.0,290.0 161.5,278.0Q178.0,266.0 202.0,266.0Q245.0,266.0 259.5,300.5Q274.0,335.0 277.0,423.0L351.0,423.0Q354.0,335.0 370.0,300.5Q386.0,266.0 427.0,266.0Q449.0,266.0 465.0,278.5Q481.0,291.0 490.5,325.5Q500.0,360.0 502.0,427.0L581.0,422.0Q578.0,331.0 559.5,282.0Q541.0,233.0 508.5,214.0Q476.0,195.0 431.0,195.0Q387.0,195.0 359.5,214.0Q332.0,233.0 314.0,279.0Q296.0,233.0 268.5,214.0Q241.0,195.0 198.0,195.0Z" transform="translate(2314, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(2942, 1231)"/>
<path d="M583.0,-117.0L508.0,-117.0Q484.0,-30.0 395.0,-30.0Q349.0,-30.0 311.0,-38.5Q273.0,-47.0 226.0,-47.0Q184.0,-47.0 142.5,-33.5Q101.0,-20.0 73.5,13.5Q46.0,47.0 46.0,108.0Q46.0,128.0 49.0,145.5Q52.0,163.0 55.0,174.0L132.0,165.0Q128.0,152.0 126.0,139.0Q124.0,126.0 124.0,111.0Q124.0,61.0 152.0,43.0Q180.0,25.0 223.0,25.0Q254.0,25.0 278.0,29.5Q302.0,34.0 325.0,38.0Q348.0,42.0 375.0,42.0Q462.0,42.0 508.0,-19.0L508.0,12.0Q465.0,66.0 415.0,105.0Q365.0,144.0 299.5,170.0Q234.0,196.0 145.0,212.0L109.0,303.0Q155.0,334.0 208.0,362.0Q261.0,390.0 313.0,414.0Q275.0,443.0 225.5,465.5Q176.0,488.0 109.0,502.0L131.0,551.0L-10.0,551.0L-10.0,622.0L909.0,622.0L909.0,551.0L205.0,551.0Q242.0,538.0 279.0,518.0Q316.0,498.0 347.0,475.0Q378.0,452.0 397.0,432.0L402.0,376.0Q353.0,354.0 299.0,327.5Q245.0,301.0 203.0,276.0Q273.0,259.0 326.5,236.5Q380.0,214.0 423.5,182.5Q467.0,151.0 508.0,107.0Q507.0,124.0 506.5,142.0Q506.0,160.0 506.0,179.0L506.0,510.0L519.0,510.0Q601.0,510.0 675.0,488.5Q749.0,467.0 800.0,414.0Q824.0,389.0 838.5,357.5Q853.0,326.0 853.0,288.0Q853.0,255.0 839.5,225.5Q826.0,196.0 796.0,177.0Q766.0,158.0 716.0,158.0Q701.0,158.0 686.5,159.0Q672.0,160.0 658.0,163.0L663.0,234.0Q669.0,233.0 678.0,232.5Q687.0,232.0 697.0,232.0Q746.0,232.0 760.5,251.0Q775.0,270.0 775.0,296.0Q775.0,347.0 723.5,386.0Q672.0,425.0 583.0,434.0L583.0,-117.0Z" transform="translate(2942, 908)"/>
<path d="M-286.0,-383.0Q-313.0,-383.0 -345.0,-371.5Q-377.0,-360.0 -399.5,-335.0Q-422.0,-310.0 -422.0,-268.0Q-422.0,-217.0 -383.0,-186.5Q-344.0,-156.0 -274.0,-156.0Q-223.0,-156.0 -172.0,-173.0L-172.0,-109.0L-95.0,-109.0L-95.0,-162.0Q-95.0,-171.0 -95.5,-182.0Q-96.0,-193.0 -98.0,-205.0Q-53.0,-228.0 -7.5,-261.0Q38.0,-294.0 89.0,-334.0L44.0,-388.0Q-1.0,-351.0 -40.0,-322.0Q-79.0,-293.0 -114.0,-272.0Q-132.0,-316.0 -171.5,-349.5Q-211.0,-383.0 -286.0,-383.0ZM-351.0,-270.0Q-351.0,-298.0 -331.5,-309.5Q-312.0,-321.0 -286.0,-321.0Q-238.0,-321.0 -214.0,-296.0Q-190.0,-271.0 -181.0,-239.0Q-231.0,-220.0 -279.0,-220.0Q-315.0,-220.0 -333.0,-234.0Q-351.0,-248.0 -351.0,-270.0Z" transform="translate(3620, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3809 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(0, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(510, 908)"/>
<path d="M211.0,625.0Q306.0,625.0 353.0,578.5Q400.0,532.0 400.0,464.0Q400.0,394.0 348.0,347.0Q296.0,300.0 203.0,282.0Q303.0,253.0 370.5,202.0Q438.0,151.0 475.0,97.0Q474.0,120.0 473.5,143.0Q473.0,166.0 473.0,193.0L473.0,688.0L526.0,688.0L549.0,622.0L655.0,622.0L655.0,551.0L550.0,551.0L550.0,0.0L473.0,0.0Q435.0,55.0 383.0,103.5Q331.0,152.0 264.5,187.5Q198.0,223.0 115.0,238.0L92.0,331.0Q176.0,337.0 226.0,355.5Q276.0,374.0 297.5,402.5Q319.0,431.0 319.0,466.0Q319.0,509.0 291.0,532.0Q263.0,555.0 209.0,555.0Q159.0,555.0 137.5,535.5Q116.0,516.0 116.0,494.0Q116.0,480.0 123.5,468.0Q131.0,456.0 150.0,446.0L106.0,384.0Q78.0,403.0 58.0,430.0Q38.0,457.0 38.0,497.0Q38.0,550.0 83.0,587.5Q128.0,625.0 211.0,625.0Z" transform="translate(916, 908)"/>
<path d="M731.0,622.0L731.0,551.0L-10.0,551.0L-10.0,622.0L731.0,622.0ZM422.0,43.0Q336.0,43.0 263.0,82.0Q190.0,121.0 131.5,213.0Q73.0,305.0 29.0,465.0L105.0,485.0Q141.0,353.0 186.5,272.5Q232.0,192.0 289.5,155.5Q347.0,119.0 420.0,119.0Q500.0,119.0 544.0,160.5Q588.0,202.0 588.0,267.0Q588.0,303.0 579.0,332.0Q570.0,361.0 555.0,381.0Q520.0,334.0 479.0,309.0Q438.0,284.0 384.0,284.0Q321.0,284.0 285.0,315.5Q249.0,347.0 249.0,402.0Q249.0,425.0 256.0,447.5Q263.0,470.0 271.0,486.0L351.0,462.0Q344.0,452.0 338.0,437.0Q332.0,422.0 332.0,406.0Q332.0,379.0 347.0,367.0Q362.0,355.0 386.0,355.0Q407.0,355.0 428.0,363.0Q449.0,371.0 473.5,394.5Q498.0,418.0 527.0,466.0L590.0,476.0Q664.0,366.0 664.0,266.0Q664.0,203.0 636.0,152.5Q608.0,102.0 554.5,72.5Q501.0,43.0 422.0,43.0Z" transform="translate(1561, 908)"/>
<path d="M-177.0,-241.0Q-207.0,-241.0 -237.5,-230.5Q-268.0,-220.0 -288.0,-197.0Q-308.0,-174.0 -308.0,-137.0Q-308.0,-87.0 -268.0,-62.0Q-228.0,-37.0 -172.0,-36.0L-172.0,81.0L-101.0,81.0L-101.0,-64.0L-128.0,-102.0Q-135.0,-101.0 -144.5,-100.5Q-154.0,-100.0 -165.0,-100.0Q-235.0,-100.0 -235.0,-140.0Q-235.0,-159.0 -219.0,-169.0Q-203.0,-179.0 -179.0,-179.0Q-137.0,-179.0 -103.0,-159.0Q-69.0,-139.0 -38.0,-102.0Q7.0,-122.0 62.5,-154.0Q118.0,-186.0 163.0,-218.0L121.0,-271.0Q84.0,-243.0 46.0,-220.0Q8.0,-197.0 -22.0,-183.0Q-53.0,-211.0 -91.5,-226.0Q-130.0,-241.0 -177.0,-241.0Z" transform="translate(2167, 908)"/>
<path d="M198.0,195.0Q153.0,195.0 120.5,214.0Q88.0,233.0 69.5,282.0Q51.0,331.0 47.0,422.0L126.0,427.0Q128.0,359.0 136.5,324.5Q145.0,290.0 161.5,278.0Q178.0,266.0 202.0,266.0Q245.0,266.0 259.5,300.5Q274.0,335.0 277.0,423.0L351.0,423.0Q354.0,335.0 370.0,300.5Q386.0,266.0 427.0,266.0Q449.0,266.0 465.0,278.5Q481.0,291.0 490.5,325.5Q500.0,360.0 502.0,427.0L581.0,422.0Q578.0,331.0 559.5,282.0Q541.0,233.0 508.5,214.0Q476.0,195.0 431.0,195.0Q387.0,195.0 359.5,214.0Q332.0,233.0 314.0,279.0Q296.0,233.0 268.5,214.0Q241.0,195.0 198.0,195.0Z" transform="translate(2282, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(2910, 1231)"/>
<path d="M583.0,-117.0L508.0,-117.0Q484.0,-30.0 395.0,-30.0Q349.0,-30.0 311.0,-38.5Q273.0,-47.0 226.0,-47.0Q184.0,-47.0 142.5,-33.5Q101.0,-20.0 73.5,13.5Q46.0,47.0 46.0,108.0Q46.0,128.0 49.0,145.5Q52.0,163.0 55.0,174.0L132.0,165.0Q128.0,152.0 126.0,139.0Q124.0,126.0 124.0,111.0Q124.0,61.0 152.0,43.0Q180.0,25.0 223.0,25.0Q254.0,25.0 278.0,29.5Q302.0,34.0 325.0,38.0Q348.0,42.0 375.0,42.0Q462.0,42.0 508.0,-19.0L508.0,12.0Q465.0,66.0 415.0,105.0Q365.0,144.0 299.5,170.0Q234.0,196.0 145.0,212.0L109.0,303.0Q155.0,334.0 208.0,362.0Q261.0,390.0 313.0,414.0Q275.0,443.0 225.5,465.5Q176.0,488.0 109.0,502.0L131.0,551.0L-10.0,551.0L-10.0,622.0L909.0,622.0L909.0,551.0L205.0,551.0Q242.0,538.0 279.0,518.0Q316.0,498.0 347.0,475.0Q378.0,452.0 397.0,432.0L402.0,376.0Q353.0,354.0 299.0,327.5Q245.0,301.0 203.0,276.0Q273.0,259.0 326.5,236.5Q380.0,214.0 423.5,182.5Q467.0,151.0 508.0,107.0Q507.0,124.0 506.5,142.0Q506.0,160.0 506.0,179.0L506.0,510.0L519.0,510.0Q601.0,510.0 675.0,488.5Q749.0,467.0 800.0,414.0Q824.0,389.0 838.5,357.5Q853.0,326.0 853.0,288.0Q853.0,255.0 839.5,225.5Q826.0,196.0 796.0,177.0Q766.0,158.0 716.0,158.0Q701.0,158.0 686.5,159.0Q672.0,160.0 658.0,163.0L663.0,234.0Q669.0,233.0 678.0,232.5Q687.0,232.0 697.0,232.0Q746.0,232.0 760.5,251.0Q775.0,270.0 775.0,296.0Q775.0,347.0 723.5,386.0Q672.0,425.0 583.0,434.0L583.0,-117.0Z" transform="translate(2910, 908)"/>
<path d="M-286.0,-383.0Q-313.0,-383.0 -345.0,-371.5Q-377.0,-360.0 -399.5,-335.0Q-422.0,-310.0 -422.0,-268.0Q-422.0,-217.0 -383.0,-186.5Q-344.0,-156.0 -274.0,-156.0Q-223.0,-156.0 -172.0,-173.0L-172.0,-109.0L-95.0,-109.0L-95.0,-162.0Q-95.0,-171.0 -95.5,-182.0Q-96.0,-193.0 -98.0,-205.0Q-53.0,-228.0 -7.5,-261.0Q38.0,-294.0 89.0,-334.0L44.0,-388.0Q-1.0,-351.0 -40.0,-322.0Q-79.0,-293.0 -114.0,-272.0Q-132.0,-316.0 -171.5,-349.5Q-211.0,-383.0 -286.0,-383.0ZM-351.0,-270.0Q-351.0,-298.0 -331.5,-309.5Q-312.0,-321.0 -286.0,-321.0Q-238.0,-321.0 -214.0,-296.0Q-190.0,-271.0 -181.0,-239.0Q-231.0,-220.0 -279.0,-220.0Q-315.0,-220.0 -333.0,-234.0Q-351.0,-248.0 -351.0,-270.0Z" transform="translate(3588, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ংপগৄ</span> (Added by SIESTA)</li>


<pre>Expected: uni25CC=0+510|anusvarabeng=0+406|pabeng=1+716|gabeng=2+656|rrvocalicvowelsignbeng=2+0</pre>



<pre>Got     : uni25CC=0+510|anusvarabeng=0+438|pabeng=1+716|gabeng=2+656|rrvocalicvowelsignbeng=2+0</pre>



<pre>                                        ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2320 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(0, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(510, 908)"/>
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(948, 908)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(1664, 908)"/>
<path d="M-355.0,-80.0Q-296.0,-51.0 -233.0,-24.5Q-170.0,2.0 -105.0,25.0L-79.0,-41.0Q-124.0,-54.0 -175.5,-71.5Q-227.0,-89.0 -263.0,-106.0Q-175.0,-121.0 -103.0,-149.0Q-31.0,-177.0 28.0,-211.0L-3.0,-261.0Q-34.0,-244.0 -63.5,-230.5Q-93.0,-217.0 -121.0,-206.0Q-157.0,-218.0 -197.5,-233.5Q-238.0,-249.0 -263.0,-260.0Q-209.0,-268.0 -148.5,-288.0Q-88.0,-308.0 -32.0,-342.0L-63.0,-394.0Q-128.0,-356.0 -190.5,-339.0Q-253.0,-322.0 -323.0,-312.0L-355.0,-238.0Q-320.0,-222.0 -284.5,-206.5Q-249.0,-191.0 -207.0,-178.0Q-234.0,-171.0 -262.0,-167.0Q-290.0,-163.0 -321.0,-160.0L-355.0,-80.0Z" transform="translate(2320, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2288 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(0, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(510, 908)"/>
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(916, 908)"/>
<path d="M484.0,0.0L484.0,391.0Q423.0,476.0 372.5,516.0Q322.0,556.0 263.0,556.0Q210.0,556.0 177.5,529.0Q145.0,502.0 122.0,468.0Q138.0,477.0 162.5,482.0Q187.0,487.0 216.0,487.0Q262.0,487.0 290.5,469.0Q319.0,451.0 332.5,423.5Q346.0,396.0 346.0,369.0Q346.0,310.0 306.0,263.5Q266.0,217.0 182.0,172.0L131.0,245.0Q186.0,268.0 226.0,296.5Q266.0,325.0 266.0,365.0Q266.0,387.0 249.0,402.0Q232.0,417.0 200.0,417.0Q174.0,417.0 151.5,411.0Q129.0,405.0 103.0,392.0L22.0,458.0Q68.0,536.0 124.5,582.5Q181.0,629.0 255.0,629.0Q323.0,629.0 377.5,595.5Q432.0,562.0 487.0,496.0Q486.0,513.0 485.0,537.0Q484.0,561.0 484.0,585.0L484.0,688.0L537.0,688.0L560.0,622.0L666.0,622.0L666.0,551.0L561.0,551.0L561.0,0.0L484.0,0.0Z" transform="translate(1632, 908)"/>
<path d="M-355.0,-80.0Q-296.0,-51.0 -233.0,-24.5Q-170.0,2.0 -105.0,25.0L-79.0,-41.0Q-124.0,-54.0 -175.5,-71.5Q-227.0,-89.0 -263.0,-106.0Q-175.0,-121.0 -103.0,-149.0Q-31.0,-177.0 28.0,-211.0L-3.0,-261.0Q-34.0,-244.0 -63.5,-230.5Q-93.0,-217.0 -121.0,-206.0Q-157.0,-218.0 -197.5,-233.5Q-238.0,-249.0 -263.0,-260.0Q-209.0,-268.0 -148.5,-288.0Q-88.0,-308.0 -32.0,-342.0L-63.0,-394.0Q-128.0,-356.0 -190.5,-339.0Q-253.0,-322.0 -323.0,-312.0L-355.0,-238.0Q-320.0,-222.0 -284.5,-206.5Q-249.0,-191.0 -207.0,-178.0Q-234.0,-171.0 -262.0,-167.0Q-290.0,-163.0 -321.0,-160.0L-355.0,-80.0Z" transform="translate(2288, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">এঋর‍ূ</span> (Added by SIESTA)</li>


<pre>Expected: ebeng=0+740|rvocalicbeng=1+853|ruubeng=2+769</pre>



<pre>Got     : ebeng=0+758|rvocalicbeng=1+853|ruubeng=2+769</pre>



<pre>                   ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2380 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(0, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(758, 908)"/>
<path d="M689.0,221.0Q689.0,188.0 695.5,148.5Q702.0,109.0 716.0,68.0L646.0,52.0Q631.0,96.0 623.0,141.5Q615.0,187.0 615.0,224.0Q615.0,256.0 619.5,290.5Q624.0,325.0 635.0,354.0Q604.0,344.0 565.5,328.0Q527.0,312.0 501.0,301.0L501.0,0.0L424.0,0.0Q394.0,60.0 341.5,110.5Q289.0,161.0 221.0,196.0Q153.0,231.0 76.0,243.0L37.0,339.0Q128.0,394.0 224.5,439.0Q321.0,484.0 424.0,517.0L424.0,551.0L-10.0,551.0L-10.0,622.0L779.0,622.0L779.0,551.0L501.0,551.0L501.0,377.0Q536.0,392.0 582.5,409.5Q629.0,427.0 670.0,440.0L728.0,382.0Q705.0,343.0 697.0,301.0Q689.0,259.0 689.0,221.0ZM130.0,304.0Q181.0,293.0 238.0,266.5Q295.0,240.0 345.5,200.0Q396.0,160.0 427.0,108.0Q426.0,126.0 425.0,145.0Q424.0,164.0 424.0,189.0L424.0,439.0Q352.0,414.0 274.0,379.5Q196.0,345.0 130.0,304.0ZM185.0,-6.0Q160.0,-6.0 142.5,10.0Q125.0,26.0 125.0,52.0Q125.0,78.0 142.5,95.0Q160.0,112.0 185.0,112.0Q210.0,112.0 227.5,95.0Q245.0,78.0 245.0,52.0Q245.0,26.0 227.5,10.0Q210.0,-6.0 185.0,-6.0Z" transform="translate(1611, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2362 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(0, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(740, 908)"/>
<path d="M689.0,221.0Q689.0,188.0 695.5,148.5Q702.0,109.0 716.0,68.0L646.0,52.0Q631.0,96.0 623.0,141.5Q615.0,187.0 615.0,224.0Q615.0,256.0 619.5,290.5Q624.0,325.0 635.0,354.0Q604.0,344.0 565.5,328.0Q527.0,312.0 501.0,301.0L501.0,0.0L424.0,0.0Q394.0,60.0 341.5,110.5Q289.0,161.0 221.0,196.0Q153.0,231.0 76.0,243.0L37.0,339.0Q128.0,394.0 224.5,439.0Q321.0,484.0 424.0,517.0L424.0,551.0L-10.0,551.0L-10.0,622.0L779.0,622.0L779.0,551.0L501.0,551.0L501.0,377.0Q536.0,392.0 582.5,409.5Q629.0,427.0 670.0,440.0L728.0,382.0Q705.0,343.0 697.0,301.0Q689.0,259.0 689.0,221.0ZM130.0,304.0Q181.0,293.0 238.0,266.5Q295.0,240.0 345.5,200.0Q396.0,160.0 427.0,108.0Q426.0,126.0 425.0,145.0Q424.0,164.0 424.0,189.0L424.0,439.0Q352.0,414.0 274.0,379.5Q196.0,345.0 130.0,304.0ZM185.0,-6.0Q160.0,-6.0 142.5,10.0Q125.0,26.0 125.0,52.0Q125.0,78.0 142.5,95.0Q160.0,112.0 185.0,112.0Q210.0,112.0 227.5,95.0Q245.0,78.0 245.0,52.0Q245.0,26.0 227.5,10.0Q210.0,-6.0 185.0,-6.0Z" transform="translate(1593, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">প্্꣱ষ্প॒</span> (Added by SIESTA)</li>


<pre>Expected: pabeng=0+716|viramabeng=0+0|uni25CC=0+510|viramabeng=0+0|uniA8F1=0@0,323+0|ssapabeng=4+1075|uni0952=4@-283,-313+0</pre>



<pre>Got     : pabeng=0+716|viramabeng=0+0|uni25CC=0+510|viramabeng=0@19,3+0|uniA8F1=0@0,323+0|ssapabeng=4+1075|uni0952=4@-283,-313+0</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2301 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(0, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(716, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(716, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(1245, 911)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(1226, 1231)"/>
<path d="M242.0,264.0Q187.0,264.0 142.5,284.0Q98.0,304.0 72.0,342.5Q46.0,381.0 46.0,436.0Q46.0,472.0 59.0,501.0Q72.0,530.0 94.0,552.0Q80.0,551.0 65.5,551.0Q51.0,551.0 37.0,551.0L-10.0,551.0L-10.0,622.0L326.0,622.0Q369.0,613.0 402.5,592.0Q436.0,571.0 455.0,536.0Q498.0,578.0 546.0,603.5Q594.0,629.0 650.0,629.0Q726.0,629.0 784.5,588.5Q843.0,548.0 906.0,468.0Q904.0,488.0 903.5,510.5Q903.0,533.0 903.0,558.0L903.0,688.0L956.0,688.0L979.0,622.0L1085.0,622.0L1085.0,551.0L980.0,551.0L980.0,0.0L903.0,0.0L903.0,363.0Q887.0,385.0 873.0,404.5Q859.0,424.0 845.0,440.0L585.0,195.0L526.0,250.0L555.0,277.0Q565.0,291.0 571.5,307.0Q578.0,323.0 578.0,343.0Q578.0,368.0 563.0,383.0Q548.0,398.0 519.0,398.0Q486.0,398.0 458.0,381.0Q433.0,322.0 372.0,293.0Q311.0,264.0 242.0,264.0ZM645.0,356.0Q645.0,352.0 645.0,348.0Q657.0,361.0 669.5,373.5Q682.0,386.0 696.0,400.0L796.0,494.0Q730.0,556.0 657.0,556.0Q599.0,556.0 556.0,525.0Q513.0,494.0 479.0,452.0Q505.0,465.0 533.0,465.0Q591.0,465.0 618.0,433.5Q645.0,402.0 645.0,356.0ZM274.0,554.0Q216.0,554.0 176.0,530.0Q293.0,480.0 386.0,403.0Q400.0,428.0 400.0,457.0Q400.0,504.0 368.0,529.0Q336.0,554.0 274.0,554.0ZM122.0,436.0Q122.0,390.0 155.0,362.5Q188.0,335.0 248.0,335.0Q299.0,335.0 338.0,357.0Q243.0,432.0 131.0,480.0Q122.0,460.0 122.0,436.0Z" transform="translate(1226, 908)"/>
<path d="M-443.0,-187.0L-443.0,-116.0L-67.0,-116.0L-67.0,-187.0L-443.0,-187.0Z" transform="translate(2018, 595)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2301 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(0, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(716, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(716, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(1226, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(1226, 1231)"/>
<path d="M242.0,264.0Q187.0,264.0 142.5,284.0Q98.0,304.0 72.0,342.5Q46.0,381.0 46.0,436.0Q46.0,472.0 59.0,501.0Q72.0,530.0 94.0,552.0Q80.0,551.0 65.5,551.0Q51.0,551.0 37.0,551.0L-10.0,551.0L-10.0,622.0L326.0,622.0Q369.0,613.0 402.5,592.0Q436.0,571.0 455.0,536.0Q498.0,578.0 546.0,603.5Q594.0,629.0 650.0,629.0Q726.0,629.0 784.5,588.5Q843.0,548.0 906.0,468.0Q904.0,488.0 903.5,510.5Q903.0,533.0 903.0,558.0L903.0,688.0L956.0,688.0L979.0,622.0L1085.0,622.0L1085.0,551.0L980.0,551.0L980.0,0.0L903.0,0.0L903.0,363.0Q887.0,385.0 873.0,404.5Q859.0,424.0 845.0,440.0L585.0,195.0L526.0,250.0L555.0,277.0Q565.0,291.0 571.5,307.0Q578.0,323.0 578.0,343.0Q578.0,368.0 563.0,383.0Q548.0,398.0 519.0,398.0Q486.0,398.0 458.0,381.0Q433.0,322.0 372.0,293.0Q311.0,264.0 242.0,264.0ZM645.0,356.0Q645.0,352.0 645.0,348.0Q657.0,361.0 669.5,373.5Q682.0,386.0 696.0,400.0L796.0,494.0Q730.0,556.0 657.0,556.0Q599.0,556.0 556.0,525.0Q513.0,494.0 479.0,452.0Q505.0,465.0 533.0,465.0Q591.0,465.0 618.0,433.5Q645.0,402.0 645.0,356.0ZM274.0,554.0Q216.0,554.0 176.0,530.0Q293.0,480.0 386.0,403.0Q400.0,428.0 400.0,457.0Q400.0,504.0 368.0,529.0Q336.0,554.0 274.0,554.0ZM122.0,436.0Q122.0,390.0 155.0,362.5Q188.0,335.0 248.0,335.0Q299.0,335.0 338.0,357.0Q243.0,432.0 131.0,480.0Q122.0,460.0 122.0,436.0Z" transform="translate(1226, 908)"/>
<path d="M-443.0,-187.0L-443.0,-116.0L-67.0,-116.0L-67.0,-187.0L-443.0,-187.0Z" transform="translate(2018, 595)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ফ্অ꣱ংধএ᳘</span> (Added by SIESTA)</li>


<pre>Expected: phabeng=0+838|viramabeng=0@-221,0+0|abeng=2+893|uniA8F1=2@0,323+0|uni25CC=2+510|anusvarabeng=2+394|dhabeng=5+596|ebeng=6+758|uni1CD8=6@-124,-351+0</pre>



<pre>Got     : phabeng=0+838|viramabeng=0@-221,0+0|abeng=2+893|uniA8F1=2@0,323+0|uni25CC=2+510|anusvarabeng=2+438|dhabeng=5+596|ebeng=6+758|uni1CD8=6@-124,-351+0</pre>



<pre>                                                                                                         ++
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4033 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M848.0,622.0L848.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.5,327.5Q184.0,301.0 142.0,276.0Q246.0,250.0 316.0,207.5Q386.0,165.0 447.0,99.0Q446.0,116.0 445.5,134.0Q445.0,152.0 445.0,171.0L445.0,510.0L458.0,510.0Q540.0,510.0 614.0,488.5Q688.0,467.0 739.0,414.0Q763.0,389.0 777.5,357.5Q792.0,326.0 792.0,288.0Q792.0,255.0 778.5,225.5Q765.0,196.0 735.0,177.0Q705.0,158.0 655.0,158.0Q640.0,158.0 625.5,159.0Q611.0,160.0 597.0,163.0L602.0,234.0Q608.0,233.0 617.0,232.5Q626.0,232.0 636.0,232.0Q685.0,232.0 699.5,251.0Q714.0,270.0 714.0,296.0Q714.0,347.0 662.5,386.0Q611.0,425.0 522.0,434.0L522.0,0.0L445.0,0.0Q404.0,56.0 354.5,98.0Q305.0,140.0 239.5,168.5Q174.0,197.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L848.0,622.0Z" transform="translate(0, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(617, 908)"/>
<path d="M376.0,91.0Q308.0,91.0 246.0,123.0Q184.0,155.0 129.5,231.5Q75.0,308.0 29.0,442.0L102.0,466.0Q155.0,309.0 219.5,238.0Q284.0,167.0 378.0,167.0Q461.0,167.0 495.5,205.5Q530.0,244.0 530.0,300.0Q530.0,358.0 498.5,394.0Q467.0,430.0 420.0,430.0Q353.0,430.0 353.0,372.0Q353.0,365.0 355.0,353.0Q357.0,341.0 361.0,331.0L285.0,316.0Q278.0,337.0 274.5,354.5Q271.0,372.0 271.0,388.0Q271.0,423.0 290.0,447.5Q309.0,472.0 339.0,485.0Q330.0,507.0 311.5,524.0Q293.0,541.0 262.0,551.0L-10.0,551.0L-10.0,622.0L903.0,622.0L903.0,551.0L798.0,551.0L798.0,0.0L721.0,0.0Q693.0,56.0 653.0,98.5Q613.0,141.0 568.0,173.0Q540.0,136.0 492.0,113.5Q444.0,91.0 376.0,91.0ZM606.0,294.0Q606.0,264.0 598.0,236.0Q634.0,213.0 669.5,178.5Q705.0,144.0 724.0,109.0Q723.0,131.0 722.0,150.5Q721.0,170.0 721.0,194.0L721.0,551.0L381.0,551.0Q406.0,530.0 416.0,500.0Q474.0,499.0 516.5,472.5Q559.0,446.0 582.5,400.0Q606.0,354.0 606.0,294.0Z" transform="translate(838, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(1731, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1731, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(2241, 908)"/>
<path d="M240.0,629.0Q252.0,629.0 266.0,627.5Q280.0,626.0 293.0,624.0L287.0,552.0Q281.0,553.0 272.5,553.5Q264.0,554.0 251.0,554.0Q221.0,554.0 204.5,541.5Q188.0,529.0 188.0,509.0Q188.0,490.0 199.5,475.5Q211.0,461.0 240.0,446.0Q285.0,466.0 331.0,484.0Q377.0,502.0 424.0,517.0L424.0,622.0L606.0,622.0L606.0,551.0L501.0,551.0L501.0,0.0L424.0,0.0Q394.0,60.0 341.5,110.5Q289.0,161.0 221.0,196.0Q153.0,231.0 76.0,243.0L37.0,339.0Q105.0,380.0 173.0,414.0Q143.0,436.0 126.0,463.0Q109.0,490.0 109.0,524.0Q109.0,565.0 141.0,597.0Q173.0,629.0 240.0,629.0ZM130.0,304.0Q181.0,293.0 238.0,266.5Q295.0,240.0 345.5,200.0Q396.0,160.0 427.0,108.0Q426.0,126.0 425.0,145.0Q424.0,164.0 424.0,189.0L424.0,439.0Q352.0,414.0 274.0,379.5Q196.0,345.0 130.0,304.0Z" transform="translate(2679, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(3275, 908)"/>
<path d="M-44.0,-88.0Q-67.0,-188.0 -120.5,-229.5Q-174.0,-271.0 -251.0,-271.0Q-323.0,-271.0 -377.0,-226.5Q-431.0,-182.0 -465.0,-88.0L-394.0,-64.0Q-368.0,-134.0 -334.5,-168.0Q-301.0,-202.0 -248.0,-202.0Q-191.0,-202.0 -163.5,-165.5Q-136.0,-129.0 -120.0,-62.0L-44.0,-88.0Z" transform="translate(3909, 557)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3989 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M848.0,622.0L848.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.5,327.5Q184.0,301.0 142.0,276.0Q246.0,250.0 316.0,207.5Q386.0,165.0 447.0,99.0Q446.0,116.0 445.5,134.0Q445.0,152.0 445.0,171.0L445.0,510.0L458.0,510.0Q540.0,510.0 614.0,488.5Q688.0,467.0 739.0,414.0Q763.0,389.0 777.5,357.5Q792.0,326.0 792.0,288.0Q792.0,255.0 778.5,225.5Q765.0,196.0 735.0,177.0Q705.0,158.0 655.0,158.0Q640.0,158.0 625.5,159.0Q611.0,160.0 597.0,163.0L602.0,234.0Q608.0,233.0 617.0,232.5Q626.0,232.0 636.0,232.0Q685.0,232.0 699.5,251.0Q714.0,270.0 714.0,296.0Q714.0,347.0 662.5,386.0Q611.0,425.0 522.0,434.0L522.0,0.0L445.0,0.0Q404.0,56.0 354.5,98.0Q305.0,140.0 239.5,168.5Q174.0,197.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L848.0,622.0Z" transform="translate(0, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(617, 908)"/>
<path d="M376.0,91.0Q308.0,91.0 246.0,123.0Q184.0,155.0 129.5,231.5Q75.0,308.0 29.0,442.0L102.0,466.0Q155.0,309.0 219.5,238.0Q284.0,167.0 378.0,167.0Q461.0,167.0 495.5,205.5Q530.0,244.0 530.0,300.0Q530.0,358.0 498.5,394.0Q467.0,430.0 420.0,430.0Q353.0,430.0 353.0,372.0Q353.0,365.0 355.0,353.0Q357.0,341.0 361.0,331.0L285.0,316.0Q278.0,337.0 274.5,354.5Q271.0,372.0 271.0,388.0Q271.0,423.0 290.0,447.5Q309.0,472.0 339.0,485.0Q330.0,507.0 311.5,524.0Q293.0,541.0 262.0,551.0L-10.0,551.0L-10.0,622.0L903.0,622.0L903.0,551.0L798.0,551.0L798.0,0.0L721.0,0.0Q693.0,56.0 653.0,98.5Q613.0,141.0 568.0,173.0Q540.0,136.0 492.0,113.5Q444.0,91.0 376.0,91.0ZM606.0,294.0Q606.0,264.0 598.0,236.0Q634.0,213.0 669.5,178.5Q705.0,144.0 724.0,109.0Q723.0,131.0 722.0,150.5Q721.0,170.0 721.0,194.0L721.0,551.0L381.0,551.0Q406.0,530.0 416.0,500.0Q474.0,499.0 516.5,472.5Q559.0,446.0 582.5,400.0Q606.0,354.0 606.0,294.0Z" transform="translate(838, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(1731, 1231)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1731, 908)"/>
<path d="M78.0,486.0Q78.0,548.0 118.5,585.0Q159.0,622.0 219.0,622.0Q279.0,622.0 319.5,585.0Q360.0,548.0 360.0,486.0Q360.0,424.0 319.5,386.5Q279.0,349.0 219.0,349.0Q159.0,349.0 118.5,386.0Q78.0,423.0 78.0,486.0ZM147.0,486.0Q147.0,452.0 167.5,433.0Q188.0,414.0 219.0,414.0Q251.0,414.0 271.0,433.5Q291.0,453.0 291.0,486.0Q291.0,520.0 271.0,538.5Q251.0,557.0 219.0,557.0Q188.0,557.0 167.5,537.5Q147.0,518.0 147.0,486.0ZM123.0,314.0Q186.0,276.0 242.5,223.5Q299.0,171.0 345.5,111.0Q392.0,51.0 424.0,-8.0L359.0,-41.0Q318.0,22.0 277.5,72.5Q237.0,123.0 188.5,166.0Q140.0,209.0 73.0,250.0L123.0,314.0Z" transform="translate(2241, 908)"/>
<path d="M240.0,629.0Q252.0,629.0 266.0,627.5Q280.0,626.0 293.0,624.0L287.0,552.0Q281.0,553.0 272.5,553.5Q264.0,554.0 251.0,554.0Q221.0,554.0 204.5,541.5Q188.0,529.0 188.0,509.0Q188.0,490.0 199.5,475.5Q211.0,461.0 240.0,446.0Q285.0,466.0 331.0,484.0Q377.0,502.0 424.0,517.0L424.0,622.0L606.0,622.0L606.0,551.0L501.0,551.0L501.0,0.0L424.0,0.0Q394.0,60.0 341.5,110.5Q289.0,161.0 221.0,196.0Q153.0,231.0 76.0,243.0L37.0,339.0Q105.0,380.0 173.0,414.0Q143.0,436.0 126.0,463.0Q109.0,490.0 109.0,524.0Q109.0,565.0 141.0,597.0Q173.0,629.0 240.0,629.0ZM130.0,304.0Q181.0,293.0 238.0,266.5Q295.0,240.0 345.5,200.0Q396.0,160.0 427.0,108.0Q426.0,126.0 425.0,145.0Q424.0,164.0 424.0,189.0L424.0,439.0Q352.0,414.0 274.0,379.5Q196.0,345.0 130.0,304.0Z" transform="translate(2635, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(3231, 908)"/>
<path d="M-44.0,-88.0Q-67.0,-188.0 -120.5,-229.5Q-174.0,-271.0 -251.0,-271.0Q-323.0,-271.0 -377.0,-226.5Q-431.0,-182.0 -465.0,-88.0L-394.0,-64.0Q-368.0,-134.0 -334.5,-168.0Q-301.0,-202.0 -248.0,-202.0Q-191.0,-202.0 -163.5,-165.5Q-136.0,-129.0 -120.0,-62.0L-44.0,-88.0Z" transform="translate(3865, 557)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">৬᳖ঙ্মৢৢ꣱ক</span> (Added by SIESTA)</li>


<pre>Expected: sixbeng=0+592|uni1CD6=0@-41,-319+0|ngamabeng=2+918|lvocalicvowelsignbeng=2@225,0+0|lvocalicvowelsignbeng=2+0|uniA8F1=2@0,323+0|kabeng=8+807</pre>



<pre>Got     : sixbeng=0+592|uni1CD6=0@-41,-319+0|ngamabeng=2+918|lvocalicvowelsignbeng=2+0|lvocalicvowelsignbeng=2+0|uniA8F1=2@0,323+0|kabeng=8+807</pre>



<pre>                                                                                    ++++++
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2317 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M347.0,39.0Q295.0,39.0 248.0,58.5Q201.0,78.0 160.0,124.5Q119.0,171.0 84.0,251.0Q49.0,331.0 21.0,452.0L96.0,475.0Q124.0,344.0 159.0,264.5Q194.0,185.0 239.0,150.0Q284.0,115.0 342.0,115.0Q407.0,115.0 445.0,154.0Q483.0,193.0 483.0,271.0Q483.0,294.0 479.0,313.5Q475.0,333.0 469.0,348.0Q420.0,257.0 340.0,257.0Q296.0,257.0 270.0,282.0Q255.0,296.0 245.0,321.0Q235.0,346.0 235.0,400.0L235.0,451.0Q235.0,488.0 222.5,502.0Q210.0,516.0 166.0,517.0L175.0,593.0Q256.0,590.0 286.0,560.0Q300.0,545.0 306.0,523.0Q312.0,501.0 312.0,471.0L312.0,379.0Q312.0,354.0 320.0,341.0Q328.0,328.0 348.0,328.0Q372.0,328.0 395.0,349.5Q418.0,371.0 443.0,438.0L499.0,452.0Q527.0,415.0 543.0,364.0Q559.0,313.0 559.0,268.0Q559.0,203.0 536.5,151.0Q514.0,99.0 467.0,69.0Q420.0,39.0 347.0,39.0Z" transform="translate(0, 908)"/>
<path d="M-426.0,-94.0L-348.0,-94.0L-348.0,-202.0L-78.0,-202.0L-78.0,-271.0L-426.0,-271.0L-426.0,-94.0Z" transform="translate(551, 589)"/>
<path d="M364.0,125.0Q293.0,125.0 229.5,157.0Q166.0,189.0 115.5,261.0Q65.0,333.0 29.0,453.0L103.0,473.0Q131.0,373.0 168.5,313.0Q206.0,253.0 255.0,226.0Q304.0,199.0 366.0,199.0Q437.0,199.0 478.0,224.5Q519.0,250.0 519.0,301.0Q519.0,322.0 513.0,343.0Q465.0,302.0 427.5,290.0Q390.0,278.0 355.0,278.0Q295.0,278.0 263.0,317.0Q231.0,356.0 231.0,414.0Q231.0,458.0 243.0,492.5Q255.0,527.0 275.0,552.0Q247.0,551.0 218.0,551.0L-10.0,551.0L-10.0,622.0L928.0,622.0L928.0,551.0L823.0,551.0L823.0,-117.0L746.0,-117.0L746.0,-94.0Q702.0,-36.0 653.5,3.0Q605.0,42.0 548.0,42.0Q526.0,42.0 513.0,31.5Q500.0,21.0 500.0,4.0Q500.0,-16.0 514.0,-27.5Q528.0,-39.0 555.0,-49.0L520.0,-118.0Q474.0,-100.0 447.0,-69.0Q420.0,-38.0 420.0,4.0Q420.0,55.0 453.5,82.5Q487.0,110.0 533.0,112.0Q528.0,139.0 511.0,157.0Q452.0,125.0 364.0,125.0ZM407.0,565.0Q377.0,565.0 354.0,543.5Q331.0,522.0 318.0,488.0Q332.0,484.0 349.5,481.0Q367.0,478.0 384.0,478.0Q422.0,478.0 438.0,492.5Q454.0,507.0 454.0,527.0Q454.0,548.0 440.0,556.5Q426.0,565.0 407.0,565.0ZM746.0,98.0L746.0,551.0L518.0,551.0Q522.0,538.0 522.0,523.0Q522.0,476.0 486.5,447.0Q451.0,418.0 383.0,418.0Q363.0,418.0 342.0,421.0Q321.0,424.0 304.0,429.0Q303.0,417.0 303.0,404.0Q303.0,376.0 315.0,361.5Q327.0,347.0 356.0,347.0Q390.0,347.0 425.5,365.5Q461.0,384.0 507.0,424.0L562.0,421.0Q576.0,395.0 585.0,362.5Q594.0,330.0 594.0,297.0Q594.0,243.0 565.0,203.0Q582.0,189.0 595.0,164.5Q608.0,140.0 608.0,102.0Q648.0,89.0 682.5,63.0Q717.0,37.0 749.0,0.0Q747.0,24.0 746.5,48.5Q746.0,73.0 746.0,98.0Z" transform="translate(592, 908)"/>
<path d="M-254.0,-127.0Q-200.0,-127.0 -173.0,-150.0Q-146.0,-173.0 -146.0,-208.0Q-146.0,-220.0 -150.5,-233.0Q-155.0,-246.0 -168.0,-258.0Q-108.0,-250.0 -84.0,-232.5Q-60.0,-215.0 -60.0,-187.0Q-60.0,-170.0 -68.5,-157.0Q-77.0,-144.0 -101.5,-131.0Q-126.0,-118.0 -174.0,-104.0Q-225.0,-88.0 -252.0,-71.5Q-279.0,-55.0 -279.0,-22.0Q-279.0,-5.0 -269.0,13.0L-213.0,0.0Q-217.0,-8.0 -217.0,-16.0Q-217.0,-26.0 -202.5,-33.0Q-188.0,-40.0 -139.0,-55.0Q-79.0,-73.0 -47.0,-92.5Q-15.0,-112.0 -3.5,-135.0Q8.0,-158.0 8.0,-185.0Q8.0,-232.0 -24.0,-260.5Q-56.0,-289.0 -107.5,-301.0Q-159.0,-313.0 -220.0,-313.0L-244.0,-313.0L-256.0,-264.0Q-229.0,-256.0 -217.0,-243.5Q-205.0,-231.0 -205.0,-214.0Q-205.0,-199.0 -216.0,-189.5Q-227.0,-180.0 -252.0,-180.0Q-292.0,-180.0 -292.0,-204.0Q-292.0,-213.0 -285.0,-227.0L-345.0,-238.0Q-356.0,-218.0 -356.0,-195.0Q-356.0,-166.0 -330.5,-146.5Q-305.0,-127.0 -254.0,-127.0Z" transform="translate(1510, 908)"/>
<path d="M-254.0,-127.0Q-200.0,-127.0 -173.0,-150.0Q-146.0,-173.0 -146.0,-208.0Q-146.0,-220.0 -150.5,-233.0Q-155.0,-246.0 -168.0,-258.0Q-108.0,-250.0 -84.0,-232.5Q-60.0,-215.0 -60.0,-187.0Q-60.0,-170.0 -68.5,-157.0Q-77.0,-144.0 -101.5,-131.0Q-126.0,-118.0 -174.0,-104.0Q-225.0,-88.0 -252.0,-71.5Q-279.0,-55.0 -279.0,-22.0Q-279.0,-5.0 -269.0,13.0L-213.0,0.0Q-217.0,-8.0 -217.0,-16.0Q-217.0,-26.0 -202.5,-33.0Q-188.0,-40.0 -139.0,-55.0Q-79.0,-73.0 -47.0,-92.5Q-15.0,-112.0 -3.5,-135.0Q8.0,-158.0 8.0,-185.0Q8.0,-232.0 -24.0,-260.5Q-56.0,-289.0 -107.5,-301.0Q-159.0,-313.0 -220.0,-313.0L-244.0,-313.0L-256.0,-264.0Q-229.0,-256.0 -217.0,-243.5Q-205.0,-231.0 -205.0,-214.0Q-205.0,-199.0 -216.0,-189.5Q-227.0,-180.0 -252.0,-180.0Q-292.0,-180.0 -292.0,-204.0Q-292.0,-213.0 -285.0,-227.0L-345.0,-238.0Q-356.0,-218.0 -356.0,-195.0Q-356.0,-166.0 -330.5,-146.5Q-305.0,-127.0 -254.0,-127.0Z" transform="translate(1510, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(1510, 1231)"/>
<path d="M761.0,288.0Q761.0,255.0 748.0,225.5Q735.0,196.0 705.0,177.0Q675.0,158.0 625.0,158.0Q609.0,158.0 594.5,159.0Q580.0,160.0 566.0,163.0L572.0,235.0Q578.0,234.0 586.5,233.5Q595.0,233.0 606.0,233.0Q654.0,233.0 668.5,251.5Q683.0,270.0 683.0,296.0Q683.0,347.0 635.0,384.0Q587.0,421.0 492.0,436.0L492.0,0.0L415.0,0.0Q386.0,59.0 334.0,111.0Q282.0,163.0 215.5,198.5Q149.0,234.0 76.0,243.0L37.0,339.0Q129.0,392.0 221.0,434.5Q313.0,477.0 415.0,510.0L415.0,551.0L-10.0,551.0L-10.0,622.0L817.0,622.0L817.0,551.0L492.0,551.0L492.0,512.0Q566.0,502.0 627.0,471.5Q688.0,441.0 724.5,394.5Q761.0,348.0 761.0,288.0ZM130.0,304.0Q183.0,294.0 239.0,266.0Q295.0,238.0 342.5,197.5Q390.0,157.0 418.0,109.0Q417.0,126.0 416.0,145.0Q415.0,164.0 415.0,189.0L415.0,432.0Q342.0,409.0 266.0,373.0Q190.0,337.0 130.0,304.0Z" transform="translate(1510, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2317 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M347.0,39.0Q295.0,39.0 248.0,58.5Q201.0,78.0 160.0,124.5Q119.0,171.0 84.0,251.0Q49.0,331.0 21.0,452.0L96.0,475.0Q124.0,344.0 159.0,264.5Q194.0,185.0 239.0,150.0Q284.0,115.0 342.0,115.0Q407.0,115.0 445.0,154.0Q483.0,193.0 483.0,271.0Q483.0,294.0 479.0,313.5Q475.0,333.0 469.0,348.0Q420.0,257.0 340.0,257.0Q296.0,257.0 270.0,282.0Q255.0,296.0 245.0,321.0Q235.0,346.0 235.0,400.0L235.0,451.0Q235.0,488.0 222.5,502.0Q210.0,516.0 166.0,517.0L175.0,593.0Q256.0,590.0 286.0,560.0Q300.0,545.0 306.0,523.0Q312.0,501.0 312.0,471.0L312.0,379.0Q312.0,354.0 320.0,341.0Q328.0,328.0 348.0,328.0Q372.0,328.0 395.0,349.5Q418.0,371.0 443.0,438.0L499.0,452.0Q527.0,415.0 543.0,364.0Q559.0,313.0 559.0,268.0Q559.0,203.0 536.5,151.0Q514.0,99.0 467.0,69.0Q420.0,39.0 347.0,39.0Z" transform="translate(0, 908)"/>
<path d="M-426.0,-94.0L-348.0,-94.0L-348.0,-202.0L-78.0,-202.0L-78.0,-271.0L-426.0,-271.0L-426.0,-94.0Z" transform="translate(551, 589)"/>
<path d="M364.0,125.0Q293.0,125.0 229.5,157.0Q166.0,189.0 115.5,261.0Q65.0,333.0 29.0,453.0L103.0,473.0Q131.0,373.0 168.5,313.0Q206.0,253.0 255.0,226.0Q304.0,199.0 366.0,199.0Q437.0,199.0 478.0,224.5Q519.0,250.0 519.0,301.0Q519.0,322.0 513.0,343.0Q465.0,302.0 427.5,290.0Q390.0,278.0 355.0,278.0Q295.0,278.0 263.0,317.0Q231.0,356.0 231.0,414.0Q231.0,458.0 243.0,492.5Q255.0,527.0 275.0,552.0Q247.0,551.0 218.0,551.0L-10.0,551.0L-10.0,622.0L928.0,622.0L928.0,551.0L823.0,551.0L823.0,-117.0L746.0,-117.0L746.0,-94.0Q702.0,-36.0 653.5,3.0Q605.0,42.0 548.0,42.0Q526.0,42.0 513.0,31.5Q500.0,21.0 500.0,4.0Q500.0,-16.0 514.0,-27.5Q528.0,-39.0 555.0,-49.0L520.0,-118.0Q474.0,-100.0 447.0,-69.0Q420.0,-38.0 420.0,4.0Q420.0,55.0 453.5,82.5Q487.0,110.0 533.0,112.0Q528.0,139.0 511.0,157.0Q452.0,125.0 364.0,125.0ZM407.0,565.0Q377.0,565.0 354.0,543.5Q331.0,522.0 318.0,488.0Q332.0,484.0 349.5,481.0Q367.0,478.0 384.0,478.0Q422.0,478.0 438.0,492.5Q454.0,507.0 454.0,527.0Q454.0,548.0 440.0,556.5Q426.0,565.0 407.0,565.0ZM746.0,98.0L746.0,551.0L518.0,551.0Q522.0,538.0 522.0,523.0Q522.0,476.0 486.5,447.0Q451.0,418.0 383.0,418.0Q363.0,418.0 342.0,421.0Q321.0,424.0 304.0,429.0Q303.0,417.0 303.0,404.0Q303.0,376.0 315.0,361.5Q327.0,347.0 356.0,347.0Q390.0,347.0 425.5,365.5Q461.0,384.0 507.0,424.0L562.0,421.0Q576.0,395.0 585.0,362.5Q594.0,330.0 594.0,297.0Q594.0,243.0 565.0,203.0Q582.0,189.0 595.0,164.5Q608.0,140.0 608.0,102.0Q648.0,89.0 682.5,63.0Q717.0,37.0 749.0,0.0Q747.0,24.0 746.5,48.5Q746.0,73.0 746.0,98.0Z" transform="translate(592, 908)"/>
<path d="M-254.0,-127.0Q-200.0,-127.0 -173.0,-150.0Q-146.0,-173.0 -146.0,-208.0Q-146.0,-220.0 -150.5,-233.0Q-155.0,-246.0 -168.0,-258.0Q-108.0,-250.0 -84.0,-232.5Q-60.0,-215.0 -60.0,-187.0Q-60.0,-170.0 -68.5,-157.0Q-77.0,-144.0 -101.5,-131.0Q-126.0,-118.0 -174.0,-104.0Q-225.0,-88.0 -252.0,-71.5Q-279.0,-55.0 -279.0,-22.0Q-279.0,-5.0 -269.0,13.0L-213.0,0.0Q-217.0,-8.0 -217.0,-16.0Q-217.0,-26.0 -202.5,-33.0Q-188.0,-40.0 -139.0,-55.0Q-79.0,-73.0 -47.0,-92.5Q-15.0,-112.0 -3.5,-135.0Q8.0,-158.0 8.0,-185.0Q8.0,-232.0 -24.0,-260.5Q-56.0,-289.0 -107.5,-301.0Q-159.0,-313.0 -220.0,-313.0L-244.0,-313.0L-256.0,-264.0Q-229.0,-256.0 -217.0,-243.5Q-205.0,-231.0 -205.0,-214.0Q-205.0,-199.0 -216.0,-189.5Q-227.0,-180.0 -252.0,-180.0Q-292.0,-180.0 -292.0,-204.0Q-292.0,-213.0 -285.0,-227.0L-345.0,-238.0Q-356.0,-218.0 -356.0,-195.0Q-356.0,-166.0 -330.5,-146.5Q-305.0,-127.0 -254.0,-127.0Z" transform="translate(1735, 908)"/>
<path d="M-254.0,-127.0Q-200.0,-127.0 -173.0,-150.0Q-146.0,-173.0 -146.0,-208.0Q-146.0,-220.0 -150.5,-233.0Q-155.0,-246.0 -168.0,-258.0Q-108.0,-250.0 -84.0,-232.5Q-60.0,-215.0 -60.0,-187.0Q-60.0,-170.0 -68.5,-157.0Q-77.0,-144.0 -101.5,-131.0Q-126.0,-118.0 -174.0,-104.0Q-225.0,-88.0 -252.0,-71.5Q-279.0,-55.0 -279.0,-22.0Q-279.0,-5.0 -269.0,13.0L-213.0,0.0Q-217.0,-8.0 -217.0,-16.0Q-217.0,-26.0 -202.5,-33.0Q-188.0,-40.0 -139.0,-55.0Q-79.0,-73.0 -47.0,-92.5Q-15.0,-112.0 -3.5,-135.0Q8.0,-158.0 8.0,-185.0Q8.0,-232.0 -24.0,-260.5Q-56.0,-289.0 -107.5,-301.0Q-159.0,-313.0 -220.0,-313.0L-244.0,-313.0L-256.0,-264.0Q-229.0,-256.0 -217.0,-243.5Q-205.0,-231.0 -205.0,-214.0Q-205.0,-199.0 -216.0,-189.5Q-227.0,-180.0 -252.0,-180.0Q-292.0,-180.0 -292.0,-204.0Q-292.0,-213.0 -285.0,-227.0L-345.0,-238.0Q-356.0,-218.0 -356.0,-195.0Q-356.0,-166.0 -330.5,-146.5Q-305.0,-127.0 -254.0,-127.0Z" transform="translate(1510, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(1510, 1231)"/>
<path d="M761.0,288.0Q761.0,255.0 748.0,225.5Q735.0,196.0 705.0,177.0Q675.0,158.0 625.0,158.0Q609.0,158.0 594.5,159.0Q580.0,160.0 566.0,163.0L572.0,235.0Q578.0,234.0 586.5,233.5Q595.0,233.0 606.0,233.0Q654.0,233.0 668.5,251.5Q683.0,270.0 683.0,296.0Q683.0,347.0 635.0,384.0Q587.0,421.0 492.0,436.0L492.0,0.0L415.0,0.0Q386.0,59.0 334.0,111.0Q282.0,163.0 215.5,198.5Q149.0,234.0 76.0,243.0L37.0,339.0Q129.0,392.0 221.0,434.5Q313.0,477.0 415.0,510.0L415.0,551.0L-10.0,551.0L-10.0,622.0L817.0,622.0L817.0,551.0L492.0,551.0L492.0,512.0Q566.0,502.0 627.0,471.5Q688.0,441.0 724.5,394.5Q761.0,348.0 761.0,288.0ZM130.0,304.0Q183.0,294.0 239.0,266.0Q295.0,238.0 342.5,197.5Q390.0,157.0 418.0,109.0Q417.0,126.0 416.0,145.0Q415.0,164.0 415.0,189.0L415.0,432.0Q342.0,409.0 266.0,373.0Q190.0,337.0 130.0,304.0Z" transform="translate(1510, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ক্ষ/৾ঙএ</span> (Added by SIESTA)</li>


<pre>Expected: kassabeng=0+919|slash.beng=3+449|uni25CC=3+510|uni09FE=3+0|ngabeng=5+705|ebeng=6+758</pre>



<pre>Got     : kassabeng=0+919|slash.beng=3+449|uni25CC=3+510|uni09FE=3+0|ngabeng=5+723|ebeng=6+758</pre>



<pre>                                                                                ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3359 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M876.0,271.0Q876.0,241.0 863.5,212.5Q851.0,184.0 822.5,166.0Q794.0,148.0 745.0,148.0Q731.0,148.0 716.5,149.0Q702.0,150.0 689.0,153.0L695.0,225.0Q709.0,223.0 728.0,223.0Q772.0,223.0 785.5,239.5Q799.0,256.0 799.0,276.0Q799.0,312.0 772.0,334.0Q727.0,369.0 614.0,372.0L614.0,0.0L537.0,0.0L537.0,43.0Q491.0,116.0 446.0,155.0Q401.0,194.0 351.0,194.0Q299.0,194.0 299.0,148.0Q299.0,132.0 303.0,120.0Q307.0,108.0 311.0,99.0L234.0,83.0Q227.0,97.0 222.0,115.0Q217.0,133.0 217.0,150.0Q217.0,192.0 238.0,219.0Q259.0,246.0 294.0,257.0Q294.0,290.0 284.0,321.0Q274.0,352.0 251.0,372.0Q228.0,392.0 190.0,392.0Q158.0,392.0 144.5,378.0Q131.0,364.0 131.0,342.0Q131.0,324.0 140.0,304.0L62.0,288.0Q48.0,319.0 48.0,349.0Q48.0,387.0 69.0,414.5Q90.0,442.0 126.0,454.0Q125.0,480.0 116.5,506.0Q108.0,532.0 90.0,551.0L-10.0,551.0L-10.0,622.0L929.0,622.0L929.0,551.0L614.0,551.0L614.0,442.0Q701.0,440.0 751.0,424.0Q801.0,408.0 831.0,380.0Q856.0,358.0 866.0,330.5Q876.0,303.0 876.0,271.0ZM371.0,265.0Q371.0,264.0 371.0,263.0Q421.0,257.0 463.5,225.0Q506.0,193.0 538.0,148.0Q537.0,174.0 537.0,202.0L537.0,373.0Q484.0,375.0 443.0,391.0Q402.0,407.0 378.5,441.0Q355.0,475.0 355.0,531.0Q355.0,539.0 356.0,551.0L179.0,551.0Q200.0,515.0 202.0,462.0Q249.0,459.0 287.5,435.0Q326.0,411.0 348.5,368.0Q371.0,325.0 371.0,265.0ZM431.0,536.0Q431.0,483.0 459.0,464.0Q487.0,445.0 537.0,443.0L537.0,551.0L432.0,551.0Q431.0,542.0 431.0,536.0Z" transform="translate(0, 908)"/>
<path d="M315.0,792.0L397.0,792.0L135.0,-125.0L52.0,-125.0L315.0,792.0Z" transform="translate(919, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1368, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(1878, 908)"/>
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(1878, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(2601, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3341 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M876.0,271.0Q876.0,241.0 863.5,212.5Q851.0,184.0 822.5,166.0Q794.0,148.0 745.0,148.0Q731.0,148.0 716.5,149.0Q702.0,150.0 689.0,153.0L695.0,225.0Q709.0,223.0 728.0,223.0Q772.0,223.0 785.5,239.5Q799.0,256.0 799.0,276.0Q799.0,312.0 772.0,334.0Q727.0,369.0 614.0,372.0L614.0,0.0L537.0,0.0L537.0,43.0Q491.0,116.0 446.0,155.0Q401.0,194.0 351.0,194.0Q299.0,194.0 299.0,148.0Q299.0,132.0 303.0,120.0Q307.0,108.0 311.0,99.0L234.0,83.0Q227.0,97.0 222.0,115.0Q217.0,133.0 217.0,150.0Q217.0,192.0 238.0,219.0Q259.0,246.0 294.0,257.0Q294.0,290.0 284.0,321.0Q274.0,352.0 251.0,372.0Q228.0,392.0 190.0,392.0Q158.0,392.0 144.5,378.0Q131.0,364.0 131.0,342.0Q131.0,324.0 140.0,304.0L62.0,288.0Q48.0,319.0 48.0,349.0Q48.0,387.0 69.0,414.5Q90.0,442.0 126.0,454.0Q125.0,480.0 116.5,506.0Q108.0,532.0 90.0,551.0L-10.0,551.0L-10.0,622.0L929.0,622.0L929.0,551.0L614.0,551.0L614.0,442.0Q701.0,440.0 751.0,424.0Q801.0,408.0 831.0,380.0Q856.0,358.0 866.0,330.5Q876.0,303.0 876.0,271.0ZM371.0,265.0Q371.0,264.0 371.0,263.0Q421.0,257.0 463.5,225.0Q506.0,193.0 538.0,148.0Q537.0,174.0 537.0,202.0L537.0,373.0Q484.0,375.0 443.0,391.0Q402.0,407.0 378.5,441.0Q355.0,475.0 355.0,531.0Q355.0,539.0 356.0,551.0L179.0,551.0Q200.0,515.0 202.0,462.0Q249.0,459.0 287.5,435.0Q326.0,411.0 348.5,368.0Q371.0,325.0 371.0,265.0ZM431.0,536.0Q431.0,483.0 459.0,464.0Q487.0,445.0 537.0,443.0L537.0,551.0L432.0,551.0Q431.0,542.0 431.0,536.0Z" transform="translate(0, 908)"/>
<path d="M315.0,792.0L397.0,792.0L135.0,-125.0L52.0,-125.0L315.0,792.0Z" transform="translate(919, 908)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(1368, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(1878, 908)"/>
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(1878, 908)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(2583, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ᳶৈফেঙ᳒২꣱এৠ</span> (Added by SIESTA)</li>


<pre>Expected: aivowelsigninibeng=0+346|uni1CF6=0+628|evowelsignbeng=2+346|phabeng=2+838|ngabeng=4+723|uni1CD2=4@-107,323+0|twobeng=6+592|uniA8F1=6@0,323+0|ebeng=8+740|rrvocalicbeng=9+853</pre>



<pre>Got     : aivowelsigninibeng=0+346|uni1CF6=0+628|evowelsignbeng=2+346|phabeng=2+838|ngabeng=4+723|uni1CD2=4@-107,323+0|twobeng=6+592|uniA8F1=6@0,323+0|ebeng=8+758|rrvocalicbeng=9+853</pre>



<pre>                                                                                                                                                                ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5084 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M356.0,622.0L356.0,551.0L336.0,551.0Q305.0,544.0 269.0,520.5Q233.0,497.0 201.0,459.5Q169.0,422.0 148.5,372.0Q128.0,322.0 128.0,262.0Q128.0,190.0 149.5,147.5Q171.0,105.0 203.0,87.0Q235.0,69.0 267.0,69.0Q292.0,69.0 309.0,74.0Q326.0,79.0 348.0,92.0L383.0,31.0Q357.0,11.0 326.0,3.0Q295.0,-5.0 263.0,-5.0Q200.0,-5.0 152.0,28.0Q104.0,61.0 76.5,120.5Q49.0,180.0 49.0,260.0Q49.0,331.0 70.0,387.5Q91.0,444.0 125.0,488.0Q159.0,532.0 200.5,562.5Q242.0,593.0 283.0,611.0L283.0,617.0Q283.0,659.0 265.0,679.0Q247.0,699.0 203.0,699.0L183.0,699.0Q118.0,699.0 82.5,708.0Q47.0,717.0 22.0,736.0Q-32.0,777.0 -32.0,859.0Q-32.0,872.0 -30.5,884.5Q-29.0,897.0 -27.0,912.0L47.0,907.0Q43.0,887.0 43.0,869.0Q43.0,847.0 47.5,830.0Q52.0,813.0 62.0,802.0Q76.0,786.0 102.0,778.5Q128.0,771.0 178.0,771.0L182.0,771.0Q235.0,771.0 266.0,763.0Q297.0,755.0 319.0,734.0Q352.0,702.0 355.0,622.0L356.0,622.0Z" transform="translate(0, 908)"/>
<path d="M198.0,195.0Q153.0,195.0 120.5,214.0Q88.0,233.0 69.5,282.0Q51.0,331.0 47.0,422.0L126.0,427.0Q128.0,359.0 136.5,324.5Q145.0,290.0 161.5,278.0Q178.0,266.0 202.0,266.0Q245.0,266.0 259.5,300.5Q274.0,335.0 277.0,423.0L351.0,423.0Q354.0,335.0 370.0,300.5Q386.0,266.0 427.0,266.0Q449.0,266.0 465.0,278.5Q481.0,291.0 490.5,325.5Q500.0,360.0 502.0,427.0L581.0,422.0Q578.0,331.0 559.5,282.0Q541.0,233.0 508.5,214.0Q476.0,195.0 431.0,195.0Q387.0,195.0 359.5,214.0Q332.0,233.0 314.0,279.0Q296.0,233.0 268.5,214.0Q241.0,195.0 198.0,195.0Z" transform="translate(346, 908)"/>
<path d="M356.0,622.0L356.0,551.0L336.0,551.0Q305.0,544.0 269.0,520.5Q233.0,497.0 201.0,459.5Q169.0,422.0 148.5,372.0Q128.0,322.0 128.0,262.0Q128.0,190.0 149.5,147.5Q171.0,105.0 203.0,87.0Q235.0,69.0 267.0,69.0Q292.0,69.0 309.0,74.0Q326.0,79.0 348.0,92.0L383.0,31.0Q357.0,11.0 326.0,3.0Q295.0,-5.0 264.0,-5.0Q201.0,-5.0 152.5,28.0Q104.0,61.0 76.5,120.5Q49.0,180.0 49.0,260.0Q49.0,359.0 93.5,435.0Q138.0,511.0 208.0,554.0Q191.0,552.0 172.0,551.5Q153.0,551.0 130.0,551.0L-10.0,551.0L-10.0,622.0L356.0,622.0Z" transform="translate(974, 908)"/>
<path d="M848.0,622.0L848.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.5,327.5Q184.0,301.0 142.0,276.0Q246.0,250.0 316.0,207.5Q386.0,165.0 447.0,99.0Q446.0,116.0 445.5,134.0Q445.0,152.0 445.0,171.0L445.0,510.0L458.0,510.0Q540.0,510.0 614.0,488.5Q688.0,467.0 739.0,414.0Q763.0,389.0 777.5,357.5Q792.0,326.0 792.0,288.0Q792.0,255.0 778.5,225.5Q765.0,196.0 735.0,177.0Q705.0,158.0 655.0,158.0Q640.0,158.0 625.5,159.0Q611.0,160.0 597.0,163.0L602.0,234.0Q608.0,233.0 617.0,232.5Q626.0,232.0 636.0,232.0Q685.0,232.0 699.5,251.0Q714.0,270.0 714.0,296.0Q714.0,347.0 662.5,386.0Q611.0,425.0 522.0,434.0L522.0,0.0L445.0,0.0Q404.0,56.0 354.5,98.0Q305.0,140.0 239.5,168.5Q174.0,197.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L848.0,622.0Z" transform="translate(1320, 908)"/>
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(2158, 908)"/>
<path d="M-418.0,789.0L-90.0,789.0L-90.0,722.0L-418.0,722.0L-418.0,789.0Z" transform="translate(2774, 1231)"/>
<path d="M127.0,539.0Q127.0,579.0 170.0,631.0L233.0,596.0Q221.0,583.0 216.0,571.5Q211.0,560.0 211.0,549.0Q211.0,535.0 219.0,526.0Q227.0,517.0 249.5,510.5Q272.0,504.0 316.0,495.0Q420.0,476.0 460.0,436.5Q500.0,397.0 500.0,335.0Q500.0,275.0 453.0,230.0Q406.0,185.0 321.0,172.0Q380.0,147.0 439.0,110.5Q498.0,74.0 553.0,28.0L507.0,-26.0Q448.0,23.0 397.5,56.5Q347.0,90.0 297.5,112.5Q248.0,135.0 192.0,152.0Q136.0,169.0 65.0,185.0L80.0,256.0Q115.0,246.0 151.0,239.5Q187.0,233.0 241.0,233.0Q342.0,233.0 381.5,260.0Q421.0,287.0 421.0,332.0Q421.0,370.0 394.0,391.0Q367.0,412.0 290.0,427.0Q202.0,444.0 164.5,470.5Q127.0,497.0 127.0,539.0Z" transform="translate(2881, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(3473, 1231)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(3473, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(4231, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5066 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M356.0,622.0L356.0,551.0L336.0,551.0Q305.0,544.0 269.0,520.5Q233.0,497.0 201.0,459.5Q169.0,422.0 148.5,372.0Q128.0,322.0 128.0,262.0Q128.0,190.0 149.5,147.5Q171.0,105.0 203.0,87.0Q235.0,69.0 267.0,69.0Q292.0,69.0 309.0,74.0Q326.0,79.0 348.0,92.0L383.0,31.0Q357.0,11.0 326.0,3.0Q295.0,-5.0 263.0,-5.0Q200.0,-5.0 152.0,28.0Q104.0,61.0 76.5,120.5Q49.0,180.0 49.0,260.0Q49.0,331.0 70.0,387.5Q91.0,444.0 125.0,488.0Q159.0,532.0 200.5,562.5Q242.0,593.0 283.0,611.0L283.0,617.0Q283.0,659.0 265.0,679.0Q247.0,699.0 203.0,699.0L183.0,699.0Q118.0,699.0 82.5,708.0Q47.0,717.0 22.0,736.0Q-32.0,777.0 -32.0,859.0Q-32.0,872.0 -30.5,884.5Q-29.0,897.0 -27.0,912.0L47.0,907.0Q43.0,887.0 43.0,869.0Q43.0,847.0 47.5,830.0Q52.0,813.0 62.0,802.0Q76.0,786.0 102.0,778.5Q128.0,771.0 178.0,771.0L182.0,771.0Q235.0,771.0 266.0,763.0Q297.0,755.0 319.0,734.0Q352.0,702.0 355.0,622.0L356.0,622.0Z" transform="translate(0, 908)"/>
<path d="M198.0,195.0Q153.0,195.0 120.5,214.0Q88.0,233.0 69.5,282.0Q51.0,331.0 47.0,422.0L126.0,427.0Q128.0,359.0 136.5,324.5Q145.0,290.0 161.5,278.0Q178.0,266.0 202.0,266.0Q245.0,266.0 259.5,300.5Q274.0,335.0 277.0,423.0L351.0,423.0Q354.0,335.0 370.0,300.5Q386.0,266.0 427.0,266.0Q449.0,266.0 465.0,278.5Q481.0,291.0 490.5,325.5Q500.0,360.0 502.0,427.0L581.0,422.0Q578.0,331.0 559.5,282.0Q541.0,233.0 508.5,214.0Q476.0,195.0 431.0,195.0Q387.0,195.0 359.5,214.0Q332.0,233.0 314.0,279.0Q296.0,233.0 268.5,214.0Q241.0,195.0 198.0,195.0Z" transform="translate(346, 908)"/>
<path d="M356.0,622.0L356.0,551.0L336.0,551.0Q305.0,544.0 269.0,520.5Q233.0,497.0 201.0,459.5Q169.0,422.0 148.5,372.0Q128.0,322.0 128.0,262.0Q128.0,190.0 149.5,147.5Q171.0,105.0 203.0,87.0Q235.0,69.0 267.0,69.0Q292.0,69.0 309.0,74.0Q326.0,79.0 348.0,92.0L383.0,31.0Q357.0,11.0 326.0,3.0Q295.0,-5.0 264.0,-5.0Q201.0,-5.0 152.5,28.0Q104.0,61.0 76.5,120.5Q49.0,180.0 49.0,260.0Q49.0,359.0 93.5,435.0Q138.0,511.0 208.0,554.0Q191.0,552.0 172.0,551.5Q153.0,551.0 130.0,551.0L-10.0,551.0L-10.0,622.0L356.0,622.0Z" transform="translate(974, 908)"/>
<path d="M848.0,622.0L848.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.5,327.5Q184.0,301.0 142.0,276.0Q246.0,250.0 316.0,207.5Q386.0,165.0 447.0,99.0Q446.0,116.0 445.5,134.0Q445.0,152.0 445.0,171.0L445.0,510.0L458.0,510.0Q540.0,510.0 614.0,488.5Q688.0,467.0 739.0,414.0Q763.0,389.0 777.5,357.5Q792.0,326.0 792.0,288.0Q792.0,255.0 778.5,225.5Q765.0,196.0 735.0,177.0Q705.0,158.0 655.0,158.0Q640.0,158.0 625.5,159.0Q611.0,160.0 597.0,163.0L602.0,234.0Q608.0,233.0 617.0,232.5Q626.0,232.0 636.0,232.0Q685.0,232.0 699.5,251.0Q714.0,270.0 714.0,296.0Q714.0,347.0 662.5,386.0Q611.0,425.0 522.0,434.0L522.0,0.0L445.0,0.0Q404.0,56.0 354.5,98.0Q305.0,140.0 239.5,168.5Q174.0,197.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L848.0,622.0Z" transform="translate(1320, 908)"/>
<path d="M419.0,9.0Q353.0,9.0 296.0,30.5Q239.0,52.0 190.5,101.0Q142.0,150.0 102.0,233.0Q62.0,316.0 29.0,440.0L105.0,461.0Q142.0,320.0 186.0,237.5Q230.0,155.0 287.0,120.0Q344.0,85.0 418.0,85.0Q498.0,85.0 545.0,120.5Q592.0,156.0 592.0,217.0Q592.0,238.0 588.0,258.5Q584.0,279.0 571.0,306.0Q522.0,251.0 480.0,230.0Q438.0,209.0 402.0,209.0Q353.0,209.0 324.0,233.0Q307.0,247.0 295.5,272.0Q284.0,297.0 284.0,352.0L284.0,433.0Q232.0,459.0 190.5,498.5Q149.0,538.0 118.0,582.0L179.0,623.0Q204.0,590.0 232.0,560.0Q260.0,530.0 292.0,508.0Q310.0,568.0 355.0,598.5Q400.0,629.0 456.0,629.0Q511.0,629.0 547.5,601.5Q584.0,574.0 584.0,519.0Q584.0,479.0 562.5,452.0Q541.0,425.0 506.0,411.5Q471.0,398.0 431.0,398.0Q393.0,398.0 357.0,407.0L357.0,337.0Q357.0,312.0 366.0,297.0Q375.0,282.0 399.0,282.0Q434.0,282.0 466.0,304.0Q498.0,326.0 546.0,380.0L616.0,383.0Q639.0,346.0 653.0,303.0Q667.0,260.0 667.0,215.0Q667.0,157.0 639.0,110.5Q611.0,64.0 556.0,36.5Q501.0,9.0 419.0,9.0ZM455.0,563.0Q416.0,563.0 392.0,538.0Q368.0,513.0 360.0,474.0Q394.0,464.0 432.0,464.0Q473.0,464.0 491.0,480.5Q509.0,497.0 509.0,520.0Q509.0,540.0 494.5,551.5Q480.0,563.0 455.0,563.0Z" transform="translate(2158, 908)"/>
<path d="M-418.0,789.0L-90.0,789.0L-90.0,722.0L-418.0,722.0L-418.0,789.0Z" transform="translate(2774, 1231)"/>
<path d="M127.0,539.0Q127.0,579.0 170.0,631.0L233.0,596.0Q221.0,583.0 216.0,571.5Q211.0,560.0 211.0,549.0Q211.0,535.0 219.0,526.0Q227.0,517.0 249.5,510.5Q272.0,504.0 316.0,495.0Q420.0,476.0 460.0,436.5Q500.0,397.0 500.0,335.0Q500.0,275.0 453.0,230.0Q406.0,185.0 321.0,172.0Q380.0,147.0 439.0,110.5Q498.0,74.0 553.0,28.0L507.0,-26.0Q448.0,23.0 397.5,56.5Q347.0,90.0 297.5,112.5Q248.0,135.0 192.0,152.0Q136.0,169.0 65.0,185.0L80.0,256.0Q115.0,246.0 151.0,239.5Q187.0,233.0 241.0,233.0Q342.0,233.0 381.5,260.0Q421.0,287.0 421.0,332.0Q421.0,370.0 394.0,391.0Q367.0,412.0 290.0,427.0Q202.0,444.0 164.5,470.5Q127.0,497.0 127.0,539.0Z" transform="translate(2881, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(3473, 1231)"/>
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(3473, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0ZM295.0,-80.0Q354.0,-51.0 417.0,-24.5Q480.0,2.0 545.0,25.0L571.0,-41.0Q524.0,-56.0 476.5,-72.0Q429.0,-88.0 391.0,-105.0Q493.0,-118.0 562.5,-149.0Q632.0,-180.0 685.0,-214.0L649.0,-271.0Q571.0,-221.0 496.0,-195.5Q421.0,-170.0 329.0,-160.0L295.0,-80.0Z" transform="translate(4213, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ক্ক᳭ূঌপয্</span> (Added by SIESTA)</li>


<pre>Expected: kakabeng=0+766|uni1CED=0@-94,-363+0|uni25CC=0+510|uuvowelsignbeng=0+0|lvocalicbeng=5+621|pabeng=6+716|yabeng=7+626|viramabeng=7+0</pre>



<pre>Got     : kakabeng=0+766|uni1CED=0@-94,-363+0|uni25CC=0+510|uuvowelsignbeng=0@19,3+0|lvocalicbeng=5+639|pabeng=6+716|yabeng=7+626|viramabeng=7+0</pre>



<pre>                                                                                                ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3257 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M566.0,-14.0Q553.0,-14.0 539.5,-13.0Q526.0,-12.0 514.0,-9.0L518.0,61.0Q524.0,60.0 531.0,59.5Q538.0,59.0 547.0,59.0Q588.0,59.0 600.5,74.0Q613.0,89.0 613.0,109.0Q613.0,148.0 573.0,178.5Q533.0,209.0 456.0,222.0L456.0,-43.0L379.0,-43.0Q323.0,15.0 262.0,41.0Q201.0,67.0 129.0,79.0L93.0,160.0Q122.0,177.0 161.0,196.5Q200.0,216.0 241.0,235.0Q168.0,275.0 77.0,286.0L39.0,375.0Q119.0,418.0 209.5,455.5Q300.0,493.0 379.0,514.0L379.0,551.0L-10.0,551.0L-10.0,622.0L776.0,622.0L776.0,551.0L455.0,551.0L455.0,517.0Q521.0,506.0 578.0,482.0Q635.0,458.0 670.0,419.0Q705.0,380.0 705.0,325.0Q705.0,287.0 687.0,259.0Q669.0,231.0 631.0,220.0Q658.0,197.0 674.0,167.5Q690.0,138.0 690.0,101.0Q690.0,53.0 659.0,19.5Q628.0,-14.0 566.0,-14.0ZM628.0,333.0Q628.0,372.0 584.5,402.0Q541.0,432.0 456.0,445.0L456.0,294.0Q503.0,285.0 542.0,270.0L543.0,285.0Q548.0,284.0 554.5,283.5Q561.0,283.0 569.0,283.0Q606.0,283.0 617.0,298.0Q628.0,313.0 628.0,333.0ZM379.0,291.0L379.0,440.0Q325.0,424.0 258.5,398.5Q192.0,373.0 137.0,344.0Q190.0,333.0 232.5,312.5Q275.0,292.0 313.0,266.0Q349.0,280.0 379.0,291.0ZM379.0,220.0Q349.0,209.0 314.0,194.0Q279.0,179.0 245.0,163.0Q211.0,147.0 186.0,133.0Q241.0,120.0 289.5,98.5Q338.0,77.0 382.0,38.0Q381.0,55.0 380.0,76.5Q379.0,98.0 379.0,111.0L379.0,220.0Z" transform="translate(0, 908)"/>
<path d="M-312.0,-106.0L-267.0,-46.0L-39.0,-211.0L-84.0,-271.0L-312.0,-106.0Z" transform="translate(672, 545)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(766, 908)"/>
<path d="M-177.0,-241.0Q-207.0,-241.0 -237.5,-230.5Q-268.0,-220.0 -288.0,-197.0Q-308.0,-174.0 -308.0,-137.0Q-308.0,-87.0 -268.0,-62.0Q-228.0,-37.0 -172.0,-36.0L-172.0,8.0L-95.0,8.0L-95.0,-56.0L-128.0,-102.0Q-135.0,-101.0 -144.5,-100.5Q-154.0,-100.0 -165.0,-100.0Q-235.0,-100.0 -235.0,-140.0Q-235.0,-159.0 -219.0,-169.0Q-203.0,-179.0 -179.0,-179.0Q-137.0,-179.0 -103.0,-159.0Q-69.0,-139.0 -38.0,-102.0Q7.0,-122.0 62.5,-154.0Q118.0,-186.0 163.0,-218.0L121.0,-271.0Q84.0,-243.0 46.0,-220.0Q8.0,-197.0 -22.0,-183.0Q-53.0,-211.0 -91.5,-226.0Q-130.0,-241.0 -177.0,-241.0Z" transform="translate(1295, 911)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0Z" transform="translate(1276, 908)"/>
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(1915, 908)"/>
<path d="M636.0,622.0L636.0,551.0L531.0,551.0L531.0,0.0L454.0,0.0Q412.0,56.0 361.0,98.5Q310.0,141.0 243.0,170.0Q176.0,199.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L636.0,622.0ZM454.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.0,327.5Q183.0,301.0 141.0,275.0Q250.0,255.0 324.0,209.0Q398.0,163.0 456.0,99.0Q454.0,134.0 454.0,171.0L454.0,551.0Z" transform="translate(2631, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(3257, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3239 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M566.0,-14.0Q553.0,-14.0 539.5,-13.0Q526.0,-12.0 514.0,-9.0L518.0,61.0Q524.0,60.0 531.0,59.5Q538.0,59.0 547.0,59.0Q588.0,59.0 600.5,74.0Q613.0,89.0 613.0,109.0Q613.0,148.0 573.0,178.5Q533.0,209.0 456.0,222.0L456.0,-43.0L379.0,-43.0Q323.0,15.0 262.0,41.0Q201.0,67.0 129.0,79.0L93.0,160.0Q122.0,177.0 161.0,196.5Q200.0,216.0 241.0,235.0Q168.0,275.0 77.0,286.0L39.0,375.0Q119.0,418.0 209.5,455.5Q300.0,493.0 379.0,514.0L379.0,551.0L-10.0,551.0L-10.0,622.0L776.0,622.0L776.0,551.0L455.0,551.0L455.0,517.0Q521.0,506.0 578.0,482.0Q635.0,458.0 670.0,419.0Q705.0,380.0 705.0,325.0Q705.0,287.0 687.0,259.0Q669.0,231.0 631.0,220.0Q658.0,197.0 674.0,167.5Q690.0,138.0 690.0,101.0Q690.0,53.0 659.0,19.5Q628.0,-14.0 566.0,-14.0ZM628.0,333.0Q628.0,372.0 584.5,402.0Q541.0,432.0 456.0,445.0L456.0,294.0Q503.0,285.0 542.0,270.0L543.0,285.0Q548.0,284.0 554.5,283.5Q561.0,283.0 569.0,283.0Q606.0,283.0 617.0,298.0Q628.0,313.0 628.0,333.0ZM379.0,291.0L379.0,440.0Q325.0,424.0 258.5,398.5Q192.0,373.0 137.0,344.0Q190.0,333.0 232.5,312.5Q275.0,292.0 313.0,266.0Q349.0,280.0 379.0,291.0ZM379.0,220.0Q349.0,209.0 314.0,194.0Q279.0,179.0 245.0,163.0Q211.0,147.0 186.0,133.0Q241.0,120.0 289.5,98.5Q338.0,77.0 382.0,38.0Q381.0,55.0 380.0,76.5Q379.0,98.0 379.0,111.0L379.0,220.0Z" transform="translate(0, 908)"/>
<path d="M-312.0,-106.0L-267.0,-46.0L-39.0,-211.0L-84.0,-271.0L-312.0,-106.0Z" transform="translate(672, 545)"/>
<path d="M254.0,514.0Q284.0,514.0 284.0,486.0Q284.0,457.0 254.0,457.0Q226.0,457.0 226.0,486.0Q226.0,514.0 254.0,514.0ZM125.0,465.0Q154.0,465.0 154.0,436.0Q154.0,407.0 125.0,407.0Q97.0,407.0 97.0,436.0Q97.0,465.0 125.0,465.0ZM384.0,465.0Q413.0,465.0 413.0,436.0Q413.0,407.0 384.0,407.0Q355.0,407.0 355.0,436.0Q355.0,465.0 384.0,465.0ZM429.0,340.0Q458.0,340.0 458.0,312.0Q458.0,283.0 429.0,283.0Q400.0,283.0 400.0,312.0Q400.0,340.0 429.0,340.0ZM81.0,340.0Q109.0,340.0 109.0,312.0Q109.0,283.0 81.0,283.0Q52.0,283.0 52.0,312.0Q52.0,340.0 81.0,340.0ZM125.0,216.0Q154.0,216.0 154.0,187.0Q154.0,158.0 125.0,158.0Q97.0,158.0 97.0,187.0Q97.0,216.0 125.0,216.0ZM384.0,216.0Q413.0,216.0 413.0,187.0Q413.0,158.0 384.0,158.0Q355.0,158.0 355.0,187.0Q355.0,216.0 384.0,216.0ZM254.0,166.0Q284.0,166.0 284.0,137.0Q284.0,108.0 254.0,108.0Q226.0,108.0 226.0,137.0Q226.0,166.0 254.0,166.0Z" transform="translate(766, 908)"/>
<path d="M-177.0,-241.0Q-207.0,-241.0 -237.5,-230.5Q-268.0,-220.0 -288.0,-197.0Q-308.0,-174.0 -308.0,-137.0Q-308.0,-87.0 -268.0,-62.0Q-228.0,-37.0 -172.0,-36.0L-172.0,8.0L-95.0,8.0L-95.0,-56.0L-128.0,-102.0Q-135.0,-101.0 -144.5,-100.5Q-154.0,-100.0 -165.0,-100.0Q-235.0,-100.0 -235.0,-140.0Q-235.0,-159.0 -219.0,-169.0Q-203.0,-179.0 -179.0,-179.0Q-137.0,-179.0 -103.0,-159.0Q-69.0,-139.0 -38.0,-102.0Q7.0,-122.0 62.5,-154.0Q118.0,-186.0 163.0,-218.0L121.0,-271.0Q84.0,-243.0 46.0,-220.0Q8.0,-197.0 -22.0,-183.0Q-53.0,-211.0 -91.5,-226.0Q-130.0,-241.0 -177.0,-241.0Z" transform="translate(1276, 908)"/>
<path d="M204.0,315.0Q252.0,315.0 289.0,298.0Q326.0,281.0 347.5,250.5Q369.0,220.0 369.0,181.0Q369.0,147.0 358.5,121.5Q348.0,96.0 327.0,74.0Q414.0,85.0 463.0,122.0Q512.0,159.0 512.0,221.0Q512.0,257.0 494.5,284.5Q477.0,312.0 431.0,338.0Q385.0,364.0 298.0,394.0Q206.0,426.0 155.0,452.0Q104.0,478.0 83.5,507.0Q63.0,536.0 63.0,576.0Q63.0,611.0 84.0,642.5Q105.0,674.0 141.0,706.0L195.0,665.0Q168.0,640.0 156.0,622.0Q144.0,604.0 144.0,588.0Q144.0,573.0 150.0,560.0Q156.0,547.0 175.5,533.0Q195.0,519.0 234.5,502.5Q274.0,486.0 341.0,464.0Q446.0,430.0 500.5,393.0Q555.0,356.0 574.5,314.5Q594.0,273.0 594.0,222.0Q594.0,161.0 565.0,118.5Q536.0,76.0 486.5,50.0Q437.0,24.0 373.0,12.0Q309.0,0.0 238.0,0.0L219.0,0.0L196.0,68.0Q242.0,84.0 267.0,108.0Q292.0,132.0 292.0,169.0Q292.0,203.0 271.0,224.0Q250.0,245.0 207.0,245.0Q170.0,245.0 153.5,231.0Q137.0,217.0 137.0,196.0Q137.0,186.0 140.0,174.0Q143.0,162.0 148.0,152.0L73.0,135.0Q56.0,172.0 56.0,207.0Q56.0,255.0 93.5,285.0Q131.0,315.0 204.0,315.0Z" transform="translate(1276, 908)"/>
<path d="M726.0,622.0L726.0,551.0L621.0,551.0L621.0,0.0L544.0,0.0L544.0,363.0Q528.0,385.0 514.0,404.5Q500.0,424.0 486.0,440.0L226.0,195.0L167.0,250.0L196.0,277.0Q206.0,291.0 212.5,307.0Q219.0,323.0 219.0,343.0Q219.0,368.0 204.0,383.0Q189.0,398.0 160.0,398.0Q144.0,398.0 129.0,394.0Q114.0,390.0 98.0,380.0L22.0,452.0Q82.0,531.0 147.0,580.0Q212.0,629.0 291.0,629.0Q368.0,629.0 426.0,588.5Q484.0,548.0 547.0,468.0Q545.0,488.0 544.5,510.5Q544.0,533.0 544.0,558.0L544.0,688.0L597.0,688.0L620.0,622.0L726.0,622.0ZM286.0,356.0Q286.0,351.0 286.0,348.0Q298.0,361.0 310.5,373.5Q323.0,386.0 337.0,400.0L437.0,494.0Q372.0,556.0 298.0,556.0Q240.0,556.0 197.0,525.0Q154.0,494.0 120.0,452.0Q146.0,465.0 174.0,465.0Q232.0,465.0 259.0,433.5Q286.0,402.0 286.0,356.0Z" transform="translate(1897, 908)"/>
<path d="M636.0,622.0L636.0,551.0L531.0,551.0L531.0,0.0L454.0,0.0Q412.0,56.0 361.0,98.5Q310.0,141.0 243.0,170.0Q176.0,199.0 84.0,212.0L48.0,303.0Q94.0,334.0 147.0,362.0Q200.0,390.0 252.0,414.0Q214.0,443.0 164.5,465.5Q115.0,488.0 48.0,502.0L70.0,551.0L-10.0,551.0L-10.0,622.0L636.0,622.0ZM454.0,551.0L144.0,551.0Q181.0,538.0 218.0,518.0Q255.0,498.0 286.0,475.0Q317.0,452.0 336.0,432.0L341.0,376.0Q291.0,354.0 237.0,327.5Q183.0,301.0 141.0,275.0Q250.0,255.0 324.0,209.0Q398.0,163.0 456.0,99.0Q454.0,134.0 454.0,171.0L454.0,551.0Z" transform="translate(2613, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(3239, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">7৾ল্তৣ৫ু꣱</span> (Added by SIESTA)</li>


<pre>Expected: seven.beng=0+551|uni09FE=0@0,323+0|latasquishbeng=2+724|llvocalicvowelsignbeng=2@104,0+0|fivebeng=6+592|uvowelsignbeng=6+0|uniA8F1=6@0,323+0</pre>



<pre>Got     : seven.beng=0+551|uni09FE=0@0,323+0|latasquishbeng=2+724|llvocalicvowelsignbeng=2@-33,0+0|fivebeng=6+592|uvowelsignbeng=6+0|uniA8F1=6@0,323+0</pre>



<pre>                                                                                           ^^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1867 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M412.0,633.0L44.0,633.0L44.0,714.0L503.0,714.0L503.0,643.0L232.0,0.0L137.0,0.0L412.0,633.0Z" transform="translate(0, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(551, 1231)"/>
<path d="M484.0,-43.0Q385.0,-43.0 298.0,7.0Q211.0,57.0 145.0,148.0L209.0,192.0Q241.0,150.0 280.0,113.5Q319.0,77.0 369.5,54.0Q420.0,31.0 484.0,31.0Q557.0,31.0 587.5,57.0Q618.0,83.0 618.0,123.0Q618.0,159.0 592.0,184.5Q566.0,210.0 520.0,210.0Q483.0,210.0 467.0,193.5Q451.0,177.0 451.0,156.0Q451.0,149.0 452.0,140.5Q453.0,132.0 456.0,122.0L383.0,108.0Q378.0,124.0 375.5,139.5Q373.0,155.0 373.0,167.0Q373.0,220.0 414.5,248.0Q456.0,276.0 514.0,276.0Q517.0,276.0 519.0,276.0L519.0,370.0Q501.0,389.0 480.5,401.0Q460.0,413.0 437.0,413.0Q417.0,413.0 398.0,400.0Q379.0,387.0 379.0,352.0Q379.0,345.0 379.5,336.5Q380.0,328.0 381.0,320.0L316.0,315.0Q309.0,371.0 277.0,399.5Q245.0,428.0 203.0,428.0Q168.0,428.0 148.0,412.0Q128.0,396.0 128.0,368.0Q128.0,337.0 149.5,316.0Q171.0,295.0 218.0,281.0L192.0,207.0Q121.0,228.0 83.5,268.0Q46.0,308.0 46.0,373.0Q46.0,412.0 66.0,440.5Q86.0,469.0 120.5,484.5Q155.0,500.0 196.0,500.0Q240.0,500.0 275.0,483.5Q310.0,467.0 339.0,431.0Q353.0,457.0 378.0,471.0Q403.0,485.0 432.0,485.0Q457.0,485.0 478.0,476.5Q499.0,468.0 520.0,452.0Q520.0,464.0 519.5,475.5Q519.0,487.0 519.0,498.0L519.0,551.0L-10.0,551.0L-10.0,622.0L734.0,622.0L734.0,551.0L596.0,551.0L596.0,261.0Q644.0,242.0 668.5,203.0Q693.0,164.0 693.0,120.0Q693.0,50.0 643.5,3.5Q594.0,-43.0 484.0,-43.0Z" transform="translate(551, 908)"/>
<path d="M-449.0,-208.0Q-395.0,-208.0 -368.0,-231.0Q-341.0,-254.0 -341.0,-289.0Q-341.0,-301.0 -345.5,-314.0Q-350.0,-327.0 -363.0,-339.0Q-303.0,-331.0 -279.0,-313.5Q-255.0,-296.0 -255.0,-268.0Q-255.0,-251.0 -263.5,-238.0Q-272.0,-225.0 -296.5,-212.0Q-321.0,-199.0 -369.0,-185.0Q-420.0,-169.0 -447.0,-152.5Q-474.0,-136.0 -474.0,-103.0Q-474.0,-86.0 -464.0,-68.0L-408.0,-81.0Q-412.0,-89.0 -412.0,-97.0Q-412.0,-107.0 -397.5,-114.0Q-383.0,-121.0 -334.0,-136.0Q-274.0,-154.0 -242.0,-173.5Q-210.0,-193.0 -198.5,-216.0Q-187.0,-239.0 -187.0,-266.0Q-187.0,-313.0 -219.0,-341.5Q-251.0,-370.0 -302.5,-382.0Q-354.0,-394.0 -415.0,-394.0L-439.0,-394.0L-451.0,-345.0Q-424.0,-337.0 -412.0,-324.5Q-400.0,-312.0 -400.0,-295.0Q-400.0,-280.0 -411.0,-270.5Q-422.0,-261.0 -447.0,-261.0Q-487.0,-261.0 -487.0,-285.0Q-487.0,-294.0 -480.0,-308.0L-540.0,-319.0Q-551.0,-299.0 -551.0,-276.0Q-551.0,-247.0 -525.5,-227.5Q-500.0,-208.0 -449.0,-208.0ZM-142.0,-127.0Q-88.0,-127.0 -61.0,-150.0Q-34.0,-173.0 -34.0,-208.0Q-34.0,-220.0 -38.5,-233.0Q-43.0,-246.0 -56.0,-258.0Q4.0,-250.0 28.0,-232.5Q52.0,-215.0 52.0,-187.0Q52.0,-170.0 43.5,-157.0Q35.0,-144.0 10.5,-131.0Q-14.0,-118.0 -62.0,-104.0Q-113.0,-88.0 -140.0,-71.5Q-167.0,-55.0 -167.0,-22.0Q-167.0,-5.0 -157.0,13.0L-101.0,0.0Q-105.0,-8.0 -105.0,-16.0Q-105.0,-26.0 -90.5,-33.0Q-76.0,-40.0 -27.0,-55.0Q33.0,-73.0 65.0,-92.5Q97.0,-112.0 108.5,-135.0Q120.0,-158.0 120.0,-185.0Q120.0,-232.0 88.0,-260.5Q56.0,-289.0 4.5,-301.0Q-47.0,-313.0 -108.0,-313.0L-132.0,-313.0L-144.0,-264.0Q-117.0,-256.0 -105.0,-243.5Q-93.0,-231.0 -93.0,-214.0Q-93.0,-199.0 -104.0,-189.5Q-115.0,-180.0 -140.0,-180.0Q-180.0,-180.0 -180.0,-204.0Q-180.0,-213.0 -173.0,-227.0L-233.0,-238.0Q-244.0,-218.0 -244.0,-195.0Q-244.0,-166.0 -218.5,-146.5Q-193.0,-127.0 -142.0,-127.0Z" transform="translate(1242, 908)"/>
<path d="M313.0,0.0Q237.0,0.0 177.0,29.0Q117.0,58.0 83.0,113.5Q49.0,169.0 49.0,248.0Q49.0,328.0 93.5,394.5Q138.0,461.0 220.0,518.5Q302.0,576.0 414.0,629.0L453.0,575.0Q443.0,562.0 438.5,548.0Q434.0,534.0 434.0,519.0Q434.0,490.0 457.5,472.5Q481.0,455.0 518.0,455.0Q521.0,455.0 525.0,455.0Q529.0,455.0 533.0,456.0L566.0,400.0Q482.0,354.0 437.0,312.5Q392.0,271.0 392.0,221.0Q392.0,193.0 413.0,168.5Q434.0,144.0 492.0,144.0Q502.0,144.0 511.5,144.5Q521.0,145.0 528.0,146.0L561.0,61.0Q511.0,32.0 447.5,16.0Q384.0,0.0 313.0,0.0ZM320.0,71.0Q365.0,71.0 393.0,75.5Q421.0,80.0 454.0,89.0Q383.0,99.0 349.5,134.5Q316.0,170.0 316.0,222.0Q316.0,275.0 348.5,318.5Q381.0,362.0 446.0,407.0Q407.0,418.0 387.0,446.0Q367.0,474.0 367.0,507.0Q367.0,517.0 368.0,525.0Q262.0,470.0 196.0,398.0Q130.0,326.0 130.0,238.0Q130.0,176.0 158.0,139.0Q186.0,102.0 229.5,86.5Q273.0,71.0 320.0,71.0Z" transform="translate(1275, 908)"/>
<path d="M-286.0,-266.0Q-313.0,-266.0 -345.0,-254.5Q-377.0,-243.0 -399.5,-218.0Q-422.0,-193.0 -422.0,-151.0Q-422.0,-100.0 -383.0,-69.5Q-344.0,-39.0 -274.0,-39.0Q-223.0,-39.0 -172.0,-56.0L-172.0,8.0L-95.0,8.0L-95.0,-45.0Q-95.0,-54.0 -95.5,-65.0Q-96.0,-76.0 -98.0,-88.0Q-53.0,-111.0 -7.5,-144.0Q38.0,-177.0 89.0,-217.0L44.0,-271.0Q-1.0,-234.0 -40.0,-205.0Q-79.0,-176.0 -114.0,-155.0Q-132.0,-199.0 -171.5,-232.5Q-211.0,-266.0 -286.0,-266.0ZM-351.0,-153.0Q-351.0,-181.0 -331.5,-192.5Q-312.0,-204.0 -286.0,-204.0Q-238.0,-204.0 -214.0,-179.0Q-190.0,-154.0 -181.0,-122.0Q-231.0,-103.0 -279.0,-103.0Q-315.0,-103.0 -333.0,-117.0Q-351.0,-131.0 -351.0,-153.0Z" transform="translate(1867, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(1867, 1231)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1867 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M412.0,633.0L44.0,633.0L44.0,714.0L503.0,714.0L503.0,643.0L232.0,0.0L137.0,0.0L412.0,633.0Z" transform="translate(0, 908)"/>
<path d="M16.0,917.0L16.0,856.0Q60.0,850.0 86.0,826.0Q112.0,802.0 112.0,767.0Q112.0,696.0 31.0,677.0Q90.0,651.0 145.0,606.0L113.0,569.0Q69.0,602.0 35.5,622.0Q2.0,642.0 -34.0,655.5Q-70.0,669.0 -122.0,679.0L-112.0,728.0Q-92.0,721.0 -70.5,718.5Q-49.0,716.0 -27.0,716.0Q16.0,716.0 35.0,728.0Q54.0,740.0 54.0,764.0Q54.0,786.0 36.5,798.0Q19.0,810.0 -8.0,810.0Q-33.0,810.0 -42.5,805.0Q-52.0,800.0 -52.0,789.0Q-52.0,784.0 -50.0,778.5Q-48.0,773.0 -47.0,769.0L-101.0,757.0Q-109.0,776.0 -109.0,795.0Q-109.0,845.0 -41.0,856.0L-41.0,869.0L-142.0,869.0L-142.0,917.0L16.0,917.0Z" transform="translate(551, 1231)"/>
<path d="M484.0,-43.0Q385.0,-43.0 298.0,7.0Q211.0,57.0 145.0,148.0L209.0,192.0Q241.0,150.0 280.0,113.5Q319.0,77.0 369.5,54.0Q420.0,31.0 484.0,31.0Q557.0,31.0 587.5,57.0Q618.0,83.0 618.0,123.0Q618.0,159.0 592.0,184.5Q566.0,210.0 520.0,210.0Q483.0,210.0 467.0,193.5Q451.0,177.0 451.0,156.0Q451.0,149.0 452.0,140.5Q453.0,132.0 456.0,122.0L383.0,108.0Q378.0,124.0 375.5,139.5Q373.0,155.0 373.0,167.0Q373.0,220.0 414.5,248.0Q456.0,276.0 514.0,276.0Q517.0,276.0 519.0,276.0L519.0,370.0Q501.0,389.0 480.5,401.0Q460.0,413.0 437.0,413.0Q417.0,413.0 398.0,400.0Q379.0,387.0 379.0,352.0Q379.0,345.0 379.5,336.5Q380.0,328.0 381.0,320.0L316.0,315.0Q309.0,371.0 277.0,399.5Q245.0,428.0 203.0,428.0Q168.0,428.0 148.0,412.0Q128.0,396.0 128.0,368.0Q128.0,337.0 149.5,316.0Q171.0,295.0 218.0,281.0L192.0,207.0Q121.0,228.0 83.5,268.0Q46.0,308.0 46.0,373.0Q46.0,412.0 66.0,440.5Q86.0,469.0 120.5,484.5Q155.0,500.0 196.0,500.0Q240.0,500.0 275.0,483.5Q310.0,467.0 339.0,431.0Q353.0,457.0 378.0,471.0Q403.0,485.0 432.0,485.0Q457.0,485.0 478.0,476.5Q499.0,468.0 520.0,452.0Q520.0,464.0 519.5,475.5Q519.0,487.0 519.0,498.0L519.0,551.0L-10.0,551.0L-10.0,622.0L734.0,622.0L734.0,551.0L596.0,551.0L596.0,261.0Q644.0,242.0 668.5,203.0Q693.0,164.0 693.0,120.0Q693.0,50.0 643.5,3.5Q594.0,-43.0 484.0,-43.0Z" transform="translate(551, 908)"/>
<path d="M-449.0,-208.0Q-395.0,-208.0 -368.0,-231.0Q-341.0,-254.0 -341.0,-289.0Q-341.0,-301.0 -345.5,-314.0Q-350.0,-327.0 -363.0,-339.0Q-303.0,-331.0 -279.0,-313.5Q-255.0,-296.0 -255.0,-268.0Q-255.0,-251.0 -263.5,-238.0Q-272.0,-225.0 -296.5,-212.0Q-321.0,-199.0 -369.0,-185.0Q-420.0,-169.0 -447.0,-152.5Q-474.0,-136.0 -474.0,-103.0Q-474.0,-86.0 -464.0,-68.0L-408.0,-81.0Q-412.0,-89.0 -412.0,-97.0Q-412.0,-107.0 -397.5,-114.0Q-383.0,-121.0 -334.0,-136.0Q-274.0,-154.0 -242.0,-173.5Q-210.0,-193.0 -198.5,-216.0Q-187.0,-239.0 -187.0,-266.0Q-187.0,-313.0 -219.0,-341.5Q-251.0,-370.0 -302.5,-382.0Q-354.0,-394.0 -415.0,-394.0L-439.0,-394.0L-451.0,-345.0Q-424.0,-337.0 -412.0,-324.5Q-400.0,-312.0 -400.0,-295.0Q-400.0,-280.0 -411.0,-270.5Q-422.0,-261.0 -447.0,-261.0Q-487.0,-261.0 -487.0,-285.0Q-487.0,-294.0 -480.0,-308.0L-540.0,-319.0Q-551.0,-299.0 -551.0,-276.0Q-551.0,-247.0 -525.5,-227.5Q-500.0,-208.0 -449.0,-208.0ZM-142.0,-127.0Q-88.0,-127.0 -61.0,-150.0Q-34.0,-173.0 -34.0,-208.0Q-34.0,-220.0 -38.5,-233.0Q-43.0,-246.0 -56.0,-258.0Q4.0,-250.0 28.0,-232.5Q52.0,-215.0 52.0,-187.0Q52.0,-170.0 43.5,-157.0Q35.0,-144.0 10.5,-131.0Q-14.0,-118.0 -62.0,-104.0Q-113.0,-88.0 -140.0,-71.5Q-167.0,-55.0 -167.0,-22.0Q-167.0,-5.0 -157.0,13.0L-101.0,0.0Q-105.0,-8.0 -105.0,-16.0Q-105.0,-26.0 -90.5,-33.0Q-76.0,-40.0 -27.0,-55.0Q33.0,-73.0 65.0,-92.5Q97.0,-112.0 108.5,-135.0Q120.0,-158.0 120.0,-185.0Q120.0,-232.0 88.0,-260.5Q56.0,-289.0 4.5,-301.0Q-47.0,-313.0 -108.0,-313.0L-132.0,-313.0L-144.0,-264.0Q-117.0,-256.0 -105.0,-243.5Q-93.0,-231.0 -93.0,-214.0Q-93.0,-199.0 -104.0,-189.5Q-115.0,-180.0 -140.0,-180.0Q-180.0,-180.0 -180.0,-204.0Q-180.0,-213.0 -173.0,-227.0L-233.0,-238.0Q-244.0,-218.0 -244.0,-195.0Q-244.0,-166.0 -218.5,-146.5Q-193.0,-127.0 -142.0,-127.0Z" transform="translate(1379, 908)"/>
<path d="M313.0,0.0Q237.0,0.0 177.0,29.0Q117.0,58.0 83.0,113.5Q49.0,169.0 49.0,248.0Q49.0,328.0 93.5,394.5Q138.0,461.0 220.0,518.5Q302.0,576.0 414.0,629.0L453.0,575.0Q443.0,562.0 438.5,548.0Q434.0,534.0 434.0,519.0Q434.0,490.0 457.5,472.5Q481.0,455.0 518.0,455.0Q521.0,455.0 525.0,455.0Q529.0,455.0 533.0,456.0L566.0,400.0Q482.0,354.0 437.0,312.5Q392.0,271.0 392.0,221.0Q392.0,193.0 413.0,168.5Q434.0,144.0 492.0,144.0Q502.0,144.0 511.5,144.5Q521.0,145.0 528.0,146.0L561.0,61.0Q511.0,32.0 447.5,16.0Q384.0,0.0 313.0,0.0ZM320.0,71.0Q365.0,71.0 393.0,75.5Q421.0,80.0 454.0,89.0Q383.0,99.0 349.5,134.5Q316.0,170.0 316.0,222.0Q316.0,275.0 348.5,318.5Q381.0,362.0 446.0,407.0Q407.0,418.0 387.0,446.0Q367.0,474.0 367.0,507.0Q367.0,517.0 368.0,525.0Q262.0,470.0 196.0,398.0Q130.0,326.0 130.0,238.0Q130.0,176.0 158.0,139.0Q186.0,102.0 229.5,86.5Q273.0,71.0 320.0,71.0Z" transform="translate(1275, 908)"/>
<path d="M-286.0,-266.0Q-313.0,-266.0 -345.0,-254.5Q-377.0,-243.0 -399.5,-218.0Q-422.0,-193.0 -422.0,-151.0Q-422.0,-100.0 -383.0,-69.5Q-344.0,-39.0 -274.0,-39.0Q-223.0,-39.0 -172.0,-56.0L-172.0,8.0L-95.0,8.0L-95.0,-45.0Q-95.0,-54.0 -95.5,-65.0Q-96.0,-76.0 -98.0,-88.0Q-53.0,-111.0 -7.5,-144.0Q38.0,-177.0 89.0,-217.0L44.0,-271.0Q-1.0,-234.0 -40.0,-205.0Q-79.0,-176.0 -114.0,-155.0Q-132.0,-199.0 -171.5,-232.5Q-211.0,-266.0 -286.0,-266.0ZM-351.0,-153.0Q-351.0,-181.0 -331.5,-192.5Q-312.0,-204.0 -286.0,-204.0Q-238.0,-204.0 -214.0,-179.0Q-190.0,-154.0 -181.0,-122.0Q-231.0,-103.0 -279.0,-103.0Q-315.0,-103.0 -333.0,-117.0Q-351.0,-131.0 -351.0,-153.0Z" transform="translate(1867, 908)"/>
<path d="M-114.0,629.0Q-151.0,629.0 -179.5,647.5Q-208.0,666.0 -240.0,721.0L-199.0,741.0Q-183.0,713.0 -163.5,693.5Q-144.0,674.0 -119.0,674.0Q-104.0,674.0 -93.5,682.0Q-83.0,690.0 -83.0,703.0Q-83.0,718.0 -94.5,731.5Q-106.0,745.0 -138.0,767.0Q-175.0,793.0 -184.0,811.0Q-193.0,829.0 -193.0,847.0Q-193.0,879.0 -169.0,892.0Q-158.0,898.0 -142.5,901.5Q-127.0,905.0 -94.0,905.0L-45.0,905.0L-45.0,861.0L-96.0,861.0Q-118.0,861.0 -131.5,858.0Q-145.0,855.0 -145.0,840.0Q-145.0,832.0 -135.5,822.5Q-126.0,813.0 -96.0,793.0Q-61.0,769.0 -48.0,748.0Q-35.0,727.0 -35.0,699.0Q-35.0,668.0 -56.5,648.5Q-78.0,629.0 -114.0,629.0Z" transform="translate(1867, 1231)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">ঞওহ᳭ণ্ন্</span> (Added by SIESTA)</li>


<pre>Expected: nyabeng=0+1001|obeng=1+738|habeng=2+530|uni1CED=2@-10,-363+0|nnanabeng=4+603|viramabeng=4+0</pre>



<pre>Got     : nyabeng=0+1019|obeng=1+738|habeng=2+530|uni1CED=2@-10,-363+0|nnanabeng=4+603|viramabeng=4+0</pre>



<pre>                      +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2890 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(0, 908)"/>
<path d="M681.0,225.0Q681.0,142.0 619.5,92.0Q558.0,42.0 453.0,42.0Q359.0,42.0 279.0,87.5Q199.0,133.0 136.0,235.5Q73.0,338.0 28.0,507.0L103.0,529.0Q143.0,386.0 192.5,295.0Q242.0,204.0 306.5,161.0Q371.0,118.0 455.0,118.0Q518.0,118.0 559.0,144.5Q600.0,171.0 600.0,228.0Q600.0,255.0 587.0,276.5Q574.0,298.0 552.0,314.0Q520.0,297.0 480.0,282.0L449.0,354.0Q516.0,376.0 553.5,405.5Q591.0,435.0 591.0,482.0Q591.0,558.0 509.0,558.0Q461.0,558.0 420.5,537.5Q380.0,517.0 355.5,489.5Q331.0,462.0 331.0,439.0Q331.0,423.0 341.0,411.5Q351.0,400.0 386.0,395.0L365.0,321.0Q308.0,332.0 279.5,360.0Q251.0,388.0 251.0,431.0Q251.0,465.0 271.5,499.5Q292.0,534.0 328.0,563.5Q364.0,593.0 410.5,611.0Q457.0,629.0 509.0,629.0Q586.0,629.0 628.5,590.0Q671.0,551.0 671.0,483.0Q671.0,445.0 655.5,414.0Q640.0,383.0 613.0,358.0Q681.0,308.0 681.0,225.0Z" transform="translate(1019, 908)"/>
<path d="M540.0,622.0L540.0,551.0L211.0,551.0Q237.0,530.0 247.0,500.0Q324.0,499.0 371.5,472.0Q419.0,445.0 441.5,405.5Q464.0,366.0 464.0,325.0Q464.0,250.0 415.0,203.0Q366.0,156.0 271.0,144.0Q334.0,122.0 404.5,81.5Q475.0,41.0 540.0,-10.0L494.0,-63.0Q432.0,-17.0 380.5,16.5Q329.0,50.0 279.0,75.0Q229.0,100.0 173.0,119.0Q117.0,138.0 46.0,154.0L61.0,223.0Q96.0,213.0 128.5,208.5Q161.0,204.0 207.0,204.0Q278.0,204.0 316.5,221.0Q355.0,238.0 370.0,265.0Q385.0,292.0 385.0,320.0Q385.0,373.0 346.0,401.5Q307.0,430.0 247.0,430.0Q192.0,430.0 170.0,414.5Q148.0,399.0 148.0,370.0Q148.0,362.0 150.0,353.5Q152.0,345.0 154.0,338.0L81.0,323.0Q70.0,354.0 70.0,384.0Q70.0,425.0 96.0,452.0Q122.0,479.0 167.0,491.0Q158.0,511.0 139.5,526.5Q121.0,542.0 92.0,551.0L-10.0,551.0L-10.0,622.0L540.0,622.0Z" transform="translate(1757, 908)"/>
<path d="M-312.0,-106.0L-267.0,-46.0L-39.0,-211.0L-84.0,-271.0L-312.0,-106.0Z" transform="translate(2277, 545)"/>
<path d="M221.0,247.0Q287.0,247.0 337.5,216.5Q388.0,186.0 433.0,136.0Q431.0,156.0 431.0,175.5Q431.0,195.0 431.0,215.0L431.0,394.0Q374.0,470.0 321.0,513.0Q268.0,556.0 213.0,556.0Q178.0,556.0 150.0,536.5Q122.0,517.0 122.0,470.0Q122.0,425.0 157.0,403.0Q192.0,381.0 261.0,373.0L255.0,290.0Q195.0,296.0 146.5,317.0Q98.0,338.0 69.0,376.0Q40.0,414.0 40.0,469.0Q40.0,525.0 63.5,560.0Q87.0,595.0 124.5,612.0Q162.0,629.0 202.0,629.0Q271.0,629.0 324.5,594.0Q378.0,559.0 434.0,497.0Q432.0,515.0 431.5,536.0Q431.0,557.0 431.0,576.0L431.0,688.0L484.0,688.0L507.0,622.0L613.0,622.0L613.0,551.0L508.0,551.0L508.0,0.0L431.0,0.0L431.0,41.0Q387.0,98.0 337.5,137.0Q288.0,176.0 233.0,176.0Q203.0,176.0 187.5,163.5Q172.0,151.0 172.0,129.0Q172.0,109.0 187.5,95.5Q203.0,82.0 236.0,70.0L201.0,1.0Q152.0,19.0 121.5,53.5Q91.0,88.0 91.0,130.0Q91.0,168.0 110.0,194.0Q129.0,220.0 158.5,233.5Q188.0,247.0 221.0,247.0Z" transform="translate(2287, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(2890, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2872 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(0, 908)"/>
<path d="M681.0,225.0Q681.0,142.0 619.5,92.0Q558.0,42.0 453.0,42.0Q359.0,42.0 279.0,87.5Q199.0,133.0 136.0,235.5Q73.0,338.0 28.0,507.0L103.0,529.0Q143.0,386.0 192.5,295.0Q242.0,204.0 306.5,161.0Q371.0,118.0 455.0,118.0Q518.0,118.0 559.0,144.5Q600.0,171.0 600.0,228.0Q600.0,255.0 587.0,276.5Q574.0,298.0 552.0,314.0Q520.0,297.0 480.0,282.0L449.0,354.0Q516.0,376.0 553.5,405.5Q591.0,435.0 591.0,482.0Q591.0,558.0 509.0,558.0Q461.0,558.0 420.5,537.5Q380.0,517.0 355.5,489.5Q331.0,462.0 331.0,439.0Q331.0,423.0 341.0,411.5Q351.0,400.0 386.0,395.0L365.0,321.0Q308.0,332.0 279.5,360.0Q251.0,388.0 251.0,431.0Q251.0,465.0 271.5,499.5Q292.0,534.0 328.0,563.5Q364.0,593.0 410.5,611.0Q457.0,629.0 509.0,629.0Q586.0,629.0 628.5,590.0Q671.0,551.0 671.0,483.0Q671.0,445.0 655.5,414.0Q640.0,383.0 613.0,358.0Q681.0,308.0 681.0,225.0Z" transform="translate(1001, 908)"/>
<path d="M540.0,622.0L540.0,551.0L211.0,551.0Q237.0,530.0 247.0,500.0Q324.0,499.0 371.5,472.0Q419.0,445.0 441.5,405.5Q464.0,366.0 464.0,325.0Q464.0,250.0 415.0,203.0Q366.0,156.0 271.0,144.0Q334.0,122.0 404.5,81.5Q475.0,41.0 540.0,-10.0L494.0,-63.0Q432.0,-17.0 380.5,16.5Q329.0,50.0 279.0,75.0Q229.0,100.0 173.0,119.0Q117.0,138.0 46.0,154.0L61.0,223.0Q96.0,213.0 128.5,208.5Q161.0,204.0 207.0,204.0Q278.0,204.0 316.5,221.0Q355.0,238.0 370.0,265.0Q385.0,292.0 385.0,320.0Q385.0,373.0 346.0,401.5Q307.0,430.0 247.0,430.0Q192.0,430.0 170.0,414.5Q148.0,399.0 148.0,370.0Q148.0,362.0 150.0,353.5Q152.0,345.0 154.0,338.0L81.0,323.0Q70.0,354.0 70.0,384.0Q70.0,425.0 96.0,452.0Q122.0,479.0 167.0,491.0Q158.0,511.0 139.5,526.5Q121.0,542.0 92.0,551.0L-10.0,551.0L-10.0,622.0L540.0,622.0Z" transform="translate(1739, 908)"/>
<path d="M-312.0,-106.0L-267.0,-46.0L-39.0,-211.0L-84.0,-271.0L-312.0,-106.0Z" transform="translate(2259, 545)"/>
<path d="M221.0,247.0Q287.0,247.0 337.5,216.5Q388.0,186.0 433.0,136.0Q431.0,156.0 431.0,175.5Q431.0,195.0 431.0,215.0L431.0,394.0Q374.0,470.0 321.0,513.0Q268.0,556.0 213.0,556.0Q178.0,556.0 150.0,536.5Q122.0,517.0 122.0,470.0Q122.0,425.0 157.0,403.0Q192.0,381.0 261.0,373.0L255.0,290.0Q195.0,296.0 146.5,317.0Q98.0,338.0 69.0,376.0Q40.0,414.0 40.0,469.0Q40.0,525.0 63.5,560.0Q87.0,595.0 124.5,612.0Q162.0,629.0 202.0,629.0Q271.0,629.0 324.5,594.0Q378.0,559.0 434.0,497.0Q432.0,515.0 431.5,536.0Q431.0,557.0 431.0,576.0L431.0,688.0L484.0,688.0L507.0,622.0L613.0,622.0L613.0,551.0L508.0,551.0L508.0,0.0L431.0,0.0L431.0,41.0Q387.0,98.0 337.5,137.0Q288.0,176.0 233.0,176.0Q203.0,176.0 187.5,163.5Q172.0,151.0 172.0,129.0Q172.0,109.0 187.5,95.5Q203.0,82.0 236.0,70.0L201.0,1.0Q152.0,19.0 121.5,53.5Q91.0,88.0 91.0,130.0Q91.0,168.0 110.0,194.0Q129.0,220.0 158.5,233.5Q188.0,247.0 221.0,247.0Z" transform="translate(2269, 908)"/>
<path d="M-134.0,-17.0L112.0,-214.0L69.0,-268.0L-186.0,-81.0L-134.0,-17.0Z" transform="translate(2872, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">উ᳕ঞথহ্ন</span> (Added by SIESTA)</li>


<pre>Expected: ubeng=0+712|uni1CD5=0@-101,-313+0|nyabeng=2+1001|thabeng=3+645|hanabeng=4+751</pre>



<pre>Got     : ubeng=0+712|uni1CD5=0@-101,-313+0|nyabeng=2+1019|thabeng=3+645|hanabeng=4+751</pre>



<pre>                                                        +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3127 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M508.0,622.0Q507.0,663.0 488.5,681.0Q470.0,699.0 428.0,699.0L288.0,699.0Q223.0,699.0 187.5,708.0Q152.0,717.0 127.0,736.0Q73.0,777.0 73.0,859.0Q73.0,872.0 74.5,885.0Q76.0,898.0 78.0,912.0L152.0,907.0Q150.0,895.0 149.0,886.0Q148.0,877.0 148.0,869.0Q148.0,847.0 152.5,830.0Q157.0,813.0 167.0,802.0Q181.0,786.0 207.0,778.5Q233.0,771.0 283.0,771.0L407.0,771.0Q460.0,771.0 491.0,763.0Q522.0,755.0 544.0,734.0Q577.0,702.0 580.0,622.0L722.0,622.0L722.0,551.0L356.0,551.0L356.0,372.0Q356.0,316.0 393.0,316.0Q422.0,316.0 454.0,343.5Q486.0,371.0 529.0,433.0L589.0,442.0Q621.0,395.0 638.5,345.0Q656.0,295.0 656.0,245.0Q656.0,182.0 628.5,132.0Q601.0,82.0 547.5,53.0Q494.0,24.0 417.0,24.0Q329.0,24.0 257.0,66.0Q185.0,108.0 128.5,205.0Q72.0,302.0 29.0,465.0L105.0,485.0Q141.0,346.0 184.5,261.5Q228.0,177.0 284.0,138.5Q340.0,100.0 413.0,100.0Q493.0,100.0 536.5,140.0Q580.0,180.0 580.0,243.0Q580.0,277.0 573.0,303.5Q566.0,330.0 553.0,349.0Q514.0,295.0 473.5,268.5Q433.0,242.0 394.0,242.0Q346.0,242.0 317.0,268.0Q301.0,282.0 290.0,307.5Q279.0,333.0 279.0,393.0L279.0,551.0L-10.0,551.0L-10.0,622.0L508.0,622.0Z" transform="translate(0, 908)"/>
<path d="M-221.0,-107.0Q-219.0,-159.0 -206.5,-181.5Q-194.0,-204.0 -167.0,-204.0Q-142.0,-204.0 -128.0,-184.5Q-114.0,-165.0 -113.0,-105.0L-38.0,-109.0Q-42.0,-201.0 -74.5,-236.0Q-107.0,-271.0 -160.0,-271.0Q-225.0,-271.0 -255.0,-211.0Q-285.0,-271.0 -350.0,-271.0Q-404.0,-271.0 -436.0,-236.0Q-468.0,-201.0 -472.0,-109.0L-398.0,-105.0Q-396.0,-165.0 -382.0,-184.5Q-368.0,-204.0 -343.0,-204.0Q-316.0,-204.0 -303.0,-181.5Q-290.0,-159.0 -289.0,-107.0L-221.0,-107.0Z" transform="translate(611, 595)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(712, 908)"/>
<path d="M211.0,625.0Q306.0,625.0 353.0,578.5Q400.0,532.0 400.0,464.0Q400.0,394.0 348.0,347.0Q296.0,300.0 203.0,282.0Q303.0,253.0 370.5,202.0Q438.0,151.0 475.0,97.0Q474.0,120.0 473.5,143.0Q473.0,166.0 473.0,193.0L473.0,688.0L526.0,688.0L549.0,622.0L655.0,622.0L655.0,551.0L550.0,551.0L550.0,0.0L473.0,0.0Q435.0,55.0 383.0,103.5Q331.0,152.0 264.5,187.5Q198.0,223.0 115.0,238.0L92.0,331.0Q176.0,337.0 226.0,355.5Q276.0,374.0 297.5,402.5Q319.0,431.0 319.0,466.0Q319.0,509.0 291.0,532.0Q263.0,555.0 209.0,555.0Q159.0,555.0 137.5,535.5Q116.0,516.0 116.0,494.0Q116.0,480.0 123.5,468.0Q131.0,456.0 150.0,446.0L106.0,384.0Q78.0,403.0 58.0,430.0Q38.0,457.0 38.0,497.0Q38.0,550.0 83.0,587.5Q128.0,625.0 211.0,625.0Z" transform="translate(1731, 908)"/>
<path d="M580.0,425.0Q641.0,425.0 678.0,390.5Q715.0,356.0 715.0,301.0Q715.0,270.0 702.5,239.0Q690.0,208.0 656.0,181.0Q622.0,154.0 559.0,135.0L535.0,207.0Q584.0,220.0 612.0,241.0Q640.0,262.0 640.0,293.0Q640.0,328.0 620.0,342.0Q600.0,356.0 574.0,356.0Q540.0,356.0 508.5,330.0Q477.0,304.0 453.0,259.0Q435.0,212.0 389.5,182.5Q344.0,153.0 273.0,143.0Q336.0,121.0 406.0,81.0Q476.0,41.0 540.0,-10.0L494.0,-63.0Q432.0,-17.0 380.5,16.5Q329.0,50.0 279.0,75.0Q229.0,100.0 173.0,119.0Q117.0,138.0 46.0,154.0L61.0,223.0Q96.0,213.0 128.5,208.5Q161.0,204.0 207.0,204.0Q278.0,204.0 316.5,221.0Q355.0,238.0 370.0,265.0Q385.0,292.0 385.0,320.0Q385.0,373.0 346.0,401.5Q307.0,430.0 247.0,430.0Q192.0,430.0 170.0,414.5Q148.0,399.0 148.0,370.0Q148.0,362.0 150.0,353.5Q152.0,345.0 154.0,338.0L81.0,323.0Q70.0,354.0 70.0,384.0Q70.0,425.0 96.0,452.0Q122.0,479.0 167.0,491.0Q158.0,511.0 139.5,526.5Q121.0,542.0 92.0,551.0L-10.0,551.0L-10.0,622.0L761.0,622.0L761.0,551.0L211.0,551.0Q237.0,530.0 247.0,500.0Q310.0,499.0 353.5,480.5Q397.0,462.0 422.5,432.0Q448.0,402.0 458.0,368.0Q510.0,425.0 580.0,425.0Z" transform="translate(2376, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3109 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M508.0,622.0Q507.0,663.0 488.5,681.0Q470.0,699.0 428.0,699.0L288.0,699.0Q223.0,699.0 187.5,708.0Q152.0,717.0 127.0,736.0Q73.0,777.0 73.0,859.0Q73.0,872.0 74.5,885.0Q76.0,898.0 78.0,912.0L152.0,907.0Q150.0,895.0 149.0,886.0Q148.0,877.0 148.0,869.0Q148.0,847.0 152.5,830.0Q157.0,813.0 167.0,802.0Q181.0,786.0 207.0,778.5Q233.0,771.0 283.0,771.0L407.0,771.0Q460.0,771.0 491.0,763.0Q522.0,755.0 544.0,734.0Q577.0,702.0 580.0,622.0L722.0,622.0L722.0,551.0L356.0,551.0L356.0,372.0Q356.0,316.0 393.0,316.0Q422.0,316.0 454.0,343.5Q486.0,371.0 529.0,433.0L589.0,442.0Q621.0,395.0 638.5,345.0Q656.0,295.0 656.0,245.0Q656.0,182.0 628.5,132.0Q601.0,82.0 547.5,53.0Q494.0,24.0 417.0,24.0Q329.0,24.0 257.0,66.0Q185.0,108.0 128.5,205.0Q72.0,302.0 29.0,465.0L105.0,485.0Q141.0,346.0 184.5,261.5Q228.0,177.0 284.0,138.5Q340.0,100.0 413.0,100.0Q493.0,100.0 536.5,140.0Q580.0,180.0 580.0,243.0Q580.0,277.0 573.0,303.5Q566.0,330.0 553.0,349.0Q514.0,295.0 473.5,268.5Q433.0,242.0 394.0,242.0Q346.0,242.0 317.0,268.0Q301.0,282.0 290.0,307.5Q279.0,333.0 279.0,393.0L279.0,551.0L-10.0,551.0L-10.0,622.0L508.0,622.0Z" transform="translate(0, 908)"/>
<path d="M-221.0,-107.0Q-219.0,-159.0 -206.5,-181.5Q-194.0,-204.0 -167.0,-204.0Q-142.0,-204.0 -128.0,-184.5Q-114.0,-165.0 -113.0,-105.0L-38.0,-109.0Q-42.0,-201.0 -74.5,-236.0Q-107.0,-271.0 -160.0,-271.0Q-225.0,-271.0 -255.0,-211.0Q-285.0,-271.0 -350.0,-271.0Q-404.0,-271.0 -436.0,-236.0Q-468.0,-201.0 -472.0,-109.0L-398.0,-105.0Q-396.0,-165.0 -382.0,-184.5Q-368.0,-204.0 -343.0,-204.0Q-316.0,-204.0 -303.0,-181.5Q-290.0,-159.0 -289.0,-107.0L-221.0,-107.0Z" transform="translate(611, 595)"/>
<path d="M511.0,628.0Q551.0,628.0 578.0,619.5Q605.0,611.0 625.0,594.0Q639.0,582.0 648.5,566.0Q658.0,550.0 662.0,527.0Q697.0,565.0 735.5,586.0Q774.0,607.0 824.0,607.0Q886.0,607.0 922.5,575.0Q959.0,543.0 959.0,493.0Q959.0,470.0 950.0,442.5Q941.0,415.0 913.0,392.0Q934.0,376.0 949.5,351.5Q965.0,327.0 965.0,291.0Q965.0,242.0 929.0,204.5Q893.0,167.0 823.0,167.0Q765.0,167.0 727.5,191.5Q690.0,216.0 664.0,253.0Q666.0,237.0 666.5,221.0Q667.0,205.0 667.0,190.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0ZM819.0,538.0Q775.0,538.0 736.5,506.5Q698.0,475.0 667.0,423.0L667.0,383.0Q689.0,311.0 728.5,273.5Q768.0,236.0 820.0,236.0Q847.0,236.0 868.0,250.5Q889.0,265.0 889.0,294.0Q889.0,334.0 851.0,358.0Q829.0,350.0 802.0,344.0L785.0,412.0Q838.0,420.0 860.5,440.0Q883.0,460.0 883.0,485.0Q883.0,512.0 864.0,525.0Q845.0,538.0 819.0,538.0Z" transform="translate(712, 908)"/>
<path d="M211.0,625.0Q306.0,625.0 353.0,578.5Q400.0,532.0 400.0,464.0Q400.0,394.0 348.0,347.0Q296.0,300.0 203.0,282.0Q303.0,253.0 370.5,202.0Q438.0,151.0 475.0,97.0Q474.0,120.0 473.5,143.0Q473.0,166.0 473.0,193.0L473.0,688.0L526.0,688.0L549.0,622.0L655.0,622.0L655.0,551.0L550.0,551.0L550.0,0.0L473.0,0.0Q435.0,55.0 383.0,103.5Q331.0,152.0 264.5,187.5Q198.0,223.0 115.0,238.0L92.0,331.0Q176.0,337.0 226.0,355.5Q276.0,374.0 297.5,402.5Q319.0,431.0 319.0,466.0Q319.0,509.0 291.0,532.0Q263.0,555.0 209.0,555.0Q159.0,555.0 137.5,535.5Q116.0,516.0 116.0,494.0Q116.0,480.0 123.5,468.0Q131.0,456.0 150.0,446.0L106.0,384.0Q78.0,403.0 58.0,430.0Q38.0,457.0 38.0,497.0Q38.0,550.0 83.0,587.5Q128.0,625.0 211.0,625.0Z" transform="translate(1713, 908)"/>
<path d="M580.0,425.0Q641.0,425.0 678.0,390.5Q715.0,356.0 715.0,301.0Q715.0,270.0 702.5,239.0Q690.0,208.0 656.0,181.0Q622.0,154.0 559.0,135.0L535.0,207.0Q584.0,220.0 612.0,241.0Q640.0,262.0 640.0,293.0Q640.0,328.0 620.0,342.0Q600.0,356.0 574.0,356.0Q540.0,356.0 508.5,330.0Q477.0,304.0 453.0,259.0Q435.0,212.0 389.5,182.5Q344.0,153.0 273.0,143.0Q336.0,121.0 406.0,81.0Q476.0,41.0 540.0,-10.0L494.0,-63.0Q432.0,-17.0 380.5,16.5Q329.0,50.0 279.0,75.0Q229.0,100.0 173.0,119.0Q117.0,138.0 46.0,154.0L61.0,223.0Q96.0,213.0 128.5,208.5Q161.0,204.0 207.0,204.0Q278.0,204.0 316.5,221.0Q355.0,238.0 370.0,265.0Q385.0,292.0 385.0,320.0Q385.0,373.0 346.0,401.5Q307.0,430.0 247.0,430.0Q192.0,430.0 170.0,414.5Q148.0,399.0 148.0,370.0Q148.0,362.0 150.0,353.5Q152.0,345.0 154.0,338.0L81.0,323.0Q70.0,354.0 70.0,384.0Q70.0,425.0 96.0,452.0Q122.0,479.0 167.0,491.0Q158.0,511.0 139.5,526.5Q121.0,542.0 92.0,551.0L-10.0,551.0L-10.0,622.0L761.0,622.0L761.0,551.0L211.0,551.0Q237.0,530.0 247.0,500.0Q310.0,499.0 353.5,480.5Q397.0,462.0 422.5,432.0Q448.0,402.0 458.0,368.0Q510.0,425.0 580.0,425.0Z" transform="translate(2358, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">টীঋৎ</span> (Added by SIESTA)</li>


<pre>Expected: ttiibeng=0+833|rvocalicbeng=2+835|khandatabeng=3+525</pre>



<pre>Got     : ttiibeng=0+833|rvocalicbeng=2+853|khandatabeng=3+525</pre>



<pre>                                         +
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2211 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M431.0,733.0Q464.0,701.0 467.0,622.0L661.0,622.0Q657.0,687.0 629.0,731.0Q601.0,775.0 556.0,800.5Q511.0,826.0 455.0,837.0Q399.0,848.0 338.0,848.0Q297.0,848.0 261.5,841.5Q226.0,835.0 205.0,823.0Q184.0,811.0 184.0,792.0Q184.0,776.0 200.0,769.0L294.0,769.0Q347.0,769.0 378.0,761.5Q409.0,754.0 431.0,733.0ZM397.0,622.0Q396.0,663.0 377.5,680.5Q359.0,698.0 315.0,698.0L221.0,698.0Q156.0,698.0 120.5,707.0Q85.0,716.0 60.0,735.0Q6.0,776.0 6.0,859.0Q6.0,872.0 7.5,884.5Q9.0,897.0 11.0,912.0L85.0,907.0Q83.0,896.0 82.0,885.0Q81.0,874.0 81.0,863.0Q81.0,815.0 107.0,792.0Q108.0,848.0 167.5,882.5Q227.0,917.0 337.0,917.0Q519.0,917.0 625.0,845.5Q731.0,774.0 741.0,622.0L843.0,622.0L843.0,551.0L738.0,551.0L738.0,0.0L661.0,0.0L661.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L397.0,622.0Z" transform="translate(0, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(833, 908)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(1686, 908)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2193 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M431.0,733.0Q464.0,701.0 467.0,622.0L661.0,622.0Q657.0,687.0 629.0,731.0Q601.0,775.0 556.0,800.5Q511.0,826.0 455.0,837.0Q399.0,848.0 338.0,848.0Q297.0,848.0 261.5,841.5Q226.0,835.0 205.0,823.0Q184.0,811.0 184.0,792.0Q184.0,776.0 200.0,769.0L294.0,769.0Q347.0,769.0 378.0,761.5Q409.0,754.0 431.0,733.0ZM397.0,622.0Q396.0,663.0 377.5,680.5Q359.0,698.0 315.0,698.0L221.0,698.0Q156.0,698.0 120.5,707.0Q85.0,716.0 60.0,735.0Q6.0,776.0 6.0,859.0Q6.0,872.0 7.5,884.5Q9.0,897.0 11.0,912.0L85.0,907.0Q83.0,896.0 82.0,885.0Q81.0,874.0 81.0,863.0Q81.0,815.0 107.0,792.0Q108.0,848.0 167.5,882.5Q227.0,917.0 337.0,917.0Q519.0,917.0 625.0,845.5Q731.0,774.0 741.0,622.0L843.0,622.0L843.0,551.0L738.0,551.0L738.0,0.0L661.0,0.0L661.0,551.0L172.0,551.0L172.0,205.0Q172.0,161.0 177.0,143.0Q182.0,125.0 189.0,117.0Q207.0,96.0 244.0,96.0Q283.0,96.0 318.0,115.0Q353.0,134.0 379.0,162.0Q408.0,193.0 423.5,228.0Q439.0,263.0 439.0,299.0Q439.0,331.0 423.0,347.5Q407.0,364.0 370.0,364.0Q358.0,364.0 344.0,362.0Q330.0,360.0 317.0,357.0L306.0,428.0Q325.0,433.0 345.5,436.0Q366.0,439.0 389.0,439.0Q445.0,439.0 481.0,406.5Q517.0,374.0 517.0,303.0Q517.0,244.0 488.0,188.5Q459.0,133.0 415.0,95.0Q378.0,63.0 334.5,43.5Q291.0,24.0 239.0,24.0Q202.0,24.0 175.5,35.0Q149.0,46.0 132.0,63.0Q116.0,82.0 105.5,109.0Q95.0,136.0 95.0,191.0L95.0,551.0L-10.0,551.0L-10.0,622.0L397.0,622.0Z" transform="translate(0, 908)"/>
<path d="M183.0,430.0Q122.0,430.0 85.5,461.5Q49.0,493.0 49.0,548.0Q49.0,571.0 55.5,592.0Q62.0,613.0 71.0,628.0L147.0,607.0Q140.0,597.0 135.0,582.5Q130.0,568.0 130.0,552.0Q130.0,526.0 144.5,513.5Q159.0,501.0 182.0,501.0Q202.0,501.0 224.0,509.0Q246.0,517.0 269.5,541.0Q293.0,565.0 316.0,612.0L374.0,625.0Q402.0,598.0 431.0,557.5Q460.0,517.0 477.0,478.0L477.0,688.0L530.0,688.0L554.0,622.0L554.0,313.0Q591.0,291.0 629.0,252.5Q667.0,214.0 688.0,178.0Q687.0,195.0 686.0,213.5Q685.0,232.0 685.0,257.0L685.0,688.0L738.0,688.0L762.0,622.0L762.0,73.0L685.0,73.0Q661.0,122.0 627.0,161.5Q593.0,201.0 554.0,231.0L554.0,0.0L477.0,0.0Q449.0,53.0 400.5,100.0Q352.0,147.0 289.5,180.0Q227.0,213.0 155.0,224.0L116.0,316.0Q187.0,357.0 263.0,393.0Q339.0,429.0 416.0,457.0Q406.0,477.0 391.0,499.0Q376.0,521.0 358.0,540.0Q326.0,492.0 282.5,461.0Q239.0,430.0 183.0,430.0ZM477.0,402.0Q413.0,381.0 342.0,350.0Q271.0,319.0 209.0,284.0Q255.0,274.0 307.5,249.0Q360.0,224.0 406.5,188.5Q453.0,153.0 480.0,108.0Q479.0,125.0 478.0,143.5Q477.0,162.0 477.0,187.0L477.0,402.0Z" transform="translate(833, 908)"/>
<path d="M278.0,629.0Q339.0,629.0 377.5,609.0Q416.0,589.0 434.0,557.0Q452.0,525.0 452.0,487.0Q452.0,420.0 412.0,383.0Q372.0,346.0 295.0,346.0Q255.0,346.0 214.0,357.5Q173.0,369.0 139.0,387.0L165.0,454.0Q196.0,438.0 227.0,428.5Q258.0,419.0 289.0,419.0Q374.0,419.0 374.0,485.0Q374.0,517.0 350.0,537.5Q326.0,558.0 279.0,558.0Q207.0,558.0 166.5,519.0Q126.0,480.0 126.0,424.0Q126.0,383.0 143.5,351.5Q161.0,320.0 205.5,290.5Q250.0,261.0 331.0,225.0Q395.0,197.0 435.5,173.0Q476.0,149.0 500.0,124.5Q524.0,100.0 535.5,71.5Q547.0,43.0 552.0,5.0L480.0,-10.0Q474.0,19.0 464.5,39.5Q455.0,60.0 436.0,78.0Q417.0,96.0 382.0,115.5Q347.0,135.0 289.0,160.0Q206.0,197.0 153.0,234.5Q100.0,272.0 75.0,318.5Q50.0,365.0 50.0,426.0Q50.0,481.0 77.5,527.0Q105.0,573.0 156.0,601.0Q207.0,629.0 278.0,629.0Z" transform="translate(1668, 908)"/>
</svg>


</div>
<div class="shaping">

<li>Shaping did not match: <span class="tf">এধষ্টৃঁম়১॑</span> (Added by SIESTA)</li>


<pre>Expected: ebeng=0+740|dhabeng=1+596|ssattabeng=2+565|rvocalicvowelsignbeng=2@-58,0+0|candrabindualtbeng=2+0|manuktabeng=7+622|onebeng=9+592|uni0951=9@-41,323+0</pre>



<pre>Got     : ebeng=0+758|dhabeng=1+596|ssattabeng=2+565|rvocalicvowelsignbeng=2@-58,0+0|candrabindualtbeng=2+0|manuktabeng=7+622|onebeng=9+592|uni0951=9@-41,323+0</pre>



<pre>                   ^^
</pre>


Got: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3133 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(0, 908)"/>
<path d="M240.0,629.0Q252.0,629.0 266.0,627.5Q280.0,626.0 293.0,624.0L287.0,552.0Q281.0,553.0 272.5,553.5Q264.0,554.0 251.0,554.0Q221.0,554.0 204.5,541.5Q188.0,529.0 188.0,509.0Q188.0,490.0 199.5,475.5Q211.0,461.0 240.0,446.0Q285.0,466.0 331.0,484.0Q377.0,502.0 424.0,517.0L424.0,622.0L606.0,622.0L606.0,551.0L501.0,551.0L501.0,0.0L424.0,0.0Q394.0,60.0 341.5,110.5Q289.0,161.0 221.0,196.0Q153.0,231.0 76.0,243.0L37.0,339.0Q105.0,380.0 173.0,414.0Q143.0,436.0 126.0,463.0Q109.0,490.0 109.0,524.0Q109.0,565.0 141.0,597.0Q173.0,629.0 240.0,629.0ZM130.0,304.0Q181.0,293.0 238.0,266.5Q295.0,240.0 345.5,200.0Q396.0,160.0 427.0,108.0Q426.0,126.0 425.0,145.0Q424.0,164.0 424.0,189.0L424.0,439.0Q352.0,414.0 274.0,379.5Q196.0,345.0 130.0,304.0Z" transform="translate(758, 908)"/>
<path d="M301.0,-12.0Q214.0,-12.0 166.5,28.5Q119.0,69.0 119.0,139.0Q119.0,177.0 142.0,209.5Q165.0,242.0 207.0,269.0Q137.0,277.0 91.5,318.5Q46.0,360.0 46.0,436.0Q46.0,472.0 59.0,501.0Q72.0,530.0 94.0,552.0Q80.0,551.0 65.5,551.0Q51.0,551.0 37.0,551.0L-10.0,551.0L-10.0,622.0L393.0,622.0Q392.0,663.0 373.5,681.0Q355.0,699.0 313.0,699.0L226.0,699.0Q161.0,699.0 125.5,708.0Q90.0,717.0 65.0,736.0Q11.0,777.0 11.0,859.0Q11.0,872.0 12.5,884.5Q14.0,897.0 16.0,912.0L90.0,907.0Q86.0,887.0 86.0,869.0Q86.0,847.0 90.5,830.0Q95.0,813.0 105.0,802.0Q119.0,786.0 145.5,778.5Q172.0,771.0 221.0,771.0L292.0,771.0Q345.0,771.0 376.0,763.0Q407.0,755.0 429.0,734.0Q462.0,702.0 465.0,622.0L575.0,622.0L575.0,551.0L445.0,551.0Q476.0,512.0 476.0,453.0Q476.0,393.0 444.5,353.0Q413.0,313.0 365.0,291.0Q276.0,243.0 236.0,210.5Q196.0,178.0 196.0,136.0Q196.0,89.0 228.5,74.0Q261.0,59.0 305.0,59.0Q367.0,59.0 404.0,84.0Q441.0,109.0 441.0,139.0Q441.0,155.0 432.0,166.0Q423.0,177.0 403.0,190.0L452.0,246.0Q492.0,223.0 507.0,199.5Q522.0,176.0 522.0,147.0Q522.0,105.0 495.5,68.5Q469.0,32.0 420.0,10.0Q371.0,-12.0 301.0,-12.0ZM274.0,554.0Q216.0,554.0 176.0,530.0Q293.0,480.0 386.0,403.0Q400.0,428.0 400.0,457.0Q400.0,504.0 368.0,529.0Q336.0,554.0 274.0,554.0ZM122.0,436.0Q122.0,390.0 155.0,362.5Q188.0,335.0 248.0,335.0Q299.0,335.0 338.0,357.0Q243.0,432.0 131.0,480.0Q122.0,460.0 122.0,436.0Z" transform="translate(1354, 908)"/>
<path d="M-355.0,-80.0Q-296.0,-51.0 -233.0,-24.5Q-170.0,2.0 -105.0,25.0L-79.0,-41.0Q-126.0,-56.0 -173.5,-72.0Q-221.0,-88.0 -259.0,-105.0Q-157.0,-118.0 -87.5,-149.0Q-18.0,-180.0 35.0,-214.0L-1.0,-271.0Q-79.0,-221.0 -154.0,-195.5Q-229.0,-170.0 -321.0,-160.0L-355.0,-80.0Z" transform="translate(1861, 908)"/>
<path d="M-109.0,874.0Q-109.0,854.0 -121.5,843.0Q-134.0,832.0 -153.0,832.0Q-175.0,832.0 -186.0,844.5Q-197.0,857.0 -197.0,877.0Q-197.0,893.0 -186.5,905.0Q-176.0,917.0 -154.0,917.0Q-109.0,917.0 -109.0,874.0ZM18.0,905.0Q11.0,831.0 -28.5,783.0Q-68.0,735.0 -150.0,735.0Q-232.0,735.0 -274.0,783.0Q-316.0,831.0 -324.0,904.0L-256.0,913.0Q-251.0,860.0 -228.0,829.5Q-205.0,799.0 -154.0,799.0Q-106.0,799.0 -81.0,828.5Q-56.0,858.0 -51.0,914.0L18.0,905.0Z" transform="translate(1919, 908)"/>
<path d="M632.0,622.0L632.0,551.0L527.0,551.0L527.0,0.0L450.0,0.0L450.0,109.0Q418.0,156.0 385.0,195.0Q352.0,234.0 315.5,257.5Q279.0,281.0 236.0,281.0Q199.0,281.0 173.5,262.0Q148.0,243.0 148.0,205.0Q148.0,172.0 172.0,149.5Q196.0,127.0 243.0,111.0L218.0,34.0Q137.0,63.0 101.5,108.5Q66.0,154.0 66.0,208.0Q66.0,256.0 89.5,288.0Q113.0,320.0 148.0,336.5Q183.0,353.0 218.0,353.0Q210.0,422.0 169.5,453.5Q129.0,485.0 38.0,494.0L48.0,551.0L-10.0,551.0L-10.0,622.0L632.0,622.0ZM450.0,551.0L116.0,551.0Q199.0,540.0 246.5,489.5Q294.0,439.0 299.0,342.0Q348.0,327.0 385.0,294.0Q422.0,261.0 452.0,219.0Q451.0,234.0 450.5,249.5Q450.0,265.0 450.0,281.0L450.0,551.0ZM225.0,-127.0Q200.0,-127.0 182.5,-111.0Q165.0,-95.0 165.0,-69.0Q165.0,-43.0 182.5,-26.0Q200.0,-9.0 225.0,-9.0Q250.0,-9.0 267.5,-26.0Q285.0,-43.0 285.0,-69.0Q285.0,-95.0 267.5,-111.0Q250.0,-127.0 225.0,-127.0Z" transform="translate(1919, 908)"/>
<path d="M287.0,0.0Q202.0,0.0 162.5,36.5Q123.0,73.0 123.0,122.0Q123.0,161.0 148.0,194.0Q173.0,227.0 234.0,244.0L263.0,167.0Q232.0,160.0 218.5,149.0Q205.0,138.0 205.0,120.0Q205.0,100.0 225.5,87.5Q246.0,75.0 286.0,75.0Q348.0,75.0 382.0,105.0Q416.0,135.0 416.0,181.0Q416.0,211.0 404.0,234.5Q392.0,258.0 364.0,284.0Q336.0,310.0 287.0,344.0Q225.0,388.0 189.5,418.0Q154.0,448.0 139.5,473.5Q125.0,499.0 125.0,529.0Q125.0,552.0 138.5,579.5Q152.0,607.0 177.0,631.0L243.0,596.0Q229.0,581.0 220.0,566.0Q211.0,551.0 211.0,536.0Q211.0,518.0 219.0,502.5Q227.0,487.0 254.5,464.5Q282.0,442.0 338.0,403.0Q396.0,364.0 430.0,331.0Q464.0,298.0 478.5,263.5Q493.0,229.0 493.0,182.0Q493.0,126.0 466.5,85.0Q440.0,44.0 393.5,22.0Q347.0,0.0 287.0,0.0Z" transform="translate(2541, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(3092, 1231)"/>
</svg>
 Expected: <svg class="shaping-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3115 2325" transform="matrix(1 0 0 -1 0 0)">
<path d="M511.0,628.0Q552.0,628.0 579.5,619.5Q607.0,611.0 626.0,594.0Q645.0,578.0 656.0,554.5Q667.0,531.0 667.0,490.0L667.0,0.0L592.0,0.0Q579.0,45.0 552.5,66.0Q526.0,87.0 481.0,87.0Q445.0,87.0 414.0,83.0Q383.0,79.0 349.5,74.5Q316.0,70.0 272.0,70.0Q238.0,70.0 199.0,77.5Q160.0,85.0 125.0,106.0Q90.0,127.0 68.0,168.5Q46.0,210.0 46.0,278.0Q46.0,302.0 50.0,328.5Q54.0,355.0 58.0,377.0L135.0,366.0Q131.0,351.0 127.5,330.0Q124.0,309.0 124.0,280.0Q124.0,221.0 146.5,192.0Q169.0,163.0 204.0,153.5Q239.0,144.0 276.0,144.0Q326.0,144.0 367.5,152.5Q409.0,161.0 461.0,161.0Q504.0,161.0 536.0,148.5Q568.0,136.0 590.0,106.0L590.0,463.0Q590.0,500.0 585.0,516.0Q580.0,532.0 569.0,542.0Q551.0,557.0 514.0,557.0Q478.0,557.0 445.5,541.0Q413.0,525.0 387.5,500.0Q362.0,475.0 347.5,446.5Q333.0,418.0 333.0,393.0Q333.0,378.0 343.5,361.5Q354.0,345.0 392.0,345.0Q412.0,345.0 434.0,348.0L441.0,278.0Q419.0,270.0 376.0,270.0Q327.0,270.0 290.5,300.0Q254.0,330.0 254.0,392.0Q254.0,432.0 274.5,473.5Q295.0,515.0 331.0,550.0Q367.0,585.0 413.5,606.5Q460.0,628.0 511.0,628.0Z" transform="translate(0, 908)"/>
<path d="M240.0,629.0Q252.0,629.0 266.0,627.5Q280.0,626.0 293.0,624.0L287.0,552.0Q281.0,553.0 272.5,553.5Q264.0,554.0 251.0,554.0Q221.0,554.0 204.5,541.5Q188.0,529.0 188.0,509.0Q188.0,490.0 199.5,475.5Q211.0,461.0 240.0,446.0Q285.0,466.0 331.0,484.0Q377.0,502.0 424.0,517.0L424.0,622.0L606.0,622.0L606.0,551.0L501.0,551.0L501.0,0.0L424.0,0.0Q394.0,60.0 341.5,110.5Q289.0,161.0 221.0,196.0Q153.0,231.0 76.0,243.0L37.0,339.0Q105.0,380.0 173.0,414.0Q143.0,436.0 126.0,463.0Q109.0,490.0 109.0,524.0Q109.0,565.0 141.0,597.0Q173.0,629.0 240.0,629.0ZM130.0,304.0Q181.0,293.0 238.0,266.5Q295.0,240.0 345.5,200.0Q396.0,160.0 427.0,108.0Q426.0,126.0 425.0,145.0Q424.0,164.0 424.0,189.0L424.0,439.0Q352.0,414.0 274.0,379.5Q196.0,345.0 130.0,304.0Z" transform="translate(740, 908)"/>
<path d="M301.0,-12.0Q214.0,-12.0 166.5,28.5Q119.0,69.0 119.0,139.0Q119.0,177.0 142.0,209.5Q165.0,242.0 207.0,269.0Q137.0,277.0 91.5,318.5Q46.0,360.0 46.0,436.0Q46.0,472.0 59.0,501.0Q72.0,530.0 94.0,552.0Q80.0,551.0 65.5,551.0Q51.0,551.0 37.0,551.0L-10.0,551.0L-10.0,622.0L393.0,622.0Q392.0,663.0 373.5,681.0Q355.0,699.0 313.0,699.0L226.0,699.0Q161.0,699.0 125.5,708.0Q90.0,717.0 65.0,736.0Q11.0,777.0 11.0,859.0Q11.0,872.0 12.5,884.5Q14.0,897.0 16.0,912.0L90.0,907.0Q86.0,887.0 86.0,869.0Q86.0,847.0 90.5,830.0Q95.0,813.0 105.0,802.0Q119.0,786.0 145.5,778.5Q172.0,771.0 221.0,771.0L292.0,771.0Q345.0,771.0 376.0,763.0Q407.0,755.0 429.0,734.0Q462.0,702.0 465.0,622.0L575.0,622.0L575.0,551.0L445.0,551.0Q476.0,512.0 476.0,453.0Q476.0,393.0 444.5,353.0Q413.0,313.0 365.0,291.0Q276.0,243.0 236.0,210.5Q196.0,178.0 196.0,136.0Q196.0,89.0 228.5,74.0Q261.0,59.0 305.0,59.0Q367.0,59.0 404.0,84.0Q441.0,109.0 441.0,139.0Q441.0,155.0 432.0,166.0Q423.0,177.0 403.0,190.0L452.0,246.0Q492.0,223.0 507.0,199.5Q522.0,176.0 522.0,147.0Q522.0,105.0 495.5,68.5Q469.0,32.0 420.0,10.0Q371.0,-12.0 301.0,-12.0ZM274.0,554.0Q216.0,554.0 176.0,530.0Q293.0,480.0 386.0,403.0Q400.0,428.0 400.0,457.0Q400.0,504.0 368.0,529.0Q336.0,554.0 274.0,554.0ZM122.0,436.0Q122.0,390.0 155.0,362.5Q188.0,335.0 248.0,335.0Q299.0,335.0 338.0,357.0Q243.0,432.0 131.0,480.0Q122.0,460.0 122.0,436.0Z" transform="translate(1336, 908)"/>
<path d="M-355.0,-80.0Q-296.0,-51.0 -233.0,-24.5Q-170.0,2.0 -105.0,25.0L-79.0,-41.0Q-126.0,-56.0 -173.5,-72.0Q-221.0,-88.0 -259.0,-105.0Q-157.0,-118.0 -87.5,-149.0Q-18.0,-180.0 35.0,-214.0L-1.0,-271.0Q-79.0,-221.0 -154.0,-195.5Q-229.0,-170.0 -321.0,-160.0L-355.0,-80.0Z" transform="translate(1843, 908)"/>
<path d="M-109.0,874.0Q-109.0,854.0 -121.5,843.0Q-134.0,832.0 -153.0,832.0Q-175.0,832.0 -186.0,844.5Q-197.0,857.0 -197.0,877.0Q-197.0,893.0 -186.5,905.0Q-176.0,917.0 -154.0,917.0Q-109.0,917.0 -109.0,874.0ZM18.0,905.0Q11.0,831.0 -28.5,783.0Q-68.0,735.0 -150.0,735.0Q-232.0,735.0 -274.0,783.0Q-316.0,831.0 -324.0,904.0L-256.0,913.0Q-251.0,860.0 -228.0,829.5Q-205.0,799.0 -154.0,799.0Q-106.0,799.0 -81.0,828.5Q-56.0,858.0 -51.0,914.0L18.0,905.0Z" transform="translate(1901, 908)"/>
<path d="M632.0,622.0L632.0,551.0L527.0,551.0L527.0,0.0L450.0,0.0L450.0,109.0Q418.0,156.0 385.0,195.0Q352.0,234.0 315.5,257.5Q279.0,281.0 236.0,281.0Q199.0,281.0 173.5,262.0Q148.0,243.0 148.0,205.0Q148.0,172.0 172.0,149.5Q196.0,127.0 243.0,111.0L218.0,34.0Q137.0,63.0 101.5,108.5Q66.0,154.0 66.0,208.0Q66.0,256.0 89.5,288.0Q113.0,320.0 148.0,336.5Q183.0,353.0 218.0,353.0Q210.0,422.0 169.5,453.5Q129.0,485.0 38.0,494.0L48.0,551.0L-10.0,551.0L-10.0,622.0L632.0,622.0ZM450.0,551.0L116.0,551.0Q199.0,540.0 246.5,489.5Q294.0,439.0 299.0,342.0Q348.0,327.0 385.0,294.0Q422.0,261.0 452.0,219.0Q451.0,234.0 450.5,249.5Q450.0,265.0 450.0,281.0L450.0,551.0ZM225.0,-127.0Q200.0,-127.0 182.5,-111.0Q165.0,-95.0 165.0,-69.0Q165.0,-43.0 182.5,-26.0Q200.0,-9.0 225.0,-9.0Q250.0,-9.0 267.5,-26.0Q285.0,-43.0 285.0,-69.0Q285.0,-95.0 267.5,-111.0Q250.0,-127.0 225.0,-127.0Z" transform="translate(1901, 908)"/>
<path d="M287.0,0.0Q202.0,0.0 162.5,36.5Q123.0,73.0 123.0,122.0Q123.0,161.0 148.0,194.0Q173.0,227.0 234.0,244.0L263.0,167.0Q232.0,160.0 218.5,149.0Q205.0,138.0 205.0,120.0Q205.0,100.0 225.5,87.5Q246.0,75.0 286.0,75.0Q348.0,75.0 382.0,105.0Q416.0,135.0 416.0,181.0Q416.0,211.0 404.0,234.5Q392.0,258.0 364.0,284.0Q336.0,310.0 287.0,344.0Q225.0,388.0 189.5,418.0Q154.0,448.0 139.5,473.5Q125.0,499.0 125.0,529.0Q125.0,552.0 138.5,579.5Q152.0,607.0 177.0,631.0L243.0,596.0Q229.0,581.0 220.0,566.0Q211.0,551.0 211.0,536.0Q211.0,518.0 219.0,502.5Q227.0,487.0 254.5,464.5Q282.0,442.0 338.0,403.0Q396.0,364.0 430.0,331.0Q464.0,298.0 478.5,263.5Q493.0,229.0 493.0,182.0Q493.0,126.0 466.5,85.0Q440.0,44.0 393.5,22.0Q347.0,0.0 287.0,0.0Z" transform="translate(2523, 908)"/>
<path d="M-219.0,917.0L-219.0,626.0L-290.0,626.0L-290.0,917.0L-219.0,917.0Z" transform="translate(3074, 1231)"/>
</svg>


</div> [code: shaping-regression]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* aabeng
	* abeng
	* bababeng
	* badabeng
	* badarabeng
	* badhabeng
	* barabeng
	* barasquishbeng
	* barubeng
	* cacabeng and 192 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1), uni1CE1.UI (unencoded) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<898.0,622.0>> -> L<<898.0,622.0>--<898.0,622.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* mabeng (U+09AE): L<<450.0,551.0>--<116.0,551.0>>/B<<116.0,551.0>-<199.0,540.0>-<246.5,489.5>> = 7.549421768263246 

	* sabeng (U+09B8): L<<510.0,551.0>--<107.0,551.0>>/B<<107.0,551.0>-<183.0,540.0>-<226.5,518.0>> = 8.235619324209488 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[15] NotoSansBengali-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1012, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* aabeng
	* abeng
	* aubeng
	* bababeng
	* babhabeng
	* badabeng
	* badarabeng
	* badhabeng
	* balabeng
	* barabeng and 305 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1), uni1CE1.UI (unencoded) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
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

	* C (U+0043): X=485.5,Y=-2.0 (should be at baseline 0?)

	* G (U+0047): X=531.0,Y=0.5 (should be at baseline 0?) 

	* 68 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* W (U+0057): B<<257.0,182.5>-<263.0,150.0>-<266.0,126.0>>/B<<266.0,126.0>-<269.0,151.0>-<275.0,184.0>> = 13.967789761532726

	* W (U+0057): B<<678.0,182.0>-<684.0,150.0>-<687.0,126.0>>/B<<687.0,126.0>-<690.0,151.0>-<695.5,183.0>> = 13.967789761532726

	* Wacute (U+1E82): B<<257.0,182.5>-<263.0,150.0>-<266.0,126.0>>/B<<266.0,126.0>-<269.0,151.0>-<275.0,184.0>> = 13.967789761532726

	* Wacute (U+1E82): B<<678.0,182.0>-<684.0,150.0>-<687.0,126.0>>/B<<687.0,126.0>-<690.0,151.0>-<695.5,183.0>> = 13.967789761532726

	* Wcircumflex (U+0174): B<<257.0,182.5>-<263.0,150.0>-<266.0,126.0>>/B<<266.0,126.0>-<269.0,151.0>-<275.0,184.0>> = 13.967789761532726

	* Wcircumflex (U+0174): B<<678.0,182.0>-<684.0,150.0>-<687.0,126.0>>/B<<687.0,126.0>-<690.0,151.0>-<695.5,183.0>> = 13.967789761532726

	* Wdieresis (U+1E84): B<<257.0,182.5>-<263.0,150.0>-<266.0,126.0>>/B<<266.0,126.0>-<269.0,151.0>-<275.0,184.0>> = 13.967789761532726

	* Wdieresis (U+1E84): B<<678.0,182.0>-<684.0,150.0>-<687.0,126.0>>/B<<687.0,126.0>-<690.0,151.0>-<695.5,183.0>> = 13.967789761532726

	* Wgrave (U+1E80): B<<257.0,182.5>-<263.0,150.0>-<266.0,126.0>>/B<<266.0,126.0>-<269.0,151.0>-<275.0,184.0>> = 13.967789761532726

	* Wgrave (U+1E80): B<<678.0,182.0>-<684.0,150.0>-<687.0,126.0>>/B<<687.0,126.0>-<690.0,151.0>-<695.5,183.0>> = 13.967789761532726 

	* 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[16] NotoSansBengali-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1012, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* cacabeng
	* cachababeng
	* cachabeng and cacharabeng
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali Thin' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (U+1CE1), uni1CE1.UI (unencoded) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<848.0,622.0>> -> L<<848.0,622.0>--<848.0,622.0>>

	* rrvocalicbeng (U+09E0): L<<484.0,676.0>--<489.0,622.0>> -> L<<489.0,622.0>--<489.0,318.0>>

	* rrvocalicbeng (U+09E0): L<<677.0,676.0>--<682.0,622.0>> -> L<<682.0,622.0>--<682.0,72.0>>

	* rvocalicbeng (U+098B): L<<484.0,676.0>--<489.0,622.0>> -> L<<489.0,622.0>--<489.0,318.0>> 

	* rvocalicbeng (U+098B): L<<677.0,676.0>--<682.0,622.0>> -> L<<682.0,622.0>--<682.0,72.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* chabeng (U+099B): B<<500.5,178.5>-<433.0,122.0>-<312.0,117.0>>/B<<312.0,117.0>-<473.0,95.0>-<642.0,-1.0>> = 10.147294214439293

	* ghabeng (U+0998): B<<164.5,329.0>-<209.0,363.0>-<255.0,389.0>>/B<<255.0,389.0>-<243.0,384.0>-<230.5,381.5>> = 6.856024055205275

	* mabeng (U+09AE): L<<449.0,596.0>--<51.0,596.0>>/B<<51.0,596.0>-<136.0,582.0>-<179.0,547.5>> = 9.352979250093227

	* sabeng (U+09B8): L<<517.0,596.0>--<44.0,596.0>>/B<<44.0,596.0>-<113.0,582.0>-<160.5,564.0>> = 11.469530332866904 

	* twobeng (U+09E8): B<<252.0,187.0>-<242.0,187.0>-<233.0,188.0>>/B<<233.0,188.0>-<313.0,158.0>-<390.0,105.5>> = 14.21585347367354 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* exclam.beng (U+0021): L<<167.0,174.0>--<165.0,714.0>>

	* exclam.beng (U+0021): L<<193.0,714.0>--<191.0,174.0>>

	* exclamdown (U+00A1): L<<122.0,354.0>--<124.0,-186.0>> 

	* exclamdown (U+00A1): L<<96.0,-186.0>--<98.0,354.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[14] NotoSansBengaliUI-Black.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali UI Black' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (unencoded), uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 llvocalicvowelsignUIbeng (U+09E3), lvocalicvowelsignUIbeng (U+09E2) and rrvocalicvowelsignUIbeng (U+09C4) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* V (U+0056): B<<339.5,236.0>-<346.0,204.0>-<347.0,184.0>>/B<<347.0,184.0>-<349.0,204.0>-<354.5,235.5>> = 8.57299836361137

	* W (U+0057): B<<308.0,211.5>-<313.0,185.0>-<315.0,167.0>>/B<<315.0,167.0>-<319.0,197.0>-<325.5,236.0>> = 13.934835114501363

	* W (U+0057): B<<527.0,442.0>-<523.0,468.0>-<521.0,486.0>>/B<<521.0,486.0>-<519.0,468.0>-<514.5,442.0>> = 12.680383491819825

	* W (U+0057): B<<714.0,235.0>-<721.0,196.0>-<724.0,167.0>>/B<<724.0,167.0>-<727.0,192.0>-<734.0,229.0>> = 12.748914526401432

	* Wacute (U+1E82): B<<308.0,211.5>-<313.0,185.0>-<315.0,167.0>>/B<<315.0,167.0>-<319.0,197.0>-<325.5,236.0>> = 13.934835114501363

	* Wacute (U+1E82): B<<527.0,442.0>-<523.0,468.0>-<521.0,486.0>>/B<<521.0,486.0>-<519.0,468.0>-<514.5,442.0>> = 12.680383491819825

	* Wacute (U+1E82): B<<714.0,235.0>-<721.0,196.0>-<724.0,167.0>>/B<<724.0,167.0>-<727.0,192.0>-<734.0,229.0>> = 12.748914526401432

	* Wcircumflex (U+0174): B<<308.0,211.5>-<313.0,185.0>-<315.0,167.0>>/B<<315.0,167.0>-<319.0,197.0>-<325.5,236.0>> = 13.934835114501363

	* Wcircumflex (U+0174): B<<527.0,442.0>-<523.0,468.0>-<521.0,486.0>>/B<<521.0,486.0>-<519.0,468.0>-<514.5,442.0>> = 12.680383491819825

	* Wcircumflex (U+0174): B<<714.0,235.0>-<721.0,196.0>-<724.0,167.0>>/B<<724.0,167.0>-<727.0,192.0>-<734.0,229.0>> = 12.748914526401432 

	* 9 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[14] NotoSansBengaliUI-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (unencoded), uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 llvocalicvowelsignUIbeng (U+09E3), lvocalicvowelsignUIbeng (U+09E2) and rrvocalicvowelsignUIbeng (U+09C4) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* five.beng (U+0035): X=127.0,Y=-0.5 (should be at baseline 0?)

	* C (U+0043): X=482.0,Y=-1.0 (should be at baseline 0?)

	* G (U+0047): X=527.5,Y=1.0 (should be at baseline 0?)

	* c (U+0063): X=394.5,Y=-0.5 (should be at baseline 0?)

	* e (U+0065): X=432.5,Y=-0.5 (should be at baseline 0?)

	* g (U+0067): X=555.0,Y=-1.0 (should be at baseline 0?)

	* h (U+0068): X=295.0,Y=537.0 (should be at x-height 536?)

	* m (U+006D): X=288.5,Y=537.0 (should be at x-height 536?)

	* m (U+006D): X=481.0,Y=536.5 (should be at x-height 536?)

	* m (U+006D): X=627.5,Y=537.0 (should be at x-height 536?) 

	* 59 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* W (U+0057): B<<266.0,196.0>-<272.0,161.0>-<275.0,137.0>>/B<<275.0,137.0>-<278.0,162.0>-<284.0,196.5>> = 13.967789761532726

	* W (U+0057): B<<489.0,505.5>-<485.0,529.0>-<483.0,542.0>>/B<<483.0,542.0>-<482.0,529.0>-<477.5,505.5>> = 13.144867617550734

	* W (U+0057): B<<683.0,196.0>-<689.0,161.0>-<692.0,137.0>>/B<<692.0,137.0>-<695.0,162.0>-<701.0,196.5>> = 13.967789761532726

	* Wacute (U+1E82): B<<266.0,196.0>-<272.0,161.0>-<275.0,137.0>>/B<<275.0,137.0>-<278.0,162.0>-<284.0,196.5>> = 13.967789761532726

	* Wacute (U+1E82): B<<489.0,505.5>-<485.0,529.0>-<483.0,542.0>>/B<<483.0,542.0>-<482.0,529.0>-<477.5,505.5>> = 13.144867617550734

	* Wacute (U+1E82): B<<683.0,196.0>-<689.0,161.0>-<692.0,137.0>>/B<<692.0,137.0>-<695.0,162.0>-<701.0,196.5>> = 13.967789761532726

	* Wcircumflex (U+0174): B<<266.0,196.0>-<272.0,161.0>-<275.0,137.0>>/B<<275.0,137.0>-<278.0,162.0>-<284.0,196.5>> = 13.967789761532726

	* Wcircumflex (U+0174): B<<489.0,505.5>-<485.0,529.0>-<483.0,542.0>>/B<<483.0,542.0>-<482.0,529.0>-<477.5,505.5>> = 13.144867617550734

	* Wcircumflex (U+0174): B<<683.0,196.0>-<689.0,161.0>-<692.0,137.0>>/B<<692.0,137.0>-<695.0,162.0>-<701.0,196.5>> = 13.967789761532726

	* Wdieresis (U+1E84): B<<266.0,196.0>-<272.0,161.0>-<275.0,137.0>>/B<<275.0,137.0>-<278.0,162.0>-<284.0,196.5>> = 13.967789761532726 

	* 8 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[15] NotoSansBengaliUI-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali UI ExtraBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (unencoded), uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 llvocalicvowelsignUIbeng (U+09E3), lvocalicvowelsignUIbeng (U+09E2) and rrvocalicvowelsignUIbeng (U+09C4) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* five.beng (U+0035): X=131.0,Y=-0.5 (should be at baseline 0?)

	* C (U+0043): X=485.5,Y=-1.0 (should be at baseline 0?)

	* G (U+0047): X=535.5,Y=1.5 (should be at baseline 0?)

	* S (U+0053): X=142.0,Y=1.0 (should be at baseline 0?)

	* b (U+0062): X=298.0,Y=535.5 (should be at x-height 536?)

	* c (U+0063): X=405.0,Y=1.5 (should be at baseline 0?)

	* e (U+0065): X=441.5,Y=-0.5 (should be at baseline 0?)

	* f (U+0066): X=279.5,Y=620.5 (should be at cap-height 622?)

	* g (U+0067): X=341.0,Y=538.0 (should be at x-height 536?)

	* g (U+0067): X=565.0,Y=-1.0 (should be at baseline 0?) 

	* 67 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* V (U+0056): B<<326.0,209.5>-<333.0,177.0>-<335.0,156.0>>/B<<335.0,156.0>-<338.0,177.0>-<344.5,209.0>> = 13.570434385161475

	* W (U+0057): B<<283.5,211.5>-<290.0,175.0>-<293.0,151.0>>/B<<293.0,151.0>-<297.0,183.0>-<305.0,226.5>> = 14.25003269780357

	* W (U+0057): B<<506.5,475.5>-<502.0,500.0>-<501.0,516.0>>/B<<501.0,516.0>-<499.0,500.0>-<494.5,475.5>> = 10.701350723899111

	* Wacute (U+1E82): B<<283.5,211.5>-<290.0,175.0>-<293.0,151.0>>/B<<293.0,151.0>-<297.0,183.0>-<305.0,226.5>> = 14.25003269780357

	* Wacute (U+1E82): B<<506.5,475.5>-<502.0,500.0>-<501.0,516.0>>/B<<501.0,516.0>-<499.0,500.0>-<494.5,475.5>> = 10.701350723899111

	* Wcircumflex (U+0174): B<<283.5,211.5>-<290.0,175.0>-<293.0,151.0>>/B<<293.0,151.0>-<297.0,183.0>-<305.0,226.5>> = 14.25003269780357

	* Wcircumflex (U+0174): B<<506.5,475.5>-<502.0,500.0>-<501.0,516.0>>/B<<501.0,516.0>-<499.0,500.0>-<494.5,475.5>> = 10.701350723899111

	* Wdieresis (U+1E84): B<<283.5,211.5>-<290.0,175.0>-<293.0,151.0>>/B<<293.0,151.0>-<297.0,183.0>-<305.0,226.5>> = 14.25003269780357

	* Wdieresis (U+1E84): B<<506.5,475.5>-<502.0,500.0>-<501.0,516.0>>/B<<501.0,516.0>-<499.0,500.0>-<494.5,475.5>> = 10.701350723899111

	* Wgrave (U+1E80): B<<283.5,211.5>-<290.0,175.0>-<293.0,151.0>>/B<<293.0,151.0>-<297.0,183.0>-<305.0,226.5>> = 14.25003269780357 

	* 4 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[16] NotoSansBengaliUI-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali UI ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (unencoded), uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
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

	* 76 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<858.0,622.0>> -> L<<858.0,622.0>--<858.0,622.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* chabeng (U+099B): B<<514.0,177.5>-<450.0,123.0>-<343.0,114.0>>/B<<343.0,114.0>-<493.0,89.0>-<651.0,1.0>> = 14.27027617105606

	* mabeng (U+09AE): L<<449.0,587.0>--<64.0,587.0>>/B<<64.0,587.0>-<143.0,574.0>-<185.0,541.5>> = 9.344671902099696 

	* sabeng (U+09B8): L<<516.0,587.0>--<57.0,587.0>>/B<<57.0,587.0>-<145.0,570.0>-<197.5,544.5>> = 10.933816785755795 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[16] NotoSansBengaliUI-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali UI Light' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (unencoded), uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
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

	* C (U+0043): X=491.0,Y=-2.0 (should be at baseline 0?)

	* N (U+004E): X=153.0,Y=624.0 (should be at cap-height 622?)

	* N (U+004E): X=150.0,Y=624.0 (should be at cap-height 622?)

	* Q (U+0051): X=478.0,Y=2.0 (should be at baseline 0?)

	* S (U+0053): X=136.0,Y=-1.0 (should be at baseline 0?)

	* c (U+0063): X=385.0,Y=535.0 (should be at x-height 536?)

	* e (U+0065): X=395.0,Y=-2.0 (should be at baseline 0?) 

	* 56 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<873.0,622.0>> -> L<<873.0,622.0>--<873.0,622.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* mabeng (U+09AE): L<<450.0,574.0>--<82.0,574.0>>/B<<82.0,574.0>-<187.0,558.0>-<229.5,500.0>> = 8.664135433108044 

	* sabeng (U+09B8): L<<514.0,574.0>--<75.0,574.0>>/B<<75.0,574.0>-<159.0,558.0>-<208.0,534.0>> = 10.784297867562596 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[14] NotoSansBengaliUI-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali UI Medium' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (unencoded), uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 llvocalicvowelsignUIbeng (U+09E3), lvocalicvowelsignUIbeng (U+09E2) and rrvocalicvowelsignUIbeng (U+09C4) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* aabeng (U+0986): B<<968.5,607.0>-<991.0,592.0>-<1008.0,559.0>>/B<<1008.0,559.0>-<1006.0,564.0>-<1005.0,582.0>> = 5.453918888591197

	* mabeng (U+09AE): L<<443.0,539.0>--<157.0,539.0>>/B<<157.0,539.0>-<228.0,521.0>-<265.0,472.0>> = 14.22596389875178 

	* sabeng (U+09B8): L<<504.0,539.0>--<143.0,539.0>>/B<<143.0,539.0>-<204.0,527.0>-<240.0,506.5>> = 11.129189289611167 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[14] NotoSansBengaliUI-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (unencoded), uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 llvocalicvowelsignUIbeng (U+09E3), lvocalicvowelsignUIbeng (U+09E2) and rrvocalicvowelsignUIbeng (U+09C4) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<898.0,622.0>> -> L<<898.0,622.0>--<898.0,622.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* mabeng (U+09AE): L<<450.0,551.0>--<116.0,551.0>>/B<<116.0,551.0>-<199.0,540.0>-<246.5,489.5>> = 7.549421768263246 

	* sabeng (U+09B8): L<<510.0,551.0>--<107.0,551.0>>/B<<107.0,551.0>-<183.0,540.0>-<226.5,518.0>> = 8.235619324209488 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[15] NotoSansBengaliUI-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali UI SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (unencoded), uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
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

	* C (U+0043): X=485.5,Y=-2.0 (should be at baseline 0?)

	* G (U+0047): X=531.0,Y=0.5 (should be at baseline 0?) 

	* 54 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* W (U+0057): B<<257.0,182.5>-<263.0,150.0>-<266.0,126.0>>/B<<266.0,126.0>-<269.0,151.0>-<275.0,184.0>> = 13.967789761532726

	* W (U+0057): B<<678.0,182.0>-<684.0,150.0>-<687.0,126.0>>/B<<687.0,126.0>-<690.0,151.0>-<695.5,183.0>> = 13.967789761532726

	* Wacute (U+1E82): B<<257.0,182.5>-<263.0,150.0>-<266.0,126.0>>/B<<266.0,126.0>-<269.0,151.0>-<275.0,184.0>> = 13.967789761532726

	* Wacute (U+1E82): B<<678.0,182.0>-<684.0,150.0>-<687.0,126.0>>/B<<687.0,126.0>-<690.0,151.0>-<695.5,183.0>> = 13.967789761532726

	* Wcircumflex (U+0174): B<<257.0,182.5>-<263.0,150.0>-<266.0,126.0>>/B<<266.0,126.0>-<269.0,151.0>-<275.0,184.0>> = 13.967789761532726

	* Wcircumflex (U+0174): B<<678.0,182.0>-<684.0,150.0>-<687.0,126.0>>/B<<687.0,126.0>-<690.0,151.0>-<695.5,183.0>> = 13.967789761532726

	* Wdieresis (U+1E84): B<<257.0,182.5>-<263.0,150.0>-<266.0,126.0>>/B<<266.0,126.0>-<269.0,151.0>-<275.0,184.0>> = 13.967789761532726

	* Wdieresis (U+1E84): B<<678.0,182.0>-<684.0,150.0>-<687.0,126.0>>/B<<687.0,126.0>-<690.0,151.0>-<695.5,183.0>> = 13.967789761532726

	* Wgrave (U+1E80): B<<257.0,182.5>-<263.0,150.0>-<266.0,126.0>>/B<<266.0,126.0>-<269.0,151.0>-<275.0,184.0>> = 13.967789761532726

	* Wgrave (U+1E80): B<<678.0,182.0>-<684.0,150.0>-<687.0,126.0>>/B<<687.0,126.0>-<690.0,151.0>-<695.5,183.0>> = 13.967789761532726 

	* 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[16] NotoSansBengaliUI-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 404, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Sans Bengali UI Thin' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: sfthyphen.beng	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni1CE1 (unencoded), uni1CE1.UI (U+1CE1) and uni1CF7 (U+1CF7) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 llvocalicvowelsignUIbeng (U+09E3), lvocalicvowelsignUIbeng (U+09E2) and rrvocalicvowelsignUIbeng (U+09C4) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+1CE1 and U+1CF7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* aabeng (U+0986): L<<-10.0,622.0>--<848.0,622.0>> -> L<<848.0,622.0>--<848.0,622.0>>

	* llvocalicvowelsignUIbeng (U+09E3): L<<-161.0,-164.0>--<-161.0,-164.0>> -> L<<-161.0,-164.0>--<-161.0,-164.0>>

	* rrvocalicbeng (U+09E0): L<<484.0,676.0>--<489.0,622.0>> -> L<<489.0,622.0>--<489.0,318.0>>

	* rrvocalicbeng (U+09E0): L<<677.0,676.0>--<682.0,622.0>> -> L<<682.0,622.0>--<682.0,72.0>>

	* rvocalicbeng (U+098B): L<<484.0,676.0>--<489.0,622.0>> -> L<<489.0,622.0>--<489.0,318.0>> 

	* rvocalicbeng (U+098B): L<<677.0,676.0>--<682.0,622.0>> -> L<<682.0,622.0>--<682.0,72.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* chabeng (U+099B): B<<500.5,178.5>-<433.0,122.0>-<312.0,117.0>>/B<<312.0,117.0>-<473.0,95.0>-<642.0,-1.0>> = 10.147294214439293

	* ghabeng (U+0998): B<<164.5,329.0>-<209.0,363.0>-<255.0,389.0>>/B<<255.0,389.0>-<243.0,384.0>-<230.5,381.5>> = 6.856024055205275

	* mabeng (U+09AE): L<<449.0,596.0>--<51.0,596.0>>/B<<51.0,596.0>-<136.0,582.0>-<179.0,547.5>> = 9.352979250093227

	* sabeng (U+09B8): L<<517.0,596.0>--<44.0,596.0>>/B<<44.0,596.0>-<113.0,582.0>-<160.5,564.0>> = 11.469530332866904 

	* twobeng (U+09E8): B<<252.0,187.0>-<242.0,187.0>-<233.0,188.0>>/B<<233.0,188.0>-<313.0,158.0>-<390.0,105.5>> = 14.21585347367354 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* exclam.beng (U+0021): L<<167.0,174.0>--<165.0,714.0>>

	* exclam.beng (U+0021): L<<193.0,714.0>--<191.0,174.0>>

	* exclamdown (U+00A1): L<<122.0,354.0>--<124.0,-186.0>> 

	* exclamdown (U+00A1): L<<96.0,-186.0>--<98.0,354.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[12] NotoSansBengali[wdth,wght].ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Check font names are correct (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_names">com.google.fonts/check/font_names</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:expected_font_names> had an error: KeyError: 'fvar'
</div></details><details><summary>💔 <b>ERROR:</b> Check a font's STAT table contains compulsory Axis Values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT">com.google.fonts/check/STAT</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:expected_font_names> had an error: KeyError: 'fvar'
</div></details><details><summary>💔 <b>ERROR:</b> Check variable font instances (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fvar_instances">com.google.fonts/check/fvar_instances</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:expected_font_names> had an error: KeyError: 'fvar'
</div></details><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1012, but got 917 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>


* 🔥 **FAIL** Glyph 0x00A0 is called "uni00A0.beng": Change to "uni00A0" [code: non-compliant-00a0]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- asciicircum

	- asciitilde

	- asterisk

	- backslash

	- banuktahalfbeng

	- bar

	- bhanuktahalfbeng

	- braceleft

	- braceright

	- bracketleft 

	- 81 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 nuktabeng (U+09BC), uni09FE (U+09FE) and uniA8F1 (U+A8F1) [code: mark-chars]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 3 | 82 | 200 | 2154 | 116 | 1755 | 0 |
| 0% | 2% | 5% | 50% | 3% | 41% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
