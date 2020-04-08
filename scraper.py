import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur

from typing import List


indexes = ['MSFT', 'goog', 'aapl']


class StockScraper:

    def __init__(self, ticker_index: str):
        self.ticker_index = ticker_index
        self.data_segments = ['/financials?p=', '/balance-sheet?p=', '/cash-flow?p=']
        self.financials = None
        self.balance_sheet = None
        self.cash_flow = None
        self.key_stats = None
        self.base_url = 'https://finance.yahoo.com/quote/'

    def pull_format_filter_web_data(self, scrape_url: str):
        read_data = ur.urlopen(scrape_url).read()
        souped_data = BeautifulSoup(read_data, 'lxml')
        step1 = []
        for data in souped_data.find_all('div'):
            step1.append(data.string)
        step2 = [e for e in step1 if e not in ('Operating Expenses', 'Non-recurring Events')]
        step3 = list(filter(None, step2))
        return step3[12:]

    def convert_to_dataframe(self, data: list) -> pd.DataFrame:
        formatted_data = list(zip(*[iter(data)]*6))
        framed_data = pd.DataFrame(formatted_data[0:])
        return framed_data

    def pull_all_data(self):
        pulls = []
        for segment in self.data_segments:
            pull_url = self.base_url + self.ticker_index + segment + self.ticker_index
            preframe_data = self.pull_format_filter_web_data(pull_url)
            pulls.append(self.convert_to_dataframe(preframe_data))
        self.parse_out_data(pulls)

    def parse_out_data(self, pulls: List[pd.DataFrame]):
        self.financials, self.balance_sheet, self.cash_flow = pulls

    def pull_segment_data(self, segment: str) -> pd.DataFrame:
        pull_url = self.base_url + self.ticker_index + segment + self.ticker_index
        preframe_data = self.pull_format_filter_web_data(pull_url)
        return self.convert_to_dataframe(preframe_data)

    def pull_key_statistics(self) -> None:
        pull_url = self.base_url + self.ticker_index + '/key-statistics?p=' + self.ticker_index
        df_list = pd.read_html(pull_url)
        result_df = df_list[0]
        for df in df_list[1:]:
            result_df = result_df.append(df)
        self.key_stats = result_df.set_index(0).T
        breakpoint()


if __name__ == "__main__":
    scraper = StockScraper(indexes[1])
    #scraper.pull_all_data()
    #breakpoint()
    #scraper.pull_segment_data('/key-statistics?p=')
    scraper.pull_key_statistics()
