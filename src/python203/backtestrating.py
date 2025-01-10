
class BacktestRating:
    def __init__(self, backtest: Backtest):
        """
        Initialize the BacktestRating class with a Backtest object.
        :param backtest: Backtest object from pybacktestchain.
        """
        self.backtest = backtest
        self.results = None

    def run_backtest(self):
        """
        Executes the backtest and stores the results.
        """
        print("Running the backtest...")
        self.results = self.backtest.run_backtest()
        if self.results is None:
            raise ValueError("Backtest returned no results. Check the Backtest configuration.")

    def calculate_sharpe_ratio(self):
        """
        Calculate the Sharpe ratio.
        :return: Sharpe ratio as a float.
        """
        daily_returns = self.results['returns']
        if len(daily_returns) == 0 or np.std(daily_returns) == 0:
            return 0
        risk_free_rate = 0.01  # Annual risk-free rate
        excess_returns = daily_returns - risk_free_rate / 252  # Convert to daily
        return np.mean(excess_returns) / np.std(excess_returns)

    def calculate_max_drawdown(self):
        """
        Calculate the maximum drawdown.
        :return: Maximum drawdown as a float.
        """
        portfolio_values = self.results['portfolio_values']
        running_max = np.maximum.accumulate(portfolio_values)
        drawdowns = portfolio_values / running_max - 1
        return drawdowns.min()

    def calculate_win_rate(self):
        """
        Calculate the win rate of trades.
        :return: Win rate as a float between 0 and 1.
        """
        trades = self.results['trades']
        if len(trades) == 0:
            return 0
        return sum(trades) / len(trades)

    def calculate_metrics(self):
        """
        Calculate all metrics (Sharpe ratio, maximum drawdown, win rate).
        :return: Dictionary containing the calculated metrics.
        """
        if not self.results:
            raise ValueError("Backtest results not found. Run the backtest first.")

        sharpe_ratio = self.calculate_sharpe_ratio()
        max_drawdown = self.calculate_max_drawdown()
        win_rate = self.calculate_win_rate()

        return {
            "Sharpe Ratio": sharpe_ratio,
            "Maximum Drawdown": max_drawdown,
            "Win Rate": win_rate,
        }




