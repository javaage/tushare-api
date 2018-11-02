from dao.ichess import Attend

def getAttendList():
    result = []
    query = Attend.select();
    for attend in query:
        result.append(attend)
    return result

def getAttendByCode(code):
    query = Attend.select().where(Attend.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveAttend(attend):
    return Attend.insert(attend).execute()

def updateAttend(attend):
    return Attend.update(attend).where(Attend.code==attend['code']).execute()

def deleteAttend(code):
    return Attend.delete().where(Attend.code==code).execute()