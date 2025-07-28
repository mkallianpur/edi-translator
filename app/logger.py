import os
import logging

def setup_logger(log_file = 'app.log',log_level=logging.INFO):
	
	logging.INFO("Started setting up logger")
	
	log_path os.makedirs('logs',exist_ok = True)
	os.path.join(log_path,log_file)
	
	logging.basicConfig(
	level = level_log,
	format = f"%(asctime)s - %(levelname)s - %(message)s"
	handlers = [
		logging.FileHandler(log_path),
		logging.SreamHandler()
		])
		
	logging.info("logger initialized")
	

