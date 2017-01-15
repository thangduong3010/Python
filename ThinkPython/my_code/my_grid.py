def do_twice(f):
	f()
	f()

def do_four(f):
	f()
	f()
	f()
	f()

def print_beam():
	print '+ - - - -',

def print_beams():
	do_twice(print_beam)
	print '+'

def print_post():
	print '/        ',

def print_posts():
	do_twice(print_post)
	print '/'

def print_rows():
	print_beams()
	do_four(print_posts)

def print_grid():
	do_twice(print_rows)
	print_beams()
	

if __name__ == "__main__":
	print_grid()