# Overview

This package converts text encoded using the legacy SIL IPA93 font to
unicode.

It contains one function, convert_to_unicode(), which relies on a
dictionary mapping IPA93 glyph codes to their corresponding unicode
code point(s). This is useful if, for example, you are working with a
resource like the [MOSS Aphasia MAPPD dataset]
(https://www.mappd.org/about.html).

The package also exposes the dictionary itself, sil_to_unicode_dict,
in case it is more convenient to use that directly. Lastly, this
package contains a list of all the unicode diacritics
(ipa_diacritics_unicode), which may be useful for removing diacritics
from the input in a post-processing step.

## Notes

* The IPA93 glyph access codes (and descriptions in the comments) were
copied from the file Ipa93.pdf, which can be found in the [IPA93 fonts
zip archive]
(https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=silipa93-2.00.zip&filename=silipa93.zip).
* Glyph access code 202 "minute space" does not have an obvious
unicode equivalent and is not handled in this package.
* The interpretation of glyph access codes 232, 134, 216, 128, 133,
217 in this package is based on [ipa-braille-final.pdf]
(http://brailleauthority.org/ipa/ipa-braille-final.pdf) and understood
to represent various tone bars (see
http://www.internationalphoneticalphabet.org/ipa-charts/tones-and-accents/
as well as comments in the code).

# Usage

The following code snippet illustrates the usage of the function
convert_to_unicode, which takes a string of SIL IPA93 glyph access
codes and returns an equivalent unicode string. In this example, we
assume the input excel file MAPPD.xlsx contains a structured data set
in which the IPA93 data lives in a column called "Phonetic_response."
We send each data point in this column to convert_to_unicode(), store
the result in a new column called "New_phonetic_response," and write
the new data set to a file called "MAPPD.new.xlsx":

    import pandas as pd

    mappd_df = pd.read_excel('MAPPD.xlsx')
    # The input to convert_to_unicode() is a string so handle null values
    # appropriately first.
    mappd_df['New_phonetic_response'] = mappd_df.Phonetic_response.fillna('')
    mappd_df.New_phonetic_response = mappd_df.New_phonetic_response.map(lambda x: convert_to_unicode(x))
    mappd_df.to_excel('MAPPD.new.xlsx', index=False)
    
