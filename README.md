#### Realistic Domain Name Generator

Generate memorable domain names

Usages:
```bash
python dga.py <TLD> <domain_count>
```

```bash
DGA_DOMAIN_COUNT=<domain_count> DGA_TLD=<TLD> python dga.py
```

You can also use the generator without without cloning the repo
```bash
curl -s "https://raw.githubusercontent.com/jhorowitz/domain-name-generation/master/dga.py" | DGA_DOMAIN_COUNT=<domain_count> DGA_TLD=<TLD> python
```

Example:

```bash
➜  curl -s "https://raw.githubusercontent.com/jhorowitz/domain-name-generation/master/dga.py" | DGA_DOMAIN_COUNT=10 DGA_TLD=co.uk python
viscositycustomerexalted.co.uk
arguegreyhoundzigzagged.co.uk
runwayquiverimmovable.co.uk
unclogsemesteremerald.co.uk
sinisterpromotermuck.co.uk
mooingpunisherunvarying.co.uk
richnesswrongfulenviable.co.uk
harvestuntrueelastic.co.uk
breweryclassbriskly.co.uk
spoolhardshipcanal.co.uk
```

##### TODO:
Separate word list into parts of speech (nouns, verbs, etc.) to make better domain names

