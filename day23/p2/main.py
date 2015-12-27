
class Inst(object):
    def __init__(self,line):
        parts=[x.strip() for x in line.split(' ')]
        self.op = parts[0]
        self.first = parts[1].split(',')[0]
        if self.op == 'jmp':
            self.first = int(self.first)
        if len(parts) > 2:
            self.second = int(parts[2])
        else:
            self.second = None
    def __str__(self):
        ret = "%s %s" % (self.op, self.first)
        if self.second is not None:
            ret = "%s, %s" % (ret, self.second)
        return ret
def main():
    iset=[]
    with open('../input.txt', 'r') as fp:
        while True:
            line=fp.readline()
            if line is None or line == '':
                break
            iset.append(Inst(line))
    #Registers
    r={'a':1}
    pos = 0
    #While instruction pointer is within instruction set
    while pos >= 0 and pos < len(iset):
        i = iset[pos]
        if i.op == 'jmp':
            pos = pos + i.first
        else:
            #Initialize register if necessary
            if i.first not in r:
                r[i.first] = 0
            if i.op == 'jie' and r[i.first] % 2 == 0:
                pos = pos + i.second
            elif i.op == 'jio' and r[i.first] == 1:
                pos = pos + i.second
            else:
                if i.op == 'hlf':
                    r[i.first] = r[i.first] / 2
                elif i.op == 'tpl':
                    r[i.first] = r[i.first] * 3
                elif i.op == 'inc':
                    r[i.first] = r[i.first] + 1
                pos = pos + 1
    print r['b']
if __name__ == '__main__':
    main()