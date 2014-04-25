#!/usr/bin/env python
#coding=utf8
"""
Join dic files to make a dic file for hunspell.
    
USAGE: join_dicts.py [options] <file/directory>...

DESCRIPTION
Join dic files to make a dic file for hunspell.

ARGS:
    -d  dictionaries to combine
    
EXAMPLE: python join_dicts.py -d en_GB_geo.dic en_NZ_geo_oil_maori.dic


VERSION

    $Id$

"""

"""

TOOLS
http://marcoagpinto.cidadevirtual.pt/proofingtoolgui.html An Open Source tool coded in PureBasic for editing the Dictionary/Thesaurus/Hyphenation of OpenOffice/LibreOffice/Firefox/Thunderbird
http://latexeditor.org/credits.html
"""


import sys, os
import argparse


def skeleton(input):
    """
    The main function of this program. 
    """
    # read in dics
    # remove silly lines
    # sort
    # check for encoding?
    # write count as first line
    # write lines
    files=os.listdir(input)
    input=[]
    for i in files:
        if os.path.isfile(i):
            if os.path.splitext(i)[1]=='.dic':
                input.append(i)
            if os.path.splitext(i)[1]=='.txt':
                input.append(i)
    
    def remove_values_from_list(the_list, val):
        return [value for value in the_list if value != val]
        
    def remove_dups(seq):
        seen = set()
        seen_add = seen.add
        return [ x for x in seq if x not in seen and not seen_add(x)]
        
    def remove_non_unicode(seq):
        seen = set()
        seen_add = seen.add
        newseq=[]
        for v in seq:
            try:
                newseq.append(unicode(v,'utf-8'))
            except UnicodeDecodeError:
                pass
            #except UnicodeEncodeError:
            #pass
        return newseq
    
    print "Dictionarys to combine: ", input
    wordlist=[]
    # open them all
    for obj in input:
        lines=open(obj,'r').readlines()
        if lines[0].strip().isdigit():
            lines=lines[1:] # remove the first lien which is a wordcount in dic files
        wordlist.extend(lines)
    print "Uncleaned wordlist is", len(wordlist)
    wordlist.sort() # sort the content
    wordlist=remove_values_from_list(wordlist,'\n')
    wordlist=remove_dups(wordlist)
    wordlist=remove_non_unicode(wordlist)

    len_rows=str(len(wordlist))+'\n'  # get length
    
    import codecs
    outfile=codecs.open(args.out,'w','UTF-8')
    outfile.write(len_rows)
    #from django.utils.encoding import smart_str
    for word in wordlist:
        outfile.write((word))
    print "Output words", len_rows
    
    outfile.close()
        
#skeleton


def main():
    """
    Main entry point.

    Note that the input file can be specified as - in which case standard
    input is used. Passing the -h argument causes a help text to be printed.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__.split('\n\n\n')[0],
        epilog='You can add some extra information about the arguments here.')
    parser.add_argument('-o','--out', default=sys.stdout)
    parser.add_argument('dics',type=str,  help='directory with text files or dics to be combines')
    global args
    args = parser.parse_args()
    skeleton(args.dics)


if __name__ == '__main__':
    main()
