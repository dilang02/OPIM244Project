# Tool 3
def tool_3():
  import pandas as pd # Import packages for math/data visualization
  import numpy as np
  import matplotlib.pyplot as plt
  # Import the CSV Data from AlphaVantage
  symbol_list = [] # Establish variables as empty lists & dataframes
  stock_list =[]
  df_list = []
  df_p_list = []
  df_p = pd.DataFrame()
  returns_p = pd.DataFrame()

  while True: # Allow for multiple stock inputs with while loop, exit loop once all stocks have been inputted
    symbol_input = input("Please input the ticker symbol for your stock: ")
    if symbol_input == "DONE":
      break
    else:
      symbol_input = symbol_input.upper()
      symbol_list.append(symbol_input)
  for x in range(len(symbol_list)): # Create dataframe of portfolio & returns using correct stocks
    stock_data = pd.read_csv(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol_list[x]}&apikey={API_KEY}&datatype=csv')
    stock_list.append(stock_data)
    df_data = pd.DataFrame(stock_data)
    df_list.append(df_data)
    df_p[symbol_list[x]] = df_data['adjusted_close']
    df_p_list.append(df_p)
    returns_p[symbol_list[x]] = df_p[symbol_list[x]].pct_change()

  print("STOCKS:",symbol_list,) # Output the returns portfolio with listed stocks
  print(returns_p)

  cov_matrix = returns_p.cov()*252 # Calculate and display the covariance matrix
  cov_matrix

  p_returns = [] # Create more variables for efficient frontier determination
  p_volatility = []
  p_weights = []
  assets = len(df_p.columns)
  portfolios = 10000
  i_returns =  returns_p.mean()

  for x in range(portfolios): # Simulation model to generate possible portfolios
    weights = np.random.random(assets)
    weights = weights / np.sum(weights)
    p_weights.append(weights)
    returns = np.dot(weights, i_returns)
    p_returns.append(returns)
    var = cov_matrix.mul(weights, axis=0).mul(weights,axis=1).sum().sum()
    sd = np.sqrt(var)
    ann_sd = sd*np.sqrt(250)
    p_volatility.append(ann_sd)
  
  data = {'Returns':p_returns, 'Volatility':p_volatility} # Create weighted portfolio dataframe with all simulations
  for a, b in enumerate(df_p.columns.tolist()):
    data[b+' weight'] = [w[a] for w in p_weights]
  final_df = pd.DataFrame(data)
  print(final_df.head()) # Display dataframe and covariance matrix
  print(cov_matrix)

  final_df.plot.scatter(x='Volatility',y='Returns') # Visualize the efficient frontier
  plt.xlabel("Risk")
  plt.ylabel("Expected Returns")

  min_vol = final_df.iloc[final_df['Volatility'].idxmin()] # Determine portfolio with the lowest volatility and output
  print("Minimum Volatility Portfolio:")
  print(min_vol)

  rf = input("Please input risk tolerance") # Determine optimal risky portfolio given risk tolerance value and output
  rf = float(rf)
  optimal_p = final_df.iloc[((final_df['Returns']-rf)/final_df['Volatility']).idxmax()]
  print("Optimal Risky Portfolio:")
  print(optimal_p)