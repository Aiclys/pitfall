#!/usr/bin/env python3

letter_frequencies = {
    "a" : 8.167,
    "b" : 1.492,
    "c" : 2.782,
    "d" : 4.253,
    "e" : 12.702,
    "f" : 2.228,
    "g" : 2.015,
    "h" : 6.094,
    "i" : 6.966,
    "j" : 0.153,
    "k" : 0.772,
    "l" : 4.025,
    "m" : 2.406,
    "n" : 6.749,
    "o" : 7.507,
    "p" : 1.929,
    "q" : 0.095,
    "r" : 5.987,
    "s" : 6.327,
    "t" : 9.056,
    "u" : 2.758,
    "v" : 0.978,
    "w" : 2.36,
    "x" : 0.15,
    "y" : 1.974,
    "z" : 0.074
}

most_common_words = {
    "the" : 6.42,
    "of" : 2.76,
    "and" : 2.75,
    "to" : 2.67,
    "a" : 2.43,
    "in" : 2.31,
    "is" : 1.12,
    "for" : 1.01,
    "that" : 0.92,
    "was" : 0.88,
    "on" : 0.78,
    "with" : 0.75,
    "he" : 0.75,
    "it" : 0.74,
    "as" : 0.71,
    "at" : 0.58,
    "his" : 0.55,
    "by" : 0.51,
    "be" : 0.48,
    "from" : 0.47,
    "are" : 0.47,
    "this" : 0.42,
    "I" : 0.41,
    "but" : 0.40,
    "have" : 0.39,
    "an" : 0.37,
    "has" : 0.35,
    "not" : 0.34,
    "they" : 0.33,
    "or" : 0.30
}

most_common_beginning_of_word_letters = {
    "t" : 15.94,
    "a" : 15.5,
    "i" : 8.23,
    "s" : 7.75,
    "o" : 7.12,
    "c" : 5.97,
    "m" : 4.26,
    "f" : 4.08,
    "p" : 4.0,
    "w" : 3.82
}

most_common_end_of_word_letters = {
    "e" : 19.17,
    "s" : 14.35,
    "d" : 9.23,
    "t" : 8.64,
    "n" : 7.86,
    "y" : 7.3,
    "r" : 6.93,
    "o" : 4.67,
    "l" : 4.56,
    "f" : 4.08
}

most_common_bigrams = {
    "th" : 3.56,
    "he" : 3.08,
    "in" : 2.43,
    "er" : 2.05,
    "an" : 1.99,
    "re" : 1.85,
    "on" : 1.76,
    "at" : 1.49,
    "en" : 1.45,
    "nd" : 1.35,
    "ti" : 1.34,
    "es" : 1.34,
    "or" : 1.28,
    "te" : 1.21,
    "of" : 1.18,
    "ed" : 1.17,
    "is" : 1.13,
    "it" : 1.12,
    "al" : 1.09,
    "ar" : 1.08,
    "st" : 1.05,
    "nt" : 1.04,
    "to" : 1.04
}

most_common_trigrams = {
    "the" : 1.81,
    "and" : 0.73,
    "ing" : 0.72,
    "ent" : 0.42,
    "ion" : 0.42,
    "her" : 0.36,
    "for" : 0.34,
    "tha" : 0.33,
    "nth" : 0.33,
    "int" : 0.32,
    "ere" : 0.31,
    "tio" : 0.31,
    "ter" : 0.30,
    "est" : 0.28,
    "ers" : 0.28,
    "ati" : 0.26,
    "hat" : 0.26,
    "ate" : 0.25,
    "all" : 0.25,
    "eth" : 0.24,
    "hes" : 0.24,
    "ver" : 0.24,
    "his" : 0.24,
    "oft" : 0.22,
    "ith" : 0.21,
    "fth" : 0.21,
    "sth" : 0.21,
    "oth" : 0.21,
    "res" : 0.21,
    "ont" : 0.20,
}

most_common_quadgrams = {
    "tion" : 0.31,
    "nthe" : 0.27,
    "ther" : 0.24,
    "that" : 0.21,
    "ofth" : 0.19,
    "fthe" : 0.19,
    "thes" : 0.18,
    "with" : 0.18,
    "inth" : 0.17,
    "atio" : 0.17,
    "othe" : 0.16,
    "tthe" : 0.16,
    "dthe" : 0.15,
    "ingt" : 0.15,
    "ethe" : 0.15,
    "sand" : 0.14,
    "sthe" : 0.14,
    "here" : 0.13,
    "thec" : 0.13,
    "ment" : 0.12,
    "them" : 0.12,
    "rthe" : 0.12,
    "thep" : 0.11,
    "from" : 0.10,
    "this" : 0.10,
    "ting" : 0.10,
    "thei" : 0.10,
    "ngth" : 0.10,
    "ions" : 0.10,
    "andt" : 0.10,
}

most_common_quintgrams = {
    "ofthe" : 0.18,
    "ation" : 0.17,
    "inthe" : 0.16,
    "there" : 0.09,
    "ingth" : 0.09,
    "tothe" : 0.08,
    "ngthe" : 0.08,
    "other" : 0.07,
    "atthe" : 0.07,
    "tions" : 0.07,
    "andth" : 0.07,
    "ndthe" : 0.07,
    "onthe" : 0.07,
    "edthe" : 0.06,
    "their" : 0.06,
    "tiona" : 0.06,
    "orthe" : 0.06,
    "forth" : 0.06,
    "ingto" : 0.06,
    "theco" : 0.05,
    "ction" : 0.05,
    "which" : 0.05,
    "these" : 0.05,
    "after" : 0.05,
    "eofth" : 0.05,
    "about" : 0.04,
    "erthe" : 0.04,
    "ional" : 0.04,
    "first" : 0.04,
    "would" : 0.04
}
