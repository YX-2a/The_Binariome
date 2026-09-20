def read_level (filename):
    with open (filename) as levl:
        levl_raw = levl.readlines ()

    i0, i1, tit, hi, wi,gl, can_list = None,None,None,None,None,None,[]

    for i in levl_raw :
        if "YLFSys ==" in i:
            i0 = i
        if "== YLFSys" in i:
            i1 = i
        else:
            continue
        
    inde1 = levl_raw.index(i0) + 1
    inde2 = levl_raw.index(i1) 
    
    levl_uck = levl_raw [ inde1 : inde2 ]
    levl_uck = [i.strip() for i in levl_uck]
    levl_uck = [i for i in levl_uck if i != ""]

    tit = levl_uck[0].replace ("t:","")
    hi = int(levl_uck[1].replace ("h:",""))
    wi = int(levl_uck[2].replace ("w:",""))
    gl = int(levl_uck[3].replace ("g:",""))
    levl_uck = levl_uck[4:]

    for i in levl_uck:
        for car in i:
            i = i[i.index(car):]
            if car == ":":
                i = i[i.index(":") + 1:]
                break

        if ",l" in i:
            can_list.append ( [ int (i[:i.index(",l")].split(",")[0]),int (i[:i.index(",l")].split(",")[1]), True ])

        else:
            can_list.append ([ int(i.split(",")[0]),int (i.split(",")[1]), False ] )
            
    return tit, hi, wi, gl, can_list
