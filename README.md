#### Realistic Domain Name Generator

Generate memorable domain names

Basic Usage:
```bash
python dga.py <TLD> <domain_count>
```

Using shebang:
```bash
# You may need to set executable permissions using: chmod +x dga.py
./dga.py <TLD> <domain_count>
```

With environment variables:
```bash
DGA_DOMAIN_COUNT=<domain_count> DGA_TLD=<TLD> python dga.py
```

Without cloning the repo:
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

