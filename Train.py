'''
Fianl data stored in FinalData directory used to train ML model
'''
import numpy
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC

def read_from_file(file):
    f = open(file,"r")
    final = []
    i = 0
    k = 0
    for x in range(0,31):
        final.append([])
    for line in f:
        if line != "\n":
            i += 1
            line = line.replace("\n",'')
            final[k].append(line.split(","))
        elif line == "\n":
            k += 1
    return final

f1 = read_from_file("FinalData/O.txt")
f2 = read_from_file("FinalData/S.txt")
f3 = read_from_file("FinalData/V.txt")
f4 = read_from_file("FinalData/W.txt")


def format_file(f):
    final_data = []
    for row in f:
        row_array = numpy.array([])
        for item in row:
            new_item = numpy.asarray(item, dtype='float')
            row_array = numpy.concatenate((row_array,new_item), 0)
        final_data.append(row_array)
    return final_data

mat1 = format_file(f1)
mat2 = format_file(f2)
mat3 = format_file(f3)
mat4 = format_file(f4)

mo1 = numpy.full((31,),1, dtype=numpy.int)
mo2 = numpy.full((31,),2, dtype=numpy.int)
mo3 = numpy.full((31,),3, dtype=numpy.int)
mo4 = numpy.full((31,),4, dtype=numpy.int)


X = numpy.concatenate((mat1, mat2, mat3, mat4),0)
Y = numpy.concatenate((mo1, mo2, mo3, mo4), 0)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)


clf = SVC(kernel='rbf', C=4)
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
