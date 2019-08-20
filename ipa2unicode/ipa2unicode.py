#!/usr/bin/env python
# coding: utf-8

__author__ = "Brooke Cowan <cowanb@ohsu.edu"

"""
    This package converts text encoded using the legacy SIL IPA93 font to unicode. It contains one function, 
    convert_to_unicode(), which relies on a dictionary mapping IPA93 glyph codes to their corresponding unicode
    code point(s). This is useful if, for example, you are working with a resource like the MOSS Aphasia MAPPD 
    dataset (https://www.mappd.org/about.html). The package also exposes the dictionary itself, sil_to_unicode_dict,
    in case it is more convenient to use that directly. Lastly, this package contains a list of all the unicode 
    diacritics (ipa_diacritics_unicode), which may be useful for removing diacritics from the input in a post-processing
    step.
    NB:
    - The IPA93 glyph access codes (and descriptions in the comments) were copied from the file Ipa93.pdf, which 
      can be found in the IPA93 fonts zip archive:
      https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=silipa93-2.00.zip&filename=silipa93.zip
    - Glyph access code 202 "minute space" does not have an obvious unicode equivalent and is not handled in this package.
    - The interpretation of glyph access codes 232, 134, 216, 128, 133, 217 in this package is based on 
      ipa-braille-final.pdf (http://brailleauthority.org/ipa/ipa-braille-final.pdf) and understood to represent various
      tone bars (see http://www.internationalphoneticalphabet.org/ipa-charts/tones-and-accents/ and comments
      in the code).
"""
sil_to_unicode_dict = {
    # Glyph access code : unicode
    # Glyph access codes come from the file Ipa93.pdf included in the silipa93.zip file containing the SIL IPA93 font.
    97: '\u0061',  # lowercase A
    140: '\u0250',  # turned A
    65: '\u0251',  # cursive A
    129: '\u0252',  # turned cursive A
    81: '\u00E6',  # ash digraph
    98: '\u0062',  # lowercase B
    186: '\u0253',  # hooktop B
    245: '\u0299',  # small capital B
    66: '\u03B2',  # beta
    99: '\u0063',  # lowercase C
    141: '\u0254',  # open O
    254: '\u0255',  # curly-tail C

    67: '\u00E7',  # C cedilla
    100: '\u0064',  # lowercase D
    235: '\u0257',  # hooktop D
    234: '\u0256',  # right-tail D
    68: '\u00F0',  # eth
    101: '\u0065',  # lowercase E
    171: '\u0259',  # schwa
    130: '\u0258',  # reversed E
    69: '\u025B',  # epsilon
    206: '\u025C',  # reversed epsilon
    207: '\u025E',  # closed reversed epsilon
    102: '\u0066',  # lowercase F
    103: '\u0261',  # lowercase G

    169: '\u0260',  # hooktop G
    71: '\u0262',  # small capital G
    253: '\u029B',  # hooktop small capital G
    104: '\u0068',  # lowercase H
    72: '\u02B0',  # superscript H
    250: '\u0266',  # hooktop H
    238: '\u0267',  # hooked heng
    240: '\u0127',  # crossed H
    231: '\u0265',  # turned H
    75: '\u029C',  # small capital H
    105: '\u0069',  # lowercase I
    34: '\u0131',  # undotted I
    246: '\u0268',  # barred I

    # 174 : '\u1D7B', # This is a capital barred I
    174: '\u0131\u0335',  # undotted barred I
    73: '\u026A',  # small capital I
    106: '\u006A',  # lowercase J
    190: '\u0237',  # dotless J
    74: '\u02B2',  # superscript J
    239: '\u025F',  # barred dotless J
    198: '\u029D',  # curly-tail J
    215: '\u0284',  # hooktop barred dotless J
    107: '\u006B',  # lowercase K
    108: '\u006C',  # lowercase L
    58: '\u02E1',  # superscript L
    241: '\u026D',  # right-tail L
    194: '\u026C',  # belted L

    76: '\u026E',  # L-yogh digraph
    59: '\u029F',  # small capital L
    109: '\u006D',  # lowercase M
    201: '\u1D50',  # superior M
    77: '\u0271',  # left-tail M (at right)
    181: '\u026F',  # turned M
    229: '\u0270',  # turned M, right leg
    110: '\u006E',  # lowercase N
    60: '\u207F',  # superscript N
    78: '\u014B',  # eng
    212: '\u1D51',  # superscript eng
    247: '\u0273',  # right-tail N
    248: '\u0272',  # left-tail N (at left)

    203: '\u1DAE',  # superscript left-tail N (at left)
    178: '\u0274',  # small capital N
    111: '\u006F',  # lowercase O
    79: '\u00F8',  # slashed O
    80: '\u0275',  # barred O
    184: '\u0278',  # phi
    84: '\u03B8',  # theta
    191: '\u0153',  # O-E digraph
    175: '\u0276',  # small capital O-E digraph
    135: '\u0298',  # bull's eye
    112: '\u0070',  # lowercase P
    113: '\u0071',  # lowercase Q
    114: '\u0072',  # lowercase R

    168: '\u0279',  # turned R
    228: '\u027A',  # turned long-leg R
    125: '\u027D',  # right-tail R
    82: '\u027E',  # fish-hook R
    211: '\u027B',  # turned R, right tail
    123: '\u0280',  # small capital R
    210: '\u0281',  # inverted small capital R
    115: '\u0073',  # lowercase S
    167: '\u0282',  # right-tail S (at left)
    83: '\u0283',  # esh
    116: '\u0074',  # lowercase T
    255: '\u0288',  # right-tail T
    117: '\u0075',  # lowercase U

    172: '\u0289',  # barred U
    86: '\u028B',  # cursive V
    85: '\u028A',  # upsilon
    118: '\u0076',  # lowercase V
    195: '\u028C',  # turned V
    196: '\u0263',  # gamma
    236: '\u02E0',  # superscript gamma
    70: '\u0264',  # ram's horns
    119: '\u0077',  # lowercase W
    87: '\u02B7',  # superscript W
    227: '\u028D',  # turned W
    120: '\u0078',  # lowercase X
    88: '\u03C7',  # chi

    121: '\u0079',  # lowercase Y
    180: '\u028E',  # turned Y
    89: '\u028F',  # small capital Y
    122: '\u007A',  # lowercase Z
    252: '\u0291',  # curly-tail Z
    189: '\u0290',  # right-tail Z
    90: '\u0292',  # yogh
    63: '\u0294',  # glottal stop
    251: '\u02A1',  # barred glottal stop
    192: '\u0295',  # reversed glottal stop
    179: '\u02E4',  # superscript reversed glottal stop
    185: '\u02A2',  # barred reversed glottal stop
    151: '\u01C3',  # exclamation point

    44: '\u002C',  # comma
    46: '\u002E',  # period
    39: '\u02BC',  # apostrophe
    91: '\u005B',  # left square bracket
    93: '\u005D',  # right square bracket
    62: '\u02D1',  # half-length mark
    249: '\u02D0',  # length mark
    131: '\u0361',  # top tie bar
    237: '\u203F',  # bottom tie bar
    150: '\u007C',  # vertical line
    124: '\u031A',  # corner
    61: '\u0320',  # under-bar (o-width)
    173: '\u0320',  # under-bar (i-width)

    35: '\u0304',  # macron (o-width)
    220: '\u0304',  # macron (i-width)
    147: '\u0304',  # macron (high o-width)
    148: '\u0304',  # macron (high i-width)
    48: '\u0330',  # subscript tilde (o-width)
    188: '\u0330',  # subscript tilde (i-width)
    242: '\u0334',  # superimposed tilde
    41: '\u0303',  # superscript tilde (o-width)
    226: '\u0303',  # superscript tilde (i-width)
    64: '\u0301',  # acute accent (o-width)
    219: '\u0301',  # acute accent (i-width)
    143: '\u0301',  # acute accent (high o-width)
    144: '\u0301',  # acute accent (high i-width)

    33: '\u030B',  # double acute accent (o-width)
    218: '\u030B',  # double acute accent (i-width)
    136: '\u030B',  # double acute accent (high o-width)
    137: '\u030B',  # double acute accent (high i-width)
    36: '\u0300',  # grave accent (o-width)
    221: '\u0300',  # grave accent (i-width)
    152: '\u0300',  # grave accent (high o-width)
    153: '\u0300',  # grave accent (high i-width)
    37: '\u030F',  # double grave accent (o-width)
    222: '\u030F',  # double grave accent (i-width)
    157: '\u030F',  # double grave accent (high o-width)
    158: '\u030F',  # double grave accent (high i-width)
    94: '\u0302',  # circumflex (o-width)

    223: '\u0302',  # circumflex (i-width)
    233: '\u0302',  # circumflex (high o-width)
    230: '\u0302',  # circumflex (high i-width)
    38: '\u030C',  # wedge (o-width)
    224: '\u030C',  # wedge (i-width)
    244: '\u030C',  # wedge (high o-width)
    243: '\u030C',  # wedge (high i-width)
    45: '\u0324',  # superscript umlaut (o-width)
    208: '\u0324',  # superscript umlaut (i-width)
    95: '\u0308',  # umlaut
    164: '\u032C',  # superscript wedge
    40: '\u0306',  # breve (o-width)
    225: '\u0306',  # breve (i-width)

    57: '\u032F',  # superscript arch (o-width)
    187: '\u032F',  # superscript arch (i-width)
    209: '\u033C',  # superscript seagull
    56: '\u0325',  # under-ring (o-width)
    165: '\u0325',  # under-ring (i-width)
    42: '\u030A',  # over-ring (o-width)
    161: '\u030A',  # over-ring (i-width)
    96: '\u0329',  # syllabicity mark
    43: '\u031F',  # superscript plus (o-width)
    177: '\u031F',  # superscript plus (i-width)
    126: '\u033D',  # over-cross
    213: '\u02DE',  # right hook
    53: '\u032A',  # subscript bridge

    176: '\u033A',  # inverted subscript bridge
    54: '\u033B',  # subscript square
    52: '\u031E',  # lowering sign (o-width)
    162: '\u031E',  # lowering sign (i-width)
    51: '\u031D',  # raising sign (o-width)
    163: '\u031D',  # raising sign (i-width)
    49: '\u0318',  # advancing sign (o-width)
    193: '\u0318',  # advancing sign (i-width)
    50: '\u0319',  # retracting sign (o-width)
    170: '\u0319',  # retracting sign (i-width)
    55: '\u031C',  # subscript left half-ring
    166: '\u0339',  # subscript right half-ring
    138: '\u02E5',  # extra-high tone bar

    145: '\u02E6',  # high tone bar
    149: '\u02E7',  # mid tone bar
    154: '\u02E8',  # low tone bar
    159: '\u02E9',  # extra-low tone bar
    # http://www.internationalphoneticalphabet.org/ipa-charts/tones-and-accents/
    232: '\u02E9\u02E5',  # right Bar 15 -- "Rising tone bar" or "Rising contour tone"
    134: '\u02E5\u02E9',  # right Bar 51 -- "Falling tone bar" or "Falling contour tone"
    216: '\u02E7\u02E5',  # right Bar 35 -- "High rising tone bar" or "High rising contour tone"
    128: '\u02E9\u02E7',  # right Bar 13 -- "Low rising tone bar" or "Low rising contour tone"
    133: '\u02E5\u02E7',  # right Bar 53 -- "High falling tone bar" or "High falling contour tone"
    217: '\u02E7\u02E9',  # right Bar 31 -- "Low falling tone bar" or "Low falling contour tone"
    155: '\u2193',  # down arrow

    139: '\u2191',  # up arrow
    205: '\u2198',  # downward diagonal arrow
    204: '\u2197',  # upward diagonal arrow
    199: '\u02CC',  # vertical stroke (inferior)
    200: '\u02C8',  # vertical stroke (superior)
    142: '\u01C0',  # pipe
    156: '\u01C2',  # double-barred pipe
    132: '\u2016',  # double vertical line
    146: '\u01C1',  # double pipe
    # 202 : '\u',     # minute space ... Not sure what this is.
    92: '\u005C',  # backward slash
    47: '\u002F',  # forward slash
    214: '\u2010',  # hyphen dash

    # Preserve spaces.
    32: '\u0020',  # ASCII space character
}

