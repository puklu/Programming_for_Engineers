# Author: Vivek Punia
# HW07-Tiled text file- solution for Programming for Engineers


import fileinput

def make_tile(n, block):
    
    # finding the width  of the tile
    widths = []
    for i in range(len(block)):
        widths.append(len(block[i]))
    width = max(widths)
    
    tile_no = n+1
    height = len(block)

    count = max(tile_no, width, height)
    
    # counting the number of "-" needed to be printed
    count_for_minuses = 0
    while count != 0:
        count = count//10
        count_for_minuses +=1

    ## counting how many white spaces are needed to print the text as right aligned based on the number of digits
    # counting the number of digits of the tile number
    count_for_tile = 0
    countT = tile_no
    while countT != 0:
        countT = countT//10
        count_for_tile +=1
    # print(count_for_tile)
    
    # counting the number of digits of the width number
    count_for_width = 0
    countW = width
    while countW != 0:
        countW = countW//10
        count_for_width +=1
    # print(count_for_width)

    # counting the number of digits of the height number
    count_for_height = 0
    countH = height
    while countH != 0:
        countH = countH//10
        count_for_height +=1  
    # print(count_for_height)

    # which of the above number has the most number of digits
    maxcounts = max(count_for_tile, count_for_width, count_for_height)
    
    # counting the number of white spaces by which the number needs to be shifted to the right to right-align perfectly
    count_for_tile = maxcounts - count_for_tile
    count_for_width = maxcounts - count_for_width
    count_for_height = maxcounts - count_for_height 

    # printing the tile info
    print("+" + "-"*(9+count_for_minuses+1) + "+")
    print("| "+ "Tile:   " + " "*count_for_tile + str(tile_no) + " |")
    print("| "+ "Width:  " + " "*count_for_width + str(width) + " |")
    print("| "+ "Height: " + " "*count_for_height + str(height) + " |")
    
    # figuring out if the tile info box is longer or the box with the contents
    length_for_tile_line = len(" "+ "Tile:   " + " "*count_for_tile + str(tile_no) + " ")
    length_for_width_line = len(" "+ "Width:  " + " "*count_for_width + str(width) + " ")
    length_for_height_line = len(" "+ "Height: " + " "*count_for_height + str(height) + " ")
    max_length_of_lines= max(length_for_tile_line,length_for_width_line,length_for_height_line)

    # printing the last line of the tile info box based on what is longer
    if width < max_length_of_lines:
        print("+"+ "-"*width + "+" + "-"*(10 + count_for_minuses - width - 1) + "+")
    elif width == max_length_of_lines:
        print("+"+ "-"*width + "+")
    else :
        print("+"+ "-"*max_length_of_lines + "+" + "-"*(width - max_length_of_lines - 1) + "+")    
    
    # finally printing the contents of the tile
    for word in block[::-1]:
        print("|"+ " "*(width - len(word)) +word+"|")

    # printing the last line of the tile
    print("+"+ "-"*width + "+")
    # print()

def solution(text):
    
    # print(text)

    # variable to arrange the words into blocks according to the conditions of the question
    blocks = [[] for i in range(len(text))]
    
    # appending the first word to start
    blocks[0].append(text[0])  

    i= 0
    j = 1
 
    while i < (len(text)) :  
        if j == (len(text)):  
            i = i+1         # to exit the while loop 
        else:    
            while j < (len(text)) :
                if len(text[j])<=len(blocks[i][len(blocks[i])-1]):
                    blocks[i].append(text[j])
                    j +=1
                    
                else:
                    blocks[i+1].append(text[j])
                    i = i+1
                    j = j+1
                    break    

    # removing the empty list for the list of lists        
    blocks = list(filter(None, blocks))

    # print(blocks)

    # make/printing the tiles 
    for i in range(len(blocks)):
        make_tile(i,blocks[i])
    


if __name__ == '__main__':

    # path of the text file
    # path = "/home/vivek/Documents/FEL/Second Semester/Programming for Engineers/Homeworks/hw07/datapub/"
    # fname = "pub01.in"  # file name

    # opening the file
    # file = open( path + fname, "r" )

    # array to contain the words of the text
    data = []

    for line in fileinput.input():
        data.append(line.rstrip().split())

    new_new_text = []

    for k in range(len(data)):
        for l in range(len(data[k])):
            new_new_text.append(data[k][l])

    # # removing all the empty elements from the list

    new_new_text = list(filter(None, new_new_text))

    # # calling the solution function
    solution(new_new_text)