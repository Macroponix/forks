def extractText(dct):
    res = []
    
    if 'text' in dct:
        res.append(dct['text'].strip())
        
    if dct['children']:
        for x in dct['children']:
            res.append(extractText(x))
    
    return res
