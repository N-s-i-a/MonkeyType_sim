q=0
words=0
baselist=[
    "Lorem", "ipsum", "dolor", "sit", "amet,", "consectetur", "adipisicing", 
    "elit.", "Maiores", "ut", "eum", "natus,", "eaque", "ad,", "repellendus", 
    "maxime", "quis", "dolore", "delectus", "facere,", "quibusdam", "animi", 
    "iure.", "Impedit,", "accusantium", "deserunt.", "Earum", "excepturi", 
    "odio", "aliquid", "sint", "ducimus", "eos", "quo,", "inventore", 
    "nostrum,", "in", "nulla", "quaerat", "officia", "natus", "expedita", 
    "recusandae", "ut", "laudantium,", "aspernatur", "sit", "quas", "iste!", 
    "Nulla?"
]

def recheck(temporary):
    p=0
    templist=[]
    global words
    for i in range(p,len(temporary)):
        if temporary[i]==" ":
            templist.append(temporary[p:i])
            p=i+1

    words=len(temporary)/5
    def accurate():
        global q
        acc=0
        x=0
        while x<len(baselist):
            if x>len(templist)-1:
                break
            elif templist[x]==baselist[x]:
                acc+=1  
            x+=1
        q=acc*2
    accurate()




