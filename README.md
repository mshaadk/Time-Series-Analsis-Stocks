# Time Series Analysis - Stocks

## Overview

The **Time Series Analysis - Stocks** application is a web-based tool for analyzing stock market data. Built using Python, Streamlit, and Plotly, this application allows users to visualize historical stock prices through different types of charts. 

Key features include:
- **Line Plot**: Visualizes the closing prices of a stock over time.
- **Candlestick Chart**: Provides a detailed view of stock price movements with open, high, low, and close values.
- **Bar Plot**: Displays the closing prices using a bar chart.
- **Interactive Candlestick Chart**: Features interactive buttons and a slider for a more dynamic analysis.

## Requirements

Before running the application, ensure you have the following Python packages installed:
- `pandas`
- `yfinance`
- `streamlit`
- `plotly`

You can install the required packages using pip:

```bash
pip install pandas yfinance streamlit plotly
```

## Usage
### 1. Clone the Repository

```bash
git clone https://github.com/mshaadk/Time-Series-Analsis-Stocks.git
cd Time-Series-Analsis-Stocks
```

### 2. Run the Application

Navigate to the project directory and start the Streamlit server:

```bash
streamlit run app.py
```

This command will open the application in your default web browser.

### 3. Enter Stock Ticker Symbol

On the left sidebar, you will find a text input field where you can enter the ticker symbol of the stock you want to analyze (e.g., `AAPL` for Apple Inc.). The application will fetch historical data and display the following charts:

- **Line Plot**: Shows the closing prices over time.
- **Candlestick Chart**: Displays detailed price movements.
- **Bar Plot**: Represents closing prices with bars.
- **Interactive Candlestick Chart**: Allows for detailed exploration with a range slider and date selector buttons.

## Example
Here's an example of what you can expect when using the application:

1. **Enter Stock Symbol**: `AAPL`
2. **View Charts**: Observe the various charts provided (Line Plot, Candlestick Chart, Bar Plot, and Interactive Candlestick Chart) for the Apple Inc. stock.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please submit a pull request or open an issue.

## Contact
For questions or inquiries, please contact [Mohamed Shaad](https://www.linkedin.com/in/mohamedshaad/).
