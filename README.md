# NatWest2Mint

Quick and simple Python script to convert NatWest CSV files in to Mint CSV files that can be imported in to Quicken.

Getting data out of NatWest and in to Quicken doesn't work out of the box. This script works best when you use the column layout in the screenshot below.

## Usage

Simply run the script against a valid NatWest CSV export:

```
$ python natwest2mint.py -f natwest.csv > mint.csv
```

Quicken seems to have an odd bug whereby every time you import, it adds it as a new credit card. Just highlight the transactions, drop them on your chosen account and delete the empty credit card.

### Quicken Columns

The data in NatWest and Mint exports differs, so I've found the best column layout looks like this:

![columns](https://i.imgur.com/0J9MaSj.png)

### Disclaimer

This script was written in 10 minutes at midnight, no guarantees of any kind.


