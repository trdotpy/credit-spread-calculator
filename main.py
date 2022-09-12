# Credit Spread Risk Calculator

# Trade Size
tradeSize = int(input('Enter the amount of spreads being traded: '))
# Strike price of long leg
longStrike = int(input('Enter the strike price of your long leg: '))
# Strike price of short leg
shortStrike = int(input('Enter the strike price of your short leg: '))
# Credit received by selling short leg
premReceived = float(input('Credit received: '))
# Width between two strikes
spreadWidth = abs(shortStrike - longStrike)
maxRisk = int(tradeSize * (spreadWidth - premReceived) * 100)


print(f'Spread width: {spreadWidth}')
print(f'Maximum risk: ${maxRisk}')


