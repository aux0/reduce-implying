from __future__ import print_function
import argparse
import sys

EPILOG = '''
note:
  When selecting the word to reduce the text to don't forget
  that a word is also all of the non-space characters
  like apostrophes, commas, etc. For example, in the text
  ">there's a hue in my hue", ">there's" would be a word and
  not "there", "there's" or ">there".

examples:
  reduce_implying.py ">there's a hue in my hue" hue
    >there's a hue in my hue
    >there's a hue in my
    >there's a hue in
    >there's a hue

  reduce_implying.py ">there's a hue in my hue" hue -c 2
    >there's a hue in my hue

  reduce_implying.py "there's a hue in my hue" there's
    there's a hue in my hue
    there's a hue in my
    there's a hue in
    there's a hue
    there's a
    there's

  reduce_implying.py "there's a hue in my hue" hue -d bi
    there's a hue in my hue
    a hue in my
    hue in
    hue

  reduce_implying.py "there's a hue in my hue" hue -c 2 -d lr
    there's a hue in my hue
    a hue in my hue
    hue in my hue
    in my hue
    my hue
    hue
'''

def reduce_implying(text, word, occurrence, direction):
    text = text.split()
    current_occurence = 1
    word_index = 0
    reduced = []

    # locate the nth occurence of word in text
    for current_word in text:
        if current_word == word:
            if current_occurence == occurrence:
                break
            current_occurence += 1
        word_index += 1

    # build a list of indices of words that come before/after our word (including the word itself)
    # [0, word_index]
    lr_indices = range(0, word_index + 1)
    # [end_of_text, word_index]
    rl_indices = range(len(text) - 1, word_index - 1, -1)

    # now use those indices to gradually slice shorter and shorter portions of our text until we get a list containing only our word
    if direction == 'lr':
        for lbound in lr_indices:
            reduced.append(' '.join(text[lbound:]))
    elif direction == 'rl':
        for ubound in rl_indices:
            reduced.append(' '.join(text[:ubound + 1]))
    elif direction == 'bi':
        # we first pad the shorter list with -1
        l = abs(len(lr_indices) - len(rl_indices))

        (lr_indices if len(lr_indices) < len(rl_indices) else rl_indices).extend([-1] * l)

        # then we slice our text using pairs of indices from the two lists
        # if we find a -1 we slice starting from/ending at word_index
        for lbound, ubound in zip(lr_indices, rl_indices):
            if lbound == -1:
                reduced.append(' '.join(text[word_index:ubound + 1]))
            elif ubound == -1:
                reduced.append(' '.join(text[lbound:word_index + 1]))
            else:
                reduced.append(' '.join(text[lbound:ubound + 1]))

    return reduced

def main():
    parser = argparse.ArgumentParser(prog='reduce_implying', epilog=EPILOG, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('text', help='the text to be reduced')
    parser.add_argument('word', help='the word to reduce the text to')
    parser.add_argument('-c', '--occurrence', metavar='N', type=int, default=1, help='the occurrence of the word that will be used in case of multiple matches (default: 1)')
    parser.add_argument('-d', '--direction', choices=['lr', 'rl', 'bi'], default='rl', help='the direction of reduction; lr stands for left-to-right, rl for right-to-left and bi for bidirectional (default: rl)')
    args = parser.parse_args()

    if args.word not in args.text.split():
        print('error: word \'{}\' wasn\'t found in the text'.format(args.word))
        sys.exit(1)

    count = args.text.count(args.word)

    if count > 1 and (args.occurrence < 0 or args.occurrence > count):
        print('error: occurrence #{} doesn\'t exist'.format(args.occurrence))
        sys.exit(1)

    print('\n'.join(reduce_implying(args.text, args.word, args.occurrence, args.direction)))

if __name__ == '__main__':
    main()
