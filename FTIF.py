'''
FTIF.py ===>> Filtering, Truncation, Interpolation And Feature Selection(using FFT)
Final data to be used be classifier for trainig is stored in FinalData directory.
FinalData ==> 31 training examples for 4 classes each.
'''
import numpy
from scipy.interpolate import interp1d
from pandas import *


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

file = read_from_file("/Users/Shubham/PycharmProjects/GsRec/RawData/O.txt")


def filter(file, a):
    filter_file = []
    filter_row = []
    for x in range(0,31):
        filter_file.append([])
        for row in file[x]:
            filter_row.append(row[0])
            for i in range(1,100):
                filter_row.append(a*float(row[i-1]) + (1-a)*float(filter_row[i-1]))
            filter_file[x].append(filter_row)
            filter_row = []
    return filter_file


filter_file = filter(file,0.3)


def truncate(file, a):
    std_list = []
    temp_list = []
    for x in range(0,31):
        std_list.append([])
        for row in file[x]:
            threshold = a*(numpy.std(numpy.array(row).astype(numpy.float))**1/2)
            for i in row:
                if abs(float(i)) > float(threshold):
                    temp_list.append(i)
                else:
                    temp_list.append(numpy.nan)
            std_list[x].append(temp_list)
            temp_list = []
    return std_list

truncation = truncate(filter_file, 0.37)

i_polate_list = []
for x in range(0,31):
    i_polate_list.append([])
    for row in truncation[x]:
        row = numpy.array(row, dtype=numpy.float64)
        not_nan = numpy.logical_not(np.isnan(row))
        indices = numpy.arange(len(row))
        new_row = numpy.interp(indices, indices[not_nan], row[not_nan])
        i_polate_list[x].append(new_row)


final_data = i_polate_list

amp = []
for x in range(0, 31):
    amp.append([])
    for row in i_polate_list[x]:
        fourier = numpy.fft.fft(row, 21)
        sup = []
        for y in range(21):
            sup.append(((fourier[y].real ** 2 + fourier[y].imag ** 2) ** 1 / 2)/100)
        amp[x].append(sup)

for x in range(0, 31):
    for y in range(0, 3):
        final_data[x][y] = numpy.concatenate((final_data[x][y], amp[x][y]),0)

f = open('/Users/Shubham/PycharmProjects/GsRec/FinalData/O.txt', 'w')
for x in range(0, 31):
    for y in range(0,3):
        for z in range(0,121):
            f.write(str(final_data[x][y][z]))
            if z == 120:
                f.write('\n')
            else:
                f.write(',')
    f.write('\n')