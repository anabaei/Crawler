
# function minimumSwaps(arr) {
# let i = 0, count = 0;
# while (i < arr.length-1) {
# if (arr[i] === i + 1) {
# i++;
# }
# else {
# let temp = arr[i];
# arr[i] = arr[arr[i] - 1];
# arr[temp - 1] = temp;
# count++;
# }
# }
# return count;
# }



# arr = [5,1,3,2]

# nodes = {}
# for k in range(0,len(arr)):
#          nodes[k] = False


# print(nodes)
# def min(arr):
#     cnt = 0

#     brr = sorted(arr)
    
#     # find cycles
#     i = 0
#     v = {}
#     for k in range(0,len(arr)):
#         v['k'] = -1
     
   
#     for i,item in enumerate(arr):
#         res.append((i,item))
    
#     res = sorted(res.keys())
    
     
    
#     print(res)
  
    




#     print(brr)
#     return cnt


# print(min([5,1,3,2]))




def minSwaps(arr): 
   
    nodes ={}
    for k in range(0,len(arr)):
         nodes[k] = False

    Myarray = []
   
    for i,item in enumerate(arr):
        Myarray.append((i,item)) 
      

    Myarray.sort(key = lambda it:it[1]) 
    ans = 0
    for i in range(len(arr)): 
        if nodes[i]: 
            continue
        if Myarray[i][0] == i: 
            continue
        move = 0
        j = i 
        while not nodes[j]: 
        
            nodes[j] = True
        
            j = Myarray[j][0] 
       
            move += 1

        if move > 0: 
            ans += (move - 1) 

    return ans 
  
# Driver Code      
arr = [1, 5, 4, 3, 2] 
print(minSwaps(arr)) 
  

#print(getMinimumMoves([5,1,3,2]))


# cnt = 0
#     for i in (arr):
#         move = False
#         for j in range(arr.index(i), len(arr)):
#             #print(arr[j])
#             if(i>arr[j]):
#                 move = True
#                 temp = i
#                 arr[arr.index(i)] = arr[j]
#                 arr[j] = temp
#         if(move):
#             cnt= cnt+1
#     return cnt 