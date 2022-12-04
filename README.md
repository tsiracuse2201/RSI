# Given a ticker, this calculates RSI for minute by minute calculations. 
This is meant as a template for anything working with RSI and data streaming. 
I found most program out there rather horrible so I just made my own. Ultimately, 
I would want to use something like this to fill market orders based on RSI rather than 
TWAP and VWAP because it is in between the two. VWAP can be overly selective for orders but 
TWAP is vulnerable to overpricing. 
