import string 
class LEXER(): 
    def __init__(self,filename="input.txt"): 
        code = open(filename, "r").read() 
        tokens_array = self.split(' '.join(code.split())) 
        self.show(self.count(tokens_array)) 

    def split(self,in_string): 
        array,t = [],'' 
        for char in in_string: 
            if char not in string.ascii_letters+string.digits: 
                if t !='':array.append((t,self.get_type(t))) 
                if char!=' ':array.append((char,self.get_type(char))) 
                t = ''
            else:
                t+=char
        if t!='': 
            array.append((t,self.get_type(t))) 
        return array

    def get_type(self,in_string): 
        if in_string == 'int' or in_string == 'char' or in_string == 'for' or in_string == 'while': return 'keyword' 
        elif in_string == '>' or in_string == '>=' or in_string == '<' or in_string == '<=' or in_string == '==' or in_string == '!=': return 'reln' 
        elif in_string == '+' or in_string == '-' or in_string == '*' or in_string == '/' or in_string == '%': return 'arith' 
        elif in_string == '=' : return 'assign' 
        elif in_string[0] in string.ascii_letters:return 'id' 
        elif in_string[0] in string.digits:return 'num' 
        else: return 'punc'
    
    def count(self,array_in): 
        count_dict = {} 
        for a in array_in: 
            if a[0] in count_dict: 
                count_dict[a[0]][0]+=1 
            else: 
                count_dict[a[0]]=[1,a[1]] 
        return count_dict

    def show(self,count): 
        print("{0:7s} | {1:6s} | {2:10s}|".format("type","count","word")) 
        print("-"*8+"+"+"-"*8+"+"+"-"*11+"|") 
        for key, value in count.items(): 
            print("{0:7s} | {1:6d} | {2:10s}|".format(value[1],value[0],key))
        keyword = 0
        reln = 0
        arith = 0
        assign = 0
        ident = 0
        num = 0
        punc = 0
        for key, value in count.items():
            if key == 'int' or key == 'char' or key == 'for' or key == 'while':
                keyword +=  value[0] 
            elif key == '>' or key == '>=' or key == '<' or key == '<=' or key == '==' or key == '!=':
                reln += value[0] 
            elif key == '+' or key == '-' or key == '*' or key == '/' or key == '%':
                arith += value[0] 
            elif key == '=' :
                assign += value[0] 
            elif value[1] == 'id':
                ident += value[0]
            elif value[1] == 'num':
                num += value[0]
            else:
                punc += value[0]
        dic = {"Keywords":keyword,"Relations":reln,"Arithmetics":arith,"Assignments":assign,"Ids":ident,"Numbers":num,"Punctuators":punc}
        print("{0:20s} | {1:6s} |".format("type","total")) 
        print("-"*21+"|"+"-"*8+"|") 
        for key, value in dic.items(): 
            print("{0:20s} | {1:6d} |".format(key,value))

if __name__ == '__main__': 
    LEXER()
