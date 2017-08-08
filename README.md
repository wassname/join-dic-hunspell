join-dic-hunspell
=================

Join dic files to make a dic file for hunspell

## DESCRIPTION
Join dic files and wordlists to make a dic file for hunspell. This can be used
in TeXstudio and other programs. This repository includes some technical word
lists for testing. Also a generic .aff file to go with the produced .dic file.

## USAGE
``` bash
$ join_dicts.py [options] <file/directory>...
```

#### ARGS
``` bash
-d <dictionary1> <dictionary2> ... # Dictionaries to combine
```

#### EXAMPLE
``` bash
$ python join_dicts.py -d wordlist1.dic wordlist2.dic
```

#### LICENSE

This uses the same license as hunspell: GNU Lesser or General Public License or Mozilla Public License.
