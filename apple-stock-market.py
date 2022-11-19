# apple-stock-market.py

# Importing Libraries
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.io as pio
import matplotlib.pyplot as go
import matplotlib.dates as mpl_dates
from mpl_finance import candlestick_ohlc

# Loading Dataset
data = pd.read_csv("Apple_stock_history.csv")

# Checking data from file
print(data.head())
print(data.info())
print(data.isnull().sum())

# Drop NA data
data = data.dropna()

# Plot Style
# Chart-1 - loading from matplotlib.pyplot
go.style.use('ggplot')
figure, ax = go.subplots()

# Open-high-low-close chart
ohlc = data.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
ohlc['Date'] = pd.to_datetime(ohlc['Date'])
ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
ohlc = ohlc.astype(float)

# Label Chart axis and title
ax.set_xlabel('Date')
ax.set_ylabel('Price')
figure.suptitle('Daily Candlestick Chart of NIFTY50')
candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)

date_format = mpl_dates.DateFormatter('%d-%m-%Y')
ax.xaxis.set_major_formatter(date_format)
figure.autofmt_xdate()

figure.tight_layout()
plt.show()


# Chart-2 - loading from plotly library
figure = px.bar(data, x = "Date", y= "Close", color="Close")
figure.update_xaxes(rangeslider_visible=True)
figure.update_layout(title = "Twitter Stock Prices Over the Years2",
                     xaxis_rangeslider_visible=False)
figure.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=2, label="2y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
figure.show()


# Chart-3 - loading from plotly library
data["Date"] = pd.to_datetime(data["Date"], format = '%Y-%m-%d')
data['Year'] = data['Date'].dt.year
data["Month"] = data["Date"].dt.month
fig = px.line(data,
              x="Month",
              y="Close",
              color='Year',
              title="Complete Timeline of Twitter3")
fig.show()