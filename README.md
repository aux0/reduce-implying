# reduce-implying

`reduce-implying` reduces your implies!

## Usage

```
usage: reduce_implying [-h] [-c N] [-d {lr,rl,bi}] text word

positional arguments:
  text                  the text to be reduced
  word                  the word to reduce the text to

optional arguments:
  -h, --help            show this help message and exit
  -c N, --occurrence N  the occurrence of the word that will be used in case
                        of multiple matches (default: 1)
  -d {lr,rl,bi}, --direction {lr,rl,bi}
                        the direction of reduction; lr stands for left-to-
                        right, rl for right-to-left and bi for bidirectional
                        (default: rl)
```

## Examples

```
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
```

## Note

When selecting the word to reduce the text to don't forget that a word is also all of the non-space characters like apostrophes, commas, etc. For example, in the text `>there's a hue in my hue`, `>there's` would be a word while `there`, `there's` and `>there` wouldn't.

Happy reducing! :^)
