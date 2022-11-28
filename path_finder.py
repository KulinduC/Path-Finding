#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:55:29 2021

@author: kulinducooray
"""


import util 


def get_nbrs(r,col,row,colum): #appends touples that are verified neighbors of a given touple with the grid's row and column that the input touple is from
    num = 0
    list1 = [] #creates an empty list to store neighbors
    if (r > 0 and r <= row-1): 
        num = r - 1
        list1.append((num,col))
    if (col > 0 and col <= colum-1):
        num = col - 1
        list1.append((r,num))
    if (r >= 0 and r < row-1):
        num = r + 1
        list1.append((num,col))
    if (col >= 0 and col < colum-1):
        num = col + 1
        list1.append((r,num))
    new_list1 = sorted(list1) #sorts the list to have the touples from least to greatest 
    return new_list1

def path():
    place = False
    list2 = util.get_path(n) #gets the list of all the path tuples
    list4 = []
    down = 0
    up = 0
    for i in range(len(list2)-1): # goes through the list of path tuples minus one because the index next to i will be compared with it
        list3 = get_nbrs(list2[i][0],list2[i][1],row,colum) #creates a list of neighbors for each iteration of i
        for j in list3: #goes through list3 to find if j as a neighbor equals an i+1 tuple to see if that touple is in fact a neighbor of i 
            if list2[i+1] == j:
                place = True
                break #if it finds that it is a neighbor it breaks the for loop and goes on to do the other touples in list2
            else:
                place = False #if place is false then the numbers that made place false are stored in bad_num and bad_num2
        if (place == False):
            bad_num = list2[i]
            bad_num2 = list2[i+1]
            break #it breaks out of the main for loop to print out that there is an invalid path
    if (place):
        print("Valid path") 
        list5 = util.get_grid(n)
        for a in list2: #goes through the path tuples and compares it with the tuple indexes of the grid to find a match and if it is a match then that grid value is appeneded to a list
            for i in range(len(list5)):
                for j in range(len(list5[i])):
                    if (i,j)  == a:
                        list4.append(list5[i][j])
        for i in range(len(list4)-1): #goes through the list of grid values and sees if it is increasing or decreasing and records by the change 
            if (list4[i] > list4[i+1]):
                down += (list4[i] - list4[i+1])
            elif (list4[i] < list4[i+1]):
                up += (list4[i+1] - list4[i])
        print("Downward {}".format(down))
        print("Upward {}".format(up))
        
    else:
        print("Path: invalid step from {} to {}".format(bad_num,bad_num2))
        
def steep(start1,start2, max_num):
    final_list = [(start1,start2)] #creates a list to eventually store all the correct neighbors for this path
    grid_lst = util.get_grid(n)   
    place2 = False
    while not place2:
        steep_list = get_nbrs(start1, start2, row, colum)
        gmax_con = False
        local = False
        no_max = False
        num_list = []
        good_vals = []
        for a in range(len(grid_lst)): #goes through the grid list to find the numerical value of the touple (start1,start2)
            for b in range(len(grid_lst[a])):
                if (a,b)  == (start1,start2):
                    temp_num = grid_lst[a][b]
                    
        for z in steep_list: #appends the numerical value and its coordinate (tuple) as a list in the list num_list
            for i in range(len(grid_lst)):
                for j in range(len(grid_lst[i])):
                    if (i,j)  == z:
                        num_list.append([grid_lst[i][j],(i,j)])
                        
        for y in num_list: #goes through num_list to find the elements that satisfy the correct conditions and appends them to a new list 
            if (temp_num < y[0] and y[0] - temp_num <= max_num):
                good_vals.append(y)
        
        if (len(good_vals) > 0): #if the length good_vals is greater than 0 it stores the max element of the list 
            max_lst = max(good_vals)
        else:
            max_lst = good_vals #if there is only one element, it just assigns that element to max_lst
        
        if (len(max_lst) != 0): # if the length max_lst isnt 0 then it sees if the numerical value is equal to the global max 
            if (max_lst[0] == gmax):
                gmax_con = True
            else: #it also adds all the neighbors of the starting touple and adds those to a list called temp_list
                other_neighbors = get_nbrs(max_lst[1][0], max_lst[1][1], row, colum)
                temp_list = []
                for c in other_neighbors:
                    for d in range(len(grid_lst)):
                        for e in range(len(grid_lst[d])):
                            if c == (d,e):
                                temp_list.append(grid_lst[d][e])
           
                for h in temp_list: #goes through the list and sees if numerical value of max_lst is a local maximum 
                    if (max_lst[0] < h):
                        local = False #if it is false for even one its neighbor the for loop breaks and local = False 
                        break
                    elif (max_lst[0] > h):
                        local = True
                    
    
                for f in temp_list: #goes through the list and sees if the numerical value of max_lst is smaller than all of its neighbors and can't go to them because of the maximum height limit
                    if (f - max_lst[0] <= max_num):
                        no_max = False #if it finds a difference that is equal to or less than max_num it breaks the for loop meaning it wasn't a no maximum 
                        break
                    else:
                        no_max = True
            start1 = max_lst[1][0] #updates the start1 and start2 values in the max_lst to go through the while again with these new values 
            start2 = max_lst[1][1]
            final_list.append((start1,start2)) #appends the correct path touple to the final_list list 
        else:
            no_max = True
                
        
        
        if (gmax_con): # if gmax_con or local or no_max is true then the loop ends since place2 becomes True
            place2 = True
        elif (local):
            place2 = True
        elif (no_max):
            place2 = True            
    result = '' # creates the result string and adds each value in final_list and creates a new line after every 5 elements 
    for k in range(len(final_list)): 
        if (k % 5 == 0 and k != 0):
            result += "\n"+str(final_list[k]) + " "
        else:
            result += str(final_list[k]) + " "
    print(result)
    
   
   
    if (gmax_con): #prints the correct description at the end of the path based on gmax_con, local or no_max
        print("global maximum")
    elif (local):
        print("local maximum")
    elif (no_max):
        print("no maximum")
        
    
    

def grad(start1,start2, max_num): #does the same function as def steep only difference is it takes the minimum numerical value to go through the path
    final_list = [(start1,start2)]
    grid_lst = util.get_grid(n)   
    place2 = False
    while not place2:
        steep_list = get_nbrs(start1, start2, row, colum)
        gmax_con = False
        local = False
        no_max = False
        num_list = []
        good_vals = []
        for a in range(len(grid_lst)):
            for b in range(len(grid_lst[a])):
                if (a,b)  == (start1,start2):
                    temp_num = grid_lst[a][b]
                    
        for z in steep_list:
            for i in range(len(grid_lst)):
                for j in range(len(grid_lst[i])):
                    if (i,j)  == z:
                        num_list.append([grid_lst[i][j],(i,j)])
                        
        for y in num_list:
            if (temp_num < y[0] and y[0] - temp_num <= max_num):
                good_vals.append(y)
        
        if (len(good_vals) > 0):
            min_lst = min(good_vals) #this is the only difference from def steep since this function wants to go through the path at a gradual pace 
        else:
            min_lst = good_vals
        
        if (len(min_lst) != 0):
            if (min_lst[0] == gmax):
                gmax_con = True
            else:
                other_neighbors = get_nbrs(min_lst[1][0], min_lst[1][1], row, colum)
                temp_list = []
                for c in other_neighbors:
                    for d in range(len(grid_lst)):
                        for e in range(len(grid_lst[d])):
                            if c == (d,e):
                                temp_list.append(grid_lst[d][e])
           
                for h in temp_list:
                    if (min_lst[0] < h):
                        local = False
                        break
                    elif (min_lst[0] > h):
                        local = True
                    
    
                for f in temp_list:
                    if (f - min_lst[0] <= max_num):
                        no_max = False
                        break
                    else:
                        no_max = True
            start1 = min_lst[1][0]
            start2 = min_lst[1][1]
            final_list.append((start1,start2))
        else:
            no_max = True
                
        
        
        if (gmax_con):
            place2 = True
        elif (local):
            place2 = True
        elif (no_max):
            place2 = True            
                    
    result = ''
    for k in range(len(final_list)):
        if (k % 5 == 0 and k != 0):
            result += "\n"+str(final_list[k]) + " "
        else:
            result += str(final_list[k]) + " "
    print(result)
   
    if (gmax_con):
        print("global maximum")
    elif (local):
        print("local maximum")
    elif (no_max):
        print("no maximum")


if __name__ == "__main__":
    placeholder = True
    while placeholder: #asks the user for a valid input of n and if it is 0 it breaks the while loop
        n = int(input("Enter a grid index less than or equal to 3 (0 to end): "))
        print(n)
        if (n < 0 or n > 3):
            placeholder = True
        elif (n > 0 and n <= 3):
            placeholder = False
        elif (n == 0):
            break
    max_num = int(input("Enter the maximum step height: ")) 
    print(max_num)
    user = input("Should the path grid be printed (Y or N): ")
    print(user.strip())
    
   
        
    row = len(util.get_grid(n)) #gets the row of the grid 
    colum = len(util.get_grid(n)[0]) #gets the column of the grid 

    print("Grid has {} rows and {} columns".format(row,colum))
    
    grid_list = util.get_grid(n)
    tempList = []
    for i in range(len(grid_list)): #goes through the grid and appends its numerical value and touple to tempList
        for j in range(len(grid_list[i])):
            tempList.append([grid_list[i][j],(i,j)])
    max_list = max(tempList) #finds the max value of tempList and gets its numerical value 
    gmax = max_list[0]
    print("global max: {} {}".format(max_list[1],gmax))
            
    start_loc = util.get_start_locations(n)
    print("===")
    for i in start_loc: #goes through all the starting locations and runs the steep and grad functions twice for each one 
        for j in range(2):
            if j == 0:
                print("steepest path")
                steep(i[0],i[1],max_num)
                print("...")
            elif(j == 1):
                print("most gradual path")
                grad(i[0],i[1],max_num)
        print("===")
           
            
        
            
            
            
            
            
