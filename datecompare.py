#date format: ri-month-year
#e.g. 23-Mar-18
month = ['January','February','March','April','May',\
    'June','July','August','September','October','November','December']

class Date:
    def __init__(self,dt):
        datels = dt.split(' ')
        self.date = dt
        yr = datels[2]
        mth = str(month.index(datels[0]) + 1)
        if len(mth) == 1:
            mth = '0' + mth
        dy = datels[1][:-1]
        if len(dy) == 1:
            dy = '0' + dy
        self.cpdt = eval(yr + mth + dy)

def rankDate(dateList):
    return mergesort(dateList,0,len(dateList)-1)

def mergesort(lis,left,right):  #lis:inside are dates of Date class
    if left > right:
        return []
    if left == right:
        return lis[left:right+1]
    mid = int((left + right)/2)
    p = mergesort(lis,left,mid)
    q = mergesort(lis,mid+1,right)
    return merge(p,q)
def merge(a,b):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    L = []
    i = j = 0
    while True:
        if a[i].cpdt <b[j].cpdt:
            L.append(a[i])
            i +=1
        else:
            L.append(b[j])
            j +=1
        if i > len(a) - 1 or j > len(b) - 1:
            break
    k = i
    while k < len(a):
        L.append(a[k])
        k += 1
    k = j
    while k < len(b):
        L.append(b[k])
        k += 1
    return L

def load_file(p_file):
    f = open(p_file,'r',encoding='UTF-8')
    attributes = f.readline().strip('\n').strip('"').split('","')
    for i in range(1,4):
        attributes.append(attributes[1])
        attributes.remove(attributes[1])

    attributes_value_dict = {}
    for i in attributes:
        attributes_value_dict[i] = []
    # read data
    data_set = []  
    for line in f.readlines():
        ar_1 = line.strip('\n').split(',')
        if 'NA' in ar_1:  #If there is NA is the data, discard it.
            continue  
        temp_array = line.strip('\n').strip('"').split('","')
        splt = temp_array[1]
        temp_array.remove(temp_array[1])
        spltlist = splt.split('"')
        temp_array.append(spltlist[0])
        temp_array.append(spltlist[1][1:-1])
        temp_array.append(spltlist[2])
        if '' in temp_array:
            continue
        example = {}  # 样本(X,y)
        for i in range(len(temp_array)):
            example[attributes[i]] = temp_array[i]
            if temp_array[i] not in attributes_value_dict[attributes[i]]:
                attributes_value_dict[attributes[i]].append(temp_array[i])
        data_set.append(example)
    f.close()
    return data_set,attributes_value_dict

dates = []
for i in data_set:
    # print(i['Last.Updated'],end='')
    dat = Date(i['Last.Updated'])
    # print(dat.cpdt)
    dates.append(dat)

m = rankDate(dates)
countr = 0
for i in m:
    # print(i.date)
    countr +=1
# print(countr)


dataSet, attriList = load_file('test.csv')





