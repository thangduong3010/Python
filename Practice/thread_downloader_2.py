# python 2 version
import os
import urllib2

from threading import Thread

class DownloadThread(Thread):
	"""
	A threading example that can download a file
	"""
	def __init__(self, url, name, saved_folder):
		""" Initialises the thread """
		Thread.__init__(self)
		self.url = url
		self.name = name
		self.folder = saved_folder

	def run(self):
		""" Runs the thread """
		handle = urllib2.urlopen(self.url)
		fname = self.folder + "\\" + os.path.basename(self.url)

		with open(fname, "wb") as f_handler:
			while True:
				chunk = handle.read(1024)
				if not chunk:
					break
				f_handler.write(chunk) # write downloaded data to file

		msg = "%s has finished downloading %s!" % (self.name, self.url)
		print(msg)

def main(urls, saved_folder):
	for item, url in enumerate(urls):
		name = "Thread %s" % (item + 1)
		thread = DownloadThread(url, name, saved_folder)
		thread.start()

if __name__ == "__main__":
	saved_folder = r"F:\Github\Python\Practice\Files\data"
	urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
			"http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"
	]

	main(urls, saved_folder)