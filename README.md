# NatWest2Mint

Quick and simple Python script to convert NatWest CSV files in to Mint CSV files that can be imported in to Quicken. 

## Usage

Simply run the script against a valid NatWest CSV export:

```
$ python natwest2mint.py -f natwest.csv > mint.csv
```

Quicken seems to have an odd bug whereby every time you import from a Mint CSV, it adds it as a new credit card. Just highlight the transactions, drop them on your chosen account and delete the empty credit card. YMMV.

### Quicken Columns

The data in NatWest and Mint exports differ, so I've found the best column layout looks like this:

![columns](https://i.imgur.com/0J9MaSj.png)

### Disclaimer

This script was written in 10 minutes at midnight, no guarantees of any kind.


