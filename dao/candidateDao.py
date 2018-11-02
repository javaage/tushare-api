from dao.ichess import Candidate

def getLastCandidate():
    query = Candidate.select().order_by(Candidate.id.desc());
    if(query):
        return query.get()
    else:
        return

def getCandidateList():
    result = []
    query = Candidate.select();
    for candidate in query:
        result.append(candidate)
    return result

def getCandidateByCode(code):
    query = Candidate.select().where(Candidate.code==code)
    if(query):
        return query.get()
    else:
        return
    
def saveCandidate(candidate):
    return Candidate.insert(candidate).execute()

def updateCandidate(candidate):
    return Candidate.update(candidate).where(Candidate.code==candidate['code']).execute()

def deleteCandidate(code):
    return Candidate.delete().where(Candidate.code==code).execute()