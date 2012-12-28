# The Grinder 3.11
# HTTP script recorded by TCPProxy at Dec 20, 2012 12:28:04 PM

from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()

# To use a proxy server, uncomment the next line and set the host and port.
# connectionDefaults.setProxyServer("localhost", 8001)

def createRequest(test, url, headers=None):
    """Create an instrumented HTTPRequest."""
    request = HTTPRequest(url=url)
    if headers: request.headers=headers
    test.record(request, HTTPRequest.getHttpMethodFilter())
    return request

# These definitions at the top level of the file are evaluated once,
# when the worker process is started.

connectionDefaults.defaultHeaders = \
  [ NVPair('Accept-Encoding', 'gzip, deflate'),
    NVPair('Accept-Language', 'en-us,en;q=0.5'),
    NVPair('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0.1'), ]

headers0= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'http://aries:8080/ui-fw/tasks.htm'),
    NVPair('Cache-Control', 'no-cache'), ]

headers1= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://aries:8080/ui-fw/tasks.htm'),
    NVPair('Cache-Control', 'no-cache'), ]

headers2= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://aries:8080/ui-fw/tasks.htm'),
    NVPair('Cache-Control', 'no-cache'), ]

headers3= \
  [ NVPair('Accept', 'application/xml, text/xml, */*; q=0.01'),
    NVPair('Referer', 'http://aries:8080/ui-fw/tasks.htm'),
    NVPair('Cache-Control', 'no-cache'), ]

headers4= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://aries:8080/ui-fw/style/jqueryui/jquery.ui.theme.css'),
    NVPair('Cache-Control', 'no-cache'), ]

headers5= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://aries:8080/ui-fw/style/flexigrid.css'),
    NVPair('Cache-Control', 'no-cache'), ]

headers6= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ]

headers7= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'), ]

headers8= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://ramanujan:8080/style/custom/customLogin.css'), ]

headers9= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://ramanujan:8080/login.htm;jsessionid=13CAD5C8E31C5AB18BE953D1D189E8F9'), ]

headers10= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'http://ramanujan:8080/index.htm'), ]

headers11= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://ramanujan:8080/index.htm'), ]

headers12= \
  [ NVPair('Accept', 'application/json, text/javascript, */*; q=0.01'),
    NVPair('Referer', 'http://ramanujan:8080/index.htm'), ]

headers13= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://ramanujan:8080/style/plugin/jquery.ui.theme.css'), ]

headers14= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://ramanujan:8080/index.htm'), ]

headers15= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'http://ramanujan:8080/ui-fw/tasks.htm?null'), ]

headers16= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://ramanujan:8080/ui-fw/tasks.htm?null'), ]

headers17= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://ramanujan:8080/ui-fw/tasks.htm?null'), ]

headers18= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://ramanujan:8080/ui-fw/style/jqueryui/jquery.ui.theme.css'), ]

headers19= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://ramanujan:8080/ui-fw/style/flexigrid.css'), ]

headers20= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://ramanujan:8080/ui-fw/tasks.htm?null'), ]

headers21= \
  [ NVPair('Accept', 'application/xml, text/xml, */*; q=0.01'),
    NVPair('Referer', 'http://ramanujan:8080/ui-fw/tasks.htm?null'),
    NVPair('Cache-Control', 'no-cache'), ]

headers22= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://ramanujan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=fd035c38-cd69-4d08-8641-99c30472f4d4&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NjcwODQ1OCYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09NzYyNjMyNTA0ODg4ODgzMDI3OCYmdGltZXN0YW1wPT0xMzU1OTg2NzA4NDU4JiZkaWdlc3Q9PWVqeTMvckNTK2M2ZkI3cHB2ZWxZUWFtYWNUQT0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers23= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://ramanujan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=fd035c38-cd69-4d08-8641-99c30472f4d4&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NjcwODQ1OCYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09NzYyNjMyNTA0ODg4ODgzMDI3OCYmdGltZXN0YW1wPT0xMzU1OTg2NzA4NDU4JiZkaWdlc3Q9PWVqeTMvckNTK2M2ZkI3cHB2ZWxZUWFtYWNUQT0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers24= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'http://ramanujan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=fd035c38-cd69-4d08-8641-99c30472f4d4&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NjcwODQ1OCYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09NzYyNjMyNTA0ODg4ODgzMDI3OCYmdGltZXN0YW1wPT0xMzU1OTg2NzA4NDU4JiZkaWdlc3Q9PWVqeTMvckNTK2M2ZkI3cHB2ZWxZUWFtYWNUQT0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers25= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://ramanujan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=fd035c38-cd69-4d08-8641-99c30472f4d4&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NjcwODQ1OCYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09NzYyNjMyNTA0ODg4ODgzMDI3OCYmdGltZXN0YW1wPT0xMzU1OTg2NzA4NDU4JiZkaWdlc3Q9PWVqeTMvckNTK2M2ZkI3cHB2ZWxZUWFtYWNUQT0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers26= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://ramanujan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=fd035c38-cd69-4d08-8641-99c30472f4d4&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NjcwODQ1OCYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09NzYyNjMyNTA0ODg4ODgzMDI3OCYmdGltZXN0YW1wPT0xMzU1OTg2NzA4NDU4JiZkaWdlc3Q9PWVqeTMvckNTK2M2ZkI3cHB2ZWxZUWFtYWNUQT0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers27= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://ramanujan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=26ac8b80354d82d1:-5e64727b:13bb6140d8e:-731e169.254.216.23436&type=PATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NjcwODQ1OCYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09NzYyNjMyNTA0ODg4ODgzMDI3OCYmdGltZXN0YW1wPT0xMzU1OTg2NzA4NDU4JiZkaWdlc3Q9PWVqeTMvckNTK2M2ZkI3cHB2ZWxZUWFtYWNUQT0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers28= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://ramanujan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=26ac8b80354d82d1:-5e64727b:13bb6140d8e:-731e169.254.216.23436&type=PATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NjcwODQ1OCYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09NzYyNjMyNTA0ODg4ODgzMDI3OCYmdGltZXN0YW1wPT0xMzU1OTg2NzA4NDU4JiZkaWdlc3Q9PWVqeTMvckNTK2M2ZkI3cHB2ZWxZUWFtYWNUQT0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers29= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://ramanujan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=26ac8b80354d82d1:-5e64727b:13bb6140d8e:-731e169.254.216.23436&type=PATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NjcwODQ1OCYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09NzYyNjMyNTA0ODg4ODgzMDI3OCYmdGltZXN0YW1wPT0xMzU1OTg2NzA4NDU4JiZkaWdlc3Q9PWVqeTMvckNTK2M2ZkI3cHB2ZWxZUWFtYWNUQT0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers30= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://ramanujan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=26ac8b80354d82d1:-5e64727b:13bb6140d8e:-731e169.254.216.23436&type=PATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NjcwODQ1OCYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09NzYyNjMyNTA0ODg4ODgzMDI3OCYmdGltZXN0YW1wPT0xMzU1OTg2NzA4NDU4JiZkaWdlc3Q9PWVqeTMvckNTK2M2ZkI3cHB2ZWxZUWFtYWNUQT0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

url0 = 'http://aries:8080'
url1 = 'http://ramanujan:8080'

request101 = createRequest(Test(101, 'GET tasks.htm'), url0)

request102 = createRequest(Test(102, 'GET jquery.ui.theme.css'), url0, headers0)

request103 = createRequest(Test(103, 'GET tabs.css'), url0, headers0)

request104 = createRequest(Test(104, 'GET flexigrid.css'), url0, headers0)

request105 = createRequest(Test(105, 'GET ui.dialog.content.css'), url0, headers0)

request106 = createRequest(Test(106, 'GET jquery.alerts.css'), url0, headers0)

request107 = createRequest(Test(107, 'GET jquery.qtip.css'), url0, headers0)

request108 = createRequest(Test(108, 'GET jquery-ui.css'), url0, headers0)

request109 = createRequest(Test(109, 'GET jquery.js'), url0, headers1)

request110 = createRequest(Test(110, 'GET ui-fw.js'), url0, headers1)

request111 = createRequest(Test(111, 'GET jquery-ui.js'), url0, headers1)

request112 = createRequest(Test(112, 'GET jquery-timer.js'), url0, headers1)

request113 = createRequest(Test(113, 'GET jquery.jcorners.js'), url0, headers1)

request114 = createRequest(Test(114, 'GET jquery.demensions.js'), url0, headers1)

request115 = createRequest(Test(115, 'GET jquery.ui.position.js'), url0, headers1)

request116 = createRequest(Test(116, 'GET jtabber.js'), url0, headers1)

request117 = createRequest(Test(117, 'GET jquery.qtip.js'), url0, headers1)

request118 = createRequest(Test(118, 'GET jquery.string.1.0.js'), url0, headers1)

request119 = createRequest(Test(119, 'GET style.css'), url0, headers0)

request120 = createRequest(Test(120, 'GET jqSoapClient.min.js'), url0, headers1)

request121 = createRequest(Test(121, 'GET jquery.ui.datepicker.js'), url0, headers1)

request122 = createRequest(Test(122, 'GET flexigrid.js'), url0, headers1)

request123 = createRequest(Test(123, 'GET jquery.alerts.js'), url0, headers1)

request124 = createRequest(Test(124, 'GET icon.task.png'), url0, headers2)

request125 = createRequest(Test(125, 'GET pdf.png'), url0, headers2)

request126 = createRequest(Test(126, 'GET icon.notification.png'), url0, headers2)

request127 = createRequest(Test(127, 'GET csv.png'), url0, headers2)

request128 = createRequest(Test(128, 'GET ical.png'), url0, headers2)

request129 = createRequest(Test(129, 'GET icon.process.png'), url0, headers2)

request130 = createRequest(Test(130, 'GET logo.png'), url0, headers2)

request201 = createRequest(Test(201, 'POST vacation.htm'), url0)

request301 = createRequest(Test(301, 'POST updates.htm'), url0, headers3)

request401 = createRequest(Test(401, 'POST updates.htm'), url0, headers3)

request501 = createRequest(Test(501, 'POST updates.htm'), url0, headers3)

request502 = createRequest(Test(502, 'GET ui-bg_highlight-soft_100_f6f6f6_1x100.png'), url0, headers4)

