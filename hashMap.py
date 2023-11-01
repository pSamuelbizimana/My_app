# hash table implementation 

# creating a class hashTable

class HashTable():

    def __init__(self,size):

        self.size = size     # initial size of DS
        self.table = [None]*size # initialization of the table

    def hashfunc(self,key):   # Function to calculate the index of the key in hash table
        return hash(key) % self.size
    
    def put(self,key,value):

        index = self.hashfunc(key)

        if self.table[index] is None: # check if there're no key-value pair in that index,initialize the list.
            self.table[index] = []
        for pair in self.table[index]: # iterate through the pair of index

            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key,value]) # otherwise append [key,value] pair

    def get(self,key):

        index = self.hashfunc(key)

        if self.table[index] is not None:

            for pair in self.table[index]:

                if pair[0] == key:
                    return pair[1]
        return None
    
    def remove(self,key):
        index = self.hashfunc(key)

        if self.table[index] is not None:
            for i, pair in enumerate(self.table[index]):

                if pair[0] == key:
                    del self.table[index][i]
                    return
                
# main part to excute our code

hashmap = HashTable(10) # initialize it with the size equals to ten

hashmap.put('cassava', 4)
hashmap.put('banana', 9)
hashmap.put('apple',3)

hashmap.get('apple')
hashmap.get("banana")
hashmap.get('cassava')

hashmap.remove('banana')

print(hashmap.get('banana'))
