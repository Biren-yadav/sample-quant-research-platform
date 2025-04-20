import backtrader as bt

class SmaCrossStrategy(bt.Strategy):
    
    #50/200 SMA Crossover Strategy
    params = (('fast',50), ('slow',200))

    def __init__(self):
        self.sma_fast = bt.ind.SMA(period=self.p.fast)
        self.sma_slow = bt.ind.SMA(period=self.p.slow)
        self.crossover = bt.ind.CrossOver(self.sma_fast, self.sma_slow)

        def next(self):
            if not self.position:
                if self.crossover > 0:
                    self.buy()
            elif self.crossover < 0:
                self.sell()
