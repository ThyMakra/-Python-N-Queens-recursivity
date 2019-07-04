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
# a function for printing every possible boards                
def print_board(N, tup):    
    for lis in tup:        
        for t in lis:            
            zero_list = ['0']*N
            zero_list[t[1]] = '1'
            print('  '.join(zero_list))
        print('-'*(3*N-2))
    print('='*40)
    print(f"The number of possibilities of {N} Queens in {N}X{N} board is : {len(tup)}")
    print('='*40)
def queen_bonus(N):
    if type(N) == int:
        if N > 0 and N <= 12:            
            list_a = [i for i in range(N)]
            list_b = [i for i in range(N)]
            allpos=[]
            tup_lis = []
            recurs(list_a, list_b, tup_lis, allpos)
            print_board(N, allpos)
            return len(allpos)
        else : 
            print("The parameter value must be from 1 to 12")
            return ''
    else: 
        print("The parameter must be an integer from 1 to 12")
# print(queen_bonus(6))
