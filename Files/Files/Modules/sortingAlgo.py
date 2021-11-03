import math
###Insertion Sort
##
#
def insertion_Sort(A,SortType):
    for i in range(len(A)):
        key = A[i]
        j = i-1
        while j>-1 and A[j]>=key:
            A[j+1]=A[j]
            j-=1
        A[j+1] = key
    if SortType == "Ascending":
        return A
    return list(reversed(A))


###Merge Sort
##
#
def merge_Sort(A,left,right,SortType):
    if right > left:
        mid = (left + right)//2
        
        merge_Sort(A,left,mid,SortType)
        merge_Sort(A,mid+1,right,SortType)
        
        Merge(A,left,mid,right)
    if SortType=="Ascending":   
        return A
    return list(reversed(A))
    
def Merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = []
    R = []
    for i in range(n1):
        L.append(A[p+i])
    for j in range(n2):
        R.append(A[q+1+j])
    L.append(math.inf)
    R.append(math.inf)
    
    i = 0 
    j = 0

    for k in range(p,r+1):
        if L[i]<=R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1

###Quick Sort
##
#
def quick_Sort(arr,low,high,SortType):
    if low<high:
        pivot = partition(arr,low,high)
        quick_Sort(arr,low,pivot-1,SortType)
        quick_Sort(arr,pivot+1,high,SortType)
    if SortType == "Ascending":
        return arr
    return list(reversed(arr))

def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low,high):
        if  arr[j]<pivot:
            i+=1
            arr[i],arr[j] = arr[j], arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    
    return i+1
###Strand Sort
##
#
def merge_strand(newarr,outarr,SortType):
    returnarr = []
    while len(newarr)>0 and len(outarr)>0:
        if SortType == "Ascending":
            if newarr[0]>=outarr[0]:
                returnarr.append(outarr[0])
                outarr.pop(0)
            else:
                returnarr.append(newarr[0])
                newarr.pop(0) 
        else:
            if newarr[0]<=outarr[0]:
                returnarr.append(outarr[0])
                outarr.pop(0)
            else:
                returnarr.append(newarr[0])
                newarr.pop(0) 
        
    returnarr += newarr
    returnarr += outarr
    return returnarr


def strand_Sort(inArr,SortType):
    outputarr = []
    while len(inArr)!=0:
        newarr = []
        main_count = 0
        newarr.append(inArr[0])
        prev_element = newarr[0]
        inArr.pop(0)
        if SortType == "Ascending":
            while main_count!=len(inArr):
                if inArr[main_count]>prev_element:
                    prev_element = inArr[main_count]
                    newarr.append(prev_element)
                    inArr.pop(main_count)
                    main_count-=1
                main_count+=1
        else:
            while main_count!=len(inArr):
                print(inArr[main_count],prev_element,"\t",len(inArr),main_count)
                print(newarr,outputarr,inArr)
                print("")
                if inArr[main_count]<prev_element:
                    prev_element = inArr[main_count]
                    newarr.append(prev_element)
                    inArr.pop(main_count)
                    main_count-=1
                main_count+=1
                
        outputarr = merge_strand(newarr,outputarr,SortType)
        
    return outputarr


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
def pigeonhole_Sort(A,SortType):
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
    print(pigeonhole)
    for j in range(len(pigeonhole)):
        for c in range(len(pigeonhole[j])):
            piglist = pigeonhole[j]
            if piglist:
                A[arraycount] = piglist[c]
                arraycount+=1
            
    if SortType == "Ascending":
        return A
    return list(reversed(A))


###Cocktail Sort
##
#
def cocktail_Sort(A,SortType):
    minidx = 0
    maxidx = len(A)-1
    for k in range(len(A)):
        ###
        if k%2==0:
            maxval = -math.inf
            for i in range(minidx,maxidx+1):
                if A[i]>maxval:
                    maxval = A[i]
                    maxval_idx = i

            A[maxval_idx],A[maxidx] = A[maxidx],maxval
            maxidx -= 1
            ###
        else:
            minval = math.inf
            for i in range(maxidx,minidx-1,-1):
                if A[i]<minval:
                    minval = A[i]
                    minval_idx = i
            A[minval_idx],A[minidx] = A[minidx],minval
            minval += 1
    if SortType == "Ascending":
        return A
    return list(reversed(A))


