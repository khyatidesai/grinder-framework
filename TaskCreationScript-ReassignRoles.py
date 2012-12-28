# The Grinder 3.10
# HTTP script recorded by TCPProxy at Dec 10, 2012 4:54:02 PM

from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()

# To use a proxy server, uncomment the next line and set the host and port.
# connectionDefaults.setProxyServer("localhost", 8001)

# These definitions at the top level of the file are evaluated once,
# when the worker process is started.

connectionDefaults.defaultHeaders = \
  [ NVPair('Accept-Encoding', 'gzip, deflate'),
    NVPair('Accept-Language', 'en-us,en;q=0.5'),
    NVPair('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0.1'), ]

headers0= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ]

headers1= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/login.htm'), ]

headers2= \
  [ NVPair('Accept', 'application/json, text/javascript, */*; q=0.01'),
    NVPair('Referer', 'http://titan:8080/index.htm'), ]

headers3= \
  [ NVPair('Accept', 'text/html, */*; q=0.01'),
    NVPair('Referer', 'http://titan:8080/index.htm'), ]

headers4= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/index.htm'), ]

headers5= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/ui-fw/tasks.htm?null'), ]

headers6= \
  [ NVPair('Accept', 'application/xml, text/xml, */*; q=0.01'),
    NVPair('Referer', 'http://titan:8080/ui-fw/tasks.htm?null'),
    NVPair('Cache-Control', 'no-cache'), ]

headers7= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxTesting/form.gi/IntalioInternal/ServerLaunch.html?id=f1e71b24-a117-4cef-bcc8-aa2899e6e240&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxTesting%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers8= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxTesting/form.gi/IntalioInternal/ServerLaunch.html?id=f1e71b24-a117-4cef-bcc8-aa2899e6e240&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxTesting%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers9= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxTesting/form.gi/IntalioInternal/ServerLaunch.html?id=f1e71b24-a117-4cef-bcc8-aa2899e6e240&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxTesting%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers10= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxTesting/form.gi/IntalioInternal/ServerLaunch.html?id=f1e71b24-a117-4cef-bcc8-aa2899e6e240&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxTesting%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers11= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=f973951f-16e0-459e-af0a-f2aaf6e8964b&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers12= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=f973951f-16e0-459e-af0a-f2aaf6e8964b&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers13= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=f973951f-16e0-459e-af0a-f2aaf6e8964b&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers14= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=f973951f-16e0-459e-af0a-f2aaf6e8964b&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers15= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-134d127.0.0.166&type=PATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers16= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-134d127.0.0.166&type=PATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers17= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-134d127.0.0.166&type=PATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers18= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-134d127.0.0.166&type=PATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

url0 = 'http://titan:8080'

# Create an HTTPRequest for each request, then replace the
# reference to the HTTPRequest with an instrumented version.
# You can access the unadorned instance using request101.__target__.
request101 = HTTPRequest(url=url0, headers=headers0)
request101 = Test(101, 'GET /').wrap(request101)

request102 = HTTPRequest(url=url0, headers=headers0)
request102 = Test(102, 'GET login.htm').wrap(request102)

request201 = HTTPRequest(url=url0, headers=headers1)
request201 = Test(201, 'POST login.htm').wrap(request201)

request202 = HTTPRequest(url=url0, headers=headers1)
request202 = Test(202, 'GET index.htm').wrap(request202)

request301 = HTTPRequest(url=url0, headers=headers2)
request301 = Test(301, 'GET data.json').wrap(request301)

request401 = HTTPRequest(url=url0, headers=headers2)
request401 = Test(401, 'GET dsState.json').wrap(request401)

request501 = HTTPRequest(url=url0, headers=headers3)
request501 = Test(501, 'GET task_summary.jsp').wrap(request501)

request601 = HTTPRequest(url=url0, headers=headers3)
request601 = Test(601, 'GET notifications.jsp').wrap(request601)

request701 = HTTPRequest(url=url0, headers=headers3)
request701 = Test(701, 'GET instance_status_cnt.jsp').wrap(request701)

request801 = HTTPRequest(url=url0, headers=headers3)
request801 = Test(801, 'GET avg_completion_time.jsp').wrap(request801)

request901 = HTTPRequest(url=url0, headers=headers3)
request901 = Test(901, 'GET ws_response_time.jsp').wrap(request901)

request1001 = HTTPRequest(url=url0, headers=headers3)
request1001 = Test(1001, 'GET vacation_summary.jsp').wrap(request1001)

request1101 = HTTPRequest(url=url0, headers=headers3)
request1101 = Test(1101, 'GET user_task_count.jsp').wrap(request1101)

request1102 = HTTPRequest(url=url0)
request1102 = Test(1102, 'GET ui-icons_454545_256x240.png').wrap(request1102)

request1201 = HTTPRequest(url=url0, headers=headers3)
request1201 = Test(1201, 'GET task_summary.jsp').wrap(request1201)

request1301 = HTTPRequest(url=url0, headers=headers3)
request1301 = Test(1301, 'GET avg_completion_time.jsp').wrap(request1301)

request1401 = HTTPRequest(url=url0, headers=headers3)
request1401 = Test(1401, 'GET notifications.jsp').wrap(request1401)

request1402 = HTTPRequest(url=url0)
request1402 = Test(1402, 'GET sort_both.png').wrap(request1402)

request1501 = HTTPRequest(url=url0, headers=headers3)
request1501 = Test(1501, 'GET vacation_summary.jsp').wrap(request1501)

request1601 = HTTPRequest(url=url0, headers=headers3)
request1601 = Test(1601, 'GET user_task_count.jsp').wrap(request1601)

