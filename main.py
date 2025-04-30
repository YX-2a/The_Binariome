import level_reader as lr
import config_reader as cfr

if __name__ == "__main__" :
    cf_dict = cfr.read_config ("config.conf")
    window = lr.Level(
        cf_dict[0]["levels_directory"]
        ,cf_dict[1]["help_image"]
        ,cf_dict[2]["default_level"]
        ,cf_dict[3]["skip_guide"])

    
    options = lr.read_level(cf_dict[0]["levels_directory"] + cf_dict[2]["default_level"])
    window.menu_()
    window.make_level (options[0],options[1],options[2],options[3],options[4])
    window.end_()
