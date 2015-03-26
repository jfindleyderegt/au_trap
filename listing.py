import os

path    = '/home/faedrus/Documents/au_trap/20141013/'
listing = os.listdir(path)
listing = sorted (listing)
file = open('listing.txt', 'w')
for i in range (len(listing)):
    file.write(listing[i])
    file.write('\n')
file.close()
