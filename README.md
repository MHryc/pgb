# pdb

GeneBank (`*.gb` output from NCBI PSI-BLAST) parser prototype

```
usage: pgb [-h] -i INPUT [-r RECORD] [-f FIELD]

Parse GeneBank records

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to input file
  -r RECORD, --record RECORD
                        Index (0 based) of the record to print
  -f FIELD, --field FIELD
                        Pick which field of the record to show, options: locus, definition, accession, version, keywords, source, organism, comment, features, origin
```
