#!/usr/bin/env python

from requests import get as http_get
from random import choice
import hashlib


def get_default_word_list():
    url = "https://raw.githubusercontent.com/jhorowitz/domain-name-generation/master/wordlist.txt"
    expected_hash = "6d557f0693958fb5e650b68b5bee585eb82cf4da32965505c789e924743bc522"
    return get_word_list(url, expected_hash)


def get_word_list(url, expected_hash, minimum_word_length=4):
    text = http_get(url).text
    hashed = hashlib.sha256(text).hexdigest()

    assert hashed == expected_hash, "Unexpected hash: " + hashed + "\nResponse Text Truncated:\n" + text[:100]

    return [x for x in text.split("\n") if len(x) >= minimum_word_length]


def generate_domain(word_list, tld, words_per_domain=3):
    return "".join([choice(word_list) for _ in xrange(words_per_domain)]) + tld


def generate_domains(word_list, tld, domain_count, words_per_domain=3):
    return [generate_domain(word_list, tld, words_per_domain) for _ in xrange(domain_count)]


def main(tld, domain_count, word_list):
    generated = generate_domains(word_list, tld, domain_count)

    for v in generated:
        print v


if __name__ == '__main__':
    import sys
    import os

    if len(sys.argv) == 3:
        tld = sys.argv[1]
        if tld[0] != '.':
            tld = '.' + tld

        domain_count = int(sys.argv[2])

        main(tld, domain_count, get_default_word_list())

    elif "DGA_DOMAIN_COUNT" in os.environ and "DGA_TLD" in os.environ:
        tld = os.environ["DGA_TLD"]
        if tld[0] != '.':
            tld = '.' + tld
        domain_count = int(os.environ["DGA_DOMAIN_COUNT"])
        main(tld, domain_count, get_default_word_list())

    else:
        print "Usage: python dga.py <TLD> <domain_count>"