#####
#         
#Selection sort
def selection_sort(Array,sorttype):

    expression=None
    
    if(sorttype=="Ascending"):
        expression="Array[index]>Array[y]"
    else:
        expression="Array[index]<Array[y]"

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
def Buble_sort(Array,sorttype):
    expression=None
    
    if(sorttype=="Ascending"):
        expression="Array[y]<Array[x]"
    else:
        expression="Array[y]>Array[x]"

    for x in range(0,len(Array)):
        for y in range(x+1,len(Array)):
            if(eval(expression)):
                temp=Array[y]
                Array[y]=Array[x]
                Array[x]=temp
    return Array


#####
#
#Counting Sort
def counting_sort(passed_array,sorttype):
    
    orignal_Array=[]
    sorted_index_list=[]
    
    for x in range(0,len(passed_array)):
        orignal_Array.append(passed_array[x])
        sorted_index_list.append(passed_array[x])

    for x in range(0,len(passed_array)):
        passed_array[x]=passed_array[x].lower()
        Temp=passed_array[x]
        if not(Temp.isdecimal()):
            Temp=Temp.lower()
        passed_array[x]=ord(Temp[0])


    min_vallue=min(passed_array)
    if(min_vallue<0):
        for x in range(0,len(passed_array)):
            passed_array[x]=passed_array[x]-(min_vallue)
    
    max_value=max(passed_array)+1
    counting_array=[0]*max_value
    resultant_array=[0]*len(passed_array)

    for x in range(0,len(passed_array)):
        index=passed_array[x]
        counting_array[index]=counting_array[index]+1


    for x in range(0,len(counting_array)-1):
        counting_array[x+1]=counting_array[x+1]+counting_array[x]
    
    count=len(passed_array)-1

    for x in range(len(passed_array)-1,-1,-1):
        index=passed_array[x]
        sorted_index=counting_array[index]
        counting_array[index]=counting_array[index]-1
        resultant_array[sorted_index-1]=index
        sorted_index_list[count]=sorted_index-1
        count=count-1

    
    for x in range(0,len(sorted_index_list)):
        index=sorted_index_list[x]
        resultant_array[index]=orignal_Array[x]


    if(min_vallue<0):
        for x in range(0,len(resultant_array)):
            resultant_array[x]=resultant_array[x]+(min_vallue)
    
    if(sorttype!="Ascending"):
        resultant_array.reverse()

    return resultant_array

Array=["Apple","Ball","calender","1","musawir","ahmed","zellery","pointer"]
print(counting_sort(Array,"Ascending"))


#####
##
#Shell Sort
def shellsort(Array,sorttype):
    expression1=None
    expression2=None
    if(sorttype=="Ascending"):
        expression1="Array[index+gap]<Array[index]"
        expression2="Array[prevous_indexes - gap] > Array[prevous_indexes]"
    else:
        expression1="Array[index+gap]>Array[index]"
        expression2="Array[prevous_indexes - gap] < Array[prevous_indexes]"

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
def Combsort(Array,sorttype):
    expression=None
    if(sorttype!="Ascending"):
        expression="Array[index] < Array[gap+index]"
    else:
        expression="Array[index] > Array[gap+index]"


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
def cyclesort(Array,sorttype):
    expression=None
    if(sorttype=="Ascending"):
        expression="Array[x]<value"
    else:
        expression="Array[x]>value"
    for index in range(0,len(Array)):
        value=Array[index]
        current_index=index
        for x in range(index+1,len(Array)):
            if(eval(expression)):
                current_index=current_index+1
        
        if(current_index!=index):
            while value==Array[current_index]:
                current_index=current_index+1

            Array[current_index],value=value,Array[current_index]

            while current_index!=index:
                current_index=index
                for x in range(index+1,len(Array)):
                    if(eval(expression)):
                        current_index= current_index+1
                while value==Array[current_index]:
                    current_index=current_index+1
                Array[current_index],value=value,Array[current_index]
    return Array



