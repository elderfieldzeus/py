valid_formats = ['d', 'f', 'c', 's']
valid_escapes = ['n','b', 't', '\\', '\"']

string = input("Enter string: ")

def is_valid(string, valid_formats):
    
    while '%' in string:
        ndx = string.index('%')
        
        if ndx + 1 >= len(string) or string[ndx + 1] not in valid_formats:
            return "INVALID"
            
        valid_ndx = valid_formats.index(string[ndx + 1])
        valid_formats = valid_formats[valid_ndx:]
        string = string[:ndx] + string[ndx + 1:]
        
    while '\\' in string:
        ndx = string.index('\\')
        
        if ndx + 1 >= len(string) or string[ndx + 1] not in valid_escapes:
            return "INVALID"
            
        string = string[:ndx] + string[ndx + 1:]
        
    return "VALID"
    
print("Result:", is_valid(string, valid_formats))