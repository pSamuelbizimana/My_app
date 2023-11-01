"""Given two arrays key[] and arr[] of size N and a key s. 
Each key[i] 
and arr[i] form a key-value pair. 
Find if the value of S in the N key-value pairs. """


def find_value(key,arr,s):

    for i in range(len(key)):
        if key[i] == s:
            return arr[i]
    return None


# code excution
key = [1,2,3,4,5,6]
arr = ['a','b','c','d','e']

s = 5

result = find_value(key, arr,s)

if result is not None:

    print(f"The corresponding value of {s} is {result}")

else:
    print(f'value {s} is not found')

