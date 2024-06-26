#!/usr/bin/env python3

letter_frequencies = {
    "a" : 7.60,
    "à" : 0.43,
    "â" : 0.05,
    "æ" : 0.0000062,
    "b" : 0.96,
    "c" : 3.39,
    "ç" : 0.05,
    "d" : 4.08,
    "e" : 14.47,
    "é" : 2.43,
    "è" : 0.42,
    "ê" : 0.13,
    "ë" : 0.00000034,
    "f" : 1.12,
    "g" : 1.18,
    "h" : 0.93,
    "i" : 7.21,
    "î" : 0.04,
    "ï" : 0.01,
    "j" : 0.30,
    "k" : 0.16,
    "l" : 5.86,
    "m" : 2.78,
    "n" : 7.32,
    "o" : 5.39,
    "ô" : 0.05,
    "œ" : 0.02,
    "p" : 2.98,
    "q" : 0.85,
    "r" : 6.86,
    "s" : 7.98,
    "t" : 7.11,
    "u" : 5.55,
    "ù" : 0.02,
    "û" : 0.02,
    "ü" : 0.00000091,
    "v" : 1.29,
    "w" : 0.08,
    "x" : 0.43,
    "y" : 0.34,
    "ÿ" : 0.0000000034,
    "z" : 0.10
}

most_common_words = [
    "de",
    "la",
    "le",
    "à",
    "et",
    "les",
    "des",
    "en",
    "du",
    "a",
    "un",
    "pour",
    "que",
    "dans",
    "une",
    "qui",
    "au",
    "est",
    "sur",
    "pas",
    "par",
    "plus",
    "ce",
    "avec",
    "son",
    "se",
    "ne",
    "ont",
    "été",
    "sont",
    "il",
    "aux",
    "sa",
    "cette",
    "ses",
    "fait",
    "mais",
    "ou",
    "nous",
    "deux",
    "leur",
    "tout",
    "comme",
    "ans",
    "aussi",
    "on"
]


most_common_bigrams = {
    "es" : 2.91,
    "le" : 2.08,
    "de" : 2.02,
    "en" : 1.97,
    "on" : 1.70,
    "nt" : 1.69,
    "re" : 1.62,
    "an" : 1.28,
    "la" : 1.25,
    "er" : 1.21,
    "te" : 1.19,
    "el" : 1.15,
    "se" : 1.09,
    "ti" : 1.04,
    "ur" : 1.01,
    "et" : 0.96,
    "ne" : 0.96,
    "is" : 0.94,
    "ed" : 0.93,
    "ou" : 0.93,
    "ar" : 0.88,
    "in" : 0.87,
    "it" : 0.86,
    "st" : 0.86,
    "qu" : 0.84,
    "ns" : 0.82,
    "ai" : 0.81,
    "me" : 0.79,
    "ra" : 0.79,
    "ie" : 0.76,
}

most_common_trigrams = {
    "ent" : 0.86,
    "les" : 0.71,
    "ion" : 0.56,
    "des" : 0.54,
    "ede" : 0.52,
    "que" : 0.51,
    "est" : 0.49,
    "tio" : 0.42,
    "ant" : 0.38,
    "par" : 0.37,
    "men" : 0.37,
    "del" : 0.37,
    "ela" : 0.37,
    "sde" : 0.37,
    "lle" : 0.36,
    "our" : 0.35,
    "res" : 0.32,
    "son" : 0.31,
    "tre" : 0.31,
    "ont" : 0.31,
    "eur" : 0.31,
    "ati" : 0.30,
    "une" : 0.29,
    "con" : 0.29,
    "eme" : 0.28,
    "ans" : 0.28,
}

most_common_quadgrams = {
    "tion" : 0.43,
    "ment" : 0.34,
    "emen" : 0.25,
    "dela" : 0.24,
    "atio" : 0.24,
    "ique" : 0.23,
    "elle" : 0.20,
    "dans" : 0.19,
    "pour" : 0.17,
    "esde" : 0.15,
    "edes" : 0.14,
    "onde" : 0.14,
    "iond" : 0.13,
    "ions" : 0.13,
    "ansl" : 0.12,
    "aire" : 0.12,
    "plus" : 0.12,
    "ille" : 0.12,
    "quel" : 0.12,
    "sont" : 0.11,
    "edel" : 0.11,
    "ques" : 0.11,
    "comm" : 0.11,
    "entd" : 0.11,
    "eurs" : 0.11,
    "ntde" : 0.11,
    "part" : 0.10,
    "ntre" : 0.10,
    "ouve" : 0.10,
    "ente" : 0.10
}
 
most_common_prefixes = {
    "l'-" : 0.3779,
    "d'-" : 0.3214,
    "re-" : 0.0738,
    "dé-" : 0.0633,
    "s'-" : 0.0831,
    "in-" : 0.0378,
    "ré-" : 0.0280,
    "r-" : 0.0241,
    "con-" : 0.0205,
    "n'-" : 0.0197,
    "pré-" : 0.0142,
    "é-" : 0.0136,
    "sur-" : 0.0135,
    "a-" : 0.0134,
    "im-" : 0.0129,
}

most_common_suffixes = {
    "-s" : 12.367,
    "-e" : 3.394,
    "-r" : 1.954,
    "-es" : 1.933,
    "nt" : 1.372,
    "-ment" : 0.814,
    "-a" : 0.620,
    "-ra" : 0.511,
    "-it" : 0.323,
    "-ait" : 0.317,
    "-ne" : 0.291,
    "-z" : 0.264,
    "-er" : 0.264,
    "-t" : 0.262,
    "-ront" : 0.236,
    "-ont" : 0.234,
    "-ur" : 0.233,
    "-é" : 0.204,
    "-le" : 0.200,
    "-urs" : 0.199,
}

most_common_numbers = {
    "2022" : 10.6685,
    "2021" : 6.7458,
    "000" : 4.9808,
    "10" : 4.8803,
    "2" : 4.8171,
    "2020" : 4.1369,
    "20" : 4.1158,
    "3" : 3.9696,
    "1" : 3.9571,
    "5" : 3.9162,
    "30" : 3.7999,
    "15" : 3.6452,
    "4" : 3.4542,
    "24" : 3.0111,
    "2019" : 2.9999,
    "12" : 2.9124,
    "2023" : 2.7895,
    "6" : 2.7509,
    "18" : 2.7221,
    "25" : 2.7094,
    "14" : 2.5670,
    "8" : 2.4953,
    "7" : 2.4606,
    "16" : 2.4465,
    "2018" : 2.0883,
    "100" : 2.0663,
    "9" : 1.9311,
    "0" : 0.2922
}
