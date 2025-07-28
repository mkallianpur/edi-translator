import os
import threading
from translator import translate_x12_xml

def process_file(input_file_path,output_file_path):
	try:
		translate_x12_xml(input_file_path,output_file_path)
	finally:
		os.remove(input_file_path)
		
def scan_directory(x12_dir_path,xml_dir_path,max_threads=10):
	
	files = []
	for f in os.listdir(x12_dir_path):
		if f.startswith("ISA"):
			files.append(f)
			
	threads = []
	
	for file in files:
		
		if len(threads) >= max_threads:
			for t in threads:
				t.join()
				threads = []
				
		input_path = os.path.join(x12_dir_path,file)
		output_path = os.path.join(xml_dir_path,file+'_xml')
		t = threading.Thread(target=process_file,args=(input_path,output_path))
		t.start()
		threads.append(t)
		
	for t in threads:
		t.join()
	
	print("All files processed. Shutting down!")
	
	
		