request1701 = HTTPRequest(url=url0, headers=headers3)
request1701 = Test(1701, 'GET instance_status_cnt.jsp').wrap(request1701)

request1801 = HTTPRequest(url=url0, headers=headers3)
request1801 = Test(1801, 'GET ws_response_time.jsp').wrap(request1801)

request1901 = HTTPRequest(url=url0, headers=headers4)
request1901 = Test(1901, 'GET tasks.htm').wrap(request1901)

request1902 = HTTPRequest(url=url0, headers=headers4)
request1902 = Test(1902, 'GET login.htm').wrap(request1902)

request1903 = HTTPRequest(url=url0, headers=headers4)
request1903 = Test(1903, 'GET tasks.htm').wrap(request1903)

request2001 = HTTPRequest(url=url0, headers=headers5)
request2001 = Test(2001, 'GET empty.jsp').wrap(request2001)

request2101 = HTTPRequest(url=url0)
request2101 = Test(2101, 'POST vacation.htm').wrap(request2101)

request2201 = HTTPRequest(url=url0, headers=headers6)
request2201 = Test(2201, 'POST updates.htm').wrap(request2201)

request2301 = HTTPRequest(url=url0, headers=headers6)
request2301 = Test(2301, 'POST updates.htm').wrap(request2301)

request2401 = HTTPRequest(url=url0, headers=headers6)
request2401 = Test(2401, 'POST updates.htm').wrap(request2401)

request2501 = HTTPRequest(url=url0, headers=headers5)
request2501 = Test(2501, 'GET empty.jsp').wrap(request2501)

request2601 = HTTPRequest(url=url0, headers=headers6)
request2601 = Test(2601, 'POST updates.htm').wrap(request2601)

request2701 = HTTPRequest(url=url0, headers=headers6)
request2701 = Test(2701, 'POST updates.htm').wrap(request2701)

request2801 = HTTPRequest(url=url0, headers=headers5)
request2801 = Test(2801, 'GET ServerLaunch.html').wrap(request2801)

request2901 = HTTPRequest(url=url0, headers=headers7)
request2901 = Test(2901, 'GET config.xml').wrap(request2901)

request2902 = HTTPRequest(url=url0)
request2902 = Test(2902, 'GET style.css').wrap(request2902)

request3001 = HTTPRequest(url=url0, headers=headers7)
request3001 = Test(3001, 'GET appCanvas.xml').wrap(request3001)

request3101 = HTTPRequest(url=url0, headers=headers7)
request3101 = Test(3101, 'GET translations.xml').wrap(request3101)

request3102 = HTTPRequest(url=url0, headers=headers8)
request3102 = Test(3102, 'GET Packages.js').wrap(request3102)

request3103 = HTTPRequest(url=url0, headers=headers8)
request3103 = Test(3103, 'GET logic.js').wrap(request3103)

request3104 = HTTPRequest(url=url0, headers=headers9)
request3104 = Test(3104, 'GET attachments.gif').wrap(request3104)

request3105 = HTTPRequest(url=url0, headers=headers9)
request3105 = Test(3105, 'GET close.png').wrap(request3105)

request3106 = HTTPRequest(url=url0, headers=headers9)
request3106 = Test(3106, 'GET error.gif').wrap(request3106)

request3201 = HTTPRequest(url=url0, headers=headers7)
request3201 = Test(3201, 'GET TaskManagementServicesMapping.xml').wrap(request3201)

request3301 = HTTPRequest(url=url0, headers=headers7)
request3301 = Test(3301, 'GET Tidy.xsl').wrap(request3301)

request3401 = HTTPRequest(url=url0, headers=headers10)
request3401 = Test(3401, 'POST validation').wrap(request3401)

# Insert a comment and press enteAr
# Creating PA Tak from PIPA
request3501 = HTTPRequest(url=url0, headers=headers7)
request3501 = Test(3501, 'GET TaskManagementServicesMapping.xml').wrap(request3501)

request3601 = HTTPRequest(url=url0, headers=headers7)
request3601 = Test(3601, 'GET FormModelMapping.xml').wrap(request3601)

request3701 = HTTPRequest(url=url0, headers=headers10)
request3701 = Test(3701, 'POST validation').wrap(request3701)

request3801 = HTTPRequest(url=url0, headers=headers7)
request3801 = Test(3801, 'GET empty.jsp').wrap(request3801)

request3901 = HTTPRequest(url=url0, headers=headers6)
request3901 = Test(3901, 'POST updates.htm').wrap(request3901)

request4001 = HTTPRequest(url=url0, headers=headers5)
request4001 = Test(4001, 'GET ServerLaunch.html').wrap(request4001)

request4101 = HTTPRequest(url=url0, headers=headers11)
request4101 = Test(4101, 'GET config.xml').wrap(request4101)

request4102 = HTTPRequest(url=url0)
request4102 = Test(4102, 'GET style.css').wrap(request4102)

request4201 = HTTPRequest(url=url0, headers=headers11)
request4201 = Test(4201, 'GET translations.xml').wrap(request4201)

request4301 = HTTPRequest(url=url0, headers=headers11)
request4301 = Test(4301, 'GET appCanvas.xml').wrap(request4301)

request4302 = HTTPRequest(url=url0, headers=headers12)
request4302 = Test(4302, 'GET Packages.js').wrap(request4302)

request4303 = HTTPRequest(url=url0, headers=headers12)
request4303 = Test(4303, 'GET logic.js').wrap(request4303)

request4304 = HTTPRequest(url=url0, headers=headers13)
request4304 = Test(4304, 'GET attachments.gif').wrap(request4304)

