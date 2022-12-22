import os

def makeQuery():
    result = {}
    qstr = os.getenv('QUERY_STRING', '')
    parts = qstr.split('&')
    for part in parts:
        pieces = part.split('=')
        if len(pieces) > 1:
            result[pieces[0]] = pieces[1]
        if len(pieces) == 1:
            result[pieces[0]] = ''

    return result

query = makeQuery()

print("Content-type: text/html")
print()

if 'name' in query:
    person = query['name']
else:
    person = 'unknown'

print(f'<html><body><h3>Hello {person}</h3></body></html>')