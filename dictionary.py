d={} #Empty dictionary
print(d)
d={'ham':2,"egg":3} #2 item dict
print(d)
d={"food":{"Chicken":2,"Mutton":1}} #nested dict
print(d)
d=dict(name='SK',age="21") 
print(d)
key=["ab","bc","cd"]
val=[1,2,3]
d=dict(zip(key,val))
print(d)
d2={'a':1}
d.update(d2)
print(d)
d.pop("a")
print(d) 
print(d.items())