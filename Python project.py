import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
nvidia= "NVDA"
benchmark = "SPY"
event_date= "2025-01-27"
start_date= "2024-07-27"
end_date= "2025-01-30"
nvidia_data = yf.download(nvidia,start=start_date,end=end_date)
spy_data = yf.download(benchmark,start=start_date,end=end_date)
plt.figure(figsize=(10, 5))
plt.plot(nvidia_data.index, nvidia_data["Close"], label="Nvidia (NVDA)", color="blue")
plt.axvline(pd.to_datetime(event_date), color="red", linestyle="--", label="DeepSeek Announcement")
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.title("Nvidia Stock Price Before & After DeepSeek")
plt.legend()
plt.show()
nvidia_data["Returns"] = nvidia_data["Close"].pct_change()
before_event = nvidia_data.loc[:event_date, "Returns"].mean() * 100
after_event = nvidia_data.loc[event_date:, "Returns"].mean() * 100
print(f"📊 Nvidia Average Daily Return Before Event: {before_event:.2f}%")
print(f"📊 Nvidia Average Daily Return After Event: {after_event:.2f}%")
plt.figure(figsize=(10, 5))
plt.plot(nvidia_data.index, nvidia_data["Close"] / nvidia_data["Close"].iloc[0], label="Nvidia (NVDA)", color="blue")
plt.plot(spy_data.index, spy_data["Close"] / spy_data["Close"].iloc[0], label="S&P 500 (SPY)", color="gray")
plt.axvline(pd.to_datetime(event_date), color="red", linestyle="--", label="DeepSeek Announcement")
plt.xlabel("Date")
plt.ylabel("Normalized Price")
plt.title("Nvidia vs S&P 500: Impact of DeepSeek")
plt.legend()
plt.show()
if spy_data.empty:
    print("Error: S&P 500 ETF (SPY) data not found. Check ticker or date range.")
else:
    print("SPY data loaded successfully!")
plt.figure(figsize=(10, 5))
plt.plot(nvidia_data.index, nvidia_data["Close"], label="Nvidia (NVDA)", color="blue")
plt.axvline(pd.to_datetime(event_date), color="red", linestyle="--", label="DeepSeek Announcement")
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.title("Nvidia Stock Price Before & After DeepSeek")
plt.legend()
plt.show()
plt.figure(figsize=(10, 5))
plt.plot(nvidia_data.index, nvidia_data["Close"] / nvidia_data["Close"].iloc[0], label="Nvidia (NVDA)", color="blue")
plt.plot(spy_data.index, spy_data["Close"] / spy_data["Close"].iloc[0], label="S&P 500 (SPY)", color="gray")
plt.axvline(pd.to_datetime(event_date), color="red", linestyle="--", label="DeepSeek Announcement")
plt.xlabel("Date")
plt.ylabel("Normalized Price")
plt.title("Nvidia vs S&P 500: Impact of DeepSeek")
plt.legend()
plt.show()