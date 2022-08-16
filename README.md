# visit
`visit` is short for "visualize it" - a single command line to publish a visual story for given data.

### install
> ~% brew install visit

### demo
> ~% visit https://raw.githubusercontent.com/varchar-io/visit/main/gun-incidents-2014-2022.csv
> https://columns.ai/visual/GtTxG66t55eIA5/T-flXJbu7llNeav8

### formats
Currently supports `.csv`, `.tsv` and `.json`, for JSON type, it has to be rows of object that share the same schema (nested types will be ignored for now).

### protocols
Currently only supports HTTP URL, local file, Google spreadsheets. Future support may include cloud storage (eg. S3) and Excel online.

### build
Use pyinstaller, if not installed, use `pip install -U pyinstaller` to install it.
> pyinstaller visit.py -F
