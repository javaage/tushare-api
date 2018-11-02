from dao.ichess import Sign

def getSignList():
    result = []
    query = Sign.select();
    for sign in query:
        result.append(sign)
    return result

def getSignByCode(code):
    query = Sign.select().where(Sign.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveSign(sign):
    return Sign.insert(sign).execute()

def updateSign(sign):
    return Sign.update(sign).where(Sign.code==sign['code']).execute()

def deleteSign(code):
    return Sign.delete().where(Sign.code==code).execute()