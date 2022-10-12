# Market View
Market View is a Python script that returns the most recent daily percentage changes for all stocks in the S&P 500 and downloads the data in an Excel file.

## Getting Started
### Prerequisites
- Python 3
### Installation
```
# Clone this repository
$ git clone https://github.com/seantrading/market-view

# Go into the repository
$ cd market-view

# Install dependencies
$ pip install -r requirements.txt
```
## Usage
To retrieve the data, run `$ python main.py`.

Your output should look something like this:
```
Gathering data for MMM
Gathering data for AOS
Gathering data for ABT
Gathering data for ABBV
Gathering data for ABMD
Gathering data for ACN
...
Gathering data for YUM
Gathering data for ZBRA
Gathering data for ZBH
Gathering data for ZION
Gathering data for ZTS
_ _ _ _ _ _ _ _ _

    Symbol                                 Name  Previous Close  Latest Price % Change
406    WBA       Walgreens Boots Alliance, Inc.           30.52         31.84    4.33%
482   MRNA                        Moderna, Inc.          119.32        123.42    3.44%
265    MKC    McCormick & Company, Incorporated           73.44         75.86     3.3%
278    MRK                    Merck & Co., Inc.           87.60         90.48    3.29%
276    MOS                   The Mosaic Company           51.06         52.69    3.19%
..     ...                                  ...             ...           ...      ...
179      F                   Ford Motor Company           12.20         11.36   -6.89%
258    LVS                Las Vegas Sands Corp.           42.50         39.29   -7.55%
307   NCLH  Norwegian Cruise Line Holdings Ltd.           12.90         11.91   -7.67%
34     BIO           Bio-Rad Laboratories, Inc.          428.93        392.95   -8.39%
450   WYNN                Wynn Resorts, Limited           73.09         64.14  -12.25%

[503 rows x 5 columns]

Excel file downloaded
```
