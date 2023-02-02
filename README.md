# Yahoo Finance Dashboard
This Dashboard uses Yahoo ticker symbols for identifying financial securities and fetches the
available historical data from Yahoo servers. The downloaded data is returned in the form of a
data object wrapping a Pandas DataFrame (Fields: Open, High, Low, Close, Volume).

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![pythonbadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# Demo

https://user-images.githubusercontent.com/45914161/216418332-4ee161f7-a165-40ca-89a7-838f3af6f07b.mp4

# Features of the Dashboard

- The yfinance data is used to build OHLC (candle stick graph) and Volume graphs.
- Users can select a stock from multiple stocks available.
- Users can select which technical indicator they want to apply.
- Users can select the date range for the data to be displayed on the graphs.

## Technology Stack 

1. Python 
2. Plotly Dash
3. Pandas
4. Plotly

# How to Run

To see the project working, just clone the repository and install all required libraries within requirements.txt file and run the project :)

- Clone the repository
- Setup Virtual environment
```
$ python3 -m venv env
```
- Activate the virtual environment
```
$ source env/Source/activate
```
- Install dependencies using
```
$ pip install -r requirements.txt
```
- Run index.py file

## Contact

For any feedback or queries, please reach out to me at [suwaidaslam@gmail.com](suwaidaslam@gmail.com) or My Linkedin @suwaidaslam.
