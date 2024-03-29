# INF 601 - Advanced Programming in Python
# Eve Wright
# Mini Project 1


import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from pathlib import Path


# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite
#                stock tickers for the last 10 trading days.
# (10/10 points) Store this information in a list that you will convert to a array in NumPy.
# (10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the
#                documentation for matplotlib. At minimum it just needs to show 10 data points.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder,
#                the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt
#                file which contains all the packages that need installed. You can create this fille with the output
#                of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the
#                pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.

def getClose(ticker):
    stock = yf.Ticker(ticker)
    history = stock.history(period='10d')
    closeList = []

    for price in history['Close']:
        closeList.append(price)

    closeArray = np.array(closeList)

    return closeArray

def graphClose(closeArray):
    days = list(range(1, len(closeArray) + 1))
    plt.plot(days, closeArray, 'b-o')
    # Change x-axis step to 1
    plt.xticks(np.arange(min(days), max(days)+1, 1))
    plt.xlim(max(days) + .25, min(days) - .25)

    # Create all labels
    plt.xlabel('Trading Days (Ago)')
    plt.ylabel('Closing Price')
    plt.suptitle(str(ticker))
    plt.title('Closing Price in last 10 Trading Days')

    # Save graph as png in charts
    savefile = 'charts/' + ticker + '.png'
    plt.savefig(savefile)

    plt.show()


# Create charts folder
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

# List of 5 stock tickers
tickers = ['EL', 'IPAR', 'PG', 'LRLCY', 'GPS']

# Main code, runs both functions
for ticker in tickers:
    graphClose(getClose(ticker))




