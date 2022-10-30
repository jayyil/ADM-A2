from csv_diff import load_csv, compare
import argparse
import time

def main():

	parser = argparse.ArgumentParser('Please enter the entire path of the two csv file you are going to compare')

	parser.add_argument('--file1', '-file1', type=str, help='entire path of the first csv file')

	parser.add_argument('--file2', '-file2', type=str, help='entire path of the second csv file')

	args = parser.parse_args()

	path1 = args.file1 

	path2 = args.file2

	diff = compare(
			load_csv(open(path1)),
			load_csv(open(path2))
		)

	flag = True
	for i in diff.values():
	    if i == []:
	        continue
	    else:
	        flag = False
	        break

	if flag == True:
		print('Two csv files have no difference')
	else:
		print('Two csv files are different')

if __name__ == '__main__':
	print('begin to compare tow csv files...')
	start = time.time()
	main()
	end = time.time()
	print('time used:', end-start)