import sys
import os
import threading
import urllib2

if sys.version[0] == "2":
	from Queue import Queue
else:
	from queue import Queue

class Downloader(threading.Thread):
	""" Threaded file downloader """

	def __init__(self, queue, saved_folder):
		""" Initialises the thread """
		threading.Thread.__init__(self)
		self.queue = queue
		self.folder = saved_folder

	def run(self):
		while True:
			# get the urls from the queue
			url = self.queue.get()

			# download the file
			self.download_file(url)

			# send a signal to the queue that the job is done
			self.queue.task_done()

	def download_file(self, url):
		handle = urllib2.urlopen(url)
		fname = self.folder + "\\" + os.path.basename(url)

		with open(fname, "wb") as f:
			while True:
				chunk = handle.read(1024)
				if not chunk:
					break

				f.write(chunk)

def main(urls, saved_folder):
	""" Run the program """
	queue = Queue()

	# create a thread pool and give them a queue
	for i in range(5):
		t = Downloader(queue, saved_folder)
		t.setDaemon(True)
		t.start()

	# give data to the queue
	for url in urls:
		queue.put(url)

	# wait for the queue to finish
	queue.join()


if __name__ == "__main__":
	saved_folder = r"F:\Github\Python\Practice\Files\data"
	urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"
	]
	main(urls, saved_folder)