request503 = createRequest(Test(503, 'GET ui-icons_666666_256x240.png'), url0, headers4)

request504 = createRequest(Test(504, 'GET ui-bg_flat_75_ffffff_40x100.png'), url0, headers4)

request505 = createRequest(Test(505, 'GET load.png'), url0, headers5)

request506 = createRequest(Test(506, 'GET prev.gif'), url0, headers5)

request507 = createRequest(Test(507, 'GET icon.claim.gif'), url0, headers5)

request508 = createRequest(Test(508, 'GET icon.vacation.gif'), url0, headers5)

request509 = createRequest(Test(509, 'GET icon.delete.gif'), url0, headers5)

request510 = createRequest(Test(510, 'GET icon.skip.gif'), url0, headers5)

request511 = createRequest(Test(511, 'GET icon.edit.gif'), url0, headers5)

request512 = createRequest(Test(512, 'GET fhbg.gif'), url0, headers5)

request513 = createRequest(Test(513, 'GET icon.reassign.gif'), url0, headers5)

request514 = createRequest(Test(514, 'GET icon.export.gif'), url0, headers5)

request515 = createRequest(Test(515, 'GET wbg.gif'), url0, headers5)

request516 = createRequest(Test(516, 'GET magnifier.png'), url0, headers5)

request517 = createRequest(Test(517, 'GET first.gif'), url0, headers5)

request518 = createRequest(Test(518, 'GET next.gif'), url0, headers5)

request519 = createRequest(Test(519, 'GET last.gif'), url0, headers5)

request520 = createRequest(Test(520, 'GET load.gif'), url0, headers5)

request521 = createRequest(Test(521, 'GET ui-bg_highlight-soft_25_0073ea_1x100.png'), url0)

request601 = createRequest(Test(601, 'GET empty.jsp'), url0)

request602 = createRequest(Test(602, 'GET line.gif'), url0, headers5)

request603 = createRequest(Test(603, 'GET icon.notclaimed.gif'), url0, headers2)

request701 = createRequest(Test(701, 'POST updates.htm'), url0, headers3)

request801 = createRequest(Test(801, 'GET /'), url1, headers6)

request802 = createRequest(Test(802, 'GET login.htm'), url1, headers6)

request803 = createRequest(Test(803, 'GET customLogin.css'), url1)

request804 = createRequest(Test(804, 'GET favicon.ico'), url1, headers7)

request805 = createRequest(Test(805, 'GET jquery-1.8.2.js'), url1)

request806 = createRequest(Test(806, 'GET logo.png'), url1)

request807 = createRequest(Test(807, 'GET key.png'), url1, headers8)

request808 = createRequest(Test(808, 'GET user_gray.png'), url1, headers8)

request901 = createRequest(Test(901, 'POST login.htm'), url1, headers9)

request902 = createRequest(Test(902, 'GET index.htm'), url1, headers9)

request903 = createRequest(Test(903, 'GET jquery.ui.theme.css'), url1, headers10)

request904 = createRequest(Test(904, 'GET jquery-ui-1.9.0.css'), url1, headers10)

request905 = createRequest(Test(905, 'GET jquery.dataTables.css'), url1, headers10)

request906 = createRequest(Test(906, 'GET nv.d3.css'), url1, headers10)

request907 = createRequest(Test(907, 'GET jquery.qtip.css'), url1, headers10)

request908 = createRequest(Test(908, 'GET dashboardui.css'), url1, headers10)

request909 = createRequest(Test(909, 'GET jquery-ui.js'), url1, headers11)

request910 = createRequest(Test(910, 'GET jquery.ui.position.js'), url1, headers11)

request911 = createRequest(Test(911, 'GET jquery.dashboard.min.js'), url1, headers11)

request912 = createRequest(Test(912, 'GET jquery.qtip.js'), url1, headers11)

request913 = createRequest(Test(913, 'GET themeroller.js'), url1, headers11)

request914 = createRequest(Test(914, 'GET d3.v2.js'), url1, headers11)

request915 = createRequest(Test(915, 'GET nv.d3.js'), url1, headers11)

request916 = createRequest(Test(916, 'GET tooltip.js'), url1, headers11)

request917 = createRequest(Test(917, 'GET utils.js'), url1, headers11)

request918 = createRequest(Test(918, 'GET axis.js'), url1, headers11)

request919 = createRequest(Test(919, 'GET discreteBar.js'), url1, headers11)

request920 = createRequest(Test(920, 'GET discreteBarChart.js'), url1, headers11)

request921 = createRequest(Test(921, 'GET multiBar.js'), url1, headers11)

request922 = createRequest(Test(922, 'GET multiBarChart.js'), url1, headers11)

request923 = createRequest(Test(923, 'GET legend.js'), url1, headers11)

request924 = createRequest(Test(924, 'GET scatter.js'), url1, headers11)

request925 = createRequest(Test(925, 'GET line.js'), url1, headers11)

request926 = createRequest(Test(926, 'GET pie.js'), url1, headers11)

request927 = createRequest(Test(927, 'GET jquery.dataTables.js'), url1, headers11)

request928 = createRequest(Test(928, 'GET historicalBar.js'), url1, headers11)

request929 = createRequest(Test(929, 'GET pieChart.js'), url1, headers11)

request930 = createRequest(Test(930, 'GET linePlusBarChart.js'), url1, headers11)

request931 = createRequest(Test(931, 'GET multiBarHorizontalChart.js'), url1, headers11)

request932 = createRequest(Test(932, 'GET jquery-dateFormat.js'), url1, headers11)

request933 = createRequest(Test(933, 'GET multiBarHorizontal.js'), url1, headers11)

request934 = createRequest(Test(934, 'GET dashboard.js'), url1, headers11)

request1001 = createRequest(Test(1001, 'GET data.json'), url1, headers12)

request1002 = createRequest(Test(1002, 'GET ui-icons_666666_256x240.png'), url1, headers13)

request1003 = createRequest(Test(1003, 'GET ui-bg_highlight-soft_100_f6f6f6_1x100.png'), url1, headers13)

request1004 = createRequest(Test(1004, 'GET ui-bg_flat_75_ffffff_40x100.png'), url1, headers13)

request1005 = createRequest(Test(1005, 'GET loading.gif'), url1)

request1006 = createRequest(Test(1006, 'GET ui-bg_highlight-soft_50_dddddd_1x100.png'), url1, headers13)

request1101 = createRequest(Test(1101, 'GET templates.html'), url1)

request1201 = createRequest(Test(1201, 'GET dsState.json'), url1, headers12)

request1202 = createRequest(Test(1202, 'GET ui-icons_0073ea_256x240.png'), url1, headers13)

request1203 = createRequest(Test(1203, 'GET ui-bg_highlight-soft_25_0073ea_1x100.png'), url1, headers13)

request1301 = createRequest(Test(1301, 'GET tasks.htm'), url1, headers14)

request1302 = createRequest(Test(1302, 'GET ui-bg_glass_65_ffffff_1x400.png'), url1, headers13)

request1401 = createRequest(Test(1401, 'GET login.htm'), url1, headers14)

request1402 = createRequest(Test(1402, 'GET tasks.htm'), url1, headers14)

request1403 = createRequest(Test(1403, 'GET style.css'), url1, headers15)

request1404 = createRequest(Test(1404, 'GET tabs.css'), url1, headers15)

request1405 = createRequest(Test(1405, 'GET flexigrid.css'), url1, headers15)

request1406 = createRequest(Test(1406, 'GET jquery-ui.css'), url1, headers15)

request1407 = createRequest(Test(1407, 'GET jquery.ui.theme.css'), url1, headers15)

request1408 = createRequest(Test(1408, 'GET jquery.qtip.css'), url1, headers15)

request1409 = createRequest(Test(1409, 'GET jquery.alerts.css'), url1, headers15)

request1410 = createRequest(Test(1410, 'GET ui.dialog.content.css'), url1, headers15)

request1411 = createRequest(Test(1411, 'GET ui-fw.js'), url1, headers16)

request1412 = createRequest(Test(1412, 'GET jquery.js'), url1, headers16)

request1413 = createRequest(Test(1413, 'GET jquery-timer.js'), url1, headers16)

request1414 = createRequest(Test(1414, 'GET jquery-ui.js'), url1, headers16)

request1415 = createRequest(Test(1415, 'GET jquery.jcorners.js'), url1, headers16)

request1416 = createRequest(Test(1416, 'GET jquery.demensions.js'), url1, headers16)

request1417 = createRequest(Test(1417, 'GET jquery.ui.position.js'), url1, headers16)

request1418 = createRequest(Test(1418, 'GET jtabber.js'), url1, headers16)

request1419 = createRequest(Test(1419, 'GET jquery.qtip.js'), url1, headers16)

request1420 = createRequest(Test(1420, 'GET jquery.string.1.0.js'), url1, headers16)

request1421 = createRequest(Test(1421, 'GET jqSoapClient.min.js'), url1, headers16)

request1422 = createRequest(Test(1422, 'GET jquery.ui.datepicker.js'), url1, headers16)

request1423 = createRequest(Test(1423, 'GET jquery.alerts.js'), url1, headers16)

request1424 = createRequest(Test(1424, 'GET flexigrid.js'), url1, headers16)

request1425 = createRequest(Test(1425, 'GET logo.png'), url1, headers17)

request1426 = createRequest(Test(1426, 'GET csv.png'), url1, headers17)

request1427 = createRequest(Test(1427, 'GET ical.png'), url1, headers17)

request1428 = createRequest(Test(1428, 'GET icon.task.png'), url1, headers17)

request1429 = createRequest(Test(1429, 'GET pdf.png'), url1, headers17)

request1430 = createRequest(Test(1430, 'GET icon.process.png'), url1, headers17)

request1431 = createRequest(Test(1431, 'GET icon.notification.png'), url1, headers17)

request1432 = createRequest(Test(1432, 'GET favicon.ico'), url1, headers7)

request1501 = createRequest(Test(1501, 'POST vacation.htm'), url1)

request1502 = createRequest(Test(1502, 'GET ui-bg_highlight-soft_100_f6f6f6_1x100.png'), url1, headers18)

request1503 = createRequest(Test(1503, 'GET ui-icons_666666_256x240.png'), url1, headers18)

