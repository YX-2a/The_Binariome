def read_config (file):
    with open (file) as cog:
        cflst = cog.readlines()

    cflst =  [ i.strip() for i in cflst ]

    cf_lst = []

    for i in cflst:
        for n in i:
            if n == "=":
                i = i[ i.index("=") + 1 : ]

            else:
                continue

        cf_lst.append (i)

    return [ {"levels_directory" : cf_lst[0] },
             {"help_image" : cf_lst[1] },
             {"default_level" : cf_lst[2] },
             {"skip_guide" : cf_lst[3] } ]

