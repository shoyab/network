import string
msg = raw_input("any string goes here")

cypher = ""
#creates a alphabet of lowercase ascii characters
alphabet = string.ascii_lowercase

for a in msg:

    cypher = cypher + chr(((ord(a) - 95) % 26) + 97)

print cypher 