request1504 = createRequest(Test(1504, 'GET icon.reassign.gif'), url1, headers19)

request1505 = createRequest(Test(1505, 'GET icon.edit.gif'), url1, headers19)

request1506 = createRequest(Test(1506, 'GET icon.delete.gif'), url1, headers19)

request1507 = createRequest(Test(1507, 'GET icon.export.gif'), url1, headers19)

request1508 = createRequest(Test(1508, 'GET ui-bg_flat_75_ffffff_40x100.png'), url1, headers18)

request1509 = createRequest(Test(1509, 'GET icon.skip.gif'), url1, headers19)

request1510 = createRequest(Test(1510, 'GET icon.claim.gif'), url1, headers19)

request1511 = createRequest(Test(1511, 'GET icon.vacation.gif'), url1, headers19)

request1512 = createRequest(Test(1512, 'GET load.png'), url1, headers19)

request1513 = createRequest(Test(1513, 'GET fhbg.gif'), url1, headers19)

request1514 = createRequest(Test(1514, 'GET wbg.gif'), url1, headers19)

request1515 = createRequest(Test(1515, 'GET magnifier.png'), url1, headers19)

request1516 = createRequest(Test(1516, 'GET first.gif'), url1, headers19)

request1517 = createRequest(Test(1517, 'GET prev.gif'), url1, headers19)

request1518 = createRequest(Test(1518, 'GET next.gif'), url1, headers19)

request1519 = createRequest(Test(1519, 'GET last.gif'), url1, headers19)

request1520 = createRequest(Test(1520, 'GET line.gif'), url1, headers19)

request1521 = createRequest(Test(1521, 'GET ui-bg_highlight-soft_25_0073ea_1x100.png'), url1)

request1601 = createRequest(Test(1601, 'GET empty.jsp'), url1, headers20)

request1602 = createRequest(Test(1602, 'GET load.gif'), url1, headers19)

request1701 = createRequest(Test(1701, 'POST updates.htm'), url1, headers21)

request1702 = createRequest(Test(1702, 'GET icon.claimed.gif'), url1, headers17)

request1703 = createRequest(Test(1703, 'GET icon.notclaimed.gif'), url1, headers17)

request1801 = createRequest(Test(1801, 'POST updates.htm'), url1, headers21)

request1802 = createRequest(Test(1802, 'GET ddn.png'), url1, headers19)

request1901 = createRequest(Test(1901, 'GET ServerLaunch.html'), url1, headers20)

request1902 = createRequest(Test(1902, 'GET loading.gif'), url1, headers22)

request1903 = createRequest(Test(1903, 'GET JSX30.js'), url1, headers23)

request1904 = createRequest(Test(1904, 'GET jsx.js'), url1, headers23)

request1905 = createRequest(Test(1905, 'GET JSX.css'), url1, headers24)

request2001 = createRequest(Test(2001, 'GET locale.xml'), url1, headers25)

request2101 = createRequest(Test(2101, 'GET messages.xml'), url1, headers25)

request2102 = createRequest(Test(2102, 'GET spc.gif'), url1, headers22)

request2201 = createRequest(Test(2201, 'GET logger.xml'), url1, headers25)

request2301 = createRequest(Test(2301, 'GET CSS.xml'), url1, headers25)

request2401 = createRequest(Test(2401, 'GET config.xml'), url1, headers25)

request2402 = createRequest(Test(2402, 'GET style.css'), url1, headers24)

request2501 = createRequest(Test(2501, 'GET config.xml'), url1, headers25)

request2601 = createRequest(Test(2601, 'GET translations.xml'), url1, headers25)

request2701 = createRequest(Test(2701, 'GET appCanvas.xml'), url1, headers25)

request2702 = createRequest(Test(2702, 'GET package.js'), url1, headers23)

request2703 = createRequest(Test(2703, 'GET Packages.js'), url1, headers23)

request2704 = createRequest(Test(2704, 'GET logic.js'), url1, headers23)

request2705 = createRequest(Test(2705, 'GET Button.js'), url1, headers25)

request2706 = createRequest(Test(2706, 'GET LayoutGrid.js'), url1, headers25)

request2707 = createRequest(Test(2707, 'GET Image.js'), url1, headers25)

request2708 = createRequest(Test(2708, 'GET Matrix.js'), url1, headers25)

request2709 = createRequest(Test(2709, 'GET Column.js'), url1, headers25)

request2710 = createRequest(Test(2710, 'GET Field.js'), url1, headers25)

request2711 = createRequest(Test(2711, 'GET Section.js'), url1, headers25)

request2712 = createRequest(Test(2712, 'GET DatePicker.js'), url1, headers25)

request2713 = createRequest(Test(2713, 'GET TextBox.js'), url1, headers25)

request2714 = createRequest(Test(2714, 'GET Form.js'), url1, headers25)

request2715 = createRequest(Test(2715, 'GET Cacheable.js'), url1, headers25)

request2716 = createRequest(Test(2716, 'GET Heavyweight.js'), url1, headers25)

request2717 = createRequest(Test(2717, 'GET Service.js'), url1, headers25)

request2718 = createRequest(Test(2718, 'GET next.gif'), url1, headers22)

request2719 = createRequest(Test(2719, 'GET open.gif'), url1, headers22)

request2720 = createRequest(Test(2720, 'GET attachments.gif'), url1, headers22)

request2721 = createRequest(Test(2721, 'GET close.png'), url1, headers22)

request2722 = createRequest(Test(2722, 'GET previous.gif'), url1, headers22)

request2723 = createRequest(Test(2723, 'GET error.gif'), url1, headers22)

request2801 = createRequest(Test(2801, 'GET TaskManagementServicesMapping.xml'), url1, headers25)

request2901 = createRequest(Test(2901, 'GET soap.xml'), url1, headers25)

request3001 = createRequest(Test(3001, 'GET Tidy.xsl'), url1, headers25)

request3101 = createRequest(Test(3101, 'POST validation'), url1, headers26)

request3201 = createRequest(Test(3201, 'GET FormModelMapping.xml'), url1, headers25)

request3301 = createRequest(Test(3301, 'GET TaskManagementServicesMapping.xml'), url1, headers25)

request3401 = createRequest(Test(3401, 'GET FormModelMapping.xml'), url1, headers25)

request3501 = createRequest(Test(3501, 'POST validation'), url1, headers26)

request3601 = createRequest(Test(3601, 'GET empty.jsp'), url1, headers25)

request3701 = createRequest(Test(3701, 'POST updates.htm'), url1, headers21)

request3801 = createRequest(Test(3801, 'POST updates.htm'), url1, headers21)

request3802 = createRequest(Test(3802, 'GET hl.png'), url1, headers19)

request3901 = createRequest(Test(3901, 'POST proxy.jsp'), url1, headers21)

request3902 = createRequest(Test(3902, 'GET ui-bg_highlight-soft_50_dddddd_1x100.png'), url1, headers18)

request3903 = createRequest(Test(3903, 'GET ui-icons_0073ea_256x240.png'), url1, headers18)

request4001 = createRequest(Test(4001, 'POST proxy.jsp'), url1, headers21)

request4101 = createRequest(Test(4101, 'POST proxy.jsp'), url1, headers21)

request4201 = createRequest(Test(4201, 'POST updates.htm'), url1, headers21)

request4301 = createRequest(Test(4301, 'GET ServerLaunch.html'), url1, headers20)

request4401 = createRequest(Test(4401, 'GET config.xml'), url1, headers27)

request4501 = createRequest(Test(4501, 'GET translations.xml'), url1, headers27)

request4502 = createRequest(Test(4502, 'GET style.css'), url1)

request4601 = createRequest(Test(4601, 'GET appCanvas.xml'), url1, headers27)

request4602 = createRequest(Test(4602, 'GET Packages.js'), url1, headers28)

request4603 = createRequest(Test(4603, 'GET logic.js'), url1, headers28)

request4604 = createRequest(Test(4604, 'GET attachments.gif'), url1, headers29)

request4605 = createRequest(Test(4605, 'GET close.png'), url1, headers29)

request4606 = createRequest(Test(4606, 'GET error.gif'), url1, headers29)

request4701 = createRequest(Test(4701, 'GET TaskManagementServicesMapping.xml'), url1, headers27)

request4801 = createRequest(Test(4801, 'GET Tidy.xsl'), url1, headers27)

request4901 = createRequest(Test(4901, 'POST validation'), url1, headers30)

request5001 = createRequest(Test(5001, 'GET FormModelMapping.xml'), url1, headers27)

request5101 = createRequest(Test(5101, 'GET TaskManagerProcessMapping.xml'), url1, headers27)

request5201 = createRequest(Test(5201, 'GET FormModelMapping.xml'), url1, headers27)

request5301 = createRequest(Test(5301, 'POST validation'), url1, headers30)

request5401 = createRequest(Test(5401, 'GET empty.jsp'), url1, headers27)

request5501 = createRequest(Test(5501, 'POST updates.htm'), url1, headers21)

