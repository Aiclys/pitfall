#!/usr/bin/env python3

letter_frequencies = {
    "a" : 6.34,
    "b" : 2.21,
    "c" : 2.71,
    "d" : 4.92,
    "e" : 15.99,
    "f" : 1.80,
    "g" : 3.02,
    "h" : 4.11,
    "i" : 7.60,
    "j" : 0.27,
    "k" : 1.50,
    "l" : 3.72,
    "m" : 2.75,
    "n" : 9.59,
    "o" : 2.75,
    "p" : 1.06,
    "q" : 0.04,
    "r" : 7.71,
    "s" : 6.41,
    "t" : 6.43,
    "u" : 3.76,
    "v" : 0.94,
    "w" : 1.40,
    "x" : 0.07,
    "y" : 0.13,
    "z" : 1.22,
    "ä" : 0.54,
    "ö" : 0.24,
    "ü" : 0.63,
    "ß" : 0.15,
}

most_common_bigrams = {
    "er" : 3.90,
    "en" : 3.61,
    "ch" : 2.36,
    "de" : 2.31,
    "ei" : 1.98,
    "te" : 1.98,
    "in" : 1.71,
    "nd" : 1.68,
    "ie" : 1.48,
    "ge" : 1.45,
    "st" : 1.21,
    "ne" : 1.19,
    "be" : 1.17,
    "es" : 1.17,
    "un" : 1.13,
    "re" : 1.11,
    "an" : 1.07,
    "he" : 0.89,
    "au" : 0.89,
    "ng" : 0.87,
    "se" : 0.83,
    "it" : 0.81,
    "di" : 0.81,
    "ic" : 0.80,
    "sc" : 0.77,
    "le" : 0.73,
    "da" : 0.72,
    "ns" : 0.71,
    "is" : 0.70,
    "ra" : 0.69,
}

most_common_trigrams = {
    "der" : 1.04,
    "ein" : 0.83,
    "sch" : 0.76,
    "ich" : 0.75,
    "nde" : 0.72,
    "die" : 0.62,
    "che" : 0.58,
    "ten" : 0.51,
    "und" : 0.48,
    "ine" : 0.48,
    "ter" : 0.44,
    "gen" : 0.44,
    "end" : 0.44,
    "ers" : 0.42,
    "ste" : 0.42,
    "cht" : 0.41,
    "ung" : 0.39,
    "das" : 0.38,
    "ere" : 0.38,
    "ber" : 0.36,
    "ens" : 0.36,
    "nge" : 0.35,
    "rde" : 0.35,
    "ver" : 0.34,
    "eit" : 0.33,
    "hen" : 0.31,
    "erd" : 0.30,
    "rei" : 0.30,
    "ind" : 0.29
}

most_common_quadgrams = {
    "eine" : 0.41,
    "nder" : 0.29,
    "icht" : 0.27,
    "chen" : 0.24,
    "sche" : 0.23,
    "ende" : 0.20,
    "lich" : 0.20,
    "sich" : 0.19,
    "erde" : 0.18,
    "inde" : 0.17,
    "nden" : 0.16,
    "rden" : 0.16,
    "ndie" : 0.15,
    "isch" : 0.15,
    "iche" : 0.15,
    "auch" : 0.15,
    "erst" : 0.14,
    "sein" : 0.14,
    "nter" : 0.14,
    "ngen" : 0.13,
    "nich" : 0.13,
    "eite" : 0.13,
    "ande" : 0.13,
    "tsch" : 0.12,
    "eder" : 0.12,
    "dies" : 0.12,
    "nach" : 0.12,
    "ders" : 0.11,
    "esch" : 0.11,
    "über" : 0.11,
}