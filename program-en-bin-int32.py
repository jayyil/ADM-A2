import pandas as pd 
import numpy as np 
import struct 
import os
import argparse 
import time

def encode(input_path,output_path):
	df = open(input_path,'r').read().splitlines()
	df = [int(x) for x in df]
	with open(output_path,'wb') as f:
		for d in df:
			bytes = struct.pack('i',d)
			f.write(bytes)






def main():
	parser = argparse.ArgumentParser('Please enter the entire path of the file')
	parser.add_argument('path', type=str, help='entire path of the file')
	args = parser.parse_args()

	path = args.path # get original csv file path from command line
	encoded_file_path = path+'.bin' # generate encoded bin file path

	print('begin to encode')
	start = time.time()
	encode(path,encoded_file_path)
	end = time.time()
	print('done! encoded file has writte into {}'.format(encoded_file_path))
	print('using time:', end-start)


if __name__ == '__main__':
	main()