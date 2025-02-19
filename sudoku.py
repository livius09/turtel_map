main=[[4,   3,  None,None],
      [1,   2,  3,  None],
      [None,None, 2, None],
      [2,   1,  None,None]]
s=4

ch=1
while ch!=0:
    ch=0
    for i in range(len(main)):
        for k in range(len(main[0])):

            if main[i][k] is None:
                n=[1,2,3,4]
                for u in range(s):
                    if main[i][u] in n:
                        n.remove(main[i][u])
                    if main[u][k] in n:
                        n.remove(main[u][k])
                
                if len(n)==1:
                    main[i][k]=n[0]
                    ch+=1

for row in main:
    print(row)