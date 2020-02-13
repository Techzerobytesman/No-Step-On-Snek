from __future__ import print_function


type('tr' + "y this")


slogan = 'My school is the best'

activity = 'theater'






def how_eligible(essay):
    eligibility = 0
    if '!' in essay:
        eligibility = eligibility + 1
    if '?' in essay:
        eligibility = eligibility + 1
    if '"' in essay:
        eligibility = eligibility + 1
    if ',' in essay:
        eligibility = eligibility + 1
    print('eligibility rating is' + eligibility)

a = 'one string'
b = 'another'
c = a[:3] + ' and ' + b
print(c[6:10])





