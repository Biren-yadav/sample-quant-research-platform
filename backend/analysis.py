import matplotlib.pyplot as plt
from pyfolio import create_full_tear_sheet

def generate_tear_sheet(returns):
    #Generate PyFolio performance report
    return create_full_tear_sheet(returns)