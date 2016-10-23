'''
CSV file created from Raw data stored in RawData directory
'''
f = open('/Users/Shubham/PycharmProjects/GsRec/RawData/).txt','a')

for x in range(1,32):
    stre = str(x)
    with open('/Users/Shubham/PycharmProjects/GsRec/Accelerometer_Raw_Data/O/'+stre+'.txt', 'r') as doc:
        f.write('\n')
        cnt = 0
        for line in doc:
            line = line.replace('</real>','<real>')
            line = line.replace('<real>','')
            if line != []:
                a = line
                a = float(a)
                f.write(str(a))
                cnt += 1
                if cnt == 100:
                    cnt = 0
                    f.write('\n')
                else:
                    f.write(',')
