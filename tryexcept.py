import time
import threading

if __name__ == '__main__':
	try:
		print('start')
		time.sleep(100)
		print('stop')


	except KeyboardInterrupt:
		print('You pressed CTRL-C!')
