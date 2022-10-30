import pandas as pd 
import numpy as np 
import struct 
import os 
import argparse
import time

def decode(input_path):
	decoded_items = []
	size = os.path.getsize(input_path)
	with open(input_path,'rb') as f:
		while size > 0:
			str_length_bytes = f.read(2)
			size = size - 2
			str_length = struct.unpack('h',str_length_bytes)[0]
			data = f.read(str_length + 1)
			decoded_items.append(struct.unpack('%dsb'%str_length,data))
			size = size - 1
			size = size - str_length
	return decoded_items

def write(decoded_items,decoded_file_path):
	# write into decoded_file_path
	with open(decoded_file_path,'w') as f:
		for item in decoded_items:
			for i in range(item[1]):
				f.write(item[0].decode('utf-8'))
				# f.write('\n')



def main():

	parser = argparse.ArgumentParser('Please enter the entire path of the file')

	parser.add_argument('path', type=str, help='entire path of the file')

	args = parser.parse_args()

	path = args.path # get original csv file path from command line

	decoded_file_path = path+'.csv' # generate decoded bin file path

	
	print('begin to decode')
	start = time.time()
	decoded_items = decode(path)
	write(decoded_items, decoded_file_path)
	end = time.time()
	print('done! encoded file has writte into {}'.format(decoded_file_path))
	print('using time:', end-start)


if __name__ == '__main__':
	main()