def convert_to_unicode(response: str) -> str:
    """
    Takes a string encoded in SIL IPA93 and returns the equivalent unicode string.
    Input parameter is a string of space-delimited tokens encoded in IPA93.
    Returns a string of space-delimited tokens encoded as Unicode code points.
    Raises KeyError if a byte in the input is not a valid IPA93 glyph code.
    """
    if response == '': return ''
    # glyph_codes is a list of Latin-1 decimal values
    glyph_codes = list(response.encode('ISO-8859-1'))
    # new_str is a string of unicode code points corresponding to the decimals in glyph_codes.
    try:
        new_str = ''.join([sil_to_unicode_dict[glyph_code] for glyph_code in glyph_codes])
    except KeyError:
        print('Invalid glyph code %s' % (glyph_code))
        raise
    return new_str

ipa_diacritics_unicode = [
    '\u002C',  # comma
    '\u002E',  # period
    '\u02BC',  # apostrophe
    '\u005B',  # left square bracket
    '\u005D',  # right square bracket
    '\u02D1',  # half-length mark
    '\u02D0',  # length mark
    '\u0361',  # top tie bar
    '\u203F',  # bottom tie bar
    '\u007C',  # vertical line
    '\u031A',  # corner
    '\u0320',  # under-bar (o-width)
    '\u0320',  # under-bar (i-width)

    '\u0304',  # macron (o-width)
    '\u0304',  # macron (i-width)
    '\u0304',  # macron (high o-width)
    '\u0304',  # macron (high i-width)
    '\u0330',  # subscript tilde (o-width)
    '\u0330',  # subscript tilde (i-width)
    '\u0334',  # superimposed tilde
    '\u0303',  # superscript tilde (o-width)
    '\u0303',  # superscript tilde (i-width)
    '\u0301',  # acute accent (o-width)
    '\u0301',  # acute accent (i-width)
    '\u0301',  # acute accent (high o-width)
    '\u0301',  # acute accent (high i-width)

    '\u030B',  # double acute accent (o-width)
    '\u030B',  # double acute accent (i-width)
    '\u030B',  # double acute accent (high o-width)
    '\u030B',  # double acute accent (high i-width)
    '\u0300',  # grave accent (o-width)
    '\u0300',  # grave accent (i-width)
    '\u0300',  # grave accent (high o-width)
    '\u0300',  # grave accent (high i-width)
    '\u030F',  # double grave accent (o-width)
    '\u030F',  # double grave accent (i-width)
    '\u030F',  # double grave accent (high o-width)
    '\u030F',  # double grave accent (high i-width)
    '\u0302',  # circumflex (o-width)

    '\u0302',  # circumflex (i-width)
    '\u0302',  # circumflex (high o-width)
    '\u0302',  # circumflex (high i-width)
    '\u030C',  # wedge (o-width)
    '\u030C',  # wedge (i-width)
    '\u030C',  # wedge (high o-width)
    '\u030C',  # wedge (high i-width)
    '\u0324',  # superscript umlaut (o-width)
    '\u0324',  # superscript umlaut (i-width)
    '\u0308',  # umlaut
    '\u032C',  # superscript wedge
    '\u0306',  # breve (o-width)
    '\u0306',  # breve (i-width)

    '\u032F',  # superscript arch (o-width)
    '\u032F',  # superscript arch (i-width)
    '\u033C',  # superscript seagull
    '\u0325',  # under-ring (o-width)
    '\u0325',  # under-ring (i-width)
    '\u030A',  # over-ring (o-width)
    '\u030A',  # over-ring (i-width)
    '\u0329',  # syllabicity mark
    '\u031F',  # superscript plus (o-width)
    '\u031F',  # superscript plus (i-width)
    '\u033D',  # over-cross
    '\u02DE',  # right hook
    '\u032A',  # subscript bridge

    '\u033A',  # inverted subscript bridge
    '\u033B',  # subscript square
    '\u031E',  # lowering sign (o-width)
    '\u031E',  # lowering sign (i-width)
    '\u031D',  # raising sign (o-width)
    '\u031D',  # raising sign (i-width)
    '\u0318',  # advancing sign (o-width)
    '\u0318',  # advancing sign (i-width)
    '\u0319',  # retracting sign (o-width)
    '\u0319',  # retracting sign (i-width)
    '\u031C',  # subscript left half-ring
    '\u0339',  # subscript right half-ring
    '\u02E5',  # extra-high tone bar

    '\u02E6',  # high tone bar
    '\u02E7',  # mid tone bar
    '\u02E8',  # low tone bar
    '\u02E9',  # extra-low tone bar
    # http://www.internationalphoneticalphabet.org/ipa-charts/tones-and-accents/
    '\u02E9\u02E5',  # right Bar 15 -- "Rising tone bar" or "Rising contour tone"
    '\u02E5\u02E9',  # right Bar 51 -- "Falling tone bar" or "Falling contour tone"
    '\u02E7\u02E5',  # right Bar 35 -- "High rising tone bar" or "High rising contour tone"
    '\u02E9\u02E7',  # right Bar 13 -- "Low rising tone bar" or "Low rising contour tone"
    '\u02E5\u02E7',  # right Bar 53 -- "High falling tone bar" or "High falling contour tone"
    '\u02E7\u02E9',  # right Bar 31 -- "Low falling tone bar" or "Low falling contour tone"
    '\u2193',  # down arrow

    '\u2191',  # up arrow
    '\u2198',  # downward diagonal arrow
    '\u2197',  # upward diagonal arrow
    '\u02CC',  # vertical stroke (inferior)
    '\u02C8',  # vertical stroke (superior)
    '\u01C0',  # pipe
    '\u01C2',  # double-barred pipe
    '\u2016',  # double vertical line
    '\u01C1',  # double pipe
    # '\u',     # minute space
    '\u005C',  # backward slash
    '\u002F',  # forward slash
    '\u2010',  # hyphen dash
]
