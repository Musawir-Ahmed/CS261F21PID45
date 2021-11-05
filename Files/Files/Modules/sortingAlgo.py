import math

###Insertion Sort
##
#
def insertion_Sort(A,SortType,attribute):
    for i in range(len(A)):
        key = A[i]
        j = i-1
        while j>-1 and getattr(A[j],attribute)>=getattr(key,attribute):
            A[j+1]=A[j]
            j-=1
        A[j+1] = key
    if SortType == "Ascending":
        return A
    
    return list(reversed(A))

###Merge Sort
##
#
def merge_Sort(A,left,right,SortType,attribute):
    if right > left:
        mid = (left + right)//2
        
        merge_Sort(A,left,mid,SortType,attribute)
        merge_Sort(A,mid+1,right,SortType,attribute)
        
        Merge(A,left,mid,right,attribute)

    return A
    
def Merge(A,p,q,r,attribute):
    n1 = q-p+1
    n2 = r-q
    L = []
    R = []
    for i in range(n1):
        L.append(A[p+i])
    for j in range(n2):
        R.append(A[q+1+j])
    
    i = 0 
    j = 0
    k = p
    while i<n1 and j<n2:
        if getattr(L[i],attribute)<=getattr(R[j],attribute):
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
        k+=1
    if i==len(L):
        while j < n2:
            A[k] = R[j]
            j+=1
            k+=1
    else:
        while i < len(L):
            A[k] = L[i]
            i+=1
            k+=1

def MergeSort_Controller(A,left,right,SortType,attribute):
    A=merge_Sort(A,left,right,SortType,attribute)
    if SortType=="Ascending":   
        return A
    return list(reversed(A))

###Quick Sort
##
#
def quick_Sort(arr,low,high,attribute):
    if low<high:
        pivot = partition(arr,low,high,attribute)
        quick_Sort(arr,low,pivot-1,attribute)
        quick_Sort(arr,pivot+1,high,attribute)
    return arr

def partition(arr,low,high,attribute):
    pivot = getattr(arr[high],attribute)
    i = low - 1
    
    for j in range(low,high):
        if  getattr(arr[j],attribute)<pivot:
            i+=1
            arr[i],arr[j] = arr[j], arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    
    return i+1

def quick_sort_controller(arr,low,high,SortType,attribute):
    arr=quick_Sort(arr,low,high,attribute)
    if SortType == "Ascending":
        return arr
    return list(reversed(arr))

###Strand Sort
##
#
def merge_strand(newarr,outarr,SortType,attribute):
    returnarr = []
    while len(newarr)>0 and len(outarr)>0:
        if getattr(newarr[0],attribute)>=getattr(outarr[0],attribute):
            returnarr.append(outarr[0])
            outarr.pop(0)
        else:
            returnarr.append(newarr[0])
            newarr.pop(0)         
    returnarr += newarr
    returnarr += outarr


    return returnarr


def strand_Sort(inArr,SortType,attribute):
    outputarr = []
    print(len(inArr))
    while len(inArr)!=0:
        newarr = []
        main_count = 0
        newarr.append(inArr[0])
        prev_element =newarr[0] 
        inArr.pop(0)
        while main_count!=len(inArr):
            if getattr(inArr[main_count],attribute)>getattr(prev_element,attribute):
                prev_element = inArr[main_count]
                newarr.append(prev_element)
                inArr.pop(main_count)
                main_count-=1
            main_count+=1
        outputarr = merge_strand(newarr,outputarr,SortType,attribute)
    if(SortType=="Ascending"):
        return outputarr
    return list(reversed(outputarr))



###Radix Sort
##
#
def radixcounting_sort(passed_array,divident):
    orignal_array=passed_array.copy() 
    for x in range(0,len(passed_array)):
        condition=False
        if(passed_array[x]<0):
            condition=True
            passed_array[x]=passed_array[x]*-1
        passed_array[x]=passed_array[x]/divident
        passed_array[x]=int(passed_array[x]%10)
        if(condition==True):
            passed_array[x]=passed_array[x]*-1

    min_vallue=min(passed_array)
    if(min_vallue<0):
        for x in range(0,len(passed_array)):
            passed_array[x]=passed_array[x]-(min_vallue)
    max_value=max(passed_array)+1
    counting_array=[]
    resultant_array=[]
    for x in range (0,max_value):
        counting_array.append(0)

    for x in range(0,len(passed_array)):
        resultant_array.append(0)
    

    for x in range(0,len(passed_array)):
        index=passed_array[x]
        counting_array[index]=counting_array[index]+1


    for x in range(0,len(counting_array)-1):
        counting_array[x+1]=counting_array[x+1]+counting_array[x]
        
    for x in range(len(passed_array)-1,-1,-1):
        index=passed_array[x]
        sorted_index=counting_array[index]
        counting_array[index]=counting_array[index]-1
        resultant_array[x]=sorted_index-1

    for x in range(0,len(resultant_array)):
        index=resultant_array[x]
        passed_array[index]=orignal_array[x]

    return passed_array


