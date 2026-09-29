age = int(input('Age: '))
mr = float(input('Monthly Revenue: '))
cs = int(input('Credit Score: '))
yib = float(input('Years in Business: '))
hd = bool(input('Filed a bankruptcy: (True/False) '))
cn = input('Collateral Name: ')
cv = float(input('Collateral Value: '))


ml = 0
bf = 0

if age >= 21 and yib >= 2.0 and hd == False:
  print('Baseline met')
  if cs >= 720:
    ml = mr*3
    if mr >= 50000:
      bf = ml*0.015
      print('Base fee: 1.5%')
    else:
     bf = ml*0.025
     print('Base fee: 2.5%')


     if cv >= ml:
       print('Collateral Accepted')
     else:
      print('Collateral not Accepted')
    sfr = ml*bf
    print('Surcharge added')
    if ml % 5000 != 0:
      print('250 surcharge added')
      sfr += 250
      print('Updated fee is',sfr)

  elif cs >=620 and cs < 720:
    ml = mr*2.0
    if yib >= 5:
      bf = ml*2.0
      print('Base fee: 2.0%')
    else:
      bf = ml*0.035
      print('Base fee: 3.5%')
    if cv >= ml:
     print('Collateral Accepted')
    else:
     print('Collateral not Accepted')
     sfr = ml*bf
    print('Surcharge added')
    if ml % 5000 != 0:
          print('250 surcharge added')
          sfr += 250
          print('Updated fee is',sfr)

      
  else:
    print('Rejected: Credit score too low')
else:
  print('Baseline not met')

print('===========================')
print('Max loan',ml)
print('Base fee',bf)
