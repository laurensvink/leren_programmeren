# name of student: 
# number of student:
# purpose of program: 
# structure of program: 

coinValues = [500,200,100,50,20,10,5,2,1]

# Opslaan hoeveel munten uiteindelijk teruggegeven worden
coins = {
  "500": 0,
  "200": 0,
  "100": 0,
  "50": 0,
  "20": 0,
  "10": 0,
  "5": 0,
  "2": 0,
  "1": 0
}

toPay = int(float(input('Amount to pay: ')) * 100)
paid = int(float(input('Paid amount: ')) * 100)
change = paid - toPay

while change > 0 and len(coinValues) > 0:

  coinValue = coinValues.pop(0)
  nrCoins = change // coinValue

  if nrCoins > 0:
    print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!')
    nrCoinsReturned = int(input('How many coins of ' + str(coinValue) + ' cents did you return? '))

    # Opslaan hoeveel munten werkelijk teruggegeven zijn
    coins[str(coinValue)] = nrCoinsReturned

    change -= nrCoinsReturned * coinValue

if change > 0:
  print('Change not returned: ', str(change) + ' cents')
else:
  print("\nCoins returned:")
  for c in coins:
    if coins[c] > 0:
      print(coins[c], "coins of", c, "cents")
  print('done')
