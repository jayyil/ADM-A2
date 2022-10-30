import pandas as pd 
import numpy as np 
import struct 
import os 
import argparse
import time

def encode(input_path):
	df = pd.read_csv(input_path, header=None)
	encoded_items = []
	i = 0
	while i < len(df[0]):
	#     start_pos = i
	    cnt = 1 # run_length
	    value = df[0][i]
	    j = i
	    while j < len(df[0])-1:
	        if df[0][j] == df[0][j+1]:
	            cnt += 1
	            j += 1
	        else:
	            break
	    encoded_items.append((value,cnt))
	    i = j + 1
	# print(encoded_items)
	return encoded_items

def write(encoded_items,encoded_file_path):
	# write into encoded_file_path
	with open(encoded_file_path,'wb') as f:
		for item in encoded_items:
			bytes = struct.pack('ii',item[0],item[1])
			f.write(bytes)



def main():

	parser = argparse.ArgumentParser('Please enter the entire path of the file')

	parser.add_argument('--path', '-path', type=str, help='entire path of the file')

	args = parser.parse_args()

	path = args.path # get original csv file path from command line

	encoded_file_path = path+'.rle' # generate encoded bin file path

	
	print('begin to encode')
	start = time.time()
	encoded_items = encode(path)
	write(encoded_items, encoded_file_path)
	end = time.time()
	print('done! encoded file has writte into {}'.format(encoded_file_path))
	print('using time:', end-start)


if __name__ == '__main__':
	main()