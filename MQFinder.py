import pandas as pd
import os

"""Uses the local excel file and converts it to a dataframe
    on instantiation. Will throw error if you try to get a quote on
    empty file."""
class quotes:
    def __init__(self):
        self.__quotes = pd.read_excel(r'MotivationalQuotesDatabase.xlsx')

    #deletes old excel file writes new one without used quote
    def __upDateQuotes(self):
        os.remove('MotivationalQuotesDatabase.xlsx')
        pd.to_excel('MotivationalQuotesDatabase.xlsx',
                    sheet_name = 'Quotes Database')

    def get_quote(self):

        quote_line = self.__quotes.sample()
        quote = quote_line.iloc[0][0]
        author = quote_line.iloc[0][1]
        formatString = quote + "\n" + author

        #prevents duplicate quotes has potetial to run out
        self.__quotes = self.__quotes[self.__quotes.Quote != quote]
        return formatString
