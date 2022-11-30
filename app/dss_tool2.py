# Tool 2
def tool_2():
  import numpy as np # Import packages for math/statistical calculations & visualization
  from scipy.stats import norm
  import matplotlib.pyplot as plt
  import pandas as pd

  option = input("Please enter the ticker symbol for the option: ") # Obtain input values of stock name and strike price
  K = input("Please enter the strike price of your option: ")
  K = int(K)

  option_data = pd.read_csv(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={option}&apikey={API_KEY}&datatype=csv')
  df = pd.DataFrame(option_data) # Read stock values from API
  S = df["adjusted_close"][0] # Obtain current asset price
  df['returns'] = df["adjusted_close"].pct_change()
  sigma = df['returns'].std() * np.sqrt(252) # Obtain volatility of returns
  print(df)
  r_data = pd.read_csv(f'https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=monthly&maturity=10year&apikey={API_KEY}&datatype=csv')
  df_r = pd.DataFrame(r_data)
  r = df_r["value"][0] / 100 # Obtain curent risk-free interest rate
  T = 1 # Set time to 1


  N = norm.cdf
  print(S,K,T,r,sigma) # List current asset price, strike price, time, risk-free interest rate, and volatility of returns
  def CallPrice(S, K, T, r, sigma): # Black-Scholes
    d_1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d_2 = d_1 - sigma * np.sqrt(T)
    return S * N(d_1) - K * np.exp(-r*T)*N(d_2)
  def PutPrice(S, K, T, r, sigma):
    d_1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d_2 = d_1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * N(-d_2) - S * N(-d_1)
  print("The value of the call is", "{:.2f}".format(CallPrice(S,K,T,r,sigma))) # Output values of call/put options at strike price
  print("The value of the put is","{:.2f}".format(PutPrice(S,K,T,r,sigma)))

  greeks_choice = input("View greeks?") # Ask user to display Greek option parameters
  if greeks_choice == "Y":
    print("GREEKS:")
    OptionDelta = norm.cdf(np.log(S/K) + (r + sigma**2/2)*T / (sigma*np.sqrt(T))) # Calculate Greeks
    OptionGamma = norm.pdf(np.log(S/K) + (r + sigma**2/2)*T / (sigma*np.sqrt(T))) / (S * sigma * np.sqrt(T))
    OptionVega = norm.pdf(np.log(S/K) + (r + sigma**2/2)*T / (sigma*np.sqrt(T))) * S * np.sqrt(T)
    OptionTheta = (-S * norm.pdf(np.log(S/K) + (r + sigma**2/2)*T / (sigma*np.sqrt(T))) * sigma)/(2*np.sqrt(T)) - (r * K * np.exp(-r*T)*norm.cdf(np.log(S/K) + (r + sigma**2/2)*T / (sigma*np.sqrt(T))-(sigma*np.sqrt(T))))
    OptionRho = K * T * np.exp(-r*T)*norm.cdf(np.log(S/K) + (r + sigma**2/2)*T / (sigma*np.sqrt(T))-(sigma*np.sqrt(T)))
    print("Delta = ","{:.3f}".format(OptionDelta)) # Format output values
    print("Gamma = ","{:.3f}".format(OptionGamma))
    print("Vega = ","{:.3f}".format(OptionVega))
    print("Theta = ","{:.3f}".format(OptionTheta))
    print("Rho = ","{:.3f}".format(OptionRho))
    if OptionDelta >= 0:
      print("To hedge against this option's risk, please take a short position on","{:.0%}".format(OptionDelta),"of your total shares")
    else:
      print(print("To hedge against this option's risk, please take a long position on","{:.0%}".format(OptionDelta),"of your total shares"))

  sensitivity_choice = input("View call-put parity graph?") # Ask user to display visualization of option pricing
  if sensitivity_choice == "Y":
    S_min = input("Please input minimum asset price value: ") # Set minimum and maxmimum values for the x-axis
    S_min = int(S_min)
    S_max = input("Please input maximum asset price value: ")
    S_max = int(S_max)
    S_range = np.arange(S_min,S_max,0.1)
    calls = [CallPrice(S,K,T,r,sigma) for S in S_range] # Establish y-values for call/put options
    puts = [PutPrice(S,K,T,r,sigma) for S in S_range]
    plt.plot(S_range,calls,label="Call Value") # Visualize call-put parity
    plt.plot(S_range,puts,label="Put Value")
    plt.xlabel("$S_0$")
    plt.ylabel("Value")
    plt.legend()