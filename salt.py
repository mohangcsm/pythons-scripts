##################################################################
# Author : Mohan Kallepalli                                      #
# Date : 10-08-2015                                              #
##################################################################

import random
import sys

def main(argv):

	try:
		if (len(sys.argv) != 2):
			sys.exit('Usage: salt.py <salt_length>')
		else:
			charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_@#$%^&*!"
			salt_length = int(argv[0])
			if salt_length > 128:
				print "\nsalt length too high. reduced to default 128"
				salt_length = 128
			salt = ''
			for i in range(salt_length):
				salt += charset[random.randint(0,len(charset)-1)]
			
			print '***************************'
			print 'Your new salt is: \n\n' + salt + '\n'
			print '***************************'
	except:
		sys.exit('Usage: salt.py <salt_length>')
	
if __name__ == "__main__":
	main(sys.argv[1:])
