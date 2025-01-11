import logging
import pandas as pd
from datetime import datetime
from dataclasses import dataclass, field
from typing import List
from pybacktestchain.broker import Broker
from pybacktestchain.data_module import get_stocks_data

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@dataclass
class Tradesignals:
    broker: Broker
    max_allocation: float = 0.2  # Maximum allocation per asset

    def execute_trades(self, data: pd.DataFrame):
        """
        Execute trades based on the volume-based strategy signals.

        Args:
            data (pd.DataFrame): Market data with signals.

        Returns:
            pd.DataFrame: A DataFrame of executed trades (transaction log).
        """
        if "Position" not in data.columns:
            raise KeyError("Missing 'Position' column in data. Ensure signals are generated.")

        detailed_signals = []  # To track detailed signals for the first 20 days
        for date in sorted(data["Date"].unique()):
            daily_data = data[data["Date"] == date]
            prices = dict(zip(daily_data["ticker"], daily_data["Adj Close"]))

            for _, row in daily_data.iterrows():
                ticker = row["ticker"]
                signal = row["Position"]
                price = row["Adj Close"]
                max_position_value = self.broker.get_cash_balance() * self.max_allocation
                max_quantity = int(max_position_value / price)

                if signal == 1:  # Buy signal
                    quantity = min(max_quantity, int(self.broker.get_cash_balance() / price))
                    if quantity > 0:
                        self.broker.buy(ticker, quantity, price, date)
                        detailed_signals.append({"Date": date, "Ticker": ticker, "Signal": "BUY", "Price": price})

                elif signal == -1:  # Sell signal
                    if ticker in self.broker.positions:
                        self.broker.sell(ticker, self.broker.positions[ticker].quantity, price, date)
                        detailed_signals.append({"Date": date, "Ticker": ticker, "Signal": "SELL", "Price": price})

            # Stop tracking after 5 days
            if len(detailed_signals) >= 5:
                break

        logging.info("Detailed signals for the first 5 days:")
        for signal in detailed_signals:
            logging.info(signal)

        return self.broker.transaction_log

@dataclass
class VolumeBacktest:
    initial_date: datetime
    final_date: datetime
    universe: List[str] = field(default_factory=lambda: ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NVDA', 'INTC', 'CSCO', 'NFLX'])
    initial_cash: int = 1_000_000  # Initial cash in the portfolio
    verbose: bool = True
    broker: Broker = field(init=False)

    def __post_init__(self):
        self.broker = Broker(cash=self.initial_cash, verbose=self.verbose)

    def compute_signals(self, data: pd.DataFrame):
        """
        Generate trading signals based on a volume-based strategy.

        Args:
            data (pd.DataFrame): Market data.

        Returns:
            pd.DataFrame: Data with added trading signals.
        """
        logging.info("Generating volume-based signals...")
        data = data.sort_values(by=["ticker", "Date"])

        # Compute average volume over the last 15 days
        data["Avg Volume"] = data.groupby("ticker")["Volume"].transform(lambda x: x.rolling(15).mean())

        # Generate signals: 1 for high volume, -1 for low volume
        data["Position"] = 0
        data.loc[data["Volume"] > data["Avg Volume"] * 1.5, "Position"] = 1  # Buy signal
        data.loc[data["Volume"] < data["Avg Volume"] * 0.5, "Position"] = -1  # Sell signal

        data = data.dropna(subset=["Avg Volume"])  # Remove rows with NaN Avg Volume
        return data
