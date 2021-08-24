def ReturnAList(external_list):
    l = external_list.copy()
    if len(l) == 1:
        print(type(l))
        return(l)
    l.pop()
    ReturnAList(l)

def EvenSimpler(external_list):
    l = external_list.copy()
    if len(l) == 1:
        
        return(l)
    l.pop()
    EvenSimpler(l)


external_list = [1,3,4,5]
print(external_list)
# print(ReturnAList(external_list))
print(EvenSimpler(external_list))
print(external_list)