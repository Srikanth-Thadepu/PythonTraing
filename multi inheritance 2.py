class Father:
    def dad(self):
        return "Love u dad"
class Mother:
    def beta(self):
        return "Love u kanayya"

class Son(Father,Mother):
    def ha_maa(self):
        return "Love u too"

son=Son()
print(son.dad())
print(son.beta())
i=Mother()
i=son
print(i.ha_maa())