request5502 = createRequest(Test(5502, 'GET ui-icons_ffffff_256x240.png'), url1, headers18)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET tasks.htm (requests 101-130)."""
    result = request101.GET('/ui-fw/tasks.htm', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://aries:8080/index.htm'),
        NVPair('Cache-Control', 'no-cache'), ))
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

    grinder.sleep(75)
    request102.GET('/ui-fw/style/jqueryui/jquery.ui.theme.css')

    request103.GET('/ui-fw/style/tabs.css')

    request104.GET('/ui-fw/style/flexigrid.css')

    request105.GET('/ui-fw/style/jqueryui/ui.dialog.content.css')

    request106.GET('/ui-fw/style/jqueryui/jquery.alerts.css')

    request107.GET('/ui-fw/style/jqueryui/jquery.qtip.css')

    request108.GET('/ui-fw/style/jqueryui/jquery-ui.css')

    request109.GET('/ui-fw/script/jquery.js')

    request110.GET('/ui-fw/script/ui-fw.js')

    request111.GET('/ui-fw/script/jquery-ui.js')

    request112.GET('/ui-fw/script/jquery-timer.js')

    request113.GET('/ui-fw/script/jquery.jcorners.js')

    request114.GET('/ui-fw/script/jquery.demensions.js')

    request115.GET('/ui-fw/script/jquery.ui.position.js')

    request116.GET('/ui-fw/script/jtabber.js')

    request117.GET('/ui-fw/script/jquery.qtip.js')

    request118.GET('/ui-fw/script/jquery.string.1.0.js')

    request119.GET('/ui-fw/style.css')

    request120.GET('/ui-fw/script/jqSoapClient.min.js')

    request121.GET('/ui-fw/script/ui/jquery.ui.datepicker.js')

    grinder.sleep(15)
    request122.GET('/ui-fw/script/flexigrid.js')

    request123.GET('/ui-fw/script/jquery.alerts.js')

    grinder.sleep(122)
    request124.GET('/ui-fw/images/icons/icon.task.png')

    request125.GET('/ui-fw/images/icons/export/pdf.png')

    request126.GET('/ui-fw/images/icons/icon.notification.png')

    request127.GET('/ui-fw/images/icons/export/csv.png')

    request128.GET('/ui-fw/images/icons/export/ical.png')

    request129.GET('/ui-fw/images/icons/icon.process.png')

    request130.GET('/ui-fw/images/logo.png')

    return result

  def page2(self):
    """POST vacation.htm (request 201)."""
    result = request201.POST('/ui-fw/vacation.htm',
      ( NVPair('action', 'Validate'), ),
      ( NVPair('Accept', 'application/json, text/javascript, */*; q=0.01'),
        NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
        NVPair('Referer', 'http://aries:8080/ui-fw/tasks.htm'),
        NVPair('Cache-Control', 'no-cache'), ))

    return result

  def page3(self):
    """POST updates.htm (request 301)."""
    result = request301.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 43 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '11d1def534ea1be0:60f86172:13bb6a2dfd9:-7...'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'PATask'
    # 4 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/SubstarctDates/form.gi/Intal...'
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.
    self.token_user = \
      httpUtilities.valueFromBodyURI('user') # 'intalio\\admin'
    self.token_claimTaskOnOpen = \
      httpUtilities.valueFromBodyURI('claimTaskOnOpen') # 'false'

    return result

  def page4(self):
    """POST updates.htm (request 401)."""
    result = request401.POST('/ui-fw/updates.htm',
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
      httpUtilities.valueFromBodyURI('id') # 'notify-9F3O-WE9Q-G0D9-IU40'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'Notification'
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/RepeatEvery_PXEI_897/Forms/n...'
    self.token_token = \
      httpUtilities.valueFromBodyURI('token') # 'VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlz...'

    return result

  def page5(self):
    """POST updates.htm (requests 501-521)."""
    result = request501.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PIPATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 27 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '6d316302-675f-46d7-b65d-14e904fdd1e0'
    # 15 different values for token_type found in response, using the first one.
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'PIPATask'
    # 40 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/AjaxPA1/form.gi/IntalioInter...'
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.
    self.token_claim2000TaskOnOpen = \
      httpUtilities.valueFromBodyURI('''claim\r
2000\r
TaskOnOpen''') # 'false'

    request502.GET('/ui-fw/images/ui-bg_highlight-soft_100_f6f6f6_1x100.png')

    request503.GET('/ui-fw/images/ui-icons_666666_256x240.png')

    request504.GET('/ui-fw/images/ui-bg_flat_75_ffffff_40x100.png')

    request505.GET('/ui-fw/images/flexigrid/load.png')

    request506.GET('/ui-fw/images/flexigrid/prev.gif')

    request507.GET('/ui-fw/images/icons/icon.claim.gif')

    request508.GET('/ui-fw/images/icons/icon.vacation.gif')

    request509.GET('/ui-fw/images/icons/icon.delete.gif')

    request510.GET('/ui-fw/images/icons/icon.skip.gif')

    request511.GET('/ui-fw/images/icons/icon.edit.gif')

    request512.GET('/ui-fw/images/flexigrid/fhbg.gif')

    request513.GET('/ui-fw/images/icons/icon.reassign.gif')

    request514.GET('/ui-fw/images/icons/icon.export.gif')

    request515.GET('/ui-fw/images/flexigrid/wbg.gif')

    request516.GET('/ui-fw/images/flexigrid/magnifier.png')

    request517.GET('/ui-fw/images/flexigrid/first.gif')

    request518.GET('/ui-fw/images/flexigrid/next.gif')

    request519.GET('/ui-fw/images/flexigrid/last.gif')

    request520.GET('/ui-fw/images/flexigrid/load.gif')

    request521.GET('/ui-fw/images/ui-bg_highlight-soft_25_0073ea_1x100.png', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://aries:8080/ui-fw/style/tabs.css'),
        NVPair('Cache-Control', 'no-cache'), ))

    return result

  def page6(self):
    """GET empty.jsp (requests 601-603)."""
    result = request601.GET('/ui-fw/script/empty.jsp', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://aries:8080/ui-fw/tasks.htm'), ))

    request602.GET('/ui-fw/images/flexigrid/line.gif')

    grinder.sleep(215)
    request603.GET('/ui-fw/images/icons/icon.notclaimed.gif')

    return result

  def page7(self):
    """POST updates.htm (request 701)."""
    result = request701.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 43 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '11d1def534ea1be0:60f86172:13bb6a2dfd9:-7...'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'PATask'
    # 4 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/SubstarctDates/form.gi/Intal...'
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page8(self):
    """GET / (requests 801-808)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request801.GET('/')
    self.token_jsessionid = \
      httpUtilities.valueFromLocationURI('jsessionid') # '13CAD5C8E31C5AB18BE953D1D189E8F9'

    request802.GET('/login.htm;jsessionid=' +
      self.token_jsessionid)
    self.token_actionName = \
      httpUtilities.valueFromHiddenInput('actionName') # 'logIn'

    grinder.sleep(14)
    request803.GET('/style/custom/customLogin.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://ramanujan:8080/login.htm;jsessionid=13CAD5C8E31C5AB18BE953D1D189E8F9'), ))

    request804.GET('/favicon.ico')

    request805.GET('/scripts/plugin/jquery-1.8.2.js', None,
      ( NVPair('Accept', '*/*'),
        NVPair('Referer', 'http://ramanujan:8080/login.htm;jsessionid=13CAD5C8E31C5AB18BE953D1D189E8F9'), ))
    self.token_ = \
      httpUtilities.valueFromHiddenInput('') # 'false'

    grinder.sleep(11)
    request806.GET('/images/logo.png', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://ramanujan:8080/login.htm;jsessionid=13CAD5C8E31C5AB18BE953D1D189E8F9'), ))

    grinder.sleep(64)
    request807.GET('/images/key.png')

    grinder.sleep(20)
    request808.GET('/images/user_gray.png')

    return result

  def page9(self):
    """POST login.htm (requests 901-934)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request901.POST('/login.htm;jsessionid=' +
      self.token_jsessionid,
      ( NVPair('actionName', self.token_actionName),
        NVPair('username', 'admin'),
        NVPair('password', 'changeit'),
        NVPair('submit', 'Login'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    grinder.sleep(28)
    request902.GET('/index.htm')
    self.token_accessible = \
      httpUtilities.valueFromHiddenInput('accessible') # ''

    grinder.sleep(18)
    request903.GET('/style/plugin/jquery.ui.theme.css')

    request904.GET('/style/plugin/jquery-ui-1.9.0.css')

    request905.GET('/style/plugin/jquery.dataTables.css')

    request906.GET('/style/plugin/nv.d3.css')

    request907.GET('/style/plugin/jquery.qtip.css')

    request908.GET('/style/custom/dashboardui.css')

    request909.GET('/scripts/plugin/jquery-ui.js')

    request910.GET('/scripts/plugin/jquery.ui.position.js')

    request911.GET('/scripts/plugin/jquery.dashboard.min.js')

    request912.GET('/scripts/plugin/jquery.qtip.js')

    request913.GET('/scripts/plugin/themeroller.js')
    # 22 different values for token_ffDefault found in response, using the first one.
    self.token_ffDefault = \
      httpUtilities.valueFromBodyURI('ffDefault') # 'Trebuchet+MS,+Tahoma,+Verdana,+Arial,+sa...'
    # 8 different values for token_fwDefault found in response, using the first one.
    self.token_fwDefault = \
      httpUtilities.valueFromBodyURI('fwDefault') # 'bold'
    # 5 different values for token_fsDefault found in response, using the first one.
    self.token_fsDefault = \
      httpUtilities.valueFromBodyURI('fsDefault') # '1.1em'
    # 19 different values for token_cornerRadius found in response, using the first one.
    self.token_cornerRadius = \
      httpUtilities.valueFromBodyURI('cornerRadius') # '4px'
    # 24 different values for token_bgColorHeader found in response, using the first one.
    self.token_bgColorHeader = \
      httpUtilities.valueFromBodyURI('bgColorHeader') # 'f6a828'
    # 17 different values for token_bgTextureHeader found in response, using the first one.
    self.token_bgTextureHeader = \
      httpUtilities.valueFromBodyURI('bgTextureHeader') # '12_gloss_wave.png'
    # 22 different values for token_bgImgOpacityHeader found in response, using the first one.
    self.token_bgImgOpacityHeader = \
      httpUtilities.valueFromBodyURI('bgImgOpacityHeader') # '35'
    # 24 different values for token_borderColorHeader found in response, using the first one.
    self.token_borderColorHeader = \
      httpUtilities.valueFromBodyURI('borderColorHeader') # 'e78f08'
    # 15 different values for token_fcHeader found in response, using the first one.
    self.token_fcHeader = \
      httpUtilities.valueFromBodyURI('fcHeader') # 'ffffff'
    # 19 different values for token_iconColorHeader found in response, using the first one.
    self.token_iconColorHeader = \
      httpUtilities.valueFromBodyURI('iconColorHeader') # 'ffffff'
    # 23 different values for token_bgColorContent found in response, using the first one.
    self.token_bgColorContent = \
      httpUtilities.valueFromBodyURI('bgColorContent') # 'eeeeee'
    # 23 different values for token_bgTextureContent found in response, using the first one.
    self.token_bgTextureContent = \
      httpUtilities.valueFromBodyURI('bgTextureContent') # '03_highlight_soft.png'
    # 16 different values for token_bgImgOpacityContent found in response, using the first one.
    self.token_bgImgOpacityContent = \
      httpUtilities.valueFromBodyURI('bgImgOpacityContent') # '100'
    # 22 different values for token_borderColorContent found in response, using the first one.
    self.token_borderColorContent = \
      httpUtilities.valueFromBodyURI('borderColorContent') # 'dddddd'
    # 22 different values for token_fcContent found in response, using the first one.
    self.token_fcContent = \
      httpUtilities.valueFromBodyURI('fcContent') # '333333'
    # 20 different values for token_iconColorContent found in response, using the first one.
    self.token_iconColorContent = \
      httpUtilities.valueFromBodyURI('iconColorContent') # '222222'
    # 23 different values for token_bgColorDefault found in response, using the first one.
    self.token_bgColorDefault = \
      httpUtilities.valueFromBodyURI('bgColorDefault') # 'f6f6f6'
    # 15 different values for token_bgTextureDefault found in response, using the first one.
    self.token_bgTextureDefault = \
      httpUtilities.valueFromBodyURI('bgTextureDefault') # '02_glass.png'
    # 21 different values for token_bgImgOpacityDefault found in response, using the first one.
    self.token_bgImgOpacityDefault = \
      httpUtilities.valueFromBodyURI('bgImgOpacityDefault') # '100'
    # 22 different values for token_borderColorDefault found in response, using the first one.
    self.token_borderColorDefault = \
      httpUtilities.valueFromBodyURI('borderColorDefault') # 'cccccc'
    # 24 different values for token_fcDefault found in response, using the first one.
    self.token_fcDefault = \
      httpUtilities.valueFromBodyURI('fcDefault') # '1c94c4'
    # 24 different values for token_iconColorDefault found in response, using the first one.
    self.token_iconColorDefault = \
      httpUtilities.valueFromBodyURI('iconColorDefault') # 'ef8c08'
    # 24 different values for token_bgColorHover found in response, using the first one.
    self.token_bgColorHover = \
      httpUtilities.valueFromBodyURI('bgColorHover') # 'fdf5ce'
    # 15 different values for token_bgTextureHover found in response, using the first one.
    self.token_bgTextureHover = \
      httpUtilities.valueFromBodyURI('bgTextureHover') # '02_glass.png'
    # 19 different values for token_bgImgOpacityHover found in response, using the first one.
    self.token_bgImgOpacityHover = \
      httpUtilities.valueFromBodyURI('bgImgOpacityHover') # '100'
    # 24 different values for token_borderColorHover found in response, using the first one.
    self.token_borderColorHover = \
      httpUtilities.valueFromBodyURI('borderColorHover') # 'fbcb09'
    # 24 different values for token_fcHover found in response, using the first one.
    self.token_fcHover = \
      httpUtilities.valueFromBodyURI('fcHover') # 'c77405'
    # 24 different values for token_iconColorHover found in response, using the first one.
    self.token_iconColorHover = \
      httpUtilities.valueFromBodyURI('iconColorHover') # 'ef8c08'
    # 19 different values for token_bgColorActive found in response, using the first one.
    self.token_bgColorActive = \
      httpUtilities.valueFromBodyURI('bgColorActive') # 'ffffff'
    # 21 different values for token_bgTextureActive found in response, using the first one.
    self.token_bgTextureActive = \
      httpUtilities.valueFromBodyURI('bgTextureActive') # '02_glass.png'
    # 20 different values for token_bgImgOpacityActive found in response, using the first one.
    self.token_bgImgOpacityActive = \
      httpUtilities.valueFromBodyURI('bgImgOpacityActive') # '65'
    # 24 different values for token_borderColorActive found in response, using the first one.
    self.token_borderColorActive = \
      httpUtilities.valueFromBodyURI('borderColorActive') # 'fbd850'
    # 24 different values for token_fcActive found in response, using the first one.
    self.token_fcActive = \
      httpUtilities.valueFromBodyURI('fcActive') # 'eb8f00'
    # 24 different values for token_iconColorActive found in response, using the first one.
    self.token_iconColorActive = \
      httpUtilities.valueFromBodyURI('iconColorActive') # 'ef8c08'
    # 24 different values for token_bgColorHighlight found in response, using the first one.
    self.token_bgColorHighlight = \
      httpUtilities.valueFromBodyURI('bgColorHighlight') # 'ffe45c'
    # 20 different values for token_bgTextureHighlight found in response, using the first one.
    self.token_bgTextureHighlight = \
      httpUtilities.valueFromBodyURI('bgTextureHighlight') # '03_highlight_soft.png'
    # 23 different values for token_bgImgOpacityHighlight found in response, using the first one.
    self.token_bgImgOpacityHighlight = \
      httpUtilities.valueFromBodyURI('bgImgOpacityHighlight') # '75'
    # 24 different values for token_borderColorHighlight found in response, using the first one.
    self.token_borderColorHighlight = \
      httpUtilities.valueFromBodyURI('borderColorHighlight') # 'fed22f'
    # 17 different values for token_fcHighlight found in response, using the first one.
    self.token_fcHighlight = \
      httpUtilities.valueFromBodyURI('fcHighlight') # '363636'
    # 24 different values for token_iconColorHighlight found in response, using the first one.
    self.token_iconColorHighlight = \
      httpUtilities.valueFromBodyURI('iconColorHighlight') # '228ef1'
    # 24 different values for token_bgColorError found in response, using the first one.
    self.token_bgColorError = \
      httpUtilities.valueFromBodyURI('bgColorError') # 'b81900'
    # 21 different values for token_bgTextureError found in response, using the first one.
    self.token_bgTextureError = \
      httpUtilities.valueFromBodyURI('bgTextureError') # '08_diagonals_thick.png'
    # 24 different values for token_bgImgOpacityError found in response, using the first one.
    self.token_bgImgOpacityError = \
      httpUtilities.valueFromBodyURI('bgImgOpacityError') # '18'
    # 18 different values for token_borderColorError found in response, using the first one.
    self.token_borderColorError = \
      httpUtilities.valueFromBodyURI('borderColorError') # 'cd0a0a'
    # 13 different values for token_fcError found in response, using the first one.
    self.token_fcError = \
      httpUtilities.valueFromBodyURI('fcError') # 'ffffff'
    # 24 different values for token_iconColorError found in response, using the first one.
    self.token_iconColorError = \
      httpUtilities.valueFromBodyURI('iconColorError') # 'ffd27a'
    # 23 different values for token_bgColorOverlay found in response, using the first one.
    self.token_bgColorOverlay = \
      httpUtilities.valueFromBodyURI('bgColorOverlay') # '666666'
    # 21 different values for token_bgTextureOverlay found in response, using the first one.
    self.token_bgTextureOverlay = \
      httpUtilities.valueFromBodyURI('bgTextureOverlay') # '08_diagonals_thick.png'
    # 21 different values for token_bgImgOpacityOverlay found in response, using the first one.
    self.token_bgImgOpacityOverlay = \
      httpUtilities.valueFromBodyURI('bgImgOpacityOverlay') # '20'
    # 23 different values for token_opacityOverlay found in response, using the first one.
    self.token_opacityOverlay = \
      httpUtilities.valueFromBodyURI('opacityOverlay') # '50'
    # 21 different values for token_bgColorShadow found in response, using the first one.
    self.token_bgColorShadow = \
      httpUtilities.valueFromBodyURI('bgColorShadow') # '000000'
    # 6 different values for token_bgTextureShadow found in response, using the first one.
    self.token_bgTextureShadow = \
      httpUtilities.valueFromBodyURI('bgTextureShadow') # '01_flat.png'
    # 23 different values for token_bgImgOpacityShadow found in response, using the first one.
    self.token_bgImgOpacityShadow = \
      httpUtilities.valueFromBodyURI('bgImgOpacityShadow') # '10'
    # 19 different values for token_opacityShadow found in response, using the first one.
    self.token_opacityShadow = \
      httpUtilities.valueFromBodyURI('opacityShadow') # '20'
    # 22 different values for token_thicknessShadow found in response, using the first one.
    self.token_thicknessShadow = \
      httpUtilities.valueFromBodyURI('thicknessShadow') # '5px'
    # 23 different values for token_offsetTopShadow found in response, using the first one.
    self.token_offsetTopShadow = \
      httpUtilities.valueFromBodyURI('offsetTopShadow') # '-5px'
    # 23 different values for token_offsetLeftShadow found in response, using the first one.
    self.token_offsetLeftShadow = \
      httpUtilities.valueFromBodyURI('offsetLeftShadow') # '-5px'
    # 21 different values for token_cornerRadiusShadow found in response, using the first one.
    self.token_cornerRadiusShadow = \
      httpUtilities.valueFromBodyURI('cornerRadiusShadow') # '5px'
    self.token_tr = \
      httpUtilities.valueFromBodyURI('tr') # 'ffDefault=Helvetica,Arial,sans-serif'
    self.token_fsDefaultUnit = \
      httpUtilities.valueFromBodyURI('fsDefaultUnit') # 'em'
    self.token_cornerRadiusUnit = \
      httpUtilities.valueFromBodyURI('cornerRadiusUnit') # 'px'

    request914.GET('/scripts/plugin/d3.v2.js')

    request915.GET('/scripts/plugin/nv.d3.js')

    request916.GET('/scripts/plugin/tooltip.js')

    request917.GET('/scripts/plugin/utils.js')

    request918.GET('/scripts/plugin/axis.js')

    request919.GET('/scripts/plugin/discreteBar.js')

    request920.GET('/scripts/plugin/discreteBarChart.js')

    grinder.sleep(34)
    request921.GET('/scripts/plugin/multiBar.js')

    request922.GET('/scripts/plugin/multiBarChart.js')

    request923.GET('/scripts/plugin/legend.js')

    request924.GET('/scripts/plugin/scatter.js')

    grinder.sleep(34)
    request925.GET('/scripts/plugin/line.js')

    grinder.sleep(28)
    request926.GET('/scripts/plugin/pie.js')

    request927.GET('/scripts/plugin/jquery.dataTables.js')

    request928.GET('/scripts/plugin/historicalBar.js')

    request929.GET('/scripts/plugin/pieChart.js')

    request930.GET('/scripts/plugin/linePlusBarChart.js')

    request931.GET('/scripts/plugin/multiBarHorizontalChart.js')

    request932.GET('/scripts/plugin/jquery-dateFormat.js')

    request933.GET('/scripts/plugin/multiBarHorizontal.js')

    request934.GET('/scripts/custom/dashboard.js')

    return result

  def page10(self):
    """GET data.json (requests 1001-1006)."""
    self.token_action = \
      'getStateWidgetData'
    self.token__ = \
      '1355986699604'
    result = request1001.GET('/data.json' +
      '?action=' +
      self.token_action +
      '&_=' +
      self.token__)

    request1002.GET('/images/ui-icons_666666_256x240.png')

    request1003.GET('/images/ui-bg_highlight-soft_100_f6f6f6_1x100.png')

    request1004.GET('/images/ui-bg_flat_75_ffffff_40x100.png')

    request1005.GET('/images/loading.gif', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://ramanujan:8080/style/custom/dashboardui.css'), ))

    grinder.sleep(77)
    request1006.GET('/images/ui-bg_highlight-soft_50_dddddd_1x100.png')

    return result

  def page11(self):
    """GET templates.html (request 1101)."""
    result = request1101.GET('/templates.html', None,
      ( NVPair('Accept', 'text/html, */*; q=0.01'),
        NVPair('Referer', 'http://ramanujan:8080/index.htm'), ))

    return result

  def page12(self):
    """GET dsState.json (requests 1201-1203)."""
    self.token_action = \
      'getState'
    self.token_ignore_cache = \
      '1355986707379'
    result = request1201.GET('/dsState.json' +
      '?action=' +
      self.token_action +
      '&ignore_cache=' +
      self.token_ignore_cache)

    grinder.sleep(24)
    request1202.GET('/images/ui-icons_0073ea_256x240.png')

    grinder.sleep(1923)
    request1203.GET('/images/ui-bg_highlight-soft_25_0073ea_1x100.png')

    return result

  def page13(self):
    """GET tasks.htm (requests 1301-1302)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request1301.GET('/ui-fw/tasks.htm')

    request1302.GET('/images/ui-bg_glass_65_ffffff_1x400.png')

    return result

  def page14(self):
    """GET login.htm (requests 1401-1432)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request1401.GET('/ui-fw/login.htm')

    request1402.GET('/ui-fw/tasks.htm' +
      '?null')
    # 2 different values for token_token found in response, using the first one.
    self.token_token = \
      httpUtilities.valueFromBodyURI('token') # 'VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlz...'
    self.token_actionName = \
      httpUtilities.valueFromHiddenInput('actionName') # ''

    grinder.sleep(15)
    request1403.GET('/ui-fw/style.css')

    request1404.GET('/ui-fw/style/tabs.css')

    request1405.GET('/ui-fw/style/flexigrid.css')

    request1406.GET('/ui-fw/style/jqueryui/jquery-ui.css')

    request1407.GET('/ui-fw/style/jqueryui/jquery.ui.theme.css')

    request1408.GET('/ui-fw/style/jqueryui/jquery.qtip.css')

    request1409.GET('/ui-fw/style/jqueryui/jquery.alerts.css')

    request1410.GET('/ui-fw/style/jqueryui/ui.dialog.content.css')

    request1411.GET('/ui-fw/script/ui-fw.js')

    request1412.GET('/ui-fw/script/jquery.js')

    request1413.GET('/ui-fw/script/jquery-timer.js')

    request1414.GET('/ui-fw/script/jquery-ui.js')

    request1415.GET('/ui-fw/script/jquery.jcorners.js')

    request1416.GET('/ui-fw/script/jquery.demensions.js')

    request1417.GET('/ui-fw/script/jquery.ui.position.js')

    request1418.GET('/ui-fw/script/jtabber.js')

    request1419.GET('/ui-fw/script/jquery.qtip.js')

    request1420.GET('/ui-fw/script/jquery.string.1.0.js')

    request1421.GET('/ui-fw/script/jqSoapClient.min.js')

    grinder.sleep(23)
    request1422.GET('/ui-fw/script/ui/jquery.ui.datepicker.js')

    request1423.GET('/ui-fw/script/jquery.alerts.js')

    request1424.GET('/ui-fw/script/flexigrid.js')

    request1425.GET('/ui-fw/images/logo.png')

    request1426.GET('/ui-fw/images/icons/export/csv.png')

    request1427.GET('/ui-fw/images/icons/export/ical.png')

    request1428.GET('/ui-fw/images/icons/icon.task.png')

    request1429.GET('/ui-fw/images/icons/export/pdf.png')

    request1430.GET('/ui-fw/images/icons/icon.process.png')

    request1431.GET('/ui-fw/images/icons/icon.notification.png')

    request1432.GET('/ui-fw/favicon.ico')

    return result

  def page15(self):
    """POST vacation.htm (requests 1501-1521)."""
    result = request1501.POST('/ui-fw/vacation.htm',
      ( NVPair('action', 'Validate'), ),
      ( NVPair('Accept', 'application/json, text/javascript, */*; q=0.01'),
        NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
        NVPair('Referer', 'http://ramanujan:8080/ui-fw/tasks.htm?null'),
        NVPair('Cache-Control', 'no-cache'), ))

    grinder.sleep(185)
    request1502.GET('/ui-fw/images/ui-bg_highlight-soft_100_f6f6f6_1x100.png')

    request1503.GET('/ui-fw/images/ui-icons_666666_256x240.png')

    request1504.GET('/ui-fw/images/icons/icon.reassign.gif')

    request1505.GET('/ui-fw/images/icons/icon.edit.gif')

    request1506.GET('/ui-fw/images/icons/icon.delete.gif')

    request1507.GET('/ui-fw/images/icons/icon.export.gif')

    request1508.GET('/ui-fw/images/ui-bg_flat_75_ffffff_40x100.png')

    request1509.GET('/ui-fw/images/icons/icon.skip.gif')

    request1510.GET('/ui-fw/images/icons/icon.claim.gif')

    request1511.GET('/ui-fw/images/icons/icon.vacation.gif')

    request1512.GET('/ui-fw/images/flexigrid/load.png')

    request1513.GET('/ui-fw/images/flexigrid/fhbg.gif')

    request1514.GET('/ui-fw/images/flexigrid/wbg.gif')

    request1515.GET('/ui-fw/images/flexigrid/magnifier.png')

    request1516.GET('/ui-fw/images/flexigrid/first.gif')

    request1517.GET('/ui-fw/images/flexigrid/prev.gif')

    request1518.GET('/ui-fw/images/flexigrid/next.gif')

    request1519.GET('/ui-fw/images/flexigrid/last.gif')

    request1520.GET('/ui-fw/images/flexigrid/line.gif')

    request1521.GET('/ui-fw/images/ui-bg_highlight-soft_25_0073ea_1x100.png', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://ramanujan:8080/ui-fw/style/tabs.css'), ))

    return result

  def page16(self):
    """GET empty.jsp (requests 1601-1602)."""
    result = request1601.GET('/ui-fw/script/empty.jsp')

    request1602.GET('/ui-fw/images/flexigrid/load.gif')

    return result

  def page17(self):
    """POST updates.htm (requests 1701-1703)."""
    result = request1701.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 10 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '26ac8b80354d82d1:7f1f730:13bb84af6cb:-37...'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'PATask'
    # 10 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/SampleAjaxPAWithTimer/sample...'
    self.token_token = \
      httpUtilities.valueFromBodyURI('token') # 'VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlz...'

    grinder.sleep(155)
    request1702.GET('/ui-fw/images/icons/icon.claimed.gif')

    request1703.GET('/ui-fw/images/icons/icon.notclaimed.gif')

    return result

  def page18(self):
    """POST updates.htm (requests 1801-1802)."""
    result = request1801.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PIPATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 27 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '7e9c029c-9139-4cb0-9954-b3919d27ee29'
    # 15 different values for token_type found in response, using the first one.
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'PIPATask'
    # 40 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/AjaxChainedExecution/SelectT...'
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.
    # 1 different values for token_user found in response; the first matched
    # the last known value of token_user - don't update the variable.
    self.token_claimTaskOnOpe1cben = \
      httpUtilities.valueFromBodyURI('''claimTaskOnOpe\r
1cbe\r
n''') # 'false'

    grinder.sleep(712)
    request1802.GET('/ui-fw/images/flexigrid/ddn.png')

    return result

  def page19(self):
    """GET ServerLaunch.html (requests 1901-1905)."""
    self.token_id = \
      'fd035c38-cd69-4d08-8641-99c30472f4d4'
    self.token_url = \
      '/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html'
    result = request1901.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html' +
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

    grinder.sleep(13)
    request1902.GET('/gi/files/images/loading.gif')

    request1903.GET('/gi/files/JSX/js/JSX30.js')

    grinder.sleep(58)
    request1904.GET('/gi/files/JSX/js/fx/jsx.js')

    grinder.sleep(239)
    request1905.GET('/gi/files/JSX/css/fx/JSX.css')

    return result

  def page20(self):
    """GET locale.xml (request 2001)."""
    result = request2001.GET('/gi/files/JSX/locale/locale.xml')

    return result

  def page21(self):
    """GET messages.xml (requests 2101-2102)."""
    result = request2101.GET('/gi/files/JSX/locale/messages.xml')

    request2102.GET('/gi/files/JSX/images/spc.gif')

    return result

  def page22(self):
    """GET logger.xml (request 2201)."""
    result = request2201.GET('/gi/files/logger.xml')

    return result

  def page23(self):
    """GET CSS.xml (request 2301)."""
    result = request2301.GET('/gi/files/JSX/jss/CSS.xml')

    return result

  def page24(self):
    """GET config.xml (requests 2401-2402)."""
    result = request2401.GET('/gi/apppath/SubstarctDates/form.gi/config.xml')

    request2402.GET('/gi/apppath/SubstarctDates/form.gi/css/style.css')

    return result

  def page25(self):
    """GET config.xml (request 2501)."""
    result = request2501.GET('/gi/files/JSX/addins/intalioajax-addins/config.xml')

    return result

  def page26(self):
    """GET translations.xml (request 2601)."""
    result = request2601.GET('/gi/apppath/SubstarctDates/form.gi/jss/translations.xml')

    return result

  def page27(self):
    """GET appCanvas.xml (requests 2701-2723)."""
    result = request2701.GET('/gi/apppath/SubstarctDates/form.gi/components/appCanvas.xml')

    grinder.sleep(26)
    request2702.GET('/gi/files/JSX/addins/intalioajax-addins/js/com/intalio/ria/package.js')

    grinder.sleep(63)
    request2703.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/Packages.js')
    self.token_imgsrc = \
      httpUtilities.valueFromBodyURI('<img src') # ''
    self.token_ahref = \
      httpUtilities.valueFromBodyURI('<a href') # ''

    grinder.sleep(55)
    request2704.GET('/gi/apppath/SubstarctDates/form.gi/js/logic.js')

    grinder.sleep(23)
    request2705.GET('/gi/files/JSX/js/jsx3/gui/Button.js')

    request2706.GET('/gi/files/JSX/js/jsx3/gui/LayoutGrid.js')

    request2707.GET('/gi/files/JSX/js/jsx3/gui/Image.js')

    request2708.GET('/gi/files/JSX/js/jsx3/gui/Matrix.js')

    request2709.GET('/gi/files/JSX/js/jsx3/gui/Matrix/Column.js')

    request2710.GET('/gi/files/JSX/addins/intalioajax-addins/js/com/intalio/ria/Field.js')

    request2711.GET('/gi/files/JSX/addins/intalioajax-addins/js/com/intalio/ria/Section.js')

    request2712.GET('/gi/files/JSX/js/jsx3/gui/DatePicker.js')

    request2713.GET('/gi/files/JSX/js/jsx3/gui/TextBox.js')

    grinder.sleep(70)
    request2714.GET('/gi/files/JSX/js/jsx3/gui/Form.js')

    grinder.sleep(19)
    request2715.GET('/gi/files/JSX/js/jsx3/xml/Cacheable.js')

    grinder.sleep(54)
    request2716.GET('/gi/files/JSX/js/jsx3/gui/Heavyweight.js')

    grinder.sleep(136)
    request2717.GET('/gi/files/JSX/js/jsx3/net/Service.js')

    request2718.GET('/gi/files/JSX/images/jsxdatepicker/next.gif')

    request2719.GET('/gi/files/JSX/images/jsxdatepicker/open.gif')

    request2720.GET('/gi/apppath/SubstarctDates/form.gi/images/attachments.gif')

    request2721.GET('/gi/apppath/SubstarctDates/form.gi/images/close.png')

    request2722.GET('/gi/files/JSX/images/jsxdatepicker/previous.gif')

    request2723.GET('/gi/apppath/SubstarctDates/form.gi/images/error.gif')

    return result

  def page28(self):
    """GET TaskManagementServicesMapping.xml (request 2801)."""
    result = request2801.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page29(self):
    """GET soap.xml (request 2901)."""
    result = request2901.GET('/gi/files/JSX/stubs/soap.xml')

    return result

  def page30(self):
    """GET Tidy.xsl (request 3001)."""
    result = request3001.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/Tidy.xsl')

    return result

  def page31(self):
    """POST validation (request 3101)."""
    result = request3101.POST('/gi/validation',
      ( NVPair('assembly', 'SubstarctDates'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>fd035c38-cd69-4d08-8641-99c30472f4d4</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NjcwODQ1OCYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09NzYyNjMyNTA0ODg4ODgzMDI3OCYmdGltZXN0YW1wPT0xMzU1OTg2NzA4NDU4JiZkaWdlc3Q9PWVqeTMvckNTK2M2ZkI3cHB2ZWxZUWFtYWNUQT0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page32(self):
    """GET FormModelMapping.xml (request 3201)."""
    result = request3201.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page33(self):
    """GET TaskManagementServicesMapping.xml (request 3301)."""
    result = request3301.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page34(self):
    """GET FormModelMapping.xml (request 3401)."""
    result = request3401.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page35(self):
    """POST validation (request 3501)."""
    result = request3501.POST('/gi/validation',
      ( NVPair('assembly', 'SubstarctDates'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:initRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>fd035c38-cd69-4d08-8641-99c30472f4d4</jsx1:taskId><jsx1:input><a0:FormModel xmlns:a0=\"http://www.intalio.com/gi/form.gi\"><date1>2012-12-19</date1><date2>2012-12-22</date2></a0:FormModel></jsx1:input><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NjcwODQ1OCYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09NzYyNjMyNTA0ODg4ODgzMDI3OCYmdGltZXN0YW1wPT0xMzU1OTg2NzA4NDU4JiZkaWdlc3Q9PWVqeTMvckNTK2M2ZkI3cHB2ZWxZUWFtYWNUQT0mJiYmVE9LRU4=</jsx1:participantToken><jsx1:formUrl>/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html</jsx1:formUrl></jsx1:initRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page36(self):
    """GET empty.jsp (request 3601)."""
    result = request3601.GET('/ui-fw/script/empty.jsp')

    return result

  def page37(self):
    """POST updates.htm (request 3701)."""
    result = request3701.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PIPATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 27 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '7e9c029c-9139-4cb0-9954-b3919d27ee29'
    # 14 different values for token_type found in response; the first matched
    # the last known value of token_type - don't update the variable.
    # 40 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/AjaxChainedExecution/SelectT...'
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.
    # 1 different values for token_user found in response; the first matched
    # the last known value of token_user - don't update the variable.

    return result

  def page38(self):
    """POST updates.htm (requests 3801-3802)."""
    result = request3801.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 10 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '26ac8b80354d82d1:7f1f730:13bb84af6cb:-37...'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'PATask'
    # 10 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/SampleAjaxPAWithTimer/sample...'

    grinder.sleep(953)
    request3802.GET('/ui-fw/images/flexigrid/hl.png')

    return result

  def page39(self):
    """POST proxy.jsp (requests 3901-3903)."""
    result = request3901.POST('/ui-fw/script/proxy.jsp',
      '<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\"><soapenv:Body><getAssignedRoles xmlns=\"http://tempo.intalio.org/security/RBACQueryService/\"><user>intalio\\\\admin</user></getAssignedRoles></soapenv:Body></soapenv:Envelope>',
      ( NVPair('Content-Type', 'text/xml; charset=\"utf-8\"'), ))

    grinder.sleep(16)
    request3902.GET('/ui-fw/images/ui-bg_highlight-soft_50_dddddd_1x100.png')

    request3903.GET('/ui-fw/images/ui-icons_0073ea_256x240.png')

    return result

  def page40(self):
    """POST proxy.jsp (request 4001)."""
    result = request4001.POST('/ui-fw/script/proxy.jsp',
      '<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\"><soapenv:Body><getAssignedUsers xmlns=\"http://tempo.intalio.org/security/RBACQueryService/\"><role>intalio\\\\WorkflowAdministrator</role></getAssignedUsers></soapenv:Body></soapenv:Envelope>',
      ( NVPair('Content-Type', 'text/xml; charset=\"utf-8\"'), ))

    return result

  def page41(self):
    """POST proxy.jsp (request 4101)."""
    result = request4101.POST('/ui-fw/script/proxy.jsp',
      '<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\"><soapenv:Body><reassign xmlns=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><taskId>26ac8b80354d82d1:-5e64727b:13bb6140d8e:-731e169.254.216.23436</taskId><userOwner></userOwner><roleOwner>intalio\\\\WorkflowAdministrator</roleOwner><taskState>READY</taskState><participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NjcwODQ1OCYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09NzYyNjMyNTA0ODg4ODgzMDI3OCYmdGltZXN0YW1wPT0xMzU1OTg2NzA4NDU4JiZkaWdlc3Q9PWVqeTMvckNTK2M2ZkI3cHB2ZWxZUWFtYWNUQT0mJiYmVE9LRU4=</participantToken><userAction>REASSIGN</userAction></reassign></soapenv:Body></soapenv:Envelope>',
      ( NVPair('Content-Type', 'text/xml; charset=\"utf-8\"'), ))

    return result

  def page42(self):
    """POST updates.htm (request 4201)."""
    result = request4201.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 12 different values for token_id found in response; the first matched
    # the last known value of token_id - don't update the variable.
    # 12 different values for token_url found in response; the first matched
    # the last known value of token_url - don't update the variable.
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page43(self):
    """GET ServerLaunch.html (request 4301)."""
    self.token_id = \
      '26ac8b80354d82d1:-5e64727b:13bb6140d8e:-731e169.254.216.23436'
    self.token_url = \
      '/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html'
    result = request4301.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html' +
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

  def page44(self):
    """GET config.xml (request 4401)."""
    result = request4401.GET('/gi/apppath/SubstarctDates/form.gi/config.xml')

    return result

  def page45(self):
    """GET translations.xml (requests 4501-4502)."""
    result = request4501.GET('/gi/apppath/SubstarctDates/form.gi/jss/translations.xml')

    grinder.sleep(88)
    request4502.GET('/gi/apppath/SubstarctDates/form.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://ramanujan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=26ac8b80354d82d1:-5e64727b:13bb6140d8e:-731e169.254.216.23436&type=PATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NjcwODQ1OCYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09NzYyNjMyNTA0ODg4ODgzMDI3OCYmdGltZXN0YW1wPT0xMzU1OTg2NzA4NDU4JiZkaWdlc3Q9PWVqeTMvckNTK2M2ZkI3cHB2ZWxZUWFtYWNUQT0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page46(self):
    """GET appCanvas.xml (requests 4601-4606)."""
    result = request4601.GET('/gi/apppath/SubstarctDates/form.gi/components/appCanvas.xml')

    grinder.sleep(58)
    request4602.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/Packages.js')

    grinder.sleep(58)
    request4603.GET('/gi/apppath/SubstarctDates/form.gi/js/logic.js')

    grinder.sleep(178)
    request4604.GET('/gi/apppath/SubstarctDates/form.gi/images/attachments.gif')

    request4605.GET('/gi/apppath/SubstarctDates/form.gi/images/close.png')

    request4606.GET('/gi/apppath/SubstarctDates/form.gi/images/error.gif')

    return result

  def page47(self):
    """GET TaskManagementServicesMapping.xml (request 4701)."""
    result = request4701.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page48(self):
    """GET Tidy.xsl (request 4801)."""
    result = request4801.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/Tidy.xsl')

    return result

  def page49(self):
    """POST validation (request 4901)."""
    result = request4901.POST('/gi/validation',
      ( NVPair('assembly', 'SubstarctDates'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>26ac8b80354d82d1:-5e64727b:13bb6140d8e:-731e169.254.216.23436</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NjcwODQ1OCYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09NzYyNjMyNTA0ODg4ODgzMDI3OCYmdGltZXN0YW1wPT0xMzU1OTg2NzA4NDU4JiZkaWdlc3Q9PWVqeTMvckNTK2M2ZkI3cHB2ZWxZUWFtYWNUQT0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page50(self):
    """GET FormModelMapping.xml (request 5001)."""
    result = request5001.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page51(self):
    """GET TaskManagerProcessMapping.xml (request 5101)."""
    result = request5101.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/TaskManagerProcessMapping.xml')

    return result

  def page52(self):
    """GET FormModelMapping.xml (request 5201)."""
    result = request5201.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page53(self):
    """POST validation (request 5301)."""
    result = request5301.POST('/gi/validation',
      ( NVPair('assembly', 'SubstarctDates'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:completeTaskRequest xmlns:jsx1=\"http://www.intalio.com/bpms/workflow/ib4p_20051115\"><jsx1:taskMetaData><jsx1:taskId>26ac8b80354d82d1:-5e64727b:13bb6140d8e:-731e169.254.216.23436</jsx1:taskId></jsx1:taskMetaData><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NjcwODQ1OCYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09NzYyNjMyNTA0ODg4ODgzMDI3OCYmdGltZXN0YW1wPT0xMzU1OTg2NzA4NDU4JiZkaWdlc3Q9PWVqeTMvckNTK2M2ZkI3cHB2ZWxZUWFtYWNUQT0mJiYmVE9LRU4=</jsx1:participantToken><jsx1:user>intalio\\admin</jsx1:user><jsx1:taskOutput><a0:FormModel xmlns:a0=\"http://www.intalio.com/gi/form.gi\"><result>-P22D</result></a0:FormModel></jsx1:taskOutput></jsx1:completeTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page54(self):
    """GET empty.jsp (request 5401)."""
    result = request5401.GET('/ui-fw/script/empty.jsp')

    return result

  def page55(self):
    """POST updates.htm (requests 5501-5502)."""
    result = request5501.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 10 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '26ac8b80354d82d1:7f1f730:13bb84af6cb:-37...'
    # 10 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/SampleAjaxPAWithTimer/sample...'

    grinder.sleep(380)
    request5502.GET('/ui-fw/images/ui-icons_ffffff_256x240.png')

    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    self.page1()      # GET tasks.htm (requests 101-130)
    self.page2()      # POST vacation.htm (request 201)

    grinder.sleep(108)
    self.page3()      # POST updates.htm (request 301)
    self.page4()      # POST updates.htm (request 401)
    self.page5()      # POST updates.htm (requests 501-521)
    self.page6()      # GET empty.jsp (requests 601-603)

    grinder.sleep(101)
    self.page7()      # POST updates.htm (request 701)

    grinder.sleep(1485)
    self.page8()      # GET / (requests 801-808)

    grinder.sleep(5818)
    self.page9()      # POST login.htm (requests 901-934)

    grinder.sleep(161)
    self.page10()     # GET data.json (requests 1001-1006)
    self.page11()     # GET templates.html (request 1101)
    self.page12()     # GET dsState.json (requests 1201-1203)

    grinder.sleep(559)
    self.page13()     # GET tasks.htm (requests 1301-1302)
    self.page14()     # GET login.htm (requests 1401-1432)

    grinder.sleep(81)
    self.page15()     # POST vacation.htm (requests 1501-1521)
    self.page16()     # GET empty.jsp (requests 1601-1602)

    grinder.sleep(439)
    self.page17()     # POST updates.htm (requests 1701-1703)

    grinder.sleep(1485)
    self.page18()     # POST updates.htm (requests 1801-1802)

    grinder.sleep(1013)
    self.page19()     # GET ServerLaunch.html (requests 1901-1905)
    self.page20()     # GET locale.xml (request 2001)
    self.page21()     # GET messages.xml (requests 2101-2102)
    self.page22()     # GET logger.xml (request 2201)

    grinder.sleep(78)
    self.page23()     # GET CSS.xml (request 2301)
    self.page24()     # GET config.xml (requests 2401-2402)

    grinder.sleep(69)
    self.page25()     # GET config.xml (request 2501)
    self.page26()     # GET translations.xml (request 2601)
    self.page27()     # GET appCanvas.xml (requests 2701-2723)

    grinder.sleep(18)
    self.page28()     # GET TaskManagementServicesMapping.xml (request 2801)

    grinder.sleep(54)
    self.page29()     # GET soap.xml (request 2901)
    self.page30()     # GET Tidy.xsl (request 3001)
    self.page31()     # POST validation (request 3101)

    grinder.sleep(12)
    self.page32()     # GET FormModelMapping.xml (request 3201)

    grinder.sleep(6098)
    self.page33()     # GET TaskManagementServicesMapping.xml (request 3301)

    grinder.sleep(20)
    self.page34()     # GET FormModelMapping.xml (request 3401)

    grinder.sleep(51)
    self.page35()     # POST validation (request 3501)

    grinder.sleep(14)
    self.page36()     # GET empty.jsp (request 3601)

    grinder.sleep(536)
    self.page37()     # POST updates.htm (request 3701)

    grinder.sleep(254)
    self.page38()     # POST updates.htm (requests 3801-3802)

    grinder.sleep(5367)
    self.page39()     # POST proxy.jsp (requests 3901-3903)

    grinder.sleep(1661)
    self.page40()     # POST proxy.jsp (request 4001)

    grinder.sleep(899)
    self.page41()     # POST proxy.jsp (request 4101)

    grinder.sleep(2709)
    self.page42()     # POST updates.htm (request 4201)

    grinder.sleep(6142)
    self.page43()     # GET ServerLaunch.html (request 4301)

    grinder.sleep(105)
    self.page44()     # GET config.xml (request 4401)
    self.page45()     # GET translations.xml (requests 4501-4502)
    self.page46()     # GET appCanvas.xml (requests 4601-4606)
    self.page47()     # GET TaskManagementServicesMapping.xml (request 4701)

    grinder.sleep(55)
    self.page48()     # GET Tidy.xsl (request 4801)
    self.page49()     # POST validation (request 4901)
    self.page50()     # GET FormModelMapping.xml (request 5001)

    grinder.sleep(1125)
    self.page51()     # GET TaskManagerProcessMapping.xml (request 5101)

    grinder.sleep(31)
    self.page52()     # GET FormModelMapping.xml (request 5201)

    grinder.sleep(47)
    self.page53()     # POST validation (request 5301)
    self.page54()     # GET empty.jsp (request 5401)

    grinder.sleep(526)
    self.page55()     # POST updates.htm (requests 5501-5502)


# Instrument page methods.
Test(100, 'Page 1').record(TestRunner.page1)
Test(200, 'Page 2').record(TestRunner.page2)
Test(300, 'Page 3').record(TestRunner.page3)
Test(400, 'Page 4').record(TestRunner.page4)
Test(500, 'Page 5').record(TestRunner.page5)
Test(600, 'Page 6').record(TestRunner.page6)
Test(700, 'Page 7').record(TestRunner.page7)
Test(800, 'Page 8').record(TestRunner.page8)
Test(900, 'Page 9').record(TestRunner.page9)
Test(1000, 'Page 10').record(TestRunner.page10)
Test(1100, 'Page 11').record(TestRunner.page11)
Test(1200, 'Page 12').record(TestRunner.page12)
Test(1300, 'Page 13').record(TestRunner.page13)
Test(1400, 'Page 14').record(TestRunner.page14)
Test(1500, 'Page 15').record(TestRunner.page15)
Test(1600, 'Page 16').record(TestRunner.page16)
Test(1700, 'Page 17').record(TestRunner.page17)
Test(1800, 'Page 18').record(TestRunner.page18)
Test(1900, 'Page 19').record(TestRunner.page19)
Test(2000, 'Page 20').record(TestRunner.page20)
Test(2100, 'Page 21').record(TestRunner.page21)
Test(2200, 'Page 22').record(TestRunner.page22)
Test(2300, 'Page 23').record(TestRunner.page23)
Test(2400, 'Page 24').record(TestRunner.page24)
Test(2500, 'Page 25').record(TestRunner.page25)
Test(2600, 'Page 26').record(TestRunner.page26)
Test(2700, 'Page 27').record(TestRunner.page27)
Test(2800, 'Page 28').record(TestRunner.page28)
Test(2900, 'Page 29').record(TestRunner.page29)
Test(3000, 'Page 30').record(TestRunner.page30)
Test(3100, 'Page 31').record(TestRunner.page31)
Test(3200, 'Page 32').record(TestRunner.page32)
Test(3300, 'Page 33').record(TestRunner.page33)
Test(3400, 'Page 34').record(TestRunner.page34)
Test(3500, 'Page 35').record(TestRunner.page35)
Test(3600, 'Page 36').record(TestRunner.page36)
Test(3700, 'Page 37').record(TestRunner.page37)
Test(3800, 'Page 38').record(TestRunner.page38)
Test(3900, 'Page 39').record(TestRunner.page39)
Test(4000, 'Page 40').record(TestRunner.page40)
Test(4100, 'Page 41').record(TestRunner.page41)
Test(4200, 'Page 42').record(TestRunner.page42)
Test(4300, 'Page 43').record(TestRunner.page43)
Test(4400, 'Page 44').record(TestRunner.page44)
Test(4500, 'Page 45').record(TestRunner.page45)
Test(4600, 'Page 46').record(TestRunner.page46)
Test(4700, 'Page 47').record(TestRunner.page47)
Test(4800, 'Page 48').record(TestRunner.page48)
Test(4900, 'Page 49').record(TestRunner.page49)
Test(5000, 'Page 50').record(TestRunner.page50)
Test(5100, 'Page 51').record(TestRunner.page51)
Test(5200, 'Page 52').record(TestRunner.page52)
Test(5300, 'Page 53').record(TestRunner.page53)
Test(5400, 'Page 54').record(TestRunner.page54)
Test(5500, 'Page 55').record(TestRunner.page55)
