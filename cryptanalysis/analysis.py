#!/usr/bin/env python3
import english_frequencies as ef
import german_frequencies as gf
import french_frequencies as ff
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def get_frequencies(text_file=False, text=False, mode="text"):
    if text_file != False and text == False:
        with open(text_file, "r") as fl:
            sign_count = {}
            msg = fl.read()
            for sign in msg:
                if sign in sign_count:
                    sign_count[sign] += 1
                else:
                    sign_count[sign] = 0
                    sign_count[sign] += 1

    elif text != False and text_file == False:
        sign_count = {}
        for sign in text:
            if sign in sign_count:
                sign_count[sign] += 1
            else:
                sign_count[sign] = 0
                sign_count[sign] += 1

    if mode == "text":
        for i in sign_count:
            print(f"{i} : {sign_count[i]}")

    elif mode == "visual":
        fig, ax = plt.subplots(figsize=(30, 20), layout="constrained")
        sign_names = list(sign_count.keys())
        sign_frequencies = list(sign_count.values())
        ax.bar(sign_names, sign_frequencies)
        fig.suptitle("Character frequencies visualized")
        plt.show

def language_frequencies(language, which_frequency, mode="text"):
    if mode == "text":
        if language == "english":
            if which_frequency in ["letters", "monograms"]:
                frequencies = ef.letter_frequencies
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "words":
                frequencies = ef.most_common_words
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "beginning of word letters":
                frequencies = ef.most_common_beginning_of_word_letters
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "end of word letters":
                frequencies = ef.most_common_end_of_word_letters
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "bigrams":
                frequencies = ef.most_common_bigrams
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "trigrams":
                frequencies = ef.most_common_trigrams
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "quadgrams":
                frequencies = ef.most_common_quadgrams
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "quintgrams":
                frequencies = ef.most_common_quintgrams
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")

        elif language == "german":
            if which_frequency in ["letters", "monograms"]:
                frequencies = gf.letter_frequencies
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "bigrams":
                frequencies = gf.most_common_bigrams
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "trigrams":
                frequencies = gf.most_common_trigrams
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "quadgrams":
                frequencies = gf.most_common_quadgrams
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")

        elif language == "french":
            if which_frequency in ["letters", "monograms"]:
                frequencies = ff.letter_frequencies
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "words":
                frequencies = ff.letter_frequencies
                print(frequencies)
            elif which_frequency == "bigrams":
                frequencies = ff.most_common_bigrams
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "trigrams":
                frequencies = ff.most_common_trigrams
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "quadgrams":
                frequencies = ff.most_common_quadgrams
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "prefixes":
                frequencies = ff.most_common_prefixes
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "suffixes":
                frequencies = ff.most_common_suffixes
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")
            elif which_frequency == "numbers":
                frequencies = ff.most_common_numbers
                for frequency in frequencies:
                    print(f"{frequency} : {frequencies[frequency]}%")


    elif mode == "visual":
        fig, ax = plt.subplots(figsize=(26, 16), layout="constrained")
        if language == "english":
            if which_frequency in ["letters", "monograms"]:
                sign_names = list(ef.letter_frequencies.keys())
                sign_frequencies = list(ef.letter_frequencies.values())
            elif which_frequency == "words":
                sign_names = list(ef.most_common_words.keys())
                sign_frequencies = list(ef.most_common_words.values())
            elif which_frequency == "beginning of word letters":
                sign_names = list(ef.most_common_beginning_of_word_letters.keys())
                sign_frequencies = list(ef.most_common_beginning_of_word_letters.values())
            elif which_frequency == "end of word letters":
                sign_names = list(ef.most_common_end_of_word_letters.keys())
                sign_frequencies = list(ef.most_common_end_of_word_letters.values())
            elif which_frequency == "bigrams":
                sign_names = list(ef.most_common_bigrams.keys())
                sign_frequencies = list(ef.most_common_bigrams.values())
            elif which_frequency == "trigrams":
                sign_names = list(ef.most_common_trigrams.keys())
                sign_frequencies = list(ef.most_common_trigrams.values())
            elif which_frequency == "quadgrams":
                sign_names = list(ef.most_common_quadgrams.keys())
                sign_frequencies = list(ef.most_common_quadgrams.values())
            elif which_frequency == "quintgrams":
                sign_names = list(ef.most_common_quintgrams.keys())
                sign_frequencies = list(ef.most_common_quintgrams.values())

        elif language == "german":
            if which_frequency in ["letters", "monograms"]:
                sign_names = list(gf.letter_frequencies.keys())
                sign_frequencies = list(gf.letter_frequencies.values())
            elif which_frequency == "bigrams":
                sign_names = list(gf.most_common_bigrams.keys())
                sign_frequencies = list(gf.most_common_bigrams.values())
            elif which_frequency == "trigrams":
                sign_names = list(gf.most_common_trigrams.keys())
                sign_frequencies = list(gf.most_common_trigrams.values())
            elif which_frequency == "quadgrams":
                sign_names = list(gf.most_common_quadgrams.keys())
                sign_frequencies = list(gf.most_common_quadgrams.values())

        elif language == "french":
            if which_frequency in ["letters", "monograms"]:
                sign_names = list(ff.letter_frequencies.keys())
                sign_frequencies = list(ff.letter_frequencies.values())
            elif which_frequency == "bigrams":
                sign_names = list(ff.most_common_bigrams.keys())
                sign_frequencies = list(ff.most_common_bigrams.values())
            elif which_frequency == "trigrams":
                sign_names = list(ff.most_common_trigrams.keys())
                sign_frequencies = list(ff.most_common_trigrams.values())
            elif which_frequency == "quadgrams":
                sign_names = list(ff.most_common_quadgrams.keys())
                sign_frequencies = list(ff.most_common_quadgrams.values())
            elif which_frequency == "prefixes":
                sign_names = list(ff.most_common_prefixes.keys())
                sign_frequencies = list(ff.most_common_prefixes.values())
            elif which_frequency == "suffixes":
                sign_names = list(ff.most_common_suffixes.keys())
                sign_frequencies = list(ff.most_common_suffixes.values())
            elif which_frequency == "numbers":
                sign_names = list(ff.most_common_numbers.keys())
                sign_frequencies = list(ff.most_common_numbers.values())


        ax.bar(sign_names, sign_frequencies)
        fig.suptitle("Frequencies visualized")

        plt.show()



