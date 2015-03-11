from xml.etree import ElementTree
from string import Template
import sys
cls_begin_string = "public class %s{"
attribute_string = "$type $name = $default;"
method_string = "$return $name($params){\n}"
cls_end_string = "}"


class Handler(object):
	"""docstring for Handler"""
	def attribute(self, e):
		"""docstring for attribute"""
		print Template(attribute_string).safe_substitute(e.attrib)

	def method(self, e):
		"""docstring for method"""
		print Template(method_string).safe_substitute(e.attrib)
	def cls(self, e):
		"""docstring for cls"""
		print cls_begin_string % e.tag

def iterate(xmlstring):
	handle = Handler()
	root = ElementTree.fromstring(xmlstring)
	for  e in root.iter():
		getattr(handle, e.tag)(e)
	print cls_end_string
	return 


def dct(xmlstring, tag):
        data = {}
        root = ElementTree.fromstring(xmlstring)
        for e in root.find(tag).iter():
          data.update(e.attrib)
        return data

if __name__ == '__main__':
	xmlstring = sys.stdin.read()
	iterate(xmlstring)
