def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
# 'earth/mars/venus' (Output)
concat("earth", "mars", "venus", sep=".")
# 'earth.mars.venus' (Output)