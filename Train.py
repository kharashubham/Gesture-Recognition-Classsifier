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

f1 = read_from_file("/Users/Shubham/PycharmProjects/GsRec/FinalData/O.txt")
f2 = read_from_file("/Users/Shubham/PycharmProjects/GsRec/FinalData/S.txt")
f3 = read_from_file("/Users/Shubham/PycharmProjects/GsRec/FinalData/V.txt")
f4 = read_from_file("/Users/Shubham/PycharmProjects/GsRec/FinalData/W.txt")

mat1 = numpy.asarray(f1, dtype='float')
mo1 = numpy.full((31,),1,dtype=numpy.int)
mat2 = numpy.asarray(f2, dtype='float')
mo2 = numpy.full((31,),2,dtype=numpy.int)
mat3 = numpy.asarray(f3, dtype='float')
mo3 = numpy.full((31,),3,dtype=numpy.int)
mat4 = numpy.asarray(f4, dtype='float')
mo4 = numpy.full((31,),4,dtype=numpy.int)


X = numpy.concatenate((mat1, mat2, mat3, mat4),0)
Y = numpy.concatenate((mo1, mo2, mo3, mo4), 0)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)





