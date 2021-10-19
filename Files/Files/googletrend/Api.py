import pandas as pd                        
from pytrends.request import TrendReq
pytrend = TrendReq()

# Get Google Hot Trends data
def get_keyword():
    df = pytrend.trending_searches(pn="united_states")
    return df