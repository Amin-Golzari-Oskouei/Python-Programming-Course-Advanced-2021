import subprocess
import os
import time
import jdatetime
import pandas as pd
import json
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class HolidaysFetcher:

    def __init__(self):
        pass

    def run_pipe2time(self, year: str):
        """
        Run pipe2time node module on the given year.
        this function first needs node js to be installed in the os
        then 'npm i' command on the pipe2time folder to install corresponding dependencies

        Parameters
        ----------
        year : str
            Year to run

        Returns
        ----------
        None :
            None but the pipe2time output is saved in the pipe2time/api folder
        """

        path_pipe2time = os.path.join(ROOT_DIR, 'pipe2time.ir')

        proc = subprocess.Popen(['npm', 'start', '--prefix', path_pipe2time.__str__()], shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        time.sleep(1)
        proc.stdin.write('{}\n'.format(year).encode('utf-8'))
        # proc.stdin.flush()
        time.sleep(1)
        proc.stdin.write('{}\n'.format('Y').encode('utf-8'))
        # proc.stdin.flush()
        time.sleep(1)
        proc.stdin.write('{}\n'.format('Y').encode('utf-8'))
        # proc.stdin.flush()

        stdout, stderr = proc.communicate()
        print(stdout, stderr)
        time.sleep(2)

    def parse_holiday_json(self, year: str):
        """
        Parse fetched json for a given year which is save in pipe2time/api and return corresponding dataframe

        Parameters
        ----------
        year : str
            Year to parse

        Returns
        ----------
        df : pandas.DataFrame
            dataframe containing holidays for the year
        """

        df = pd.DataFrame(columns=['date', 'fa_date', 'reason'])

        path_index = os.path.join(ROOT_DIR, 'pipe2time.ir', 'api', year, 'index.json')

        with open(path_index, encoding='utf-8') as handle:
            json_dict = json.loads(handle.read())

        for d_month in json_dict[year]:
            for event in d_month['events']:
                if event['isHoliday']:
                    df.loc[len(df)] = [datetime.strptime(event['mDate'], '%Y/%m/%d'),
                                       int(jdatetime.datetime.strptime(event['jDate'], '%Y/%m/%d').strftime(
                                           '%Y%m%d')),
                                       event['text']]
        return df
