from crud import csv

'''
[]-
[]
now
'''
@csv.route('/csv/<int:head>:<int:tail>')
@csv.route('/csv/<int:head>:<int:tail>:<int:scale>')
def csv(head=0, tail=-0, scale=1):
    return

