import sys
g = {}
t = []
end = 2
if len(sys.argv) == 2:
    f = open(sys.argv[1])
elif len(sys.argv) == 4:
    f = open(sys.argv[3])
    end = int(sys.argv[2])

with (f) as graph_input:
    for line in graph_input:
        nodes = [int(x) for x in line.split()]
        if len(nodes) != 2:
            continue
        if nodes[0] not in g:
            g[nodes[0]] = []
        if nodes[1] not in g:
            g[nodes[1]] = []
        g[nodes[0]].append(nodes[1])
        g[nodes[1]].append(nodes[0])
i=0
c=1
while not ( c==len(g) + 1 ):
    for v in g[c]:
        i +=1
    c += 1
syn=i
d=1
c=1
t1 = len(g)
while not ( c==t1 + 1 ):
    t.append([c])
    c += 1
f.close()

def e(a,b):
    r1=0
    t2=0
    while not ( r1==len(t[b-1])):
        r2=0
        while not ( r2==len(t[a-1])):
            t2= t2 + g[t[b-1][r1]].count(t[a-1][r2])
            r2 += 1
        r1 += 1
    return t2

def a(i):
    s=0
    r3=0
    while not (r3==len(t)):
        r3 += 1
        e(i,r3)
        s=  s + e(i,r3)
    return s

i=0
Q=0
while not (i == len(t)):
    Q= Q + e(i,i)/syn - (a(i)*a(i)) / (syn * syn)
    i +=1

while len(t) > end:
    max = -9999999999999
    i=0
    th = []
    ah = []
    while not (i == len(t)):
        j=0
        while not (j == len(t)):
            DQ = 2*((e(i,j)/syn) - (a(i)*a(j)) / (syn * syn))
            if DQ > max and i!=j:
                max = DQ
                ah = t[i-1]
                th = t[j-1]
                ni = i-1
                nj = j-1
            j += 1
        i += 1
    t[ni].extend(th)
    del t[nj]
    Q = Q + max

i=0
while not (i == end):
    print (sorted(t[i]))
    i  += 1
print ("Q = %.4f" % (Q))
