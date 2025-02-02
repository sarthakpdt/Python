dic={"ravi":15,"sarthak":1,"ronaldo":7,"messi":10}
a=list(dic.keys())
a.sort()
for i in a:
    res={i:dic[i]}
    print(res)
