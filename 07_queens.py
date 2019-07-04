def isnot_diagonal (tupxaxb, lis_tupab):        
    xa,xb = tupxaxb
    for a,b in lis_tupab:
        if a + b == xa + xb or a - b == xa - xb :
            return False 
    return True
def recurs(lis_a,lis_b, tup_lis, allpos):
    xa = lis_a[len(tup_lis)]    
    for xb in lis_b:                
        if isnot_diagonal((xa,xb),tup_lis):
            temptup_lis = list(tup_lis)
            temptup_lis.append((xa,xb))            
            temp_lisb = list(lis_b)
            temp_lisb.remove(xb)
            if len(temptup_lis) == len(lis_a) :
                allpos.append(temptup_lis)
            else :
                recurs(lis_a,temp_lisb,temptup_lis,allpos)
def queens():
    list_a = [i for i in range(8)]
    list_b = [i for i in range(8)]
    allpos=[]
    tup_lis = []
    recurs(list_a, list_b, tup_lis, allpos)
    return len(allpos)