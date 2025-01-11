from dataclasses import dataclass, field
import logging
import pandas as pd
from datetime import datetime
from dataclasses import dataclass, field
from typing import List
from pybacktestchain.broker import Broker
from pybacktestchain.data_module import get_stocks_data

@dataclass
class BacktestRating:
    sharpe_threshold: float = 1.0
    max_drawdown_threshold: float = -0.2

    def rate_backtest(self, metrics: dict) -> float:
        """
        Calculates a rating score for the backtest from 0 to 10 based on Sharpe Ratio and Max Drawdown.

        Args:
            metrics (dict): Performance metrics from the backtest.

        Returns:
            float: Rating score between 0 and 10.
        """
        sharpe_ratio = metrics.get("Sharpe Ratio")
        max_drawdown = metrics.get("Maximum Drawdown")

        if sharpe_ratio is None or max_drawdown is None:
            return 0.0  # Insufficient data yields the lowest score

        # Sharpe Ratio Score (75% weight)
        sharpe_score = min(7.5, max(0, sharpe_ratio / self.sharpe_threshold * 7.5))

        # Maximum Drawdown Score (25% weight, inverted scale)
        if max_drawdown <= self.max_drawdown_threshold:
            max_drawdown_score = 0
        else:
            max_drawdown_score = min(2.5, max(0, (1 + max_drawdown / self.max_drawdown_threshold) * 2.5))

        # Final weighted score
        total_score = sharpe_score + max_drawdown_score
        return round(min(total_score, 10), 2)

@dataclass
class BacktestEvaluator:
    def compute_metrics(self, trades: pd.DataFrame):
        """
        Calculates performance metrics: Sharpe Ratio, Max Drawdown, and Win Rate.

        Args:
            trades (pd.DataFrame): Transaction log.

        Returns:
            dict: Dictionary containing Sharpe Ratio and Max Drawdown.
        """
        logging.info("Calculating performance metrics...")

        if trades.empty:
            logging.error("No trades executed. Cannot calculate metrics.")
            return {"Sharpe Ratio": None, "Maximum Drawdown": None}

        # Calculate daily returns
        trades["Daily Returns"] = trades["Price"].pct_change().dropna()

        # Sharpe Ratio
        risk_free_rate = 0.01  # Annualized risk-free rate
        daily_excess_returns = trades["Daily Returns"] - (risk_free_rate / 252)  # Excess returns
        sharpe_ratio = daily_excess_returns.mean() / daily_excess_returns.std()

        # Maximum Drawdown
        rolling_max = trades["Price"].cummax()
        drawdown = (trades["Price"] - rolling_max) / rolling_max
        max_drawdown = drawdown.min()

        return {
            "Sharpe Ratio": sharpe_ratio,
            "Maximum Drawdown": max_drawdown,
        }