s1=input("Enter first file name: ")
s2=input("Enter second file name: ")

class plagarism(object):
    def file_open(self,name):
        o=open(name)
        r=o.read()
        r=r.lower()
        list1=[]
        list1=r.split()
        return list1
    def dic(self,list1):
        dic={}
        for i in list1:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        return dic

    
    def uniqkeys(self,ck):
        uniqkeys=[]
        for i in ck:
            if i not in uniqkeys:
                uniqkeys.append(i)
        return uniqkeys


    def dotproduct(self,uniqkeys,d1,d2):
        num=0
        for i in uniqkeys:
            p=d1.get(i,0)*d2.get(i,0)
            num+=p

    
        sum1=0
        sum2=0

        for i in uniqkeys:
            sum1+=(d1.get(i,0))**2
            sum2+=(d2.get(i,0))**2
        den=(sum1*sum2)**0.5
        dotproduct=num/den
        return dotproduct
p1=plagarism()
d1=(p1.dic(p1.file_open(s1)))
d2=(p1.dic(p1.file_open(s2)))

keys1=list(d1.keys())
keys2=list(d2.keys())
ckeys=keys1+keys2
ck=p1.uniqkeys(ckeys)
v=p1.dotproduct(ck,d1,d2)

percentage=v*100
print(percentage)
