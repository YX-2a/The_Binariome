import level_reader as lr
import level_maker as lk
import config_reader as cfr

if __name__ == "__main__" :
    cf_dicts = cfr.read_config ("config.conf")
    window = lk.Level(
        cf_dicts[0]["lvl_dir"]
        ,cf_dicts[0]["hlp_img"]
        ,cf_dicts[0]["def_lvl"]
        ,cf_dicts[0]["skip_gd"]
        ,cf_dicts[0]["ico_img"]
        ,cf_dicts[1]["bg_clr"]
        ,cf_dicts[1]["ib_clr"]
        ,cf_dicts[1]["fg_clr"]
        )

    menu = window.menu_()
    level_menu = menu.nametowidget(menu.entrycget(menu.index("Levels"), "menu"))
    level_menu.invoke(level_menu.index(cf_dicts[0]["def_lvl"]))
    window.end_()