request4305 = HTTPRequest(url=url0, headers=headers13)
request4305 = Test(4305, 'GET close.png').wrap(request4305)

request4306 = HTTPRequest(url=url0, headers=headers13)
request4306 = Test(4306, 'GET error.gif').wrap(request4306)

request4401 = HTTPRequest(url=url0, headers=headers11)
request4401 = Test(4401, 'GET TaskManagementServicesMapping.xml').wrap(request4401)

request4501 = HTTPRequest(url=url0, headers=headers11)
request4501 = Test(4501, 'GET Tidy.xsl').wrap(request4501)

request4601 = HTTPRequest(url=url0, headers=headers14)
request4601 = Test(4601, 'POST validation').wrap(request4601)

# Subtrating Dates PIPA TAsk
request4701 = HTTPRequest(url=url0, headers=headers11)
request4701 = Test(4701, 'GET TaskManagementServicesMapping.xml').wrap(request4701)

request4801 = HTTPRequest(url=url0, headers=headers11)
request4801 = Test(4801, 'GET FormModelMapping.xml').wrap(request4801)

request4901 = HTTPRequest(url=url0, headers=headers14)
request4901 = Test(4901, 'POST validation').wrap(request4901)

request5001 = HTTPRequest(url=url0, headers=headers11)
request5001 = Test(5001, 'GET empty.jsp').wrap(request5001)

request5101 = HTTPRequest(url=url0, headers=headers6)
request5101 = Test(5101, 'POST updates.htm').wrap(request5101)

request5201 = HTTPRequest(url=url0, headers=headers6)
request5201 = Test(5201, 'POST updates.htm').wrap(request5201)

# completing PA TAsk Subtract Dates
request5301 = HTTPRequest(url=url0, headers=headers5)
request5301 = Test(5301, 'GET ServerLaunch.html').wrap(request5301)

request5401 = HTTPRequest(url=url0, headers=headers15)
request5401 = Test(5401, 'GET config.xml').wrap(request5401)

request5402 = HTTPRequest(url=url0)
request5402 = Test(5402, 'GET style.css').wrap(request5402)

request5501 = HTTPRequest(url=url0, headers=headers15)
request5501 = Test(5501, 'GET translations.xml').wrap(request5501)

request5601 = HTTPRequest(url=url0, headers=headers15)
request5601 = Test(5601, 'GET appCanvas.xml').wrap(request5601)

request5602 = HTTPRequest(url=url0, headers=headers16)
request5602 = Test(5602, 'GET Packages.js').wrap(request5602)

request5603 = HTTPRequest(url=url0, headers=headers16)
request5603 = Test(5603, 'GET logic.js').wrap(request5603)

request5604 = HTTPRequest(url=url0, headers=headers17)
request5604 = Test(5604, 'GET attachments.gif').wrap(request5604)

request5605 = HTTPRequest(url=url0, headers=headers17)
request5605 = Test(5605, 'GET close.png').wrap(request5605)

request5606 = HTTPRequest(url=url0, headers=headers17)
request5606 = Test(5606, 'GET error.gif').wrap(request5606)

request5701 = HTTPRequest(url=url0, headers=headers15)
request5701 = Test(5701, 'GET TaskManagementServicesMapping.xml').wrap(request5701)

request5801 = HTTPRequest(url=url0, headers=headers15)
request5801 = Test(5801, 'GET Tidy.xsl').wrap(request5801)

request5901 = HTTPRequest(url=url0, headers=headers18)
request5901 = Test(5901, 'POST validation').wrap(request5901)

request6001 = HTTPRequest(url=url0, headers=headers15)
request6001 = Test(6001, 'GET FormModelMapping.xml').wrap(request6001)

request6101 = HTTPRequest(url=url0, headers=headers15)
request6101 = Test(6101, 'GET TaskManagerProcessMapping.xml').wrap(request6101)

request6201 = HTTPRequest(url=url0, headers=headers15)
request6201 = Test(6201, 'GET FormModelMapping.xml').wrap(request6201)

request6301 = HTTPRequest(url=url0, headers=headers18)
request6301 = Test(6301, 'POST validation').wrap(request6301)

request6401 = HTTPRequest(url=url0, headers=headers15)
request6401 = Test(6401, 'GET empty.jsp').wrap(request6401)

