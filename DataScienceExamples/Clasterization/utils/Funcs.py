def convertDate(d):
    r = []
    if(isinstance(d,str)):
        d = d.split(' ')
        if(d[0][0] == '0'):
            d[0] = d[0][1:]
            print(d[0])
            if(d[0][2] == '0'):
                d[0] = d[0][0:2] + d[0][3:]

        dat = d[0].split('/')
        j = len(dat)
        while(j > 0):
            j -= 1
            for i in range(0,len(dat[j])):
                r.append(dat[j][i])
        i = 0
        if(len(d) > 1):
            l = len(d[1])
            while(i < l):
                if(d[1][i] == ' ' or d[1][i] == ':' or d[1][i] == '/' or d[1][i] == '.'):
                    i += 1
                    continue
                r.append(d[1][i])
                i += 1

    return int(''.join(r))