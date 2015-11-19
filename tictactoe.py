import sys
import getopt
import time

class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

def main(argv=None):
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "h", ["help"])
		except getopt.error, msg:
			raise Usage(msg)
	       # more code, unchanged
	except Usage, err:
		print >>sys.stderr, err.msg
		print >>sys.stderr, "for help use --help"
		return 2
def loop():
	try:
		while True:
			print("hola")
			time.sleep(0.5)	
	except KeyboardInterrupt:
		return
if __name__ == "__main__":
	loop()	
	print("end")
	sys.exit(main())
