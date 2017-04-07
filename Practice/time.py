
def make_readable(ss):
    """ Take non-negative integer(seconds) and return string HH:MM::SS
    """

    hh = int(ss / (60*60))
    ss = ss % (60*60)

    mm = int(ss / 60)
    ss = ss % 60

    return "%02d:%02d:%02d" % (hh, mm, ss)

if __name__ == '__main__':
    print (make_readable(359999))
