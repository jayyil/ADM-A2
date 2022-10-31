import pandas as pd 
import numpy as np 
import struct 
import os 
import argparse
import time

def decode(input_path,output_path):
	decoded_items = []
	size = os.path.getsize(input_path)
	with open(input_path,'rb') as f:
		for i in range(int(size/2)):
			data = f.read(2)
			decoded_items.append(struct.unpack('h',data))
	with open(output_path,'w') as f:
		for item in decoded_items:
			f.write(str(item[0]))
			f.write('\n')




def main():

	parser = argparse.ArgumentParser('Please enter the entire path of the file')

	parser.add_argument('path', type=str, help='entire path of the file')

	args = parser.parse_args()

	path = args.path # get original csv file path from command line

	decoded_file_path = path+'.csv' # generate decoded bin file path

	
	print('begin to decode')
	start = time.time()
	decoded_items = decode(path,decoded_file_path)
	end = time.time()
	print('done! decoded file has writte into {}'.format(decoded_file_path))
	print('using time:', end-start)


if __name__ == '__main__':
	main()