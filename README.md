reduce-implying
===============

`reduce-implying` reduces your implies!

Usage
=====

```
usage: reduce_implying [-h] t w [o]

positional arguments:
  t           the text to be reduced
  w           the word to reduce the text to
  o           the occurence of w in t to use in case multiple occurrences are found (default: 1)
```

Examples
========

```
reduce_implying.py ">there's a hue in my hue" hue
    >there's a hue in my hue
    >there's a hue in my
    >there's a hue in
    >there's a hue
```

```
reduce_implying.py ">there's a hue in my hue" hue 2
    >there's a hue in my hue
```

```
reduce_implying.py "there's a hue in my hue" there's
    there's a hue in my hue
    there's a hue in my
    there's a hue in
    there's a hue
    there's a
    there's
```

Note
====
When selecting the word to reduce the text to don't forget that a word is also all of the non-space characters like apostrophes, commas, etc. For example, in the text `>there's a hue in my hue`, `>there's` would be a word while `there`, `there's` and `>there` wouldn't.

Happy reducing! :^)