def redix_sort(passed_array,SortType):
    max_value=max(passed_array)
    divident=1
    while int(max_value/divident) >0:
        passed_array=radixcounting_sort(passed_array,divident)
        divident=divident*10
    if SortType=="Ascending":
        return passed_array
    return list(reversed(passed_array))


###Pigeonhole Sort
##
#
def pigeonhole_Sort(A,SortType,attribute):
    if str(A[0]).isdigit():
        maxelement = max(A)
        minelement = min(A)
        arr_range = maxelement-minelement+1
        pigeonhole = []
        for k in range(arr_range):
            pigeonhole.append([]*arr_range)

        for i in range(len(A)):
            
            piglist = pigeonhole[A[i]-minelement]
            piglist.append(A[i])
            pigeonhole[A[i]-minelement] = piglist

        arraycount = 0 
        for j in range(len(pigeonhole)):
            for c in range(len(pigeonhole[j])):
                piglist = pigeonhole[j]
                if piglist:
                    A[arraycount] = piglist[c]
                    arraycount+=1
    else:
        temp=[]
        for x in range(0,len(A)):
            object_attribute=getattr(A[x],attribute)
            temp.append(object_attribute)
        
        maxelement = max(temp)
        minelement = min(temp)
        arr_range = ord(maxelement[0])-ord(minelement[0])+1
        pigeonhole = []
        for k in range(arr_range):
            pigeonhole.append([]*arr_range)

        for i in range(len(A)):
            key = getattr(A[i],attribute)
            piglist = pigeonhole[ord(key[0])-ord(minelement[0])]
            piglist.append(A[i])
            pigeonhole[ord(key[0])-ord(minelement[0])] = piglist

        arraycount = 0 
        for j in range(len(pigeonhole)):
            for c in range(len(pigeonhole[j])):
                piglist = pigeonhole[j]
                if piglist:
                    A[arraycount] = piglist[c]
                    arraycount+=1
    if(SortType=="Ascending"):
        return A
    
    return list(reversed(A))


###Cocktail Sort
##
#
def cocktail_Sort(A,SortType,attribute):
    low = 0
    high = len(A)-1
    while low<high:
        for k in range(low,high):
            if getattr(A[k],attribute)>getattr(A[k+1],attribute):
                A[k],A[k+1] = A[k+1],A[k]
        for i in range(high,low,-1):
            if getattr(A[i],attribute)<getattr(A[i-1],attribute):
                A[i],A[i-1] = A[i-1],A[i]
        low+=1
        high-=1 
    if SortType == "Ascending":
        return A
    return list(reversed(A))


#####
#         
#Selection sort
def selection_sort(Array,sorttype,attribute):

    expression=None
    
    if(sorttype=="Ascending"):
        expression="getattr(Array[index],attribute)>getattr(Array[y],attribute)"
    else:
        expression="getattr(Array[index],attribute)<getattr(Array[y],attribute)"

    for x in range(0,len(Array)):
        index=x
        for y in range(x+1,len(Array)):
            if(eval(expression)):
                index=y 
        temp=Array[index]
        Array[index]=Array[x]
        Array[x]=temp
    return Array   


#####
#
#buuble sort algorithm
def Buble_sort(Array,sorttype,attribute):
    for x  in range(0,len(Array)):
        expression=None
    if(sorttype=="Ascending"):
        expression="getattr(Array[y],attribute)>getattr(Array[x],attribute)"
    else:
        expression="getattr(Array[y],attribute)<getattr(Array[x],attribute)"

    for x in range(0,len(Array)):
        for y in range(0,len(Array)):
            if(eval(expression)):

                temp=Array[y]
                Array[y]=Array[x]
                Array[x]=temp
    
    return Array

