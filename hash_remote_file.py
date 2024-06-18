import os, hashlib, urllib.request, optparse

def get_remote_md5_sum(url,algorithm):
	remote = urllib.request.urlopen(url)
	return hash(remote, algorithm)

def hash(remote, algorithm="md5"):
	max_file_size=100*1024*1024
	if algorithm=="md5":
		hash = hashlib.md5()
	elif algorithm=="sha1":
		hash = hashlib.sha1()
	elif algorithm=="sha256":
		hash = hashlib.sha256()
	elif algorithm=="sha384":
		hash = hashlib.sha384()
	elif algorithm=="sha512":
		hash = hashlib.sha512()

	total_read = 0
	while True:
		data = remote.read(4096)
		total_read += 4096

		if not data or total_read > max_file_size:
			break

		hash.update(data)

	return hash.hexdigest()

if __name__ == '__main__':
	opt = optparse.OptionParser()
	opt.add_option('--url', '-u', default='http://www.google.com')
	opt.add_option('--algorithm', '-a', default='md5')

	options, args = opt.parse_args()
	print (get_remote_md5_sum(options.url, options.algorithm))