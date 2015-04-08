import traceback as tb

class myexceptionhandler(object):
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        print tb.print_tb(traceback)
        return True # tear it down

with myexceptionhandler():
    print "do some stuff here"
    1/0

print "should still reach this point"
