inp=['RCB','CSK','MI','SRK','KKR','GT','RR']

out=[]
for i in range(len(inp)):
    p=1
    for j in range(len(inp)):
        if i<j:
            print(inp[i],'vs' + inp[j])