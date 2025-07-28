import os
import logging
from pyx12.x12n_document import X12Document
from pyx12.params import params
from pyx12.map_walker import walk_tree
from pyx12.errors import EngineError
import xml.etree.ElementTree as ET

def translate_x12_to_xml(input_file,output_file):

	try
	
		logging.info(f"Start Translating x12 file : {input_file}")
		
		param = params()
		param.set('map_path','etc/pyx12/maps')
		param.set('xml_path','etc/pyx12/xml')
		
		with open(input_file,r) as edi_file:
			x12_file = X12NDocument(param)
			x12_file.read(edi_file)
			
		root = ET.Element("X12Message")
		walk_tree = walk_tree(x12_file.get_root(),parent_elem = root)
		
		tree = ET.ElemenetTree(root)
		tree.write(output_file,encoding = 'utf-8',xml_declaration = True)
		
		logging.info(f"Successfully Translated x12 file  to {output_file}")
	
	except EngineError e:
	
		logging.error(f"pyx12 Engine Error : {e}")
		
	except Exception e:
		
		logging.error(f"Error occured while translating {input_file} : {e}")
