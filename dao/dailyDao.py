from dao.ichess import Daily

def getDailyList():
    result = []
    query = Daily.select();
    for daily in query:
        result.append(daily)
    return result

def getDailyByCode(code):
    query = Daily.select().where(Daily.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveDaily(daily):
    return Daily.insert(daily).execute()

def updateDaily(daily):
    return Daily.update(daily).where(Daily.code==daily['code']).execute()

def deleteDaily(code):
    return Daily.delete().where(Daily.code==code).execute()