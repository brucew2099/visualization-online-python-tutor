# inputs:
amountBorrowed = 1000
annualRate = 0.08
currentYear = 2010
yearsToBorrow = 10

# output:
amountOwed = amountBorrowed

for _ in range(yearsToBorrow):
  currentYear = currentYear + 1
  amountOwed = amountOwed + (amountOwed * annualRate)
  currentYear = currentYear + 1

