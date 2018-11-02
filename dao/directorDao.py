from dao.ichess import Director

def getDirectorList():
    result = []
    query = Director.select();
    for director in query:
        result.append(director)
    return result

def getDirectorByCode(code):
    query = Director.select().where(Director.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveDirector(director):
    return Director.insert(director).execute()

def updateDirector(director):
    return Director.update(director).where(Director.code==director['code']).execute()

def deleteDirector(code):
    return Director.delete().where(Director.code==code).execute()