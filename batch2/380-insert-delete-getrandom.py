class RandomizedSet:

    def __init__(self):
        self.val_to_list = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_list:
            return False
        self.values.append(val)
        self.val_to_list[val] = len(self.values)-1
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.val_to_list:
            return False
        replacement_element = self.values[-1]
        index = self.val_to_list[val]
        self.values[index] = replacement_element
        self.val_to_list[replacement_element] = index
        self.values.pop()
        del self.val_to_list[val]
        return True        

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
