import numpy as np
import pandas as pd
from holidays_fetcher import HolidaysFetcher
import time

list_years = np.arange(1370, 1431)

if __name__ == '__main__':
    # convert each item in list to str
    list_years = [str(i) for i in list_years]

    hf = HolidaysFetcher()
    # create an empty dataframe to aggregate data from different years
    df = pd.DataFrame()
    for year in list_years:
        hf.run_pipe2time(year)

        df = pd.concat([df, hf.parse_holiday_json(year)])
        time.sleep(0.1)

    # save as csv
    df.to_csv('iran_holidays.csv')
