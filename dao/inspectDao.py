from dao.ichess import Inspect

def getInspectList():
    result = []
    query = Inspect.select();
    for inspect in query:
        result.append(inspect)
    return result

def getInspectByCode(code):
    query = Inspect.select().where(Inspect.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveInspect(inspect):
    return Inspect.insert(inspect).execute()

def updateInspect(inspect):
    return Inspect.update(inspect).where(Inspect.code==inspect['code']).execute()

def deleteInspect(code):
    return Inspect.delete().where(Inspect.code==code).execute()