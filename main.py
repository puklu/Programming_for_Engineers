

def solution(text):
    
    print(text)

    blocks = [[] for i in range(len(text))]
    
    blocks[0].append(text[0])  

    i= 0
    j = 1
 
    while i < (len(text))-1 :  
        if j == (len(text))-1:
            i = i+1
        else:    
            while j < (len(text))-1 :
                if len(text[j])<=len(blocks[i][len(blocks[i])-1]):
                    blocks[i].append(text[j])
                    j +=1
                    
                else:
                    blocks[i+1].append(text[j])
                    i = i+1
                    j = j+1
                    break    
            
    blocks = list(filter(None, blocks))
    print(blocks)


if __name__ == '__main__':

    # path
    path = "/home/vivek/Downloads/datapub/"
    fname = "pub01.in"

    file = open( path + fname, "r" )

    data = []
    while True:
        line = file.read()
        data.append(line)
        # print( line )  # echo file header
        if line == "": break
    
    new_text = []
    new_new_text = []
    new_new_new_text = []

    for i in range(len(data)):
        new_text.append(data[i].split(" "))
    
    for j in range(len(new_text[0])):
        new_new_text.append(new_text[0][j].split("\n"))

    for k in range(len(new_new_text)):
        for l in range(len(new_new_text[k])):
            new_new_new_text.append(new_new_text[k][l])


    # print(new_text)
    # print(new_new_text)
    # print(new_new_new_text)

    solution(new_new_new_text)