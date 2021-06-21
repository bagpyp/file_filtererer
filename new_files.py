import datetime as dt
from glob import glob 
from pandas import Series, to_datetime
from sys import argv  
from pprint import pprint

drive = 'files/'
pattern = '*.txt'


def new_files(date, day_buffer, drive=drive, pattern=pattern):
    """
    Function to only look at new-ish files given a fixed date
    Args: 
        date (string, like '03142021')
        day_buffer (int or string, like 10)
        drive (string, like 'files/')
        pattern (glob pattern like '*.txt'')
    Returns:
        list of files in drive that match pattern with names dated after date - day_buffer
    """
    files = [g.split('/')[-1].split('.')[0] for g in glob(drive+pattern)]
    if files:
        s = to_datetime(Series(files), format='%m%d%Y')
        nf = s[s>to_datetime(date,format='%m%d%Y') - dt.timedelta(days=int(day_buffer))].sort_values().dt.strftime('%m%d%Y')
        return [f'files/{f}.txt' for f in nf]
    
if __name__ == '__main__':
    if len(argv) == 3:
        pprint(new_files(argv[1],argv[2]))
    else:
        print('dispplaying files to check when date = 2021-10-31 '
        +'and day_buffer = 5')
        pprint(new_files('10312021',5))