def check(value):
    try:
        return int(value)
    except ValueError:
         return value

#####
#
#Counting Sort
def counting_sort(passed_array,sorttype,attribute,sortingOf):
    orignal_Array=[]
    sorted_index_list=[]
    temp=[]
    for x in range(0,len(passed_array)):
        orignal_Array.append(passed_array[x])
        sorted_index_list.append(0)
        temp.append(0)

    for x in range(0,len(passed_array)):
        object_attribute=getattr(passed_array[x],attribute)
        temp[x]=object_attribute
        if(sortingOf==str):
            Temp=temp[x]
            temp[x]=ord(Temp[0])

    max_value=max(temp)+1
    counting_array=[0]*max_value
    resultant_array=[0]*len(temp)

    for x in range(0,len(temp)):
        index=temp[x]
        counting_array[index]=counting_array[index]+1


    for x in range(0,len(counting_array)-1):
        counting_array[x+1]=counting_array[x+1]+counting_array[x]
    
    count=len(passed_array)-1

    for x in range(len(passed_array)-1,-1,-1):
        index=temp[x]
        sorted_index=counting_array[index]
        counting_array[index]=counting_array[index]-1
        resultant_array[sorted_index-1]=index
        sorted_index_list[count]=sorted_index-1
        count=count-1

    
    for x in range(0,len(sorted_index_list)):
        index=sorted_index_list[x]
        resultant_array[index]=orignal_Array[x]

    if(sorttype!="Ascending"):
        resultant_array.reverse()


    return resultant_array


#####
##
#Shell Sort
def shellsort(Array,sorttype,attribute):
    expression1=None
    expression2=None
    if(sorttype=="Ascending"):
        expression1="getattr(Array[index+gap],attribute)<getattr(Array[index],attribute)"
        expression2="getattr(Array[prevous_indexes - gap],attribute) > getattr(Array[prevous_indexes],attribute)"
    else:
        expression1="getattr(Array[index+gap],attribute)>getattr(Array[index],attribute)"
        expression2="getattr(Array[prevous_indexes - gap],attribute) < getattr(Array[prevous_indexes],attribute)"

    gap=int(len(Array)/2)
    while gap>0:
        index=0
        while (gap+index) < len(Array):
            if(eval(expression1)):
                Array[index],Array[index+gap]=Array[index+gap],Array[index]
			
            prevous_indexes=index
            
            while prevous_indexes - gap >= 0:
                
                if eval(expression2):
                    Array[prevous_indexes-gap],Array[prevous_indexes] = Array[prevous_indexes],Array[prevous_indexes-gap]
				
                prevous_indexes =prevous_indexes-1
            index=index+1
        gap=int(gap/2)

    return Array


#####
#
#Comb Sort
def Combsort(Array,sorttype,attribute):
    expression=None
    if(sorttype!="Ascending"):
        expression="getattr(Array[index],attribute)<getattr(Array[gap+index],attribute)"
    else:
        expression="getattr(Array[index],attribute)>getattr(Array[gap+index],attribute)"


    gap=int(len(Array))
    while gap>0:
        index=0
        while (gap+index)<len(Array):
            if eval(expression) :
                Array[index],Array[index+gap]=Array[index+gap],Array[index]
            index=index+1
        gap=int(gap/1.3)

    return Array



######
###
#CycleSort
def cyclesort(Array,sorttype,attribute):
    expression=None
    
    constant_expression1="getattr(value,attribute)==getattr(Array[current_index],attribute)"
    constant_expression2="getattr(value,attribute)==getattr(Array[current_index],attribute)"
    
    if(sorttype=="Ascending"):
        expression="getattr(Array[x],attribute)<getattr(value,attribute)"
    else:
        expression="getattr(Array[x],attribute)>getattr(value,attribute)"
    for index in range(0,len(Array)):
        value=Array[index]
        current_index=index
        for x in range(index+1,len(Array)):
            if(eval(expression)):
                current_index=current_index+1
        
        if(current_index!=index):
            while eval(constant_expression1):
                current_index=current_index+1

            Array[current_index],value=value,Array[current_index]

            while current_index!=index:
                current_index=index
                for x in range(index+1,len(Array)):
                    if(eval(expression)):
                        current_index= current_index+1
                while eval(constant_expression2):
                    current_index=current_index+1
                Array[current_index],value=value,Array[current_index]
    return Array
