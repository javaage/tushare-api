from dao.ichess import *

def getLastCandidate():
    query = Candidate.select().order_by(Candidate.id.desc());
    if(query):
        return query.get()
    else:
        return