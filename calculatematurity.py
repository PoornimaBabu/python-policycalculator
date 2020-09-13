#This is an external file

import sys

policynumber = sys.argv[1]
policyStartDate = sys.argv[2]
premium = sys.argv[3]
membership = sys.argv[4]
policynum = policynumber[0]

#If Policy type is A and Start Date is before 1990 it is eligible for one off cash bonus
if policynum == 'A' and policyStartDate < "01/01/1990":
    maturityamount=((int(premium) - (int(premium) * (0.03)) + 1000) * 1.25)
elif policynum == 'A' and policyStartDate > "01/01/1990":
    maturityamount=((int(premium) - (int(premium) * (0.03)) + 0) * 1.25)
#If Policy type is B and Membership is Yes it is eligible for one off cash bonus
elif policynum == 'B' and membership == "yes":
    maturityamount=((int(premium) - (int(premium) * (0.05)) + 1000) * 1.25)
elif policynum == 'B' and membership == "no":
    maturityamount=((int(premium) - (int(premium) * (0.05)) + 0) * 1.25)
#If Policy type is C, Start Date is before 1990 and Membership is Yes it is eligible for one off cash bonus
elif policynum == 'C' and policyStartDate < "01/01/1990" and membership == "yes":
    maturityamount=((int(premium) - (int(premium) * (0.07)) + 1000) * 1.25)
elif policynum == 'C' and policyStartDate > "01/01/1990" and membership == "no":
    maturityamount=((int(premium) - (int(premium) * (0.07)) + 0) * 1.25)
else :
    maturityamount=((int(premium) - (int(premium) * (3 / 100 )) + 0) * 1.25)


print("%d" % maturityamount)

