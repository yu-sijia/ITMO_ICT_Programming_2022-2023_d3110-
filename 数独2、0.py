import copy
import time
def valueRange(row):
    temp = copy.deepcopy(row)
    row_value_range = list(range(1,10))
    for i in row:
        if i == '':
            continue
        else:
            if row_value_range.count(i) > 0:
                row_value_range.remove(i)
            else:
                continue
    for j in range(9):
        if temp[j] == '':
            temp[j] = row_value_range
        else:
            temp[j] = [temp[j]]
    return temp
def rowValueRange(soduku):
    row_value_range = []
    for row in soduku:
        row_value_range.append(valueRange(row))
    return row_value_range
def colValueRange(soduku):
    soduku_invert = [list(i) for i in list(zip(*soduku))]
    temp = rowValueRange(soduku_invert)
    s_column_vrange = [list(i) for i in list(zip(*temp))]
    return s_column_vrange
def matrix_invert(lista):
    listb = [[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            k = i//3
            l = j//3
            m = k*3 + l
            listb[m].append(lista[i][j])
    return listb
def matrixValueRange(soduku):
    matrix = matrix_invert(soduku)
    temp = rowValueRange(matrix)
    matrix_vrange = matrix_invert(temp)
    return matrix_vrange
def inersection(lista,listb,listc):
    tempa = []
    tempb = []
    for i in lista:
        for j in listb:
            if i == j:
                tempa.append(i)
    for k in listc:
        for l in tempa:
            if k == l:
                tempb.append(k)
    return tempb
def totalValueRange(soduku):
    row_value_range = rowValueRange(soduku)
    col_value_range = colValueRange(soduku)
    matrix_value_range = matrixValueRange(soduku)
    total_value_range = [[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            total_value_range[i].append(inersection(row_value_range[i][j],col_value_range[i][j],matrix_value_range[i][j]))
    return total_value_range
def checkUnique(list):
    listb = copy.deepcopy(list)
    templist = []
    for i in listb:
        templist.extend(i)
    for i in range(len(list)):
        for j in list[i]:
            if templist.count(j) == 1:
                listb[i] = [j]
    list = listb
    return list
def row_checkUnique(s_row_vrange):
    temp = []
    for list in s_row_vrange:
        temp.append(checkUnique(list))
    s_row_vrange = temp
    return s_row_vrange
def soduku_checkUnique(s_row_vrange):
    temp = []
    temp_b = []
    s_row_vrange = row_checkUnique(s_row_vrange)
    for i in list(zip(*s_row_vrange)):
        temp.append(list(i))
    temp = row_checkUnique(temp)
    for i in list(zip(*temp)):
        temp_b.append(list(i))
    temp_c = matrix_invert(temp_b)
    temp_c = row_checkUnique(temp_c)
    temp_d = matrix_invert(temp_c)
    return temp_d

def generator_soduku(total_value_range):
    soduku = [[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            if len(total_value_range[i][j]) == 1:
                soduku[i].append(total_value_range[i][j][0])
            else:
                soduku[i].append('')
    return soduku
def reduce_totalValueRange(soduku):
    for n in range(100):
        total_value_range = totalValueRange(soduku)
        total_value_range = soduku_checkUnique(total_value_range)
        soduku = generator_soduku(total_value_range)
        if total_value_range == totalValueRange(generator_soduku(total_value_range)):
            break
    return total_value_range

def row_checkRepeat(s_value_range):
    for i in s_value_range:
        temp = []
        for j in i:
            if len(j) == 1:
                temp.append(j[0])
        len_temp = len(temp)
        if len_temp != len(list(set(temp))):
            return False
    return True
def soduku_checkRepeat(s_value_range):
    temp_col = list(zip(*s_value_range))
    temp_matrix = matrix_invert(s_value_range)
    return row_checkRepeat(s_value_range) and row_checkRepeat(temp_col) and row_checkRepeat(temp_matrix)
def sodukuRate(s_row_vrange):
    rate = 1
    for i in s_row_vrange:
        for j in i:
            rate *= len(j)
    return rate
def trial(total_value_range):
    for i in range(9):
        for j in range(9):
            if len(total_value_range[i][j]) > 1:
                for k in total_value_range[i][j]:
                    test_value = copy.deepcopy(total_value_range)
                    test_value[i][j] = [k]
                    test_value = reduce_totalValueRange(generator_soduku(test_value))
                    if soduku_checkRepeat(test_value):
                        if sodukuRate(test_value) == 1:
                            return test_value
                        else:
                            if trial(test_value):
                                return trial(test_value)
                    else:
                        continue
                return False

if __name__ == '__main__':
    t1 = time.time()
    soduku = [[] for i in range(9)]
    soduku[0] = ['','','',5,'',2,'','','']
    soduku[1] = ['',1,6,'','','','',8,'']
    soduku[2] = ['','','','','','','','','']
    soduku[3] = ['',7,'','',3,'','',1,'']
    soduku[4] = ['',6,'','','','','','','']
    soduku[5] = [5,'','','','',9,'','','']
    soduku[6] = ['',3,'','',8,'','','','']
    soduku[7] = ['','','','','','',2,'','']
    soduku[8] = [7,'','','','','',5,'',9]

    a = reduce_totalValueRange(soduku)
    for i in trial(a):
        print(i)

    print("Время запуска = {}секунд".format(round(time.time() - t1,2)))
