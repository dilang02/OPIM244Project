# -*- coding: utf-8 -*-
"""OPIM 244 Final Project
*   Tool 1: Stock Price Visualization
* Tool 2: Option Pricing w/ Black-Scholes Model
  *   Determine Black-Scholes Inputs from API Data
  * Call-Put Parity Graph
  * Greeks & Delta Hedging Calculator
* Tool 3: Multi-Asset Portfolio Optimization
"""

# Tool 1
def tool_1():
  import pandas as pd
  # Import the CSV Data from AlphaVantage
  symbol = input("Please input the ticker symbol for your stock: ") # Request input values for stock symbol
  symbol = symbol.upper()
  stock_data = pd.read_csv(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&datatype=csv')
  df = pd.DataFrame(stock_data)
  print(df) # Output the values for the stock

  import plotly.express as px # Visualize stock price over time
  stock_chart = px.line(df,x="timestamp",y="adjusted_close",title=f"{symbol} Stock Price Over Time",labels={"timestamp":"Date","adjusted_close":"Price"})
  stock_chart.show()
