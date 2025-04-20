import backtrader as bt
from .strategies import SmaCrossStrategy

def run_backtest(data, strategy=SmaCrossStrategy, initial_cash=100000):
    #Run backtest with Backtrader
    cerebro = bt.Cerebro()
    data_feed = bt.feeds.PandasData(dataname=data)
    cerebro.adddata(data_feed)
    cerebro.addstrategy(strategy)
    cerebro.broker.set_cash(initial_cash)
    
    # Add analyzers
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
    
    results = cerebro.run()
    return {
        'cerebro': cerebro,
        'results': results[0],
        'sharpe': results[0].analyzers.sharpe.get_analysis(),
        'drawdown': results[0].analyzers.drawdown.get_analysis()
    }