![Visit](visit.png)

# visit
`visit` is short for "visualize it" - a single command line to publish a visual story for given data.

### install
Execute in a terminal:
``` bash
brew tap varchar-io/visit && brew install visit
```

### demo
Type in terminal
``` bash
visit gdp-state.csv
```
>
> Visit URL: https://columns.ai/visual/93yYkQWBXXDyR1/T-sto2e3DKmsofyT

![visit demo graph](imgs/visit-demo.png)

### formats
Currently supports `.csv`, `.tsv` and `.json`, for JSON type, it has to be rows of object that share the same schema (nested types will be ignored for now).

### protocols
Currently only supports a local csv.

Future support include data from HTTP URL, Google spreadsheets and cloud storage (eg. S3) and Excel online.

### build
Use pyinstaller, if not installed, use `pip install -U pyinstaller` to install it.
``` bash
pyinstaller visit.py -F
```