request6501 = HTTPRequest(url=url0, headers=headers6)
request6501 = Test(6501, 'POST updates.htm').wrap(request6501)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET / (requests 101-102)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request101.GET('/')

    request102.GET('/login.htm')
    self.token_actionName = \
      httpUtilities.valueFromHiddenInput('actionName') # 'logIn'

    return result

  def page2(self):
    """POST login.htm (requests 201-202)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request201.POST('/login.htm',
      ( NVPair('actionName', self.token_actionName),
        NVPair('username', 'admin'),
        NVPair('password', 'changeit'),
        NVPair('submit', 'Login'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    grinder.sleep(32)
    request202.GET('/index.htm')
    self.token_accessible = \
      httpUtilities.valueFromHiddenInput('accessible') # ''

    return result

  def page3(self):
    """GET data.json (request 301)."""
    self.token_filter = \
      '1d'
    self.token__ = \
      '1355138650720'
    result = request301.GET('/data.json' +
      '?filter=' +
      self.token_filter +
      '&_=' +
      self.token__)

    return result

  def page4(self):
    """GET dsState.json (request 401)."""
    self.token_action = \
      'getState'
    self.token_ignore_cache = \
      '1355138650884'
    result = request401.GET('/dsState.json' +
      '?action=' +
      self.token_action +
      '&ignore_cache=' +
      self.token_ignore_cache)

    return result

  def page5(self):
    """GET task_summary.jsp (request 501)."""
    result = request501.GET('/widgets/task_summary.jsp')

    return result

  def page6(self):
    """GET notifications.jsp (request 601)."""
    result = request601.GET('/widgets/notifications.jsp')

    return result

  def page7(self):
    """GET instance_status_cnt.jsp (request 701)."""
    result = request701.GET('/widgets/instance_status_cnt.jsp')

    return result

  def page8(self):
    """GET avg_completion_time.jsp (request 801)."""
    result = request801.GET('/widgets/avg_completion_time.jsp')

    return result

  def page9(self):
    """GET ws_response_time.jsp (request 901)."""
    result = request901.GET('/widgets/ws_response_time.jsp')

    return result

  def page10(self):
    """GET vacation_summary.jsp (request 1001)."""
    result = request1001.GET('/widgets/vacation_summary.jsp')

    return result

  def page11(self):
    """GET user_task_count.jsp (requests 1101-1102)."""
    result = request1101.GET('/widgets/user_task_count.jsp')

    request1102.GET('/images/ui-icons_454545_256x240.png', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://titan:8080/style/plugin/jquery.ui.theme.css'), ))

    return result

  def page12(self):
    """GET task_summary.jsp (request 1201)."""
    result = request1201.GET('/widgets/task_summary.jsp')

    return result

  def page13(self):
    """GET avg_completion_time.jsp (request 1301)."""
    result = request1301.GET('/widgets/avg_completion_time.jsp')

    return result

  def page14(self):
    """GET notifications.jsp (requests 1401-1402)."""
    result = request1401.GET('/widgets/notifications.jsp')

    request1402.GET('/images/sort_both.png', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://titan:8080/style/plugin/jquery.dataTables.css'), ))

    return result

  def page15(self):
    """GET vacation_summary.jsp (request 1501)."""
    result = request1501.GET('/widgets/vacation_summary.jsp')

    return result

  def page16(self):
    """GET user_task_count.jsp (request 1601)."""
    result = request1601.GET('/widgets/user_task_count.jsp')

    return result

  def page17(self):
    """GET instance_status_cnt.jsp (request 1701)."""
    result = request1701.GET('/widgets/instance_status_cnt.jsp')

    return result

  def page18(self):
    """GET ws_response_time.jsp (request 1801)."""
    result = request1801.GET('/widgets/ws_response_time.jsp')

    return result

  def page19(self):
    """GET tasks.htm (requests 1901-1903)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request1901.GET('/ui-fw/tasks.htm')

    grinder.sleep(209)
    
    # Expecting 302 'Moved Temporarily'
    request1902.GET('/ui-fw/login.htm')

    grinder.sleep(105)
    request1903.GET('/ui-fw/tasks.htm' +
      '?null')
    self.token_token = \
      httpUtilities.valueFromBodyURI('token') # 'VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlz...'
    self.token_actionName = \
      httpUtilities.valueFromHiddenInput('actionName') # ''
    self.token_formURL = \
      httpUtilities.valueFromHiddenInput('formURL') # ''
    self.token_taskType = \
      httpUtilities.valueFromHiddenInput('taskType') # ''
    self.token_isViewTask = \
      httpUtilities.valueFromHiddenInput('isViewTask') # ''
    self.token_searchUser = \
      httpUtilities.valueFromHiddenInput('searchUser') # 'null'
    self.token_currTab = \
      httpUtilities.valueFromHiddenInput('currTab') # ''

    return result

  def page20(self):
    """GET empty.jsp (request 2001)."""
    result = request2001.GET('/ui-fw/script/empty.jsp')

    return result

  def page21(self):
    """POST vacation.htm (request 2101)."""
    result = request2101.POST('/ui-fw/vacation.htm',
      ( NVPair('action', 'Validate'), ),
      ( NVPair('Accept', 'application/json, text/javascript, */*; q=0.01'),
        NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
        NVPair('Referer', 'http://titan:8080/ui-fw/tasks.htm?null'),
        NVPair('Cache-Control', 'no-cache'), ))

    return result

  def page22(self):
    """POST updates.htm (request 2201)."""
    result = request2201.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 28 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '11d1def534ea1be0:-22d659cb:13b835e25e8:-...'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'PATask'
    # 28 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # 'http://localhost:8080/wds/AbsenceRequest...'
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.
    self.token_user = \
      httpUtilities.valueFromBodyURI('user') # 'intalio\\admin'
    self.token_claimTaskOnOpen = \
      httpUtilities.valueFromBodyURI('claimTaskOnOpen') # 'false'

    return result

  def page23(self):
    """POST updates.htm (request 2301)."""
    result = request2301.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'Notification'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 29 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # 'notify-L571-KMYK-R1JS-7XDM'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'Notification'
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/RepeatEvery_PXEI_897/Forms/n...'
    # 2 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.
    # 1 different values for token_user found in response; the first matched
    # the last known value of token_user - don't update the variable.

    return result

  def page24(self):
    """POST updates.htm (request 2401)."""
    result = request2401.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PIPATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 22 different values for token_id found in response; the first matched
    # the last known value of token_id - don't update the variable.
    # 31 different values for token_type found in response; the first matched
    # the last known value of token_type - don't update the variable.
    # 33 different values for token_url found in response; the first matched
    # the last known value of token_url - don't update the variable.
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page25(self):
    """GET empty.jsp (request 2501)."""
    result = request2501.GET('/ui-fw/script/empty.jsp')

    return result

  def page26(self):
    """POST updates.htm (request 2601)."""
    result = request2601.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 27 different values for token_id found in response; the first matched
    # the last known value of token_id - don't update the variable.
    # 27 different values for token_url found in response; the first matched
    # the last known value of token_url - don't update the variable.
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page27(self):
    """POST updates.htm (request 2701)."""
    result = request2701.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PIPATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 23 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # 'f1e71b24-a117-4cef-bcc8-aa2899e6e240'
    # 13 different values for token_type found in response, using the first one.
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'PIPATask'
    # 34 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/AjaxTesting/form.gi/IntalioI...'
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page28(self):
    """GET ServerLaunch.html (request 2801)."""
    result = request2801.GET('/gi/apppath/AjaxTesting/form.gi/IntalioInternal/ServerLaunch.html' +
      '?id=' +
      self.token_id +
      '&type=' +
      self.token_type +
      '&url=' +
      self.token_url +
      '&token=' +
      self.token_token +
      '&user=' +
      self.token_user +
      '&claimTaskOnOpen=' +
      self.token_claimTaskOnOpen)

    return result

  def page29(self):
    """GET config.xml (requests 2901-2902)."""
    result = request2901.GET('/gi/apppath/AjaxTesting/form.gi/config.xml')

    grinder.sleep(113)
    request2902.GET('/gi/apppath/AjaxTesting/form.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxTesting/form.gi/IntalioInternal/ServerLaunch.html?id=f1e71b24-a117-4cef-bcc8-aa2899e6e240&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxTesting%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page30(self):
    """GET appCanvas.xml (request 3001)."""
    result = request3001.GET('/gi/apppath/AjaxTesting/form.gi/components/appCanvas.xml')

    return result

  def page31(self):
    """GET translations.xml (requests 3101-3106)."""
    result = request3101.GET('/gi/apppath/AjaxTesting/form.gi/jss/translations.xml')

    grinder.sleep(65)
    request3102.GET('/gi/apppath/AjaxTesting/form.gi/IntalioInternal/Packages.js')
    self.token_imgsrc = \
      httpUtilities.valueFromBodyURI('<img src') # ''
    self.token_ahref = \
      httpUtilities.valueFromBodyURI('<a href') # ''

    grinder.sleep(47)
    request3103.GET('/gi/apppath/AjaxTesting/form.gi/js/logic.js')

    grinder.sleep(128)
    request3104.GET('/gi/apppath/AjaxTesting/form.gi/images/attachments.gif')

    request3105.GET('/gi/apppath/AjaxTesting/form.gi/images/close.png')

    request3106.GET('/gi/apppath/AjaxTesting/form.gi/images/error.gif')

    return result

  def page32(self):
    """GET TaskManagementServicesMapping.xml (request 3201)."""
    result = request3201.GET('/gi/apppath/AjaxTesting/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page33(self):
    """GET Tidy.xsl (request 3301)."""
    result = request3301.GET('/gi/apppath/AjaxTesting/form.gi/IntalioInternal/Tidy.xsl')

    return result

  def page34(self):
    """POST validation (request 3401)."""
    result = request3401.POST('/gi/validation',
      ( NVPair('assembly', 'AjaxTesting'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>f1e71b24-a117-4cef-bcc8-aa2899e6e240</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page35(self):
    """GET TaskManagementServicesMapping.xml (request 3501)."""
    result = request3501.GET('/gi/apppath/AjaxTesting/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page36(self):
    """GET FormModelMapping.xml (request 3601)."""
    result = request3601.GET('/gi/apppath/AjaxTesting/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page37(self):
    """POST validation (request 3701)."""
    result = request3701.POST('/gi/validation',
      ( NVPair('assembly', 'AjaxTesting'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:initRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>f1e71b24-a117-4cef-bcc8-aa2899e6e240</jsx1:taskId><jsx1:input><a0:FormModel xmlns:a0=\"http://www.intalio.com/gi/form.gi\"><name>Khyati</name></a0:FormModel></jsx1:input><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO</jsx1:participantToken><jsx1:formUrl>/gi/apppath/AjaxTesting/form.gi/IntalioInternal/ServerLaunch.html</jsx1:formUrl></jsx1:initRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page38(self):
    """GET empty.jsp (request 3801)."""
    result = request3801.GET('/ui-fw/script/empty.jsp')

    return result

  def page39(self):
    """POST updates.htm (request 3901)."""
    result = request3901.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PIPATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 23 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # 'f1e71b24-a117-4cef-bcc8-aa2899e6e240'
    # 13 different values for token_type found in response, using the first one.
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'PIPATask'
    # 34 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/AjaxTesting/form.gi/IntalioI...'
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page40(self):
    """GET ServerLaunch.html (request 4001)."""
    self.token_id = \
      'f973951f-16e0-459e-af0a-f2aaf6e8964b'
    self.token_url = \
      '/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html'
    result = request4001.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html' +
      '?id=' +
      self.token_id +
      '&type=' +
      self.token_type +
      '&url=' +
      self.token_url +
      '&token=' +
      self.token_token +
      '&user=' +
      self.token_user +
      '&claimTaskOnOpen=' +
      self.token_claimTaskOnOpen)

    return result

  def page41(self):
    """GET config.xml (requests 4101-4102)."""
    result = request4101.GET('/gi/apppath/SubstarctDates/form.gi/config.xml')

    grinder.sleep(75)
    request4102.GET('/gi/apppath/SubstarctDates/form.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=f973951f-16e0-459e-af0a-f2aaf6e8964b&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page42(self):
    """GET translations.xml (request 4201)."""
    result = request4201.GET('/gi/apppath/SubstarctDates/form.gi/jss/translations.xml')

    return result

  def page43(self):
    """GET appCanvas.xml (requests 4301-4306)."""
    result = request4301.GET('/gi/apppath/SubstarctDates/form.gi/components/appCanvas.xml')

    grinder.sleep(51)
    request4302.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/Packages.js')

    grinder.sleep(38)
    request4303.GET('/gi/apppath/SubstarctDates/form.gi/js/logic.js')

    grinder.sleep(210)
    request4304.GET('/gi/apppath/SubstarctDates/form.gi/images/attachments.gif')

    request4305.GET('/gi/apppath/SubstarctDates/form.gi/images/close.png')

    request4306.GET('/gi/apppath/SubstarctDates/form.gi/images/error.gif')

    return result

  def page44(self):
    """GET TaskManagementServicesMapping.xml (request 4401)."""
    result = request4401.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page45(self):
    """GET Tidy.xsl (request 4501)."""
    result = request4501.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/Tidy.xsl')

    return result

  def page46(self):
    """POST validation (request 4601)."""
    result = request4601.POST('/gi/validation',
      ( NVPair('assembly', 'SubstarctDates'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>f973951f-16e0-459e-af0a-f2aaf6e8964b</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page47(self):
    """GET TaskManagementServicesMapping.xml (request 4701)."""
    result = request4701.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page48(self):
    """GET FormModelMapping.xml (request 4801)."""
    result = request4801.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page49(self):
    """POST validation (request 4901)."""
    result = request4901.POST('/gi/validation',
      ( NVPair('assembly', 'SubstarctDates'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:initRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>f973951f-16e0-459e-af0a-f2aaf6e8964b</jsx1:taskId><jsx1:input><a0:FormModel xmlns:a0=\"http://www.intalio.com/gi/form.gi\"><date1>2012-12-12</date1><date2>2012-12-11</date2></a0:FormModel></jsx1:input><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO</jsx1:participantToken><jsx1:formUrl>/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html</jsx1:formUrl></jsx1:initRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page50(self):
    """GET empty.jsp (request 5001)."""
    result = request5001.GET('/ui-fw/script/empty.jsp')

    return result

  def page51(self):
    """POST updates.htm (request 5101)."""
    result = request5101.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PIPATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 23 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # 'f1e71b24-a117-4cef-bcc8-aa2899e6e240'
    # 12 different values for token_type found in response; the first matched
    # the last known value of token_type - don't update the variable.
    # 34 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/AjaxTesting/form.gi/IntalioI...'
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page52(self):
    """POST updates.htm (request 5201)."""
    result = request5201.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 31 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '11d1def534ea1be0:-22d659cb:13b835e25e8:-...'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'PATask'
    # 25 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/SubstarctDates/form.gi/Intal...'
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page53(self):
    """GET ServerLaunch.html (request 5301)."""
    result = request5301.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html' +
      '?id=' +
      self.token_id +
      '&type=' +
      self.token_type +
      '&url=' +
      self.token_url +
      '&token=' +
      self.token_token +
      '&user=' +
      self.token_user +
      '&claimTaskOnOpen=' +
      self.token_claimTaskOnOpen)

    return result

  def page54(self):
    """GET config.xml (requests 5401-5402)."""
    result = request5401.GET('/gi/apppath/SubstarctDates/form.gi/config.xml')

    grinder.sleep(118)
    request5402.GET('/gi/apppath/SubstarctDates/form.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-134d127.0.0.166&type=PATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page55(self):
    """GET translations.xml (request 5501)."""
    result = request5501.GET('/gi/apppath/SubstarctDates/form.gi/jss/translations.xml')

    return result

  def page56(self):
    """GET appCanvas.xml (requests 5601-5606)."""
    result = request5601.GET('/gi/apppath/SubstarctDates/form.gi/components/appCanvas.xml')

    grinder.sleep(81)
    request5602.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/Packages.js')

    grinder.sleep(52)
    request5603.GET('/gi/apppath/SubstarctDates/form.gi/js/logic.js')

    grinder.sleep(163)
    request5604.GET('/gi/apppath/SubstarctDates/form.gi/images/attachments.gif')

    request5605.GET('/gi/apppath/SubstarctDates/form.gi/images/close.png')

    request5606.GET('/gi/apppath/SubstarctDates/form.gi/images/error.gif')

    return result

  def page57(self):
    """GET TaskManagementServicesMapping.xml (request 5701)."""
    result = request5701.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page58(self):
    """GET Tidy.xsl (request 5801)."""
    result = request5801.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/Tidy.xsl')

    return result

  def page59(self):
    """POST validation (request 5901)."""
    result = request5901.POST('/gi/validation',
      ( NVPair('assembly', 'SubstarctDates'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>11d1def534ea1be0:-22d659cb:13b835e25e8:-134d127.0.0.166</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page60(self):
    """GET FormModelMapping.xml (request 6001)."""
    result = request6001.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page61(self):
    """GET TaskManagerProcessMapping.xml (request 6101)."""
    result = request6101.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/TaskManagerProcessMapping.xml')

    return result

  def page62(self):
    """GET FormModelMapping.xml (request 6201)."""
    result = request6201.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page63(self):
    """POST validation (request 6301)."""
    result = request6301.POST('/gi/validation',
      ( NVPair('assembly', 'SubstarctDates'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:completeTaskRequest xmlns:jsx1=\"http://www.intalio.com/bpms/workflow/ib4p_20051115\"><jsx1:taskMetaData><jsx1:taskId>11d1def534ea1be0:-22d659cb:13b835e25e8:-134d127.0.0.166</jsx1:taskId></jsx1:taskMetaData><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTEzODYzMDE0MyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09LTEzMDU2OTQxMjQ2MTU4OTkzODkmJnRpbWVzdGFtcD09MTM1NTEzODYzMDE0MyYmZGlnZXN0PT03aFhIUkpKdWxVS2tucWV1d0lJSEpQdUNqYVU9JiYmJlRPS0VO</jsx1:participantToken><jsx1:user>intalio\\admin</jsx1:user><jsx1:taskOutput><a0:FormModel xmlns:a0=\"http://www.intalio.com/gi/form.gi\"><result>P1D</result></a0:FormModel></jsx1:taskOutput></jsx1:completeTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page64(self):
    """GET empty.jsp (request 6401)."""
    result = request6401.GET('/ui-fw/script/empty.jsp')

    return result

  def page65(self):
    """POST updates.htm (request 6501)."""
    result = request6501.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 28 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '11d1def534ea1be0:-22d659cb:13b835e25e8:-...'
    # 28 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # 'http://localhost:8080/wds/AbsenceRequest...'
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    self.page1()      # GET / (requests 101-102)

    grinder.sleep(1635)
    self.page2()      # POST login.htm (requests 201-202)

    grinder.sleep(227)
    self.page3()      # GET data.json (request 301)

    grinder.sleep(56)
    self.page4()      # GET dsState.json (request 401)

    grinder.sleep(112)
    self.page5()      # GET task_summary.jsp (request 501)
    self.page6()      # GET notifications.jsp (request 601)
    self.page7()      # GET instance_status_cnt.jsp (request 701)
    self.page8()      # GET avg_completion_time.jsp (request 801)
    self.page9()      # GET ws_response_time.jsp (request 901)
    self.page10()     # GET vacation_summary.jsp (request 1001)
    self.page11()     # GET user_task_count.jsp (requests 1101-1102)

    grinder.sleep(60)
    self.page12()     # GET task_summary.jsp (request 1201)

    grinder.sleep(149)
    self.page13()     # GET avg_completion_time.jsp (request 1301)
    self.page14()     # GET notifications.jsp (requests 1401-1402)
    self.page15()     # GET vacation_summary.jsp (request 1501)
    self.page16()     # GET user_task_count.jsp (request 1601)

    grinder.sleep(294)
    self.page17()     # GET instance_status_cnt.jsp (request 1701)
    self.page18()     # GET ws_response_time.jsp (request 1801)

    grinder.sleep(224)
    self.page19()     # GET tasks.htm (requests 1901-1903)

    grinder.sleep(160)
    self.page20()     # GET empty.jsp (request 2001)

    grinder.sleep(15)
    self.page21()     # POST vacation.htm (request 2101)

    grinder.sleep(105)
    self.page22()     # POST updates.htm (request 2201)
    self.page23()     # POST updates.htm (request 2301)

    grinder.sleep(31)
    self.page24()     # POST updates.htm (request 2401)

    grinder.sleep(264)
    self.page25()     # GET empty.jsp (request 2501)

    grinder.sleep(118)
    self.page26()     # POST updates.htm (request 2601)

    grinder.sleep(2167)
    self.page27()     # POST updates.htm (request 2701)

    grinder.sleep(1022)
    self.page28()     # GET ServerLaunch.html (request 2801)

    grinder.sleep(111)
    self.page29()     # GET config.xml (requests 2901-2902)

    grinder.sleep(12)
    self.page30()     # GET appCanvas.xml (request 3001)
    self.page31()     # GET translations.xml (requests 3101-3106)
    self.page32()     # GET TaskManagementServicesMapping.xml (request 3201)

    grinder.sleep(59)
    self.page33()     # GET Tidy.xsl (request 3301)
    self.page34()     # POST validation (request 3401)

    grinder.sleep(37046)
    self.page35()     # GET TaskManagementServicesMapping.xml (request 3501)

    grinder.sleep(60)
    self.page36()     # GET FormModelMapping.xml (request 3601)

    grinder.sleep(16)
    self.page37()     # POST validation (request 3701)

    grinder.sleep(17)
    self.page38()     # GET empty.jsp (request 3801)

    grinder.sleep(33)
    self.page39()     # POST updates.htm (request 3901)

    grinder.sleep(5420)
    self.page40()     # GET ServerLaunch.html (request 4001)

    grinder.sleep(101)
    self.page41()     # GET config.xml (requests 4101-4102)
    self.page42()     # GET translations.xml (request 4201)
    self.page43()     # GET appCanvas.xml (requests 4301-4306)
    self.page44()     # GET TaskManagementServicesMapping.xml (request 4401)

    grinder.sleep(57)
    self.page45()     # GET Tidy.xsl (request 4501)
    self.page46()     # POST validation (request 4601)

    grinder.sleep(23602)
    self.page47()     # GET TaskManagementServicesMapping.xml (request 4701)

    grinder.sleep(66)
    self.page48()     # GET FormModelMapping.xml (request 4801)

    grinder.sleep(54)
    self.page49()     # POST validation (request 4901)

    grinder.sleep(13)
    self.page50()     # GET empty.jsp (request 5001)

    grinder.sleep(31)
    self.page51()     # POST updates.htm (request 5101)

    grinder.sleep(1461)
    self.page52()     # POST updates.htm (request 5201)

    grinder.sleep(13934)
    self.page53()     # GET ServerLaunch.html (request 5301)

    grinder.sleep(118)
    self.page54()     # GET config.xml (requests 5401-5402)
    self.page55()     # GET translations.xml (request 5501)
    self.page56()     # GET appCanvas.xml (requests 5601-5606)
    self.page57()     # GET TaskManagementServicesMapping.xml (request 5701)

    grinder.sleep(62)
    self.page58()     # GET Tidy.xsl (request 5801)
    self.page59()     # POST validation (request 5901)

    grinder.sleep(13)
    self.page60()     # GET FormModelMapping.xml (request 6001)

    grinder.sleep(2651)
    self.page61()     # GET TaskManagerProcessMapping.xml (request 6101)

    grinder.sleep(35)
    self.page62()     # GET FormModelMapping.xml (request 6201)

    grinder.sleep(52)
    self.page63()     # POST validation (request 6301)

    grinder.sleep(16)
    self.page64()     # GET empty.jsp (request 6401)

    grinder.sleep(39)
    self.page65()     # POST updates.htm (request 6501)

def instrumentMethod(test, method_name, c=TestRunner):
  """Instrument a method with the given Test."""
  unadorned = getattr(c, method_name)
  import new
  method = new.instancemethod(test.wrap(unadorned), None, c)
  setattr(c, method_name, method)

# Replace each method with an instrumented version.
# You can call the unadorned method using self.page1.__target__().
instrumentMethod(Test(100, 'Page 1'), 'page1')
instrumentMethod(Test(200, 'Page 2'), 'page2')
instrumentMethod(Test(300, 'Page 3'), 'page3')
instrumentMethod(Test(400, 'Page 4'), 'page4')
instrumentMethod(Test(500, 'Page 5'), 'page5')
instrumentMethod(Test(600, 'Page 6'), 'page6')
instrumentMethod(Test(700, 'Page 7'), 'page7')
instrumentMethod(Test(800, 'Page 8'), 'page8')
instrumentMethod(Test(900, 'Page 9'), 'page9')
instrumentMethod(Test(1000, 'Page 10'), 'page10')
instrumentMethod(Test(1100, 'Page 11'), 'page11')
instrumentMethod(Test(1200, 'Page 12'), 'page12')
instrumentMethod(Test(1300, 'Page 13'), 'page13')
instrumentMethod(Test(1400, 'Page 14'), 'page14')
instrumentMethod(Test(1500, 'Page 15'), 'page15')
instrumentMethod(Test(1600, 'Page 16'), 'page16')
instrumentMethod(Test(1700, 'Page 17'), 'page17')
instrumentMethod(Test(1800, 'Page 18'), 'page18')
instrumentMethod(Test(1900, 'Page 19'), 'page19')
instrumentMethod(Test(2000, 'Page 20'), 'page20')
instrumentMethod(Test(2100, 'Page 21'), 'page21')
instrumentMethod(Test(2200, 'Page 22'), 'page22')
instrumentMethod(Test(2300, 'Page 23'), 'page23')
instrumentMethod(Test(2400, 'Page 24'), 'page24')
instrumentMethod(Test(2500, 'Page 25'), 'page25')
instrumentMethod(Test(2600, 'Page 26'), 'page26')
instrumentMethod(Test(2700, 'Page 27'), 'page27')
instrumentMethod(Test(2800, 'Page 28'), 'page28')
instrumentMethod(Test(2900, 'Page 29'), 'page29')
instrumentMethod(Test(3000, 'Page 30'), 'page30')
instrumentMethod(Test(3100, 'Page 31'), 'page31')
instrumentMethod(Test(3200, 'Page 32'), 'page32')
instrumentMethod(Test(3300, 'Page 33'), 'page33')
instrumentMethod(Test(3400, 'Page 34'), 'page34')
instrumentMethod(Test(3500, 'Page 35'), 'page35')
instrumentMethod(Test(3600, 'Page 36'), 'page36')
instrumentMethod(Test(3700, 'Page 37'), 'page37')
instrumentMethod(Test(3800, 'Page 38'), 'page38')
instrumentMethod(Test(3900, 'Page 39'), 'page39')
instrumentMethod(Test(4000, 'Page 40'), 'page40')
instrumentMethod(Test(4100, 'Page 41'), 'page41')
instrumentMethod(Test(4200, 'Page 42'), 'page42')
instrumentMethod(Test(4300, 'Page 43'), 'page43')
instrumentMethod(Test(4400, 'Page 44'), 'page44')
instrumentMethod(Test(4500, 'Page 45'), 'page45')
instrumentMethod(Test(4600, 'Page 46'), 'page46')
instrumentMethod(Test(4700, 'Page 47'), 'page47')
instrumentMethod(Test(4800, 'Page 48'), 'page48')
instrumentMethod(Test(4900, 'Page 49'), 'page49')
instrumentMethod(Test(5000, 'Page 50'), 'page50')
instrumentMethod(Test(5100, 'Page 51'), 'page51')
instrumentMethod(Test(5200, 'Page 52'), 'page52')
instrumentMethod(Test(5300, 'Page 53'), 'page53')
instrumentMethod(Test(5400, 'Page 54'), 'page54')
instrumentMethod(Test(5500, 'Page 55'), 'page55')
instrumentMethod(Test(5600, 'Page 56'), 'page56')
instrumentMethod(Test(5700, 'Page 57'), 'page57')
instrumentMethod(Test(5800, 'Page 58'), 'page58')
instrumentMethod(Test(5900, 'Page 59'), 'page59')
instrumentMethod(Test(6000, 'Page 60'), 'page60')
instrumentMethod(Test(6100, 'Page 61'), 'page61')
instrumentMethod(Test(6200, 'Page 62'), 'page62')
instrumentMethod(Test(6300, 'Page 63'), 'page63')
instrumentMethod(Test(6400, 'Page 64'), 'page64')
instrumentMethod(Test(6500, 'Page 65'), 'page65')
