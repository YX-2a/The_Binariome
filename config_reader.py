def raw_values (iter_):
    n_iter_ = []

    for i in iter_:
        for n in i:
            if n == "=":
                i = i[ i.index("=") + 1 : ]

            else:
                continue
        
        n_iter_.append (i)

    return n_iter_

def read_config (file):
    with open (file) as cog:
        cflst = cog.readlines()

    cflst =  [ i.strip() for i in cflst ]

    lvlsf = cflst [cflst.index ("[Level Conf]") + 1 : cflst.index("[Canvas Conf]")]
    cvlsf = cflst [cflst.index ("[Canvas Conf]") + 1 : ]

    lvl_sf = raw_values (lvlsf)
    cv_sf = raw_values (cvlsf)

    return [ {"lvl_dir":lvl_sf[0],"hlp_img":lvl_sf[1],"def_lvl":lvl_sf[2],"skip_gd":lvl_sf[3],"ico_img":lvl_sf[4]}
             , {"bg_clr":cv_sf[0],"ib_clr":cv_sf[1],"fg_clr":cv_sf[2]} ]

