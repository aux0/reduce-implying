from __future__ import print_function
import argparse
import sys

epilog = '''
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

  reduce_implying.py ">there's a hue in my hue" hue 2
    >there's a hue in my hue
	
  reduce_implying.py "there's a hue in my hue" there's
    there's a hue in my hue
    there's a hue in my
    there's a hue in
    there's a hue
    there's a
    there's
'''

def reduce(text, word, occurrence):
	text = text.split()
	current = 1
	word_index = 0
	reduced = []
	
	for w in text:
		if (w == word):
			if (current == occurrence):
				break
			current += 1
		word_index += 1
	
	for i in range(len(text) - 1, word_index - 1, -1):
		reduced.append('{}'.format(' '.join(text[0:i + 1])))
		
	return reduced

def main():
	parser = argparse.ArgumentParser(prog='reduce_implying', epilog=epilog, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('text', metavar='t', help='the text to be reduced')
	parser.add_argument('word', metavar='w', help='the word to reduce the text to')
	parser.add_argument('occurrence', metavar='o', nargs='?', type=int, default=1, help='the occurence of w in t to use in case multiple occurrences are found (default: 1)')
	args = parser.parse_args()
	
	if (args.word not in args.text.split()):
		print('error: word \'{}\' wasn\'t found in the text'.format(args.word))
		sys.exit(1)
		
	count = args.text.count(args.word)
	
	if (count > 1 and (args.occurrence < 0 or args.occurrence > count)):
		print('error: occurrence #{} doesn\'t exist'.format(args.occurrence))
		sys.exit(1)
		
	print('\n'.join(reduce(args.text, args.word, args.occurrence)))
	
if (__name__ == '__main__'):
	main()
