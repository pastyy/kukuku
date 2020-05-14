
class Price:
    def __init__(self,pc):
        if pc =='0':
            self.val = 0
        else:
            self.val = eval(pc[1:])
class Date:
    def __init__(self,dt):
        month = ['January','February','March','April','May',\
            'June','July','August','September','October','November','December']
        datels = dt.split(' ')
        self.date = dt
        yr = datels[2]
        mth = str(month.index(datels[0]) + 1)
        if len(mth) == 1:
            mth = '0' + mth
        dy = datels[1][:-1]
        if len(dy) == 1:
            dy = '0' + dy
        self.val = eval(yr + mth + dy)
#if size varies with device, set it to 0 (for the sake of convenience.)
class Size:
    def __init__(self,sz):
        self.size = sz
        if self.size == 'Varies with device':
            self.val = 0
        elif self.size[-1] == 'M':
            self.val = eval(self.size[:-1]) * 10**6
        else:
            self.val = eval(self.size[:-1]) * 10**3
class Installs:
    def __init__(self,ist):
        self.installs = ist
        if ',' in ist:
            ist = ist.replace(',','')
        self.val = eval(ist[:-1])
class Version:
    def __init__(self,vs):
        self.version = vs

        if vs == 'Varies with device':
            self.val = 0
        else:
            id_start = 0
            for char in vs:
                if char.isdigit():
                    break
                id_start +=1

            try:
                id_1 = vs.index('.')
                try:
                    self.val = eval(vs[id_start:])   
                except:
                    for i in range(id_1+1,len(vs)):
                        if not vs[i].isdigit():
                            self.val = eval(vs[id_start:i])
                            break
            except:
                try:
                    self.val = eval(vs[id_start:])
                except:
                    self.val = 100




def rankClass(p_list):
    return mergesort(p_list,0,len(p_list)-1)

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
        if a[i].val <b[j].val:
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
'''data_set contains all the data in the form of 
    [{attribute1:value11,attribute2:value12,...},{attribute1:value21...},...]

attributes_value_dict contains all the attributes 
   and their posiible values in the form 
   of {attribute1:[v1,v2,v3...],attribute2:[u1,u2,...],...}
   '''
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
dataSet, attriList = load_file('test.csv')
# print(attriList['Size'])

'''deal with dates'''
# dates = []
# for i in dataSet:
#     # print(i['Last.Updated'],end='')
#     dat = Date(i['Last.Updated'])
#     # print(dat.val)
#     dates.append(dat)

# m = rankClass(dates)  #sorted dates(Date class)
def numericApart(p_data_set,p_num_attribute,p_class,p_mid):
    modified_data_set = p_data_set[:]
    for i in modified_data_set:
        a = p_class(i[p_num_attribute])
        if isinstance(a,int) or isinstance(a,float):
            value = a
        else:
            value = a.val
        if value > p_mid:
            i[p_num_attribute] = 'larger'
        else:
            i[p_num_attribute] = 'smaller or else'

    return modified_data_set

def characterApart(p_data_set,p_cha_attribute,p_chosen):
    modified_data_set = p_data_set[:]
    for i in modified_data_set:
        if i[p_cha_attribute] != p_chosen:
            i[p_cha_attribute] = 'not ' + p_chosen
    return modified_data_set
    

print(numericApart(dataSet,'Installs',Installs,1000)[:5])

# print(Version == int)







