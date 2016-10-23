'''
Clean the raw data obtained from iOS app(in Accelerometer_Raw_Data Directory).
Output raw data stored in RawData Directory.
'''
for x in range(1,32):
    stre = str(x)
    fo = open('/Users/Shubham/PycharmProjects/GsRec/Accelerometer_Raw_Data/Z/'+stre+'.txt','r')
    lines = fo.readlines()
    fo.close()
    fo = open('/Users/Shubham/PycharmProjects/GsRec/Accelerometer_Raw_Data/Z/'+stre+'.txt', 'w')
    for line in lines:
        if line == '<?xml version="1.0" encoding="UTF-8"?>'+'\n':
            continue
        elif line == '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">'+'\n':
            continue
        elif line == '<plist version="1.0">'+'\n':
            continue
        elif line == '<dict>'+'\n':
            continue
        elif line == '\t'+'<key>X-Values</key>'+'\n':
            fo.write(lines[20])
        elif line == '\t'+'<array>'+'\n':
            continue
        elif line == '\t'+'</array>'+'\n':
            continue
        elif line == '\t'+'<key>Y-Values</key>'+'\n':
            fo.write(lines[120])
        elif line == '\t'+'<key>Z-Values</key>'+'\n':
            fo.write(lines[220])
        elif line == '</dict>'+'\n':
            continue
        elif line == '</plist>'+'\n':
            continue
        elif line == '\n':
            continue
        else:fo.write(line)