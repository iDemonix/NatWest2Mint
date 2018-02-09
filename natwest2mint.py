#!/env/python

# NatWest2Mint
# https://github.com/iDemonix/NatWest2Mint

import argparse
import csv

# return a valid row for Mint
def mintRow(csvdate, csvamount, csvtype, csvdesc='', csvorigdesc='', csvcategory='', csvname='', csvlabels='', csvnotes=''):
    return "%s,%s,%s,%s,%s,%s,%s,%s,\"%s\"" % (csvdate, csvdesc, csvorigdesc, csvamount, csvtype, csvcategory, csvname, csvlabels, csvnotes)

# parse args
parser = argparse.ArgumentParser(description='converts a NatWest CSV to a Mint CSV for Quicken import')
parser.add_argument('-f', action="store", dest="file", required=True)
args = parser.parse_args()

# read csv line by line
with open(args.file) as f:
    content = f.readlines()

# strip whitespace
content = [x.strip() for x in content]

# remove blank lines
content = filter(None, content)

# remove column header row
content.pop(0)

for l in csv.reader(content, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
    # NWOLB format
    # 0=date, 1=type, 2=desc, 3=value, 4=balance, 5=acc_name, 6=acc_number

    # debit or credit
    if -float(l[3]) > 0:
        csvtype = 'debit'
        csvamount = -float(l[3])
    else:
        csvtype = 'credit'
        csvamount = float(l[3])

    # ensure 2 decimal places
    csvamount = '{0:.2f}'.format(csvamount)

    # convert dates to simplified English as that's what mint outputs
    csvdateparts = l[0].split('/')
    csvdate = "%s/%s/%s" % (csvdateparts[1], csvdateparts[0], csvdateparts[2])

    # output
    print mintRow(csvdate, csvamount, csvtype, l[5], l[6], '', l[1], '', l[2])
