import collections
def check(a1,a2):
    # CHECK WHETHER INPUT IS IN OBJECTS OR NOT
    d1=collections.Counter(a1)
    d2=collections.Counter(a2)
    for i in d1:
        if(i in d2):
            if(d1[i]<=d2[i]):
                continue
        else:
            return False
    return True



def findparent(n):
    for i in memb:
        if(n in memb[i]):
            return i        
        


def eval(rules,obj,membn):
    if(membstat[membn]==False):
        return -1
    c1=0
    n=len(rules)
    i=0
    while(i<n):
        #print(2,check(rules[i][0],obj),n,i,rules[i][0],obj,membn) --DEBUG
        if(check(rules[i][0],obj)):
            #IF THERE IS A MATCH THEN PRODUCE OUTPUT BY CONSUMING INPUT
            c1+=1
            p=rules[i][0]
            #CONSUME INPUT
            for j in p:
                obj.remove(j)
            #PRODUCE OUTPUT
            #print(obj) --debug
            # IF OUTPUT OF  ANY RULE IS INPUT TO OTHER MEMBRANE
            if('-' in rules[i][1]):
                kk=rules[i][1].split('-')
                #print(kk)  --debug
                num=int(kk[1])
                for j in kk[2]:
                    objects[num].append(j)

                
                i=0
                continue

            for j in rules[i][1]:
                # IF THE MEMBRANE DISSOVLES
                if(j=='0'):
                    membstat[membn]=False
                    par=findparent(membn)
                    #print(par,membn,memb)  --DEBUG
                    for ij in obj:
                        objects[par].append(ij)
                    break
                    
                else:
                    obj.append(j)
            
            if(membstat[membn]==False):
                break
            
            
                
            i=0
        else:
            i+=1
            
    if(c1==0):
        #IF NO MATCH OCCURS
        return -1
    else:
        return obj
        
                
        
        




n=int(input("NO OF MEMBRANES PRESENT\n"))
print("ENTER THE STRUCTURE OF MEMBRANE IN THE FORM OF \n* PARENT CHILD  *\nwhere outer membrane label is 1")
memb={}
membstat={}
for i in range(1,n+1):
    memb[i]=[]
    membstat[i]=True


# 0 for dissolve
# 1-a for input into ath membrane


#1 as OUTER MEMBRANE
for i in range(n-1):
    p,q=[int(x) for x in input().split()]
    memb[p].append(q)

objects={}
for i in range(1,n+1):
    objects[i]=-1
print("ENTER THE OBJECTS IN EACH MEMBRANE")
for i in range(1,n+1):
    print("OBJECTS IN MEMBRANE-REGION : "+str(i))
    objects[i]=input().split()


rules={}
for i in range(1,n+1):
    rules[i]=[]
print("ENTER THE RULES IN EACH MEMBRANE")
print("IN THE FORMAT  * INITIAL  FINAL *")
for i in range(1,n+1):
    print("NO OF RULES IN REGION "+str(i))
    k=int(input())
    print("RULES")
    for j in range(k):
        rules[i].append(input().split())
        

#print(memb)
#print(objects)
#print(rules)





while(1):
    
    curr=[]
    chk=0
    #EACH ITERATION CHECK IF ANY REACTION IS POSSIBLE OR NOT
    #IF POSSIBLE THEN PRODUCE RESULTS
    for i in range(1,n+1):
        #print("memb",i) --debug
        obj=eval(rules[i],objects[i],i)
        if(obj!=-1):
            objects[i]=obj
            chk=1
    if(chk==0):
        break
        #NO REACTION IS POSSIBLE FROM THIS STEP SO PROGRAM TERMINATES


        

print(objects)

#OUTPUT CODE AS NEEDED

if(len(objects[i])>1):
    print("YES")
else:
    print("NO")








"""
3
1 2
1 3

a a a c c d
a
2
a a
dcf 1-3-a
3
ac f
af c
d d0
0



"""









    


    
    

    




