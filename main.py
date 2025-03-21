import level_reader as lr


if __name__ == "__main__" :
    window = lr.Level()
    options = lr.read_level("./levels/level_1.ylfs")
    window.make_level (options[0],options[1],options[2],options[3])
    window.end_()
