
# implimentation of the NOn repeatable character in the string

def FirstNonRepeatable(s):

    for i in s:

        if (s.find(i, (s.find(i)+ 1))) == -1:
            print('first non character is ', i)

            break
    return

# main func

s = 'geeksforgeeks'

FirstNonRepeatable(s)

    

