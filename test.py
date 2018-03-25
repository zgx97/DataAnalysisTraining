#!/usr/bin/env python
# coding=utf-8


import pandas as pd 

budget = pd.read_csv("./data.csv")
budget = budget.sort_values('Count', ascending=False)[:5]
print budget

# pd.options.display.mpl_style = 'default'
print type(budget)
budget_plot = budget.plot(kind="bar", x=budget['Word'], title="Words Count Table", legend=False)
print "budge : %s" % budget['Word']
fig = budget_plot.get_figure()
fig.savefig("test.png")