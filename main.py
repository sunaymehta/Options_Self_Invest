import all_imports as ai
import train as train

current_security_price = float(input('Enter the current value of underlying security: '))

min_option_strike_ticker = 50

print('Pick a direction amongst these 4 by entering the option number associated with it: ')

print('1. Security WILL BE ABOVE...')
print('2. Security WILL BE BELOW...')

direction_index = int(input('Enter the number 1 or 2: '))
client_limit_prediction = int(input('Enter the limit price: '))

if(direction_index>2 or direction_index<1):
    print('invalid input')
    pass

elif(direction_index == 1):   #Bull Call Spread OR Bull Put Spread
    print('You can take 2 possible strategies depending on your risk and return appetite: ')
    print('1. Bull Put Spread: For moderately bullish behaviour')
    sell_strike = (int(client_limit_prediction/50)*50)
    buy_strike = sell_strike - (2*min_option_strike_ticker)
    print('Buy',buy_strike,'Put Option')
    print('Sell',sell_strike,'Put Option')
    print('-----------------------------------')

    print('2. Bull Call Spread: For aggressively bullish behaviour')
    sell_strike = (int(client_limit_prediction/50)*50)
    buy_strike = sell_strike - (2*min_option_strike_ticker)
    print('Buy', buy_strike, 'Call Option')
    print('Sell', sell_strike, 'Call Option')
    print('-----------------------------------')
    print('Both these strategies will yield 100% positive results if the direction predicted is correct.')
    print('However, they will surely yield negative results if the direction predicted is incorrect')

elif(direction_index == 2): #Bear Call Spread OR Bear Put Spread
    print('You can take 2 possible strategies depending on your risk and return appetite: ')
    print('1. Bear Call Spread: For moderately bearish behaviour')
    sell_strike = (int((client_limit_prediction+49)/50)*50)
    buy_strike =  sell_strike + (2*min_option_strike_ticker)
    print('Buy', buy_strike, 'Call Option')
    print('Sell', sell_strike, 'Call Option')
    print('-----------------------------------')

    print('2. Bear Put Spread: For aggressively behaviour behaviour')
    sell_strike = (int((client_limit_prediction+49)/50)*50)
    buy_strike = sell_strike + (2*min_option_strike_ticker)
    print('Buy', buy_strike, 'Put Option')
    print('Sell', sell_strike, 'Put Option')
    print('-----------------------------------')
    print('Both these strategies will yield 100% positive results if the direction predicted is correct.')
    print('However, they will surely yield negative results if the direction predicted is incorrect')