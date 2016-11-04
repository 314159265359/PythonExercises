days = "Mon Tue Wed Thu Fri Sat Sun"
months1 = "\nJan\nFeb\nMar\nApr\nMay\nJun"
months2 = "\nJul\nAug\nSep\nOct\nNov\nDec"

#sample = "Sample %r string with %r : %r"
sample = "Sample %r string with : %r"

print  "Here are the days: ", days
print  "Here are the months: ", months1, months2
#print sample % (months1,"%r", months2)
print sample % (months1,months2)

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""