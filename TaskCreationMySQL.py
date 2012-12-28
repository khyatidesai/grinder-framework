# The Grinder 3.10
# HTTP script recorded by TCPProxy at Dec 10, 2012 5:22:56 PM

from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair

from java.sql  import *
from java.lang import *
from com.mysql.jdbc import Driver
from java.lang.System import out 
from java.util import Random


DriverManager.registerDriver(Driver())


# Update Database properties

# def getConnection():
#    return DriverManager.getConnection(
#        "jdbc:oracle:thin:@bpmdbu21.sg.db.com:1531:HKBPMS", "BPMS52PROD", "Gat3waY234")

def getConnection():
    return DriverManager.getConnection(
        "jdbc:mysql://192.168.1.116:3306/bpmsdb_titan?useUnicode=true&characterEncoding=UTF-8&autoReconnect=true", "root", "")


def ensureClosed(object):
    try: object.close()
    except: pass


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
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers1= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/index.htm'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers2= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'http://titan:8080/index.htm'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers3= \
  [ NVPair('Accept', 'application/json, text/javascript, */*; q=0.01'),
    NVPair('Referer', 'http://titan:8080/index.htm'), ]

headers4= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/style/plugin/jquery.ui.theme.css'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers5= \
  [ NVPair('Accept', 'text/html, */*; q=0.01'),
    NVPair('Referer', 'http://titan:8080/index.htm'), ]

headers6= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/login.htm'), ]

headers7= \
  [ NVPair('Accept', 'application/json, text/javascript, */*; q=0.01'),
    NVPair('Referer', 'http://titan:8080/index.htm;jsessionid=0D7D89DBE69BEC9D45709F9FA00D92A9'), ]

headers8= \
  [ NVPair('Accept', 'text/html, */*; q=0.01'),
    NVPair('Referer', 'http://titan:8080/index.htm;jsessionid=0D7D89DBE69BEC9D45709F9FA00D92A9'), ]

headers9= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/index.htm;jsessionid=0D7D89DBE69BEC9D45709F9FA00D92A9'), ]

headers10= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/ui-fw/tasks.htm?null'), ]

headers11= \
  [ NVPair('Accept', 'application/xml, text/xml, */*; q=0.01'),
    NVPair('Referer', 'http://titan:8080/ui-fw/tasks.htm?null'),
    NVPair('Cache-Control', 'no-cache'), ]

headers12= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxTesting/form.gi/IntalioInternal/ServerLaunch.html?id=f1e71b24-a117-4cef-bcc8-aa2899e6e240&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxTesting%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers13= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxTesting/form.gi/IntalioInternal/ServerLaunch.html?id=f1e71b24-a117-4cef-bcc8-aa2899e6e240&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxTesting%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers14= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxTesting/form.gi/IntalioInternal/ServerLaunch.html?id=f1e71b24-a117-4cef-bcc8-aa2899e6e240&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxTesting%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers15= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxTesting/form.gi/IntalioInternal/ServerLaunch.html?id=f1e71b24-a117-4cef-bcc8-aa2899e6e240&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxTesting%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers16= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/ServerLaunch.html?id=3d124bc6-c2f2-4c7b-b7df-1c2dfe28aa0c&type=PIPATask&url=http%3A%2F%2Ftitan%3A8080%2Fgi%2Fapppath%2FScheduleActionPA%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers17= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/ServerLaunch.html?id=3d124bc6-c2f2-4c7b-b7df-1c2dfe28aa0c&type=PIPATask&url=http%3A%2F%2Ftitan%3A8080%2Fgi%2Fapppath%2FScheduleActionPA%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers18= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/ServerLaunch.html?id=3d124bc6-c2f2-4c7b-b7df-1c2dfe28aa0c&type=PIPATask&url=http%3A%2F%2Ftitan%3A8080%2Fgi%2Fapppath%2FScheduleActionPA%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers19= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/ServerLaunch.html?id=3d124bc6-c2f2-4c7b-b7df-1c2dfe28aa0c&type=PIPATask&url=http%3A%2F%2Ftitan%3A8080%2Fgi%2Fapppath%2FScheduleActionPA%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers20= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/xFormsManager/init?id=6c8f64ba-1c38-4dec-82e4-33a632752d4c&type=PIPATask&url=oxf%3A%2F%2FWorkflowTabPane%2Fdetails.xform&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers21= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/xFormsManager/init?id=6c8f64ba-1c38-4dec-82e4-33a632752d4c&type=PIPATask&url=oxf%3A%2F%2FWorkflowTabPane%2Fdetails.xform&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers22= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/ui-fw/tasks.htm'), ]

headers23= \
  [ NVPair('Accept', 'application/json, text/javascript, */*; q=0.01'),
    NVPair('Referer', 'http://titan:8080/ui-fw/tasks.htm'),
    NVPair('Cache-Control', 'no-cache'), ]

headers24= \
  [ NVPair('Accept', 'application/xml, text/xml, */*; q=0.01'),
    NVPair('Referer', 'http://titan:8080/ui-fw/tasks.htm'),
    NVPair('Cache-Control', 'no-cache'), ]

headers25= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/IntalioInternal/ServerLaunch.html?id=9652e37c-8ffb-494f-b736-81fd046c35cb&type=PIPATask&url=%2Fgi%2Fapppath%2FTestWidgetForMobile%2FIntalioWidgets.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers26= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/IntalioInternal/ServerLaunch.html?id=9652e37c-8ffb-494f-b736-81fd046c35cb&type=PIPATask&url=%2Fgi%2Fapppath%2FTestWidgetForMobile%2FIntalioWidgets.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers27= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/IntalioInternal/ServerLaunch.html?id=9652e37c-8ffb-494f-b736-81fd046c35cb&type=PIPATask&url=%2Fgi%2Fapppath%2FTestWidgetForMobile%2FIntalioWidgets.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers28= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=f973951f-16e0-459e-af0a-f2aaf6e8964b&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers29= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=f973951f-16e0-459e-af0a-f2aaf6e8964b&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers30= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=f973951f-16e0-459e-af0a-f2aaf6e8964b&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers31= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=f973951f-16e0-459e-af0a-f2aaf6e8964b&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers32= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/IntalioInternal/ServerLaunch.html?id=0cf9b4b5-9624-41ba-94b7-a420e29513e0&type=PIPATask&url=%2Fgi%2Fapppath%2FScheduleActions_PXEI_874%2FActionForms.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers33= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/IntalioInternal/ServerLaunch.html?id=0cf9b4b5-9624-41ba-94b7-a420e29513e0&type=PIPATask&url=%2Fgi%2Fapppath%2FScheduleActions_PXEI_874%2FActionForms.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers34= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/IntalioInternal/ServerLaunch.html?id=0cf9b4b5-9624-41ba-94b7-a420e29513e0&type=PIPATask&url=%2Fgi%2Fapppath%2FScheduleActions_PXEI_874%2FActionForms.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers35= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/IntalioInternal/ServerLaunch.html?id=0cf9b4b5-9624-41ba-94b7-a420e29513e0&type=PIPATask&url=%2Fgi%2Fapppath%2FScheduleActions_PXEI_874%2FActionForms.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers36= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/IntalioInternal/ServerLaunch.html?id=d8ae9f02-c9e9-4017-a33a-2c129d400e29&type=PIPATask&url=%2Fgi%2Fapppath%2FRepeatEvery_PXEI_897%2FForms%2Fstart.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers37= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/IntalioInternal/ServerLaunch.html?id=d8ae9f02-c9e9-4017-a33a-2c129d400e29&type=PIPATask&url=%2Fgi%2Fapppath%2FRepeatEvery_PXEI_897%2FForms%2Fstart.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers38= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/IntalioInternal/ServerLaunch.html?id=d8ae9f02-c9e9-4017-a33a-2c129d400e29&type=PIPATask&url=%2Fgi%2Fapppath%2FRepeatEvery_PXEI_897%2FForms%2Fstart.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers39= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/IntalioInternal/ServerLaunch.html?id=d8ae9f02-c9e9-4017-a33a-2c129d400e29&type=PIPATask&url=%2Fgi%2Fapppath%2FRepeatEvery_PXEI_897%2FForms%2Fstart.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers40= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/Ajax_Radio/Radiobuttons.gi/IntalioInternal/ServerLaunch.html?id=7647e069-9da2-4866-88d2-8f7f91b0db18&type=PIPATask&url=%2Fgi%2Fapppath%2FAjax_Radio%2FRadiobuttons.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers41= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/Ajax_Radio/Radiobuttons.gi/IntalioInternal/ServerLaunch.html?id=7647e069-9da2-4866-88d2-8f7f91b0db18&type=PIPATask&url=%2Fgi%2Fapppath%2FAjax_Radio%2FRadiobuttons.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers42= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/Ajax_Radio/Radiobuttons.gi/IntalioInternal/ServerLaunch.html?id=7647e069-9da2-4866-88d2-8f7f91b0db18&type=PIPATask&url=%2Fgi%2Fapppath%2FAjax_Radio%2FRadiobuttons.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers43= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/Ajax_Radio/Radiobuttons.gi/IntalioInternal/ServerLaunch.html?id=7647e069-9da2-4866-88d2-8f7f91b0db18&type=PIPATask&url=%2Fgi%2Fapppath%2FAjax_Radio%2FRadiobuttons.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers44= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/Ajax_Radio/Radiobuttons.gi/IntalioInternal/ServerLaunch.html?id=7647e069-9da2-4866-88d2-8f7f91b0db18&type=PIPATask&url=%2Fgi%2Fapppath%2FAjax_Radio%2FRadiobuttons.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers45= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxDatePicker/DatePicker.gi/IntalioInternal/ServerLaunch.html?id=5813e897-a8c8-48d8-96a7-fa864a420f2e&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxDatePicker%2FDatePicker.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers46= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxDatePicker/DatePicker.gi/IntalioInternal/ServerLaunch.html?id=5813e897-a8c8-48d8-96a7-fa864a420f2e&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxDatePicker%2FDatePicker.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers47= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxDatePicker/DatePicker.gi/IntalioInternal/ServerLaunch.html?id=5813e897-a8c8-48d8-96a7-fa864a420f2e&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxDatePicker%2FDatePicker.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers48= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/IntalioInternal/ServerLaunch.html?id=fa2a15cb-b048-4f17-a5b0-20e55c6a74b2&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxCheckbox%2FAjaxCheckbox.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers49= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/IntalioInternal/ServerLaunch.html?id=fa2a15cb-b048-4f17-a5b0-20e55c6a74b2&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxCheckbox%2FAjaxCheckbox.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers50= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/IntalioInternal/ServerLaunch.html?id=fa2a15cb-b048-4f17-a5b0-20e55c6a74b2&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxCheckbox%2FAjaxCheckbox.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers51= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/IntalioInternal/ServerLaunch.html?id=a9802d95-55dd-464e-93dd-c6eaf7d35d5f&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxChainedExecution%2FSelectTransportation.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers52= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/IntalioInternal/ServerLaunch.html?id=a9802d95-55dd-464e-93dd-c6eaf7d35d5f&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxChainedExecution%2FSelectTransportation.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers53= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/IntalioInternal/ServerLaunch.html?id=a9802d95-55dd-464e-93dd-c6eaf7d35d5f&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxChainedExecution%2FSelectTransportation.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers54= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/xFormsManager/init?id=8c9086f2-6ff4-4374-a570-3016ddec072e&type=PIPATask&url=%2FAbsenceRequest%2FAbsenceRequest.xform&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers55= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/xFormsManager/init?id=8c9086f2-6ff4-4374-a570-3016ddec072e&type=PIPATask&url=%2FAbsenceRequest%2FAbsenceRequest.xform&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers56= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/xFormsManager/act?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-1249127.0.0.184&type=PATask&url=http%3A%2F%2Flocalhost%3A8080%2Fwds%2FAbsenceRequest%2FAbsenceApproval.xform&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers57= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/xFormsManager/act?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-1249127.0.0.184&type=PATask&url=http%3A%2F%2Flocalhost%3A8080%2Fwds%2FAbsenceRequest%2FAbsenceApproval.xform&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers58= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/xFormsManager/act?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-1249127.0.0.184&type=PATask&url=http%3A%2F%2Flocalhost%3A8080%2Fwds%2FAbsenceRequest%2FAbsenceApproval.xform&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers59= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-127b127.0.0.180&type=PATask&url=%2Fgi%2Fapppath%2FRepeatEvery_PXEI_897%2FForms%2FPA.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers60= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-127b127.0.0.180&type=PATask&url=%2Fgi%2Fapppath%2FRepeatEvery_PXEI_897%2FForms%2FPA.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers61= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-127b127.0.0.180&type=PATask&url=%2Fgi%2Fapppath%2FRepeatEvery_PXEI_897%2FForms%2FPA.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers62= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-127b127.0.0.180&type=PATask&url=%2Fgi%2Fapppath%2FRepeatEvery_PXEI_897%2FForms%2FPA.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers63= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-1282127.0.0.174&type=PATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers64= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-1282127.0.0.174&type=PATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers65= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-1282127.0.0.174&type=PATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers66= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-1282127.0.0.174&type=PATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers67= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-12ac127.0.0.169&type=PATask&url=http%3A%2F%2Ftitan%3A8080%2Fgi%2Fapppath%2FScheduleActionPA%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers68= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-12ac127.0.0.169&type=PATask&url=http%3A%2F%2Ftitan%3A8080%2Fgi%2Fapppath%2FScheduleActionPA%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers69= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-12ac127.0.0.169&type=PATask&url=http%3A%2F%2Ftitan%3A8080%2Fgi%2Fapppath%2FScheduleActionPA%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers70= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-12ac127.0.0.169&type=PATask&url=http%3A%2F%2Ftitan%3A8080%2Fgi%2Fapppath%2FScheduleActionPA%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers71= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/xFormsManager/act?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-70a9127.0.0.161&type=PATask&url=http%3A%2F%2Flocalhost%3A8080%2Fwds%2FAbsenceRequest%2FAbsenceApproval.xform&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers72= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://titan:8080/xFormsManager/act?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-70a9127.0.0.161&type=PATask&url=http%3A%2F%2Flocalhost%3A8080%2Fwds%2FAbsenceRequest%2FAbsenceApproval.xform&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

url0 = 'http://titan:8080'

# Create an HTTPRequest for each request, then replace the
# reference to the HTTPRequest with an instrumented version.
# You can access the unadorned instance using request101.__target__.
request101 = HTTPRequest(url=url0, headers=headers0)
request101 = Test(101, 'GET /').wrap(request101)

request102 = HTTPRequest(url=url0, headers=headers0)
request102 = Test(102, 'GET login.htm').wrap(request102)

request103 = HTTPRequest(url=url0, headers=headers0)
request103 = Test(103, 'GET index.htm').wrap(request103)

request104 = HTTPRequest(url=url0, headers=headers1)
request104 = Test(104, 'GET jquery-1.8.2.js').wrap(request104)

request105 = HTTPRequest(url=url0, headers=headers1)
request105 = Test(105, 'GET jquery.ui.core.js').wrap(request105)

request106 = HTTPRequest(url=url0, headers=headers1)
request106 = Test(106, 'GET jquery.qtip.js').wrap(request106)

request107 = HTTPRequest(url=url0, headers=headers1)
request107 = Test(107, 'GET jquery-ui.js').wrap(request107)

request108 = HTTPRequest(url=url0, headers=headers1)
request108 = Test(108, 'GET jquery.dashboard.min.js').wrap(request108)

request109 = HTTPRequest(url=url0, headers=headers1)
request109 = Test(109, 'GET d3.v2.js').wrap(request109)

request110 = HTTPRequest(url=url0, headers=headers1)
request110 = Test(110, 'GET jquery.ui.button.js').wrap(request110)

request111 = HTTPRequest(url=url0, headers=headers1)
request111 = Test(111, 'GET jquery.ui.widget.js').wrap(request111)

request112 = HTTPRequest(url=url0, headers=headers1)
request112 = Test(112, 'GET nv.d3.js').wrap(request112)

request113 = HTTPRequest(url=url0, headers=headers1)
request113 = Test(113, 'GET utils.js').wrap(request113)

request114 = HTTPRequest(url=url0, headers=headers1)
request114 = Test(114, 'GET discreteBar.js').wrap(request114)

request115 = HTTPRequest(url=url0, headers=headers1)
request115 = Test(115, 'GET multiBar.js').wrap(request115)

request116 = HTTPRequest(url=url0, headers=headers1)
request116 = Test(116, 'GET discreteBarChart.js').wrap(request116)

request117 = HTTPRequest(url=url0, headers=headers1)
request117 = Test(117, 'GET tooltip.js').wrap(request117)

request118 = HTTPRequest(url=url0, headers=headers1)
request118 = Test(118, 'GET legend.js').wrap(request118)

request119 = HTTPRequest(url=url0, headers=headers1)
request119 = Test(119, 'GET multiBarChart.js').wrap(request119)

request120 = HTTPRequest(url=url0, headers=headers1)
request120 = Test(120, 'GET scatter.js').wrap(request120)

request121 = HTTPRequest(url=url0, headers=headers1)
request121 = Test(121, 'GET axis.js').wrap(request121)

request122 = HTTPRequest(url=url0, headers=headers1)
request122 = Test(122, 'GET line.js').wrap(request122)

request123 = HTTPRequest(url=url0, headers=headers1)
request123 = Test(123, 'GET themeroller.js').wrap(request123)

request124 = HTTPRequest(url=url0, headers=headers1)
request124 = Test(124, 'GET multiBarHorizontal.js').wrap(request124)

request125 = HTTPRequest(url=url0, headers=headers1)
request125 = Test(125, 'GET pieChart.js').wrap(request125)

request126 = HTTPRequest(url=url0, headers=headers1)
request126 = Test(126, 'GET pie.js').wrap(request126)

request127 = HTTPRequest(url=url0, headers=headers2)
request127 = Test(127, 'GET jquery-ui-1.9.0.css').wrap(request127)

request128 = HTTPRequest(url=url0, headers=headers1)
request128 = Test(128, 'GET dashboard.js').wrap(request128)

request129 = HTTPRequest(url=url0, headers=headers1)
request129 = Test(129, 'GET historicalBar.js').wrap(request129)

request130 = HTTPRequest(url=url0, headers=headers1)
request130 = Test(130, 'GET linePlusBarChart.js').wrap(request130)

request131 = HTTPRequest(url=url0, headers=headers1)
request131 = Test(131, 'GET jquery.dataTables.js').wrap(request131)

request132 = HTTPRequest(url=url0, headers=headers1)
request132 = Test(132, 'GET multiBarHorizontalChart.js').wrap(request132)

request133 = HTTPRequest(url=url0, headers=headers2)
request133 = Test(133, 'GET jquery.dataTables.css').wrap(request133)

request134 = HTTPRequest(url=url0, headers=headers1)
request134 = Test(134, 'GET jquery-dateFormat.js').wrap(request134)

request135 = HTTPRequest(url=url0, headers=headers2)
request135 = Test(135, 'GET jquery.ui.theme.css').wrap(request135)

request136 = HTTPRequest(url=url0, headers=headers2)
request136 = Test(136, 'GET jquery.qtip.css').wrap(request136)

request137 = HTTPRequest(url=url0, headers=headers2)
request137 = Test(137, 'GET nv.d3.css').wrap(request137)

request138 = HTTPRequest(url=url0, headers=headers2)
request138 = Test(138, 'GET dashboardui.css').wrap(request138)

request139 = HTTPRequest(url=url0)
request139 = Test(139, 'GET logo.png').wrap(request139)

request201 = HTTPRequest(url=url0, headers=headers3)
request201 = Test(201, 'GET data.json').wrap(request201)

request202 = HTTPRequest(url=url0)
request202 = Test(202, 'GET loading.gif').wrap(request202)

request203 = HTTPRequest(url=url0, headers=headers4)
request203 = Test(203, 'GET ui-bg_highlight-soft_100_f6f6f6_1x100.png').wrap(request203)

request204 = HTTPRequest(url=url0, headers=headers4)
request204 = Test(204, 'GET ui-icons_666666_256x240.png').wrap(request204)

request205 = HTTPRequest(url=url0, headers=headers4)
request205 = Test(205, 'GET ui-bg_flat_75_ffffff_40x100.png').wrap(request205)

request301 = HTTPRequest(url=url0)
request301 = Test(301, 'GET templates.html').wrap(request301)

request302 = HTTPRequest(url=url0, headers=headers4)
request302 = Test(302, 'GET ui-bg_highlight-soft_50_dddddd_1x100.png').wrap(request302)

request401 = HTTPRequest(url=url0, headers=headers3)
request401 = Test(401, 'GET dsState.json').wrap(request401)

request402 = HTTPRequest(url=url0, headers=headers4)
request402 = Test(402, 'GET ui-icons_0073ea_256x240.png').wrap(request402)

request501 = HTTPRequest(url=url0, headers=headers5)
request501 = Test(501, 'GET task_summary.jsp').wrap(request501)

request601 = HTTPRequest(url=url0, headers=headers5)
request601 = Test(601, 'GET user_task_count.jsp').wrap(request601)

request701 = HTTPRequest(url=url0, headers=headers5)
request701 = Test(701, 'GET notifications.jsp').wrap(request701)

request801 = HTTPRequest(url=url0, headers=headers5)
request801 = Test(801, 'GET instance_status_cnt.jsp').wrap(request801)

request901 = HTTPRequest(url=url0, headers=headers5)
request901 = Test(901, 'GET ws_response_time.jsp').wrap(request901)

request1001 = HTTPRequest(url=url0, headers=headers5)
request1001 = Test(1001, 'GET avg_completion_time.jsp').wrap(request1001)

request1101 = HTTPRequest(url=url0, headers=headers5)
request1101 = Test(1101, 'GET vacation_summary.jsp').wrap(request1101)

request1102 = HTTPRequest(url=url0, headers=headers4)
request1102 = Test(1102, 'GET ui-bg_glass_65_ffffff_1x400.png').wrap(request1102)

request1103 = HTTPRequest(url=url0, headers=headers4)
request1103 = Test(1103, 'GET ui-icons_454545_256x240.png').wrap(request1103)

request1201 = HTTPRequest(url=url0, headers=headers5)
request1201 = Test(1201, 'GET notifications.jsp').wrap(request1201)

request1301 = HTTPRequest(url=url0, headers=headers5)
request1301 = Test(1301, 'GET vacation_summary.jsp').wrap(request1301)

request1401 = HTTPRequest(url=url0, headers=headers5)
request1401 = Test(1401, 'GET task_summary.jsp').wrap(request1401)

request1402 = HTTPRequest(url=url0)
request1402 = Test(1402, 'GET sort_both.png').wrap(request1402)

request1501 = HTTPRequest(url=url0, headers=headers5)
request1501 = Test(1501, 'GET user_task_count.jsp').wrap(request1501)

request1601 = HTTPRequest(url=url0, headers=headers5)
request1601 = Test(1601, 'GET avg_completion_time.jsp').wrap(request1601)

request1701 = HTTPRequest(url=url0, headers=headers5)
request1701 = Test(1701, 'GET instance_status_cnt.jsp').wrap(request1701)

request1801 = HTTPRequest(url=url0, headers=headers5)
request1801 = Test(1801, 'GET ws_response_time.jsp').wrap(request1801)

request1802 = HTTPRequest(url=url0, headers=headers4)
request1802 = Test(1802, 'GET ui-bg_highlight-soft_25_0073ea_1x100.png').wrap(request1802)

request1803 = HTTPRequest(url=url0)
request1803 = Test(1803, 'GET ui-icons_ffffff_256x240.png').wrap(request1803)

request1901 = HTTPRequest(url=url0)
request1901 = Test(1901, 'POST login.htm').wrap(request1901)

request2001 = HTTPRequest(url=url0, headers=headers6)
request2001 = Test(2001, 'POST login.htm').wrap(request2001)

request2002 = HTTPRequest(url=url0, headers=headers6)
request2002 = Test(2002, 'GET index.htm').wrap(request2002)

request2101 = HTTPRequest(url=url0, headers=headers7)
request2101 = Test(2101, 'GET data.json').wrap(request2101)

request2201 = HTTPRequest(url=url0, headers=headers7)
request2201 = Test(2201, 'GET dsState.json').wrap(request2201)

request2301 = HTTPRequest(url=url0, headers=headers8)
request2301 = Test(2301, 'GET vacation_summary.jsp').wrap(request2301)

request2401 = HTTPRequest(url=url0, headers=headers8)
request2401 = Test(2401, 'GET instance_status_cnt.jsp').wrap(request2401)

request2501 = HTTPRequest(url=url0, headers=headers8)
request2501 = Test(2501, 'GET notifications.jsp').wrap(request2501)

request2601 = HTTPRequest(url=url0, headers=headers8)
request2601 = Test(2601, 'GET user_task_count.jsp').wrap(request2601)

request2701 = HTTPRequest(url=url0, headers=headers8)
request2701 = Test(2701, 'GET task_summary.jsp').wrap(request2701)

request2801 = HTTPRequest(url=url0, headers=headers8)
request2801 = Test(2801, 'GET avg_completion_time.jsp').wrap(request2801)

request2901 = HTTPRequest(url=url0, headers=headers8)
request2901 = Test(2901, 'GET ws_response_time.jsp').wrap(request2901)

request3001 = HTTPRequest(url=url0, headers=headers8)
request3001 = Test(3001, 'GET user_task_count.jsp').wrap(request3001)

request3101 = HTTPRequest(url=url0, headers=headers8)
request3101 = Test(3101, 'GET notifications.jsp').wrap(request3101)

request3201 = HTTPRequest(url=url0, headers=headers8)
request3201 = Test(3201, 'GET vacation_summary.jsp').wrap(request3201)

request3301 = HTTPRequest(url=url0, headers=headers8)
request3301 = Test(3301, 'GET task_summary.jsp').wrap(request3301)

request3401 = HTTPRequest(url=url0, headers=headers8)
request3401 = Test(3401, 'GET avg_completion_time.jsp').wrap(request3401)

request3501 = HTTPRequest(url=url0, headers=headers8)
request3501 = Test(3501, 'GET instance_status_cnt.jsp').wrap(request3501)

request3601 = HTTPRequest(url=url0, headers=headers8)
request3601 = Test(3601, 'GET ws_response_time.jsp').wrap(request3601)

request3701 = HTTPRequest(url=url0, headers=headers9)
request3701 = Test(3701, 'GET tasks.htm').wrap(request3701)

request3702 = HTTPRequest(url=url0, headers=headers9)
request3702 = Test(3702, 'GET login.htm').wrap(request3702)

request3703 = HTTPRequest(url=url0, headers=headers9)
request3703 = Test(3703, 'GET tasks.htm').wrap(request3703)

request3801 = HTTPRequest(url=url0, headers=headers10)
request3801 = Test(3801, 'GET empty.jsp').wrap(request3801)

request3901 = HTTPRequest(url=url0)
request3901 = Test(3901, 'POST vacation.htm').wrap(request3901)

request4001 = HTTPRequest(url=url0, headers=headers11)
request4001 = Test(4001, 'POST updates.htm').wrap(request4001)

request4101 = HTTPRequest(url=url0, headers=headers11)
request4101 = Test(4101, 'POST updates.htm').wrap(request4101)

request4201 = HTTPRequest(url=url0, headers=headers11)
request4201 = Test(4201, 'POST updates.htm').wrap(request4201)

request4301 = HTTPRequest(url=url0, headers=headers10)
request4301 = Test(4301, 'GET empty.jsp').wrap(request4301)

request4401 = HTTPRequest(url=url0, headers=headers11)
request4401 = Test(4401, 'POST updates.htm').wrap(request4401)

request4501 = HTTPRequest(url=url0, headers=headers11)
request4501 = Test(4501, 'POST updates.htm').wrap(request4501)

request4601 = HTTPRequest(url=url0, headers=headers10)
request4601 = Test(4601, 'GET ServerLaunch.html').wrap(request4601)

request4701 = HTTPRequest(url=url0, headers=headers12)
request4701 = Test(4701, 'GET config.xml').wrap(request4701)

request4702 = HTTPRequest(url=url0)
request4702 = Test(4702, 'GET style.css').wrap(request4702)

request4801 = HTTPRequest(url=url0, headers=headers12)
request4801 = Test(4801, 'GET appCanvas.xml').wrap(request4801)

request4901 = HTTPRequest(url=url0, headers=headers12)
request4901 = Test(4901, 'GET translations.xml').wrap(request4901)

request4902 = HTTPRequest(url=url0, headers=headers13)
request4902 = Test(4902, 'GET Packages.js').wrap(request4902)

request4903 = HTTPRequest(url=url0, headers=headers13)
request4903 = Test(4903, 'GET logic.js').wrap(request4903)

request4904 = HTTPRequest(url=url0, headers=headers14)
request4904 = Test(4904, 'GET attachments.gif').wrap(request4904)

request4905 = HTTPRequest(url=url0, headers=headers14)
request4905 = Test(4905, 'GET close.png').wrap(request4905)

request4906 = HTTPRequest(url=url0, headers=headers14)
request4906 = Test(4906, 'GET error.gif').wrap(request4906)

request5001 = HTTPRequest(url=url0, headers=headers12)
request5001 = Test(5001, 'GET TaskManagementServicesMapping.xml').wrap(request5001)

request5101 = HTTPRequest(url=url0, headers=headers12)
request5101 = Test(5101, 'GET Tidy.xsl').wrap(request5101)

request5201 = HTTPRequest(url=url0, headers=headers15)
request5201 = Test(5201, 'POST validation').wrap(request5201)

# Insert a comment and press enter
# 
# 
# Create Init TASK from PIPA
request5301 = HTTPRequest(url=url0, headers=headers12)
request5301 = Test(5301, 'GET TaskManagementServicesMapping.xml').wrap(request5301)

request5401 = HTTPRequest(url=url0, headers=headers12)
request5401 = Test(5401, 'GET FormModelMapping.xml').wrap(request5401)

request5501 = HTTPRequest(url=url0, headers=headers15)
request5501 = Test(5501, 'POST validation').wrap(request5501)

request5601 = HTTPRequest(url=url0, headers=headers12)
request5601 = Test(5601, 'GET empty.jsp').wrap(request5601)

request5701 = HTTPRequest(url=url0, headers=headers11)
request5701 = Test(5701, 'POST updates.htm').wrap(request5701)

request5801 = HTTPRequest(url=url0, headers=headers10)
request5801 = Test(5801, 'GET ServerLaunch.html').wrap(request5801)

request5901 = HTTPRequest(url=url0, headers=headers16)
request5901 = Test(5901, 'GET config.xml').wrap(request5901)

request5902 = HTTPRequest(url=url0)
request5902 = Test(5902, 'GET style.css').wrap(request5902)

request6001 = HTTPRequest(url=url0, headers=headers16)
request6001 = Test(6001, 'GET translations.xml').wrap(request6001)

request6101 = HTTPRequest(url=url0, headers=headers16)
request6101 = Test(6101, 'GET appCanvas.xml').wrap(request6101)

request6102 = HTTPRequest(url=url0, headers=headers17)
request6102 = Test(6102, 'GET Packages.js').wrap(request6102)

request6103 = HTTPRequest(url=url0, headers=headers17)
request6103 = Test(6103, 'GET logic.js').wrap(request6103)

request6104 = HTTPRequest(url=url0, headers=headers18)
request6104 = Test(6104, 'GET attachments.gif').wrap(request6104)

request6105 = HTTPRequest(url=url0, headers=headers18)
request6105 = Test(6105, 'GET close.png').wrap(request6105)

request6106 = HTTPRequest(url=url0, headers=headers18)
request6106 = Test(6106, 'GET error.gif').wrap(request6106)

request6201 = HTTPRequest(url=url0, headers=headers16)
request6201 = Test(6201, 'GET TaskManagementServicesMapping.xml').wrap(request6201)

request6301 = HTTPRequest(url=url0, headers=headers16)
request6301 = Test(6301, 'GET Tidy.xsl').wrap(request6301)

request6401 = HTTPRequest(url=url0, headers=headers19)
request6401 = Test(6401, 'POST validation').wrap(request6401)

# NEW PIPA FORM
request6501 = HTTPRequest(url=url0, headers=headers16)
request6501 = Test(6501, 'GET TaskManagementServicesMapping.xml').wrap(request6501)

request6601 = HTTPRequest(url=url0, headers=headers16)
request6601 = Test(6601, 'GET FormModelMapping.xml').wrap(request6601)

request6701 = HTTPRequest(url=url0, headers=headers19)
request6701 = Test(6701, 'POST validation').wrap(request6701)

request6801 = HTTPRequest(url=url0, headers=headers16)
request6801 = Test(6801, 'GET empty.jsp').wrap(request6801)

request6901 = HTTPRequest(url=url0, headers=headers11)
request6901 = Test(6901, 'POST updates.htm').wrap(request6901)

request7001 = HTTPRequest(url=url0, headers=headers10)
request7001 = Test(7001, 'GET init').wrap(request7001)

request7101 = HTTPRequest(url=url0, headers=headers20)
request7101 = Test(7101, 'POST xforms-server').wrap(request7101)

# Worplow PIPA tab form
request7201 = HTTPRequest(url=url0, headers=headers20)
request7201 = Test(7201, 'POST xforms-server').wrap(request7201)

request7301 = HTTPRequest(url=url0, headers=headers21)
request7301 = Test(7301, 'POST init').wrap(request7301)

request7401 = HTTPRequest(url=url0, headers=headers21)
request7401 = Test(7401, 'GET tasks.htm').wrap(request7401)

request7501 = HTTPRequest(url=url0, headers=headers22)
request7501 = Test(7501, 'GET empty.jsp').wrap(request7501)

request7601 = HTTPRequest(url=url0, headers=headers23)
request7601 = Test(7601, 'POST vacation.htm').wrap(request7601)

request7701 = HTTPRequest(url=url0, headers=headers24)
request7701 = Test(7701, 'POST updates.htm').wrap(request7701)

request7801 = HTTPRequest(url=url0, headers=headers24)
request7801 = Test(7801, 'POST updates.htm').wrap(request7801)

request7901 = HTTPRequest(url=url0, headers=headers24)
request7901 = Test(7901, 'POST updates.htm').wrap(request7901)

request8001 = HTTPRequest(url=url0, headers=headers22)
request8001 = Test(8001, 'GET empty.jsp').wrap(request8001)

request8101 = HTTPRequest(url=url0, headers=headers24)
request8101 = Test(8101, 'POST updates.htm').wrap(request8101)

request8201 = HTTPRequest(url=url0, headers=headers24)
request8201 = Test(8201, 'POST updates.htm').wrap(request8201)

request8301 = HTTPRequest(url=url0, headers=headers22)
request8301 = Test(8301, 'GET ServerLaunch.html').wrap(request8301)

request8401 = HTTPRequest(url=url0, headers=headers25)
request8401 = Test(8401, 'GET config.xml').wrap(request8401)

request8402 = HTTPRequest(url=url0)
request8402 = Test(8402, 'GET style.css').wrap(request8402)

request8501 = HTTPRequest(url=url0, headers=headers25)
request8501 = Test(8501, 'GET translations.xml').wrap(request8501)

request8601 = HTTPRequest(url=url0, headers=headers25)
request8601 = Test(8601, 'GET appCanvas.xml').wrap(request8601)

request8602 = HTTPRequest(url=url0, headers=headers26)
request8602 = Test(8602, 'GET Packages.js').wrap(request8602)

request8603 = HTTPRequest(url=url0, headers=headers26)
request8603 = Test(8603, 'GET logic.js').wrap(request8603)

request8604 = HTTPRequest(url=url0, headers=headers25)
request8604 = Test(8604, 'GET FileUpload.js').wrap(request8604)

request8605 = HTTPRequest(url=url0, headers=headers25)
request8605 = Test(8605, 'GET ImageButton.js').wrap(request8605)

request8606 = HTTPRequest(url=url0, headers=headers25)
request8606 = Test(8606, 'GET ColorPicker.js').wrap(request8606)

request8607 = HTTPRequest(url=url0, headers=headers25)
request8607 = Test(8607, 'GET Title.js').wrap(request8607)

request8608 = HTTPRequest(url=url0, headers=headers25)
request8608 = Test(8608, 'GET TimePicker.js').wrap(request8608)

request8609 = HTTPRequest(url=url0, headers=headers25)
request8609 = Test(8609, 'GET Slider.js').wrap(request8609)

request8610 = HTTPRequest(url=url0, headers=headers27)
request8610 = Test(8610, 'GET saturation-v.png').wrap(request8610)

request8611 = HTTPRequest(url=url0, headers=headers27)
request8611 = Test(8611, 'GET d1arrow.gif').wrap(request8611)

request8612 = HTTPRequest(url=url0, headers=headers27)
request8612 = Test(8612, 'GET hue-h.png').wrap(request8612)

request8613 = HTTPRequest(url=url0, headers=headers27)
request8613 = Test(8613, 'GET brightness-v.png').wrap(request8613)

request8614 = HTTPRequest(url=url0, headers=headers27)
request8614 = Test(8614, 'GET hue-v.png').wrap(request8614)

request8615 = HTTPRequest(url=url0, headers=headers27)
request8615 = Test(8615, 'GET saturation-h.png').wrap(request8615)

request8616 = HTTPRequest(url=url0, headers=headers25)
request8616 = Test(8616, 'GET IFrame.js').wrap(request8616)

request8617 = HTTPRequest(url=url0, headers=headers27)
request8617 = Test(8617, 'GET spin_up.gif').wrap(request8617)

request8618 = HTTPRequest(url=url0, headers=headers27)
request8618 = Test(8618, 'GET spin_down.gif').wrap(request8618)

request8619 = HTTPRequest(url=url0, headers=headers27)
request8619 = Test(8619, 'GET close.png').wrap(request8619)

request8620 = HTTPRequest(url=url0, headers=headers27)
request8620 = Test(8620, 'GET attachments.gif').wrap(request8620)

request8621 = HTTPRequest(url=url0, headers=headers27)
request8621 = Test(8621, 'GET error.gif').wrap(request8621)

request8622 = HTTPRequest(url=url0, headers=headers27)
request8622 = Test(8622, 'GET folder.gif').wrap(request8622)

request8623 = HTTPRequest(url=url0, headers=headers27)
request8623 = Test(8623, 'GET v.png').wrap(request8623)

request8624 = HTTPRequest(url=url0, headers=headers27)
request8624 = Test(8624, 'GET sort_desc.gif').wrap(request8624)

request8625 = HTTPRequest(url=url0, headers=headers27)
request8625 = Test(8625, 'GET top.gif').wrap(request8625)

request8626 = HTTPRequest(url=url0, headers=headers27)
request8626 = Test(8626, 'GET minus.gif').wrap(request8626)

request8701 = HTTPRequest(url=url0, headers=headers25)
request8701 = Test(8701, 'GET TaskManagementServicesMapping.xml').wrap(request8701)

request8702 = HTTPRequest(url=url0, headers=headers27)
request8702 = Test(8702, 'GET plus.gif').wrap(request8702)

request8801 = HTTPRequest(url=url0, headers=headers25)
request8801 = Test(8801, 'GET Tidy.xsl').wrap(request8801)

request8901 = HTTPRequest(url=url0)
request8901 = Test(8901, 'POST validation').wrap(request8901)

request8902 = HTTPRequest(url=url0, headers=headers27)
request8902 = Test(8902, 'GET logo_16.gif').wrap(request8902)

request8903 = HTTPRequest(url=url0, headers=headers27)
request8903 = Test(8903, 'GET delete.gif').wrap(request8903)

request9001 = HTTPRequest(url=url0, headers=headers24)
request9001 = Test(9001, 'POST updates.htm').wrap(request9001)

request9101 = HTTPRequest(url=url0, headers=headers22)
request9101 = Test(9101, 'GET empty.jsp').wrap(request9101)

request9201 = HTTPRequest(url=url0, headers=headers24)
request9201 = Test(9201, 'POST updates.htm').wrap(request9201)

request9301 = HTTPRequest(url=url0, headers=headers22)
request9301 = Test(9301, 'GET ServerLaunch.html').wrap(request9301)

request9401 = HTTPRequest(url=url0, headers=headers28)
request9401 = Test(9401, 'GET config.xml').wrap(request9401)

request9402 = HTTPRequest(url=url0)
request9402 = Test(9402, 'GET style.css').wrap(request9402)

request9501 = HTTPRequest(url=url0, headers=headers28)
request9501 = Test(9501, 'GET translations.xml').wrap(request9501)

request9601 = HTTPRequest(url=url0, headers=headers28)
request9601 = Test(9601, 'GET appCanvas.xml').wrap(request9601)

request9602 = HTTPRequest(url=url0, headers=headers29)
request9602 = Test(9602, 'GET Packages.js').wrap(request9602)

request9603 = HTTPRequest(url=url0, headers=headers29)
request9603 = Test(9603, 'GET logic.js').wrap(request9603)

request9604 = HTTPRequest(url=url0, headers=headers30)
request9604 = Test(9604, 'GET attachments.gif').wrap(request9604)

request9605 = HTTPRequest(url=url0, headers=headers30)
request9605 = Test(9605, 'GET close.png').wrap(request9605)

request9606 = HTTPRequest(url=url0, headers=headers30)
request9606 = Test(9606, 'GET error.gif').wrap(request9606)

request9701 = HTTPRequest(url=url0, headers=headers28)
request9701 = Test(9701, 'GET TaskManagementServicesMapping.xml').wrap(request9701)

request9801 = HTTPRequest(url=url0, headers=headers28)
request9801 = Test(9801, 'GET Tidy.xsl').wrap(request9801)

request9901 = HTTPRequest(url=url0, headers=headers31)
request9901 = Test(9901, 'POST validation').wrap(request9901)

# Subtract Dates - PIPA
request10001 = HTTPRequest(url=url0, headers=headers28)
request10001 = Test(10001, 'GET TaskManagementServicesMapping.xml').wrap(request10001)

request10101 = HTTPRequest(url=url0, headers=headers28)
request10101 = Test(10101, 'GET FormModelMapping.xml').wrap(request10101)

request10201 = HTTPRequest(url=url0, headers=headers31)
request10201 = Test(10201, 'POST validation').wrap(request10201)

request10301 = HTTPRequest(url=url0, headers=headers28)
request10301 = Test(10301, 'GET empty.jsp').wrap(request10301)

request10401 = HTTPRequest(url=url0, headers=headers24)
request10401 = Test(10401, 'POST updates.htm').wrap(request10401)

request10501 = HTTPRequest(url=url0, headers=headers22)
request10501 = Test(10501, 'GET ServerLaunch.html').wrap(request10501)

request10601 = HTTPRequest(url=url0, headers=headers32)
request10601 = Test(10601, 'GET config.xml').wrap(request10601)

request10602 = HTTPRequest(url=url0)
request10602 = Test(10602, 'GET style.css').wrap(request10602)

request10701 = HTTPRequest(url=url0, headers=headers32)
request10701 = Test(10701, 'GET translations.xml').wrap(request10701)

request10801 = HTTPRequest(url=url0, headers=headers32)
request10801 = Test(10801, 'GET appCanvas.xml').wrap(request10801)

request10802 = HTTPRequest(url=url0, headers=headers33)
request10802 = Test(10802, 'GET Packages.js').wrap(request10802)

request10803 = HTTPRequest(url=url0, headers=headers33)
request10803 = Test(10803, 'GET logic.js').wrap(request10803)

request10804 = HTTPRequest(url=url0, headers=headers34)
request10804 = Test(10804, 'GET attachments.gif').wrap(request10804)

request10805 = HTTPRequest(url=url0, headers=headers34)
request10805 = Test(10805, 'GET error.gif').wrap(request10805)

request10806 = HTTPRequest(url=url0, headers=headers34)
request10806 = Test(10806, 'GET close.png').wrap(request10806)

request10901 = HTTPRequest(url=url0, headers=headers32)
request10901 = Test(10901, 'GET TaskManagementServicesMapping.xml').wrap(request10901)

request11001 = HTTPRequest(url=url0, headers=headers32)
request11001 = Test(11001, 'GET Tidy.xsl').wrap(request11001)

request11101 = HTTPRequest(url=url0, headers=headers35)
request11101 = Test(11101, 'POST validation').wrap(request11101)

# Action PIPA Form
request11201 = HTTPRequest(url=url0, headers=headers32)
request11201 = Test(11201, 'GET TaskManagementServicesMapping.xml').wrap(request11201)

request11301 = HTTPRequest(url=url0, headers=headers32)
request11301 = Test(11301, 'GET FormModelMapping.xml').wrap(request11301)

request11401 = HTTPRequest(url=url0, headers=headers35)
request11401 = Test(11401, 'POST validation').wrap(request11401)

request11501 = HTTPRequest(url=url0, headers=headers32)
request11501 = Test(11501, 'GET empty.jsp').wrap(request11501)

request11601 = HTTPRequest(url=url0, headers=headers24)
request11601 = Test(11601, 'POST updates.htm').wrap(request11601)

request11701 = HTTPRequest(url=url0, headers=headers22)
request11701 = Test(11701, 'GET ServerLaunch.html').wrap(request11701)

request11801 = HTTPRequest(url=url0, headers=headers36)
request11801 = Test(11801, 'GET config.xml').wrap(request11801)

request11802 = HTTPRequest(url=url0)
request11802 = Test(11802, 'GET style.css').wrap(request11802)

request11901 = HTTPRequest(url=url0, headers=headers36)
request11901 = Test(11901, 'GET appCanvas.xml').wrap(request11901)

request12001 = HTTPRequest(url=url0, headers=headers36)
request12001 = Test(12001, 'GET translations.xml').wrap(request12001)

request12002 = HTTPRequest(url=url0, headers=headers37)
request12002 = Test(12002, 'GET Packages.js').wrap(request12002)

request12003 = HTTPRequest(url=url0, headers=headers37)
request12003 = Test(12003, 'GET logic.js').wrap(request12003)

request12004 = HTTPRequest(url=url0, headers=headers38)
request12004 = Test(12004, 'GET attachments.gif').wrap(request12004)

request12005 = HTTPRequest(url=url0, headers=headers38)
request12005 = Test(12005, 'GET close.png').wrap(request12005)

request12101 = HTTPRequest(url=url0, headers=headers36)
request12101 = Test(12101, 'GET TaskManagementServicesMapping.xml').wrap(request12101)

request12201 = HTTPRequest(url=url0, headers=headers36)
request12201 = Test(12201, 'GET Tidy.xsl').wrap(request12201)

request12301 = HTTPRequest(url=url0, headers=headers39)
request12301 = Test(12301, 'POST validation').wrap(request12301)

# Start Repeat Every Pipa
request12401 = HTTPRequest(url=url0, headers=headers36)
request12401 = Test(12401, 'GET TaskManagementServicesMapping.xml').wrap(request12401)

request12501 = HTTPRequest(url=url0, headers=headers36)
request12501 = Test(12501, 'GET FormModelMapping.xml').wrap(request12501)

request12601 = HTTPRequest(url=url0, headers=headers39)
request12601 = Test(12601, 'POST validation').wrap(request12601)

request12701 = HTTPRequest(url=url0, headers=headers36)
request12701 = Test(12701, 'GET empty.jsp').wrap(request12701)

request12801 = HTTPRequest(url=url0, headers=headers24)
request12801 = Test(12801, 'POST updates.htm').wrap(request12801)

request12901 = HTTPRequest(url=url0, headers=headers22)
request12901 = Test(12901, 'GET ServerLaunch.html').wrap(request12901)

request13001 = HTTPRequest(url=url0, headers=headers40)
request13001 = Test(13001, 'GET config.xml').wrap(request13001)

request13101 = HTTPRequest(url=url0, headers=headers40)
request13101 = Test(13101, 'GET translations.xml').wrap(request13101)

request13102 = HTTPRequest(url=url0, headers=headers41)
request13102 = Test(13102, 'GET style.css').wrap(request13102)

request13201 = HTTPRequest(url=url0, headers=headers40)
request13201 = Test(13201, 'GET appCanvas.xml').wrap(request13201)

request13202 = HTTPRequest(url=url0, headers=headers42)
request13202 = Test(13202, 'GET Packages.js').wrap(request13202)

request13203 = HTTPRequest(url=url0, headers=headers42)
request13203 = Test(13203, 'GET logic.js').wrap(request13203)

request13204 = HTTPRequest(url=url0, headers=headers43)
request13204 = Test(13204, 'GET attachments.gif').wrap(request13204)

request13205 = HTTPRequest(url=url0, headers=headers43)
request13205 = Test(13205, 'GET close.png').wrap(request13205)

request13206 = HTTPRequest(url=url0, headers=headers43)
request13206 = Test(13206, 'GET error.gif').wrap(request13206)

request13301 = HTTPRequest(url=url0, headers=headers40)
request13301 = Test(13301, 'GET TaskManagementServicesMapping.xml').wrap(request13301)

request13401 = HTTPRequest(url=url0, headers=headers40)
request13401 = Test(13401, 'GET Tidy.xsl').wrap(request13401)

request13501 = HTTPRequest(url=url0, headers=headers44)
request13501 = Test(13501, 'POST validation').wrap(request13501)

# Ajax Radio PIPA
request13601 = HTTPRequest(url=url0, headers=headers24)
request13601 = Test(13601, 'POST updates.htm').wrap(request13601)

request13701 = HTTPRequest(url=url0, headers=headers22)
request13701 = Test(13701, 'GET ServerLaunch.html').wrap(request13701)

request13801 = HTTPRequest(url=url0, headers=headers40)
request13801 = Test(13801, 'GET config.xml').wrap(request13801)

request13802 = HTTPRequest(url=url0, headers=headers41)
request13802 = Test(13802, 'GET style.css').wrap(request13802)

request13901 = HTTPRequest(url=url0, headers=headers40)
request13901 = Test(13901, 'GET appCanvas.xml').wrap(request13901)

request14001 = HTTPRequest(url=url0, headers=headers40)
request14001 = Test(14001, 'GET translations.xml').wrap(request14001)

request14002 = HTTPRequest(url=url0, headers=headers42)
request14002 = Test(14002, 'GET Packages.js').wrap(request14002)

request14003 = HTTPRequest(url=url0, headers=headers42)
request14003 = Test(14003, 'GET logic.js').wrap(request14003)

request14004 = HTTPRequest(url=url0, headers=headers43)
request14004 = Test(14004, 'GET attachments.gif').wrap(request14004)

request14005 = HTTPRequest(url=url0, headers=headers43)
request14005 = Test(14005, 'GET close.png').wrap(request14005)

request14006 = HTTPRequest(url=url0, headers=headers43)
request14006 = Test(14006, 'GET error.gif').wrap(request14006)

request14101 = HTTPRequest(url=url0, headers=headers40)
request14101 = Test(14101, 'GET TaskManagementServicesMapping.xml').wrap(request14101)

request14201 = HTTPRequest(url=url0, headers=headers40)
request14201 = Test(14201, 'GET Tidy.xsl').wrap(request14201)

request14301 = HTTPRequest(url=url0, headers=headers44)
request14301 = Test(14301, 'POST validation').wrap(request14301)

request14401 = HTTPRequest(url=url0, headers=headers24)
request14401 = Test(14401, 'POST updates.htm').wrap(request14401)

request14501 = HTTPRequest(url=url0, headers=headers22)
request14501 = Test(14501, 'GET ServerLaunch.html').wrap(request14501)

request14601 = HTTPRequest(url=url0, headers=headers45)
request14601 = Test(14601, 'GET config.xml').wrap(request14601)

request14701 = HTTPRequest(url=url0, headers=headers45)
request14701 = Test(14701, 'GET translations.xml').wrap(request14701)

request14702 = HTTPRequest(url=url0)
request14702 = Test(14702, 'GET style.css').wrap(request14702)

request14801 = HTTPRequest(url=url0, headers=headers45)
request14801 = Test(14801, 'GET appCanvas.xml').wrap(request14801)

request14802 = HTTPRequest(url=url0, headers=headers46)
request14802 = Test(14802, 'GET Packages.js').wrap(request14802)

request14803 = HTTPRequest(url=url0, headers=headers46)
request14803 = Test(14803, 'GET logic.js').wrap(request14803)

request14804 = HTTPRequest(url=url0, headers=headers47)
request14804 = Test(14804, 'GET attachments.gif').wrap(request14804)

request14805 = HTTPRequest(url=url0, headers=headers47)
request14805 = Test(14805, 'GET close.png').wrap(request14805)

request14806 = HTTPRequest(url=url0, headers=headers47)
request14806 = Test(14806, 'GET error.gif').wrap(request14806)

request14901 = HTTPRequest(url=url0, headers=headers45)
request14901 = Test(14901, 'GET TaskManagementServicesMapping.xml').wrap(request14901)

request15001 = HTTPRequest(url=url0, headers=headers45)
request15001 = Test(15001, 'GET Tidy.xsl').wrap(request15001)

request15101 = HTTPRequest(url=url0)
request15101 = Test(15101, 'POST validation').wrap(request15101)

# Date Picker PIPA
request15201 = HTTPRequest(url=url0, headers=headers24)
request15201 = Test(15201, 'POST updates.htm').wrap(request15201)

request15301 = HTTPRequest(url=url0, headers=headers22)
request15301 = Test(15301, 'GET empty.jsp').wrap(request15301)

request15401 = HTTPRequest(url=url0, headers=headers24)
request15401 = Test(15401, 'POST updates.htm').wrap(request15401)

request15501 = HTTPRequest(url=url0, headers=headers22)
request15501 = Test(15501, 'GET ServerLaunch.html').wrap(request15501)

request15601 = HTTPRequest(url=url0, headers=headers48)
request15601 = Test(15601, 'GET config.xml').wrap(request15601)

request15701 = HTTPRequest(url=url0, headers=headers48)
request15701 = Test(15701, 'GET translations.xml').wrap(request15701)

request15702 = HTTPRequest(url=url0)
request15702 = Test(15702, 'GET style.css').wrap(request15702)

request15801 = HTTPRequest(url=url0, headers=headers48)
request15801 = Test(15801, 'GET appCanvas.xml').wrap(request15801)

request15802 = HTTPRequest(url=url0, headers=headers49)
request15802 = Test(15802, 'GET Packages.js').wrap(request15802)

request15803 = HTTPRequest(url=url0, headers=headers49)
request15803 = Test(15803, 'GET logic.js').wrap(request15803)

request15804 = HTTPRequest(url=url0, headers=headers50)
request15804 = Test(15804, 'GET attachments.gif').wrap(request15804)

request15805 = HTTPRequest(url=url0, headers=headers50)
request15805 = Test(15805, 'GET error.gif').wrap(request15805)

request15806 = HTTPRequest(url=url0, headers=headers50)
request15806 = Test(15806, 'GET close.png').wrap(request15806)

request15901 = HTTPRequest(url=url0, headers=headers48)
request15901 = Test(15901, 'GET TaskManagementServicesMapping.xml').wrap(request15901)

request16001 = HTTPRequest(url=url0, headers=headers48)
request16001 = Test(16001, 'GET Tidy.xsl').wrap(request16001)

request16101 = HTTPRequest(url=url0)
request16101 = Test(16101, 'POST validation').wrap(request16101)

request16201 = HTTPRequest(url=url0, headers=headers24)
request16201 = Test(16201, 'POST updates.htm').wrap(request16201)

request16301 = HTTPRequest(url=url0, headers=headers22)
request16301 = Test(16301, 'GET empty.jsp').wrap(request16301)

request16401 = HTTPRequest(url=url0, headers=headers24)
request16401 = Test(16401, 'POST updates.htm').wrap(request16401)

request16501 = HTTPRequest(url=url0, headers=headers22)
request16501 = Test(16501, 'GET ServerLaunch.html').wrap(request16501)

request16601 = HTTPRequest(url=url0, headers=headers51)
request16601 = Test(16601, 'GET config.xml').wrap(request16601)

request16602 = HTTPRequest(url=url0)
request16602 = Test(16602, 'GET style.css').wrap(request16602)

request16701 = HTTPRequest(url=url0, headers=headers51)
request16701 = Test(16701, 'GET appCanvas.xml').wrap(request16701)

request16702 = HTTPRequest(url=url0, headers=headers52)
request16702 = Test(16702, 'GET Packages.js').wrap(request16702)

request16703 = HTTPRequest(url=url0, headers=headers52)
request16703 = Test(16703, 'GET logic.js').wrap(request16703)

request16704 = HTTPRequest(url=url0, headers=headers53)
request16704 = Test(16704, 'GET attachments.gif').wrap(request16704)

request16705 = HTTPRequest(url=url0, headers=headers53)
request16705 = Test(16705, 'GET error.gif').wrap(request16705)

request16706 = HTTPRequest(url=url0, headers=headers53)
request16706 = Test(16706, 'GET close.png').wrap(request16706)

request16801 = HTTPRequest(url=url0, headers=headers51)
request16801 = Test(16801, 'GET TaskManagementServicesMapping.xml').wrap(request16801)

request16901 = HTTPRequest(url=url0, headers=headers51)
request16901 = Test(16901, 'GET Tidy.xsl').wrap(request16901)

request17001 = HTTPRequest(url=url0)
request17001 = Test(17001, 'POST validation').wrap(request17001)

request17101 = HTTPRequest(url=url0, headers=headers24)
request17101 = Test(17101, 'POST updates.htm').wrap(request17101)

request17201 = HTTPRequest(url=url0, headers=headers22)
request17201 = Test(17201, 'GET empty.jsp').wrap(request17201)

request17301 = HTTPRequest(url=url0, headers=headers24)
request17301 = Test(17301, 'POST updates.htm').wrap(request17301)

request17401 = HTTPRequest(url=url0, headers=headers22)
request17401 = Test(17401, 'GET init').wrap(request17401)

# Absence requet PIPA
request17501 = HTTPRequest(url=url0, headers=headers54)
request17501 = Test(17501, 'POST xforms-server').wrap(request17501)

request17601 = HTTPRequest(url=url0, headers=headers54)
request17601 = Test(17601, 'POST xforms-server').wrap(request17601)

request17701 = HTTPRequest(url=url0, headers=headers55)
request17701 = Test(17701, 'POST init').wrap(request17701)

request17801 = HTTPRequest(url=url0, headers=headers55)
request17801 = Test(17801, 'GET tasks.htm').wrap(request17801)

request17901 = HTTPRequest(url=url0, headers=headers22)
request17901 = Test(17901, 'GET empty.jsp').wrap(request17901)

request18001 = HTTPRequest(url=url0, headers=headers23)
request18001 = Test(18001, 'POST vacation.htm').wrap(request18001)

request18101 = HTTPRequest(url=url0, headers=headers24)
request18101 = Test(18101, 'POST updates.htm').wrap(request18101)

request18201 = HTTPRequest(url=url0, headers=headers24)
request18201 = Test(18201, 'POST updates.htm').wrap(request18201)

request18301 = HTTPRequest(url=url0, headers=headers24)
request18301 = Test(18301, 'POST updates.htm').wrap(request18301)

request18401 = HTTPRequest(url=url0, headers=headers22)
request18401 = Test(18401, 'GET empty.jsp').wrap(request18401)

request18501 = HTTPRequest(url=url0, headers=headers24)
request18501 = Test(18501, 'POST updates.htm').wrap(request18501)

request18601 = HTTPRequest(url=url0, headers=headers22)
request18601 = Test(18601, 'GET act').wrap(request18601)

request18602 = HTTPRequest(url=url0, headers=headers56)
request18602 = Test(18602, 'GET attachments.gif').wrap(request18602)

request18603 = HTTPRequest(url=url0, headers=headers56)
request18603 = Test(18603, 'GET remove.gif').wrap(request18603)

# PIPA Reassign - Approval
request18701 = HTTPRequest(url=url0, headers=headers57)
request18701 = Test(18701, 'POST xforms-server').wrap(request18701)

request18801 = HTTPRequest(url=url0, headers=headers57)
request18801 = Test(18801, 'POST xforms-server').wrap(request18801)

request18901 = HTTPRequest(url=url0, headers=headers58)
request18901 = Test(18901, 'POST act').wrap(request18901)

request19001 = HTTPRequest(url=url0, headers=headers58)
request19001 = Test(19001, 'GET tasks.htm').wrap(request19001)

request19101 = HTTPRequest(url=url0, headers=headers22)
request19101 = Test(19101, 'GET empty.jsp').wrap(request19101)

request19201 = HTTPRequest(url=url0, headers=headers23)
request19201 = Test(19201, 'POST vacation.htm').wrap(request19201)

request19301 = HTTPRequest(url=url0, headers=headers24)
request19301 = Test(19301, 'POST updates.htm').wrap(request19301)

request19401 = HTTPRequest(url=url0, headers=headers24)
request19401 = Test(19401, 'POST updates.htm').wrap(request19401)

request19501 = HTTPRequest(url=url0, headers=headers24)
request19501 = Test(19501, 'POST updates.htm').wrap(request19501)

request19601 = HTTPRequest(url=url0, headers=headers22)
request19601 = Test(19601, 'GET empty.jsp').wrap(request19601)

request19701 = HTTPRequest(url=url0, headers=headers24)
request19701 = Test(19701, 'POST updates.htm').wrap(request19701)

# Reassing PA
request19801 = HTTPRequest(url=url0, headers=headers22)
request19801 = Test(19801, 'GET ServerLaunch.html').wrap(request19801)

request19901 = HTTPRequest(url=url0, headers=headers59)
request19901 = Test(19901, 'GET config.xml').wrap(request19901)

request19902 = HTTPRequest(url=url0)
request19902 = Test(19902, 'GET style.css').wrap(request19902)

request20001 = HTTPRequest(url=url0, headers=headers59)
request20001 = Test(20001, 'GET appCanvas.xml').wrap(request20001)

request20101 = HTTPRequest(url=url0, headers=headers59)
request20101 = Test(20101, 'GET translations.xml').wrap(request20101)

request20102 = HTTPRequest(url=url0, headers=headers60)
request20102 = Test(20102, 'GET Packages.js').wrap(request20102)

request20103 = HTTPRequest(url=url0, headers=headers60)
request20103 = Test(20103, 'GET logic.js').wrap(request20103)

request20104 = HTTPRequest(url=url0, headers=headers61)
request20104 = Test(20104, 'GET attachments.gif').wrap(request20104)

request20105 = HTTPRequest(url=url0, headers=headers61)
request20105 = Test(20105, 'GET close.png').wrap(request20105)

request20201 = HTTPRequest(url=url0, headers=headers59)
request20201 = Test(20201, 'GET TaskManagementServicesMapping.xml').wrap(request20201)

request20301 = HTTPRequest(url=url0, headers=headers59)
request20301 = Test(20301, 'GET Tidy.xsl').wrap(request20301)

request20401 = HTTPRequest(url=url0, headers=headers62)
request20401 = Test(20401, 'POST validation').wrap(request20401)

request20501 = HTTPRequest(url=url0, headers=headers59)
request20501 = Test(20501, 'GET FormModelMapping.xml').wrap(request20501)

request20601 = HTTPRequest(url=url0, headers=headers59)
request20601 = Test(20601, 'GET TaskManagerProcessMapping.xml').wrap(request20601)

request20701 = HTTPRequest(url=url0, headers=headers59)
request20701 = Test(20701, 'GET FormModelMapping.xml').wrap(request20701)

request20801 = HTTPRequest(url=url0, headers=headers62)
request20801 = Test(20801, 'POST validation').wrap(request20801)

request20901 = HTTPRequest(url=url0, headers=headers59)
request20901 = Test(20901, 'GET empty.jsp').wrap(request20901)

request21001 = HTTPRequest(url=url0, headers=headers24)
request21001 = Test(21001, 'POST updates.htm').wrap(request21001)

# Reassign PA
# 
request21101 = HTTPRequest(url=url0, headers=headers24)
request21101 = Test(21101, 'POST proxy.jsp').wrap(request21101)

request21201 = HTTPRequest(url=url0, headers=headers24)
request21201 = Test(21201, 'POST proxy.jsp').wrap(request21201)

request21301 = HTTPRequest(url=url0, headers=headers24)
request21301 = Test(21301, 'POST proxy.jsp').wrap(request21301)

request21401 = HTTPRequest(url=url0, headers=headers24)
request21401 = Test(21401, 'POST updates.htm').wrap(request21401)

request21501 = HTTPRequest(url=url0, headers=headers22)
request21501 = Test(21501, 'GET ServerLaunch.html').wrap(request21501)

request21601 = HTTPRequest(url=url0, headers=headers63)
request21601 = Test(21601, 'GET config.xml').wrap(request21601)

request21602 = HTTPRequest(url=url0)
request21602 = Test(21602, 'GET style.css').wrap(request21602)

request21701 = HTTPRequest(url=url0, headers=headers63)
request21701 = Test(21701, 'GET appCanvas.xml').wrap(request21701)

request21801 = HTTPRequest(url=url0, headers=headers63)
request21801 = Test(21801, 'GET translations.xml').wrap(request21801)

request21802 = HTTPRequest(url=url0, headers=headers64)
request21802 = Test(21802, 'GET Packages.js').wrap(request21802)

request21803 = HTTPRequest(url=url0, headers=headers64)
request21803 = Test(21803, 'GET logic.js').wrap(request21803)

request21804 = HTTPRequest(url=url0, headers=headers65)
request21804 = Test(21804, 'GET attachments.gif').wrap(request21804)

request21805 = HTTPRequest(url=url0, headers=headers65)
request21805 = Test(21805, 'GET close.png').wrap(request21805)

request21806 = HTTPRequest(url=url0, headers=headers65)
request21806 = Test(21806, 'GET error.gif').wrap(request21806)

request21901 = HTTPRequest(url=url0, headers=headers63)
request21901 = Test(21901, 'GET TaskManagementServicesMapping.xml').wrap(request21901)

request22001 = HTTPRequest(url=url0, headers=headers63)
request22001 = Test(22001, 'GET Tidy.xsl').wrap(request22001)

request22101 = HTTPRequest(url=url0, headers=headers66)
request22101 = Test(22101, 'POST validation').wrap(request22101)

request22201 = HTTPRequest(url=url0, headers=headers63)
request22201 = Test(22201, 'GET FormModelMapping.xml').wrap(request22201)

request22301 = HTTPRequest(url=url0, headers=headers63)
request22301 = Test(22301, 'GET TaskManagerProcessMapping.xml').wrap(request22301)

request22401 = HTTPRequest(url=url0, headers=headers63)
request22401 = Test(22401, 'GET FormModelMapping.xml').wrap(request22401)

request22501 = HTTPRequest(url=url0, headers=headers66)
request22501 = Test(22501, 'POST validation').wrap(request22501)

request22601 = HTTPRequest(url=url0, headers=headers63)
request22601 = Test(22601, 'GET empty.jsp').wrap(request22601)

request22701 = HTTPRequest(url=url0, headers=headers24)
request22701 = Test(22701, 'POST updates.htm').wrap(request22701)

# Reassihm PA
request22801 = HTTPRequest(url=url0, headers=headers24)
request22801 = Test(22801, 'POST proxy.jsp').wrap(request22801)

request22901 = HTTPRequest(url=url0, headers=headers24)
request22901 = Test(22901, 'POST proxy.jsp').wrap(request22901)

request23001 = HTTPRequest(url=url0, headers=headers24)
request23001 = Test(23001, 'POST proxy.jsp').wrap(request23001)

request23101 = HTTPRequest(url=url0, headers=headers24)
request23101 = Test(23101, 'POST updates.htm').wrap(request23101)

request23201 = HTTPRequest(url=url0, headers=headers22)
request23201 = Test(23201, 'GET ServerLaunch.html').wrap(request23201)

request23301 = HTTPRequest(url=url0, headers=headers67)
request23301 = Test(23301, 'GET config.xml').wrap(request23301)

request23302 = HTTPRequest(url=url0)
request23302 = Test(23302, 'GET style.css').wrap(request23302)

request23401 = HTTPRequest(url=url0, headers=headers67)
request23401 = Test(23401, 'GET appCanvas.xml').wrap(request23401)

request23501 = HTTPRequest(url=url0, headers=headers67)
request23501 = Test(23501, 'GET translations.xml').wrap(request23501)

request23502 = HTTPRequest(url=url0, headers=headers68)
request23502 = Test(23502, 'GET Packages.js').wrap(request23502)

request23503 = HTTPRequest(url=url0, headers=headers68)
request23503 = Test(23503, 'GET logic.js').wrap(request23503)

request23504 = HTTPRequest(url=url0, headers=headers69)
request23504 = Test(23504, 'GET attachments.gif').wrap(request23504)

request23505 = HTTPRequest(url=url0, headers=headers69)
request23505 = Test(23505, 'GET close.png').wrap(request23505)

request23506 = HTTPRequest(url=url0, headers=headers69)
request23506 = Test(23506, 'GET error.gif').wrap(request23506)

request23601 = HTTPRequest(url=url0, headers=headers67)
request23601 = Test(23601, 'GET TaskManagementServicesMapping.xml').wrap(request23601)

request23701 = HTTPRequest(url=url0, headers=headers67)
request23701 = Test(23701, 'GET Tidy.xsl').wrap(request23701)

request23801 = HTTPRequest(url=url0, headers=headers70)
request23801 = Test(23801, 'POST validation').wrap(request23801)

request23901 = HTTPRequest(url=url0, headers=headers67)
request23901 = Test(23901, 'GET FormModelMapping.xml').wrap(request23901)

request24001 = HTTPRequest(url=url0, headers=headers67)
request24001 = Test(24001, 'GET TaskManagerProcessMapping.xml').wrap(request24001)

request24101 = HTTPRequest(url=url0, headers=headers67)
request24101 = Test(24101, 'GET FormModelMapping.xml').wrap(request24101)

request24201 = HTTPRequest(url=url0, headers=headers70)
request24201 = Test(24201, 'POST validation').wrap(request24201)

request24301 = HTTPRequest(url=url0, headers=headers67)
request24301 = Test(24301, 'GET empty.jsp').wrap(request24301)

request24401 = HTTPRequest(url=url0, headers=headers24)
request24401 = Test(24401, 'POST updates.htm').wrap(request24401)

# complete absence request
request24501 = HTTPRequest(url=url0, headers=headers22)
request24501 = Test(24501, 'GET act').wrap(request24501)

request24601 = HTTPRequest(url=url0, headers=headers71)
request24601 = Test(24601, 'POST xforms-server').wrap(request24601)

request24701 = HTTPRequest(url=url0, headers=headers71)
request24701 = Test(24701, 'POST xforms-server').wrap(request24701)

request24801 = HTTPRequest(url=url0, headers=headers72)
request24801 = Test(24801, 'POST act').wrap(request24801)

request24901 = HTTPRequest(url=url0, headers=headers72)
request24901 = Test(24901, 'GET tasks.htm').wrap(request24901)

request25001 = HTTPRequest(url=url0, headers=headers22)
request25001 = Test(25001, 'GET empty.jsp').wrap(request25001)

request25101 = HTTPRequest(url=url0, headers=headers23)
request25101 = Test(25101, 'POST vacation.htm').wrap(request25101)

request25201 = HTTPRequest(url=url0, headers=headers24)
request25201 = Test(25201, 'POST updates.htm').wrap(request25201)

request25301 = HTTPRequest(url=url0, headers=headers24)
request25301 = Test(25301, 'POST updates.htm').wrap(request25301)

request25401 = HTTPRequest(url=url0, headers=headers24)
request25401 = Test(25401, 'POST updates.htm').wrap(request25401)

request25501 = HTTPRequest(url=url0, headers=headers22)
request25501 = Test(25501, 'GET empty.jsp').wrap(request25501)

request25601 = HTTPRequest(url=url0, headers=headers24)
request25601 = Test(25601, 'POST updates.htm').wrap(request25601)

request25701 = HTTPRequest(url=url0, headers=headers22)
request25701 = Test(25701, 'POST login.htm').wrap(request25701)

request25702 = HTTPRequest(url=url0, headers=headers22)
request25702 = Test(25702, 'GET login.htm').wrap(request25702)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET / (requests 101-139)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request101.GET('/')

    grinder.sleep(11)
    
    # Expecting 302 'Moved Temporarily'
    request102.GET('/login.htm')

    request103.GET('/index.htm')
    self.token_accessible = \
      httpUtilities.valueFromHiddenInput('accessible') # ''

    grinder.sleep(22)
    request104.GET('/scripts/plugin/jquery-1.8.2.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"265218-1354977540000\"'), ))

    request105.GET('/scripts/plugin/jquery.ui.core.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"8857-1354977540000\"'), ))

    request106.GET('/scripts/plugin/jquery.qtip.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"99957-1354977540000\"'), ))

    request107.GET('/scripts/plugin/jquery-ui.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"445304-1354977540000\"'), ))

    request108.GET('/scripts/plugin/jquery.dashboard.min.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"35932-1354977540000\"'), ))

    request109.GET('/scripts/plugin/d3.v2.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"239578-1354977540000\"'), ))

    request110.GET('/scripts/plugin/jquery.ui.button.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"11679-1354977540000\"'), ))

    request111.GET('/scripts/plugin/jquery.ui.widget.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"14946-1354977540000\"'), ))

    request112.GET('/scripts/plugin/nv.d3.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"303859-1354977540000\"'), ))

    request113.GET('/scripts/plugin/utils.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"2685-1354977540000\"'), ))

    request114.GET('/scripts/plugin/discreteBar.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"9938-1354977540000\"'), ))

    request115.GET('/scripts/plugin/multiBar.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"12092-1354977540000\"'), ))

    request116.GET('/scripts/plugin/discreteBarChart.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"8537-1354977540000\"'), ))

    request117.GET('/scripts/plugin/tooltip.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"3088-1354977540000\"'), ))

    request118.GET('/scripts/plugin/legend.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"6510-1354977540000\"'), ))

    request119.GET('/scripts/plugin/multiBarChart.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"11741-1354977540000\"'), ))

    request120.GET('/scripts/plugin/scatter.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"16333-1354977540000\"'), ))

    request121.GET('/scripts/plugin/axis.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"13390-1354977540000\"'), ))

    request122.GET('/scripts/plugin/line.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"9575-1354977540000\"'), ))

    request123.GET('/scripts/plugin/themeroller.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"50093-1354977540000\"'), ))

    request124.GET('/scripts/plugin/multiBarHorizontal.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"12621-1354977540000\"'), ))

    request125.GET('/scripts/plugin/pieChart.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"7476-1354977540000\"'), ))

    request126.GET('/scripts/plugin/pie.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"9586-1354977540000\"'), ))

    request127.GET('/style/plugin/jquery-ui-1.9.0.css', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"32862-1354977540000\"'), ))

    request128.GET('/scripts/custom/dashboard.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"21263-1354977540000\"'), ))

    request129.GET('/scripts/plugin/historicalBar.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"8371-1354977540000\"'), ))

    request130.GET('/scripts/plugin/linePlusBarChart.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"13068-1354977540000\"'), ))

    request131.GET('/scripts/plugin/jquery.dataTables.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"371754-1354977540000\"'), ))

    request132.GET('/scripts/plugin/multiBarHorizontalChart.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"10821-1354977540000\"'), ))

    request133.GET('/style/plugin/jquery.dataTables.css', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"5845-1354977540000\"'), ))

    request134.GET('/scripts/plugin/jquery-dateFormat.js', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"13538-1354977540000\"'), ))

    request135.GET('/style/plugin/jquery.ui.theme.css', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"17805-1354977540000\"'), ))

    request136.GET('/style/plugin/jquery.qtip.css', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"13607-1354977540000\"'), ))

    request137.GET('/style/plugin/nv.d3.css', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"10353-1354977540000\"'), ))

    request138.GET('/style/custom/dashboardui.css', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"5260-1354977540000\"'), ))

    request139.GET('/images/logo.png', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://titan:8080/index.htm'),
        NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"12666-1354977540000\"'),
        NVPair('Cache-Control', 'max-age=0'), ))

    return result

  def page2(self):
    """GET data.json (requests 201-205)."""
    self.token_filter = \
      '1d'
    self.token__ = \
      '1355140382841'
    result = request201.GET('/data.json' +
      '?filter=' +
      self.token_filter +
      '&_=' +
      self.token__)

    request202.GET('/images/loading.gif', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://titan:8080/style/custom/dashboardui.css'),
        NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"1849-1354977540000\"'),
        NVPair('Cache-Control', 'max-age=0'), ))

    request203.GET('/images/ui-bg_highlight-soft_100_f6f6f6_1x100.png', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"90-1354977540000\"'), ))

    request204.GET('/images/ui-icons_666666_256x240.png', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"4369-1354977540000\"'), ))

    grinder.sleep(38)
    request205.GET('/images/ui-bg_flat_75_ffffff_40x100.png', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"178-1354977540000\"'), ))

    return result

  def page3(self):
    """GET templates.html (requests 301-302)."""
    result = request301.GET('/templates.html', None,
      ( NVPair('Accept', 'text/html, */*; q=0.01'),
        NVPair('Referer', 'http://titan:8080/index.htm'),
        NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"2709-1354977540000\"'),
        NVPair('Cache-Control', 'max-age=0'), ))

    request302.GET('/images/ui-bg_highlight-soft_50_dddddd_1x100.png', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"92-1354977540000\"'), ))

    return result

  def page4(self):
    """GET dsState.json (requests 401-402)."""
    self.token_action = \
      'getState'
    self.token_ignore_cache = \
      '1355140383575'
    result = request401.GET('/dsState.json' +
      '?action=' +
      self.token_action +
      '&ignore_cache=' +
      self.token_ignore_cache)

    request402.GET('/images/ui-icons_0073ea_256x240.png', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"4369-1354977540000\"'), ))

    return result

  def page5(self):
    """GET task_summary.jsp (request 501)."""
    result = request501.GET('/widgets/task_summary.jsp')

    return result

  def page6(self):
    """GET user_task_count.jsp (request 601)."""
    result = request601.GET('/widgets/user_task_count.jsp')

    return result

  def page7(self):
    """GET notifications.jsp (request 701)."""
    result = request701.GET('/widgets/notifications.jsp')

    return result

  def page8(self):
    """GET instance_status_cnt.jsp (request 801)."""
    result = request801.GET('/widgets/instance_status_cnt.jsp')

    return result

  def page9(self):
    """GET ws_response_time.jsp (request 901)."""
    result = request901.GET('/widgets/ws_response_time.jsp')

    return result

  def page10(self):
    """GET avg_completion_time.jsp (request 1001)."""
    result = request1001.GET('/widgets/avg_completion_time.jsp')

    return result

  def page11(self):
    """GET vacation_summary.jsp (requests 1101-1103)."""
    result = request1101.GET('/widgets/vacation_summary.jsp')

    request1102.GET('/images/ui-bg_glass_65_ffffff_1x400.png', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"105-1354977540000\"'), ))

    request1103.GET('/images/ui-icons_454545_256x240.png', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"4369-1354977540000\"'), ))

    return result

  def page12(self):
    """GET notifications.jsp (request 1201)."""
    result = request1201.GET('/widgets/notifications.jsp')

    return result

  def page13(self):
    """GET vacation_summary.jsp (request 1301)."""
    result = request1301.GET('/widgets/vacation_summary.jsp')

    return result

  def page14(self):
    """GET task_summary.jsp (requests 1401-1402)."""
    result = request1401.GET('/widgets/task_summary.jsp')

    request1402.GET('/images/sort_both.png', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://titan:8080/style/plugin/jquery.dataTables.css'),
        NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"1185-1354977540000\"'),
        NVPair('Cache-Control', 'max-age=0'), ))

    return result

  def page15(self):
    """GET user_task_count.jsp (request 1501)."""
    result = request1501.GET('/widgets/user_task_count.jsp')

    return result

  def page16(self):
    """GET avg_completion_time.jsp (request 1601)."""
    result = request1601.GET('/widgets/avg_completion_time.jsp')

    return result

  def page17(self):
    """GET instance_status_cnt.jsp (request 1701)."""
    result = request1701.GET('/widgets/instance_status_cnt.jsp')

    return result

  def page18(self):
    """GET ws_response_time.jsp (requests 1801-1803)."""
    result = request1801.GET('/widgets/ws_response_time.jsp')

    grinder.sleep(356)
    request1802.GET('/images/ui-bg_highlight-soft_25_0073ea_1x100.png', None,
      ( NVPair('If-Modified-Since', 'Sat, 08 Dec 2012 14:39:00 GMT'),
        NVPair('If-None-Match', 'W/\"118-1354977540000\"'), ))

    request1803.GET('/images/ui-icons_ffffff_256x240.png', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://titan:8080/style/plugin/jquery.ui.theme.css'), ))

    return result

  def page19(self):
    """POST login.htm (request 1901)."""
    result = request1901.POST('/login.htm',
      ( NVPair('actionName', 'logOut'), ),
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://titan:8080/index.htm'),
        NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))
    self.token_actionName = \
      httpUtilities.valueFromHiddenInput('actionName') # 'logIn'

    return result

  def page20(self):
    """POST login.htm (requests 2001-2002)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request2001.POST('/login.htm',
      ( NVPair('actionName', self.token_actionName),
        NVPair('username', 'admin'),
        NVPair('password', 'changeit'),
        NVPair('submit', 'Login'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))
    self.token_jsessionid = \
      httpUtilities.valueFromLocationURI('jsessionid') # '0D7D89DBE69BEC9D45709F9FA00D92A9'

    grinder.sleep(11)
    request2002.GET('/index.htm;jsessionid=' +
      self.token_jsessionid)

    return result

  def page21(self):
    """GET data.json (request 2101)."""
    self.token__ = \
      '1355140387360'
    result = request2101.GET('/data.json' +
      '?filter=' +
      self.token_filter +
      '&_=' +
      self.token__)

    return result

  def page22(self):
    """GET dsState.json (request 2201)."""
    self.token_ignore_cache = \
      '1355140387489'
    result = request2201.GET('/dsState.json' +
      '?action=' +
      self.token_action +
      '&ignore_cache=' +
      self.token_ignore_cache)

    return result

  def page23(self):
    """GET vacation_summary.jsp (request 2301)."""
    result = request2301.GET('/widgets/vacation_summary.jsp')

    return result

  def page24(self):
    """GET instance_status_cnt.jsp (request 2401)."""
    result = request2401.GET('/widgets/instance_status_cnt.jsp')

    return result

  def page25(self):
    """GET notifications.jsp (request 2501)."""
    result = request2501.GET('/widgets/notifications.jsp')

    return result

  def page26(self):
    """GET user_task_count.jsp (request 2601)."""
    result = request2601.GET('/widgets/user_task_count.jsp')

    return result

  def page27(self):
    """GET task_summary.jsp (request 2701)."""
    result = request2701.GET('/widgets/task_summary.jsp')

    return result

  def page28(self):
    """GET avg_completion_time.jsp (request 2801)."""
    result = request2801.GET('/widgets/avg_completion_time.jsp')

    return result

  def page29(self):
    """GET ws_response_time.jsp (request 2901)."""
    result = request2901.GET('/widgets/ws_response_time.jsp')

    return result

  def page30(self):
    """GET user_task_count.jsp (request 3001)."""
    result = request3001.GET('/widgets/user_task_count.jsp')

    return result

  def page31(self):
    """GET notifications.jsp (request 3101)."""
    result = request3101.GET('/widgets/notifications.jsp')

    return result

  def page32(self):
    """GET vacation_summary.jsp (request 3201)."""
    result = request3201.GET('/widgets/vacation_summary.jsp')

    return result

  def page33(self):
    """GET task_summary.jsp (request 3301)."""
    result = request3301.GET('/widgets/task_summary.jsp')

    return result

  def page34(self):
    """GET avg_completion_time.jsp (request 3401)."""
    result = request3401.GET('/widgets/avg_completion_time.jsp')

    return result

  def page35(self):
    """GET instance_status_cnt.jsp (request 3501)."""
    result = request3501.GET('/widgets/instance_status_cnt.jsp')

    return result

  def page36(self):
    """GET ws_response_time.jsp (request 3601)."""
    result = request3601.GET('/widgets/ws_response_time.jsp')

    return result

  def page37(self):
    """GET tasks.htm (requests 3701-3703)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request3701.GET('/ui-fw/tasks.htm')

    
    # Expecting 302 'Moved Temporarily'
    request3702.GET('/ui-fw/login.htm')

    request3703.GET('/ui-fw/tasks.htm' +
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

  def page38(self):
    """GET empty.jsp (request 3801)."""
    result = request3801.GET('/ui-fw/script/empty.jsp')

    return result

  def page39(self):
    """POST vacation.htm (request 3901)."""
    result = request3901.POST('/ui-fw/vacation.htm',
      ( NVPair('action', 'Validate'), ),
      ( NVPair('Accept', 'application/json, text/javascript, */*; q=0.01'),
        NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
        NVPair('Referer', 'http://titan:8080/ui-fw/tasks.htm?null'),
        NVPair('Cache-Control', 'no-cache'), ))

    return result

  def page40(self):
    """POST updates.htm (request 4001)."""
    result = request4001.POST('/ui-fw/updates.htm',
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

  def page41(self):
    """POST updates.htm (request 4101)."""
    result = request4101.POST('/ui-fw/updates.htm',
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
      httpUtilities.valueFromBodyURI('id') # 'notify-1TMR-53ZQ-7GE9-0JN0'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'Notification'
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/RepeatEvery_PXEI_897/Forms/n...'
    # 2 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.
    # 1 different values for token_user found in response; the first matched
    # the last known value of token_user - don't update the variable.

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
        NVPair('type', 'PIPATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 23 different values for token_id found in response; the first matched
    # the last known value of token_id - don't update the variable.
    # 35 different values for token_type found in response; the first matched
    # the last known value of token_type - don't update the variable.
    # 35 different values for token_url found in response; the first matched
    # the last known value of token_url - don't update the variable.
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page43(self):
    """GET empty.jsp (request 4301)."""
    result = request4301.GET('/ui-fw/script/empty.jsp')

    return result

  def page44(self):
    """POST updates.htm (request 4401)."""
    result = request4401.POST('/ui-fw/updates.htm',
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

  def page45(self):
    """POST updates.htm (request 4501)."""
    result = request4501.POST('/ui-fw/updates.htm',
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

  def page46(self):
    """GET ServerLaunch.html (request 4601)."""
    result = request4601.GET('/gi/apppath/AjaxTesting/form.gi/IntalioInternal/ServerLaunch.html' +
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

  def page47(self):
    """GET config.xml (requests 4701-4702)."""
    result = request4701.GET('/gi/apppath/AjaxTesting/form.gi/config.xml')

    grinder.sleep(115)
    request4702.GET('/gi/apppath/AjaxTesting/form.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxTesting/form.gi/IntalioInternal/ServerLaunch.html?id=f1e71b24-a117-4cef-bcc8-aa2899e6e240&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxTesting%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page48(self):
    """GET appCanvas.xml (request 4801)."""
    result = request4801.GET('/gi/apppath/AjaxTesting/form.gi/components/appCanvas.xml')

    return result

  def page49(self):
    """GET translations.xml (requests 4901-4906)."""
    result = request4901.GET('/gi/apppath/AjaxTesting/form.gi/jss/translations.xml')

    grinder.sleep(44)
    request4902.GET('/gi/apppath/AjaxTesting/form.gi/IntalioInternal/Packages.js')
    self.token_imgsrc = \
      httpUtilities.valueFromBodyURI('<img src') # ''
    self.token_ahref = \
      httpUtilities.valueFromBodyURI('<a href') # ''

    grinder.sleep(69)
    request4903.GET('/gi/apppath/AjaxTesting/form.gi/js/logic.js')

    grinder.sleep(134)
    request4904.GET('/gi/apppath/AjaxTesting/form.gi/images/attachments.gif')

    request4905.GET('/gi/apppath/AjaxTesting/form.gi/images/close.png')

    request4906.GET('/gi/apppath/AjaxTesting/form.gi/images/error.gif')

    return result

  def page50(self):
    """GET TaskManagementServicesMapping.xml (request 5001)."""
    result = request5001.GET('/gi/apppath/AjaxTesting/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page51(self):
    """GET Tidy.xsl (request 5101)."""
    result = request5101.GET('/gi/apppath/AjaxTesting/form.gi/IntalioInternal/Tidy.xsl')

    return result

  def page52(self):
    """POST validation (request 5201)."""
    paTaskId=""
    size=0
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pa pa on task.id=pa.id where pa.state = \'0\' and form_url like \'%AjaxTesting%\' order by creation_date desc'
    i=1
    while (size==0):
            if(i>10):
                break
            dbConn = getConnection()
            stmt = dbConn.createStatement()
            rs = stmt.executeQuery(query)
            size =0
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("i ==>" + str(i))
            grinder.logger.info("size ==>" + str(size))
            grinder.sleep(1000*i)
            i=i+1 
            if (size>0):         
                paTaskId = rs.getString(1)
                grinder.logger.info("get PA Task Operation")
                grinder.logger.info("PA Task Id ==>" + paTaskId)

            ensureClosed(stmt)
            ensureClosed(dbConn)
    result = request5201.POST('/gi/validation',
      ( NVPair('assembly', 'AjaxTesting'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+paTaskId+'''</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page53(self):
    """GET TaskManagementServicesMapping.xml (request 5301)."""
    result = request5301.GET('/gi/apppath/AjaxTesting/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page54(self):
    """GET FormModelMapping.xml (request 5401)."""
    result = request5401.GET('/gi/apppath/AjaxTesting/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page55(self):
    """POST validation (request 5501)."""
    pipaTaskId = None
    grinder.logger.info("page 5501 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pipa pipa on task.id=pipa.id where task.form_url = \'/gi/apppath/AjaxTesting/form.gi/IntalioInternal/ServerLaunch.html\''
    dbConn = getConnection()
    stmt = dbConn.createStatement()
    try:
        rs = stmt.executeQuery(query)
        size =0
        if (rs != None):
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("size ==>" + str(size))                        
            rs.absolute(size)            
            pipaTaskId = rs.getString(1)
            grinder.logger.info("get PIPA Task Operation") 
            grinder.logger.info("PIPA Task Id ==>" + pipaTaskId)            
    finally:
        ensureClosed(stmt)
        ensureClosed(dbConn)
    result = request5501.POST('/gi/validation',
      ( NVPair('assembly', 'AjaxTesting'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:initRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+pipaTaskId+'''</jsx1:taskId><jsx1:input><a0:FormModel xmlns:a0=\"http://www.intalio.com/gi/form.gi\"><name>Veresh</name></a0:FormModel></jsx1:input><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken><jsx1:formUrl>/gi/apppath/AjaxTesting/form.gi/IntalioInternal/ServerLaunch.html</jsx1:formUrl></jsx1:initRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page56(self):
    """GET empty.jsp (request 5601)."""
    result = request5601.GET('/ui-fw/script/empty.jsp')

    return result

  def page57(self):
    """POST updates.htm (request 5701)."""
    result = request5701.POST('/ui-fw/updates.htm',
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

  def page58(self):
    """GET ServerLaunch.html (request 5801)."""
    self.token_id = \
      '3d124bc6-c2f2-4c7b-b7df-1c2dfe28aa0c'
    self.token_url = \
      'http://titan:8080/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/ServerLaunch.html'
    result = request5801.GET('/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/ServerLaunch.html' +
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

  def page59(self):
    """GET config.xml (requests 5901-5902)."""
    result = request5901.GET('/gi/apppath/ScheduleActionPA/form.gi/config.xml')

    grinder.sleep(76)
    request5902.GET('/gi/apppath/ScheduleActionPA/form.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/ServerLaunch.html?id=3d124bc6-c2f2-4c7b-b7df-1c2dfe28aa0c&type=PIPATask&url=http%3A%2F%2Ftitan%3A8080%2Fgi%2Fapppath%2FScheduleActionPA%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page60(self):
    """GET translations.xml (request 6001)."""
    result = request6001.GET('/gi/apppath/ScheduleActionPA/form.gi/jss/translations.xml')

    return result

  def page61(self):
    """GET appCanvas.xml (requests 6101-6106)."""
    result = request6101.GET('/gi/apppath/ScheduleActionPA/form.gi/components/appCanvas.xml')

    grinder.sleep(117)
    request6102.GET('/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/Packages.js')

    grinder.sleep(63)
    request6103.GET('/gi/apppath/ScheduleActionPA/form.gi/js/logic.js')

    grinder.sleep(137)
    request6104.GET('/gi/apppath/ScheduleActionPA/form.gi/images/attachments.gif')

    request6105.GET('/gi/apppath/ScheduleActionPA/form.gi/images/close.png')

    request6106.GET('/gi/apppath/ScheduleActionPA/form.gi/images/error.gif')

    return result

  def page62(self):
    """GET TaskManagementServicesMapping.xml (request 6201)."""
    result = request6201.GET('/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page63(self):
    """GET Tidy.xsl (request 6301)."""
    result = request6301.GET('/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/Tidy.xsl')

    return result

  def page64(self):
    """POST validation (request 6401)."""
    paTaskId=""
    size=0
    grinder.logger.info("page 6401 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pa pa on task.id=pa.id where pa.state = \'0\' and form_url like \'%ScheduleActionPA%\' order by creation_date desc'
    i=1
    while (size==0):
            if(i>10):
                break
            dbConn = getConnection()
            stmt = dbConn.createStatement()
            rs = stmt.executeQuery(query)
            size =0
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("i ==>" + str(i))
            grinder.logger.info("size ==>" + str(size))
            grinder.sleep(1000*i)
            i=i+1 
            if (size>0):         
                paTaskId = rs.getString(1)
                grinder.logger.info("get PA Task Operation")
                grinder.logger.info("PA Task Id ==>" + paTaskId)

            ensureClosed(stmt)
            ensureClosed(dbConn)
    result = request6401.POST('/gi/validation',
      ( NVPair('assembly', 'ScheduleActionPA'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+paTaskId+'''</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page65(self):
    """GET TaskManagementServicesMapping.xml (request 6501)."""
    result = request6501.GET('/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page66(self):
    """GET FormModelMapping.xml (request 6601)."""
    result = request6601.GET('/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page67(self):
    """POST validation (request 6701)."""
    pipaTaskId = None
    grinder.logger.info("page 6701 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pipa pipa on task.id=pipa.id where task.form_url = \'/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/ServerLaunch.html\''
    dbConn = getConnection()
    stmt = dbConn.createStatement()
    try:
        rs = stmt.executeQuery(query)
        size =1
        if (rs != None):
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("size ==>" + str(size))                        
            rs.absolute(size)            
            pipaTaskId = rs.getString(1)
            grinder.logger.info("init PIPA Task Operation") 
            grinder.logger.info("PIPA Task Id ==>" + pipaTaskId)            
    finally:
        ensureClosed(stmt)
        ensureClosed(dbConn)
    result = request6701.POST('/gi/validation',
      ( NVPair('assembly', 'ScheduleActionPA'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:initRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+pipaTaskId+'''</jsx1:taskId><jsx1:input><a0:FormModel xmlns:a0=\"http://www.intalio.com/gi/form.gi\"/></jsx1:input><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken><jsx1:formUrl>http://titan:8080/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/ServerLaunch.html</jsx1:formUrl></jsx1:initRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page68(self):
    """GET empty.jsp (request 6801)."""
    result = request6801.GET('/ui-fw/script/empty.jsp')

    return result

  def page69(self):
    """POST updates.htm (request 6901)."""
    result = request6901.POST('/ui-fw/updates.htm',
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

  def page70(self):
    """GET init (request 7001)."""
    self.token_id = \
      '6c8f64ba-1c38-4dec-82e4-33a632752d4c'
    self.token_url = \
      'oxf://WorkflowTabPane/details.xform'
    result = request7001.GET('/xFormsManager/init' +
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
    self.token_staticstate = \
      httpUtilities.valueFromHiddenInput('$static-state') # 'pers:9EF9E3C4-DDCD-EDA1-CF86-3CE76709A00...'
    self.token_dynamicstate = \
      httpUtilities.valueFromHiddenInput('$dynamic-state') # 'pers:801654EE-0EDA-1F75-14B5-B796257A9C9...'
    self.token_serverevents = \
      httpUtilities.valueFromHiddenInput('$server-events') # ''
    self.token_clientstate = \
      httpUtilities.valueFromHiddenInput('$client-state') # ''
    self.token_repeattree = \
      httpUtilities.valueFromHiddenInput('$repeat-tree') # ''
    self.token_repeatindexes = \
      httpUtilities.valueFromHiddenInput('$repeat-indexes') # ''

    return result

  def page71(self):
    """POST xforms-server (request 7101)."""
    result = request7101.POST('/xFormsManager/xforms-server',
      '''<!DOCTYPE xxforms:event-request [<!ENTITY nbsp \"&#160;\">]>\n<xxforms:event-request xmlns:xxforms=\"http://orbeon.org/oxf/xml/xforms\">\n    <xxforms:static-state>pers:9EF9E3C4-DDCD-EDA1-CF86-3CE76709A00E</xxforms:static-state>\n    <xxforms:dynamic-state>pers:801654EE-0EDA-1F75-14B5-B796257A9C99</xxforms:dynamic-state>\n    <xxforms:action>\n        <xxforms:event name=\"DOMFocusIn\" source-control-id=\"xf-16$xf-43\"></xxforms:event>\n        <xxforms:event name=\"xxforms-value-change-with-focus-change\" source-control-id=\"xf-16$xf-43\">YpE0z0eSBZU=</xxforms:event>\n    </xxforms:action>\n</xxforms:event-request>''',
      ( NVPair('Content-Type', 'application/xml; charset=UTF-8'), ))

    return result

  def page72(self):
    """POST xforms-server (request 7201)."""
    result = request7201.POST('/xFormsManager/xforms-server',
      '''<!DOCTYPE xxforms:event-request [<!ENTITY nbsp \"&#160;\">]>\n<xxforms:event-request xmlns:xxforms=\"http://orbeon.org/oxf/xml/xforms\">\n    <xxforms:static-state>pers:9EF9E3C4-DDCD-EDA1-CF86-3CE76709A00E</xxforms:static-state>\n    <xxforms:dynamic-state>pers:1AF62B80-7509-94A7-2223-D8844E13C415</xxforms:dynamic-state>\n    <xxforms:action>\n        <xxforms:event name=\"DOMFocusOut\" source-control-id=\"xf-16$xf-43\"></xxforms:event>\n        <xxforms:event name=\"DOMFocusIn\" source-control-id=\"xf-19\"></xxforms:event>\n        <xxforms:event name=\"DOMActivate\" source-control-id=\"xf-19\"></xxforms:event>\n    </xxforms:action>\n</xxforms:event-request>''',
      ( NVPair('Content-Type', 'application/xml; charset=UTF-8'), ))

    return result

  def page73(self):
    """POST init (request 7301)."""
    self.token_dynamicstate = \
      'pers:21649661-96ED-14DE-8227-ABD26B6EC7E9'
    self.token_serverevents = \
      'X2ztnLbujs+XocNBu3ADXGPfD6vdqqkYcLQqj/XYbeEKOot+i+ET3USU8tRk6y72bAz1vzPGvWtjw/4gTjAZuZEjl9QTQKtW4BMz4TkOT8XJBWtIANXLDFppGFa/o8ub50d7qy3UYWy8WH901rqOFPXtWhZryEAFnRsoo0zyvf2n+RtQnqsRyjAmg2ckRypA+ntW/pgpTvIjfXbvpwaKVf7eyjqBaxhtIngTU0Aw5L4oEHH2g9m1qiYCuA4hcT6ikYh7BKlkXxAuc='
    self.token_clientstate = \
      'initial-dynamic-state&pers%3A801654EE-0EDA-1F75-14B5-B796257A9C99&load-did-run&true'
    result = request7301.POST('/xFormsManager/init' +
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
      self.token_claimTaskOnOpen,
      ( NVPair('$static-state', self.token_staticstate),
        NVPair('$dynamic-state', self.token_dynamicstate),
        NVPair('$server-events', self.token_serverevents),
        NVPair('$client-state', self.token_clientstate),
        NVPair('$repeat-tree', self.token_repeattree),
        NVPair('$repeat-indexes', self.token_repeatindexes),
        NVPair('xf-16$xf-43', 'YpE0z0eSBZU='),
        NVPair('xf-16$xf-54$xforms-input-1', ''),
        NVPair('xf-16$xf-80$xforms-input-1', ''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    return result

  def page74(self):
    """GET tasks.htm (request 7401)."""
    result = request7401.GET('/ui-fw/tasks.htm')

    return result

  def page75(self):
    """GET empty.jsp (request 7501)."""
    result = request7501.GET('/ui-fw/script/empty.jsp')

    return result

  def page76(self):
    """POST vacation.htm (request 7601)."""
    result = request7601.POST('/ui-fw/vacation.htm',
      ( NVPair('action', 'Validate'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page77(self):
    """POST updates.htm (request 7701)."""
    result = request7701.POST('/ui-fw/updates.htm',
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
    # 28 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # 'http://titan:8080/gi/apppath/ScheduleAct...'
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page78(self):
    """POST updates.htm (request 7801)."""
    result = request7801.POST('/ui-fw/updates.htm',
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
      httpUtilities.valueFromBodyURI('id') # 'notify-TK24-1CQ4-TIQD-WXY9'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'Notification'
    # 29 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # 'oxf://WorkflowTabPane/notify.xform'
    # 2 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page79(self):
    """POST updates.htm (request 7901)."""
    result = request7901.POST('/ui-fw/updates.htm',
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
    # 18 different values for token_type found in response; the first matched
    # the last known value of token_type - don't update the variable.
    # 34 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/AjaxTesting/form.gi/IntalioI...'
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page80(self):
    """GET empty.jsp (request 8001)."""
    result = request8001.GET('/ui-fw/script/empty.jsp')

    return result

  def page81(self):
    """POST updates.htm (request 8101)."""
    result = request8101.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 30 different values for token_id found in response; the first matched
    # the last known value of token_id - don't update the variable.
    # 27 different values for token_url found in response; the first matched
    # the last known value of token_url - don't update the variable.
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page82(self):
    """POST updates.htm (request 8201)."""
    result = request8201.POST('/ui-fw/updates.htm',
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

  def page83(self):
    """GET ServerLaunch.html (request 8301)."""
    self.token_id = \
      '9652e37c-8ffb-494f-b736-81fd046c35cb'
    self.token_url = \
      '/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/IntalioInternal/ServerLaunch.html'
    result = request8301.GET('/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/IntalioInternal/ServerLaunch.html' +
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

  def page84(self):
    """GET config.xml (requests 8401-8402)."""
    result = request8401.GET('/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/config.xml')

    grinder.sleep(75)
    request8402.GET('/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/IntalioInternal/ServerLaunch.html?id=9652e37c-8ffb-494f-b736-81fd046c35cb&type=PIPATask&url=%2Fgi%2Fapppath%2FTestWidgetForMobile%2FIntalioWidgets.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page85(self):
    """GET translations.xml (request 8501)."""
    result = request8501.GET('/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/jss/translations.xml')

    return result

  def page86(self):
    """GET appCanvas.xml (requests 8601-8626)."""
    result = request8601.GET('/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/components/appCanvas.xml')

    grinder.sleep(79)
    request8602.GET('/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/IntalioInternal/Packages.js')

    grinder.sleep(41)
    request8603.GET('/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/js/logic.js')

    grinder.sleep(51)
    request8604.GET('/gi/files/JSX/addins/intalioajax-addins/js/com/intalio/ria/FileUpload.js')
    self.token_participantToken = \
      httpUtilities.valueFromHiddenInput('participantToken') # ''

    request8605.GET('/gi/files/JSX/js/jsx3/gui/ImageButton.js')

    request8606.GET('/gi/files/JSX/js/jsx3/gui/ColorPicker.js')

    request8607.GET('/gi/files/JSX/addins/intalioajax-addins/js/com/intalio/ria/Title.js')

    request8608.GET('/gi/files/JSX/js/jsx3/gui/TimePicker.js')

    request8609.GET('/gi/files/JSX/js/jsx3/gui/Slider.js')

    request8610.GET('/gi/files/JSX/images/colorpicker/saturation-v.png')

    grinder.sleep(82)
    request8611.GET('/gi/files/JSX/images/colorpicker/d1arrow.gif')

    request8612.GET('/gi/files/JSX/images/colorpicker/hue-h.png')

    request8613.GET('/gi/files/JSX/images/colorpicker/brightness-v.png')

    request8614.GET('/gi/files/JSX/images/colorpicker/hue-v.png')

    request8615.GET('/gi/files/JSX/images/colorpicker/saturation-h.png')

    request8616.GET('/gi/files/JSX/js/jsx3/gui/IFrame.js')

    grinder.sleep(294)
    request8617.GET('/gi/files/JSX/images/jsxtimepicker/spin_up.gif')

    request8618.GET('/gi/files/JSX/images/jsxtimepicker/spin_down.gif')

    request8619.GET('/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/images/close.png')

    request8620.GET('/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/images/attachments.gif')

    request8621.GET('/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/images/error.gif')

    request8622.GET('/gi/files/JSX/images/tree/folder.gif')

    request8623.GET('/gi/files/JSX/images/icons/v.png')

    request8624.GET('/gi/files/JSX/images/matrix/sort_desc.gif')

    request8625.GET('/gi/files/JSX/images/slider/top.gif')

    request8626.GET('/gi/files/JSX/images/matrix/minus.gif')

    return result

  def page87(self):
    """GET TaskManagementServicesMapping.xml (requests 8701-8702)."""
    result = request8701.GET('/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    request8702.GET('/gi/files/JSX/images/matrix/plus.gif')

    return result

  def page88(self):
    """GET Tidy.xsl (request 8801)."""
    result = request8801.GET('/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/IntalioInternal/Tidy.xsl')

    return result

  def page89(self):
    """POST validation (requests 8901-8903)."""
    pipaTaskId = None
    grinder.logger.info("page 21 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pipa pipa on task.id=pipa.id where task.form_url = \'/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/IntalioInternal/ServerLaunch.html\''
    dbConn = getConnection()
    stmt = dbConn.createStatement()
    try:
        rs = stmt.executeQuery(query)
        size =1
        if (rs != None):
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("size ==>" + str(size))                        
            rs.absolute(size)            
            pipaTaskId = rs.getString(1)
            grinder.logger.info("init PIPA Task Operation") 
            grinder.logger.info("PIPA Task Id ==>" + pipaTaskId)            
    finally:
        ensureClosed(stmt)
        ensureClosed(dbConn)
    result = request8901.POST('/gi/validation',
      ( NVPair('assembly', 'TestWidgetForMobile'),
        NVPair('form', 'IntalioWidgets.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+pipaTaskId+'''</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/TestWidgetForMobile/IntalioWidgets.gi/IntalioInternal/ServerLaunch.html?id=9652e37c-8ffb-494f-b736-81fd046c35cb&type=PIPATask&url=%2Fgi%2Fapppath%2FTestWidgetForMobile%2FIntalioWidgets.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
        NVPair('Cache-Control', 'no-cache'), ))

    grinder.sleep(55)
    request8902.GET('/gi/files/JSX/images/icons/logo_16.gif')

    request8903.GET('/gi/files/JSX/images/list/delete.gif')

    return result

  def page90(self):
    """POST updates.htm (request 9001)."""
    result = request9001.POST('/ui-fw/updates.htm',
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

  def page91(self):
    """GET empty.jsp (request 9101)."""
    result = request9101.GET('/ui-fw/script/empty.jsp')

    return result

  def page92(self):
    """POST updates.htm (request 9201)."""
    result = request9201.POST('/ui-fw/updates.htm',
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
    # 12 different values for token_type found in response; the first matched
    # the last known value of token_type - don't update the variable.
    # 33 different values for token_url found in response; the first matched
    # the last known value of token_url - don't update the variable.
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page93(self):
    """GET ServerLaunch.html (request 9301)."""
    self.token_id = \
      'f973951f-16e0-459e-af0a-f2aaf6e8964b'
    self.token_url = \
      '/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html'
    result = request9301.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html' +
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

  def page94(self):
    """GET config.xml (requests 9401-9402)."""
    result = request9401.GET('/gi/apppath/SubstarctDates/form.gi/config.xml')

    grinder.sleep(82)
    request9402.GET('/gi/apppath/SubstarctDates/form.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=f973951f-16e0-459e-af0a-f2aaf6e8964b&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page95(self):
    """GET translations.xml (request 9501)."""
    result = request9501.GET('/gi/apppath/SubstarctDates/form.gi/jss/translations.xml')

    return result

  def page96(self):
    """GET appCanvas.xml (requests 9601-9606)."""
    result = request9601.GET('/gi/apppath/SubstarctDates/form.gi/components/appCanvas.xml')

    grinder.sleep(83)
    request9602.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/Packages.js')

    grinder.sleep(76)
    request9603.GET('/gi/apppath/SubstarctDates/form.gi/js/logic.js')

    grinder.sleep(144)
    request9604.GET('/gi/apppath/SubstarctDates/form.gi/images/attachments.gif')

    request9605.GET('/gi/apppath/SubstarctDates/form.gi/images/close.png')

    request9606.GET('/gi/apppath/SubstarctDates/form.gi/images/error.gif')

    return result

  def page97(self):
    """GET TaskManagementServicesMapping.xml (request 9701)."""
    result = request9701.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page98(self):
    """GET Tidy.xsl (request 9801)."""
    result = request9801.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/Tidy.xsl')

    return result

  def page99(self):
    """POST validation (request 9901)."""
    paTaskId=""
    size=0
    grinder.logger.info("page 9901 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pa pa on task.id=pa.id where pa.state = \'0\' and form_url like \'%SubstarctDates%\' order by creation_date desc'
    i=1
    while (size==0):
            if(i>10):
                break
            dbConn = getConnection()
            stmt = dbConn.createStatement()
            rs = stmt.executeQuery(query)
            size =0
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("i ==>" + str(i))
            grinder.logger.info("size ==>" + str(size))
            grinder.sleep(1000*i)
            i=i+1 
            if (size>0):         
                paTaskId = rs.getString(1)
                grinder.logger.info("get PA Task Operation")
                grinder.logger.info("PA Task Id ==>" + paTaskId)

            ensureClosed(stmt)
            ensureClosed(dbConn)
    result = request9901.POST('/gi/validation',
      ( NVPair('assembly', 'SubstarctDates'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+paTaskId+'''</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page100(self):
    """GET TaskManagementServicesMapping.xml (request 10001)."""
    result = request10001.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page101(self):
    """GET FormModelMapping.xml (request 10101)."""
    result = request10101.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page102(self):
    """POST validation (request 10201)."""
    pipaTaskId = None
    grinder.logger.info("page 10201 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pipa pipa on task.id=pipa.id where task.form_url = \'/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html\''
    dbConn = getConnection()
    stmt = dbConn.createStatement()
    try:
        rs = stmt.executeQuery(query)
        size =1
        if (rs != None):
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("size ==>" + str(size))                        
            rs.absolute(size)            
            pipaTaskId = rs.getString(1)
            grinder.logger.info("init PIPA Task Operation") 
            grinder.logger.info("PIPA Task Id ==>" + pipaTaskId)            
    finally:
        ensureClosed(stmt)
        ensureClosed(dbConn)
    result = request10201.POST('/gi/validation',
      ( NVPair('assembly', 'SubstarctDates'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:initRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+pipaTaskId+'''</jsx1:taskId><jsx1:input><a0:FormModel xmlns:a0=\"http://www.intalio.com/gi/form.gi\"><date1>2012-12-19</date1><date2>2012-12-18</date2></a0:FormModel></jsx1:input><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken><jsx1:formUrl>/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html</jsx1:formUrl></jsx1:initRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page103(self):
    """GET empty.jsp (request 10301)."""
    result = request10301.GET('/ui-fw/script/empty.jsp')

    return result

  def page104(self):
    """POST updates.htm (request 10401)."""
    result = request10401.POST('/ui-fw/updates.htm',
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

  def page105(self):
    """GET ServerLaunch.html (request 10501)."""
    self.token_id = \
      '0cf9b4b5-9624-41ba-94b7-a420e29513e0'
    self.token_url = \
      '/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/IntalioInternal/ServerLaunch.html'
    result = request10501.GET('/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/IntalioInternal/ServerLaunch.html' +
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

  def page106(self):
    """GET config.xml (requests 10601-10602)."""
    result = request10601.GET('/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/config.xml')

    grinder.sleep(77)
    request10602.GET('/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/IntalioInternal/ServerLaunch.html?id=0cf9b4b5-9624-41ba-94b7-a420e29513e0&type=PIPATask&url=%2Fgi%2Fapppath%2FScheduleActions_PXEI_874%2FActionForms.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page107(self):
    """GET translations.xml (request 10701)."""
    result = request10701.GET('/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/jss/translations.xml')

    return result

  def page108(self):
    """GET appCanvas.xml (requests 10801-10806)."""
    result = request10801.GET('/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/components/appCanvas.xml')

    grinder.sleep(73)
    request10802.GET('/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/IntalioInternal/Packages.js')

    grinder.sleep(86)
    request10803.GET('/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/js/logic.js')

    grinder.sleep(128)
    request10804.GET('/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/images/attachments.gif')

    request10805.GET('/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/images/error.gif')

    request10806.GET('/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/images/close.png')

    return result

  def page109(self):
    """GET TaskManagementServicesMapping.xml (request 10901)."""
    result = request10901.GET('/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page110(self):
    """GET Tidy.xsl (request 11001)."""
    result = request11001.GET('/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/IntalioInternal/Tidy.xsl')

    return result

  def page111(self):
    """POST validation (request 11101)."""
    paTaskId=""
    size=0
    grinder.logger.info("page 11101 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pa pa on task.id=pa.id where pa.state = \'0\' and form_url like \'%ScheduleActions_PXEI_874%\' order by creation_date desc'  
    i=1
    while (size==0):
            if(i>10):
                break
            dbConn = getConnection()
            stmt = dbConn.createStatement()
            rs = stmt.executeQuery(query)
            size =0
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("i ==>" + str(i))
            grinder.logger.info("size ==>" + str(size))
            grinder.sleep(1000*i)
            i=i+1 
            if (size>0):         
                paTaskId = rs.getString(1)
                grinder.logger.info("get PA Task Operation")
                grinder.logger.info("PA Task Id ==>" + paTaskId)

            ensureClosed(stmt)
            ensureClosed(dbConn)
    result = request11101.POST('/gi/validation',
      ( NVPair('assembly', 'ScheduleActions_PXEI_874'),
        NVPair('form', 'ActionForms.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+paTaskId+'''</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page112(self):
    """GET TaskManagementServicesMapping.xml (request 11201)."""
    result = request11201.GET('/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page113(self):
    """GET FormModelMapping.xml (request 11301)."""
    result = request11301.GET('/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page114(self):
    """POST validation (request 11401)."""
    pipaTaskId = None
    grinder.logger.info("page 11401 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pipa pipa on task.id=pipa.id where task.form_url = \'/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/IntalioInternal/ServerLaunch.html\''
    dbConn = getConnection()
    stmt = dbConn.createStatement()
    try:
        rs = stmt.executeQuery(query)
        size =1
        if (rs != None):
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("size ==>" + str(size))                        
            rs.absolute(size)            
            pipaTaskId = rs.getString(1)
            grinder.logger.info("init PIPA Task Operation") 
            grinder.logger.info("PIPA Task Id ==>" + pipaTaskId)            
    finally:
        ensureClosed(stmt)
        ensureClosed(dbConn)
    result = request11401.POST('/gi/validation',
      ( NVPair('assembly', 'ScheduleActions_PXEI_874'),
        NVPair('form', 'ActionForms.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:initRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+pipaTaskId+'''</jsx1:taskId><jsx1:input><a0:FormModel xmlns:a0=\"http://www.intalio.com/gi/ActionForms.gi\"><textbox>Sample Form</textbox><text-output-map>[text output]</text-output-map></a0:FormModel></jsx1:input><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken><jsx1:formUrl>/gi/apppath/ScheduleActions_PXEI_874/ActionForms.gi/IntalioInternal/ServerLaunch.html</jsx1:formUrl></jsx1:initRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page115(self):
    """GET empty.jsp (request 11501)."""
    result = request11501.GET('/ui-fw/script/empty.jsp')

    return result

  def page116(self):
    """POST updates.htm (request 11601)."""
    result = request11601.POST('/ui-fw/updates.htm',
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

  def page117(self):
    """GET ServerLaunch.html (request 11701)."""
    self.token_id = \
      'd8ae9f02-c9e9-4017-a33a-2c129d400e29'
    self.token_url = \
      '/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/IntalioInternal/ServerLaunch.html'
    result = request11701.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/IntalioInternal/ServerLaunch.html' +
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

  def page118(self):
    """GET config.xml (requests 11801-11802)."""
    result = request11801.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/config.xml')

    grinder.sleep(78)
    request11802.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/IntalioInternal/ServerLaunch.html?id=d8ae9f02-c9e9-4017-a33a-2c129d400e29&type=PIPATask&url=%2Fgi%2Fapppath%2FRepeatEvery_PXEI_897%2FForms%2Fstart.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page119(self):
    """GET appCanvas.xml (request 11901)."""
    result = request11901.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/components/appCanvas.xml')

    return result

  def page120(self):
    """GET translations.xml (requests 12001-12005)."""
    result = request12001.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/jss/translations.xml')

    grinder.sleep(63)
    request12002.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/IntalioInternal/Packages.js')

    grinder.sleep(81)
    request12003.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/js/logic.js')

    grinder.sleep(147)
    request12004.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/images/attachments.gif')

    request12005.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/images/close.png')

    return result

  def page121(self):
    """GET TaskManagementServicesMapping.xml (request 12101)."""
    result = request12101.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page122(self):
    """GET Tidy.xsl (request 12201)."""
    result = request12201.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/IntalioInternal/Tidy.xsl')

    return result

  def page123(self):
    """POST validation (request 12301)."""
    paTaskId=""
    size=0
    grinder.logger.info("page 12301 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pa pa on task.id=pa.id where pa.state = \'0\' and form_url like \'%RepeatEvery_PXEI_897%\' order by creation_date desc'  
    i=1
    while (size==0):
            if(i>10):
                break
            dbConn = getConnection()
            stmt = dbConn.createStatement()
            rs = stmt.executeQuery(query)
            size =0
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("i ==>" + str(i))
            grinder.logger.info("size ==>" + str(size))
            grinder.sleep(1000*i)
            i=i+1 
            if (size>0):         
                paTaskId = rs.getString(1)
                grinder.logger.info("get PA Task Operation")
                grinder.logger.info("PA Task Id ==>" + paTaskId)

            ensureClosed(stmt)
            ensureClosed(dbConn)
    result = request12301.POST('/gi/validation',
      ( NVPair('assembly', 'RepeatEvery_PXEI_897'),
        NVPair('form', 'Forms/start.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+paTaskId+'''</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page124(self):
    """GET TaskManagementServicesMapping.xml (request 12401)."""
    result = request12401.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page125(self):
    """GET FormModelMapping.xml (request 12501)."""
    result = request12501.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page126(self):
    """POST validation (request 12601)."""
    pipaTaskId = None
    grinder.logger.info("page 12601 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pipa pipa on task.id=pipa.id where task.form_url = \'/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/IntalioInternal/ServerLaunch.html\''
    dbConn = getConnection()
    stmt = dbConn.createStatement()
    try:
        rs = stmt.executeQuery(query)
        size =1
        if (rs != None):
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("size ==>" + str(size))                        
            rs.absolute(size)            
            pipaTaskId = rs.getString(1)
            grinder.logger.info("init PIPA Task Operation") 
            grinder.logger.info("PIPA Task Id ==>" + pipaTaskId)            
    finally:
        ensureClosed(stmt)
        ensureClosed(dbConn)
    result = request12601.POST('/gi/validation',
      ( NVPair('assembly', 'RepeatEvery_PXEI_897'),
        NVPair('form', 'Forms/start.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:initRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+pipaTaskId+'''</jsx1:taskId><jsx1:input><a0:FormModel xmlns:a0=\"http://www.intalio.com/gi/Forms/start.gi\"/></jsx1:input><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken><jsx1:formUrl>/gi/apppath/RepeatEvery_PXEI_897/Forms/start.gi/IntalioInternal/ServerLaunch.html</jsx1:formUrl></jsx1:initRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page127(self):
    """GET empty.jsp (request 12701)."""
    result = request12701.GET('/ui-fw/script/empty.jsp')

    return result

  def page128(self):
    """POST updates.htm (request 12801)."""
    result = request12801.POST('/ui-fw/updates.htm',
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

  def page129(self):
    """GET ServerLaunch.html (request 12901)."""
    self.token_id = \
      '7647e069-9da2-4866-88d2-8f7f91b0db18'
    self.token_url = \
      '/gi/apppath/Ajax_Radio/Radiobuttons.gi/IntalioInternal/ServerLaunch.html'
    result = request12901.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/IntalioInternal/ServerLaunch.html' +
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

  def page130(self):
    """GET config.xml (request 13001)."""
    result = request13001.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/config.xml')

    return result

  def page131(self):
    """GET translations.xml (requests 13101-13102)."""
    result = request13101.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/jss/translations.xml')

    grinder.sleep(76)
    request13102.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/css/style.css')

    return result

  def page132(self):
    """GET appCanvas.xml (requests 13201-13206)."""
    result = request13201.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/components/appCanvas.xml')

    grinder.sleep(78)
    request13202.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/IntalioInternal/Packages.js')

    grinder.sleep(75)
    request13203.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/js/logic.js')

    grinder.sleep(135)
    request13204.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/images/attachments.gif')

    request13205.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/images/close.png')

    request13206.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/images/error.gif')

    return result

  def page133(self):
    """GET TaskManagementServicesMapping.xml (request 13301)."""
    result = request13301.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page134(self):
    """GET Tidy.xsl (request 13401)."""
    result = request13401.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/IntalioInternal/Tidy.xsl')

    return result

  def page135(self):
    """POST validation (request 13501)."""
    paTaskId=""
    size=0
    grinder.logger.info("page 13501 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pa pa on task.id=pa.id where pa.state = \'0\' and form_url like \'%Ajax_Radio%\' order by creation_date desc'  
    i=1
    while (size==0):
            if(i>10):
                break
            dbConn = getConnection()
            stmt = dbConn.createStatement()
            rs = stmt.executeQuery(query)
            size =0
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("i ==>" + str(i))
            grinder.logger.info("size ==>" + str(size))
            grinder.sleep(1000*i)
            i=i+1 
            if (size>0):         
                paTaskId = rs.getString(1)
                grinder.logger.info("get PA Task Operation")
                grinder.logger.info("PA Task Id ==>" + paTaskId)

            ensureClosed(stmt)
            ensureClosed(dbConn)
    result = request13501.POST('/gi/validation',
      ( NVPair('assembly', 'Ajax_Radio'),
        NVPair('form', 'Radiobuttons.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+paTaskId+'''</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page136(self):
    """POST updates.htm (request 13601)."""
    result = request13601.POST('/ui-fw/updates.htm',
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

  def page137(self):
    """GET ServerLaunch.html (request 13701)."""
    self.token_id = \
      '7647e069-9da2-4866-88d2-8f7f91b0db18'
    self.token_url = \
      '/gi/apppath/Ajax_Radio/Radiobuttons.gi/IntalioInternal/ServerLaunch.html'
    result = request13701.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/IntalioInternal/ServerLaunch.html' +
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

  def page138(self):
    """GET config.xml (requests 13801-13802)."""
    result = request13801.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/config.xml')

    grinder.sleep(89)
    request13802.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/css/style.css')

    return result

  def page139(self):
    """GET appCanvas.xml (request 13901)."""
    result = request13901.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/components/appCanvas.xml')

    return result

  def page140(self):
    """GET translations.xml (requests 14001-14006)."""
    result = request14001.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/jss/translations.xml')

    grinder.sleep(71)
    request14002.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/IntalioInternal/Packages.js')

    grinder.sleep(43)
    request14003.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/js/logic.js')

    grinder.sleep(165)
    request14004.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/images/attachments.gif')

    request14005.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/images/close.png')

    request14006.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/images/error.gif')

    return result

  def page141(self):
    """GET TaskManagementServicesMapping.xml (request 14101)."""
    result = request14101.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page142(self):
    """GET Tidy.xsl (request 14201)."""
    result = request14201.GET('/gi/apppath/Ajax_Radio/Radiobuttons.gi/IntalioInternal/Tidy.xsl')

    return result

  def page143(self):
    """POST validation (request 14301)."""
    paTaskId=""
    size=0
    grinder.logger.info("page 14301 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pa pa on task.id=pa.id where pa.state = \'0\' and form_url like \'%Ajax_Radio%\' order by creation_date desc'  
    i=1
    while (size==0):
            if(i>10):
                break
            dbConn = getConnection()
            stmt = dbConn.createStatement()
            rs = stmt.executeQuery(query)
            size =0
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("i ==>" + str(i))
            grinder.logger.info("size ==>" + str(size))
            grinder.sleep(1000*i)
            i=i+1 
            if (size>0):         
                paTaskId = rs.getString(1)
                grinder.logger.info("get PA Task Operation")
                grinder.logger.info("PA Task Id ==>" + paTaskId)

            ensureClosed(stmt)
            ensureClosed(dbConn)
    result = request14301.POST('/gi/validation',
      ( NVPair('assembly', 'Ajax_Radio'),
        NVPair('form', 'Radiobuttons.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+paTaskId+'''</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page144(self):
    """POST updates.htm (request 14401)."""
    result = request14401.POST('/ui-fw/updates.htm',
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

  def page145(self):
    """GET ServerLaunch.html (request 14501)."""
    self.token_id = \
      '5813e897-a8c8-48d8-96a7-fa864a420f2e'
    self.token_url = \
      '/gi/apppath/AjaxDatePicker/DatePicker.gi/IntalioInternal/ServerLaunch.html'
    result = request14501.GET('/gi/apppath/AjaxDatePicker/DatePicker.gi/IntalioInternal/ServerLaunch.html' +
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

  def page146(self):
    """GET config.xml (request 14601)."""
    result = request14601.GET('/gi/apppath/AjaxDatePicker/DatePicker.gi/config.xml')

    return result

  def page147(self):
    """GET translations.xml (requests 14701-14702)."""
    result = request14701.GET('/gi/apppath/AjaxDatePicker/DatePicker.gi/jss/translations.xml')

    request14702.GET('/gi/apppath/AjaxDatePicker/DatePicker.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxDatePicker/DatePicker.gi/IntalioInternal/ServerLaunch.html?id=5813e897-a8c8-48d8-96a7-fa864a420f2e&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxDatePicker%2FDatePicker.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page148(self):
    """GET appCanvas.xml (requests 14801-14806)."""
    result = request14801.GET('/gi/apppath/AjaxDatePicker/DatePicker.gi/components/appCanvas.xml')

    grinder.sleep(14)
    request14802.GET('/gi/apppath/AjaxDatePicker/DatePicker.gi/IntalioInternal/Packages.js')

    grinder.sleep(63)
    request14803.GET('/gi/apppath/AjaxDatePicker/DatePicker.gi/js/logic.js')

    grinder.sleep(257)
    request14804.GET('/gi/apppath/AjaxDatePicker/DatePicker.gi/images/attachments.gif')

    request14805.GET('/gi/apppath/AjaxDatePicker/DatePicker.gi/images/close.png')

    request14806.GET('/gi/apppath/AjaxDatePicker/DatePicker.gi/images/error.gif')

    return result

  def page149(self):
    """GET TaskManagementServicesMapping.xml (request 14901)."""
    result = request14901.GET('/gi/apppath/AjaxDatePicker/DatePicker.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page150(self):
    """GET Tidy.xsl (request 15001)."""
    result = request15001.GET('/gi/apppath/AjaxDatePicker/DatePicker.gi/IntalioInternal/Tidy.xsl')

    return result

  def page151(self):
    """POST validation (request 15101)."""
    pipaTaskId = None
    grinder.logger.info("page 15101 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pipa pipa on task.id=pipa.id where task.form_url = \'/gi/apppath/AjaxDatePicker/DatePicker.gi/IntalioInternal/ServerLaunch.html\''
    dbConn = getConnection()
    stmt = dbConn.createStatement()
    try:
        rs = stmt.executeQuery(query)
        size =1
        if (rs != None):
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("size ==>" + str(size))                        
            rs.absolute(size)            
            pipaTaskId = rs.getString(1)
            grinder.logger.info("get PIPA Task Operation") 
            grinder.logger.info("PIPA Task Id ==>" + pipaTaskId)            
    finally:
        ensureClosed(stmt)
        ensureClosed(dbConn)
    result = request15101.POST('/gi/validation',
      ( NVPair('assembly', 'AjaxDatePicker'),
        NVPair('form', 'DatePicker.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+pipaTaskId+'''</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxDatePicker/DatePicker.gi/IntalioInternal/ServerLaunch.html?id=5813e897-a8c8-48d8-96a7-fa864a420f2e&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxDatePicker%2FDatePicker.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
        NVPair('Cache-Control', 'no-cache'), ))

    return result

  def page152(self):
    """POST updates.htm (request 15201)."""
    result = request15201.POST('/ui-fw/updates.htm',
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

  def page153(self):
    """GET empty.jsp (request 15301)."""
    result = request15301.GET('/ui-fw/script/empty.jsp')

    return result

  def page154(self):
    """POST updates.htm (request 15401)."""
    result = request15401.POST('/ui-fw/updates.htm',
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
    # 12 different values for token_type found in response; the first matched
    # the last known value of token_type - don't update the variable.
    # 33 different values for token_url found in response; the first matched
    # the last known value of token_url - don't update the variable.
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page155(self):
    """GET ServerLaunch.html (request 15501)."""
    self.token_id = \
      'fa2a15cb-b048-4f17-a5b0-20e55c6a74b2'
    self.token_url = \
      '/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/IntalioInternal/ServerLaunch.html'
    result = request15501.GET('/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/IntalioInternal/ServerLaunch.html' +
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

  def page156(self):
    """GET config.xml (request 15601)."""
    result = request15601.GET('/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/config.xml')

    return result

  def page157(self):
    """GET translations.xml (requests 15701-15702)."""
    result = request15701.GET('/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/jss/translations.xml')

    request15702.GET('/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/IntalioInternal/ServerLaunch.html?id=fa2a15cb-b048-4f17-a5b0-20e55c6a74b2&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxCheckbox%2FAjaxCheckbox.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page158(self):
    """GET appCanvas.xml (requests 15801-15806)."""
    result = request15801.GET('/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/components/appCanvas.xml')

    grinder.sleep(65)
    request15802.GET('/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/IntalioInternal/Packages.js')

    grinder.sleep(77)
    request15803.GET('/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/js/logic.js')

    grinder.sleep(142)
    request15804.GET('/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/images/attachments.gif')

    request15805.GET('/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/images/error.gif')

    request15806.GET('/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/images/close.png')

    return result

  def page159(self):
    """GET TaskManagementServicesMapping.xml (request 15901)."""
    result = request15901.GET('/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page160(self):
    """GET Tidy.xsl (request 16001)."""
    result = request16001.GET('/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/IntalioInternal/Tidy.xsl')

    return result

  def page161(self):
    """POST validation (request 16101)."""
    pipaTaskId = None
    grinder.logger.info("page 16101 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pipa pipa on task.id=pipa.id where task.form_url = \'/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/IntalioInternal/ServerLaunch.html\''
    dbConn = getConnection()
    stmt = dbConn.createStatement()
    try:
        rs = stmt.executeQuery(query)
        size =1
        if (rs != None):
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("size ==>" + str(size))                        
            rs.absolute(size)            
            pipaTaskId = rs.getString(1)
            grinder.logger.info("init PIPA Task Operation") 
            grinder.logger.info("PIPA Task Id ==>" + pipaTaskId)            
    finally:
        ensureClosed(stmt)
        ensureClosed(dbConn)
    result = request16101.POST('/gi/validation',
      ( NVPair('assembly', 'AjaxCheckbox'),
        NVPair('form', 'AjaxCheckbox.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+pipaTaskId+'''</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxCheckbox/AjaxCheckbox.gi/IntalioInternal/ServerLaunch.html?id=fa2a15cb-b048-4f17-a5b0-20e55c6a74b2&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxCheckbox%2FAjaxCheckbox.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
        NVPair('Cache-Control', 'no-cache'), ))

    return result

  def page162(self):
    """POST updates.htm (request 16201)."""
    result = request16201.POST('/ui-fw/updates.htm',
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

  def page163(self):
    """GET empty.jsp (request 16301)."""
    result = request16301.GET('/ui-fw/script/empty.jsp')

    return result

  def page164(self):
    """POST updates.htm (request 16401)."""
    result = request16401.POST('/ui-fw/updates.htm',
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
    # 12 different values for token_type found in response; the first matched
    # the last known value of token_type - don't update the variable.
    # 33 different values for token_url found in response; the first matched
    # the last known value of token_url - don't update the variable.
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page165(self):
    """GET ServerLaunch.html (request 16501)."""
    self.token_id = \
      'a9802d95-55dd-464e-93dd-c6eaf7d35d5f'
    self.token_url = \
      '/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/IntalioInternal/ServerLaunch.html'
    result = request16501.GET('/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/IntalioInternal/ServerLaunch.html' +
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

  def page166(self):
    """GET config.xml (requests 16601-16602)."""
    result = request16601.GET('/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/config.xml')

    grinder.sleep(69)
    request16602.GET('/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/IntalioInternal/ServerLaunch.html?id=a9802d95-55dd-464e-93dd-c6eaf7d35d5f&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxChainedExecution%2FSelectTransportation.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page167(self):
    """GET appCanvas.xml (requests 16701-16706)."""
    result = request16701.GET('/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/components/appCanvas.xml')

    grinder.sleep(94)
    request16702.GET('/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/IntalioInternal/Packages.js')

    grinder.sleep(86)
    request16703.GET('/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/js/logic.js')

    grinder.sleep(140)
    request16704.GET('/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/images/attachments.gif')

    request16705.GET('/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/images/error.gif')

    request16706.GET('/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/images/close.png')

    return result

  def page168(self):
    """GET TaskManagementServicesMapping.xml (request 16801)."""
    result = request16801.GET('/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page169(self):
    """GET Tidy.xsl (request 16901)."""
    result = request16901.GET('/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/IntalioInternal/Tidy.xsl')

    return result

  def page170(self):
    """POST validation (request 17001)."""
    pipaTaskId = None
    grinder.logger.info("page 21 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pipa pipa on task.id=pipa.id where task.form_url = \'/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/IntalioInternal/ServerLaunch.html\''
    dbConn = getConnection()
    stmt = dbConn.createStatement()
    try:
        rs = stmt.executeQuery(query)
        size =1
        if (rs != None):
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("size ==>" + str(size))                        
            rs.absolute(size)            
            pipaTaskId = rs.getString(1)
            grinder.logger.info("init PIPA Task Operation") 
            grinder.logger.info("PIPA Task Id ==>" + pipaTaskId)            
    finally:
     ensureClosed(stmt)
     ensureClosed(dbConn)
    result = request17001.POST('/gi/validation',
      ( NVPair('assembly', 'AjaxChainedExecution'),
        NVPair('form', 'SelectTransportation.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+pipaTaskId+'''</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/AjaxChainedExecution/SelectTransportation.gi/IntalioInternal/ServerLaunch.html?id=a9802d95-55dd-464e-93dd-c6eaf7d35d5f&type=PIPATask&url=%2Fgi%2Fapppath%2FAjaxChainedExecution%2FSelectTransportation.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'),
        NVPair('Cache-Control', 'no-cache'), ))

    return result

  def page171(self):
    """POST updates.htm (request 17101)."""
    result = request17101.POST('/ui-fw/updates.htm',
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

  def page172(self):
    """GET empty.jsp (request 17201)."""
    result = request17201.GET('/ui-fw/script/empty.jsp')

    return result

  def page173(self):
    """POST updates.htm (request 17301)."""
    result = request17301.POST('/ui-fw/updates.htm',
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
    # 12 different values for token_type found in response; the first matched
    # the last known value of token_type - don't update the variable.
    # 33 different values for token_url found in response; the first matched
    # the last known value of token_url - don't update the variable.
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page174(self):
    """GET init (request 17401)."""
    self.token_id = \
      '8c9086f2-6ff4-4374-a570-3016ddec072e'
    self.token_url = \
      '/AbsenceRequest/AbsenceRequest.xform'
    result = request17401.GET('/xFormsManager/init' +
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
    self.token_staticstate = \
      httpUtilities.valueFromHiddenInput('$static-state') # 'pers:4CA35498-B291-AD04-B3A2-09C2ECC3E59...'
    self.token_dynamicstate = \
      httpUtilities.valueFromHiddenInput('$dynamic-state') # 'pers:8F998C4C-9B10-D981-B723-68ACEF1CF86...'
    self.token_serverevents = \
      httpUtilities.valueFromHiddenInput('$server-events') # ''
    self.token_clientstate = \
      httpUtilities.valueFromHiddenInput('$client-state') # ''
    self.token_repeattree = \
      httpUtilities.valueFromHiddenInput('$repeat-tree') # 'lineSet'
    self.token_repeatindexes = \
      httpUtilities.valueFromHiddenInput('$repeat-indexes') # 'lineSet 1'

    return result

  def page175(self):
    """POST xforms-server (request 17501)."""
    result = request17501.POST('/xFormsManager/xforms-server',
      '''<!DOCTYPE xxforms:event-request [<!ENTITY nbsp \"&#160;\">]>\n<xxforms:event-request xmlns:xxforms=\"http://orbeon.org/oxf/xml/xforms\">\n    <xxforms:static-state>pers:4CA35498-B291-AD04-B3A2-09C2ECC3E598</xxforms:static-state>\n    <xxforms:dynamic-state>pers:8F998C4C-9B10-D981-B723-68ACEF1CF86A</xxforms:dynamic-state>\n    <xxforms:action>\n        <xxforms:event name=\"DOMFocusIn\" source-control-id=\"xf-11\"></xxforms:event>\n        <xxforms:event name=\"DOMActivate\" source-control-id=\"xf-11\"></xxforms:event>\n    </xxforms:action>\n</xxforms:event-request>''',
      ( NVPair('Content-Type', 'application/xml; charset=UTF-8'), ))

    return result

  def page176(self):
    """POST xforms-server (request 17601)."""
    result = request17601.POST('/xFormsManager/xforms-server',
      '''<!DOCTYPE xxforms:event-request [<!ENTITY nbsp \"&#160;\">]>\n<xxforms:event-request xmlns:xxforms=\"http://orbeon.org/oxf/xml/xforms\">\n    <xxforms:static-state>pers:4CA35498-B291-AD04-B3A2-09C2ECC3E598</xxforms:static-state>\n    <xxforms:dynamic-state>pers:91C9E47D-F7C6-1196-7910-461962B9041B</xxforms:dynamic-state>\n    <xxforms:action>\n        <xxforms:event name=\"DOMFocusOut\" source-control-id=\"xf-11\"></xxforms:event>\n        <xxforms:event name=\"DOMFocusIn\" source-control-id=\"xf-86\"></xxforms:event>\n        <xxforms:event name=\"DOMActivate\" source-control-id=\"xf-86\"></xxforms:event>\n    </xxforms:action>\n</xxforms:event-request>''',
      ( NVPair('Content-Type', 'application/xml; charset=UTF-8'), ))

    return result

  def page177(self):
    """POST init (request 17701)."""
    self.token_dynamicstate = \
      'pers:12CE694F-9F52-814A-EEF6-0E4B14747AF4'
    self.token_serverevents = \
      'X2ztnLbujs+XocNBu3ADXGPfD6vdqqkYcLQqj/XYbeEKOot+i+ET3USU8tRk6y72bAz1vzPGvWtjw/4gTjAZuZEjl9QTQKtW4BMz4TkOT8XJBWtIANXLDFppGFa/o8ub50d7qy3UYWy8WH901rqOFPXtWhZryEAFnRsoo0zyvf2n+RtQnqsRyjAmg2ckRypA+ntW/pgpTvIjfXbvpwaKVf7eyjqBaxhtIngTU0Aw5L4oEHH2g9m1qiYCuA4hcT6ikYh7BKlkXxAuc='
    self.token_clientstate = \
      'initial-dynamic-state&pers%3A8F998C4C-9B10-D981-B723-68ACEF1CF86A&load-did-run&true'
    result = request17701.POST('/xFormsManager/init' +
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
      self.token_claimTaskOnOpen,
      ( NVPair('$static-state', self.token_staticstate),
        NVPair('$dynamic-state', self.token_dynamicstate),
        NVPair('$server-events', self.token_serverevents),
        NVPair('$client-state', self.token_clientstate),
        NVPair('$repeat-tree', self.token_repeattree),
        NVPair('$repeat-indexes', self.token_repeatindexes),
        NVPair('xf-30$xforms-input-1', 'Michael Smith'),
        NVPair('xf-32$xforms-input-1', '+1(650)596-1800'),
        NVPair('xf-33$xforms-input-1', 'msmith@examples.intalio.com'),
        NVPair('xf-38$xforms-input-1·1', '12/5/2005'),
        NVPair('xf-40$xforms-input-1·1', '12/9/2005'),
        NVPair('xf-42·1', '4YJZaO3qyVw='),
        NVPair('xf-76$xforms-input-1·1', '40'),
        NVPair('xf-38$xforms-input-1·2', '2/6/2006'),
        NVPair('xf-40$xforms-input-1·2', '2/10/2006'),
        NVPair('xf-42·2', '4YJZaO3qyVw='),
        NVPair('xf-76$xforms-input-1·2', '40'),
        NVPair('xf-38$xforms-input-1', ''),
        NVPair('xf-40$xforms-input-1', ''),
        NVPair('xf-42', '4YJZaO3qyVw='),
        NVPair('xf-76$xforms-input-1', ''),
        NVPair('xf-82$xforms-input-1', 'Emily Williams'),
        NVPair('xf-83$xforms-input-1', '+1(650)596-1800'),
        NVPair('xf-84$xforms-input-1', 'ewilliams@examples.intalio.com'),
        NVPair('xf-85', 'This is sample data for this form.'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    return result

  def page178(self):
    """GET tasks.htm (request 17801)."""
    result = request17801.GET('/ui-fw/tasks.htm')

    return result

  def page179(self):
    """GET empty.jsp (request 17901)."""
    result = request17901.GET('/ui-fw/script/empty.jsp')

    return result

  def page180(self):
    """POST vacation.htm (request 18001)."""
    result = request18001.POST('/ui-fw/vacation.htm',
      ( NVPair('action', 'Validate'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page181(self):
    """POST updates.htm (request 18101)."""
    result = request18101.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 40 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '11d1def534ea1be0:-22d659cb:13b835e25e8:-...'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'PATask'
    # 37 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # 'http://localhost:8080/wds/AbsenceRequest...'
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page182(self):
    """POST updates.htm (request 18201)."""
    result = request18201.POST('/ui-fw/updates.htm',
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
      httpUtilities.valueFromBodyURI('id') # 'notify-U6ZE-9410-1ZE2-U62U'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'Notification'
    # 3 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/RepeatEvery_PXEI_897/Forms/n...'
    # 2 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page183(self):
    """POST updates.htm (request 18301)."""
    result = request18301.POST('/ui-fw/updates.htm',
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

  def page184(self):
    """GET empty.jsp (request 18401)."""
    result = request18401.GET('/ui-fw/script/empty.jsp')

    return result

  def page185(self):
    """POST updates.htm (request 18501)."""
    result = request18501.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 39 different values for token_id found in response; the first matched
    # the last known value of token_id - don't update the variable.
    # 36 different values for token_url found in response; the first matched
    # the last known value of token_url - don't update the variable.
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page186(self):
    """GET act (requests 18601-18603)."""
    result = request18601.GET('/xFormsManager/act' +
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
    self.token_staticstate = \
      httpUtilities.valueFromHiddenInput('$static-state') # 'pers:8C2BD512-800A-0391-4B45-1048726412E...'
    self.token_dynamicstate = \
      httpUtilities.valueFromHiddenInput('$dynamic-state') # 'pers:CD841D14-68AA-E482-6A16-DB290FEE04F...'
    self.token_serverevents = \
      httpUtilities.valueFromHiddenInput('$server-events') # ''
    self.token_clientstate = \
      httpUtilities.valueFromHiddenInput('$client-state') # ''
    self.token_repeattree = \
      httpUtilities.valueFromHiddenInput('$repeat-tree') # 'attachmentsTable,lineSet'
    self.token_repeatindexes = \
      httpUtilities.valueFromHiddenInput('$repeat-indexes') # 'lineSet 1,attachmentsTable 0'

    grinder.sleep(22)
    request18602.GET('/xFormsManager/images/attachments.gif')

    request18603.GET('/xFormsManager/ops/images/xforms/remove.gif')

    return result

  def page187(self):
    """POST xforms-server (request 18701)."""
    result = request18701.POST('/xFormsManager/xforms-server',
      '''<!DOCTYPE xxforms:event-request [<!ENTITY nbsp \"&#160;\">]>\n<xxforms:event-request xmlns:xxforms=\"http://orbeon.org/oxf/xml/xforms\">\n    <xxforms:static-state>pers:8C2BD512-800A-0391-4B45-1048726412EB</xxforms:static-state>\n    <xxforms:dynamic-state>pers:CD841D14-68AA-E482-6A16-DB290FEE04F0</xxforms:dynamic-state>\n    <xxforms:action>\n        <xxforms:event name=\"DOMFocusIn\" source-control-id=\"xf-117\"></xxforms:event>\n        <xxforms:event name=\"xxforms-value-change-with-focus-change\" source-control-id=\"xf-117\">RF3uMliN1+I=</xxforms:event>\n    </xxforms:action>\n</xxforms:event-request>''',
      ( NVPair('Content-Type', 'application/xml; charset=UTF-8'), ))

    return result

  def page188(self):
    """POST xforms-server (request 18801)."""
    result = request18801.POST('/xFormsManager/xforms-server',
      '''<!DOCTYPE xxforms:event-request [<!ENTITY nbsp \"&#160;\">]>\n<xxforms:event-request xmlns:xxforms=\"http://orbeon.org/oxf/xml/xforms\">\n    <xxforms:static-state>pers:8C2BD512-800A-0391-4B45-1048726412EB</xxforms:static-state>\n    <xxforms:dynamic-state>pers:18955FE6-00E4-83A5-172C-809DAF8481AB</xxforms:dynamic-state>\n    <xxforms:action>\n        <xxforms:event name=\"DOMFocusOut\" source-control-id=\"xf-117\"></xxforms:event>\n        <xxforms:event name=\"DOMFocusIn\" source-control-id=\"xf-130\"></xxforms:event>\n        <xxforms:event name=\"DOMActivate\" source-control-id=\"xf-130\"></xxforms:event>\n    </xxforms:action>\n</xxforms:event-request>''',
      ( NVPair('Content-Type', 'application/xml; charset=UTF-8'), ))

    return result

  def page189(self):
    """POST act (request 18901)."""
    self.token_id = \
      '11d1def534ea1be0:-22d659cb:13b835e25e8:-1249127.0.0.184'
    self.token_type = \
      'PATask'
    self.token_url = \
      'http://localhost:8080/wds/AbsenceRequest/AbsenceApproval.xform'
    self.token_dynamicstate = \
      'pers:BC21D0AC-3DFE-546C-9276-C2E88E93FDB6'
    self.token_serverevents = \
      'X2ztnLbujs+XocNBu3ADXGPbA4oARPCjKA/bMdupU+9QdKsWPJocVTQ9hmj60pCxqi7t4upRjq/RJVuX1+0Qk773leOwpK94KO7as00PXCMEcM5UU3/3LWmQbifCquY/BmhwBhBp/kRgUHtzCOgRwBlnhob7HQbJs5VwX+FFv9ZUF6FH5cQzzw1SxULxggrFIjhsYzwWZki2k7U/PMrDNFWsqZObJw5R4fJmXs2P/uM0u4CkZbCw7rexZJXh3jJc/dM1xus1bnrxA='
    self.token_clientstate = \
      'initial-dynamic-state&pers%3ACD841D14-68AA-E482-6A16-DB290FEE04F0&load-did-run&true'
    result = request18901.POST('/xFormsManager/act' +
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
      self.token_claimTaskOnOpen,
      ( NVPair('$static-state', self.token_staticstate),
        NVPair('$dynamic-state', self.token_dynamicstate),
        NVPair('$server-events', self.token_serverevents),
        NVPair('$client-state', self.token_clientstate),
        NVPair('$repeat-tree', self.token_repeattree),
        NVPair('$repeat-indexes', self.token_repeatindexes),
        NVPair('xf-79', 'LzQCBxo8rXo='),
        NVPair('new-attachment-title$xforms-input-1', ''),
        NVPair('new-attachment-file', ''),
        NVPair('new-attachment-text', ''),
        NVPair('xf-113$xforms-input-1', 'Emily Williams'),
        NVPair('xf-114$xforms-input-1', '+1(650)596-1800'),
        NVPair('xf-115$xforms-input-1', 'ewilliams@examples.intalio.com'),
        NVPair('xf-117', 'RF3uMliN1+I='),
        NVPair('xf-125', ''), ),
      ( NVPair('Content-Type', 'multipart/form-data; boundary=---------------------------16600779578037619111268146518'), ),
      True)

    return result

  def page190(self):
    """GET tasks.htm (request 19001)."""
    result = request19001.GET('/ui-fw/tasks.htm')

    return result

  def page191(self):
    """GET empty.jsp (request 19101)."""
    result = request19101.GET('/ui-fw/script/empty.jsp')

    return result

  def page192(self):
    """POST vacation.htm (request 19201)."""
    result = request19201.POST('/ui-fw/vacation.htm',
      ( NVPair('action', 'Validate'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page193(self):
    """POST updates.htm (request 19301)."""
    result = request19301.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 36 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '11d1def534ea1be0:-22d659cb:13b835e25e8:-...'
    # 31 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/RepeatEvery_PXEI_897/Forms/P...'
    # 4 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page194(self):
    """POST updates.htm (request 19401)."""
    result = request19401.POST('/ui-fw/updates.htm',
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
      httpUtilities.valueFromBodyURI('id') # 'notify-NBBK-4ZJJ-LPWD-LEYS'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'Notification'
    # 29 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # 'oxf://AbsenceRequest/Notification.xform'
    # 2 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page195(self):
    """POST updates.htm (request 19501)."""
    result = request19501.POST('/ui-fw/updates.htm',
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

  def page196(self):
    """GET empty.jsp (request 19601)."""
    result = request19601.GET('/ui-fw/script/empty.jsp')

    return result

  def page197(self):
    """POST updates.htm (request 19701)."""
    result = request19701.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 36 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '11d1def534ea1be0:-22d659cb:13b835e25e8:-...'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'PATask'
    # 31 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/RepeatEvery_PXEI_897/Forms/P...'
    # 4 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page198(self):
    """GET ServerLaunch.html (request 19801)."""
    result = request19801.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/IntalioInternal/ServerLaunch.html' +
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

  def page199(self):
    """GET config.xml (requests 19901-19902)."""
    result = request19901.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/config.xml')

    grinder.sleep(116)
    request19902.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-127b127.0.0.180&type=PATask&url=%2Fgi%2Fapppath%2FRepeatEvery_PXEI_897%2FForms%2FPA.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page200(self):
    """GET appCanvas.xml (request 20001)."""
    result = request20001.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/components/appCanvas.xml')

    return result

  def page201(self):
    """GET translations.xml (requests 20101-20105)."""
    result = request20101.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/jss/translations.xml')

    grinder.sleep(55)
    request20102.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/IntalioInternal/Packages.js')

    grinder.sleep(70)
    request20103.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/js/logic.js')

    request20104.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/images/attachments.gif')

    grinder.sleep(123)
    request20105.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/images/close.png')

    return result

  def page202(self):
    """GET TaskManagementServicesMapping.xml (request 20201)."""
    result = request20201.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page203(self):
    """GET Tidy.xsl (request 20301)."""
    result = request20301.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/IntalioInternal/Tidy.xsl')

    return result

  def page204(self):
    """POST validation (request 20401)."""
    paTaskId=""
    size=0
    grinder.logger.info("page 20401 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pa pa on task.id=pa.id where pa.state = \'0\' and form_url like \'%RepeatEvery_PXEI_897%\' order by creation_date desc'
    i=1
    while (size==0):
            if(i>10):
                break
            dbConn = getConnection()
            stmt = dbConn.createStatement()
            rs = stmt.executeQuery(query)
            size =0
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("i ==>" + str(i))
            grinder.logger.info("size ==>" + str(size))
            grinder.sleep(1000*i)
            i=i+1 
            if (size>0):         
                paTaskId = rs.getString(1)
                grinder.logger.info("get PA Task Operation")
                grinder.logger.info("PA Task Id ==>" + paTaskId)

            ensureClosed(stmt)
            ensureClosed(dbConn)
    result = request20401.POST('/gi/validation',
      ( NVPair('assembly', 'RepeatEvery_PXEI_897'),
        NVPair('form', 'Forms/PA.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+paTaskId+'''</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page205(self):
    """GET FormModelMapping.xml (request 20501)."""
    result = request20501.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page206(self):
    """GET TaskManagerProcessMapping.xml (request 20601)."""
    result = request20601.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/IntalioInternal/TaskManagerProcessMapping.xml')

    return result

  def page207(self):
    """GET FormModelMapping.xml (request 20701)."""
    result = request20701.GET('/gi/apppath/RepeatEvery_PXEI_897/Forms/PA.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page208(self):
    """POST validation (request 20801)."""
    paTaskId=""
    size=0
    grinder.logger.info("page 20801 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pa pa on task.id=pa.id where pa.state = \'0\' and form_url like \'%RepeatEvery_PXEI_897%\' order by creation_date desc'
    i=1
    while (size==0):
            if(i>10):
                break
            dbConn = getConnection()
            stmt = dbConn.createStatement()
            rs = stmt.executeQuery(query)
            size =0
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("i ==>" + str(i))
            grinder.logger.info("size ==>" + str(size))
            grinder.sleep(1000*i)
            i=i+1 
            if (size>0):         
                paTaskId = rs.getString(1)
                grinder.logger.info("get PA Task Operation")
                grinder.logger.info("PA Task Id ==>" + paTaskId)

            ensureClosed(stmt)
            ensureClosed(dbConn)
    result = request20801.POST('/gi/validation',
      ( NVPair('assembly', 'RepeatEvery_PXEI_897'),
        NVPair('form', 'Forms/PA.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:completeTaskRequest xmlns:jsx1=\"http://www.intalio.com/bpms/workflow/ib4p_20051115\"><jsx1:taskMetaData><jsx1:taskId>'''+paTaskId+'''</jsx1:taskId></jsx1:taskMetaData><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken><jsx1:user>intalio\\admin</jsx1:user><jsx1:taskOutput><a0:FormModel xmlns:a0=\"http://www.intalio.com/gi/Forms/PA.gi\"/></jsx1:taskOutput></jsx1:completeTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page209(self):
    """GET empty.jsp (request 20901)."""
    result = request20901.GET('/ui-fw/script/empty.jsp')

    return result

  def page210(self):
    """POST updates.htm (request 21001)."""
    result = request21001.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 34 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '11d1def534ea1be0:-22d659cb:13b835e25e8:-...'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'PATask'
    # 28 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/SubstarctDates/form.gi/Intal...'
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page211(self):
    """POST proxy.jsp (request 21101)."""
    result = request21101.POST('/ui-fw/script/proxy.jsp',
      '<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\"><soapenv:Body><getAssignedRoles xmlns=\"http://tempo.intalio.org/security/RBACQueryService/\"><user>intalio\\\\admin</user></getAssignedRoles></soapenv:Body></soapenv:Envelope>',
      ( NVPair('Content-Type', 'text/xml; charset=\"utf-8\"'), ))

    return result

  def page212(self):
    """POST proxy.jsp (request 21201)."""
    result = request21201.POST('/ui-fw/script/proxy.jsp',
      '<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\"><soapenv:Body><getAssignedUsers xmlns=\"http://tempo.intalio.org/security/RBACQueryService/\"><role>intalio\\\\WorkflowAdministrator</role></getAssignedUsers></soapenv:Body></soapenv:Envelope>',
      ( NVPair('Content-Type', 'text/xml; charset=\"utf-8\"'), ))

    return result

  def page213(self):
    """POST proxy.jsp (request 21301)."""
    result = request21301.POST('/ui-fw/script/proxy.jsp',
      '<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\"><soapenv:Body><reassign xmlns=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><taskId>11d1def534ea1be0:-22d659cb:13b835e25e8:-1282127.0.0.174</taskId><userOwner></userOwner><roleOwner>intalio\\\\WorkflowAdministrator</roleOwner><taskState>READY</taskState><participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</participantToken><userAction>REASSIGN</userAction></reassign></soapenv:Body></soapenv:Envelope>',
      ( NVPair('Content-Type', 'text/xml; charset=\"utf-8\"'), ))

    return result

  def page214(self):
    """POST updates.htm (request 21401)."""
    result = request21401.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 33 different values for token_id found in response; the first matched
    # the last known value of token_id - don't update the variable.
    # 27 different values for token_url found in response; the first matched
    # the last known value of token_url - don't update the variable.
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.
    # 1 different values for token_claimTaskOnOpen found in response; the first matched
    # the last known value of token_claimTaskOnOpen - don't update the variable.

    return result

  def page215(self):
    """GET ServerLaunch.html (request 21501)."""
    result = request21501.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html' +
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

  def page216(self):
    """GET config.xml (requests 21601-21602)."""
    result = request21601.GET('/gi/apppath/SubstarctDates/form.gi/config.xml')

    grinder.sleep(89)
    request21602.GET('/gi/apppath/SubstarctDates/form.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-1282127.0.0.174&type=PATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page217(self):
    """GET appCanvas.xml (request 21701)."""
    result = request21701.GET('/gi/apppath/SubstarctDates/form.gi/components/appCanvas.xml')

    return result

  def page218(self):
    """GET translations.xml (requests 21801-21806)."""
    result = request21801.GET('/gi/apppath/SubstarctDates/form.gi/jss/translations.xml')

    grinder.sleep(111)
    request21802.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/Packages.js')

    grinder.sleep(57)
    request21803.GET('/gi/apppath/SubstarctDates/form.gi/js/logic.js')

    grinder.sleep(151)
    request21804.GET('/gi/apppath/SubstarctDates/form.gi/images/attachments.gif')

    request21805.GET('/gi/apppath/SubstarctDates/form.gi/images/close.png')

    request21806.GET('/gi/apppath/SubstarctDates/form.gi/images/error.gif')

    return result

  def page219(self):
    """GET TaskManagementServicesMapping.xml (request 21901)."""
    result = request21901.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page220(self):
    """GET Tidy.xsl (request 22001)."""
    result = request22001.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/Tidy.xsl')

    return result

  def page221(self):
    """POST validation (request 22101)."""
    paTaskId=""
    size=0
    grinder.logger.info("page 22101 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pa pa on task.id=pa.id where pa.state = \'0\' and form_url like \'%SubstarctDates%\' order by creation_date desc'  
    i=1
    while (size==0):
            if(i>10):
                break
            dbConn = getConnection()
            stmt = dbConn.createStatement()
            rs = stmt.executeQuery(query)
            size =0
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("i ==>" + str(i))
            grinder.logger.info("size ==>" + str(size))
            grinder.sleep(1000*i)
            i=i+1 
            if (size>0):         
                paTaskId = rs.getString(1)
                grinder.logger.info("get PA Task Operation")
                grinder.logger.info("PA Task Id ==>" + paTaskId)

            ensureClosed(stmt)
            ensureClosed(dbConn)
    result = request22101.POST('/gi/validation',
      ( NVPair('assembly', 'SubstarctDates'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+paTaskId+'''</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page222(self):
    """GET FormModelMapping.xml (request 22201)."""
    result = request22201.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page223(self):
    """GET TaskManagerProcessMapping.xml (request 22301)."""
    result = request22301.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/TaskManagerProcessMapping.xml')

    return result

  def page224(self):
    """GET FormModelMapping.xml (request 22401)."""
    result = request22401.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page225(self):
    """POST validation (request 22501)."""
    paTaskId=""
    size=0
    grinder.logger.info("page 22501 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pa pa on task.id=pa.id where pa.state = \'0\' and form_url like \'%SubstarctDates%\' order by creation_date desc'
    i=1
    while (size==0):
            if(i>10):
                break
            dbConn = getConnection()
            stmt = dbConn.createStatement()
            rs = stmt.executeQuery(query)
            size =0
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("i ==>" + str(i))
            grinder.logger.info("size ==>" + str(size))
            grinder.sleep(1000*i)
            i=i+1 
            if (size>0):         
                paTaskId = rs.getString(1)
                grinder.logger.info("get PA Task Operation")
                grinder.logger.info("PA Task Id ==>" + paTaskId)

            ensureClosed(stmt)
            ensureClosed(dbConn)
    result = request22501.POST('/gi/validation',
      ( NVPair('assembly', 'SubstarctDates'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:completeTaskRequest xmlns:jsx1=\"http://www.intalio.com/bpms/workflow/ib4p_20051115\"><jsx1:taskMetaData><jsx1:taskId>'''+paTaskId+'''</jsx1:taskId></jsx1:taskMetaData><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken><jsx1:user>intalio\\admin</jsx1:user><jsx1:taskOutput><a0:FormModel xmlns:a0=\"http://www.intalio.com/gi/form.gi\"><result>P1D</result></a0:FormModel></jsx1:taskOutput></jsx1:completeTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page226(self):
    """GET empty.jsp (request 22601)."""
    result = request22601.GET('/ui-fw/script/empty.jsp')

    return result

  def page227(self):
    """POST updates.htm (request 22701)."""
    result = request22701.POST('/ui-fw/updates.htm',
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
    # 28 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # 'http://titan:8080/gi/apppath/ScheduleAct...'
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page228(self):
    """POST proxy.jsp (request 22801)."""
    result = request22801.POST('/ui-fw/script/proxy.jsp',
      '<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\"><soapenv:Body><getAssignedRoles xmlns=\"http://tempo.intalio.org/security/RBACQueryService/\"><user>intalio\\\\admin</user></getAssignedRoles></soapenv:Body></soapenv:Envelope>',
      ( NVPair('Content-Type', 'text/xml; charset=\"utf-8\"'), ))

    return result

  def page229(self):
    """POST proxy.jsp (request 22901)."""
    result = request22901.POST('/ui-fw/script/proxy.jsp',
      '<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\"><soapenv:Body><getAssignedUsers xmlns=\"http://tempo.intalio.org/security/RBACQueryService/\"><role>intalio\\\\WorkflowAdministrator</role></getAssignedUsers></soapenv:Body></soapenv:Envelope>',
      ( NVPair('Content-Type', 'text/xml; charset=\"utf-8\"'), ))

    return result

  def page230(self):
    """POST proxy.jsp (request 23001)."""
    result = request23001.POST('/ui-fw/script/proxy.jsp',
      '<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\"><soapenv:Body><reassign xmlns=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><taskId>11d1def534ea1be0:-22d659cb:13b835e25e8:-12ac127.0.0.169</taskId><userOwner></userOwner><roleOwner>intalio\\\\WorkflowAdministrator</roleOwner><taskState>READY</taskState><participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</participantToken><userAction>REASSIGN</userAction></reassign></soapenv:Body></soapenv:Envelope>',
      ( NVPair('Content-Type', 'text/xml; charset=\"utf-8\"'), ))

    return result

  def page231(self):
    """POST updates.htm (request 23101)."""
    result = request23101.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 30 different values for token_id found in response; the first matched
    # the last known value of token_id - don't update the variable.
    # 27 different values for token_url found in response; the first matched
    # the last known value of token_url - don't update the variable.
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page232(self):
    """GET ServerLaunch.html (request 23201)."""
    result = request23201.GET('/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/ServerLaunch.html' +
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

  def page233(self):
    """GET config.xml (requests 23301-23302)."""
    result = request23301.GET('/gi/apppath/ScheduleActionPA/form.gi/config.xml')

    grinder.sleep(84)
    request23302.GET('/gi/apppath/ScheduleActionPA/form.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://titan:8080/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/ServerLaunch.html?id=11d1def534ea1be0:-22d659cb:13b835e25e8:-12ac127.0.0.169&type=PATask&url=http%3A%2F%2Ftitan%3A8080%2Fgi%2Fapppath%2FScheduleActionPA%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page234(self):
    """GET appCanvas.xml (request 23401)."""
    result = request23401.GET('/gi/apppath/ScheduleActionPA/form.gi/components/appCanvas.xml')

    return result

  def page235(self):
    """GET translations.xml (requests 23501-23506)."""
    result = request23501.GET('/gi/apppath/ScheduleActionPA/form.gi/jss/translations.xml')

    grinder.sleep(106)
    request23502.GET('/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/Packages.js')

    grinder.sleep(71)
    request23503.GET('/gi/apppath/ScheduleActionPA/form.gi/js/logic.js')

    grinder.sleep(124)
    request23504.GET('/gi/apppath/ScheduleActionPA/form.gi/images/attachments.gif')

    request23505.GET('/gi/apppath/ScheduleActionPA/form.gi/images/close.png')

    request23506.GET('/gi/apppath/ScheduleActionPA/form.gi/images/error.gif')

    return result

  def page236(self):
    """GET TaskManagementServicesMapping.xml (request 23601)."""
    result = request23601.GET('/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page237(self):
    """GET Tidy.xsl (request 23701)."""
    result = request23701.GET('/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/Tidy.xsl')

    return result

  def page238(self):
    """POST validation (request 23801)."""
    paTaskId=""
    size=0
    grinder.logger.info("page 23801 randomUser ==>") 
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pa pa on task.id=pa.id where pa.state = \'0\' and form_url like \'%ScheduleActionPA%\' order by creation_date desc'
    i=1
    while (size==0):
            if(i>10):
                break
            dbConn = getConnection()
            stmt = dbConn.createStatement()
            rs = stmt.executeQuery(query)
            size =0
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("i ==>" + str(i))
            grinder.logger.info("size ==>" + str(size))
            grinder.sleep(1000*i)
            i=i+1 
            if (size>0):         
                paTaskId = rs.getString(1)
                grinder.logger.info("get PA Task Operation")
                grinder.logger.info("PA Task Id ==>" + paTaskId)

            ensureClosed(stmt)
            ensureClosed(dbConn)
    result = request23801.POST('/gi/validation',
      ( NVPair('assembly', 'ScheduleActionPA'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>'''+paTaskId+'''</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page239(self):
    """GET FormModelMapping.xml (request 23901)."""
    result = request23901.GET('/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page240(self):
    """GET TaskManagerProcessMapping.xml (request 24001)."""
    result = request24001.GET('/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/TaskManagerProcessMapping.xml')

    return result

  def page241(self):
    """GET FormModelMapping.xml (request 24101)."""
    result = request24101.GET('/gi/apppath/ScheduleActionPA/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page242(self):
    """POST validation (request 24201)."""
    paTaskId=""
    size=0
    query = 'select distinct task.taskid from tempo_task task INNER JOIN tempo_pa pa on task.id=pa.id where pa.state = \'0\' and form_url like \'%ScheduleActionPA%\' order by creation_date desc'  
    i=1
    while (size==0):
            if(i>10):
                break
            dbConn = getConnection()
            stmt = dbConn.createStatement()
            rs = stmt.executeQuery(query)
            size =0
            rs.beforeFirst()
            rs.last()
            size = rs.getRow()
            grinder.logger.info("i ==>" + str(i))
            grinder.logger.info("size ==>" + str(size))
            grinder.sleep(1000*i)
            i=i+1 
            if (size>0):         
                paTaskId = rs.getString(1)
                grinder.logger.info("get PA Task Operation")
                grinder.logger.info("PA Task Id ==>" + paTaskId)

            ensureClosed(stmt)
            ensureClosed(dbConn)
    result = request24201.POST('/gi/validation',
      ( NVPair('assembly', 'ScheduleActionPA'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:completeTaskRequest xmlns:jsx1=\"http://www.intalio.com/bpms/workflow/ib4p_20051115\"><jsx1:taskMetaData><jsx1:taskId>'''+paTaskId+'''</jsx1:taskId></jsx1:taskMetaData><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTE0MDM2NjcxNyYmaXNXb3JrZmxvd0FkbWluPT1mYWxzZSYmcm9sZXM9PWV4YW1wbGVzXG1hbmFnZXIsaW50YWxpb1xQcm9jZXNzTWFuYWdlcixleGFtcGxlc1xlbXBsb3llZSxpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZuYW1lPT1BZG1pbmluaXN0cmF0b3ImJmVtYWlsPT1hZG1pbkBleGFtcGxlLmNvbSYmYXNzaWduUm9sZT09aW50YWxpb1xQcm9jZXNzQWRtaW5pc3RyYXRvcixleGFtcGxlc1xtYW5hZ2VyLGludGFsaW9cV29ya2Zsb3dBZG1pbmlzdHJhdG9yJiZub25jZT09Nzk5NjI4MzgxNDI5NDc1MzU1OCYmdGltZXN0YW1wPT0xMzU1MTQwMzY2NzE3JiZkaWdlc3Q9PWtLeGQxeEthM0xHUVN4NExVVGhWcXVnV0VGcz0mJiYmVE9LRU4=</jsx1:participantToken><jsx1:user>intalio\\admin</jsx1:user><jsx1:taskOutput><a0:FormModel xmlns:a0=\"http://www.intalio.com/gi/form.gi\"/></jsx1:taskOutput></jsx1:completeTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page243(self):
    """GET empty.jsp (request 24301)."""
    result = request24301.GET('/ui-fw/script/empty.jsp')

    return result

  def page244(self):
    """POST updates.htm (request 24401)."""
    result = request24401.POST('/ui-fw/updates.htm',
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

  def page245(self):
    """GET act (request 24501)."""
    result = request24501.GET('/xFormsManager/act' +
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
    self.token_staticstate = \
      httpUtilities.valueFromHiddenInput('$static-state') # 'pers:5052A299-402B-2E64-0E3F-3D20DB2B93B...'
    self.token_dynamicstate = \
      httpUtilities.valueFromHiddenInput('$dynamic-state') # 'pers:762F2406-69F6-7F28-A6DB-A6460071D62...'
    self.token_serverevents = \
      httpUtilities.valueFromHiddenInput('$server-events') # ''
    self.token_clientstate = \
      httpUtilities.valueFromHiddenInput('$client-state') # ''

    return result

  def page246(self):
    """POST xforms-server (request 24601)."""
    result = request24601.POST('/xFormsManager/xforms-server',
      '''<!DOCTYPE xxforms:event-request [<!ENTITY nbsp \"&#160;\">]>\n<xxforms:event-request xmlns:xxforms=\"http://orbeon.org/oxf/xml/xforms\">\n    <xxforms:static-state>pers:5052A299-402B-2E64-0E3F-3D20DB2B93BE</xxforms:static-state>\n    <xxforms:dynamic-state>pers:762F2406-69F6-7F28-A6DB-A6460071D62A</xxforms:dynamic-state>\n    <xxforms:action>\n        <xxforms:event name=\"DOMFocusIn\" source-control-id=\"xf-117\"></xxforms:event>\n        <xxforms:event name=\"xxforms-value-change-with-focus-change\" source-control-id=\"xf-117\">RF3uMliN1+I=</xxforms:event>\n    </xxforms:action>\n</xxforms:event-request>''',
      ( NVPair('Content-Type', 'application/xml; charset=UTF-8'), ))

    return result

  def page247(self):
    """POST xforms-server (request 24701)."""
    result = request24701.POST('/xFormsManager/xforms-server',
      '''<!DOCTYPE xxforms:event-request [<!ENTITY nbsp \"&#160;\">]>\n<xxforms:event-request xmlns:xxforms=\"http://orbeon.org/oxf/xml/xforms\">\n    <xxforms:static-state>pers:5052A299-402B-2E64-0E3F-3D20DB2B93BE</xxforms:static-state>\n    <xxforms:dynamic-state>pers:E5A83A10-8AF7-DC37-3075-696270AF27E8</xxforms:dynamic-state>\n    <xxforms:action>\n        <xxforms:event name=\"DOMFocusOut\" source-control-id=\"xf-117\"></xxforms:event>\n        <xxforms:event name=\"DOMFocusIn\" source-control-id=\"xf-130\"></xxforms:event>\n        <xxforms:event name=\"DOMActivate\" source-control-id=\"xf-130\"></xxforms:event>\n    </xxforms:action>\n</xxforms:event-request>''',
      ( NVPair('Content-Type', 'application/xml; charset=UTF-8'), ))

    return result

  def page248(self):
    """POST act (request 24801)."""
    self.token_dynamicstate = \
      'pers:5F723CD4-CEB1-CBB0-E592-A1C0457A2FC8'
    self.token_serverevents = \
      'X2ztnLbujs+XocNBu3ADXGPbA4oARPCjKA/bMdupU+9QdKsWPJocVTQ9hmj60pCxqi7t4upRjq/RJVuX1+0Qk773leOwpK94KO7as00PXCMEcM5UU3/3LWmQbifCquY/BmhwBhBp/kRgUHtzCOgRwBlnhob7HQbJs5VwX+FFv9ZUF6FH5cQzzw1SxULxggrFIjhsYzwWZki2k7U/PMrDNFWsqZObJw5R4fJmXs2P/uM0u4CkZbCw7rexZJXh3jJc/dM1xus1bnrxA='
    self.token_clientstate = \
      'initial-dynamic-state&pers%3A762F2406-69F6-7F28-A6DB-A6460071D62A&load-did-run&true'
    result = request24801.POST('/xFormsManager/act' +
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
      self.token_claimTaskOnOpen,
      ( NVPair('$static-state', self.token_staticstate),
        NVPair('$dynamic-state', self.token_dynamicstate),
        NVPair('$server-events', self.token_serverevents),
        NVPair('$client-state', self.token_clientstate),
        NVPair('$repeat-tree', self.token_repeattree),
        NVPair('$repeat-indexes', self.token_repeatindexes),
        NVPair('xf-79', 'LzQCBxo8rXo='),
        NVPair('new-attachment-title$xforms-input-1', ''),
        NVPair('new-attachment-file', ''),
        NVPair('new-attachment-text', ''),
        NVPair('xf-113$xforms-input-1', 'Emily Williams'),
        NVPair('xf-114$xforms-input-1', '+1(650)596-1800'),
        NVPair('xf-115$xforms-input-1', 'ewilliams@examples.intalio.com'),
        NVPair('xf-117', 'RF3uMliN1+I='),
        NVPair('xf-125', ''), ),
      ( NVPair('Content-Type', 'multipart/form-data; boundary=---------------------------205095582013032770001602312470'), ),
      True)

    return result

  def page249(self):
    """GET tasks.htm (request 24901)."""
    result = request24901.GET('/ui-fw/tasks.htm')

    return result

  def page250(self):
    """GET empty.jsp (request 25001)."""
    result = request25001.GET('/ui-fw/script/empty.jsp')

    return result

  def page251(self):
    """POST vacation.htm (request 25101)."""
    result = request25101.POST('/ui-fw/vacation.htm',
      ( NVPair('action', 'Validate'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page252(self):
    """POST updates.htm (request 25201)."""
    result = request25201.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 25 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '11d1def534ea1be0:-22d659cb:13b835e25e8:-...'
    # 22 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/RepeatEvery_PXEI_897/Forms/P...'
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page253(self):
    """POST updates.htm (request 25301)."""
    result = request25301.POST('/ui-fw/updates.htm',
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
      httpUtilities.valueFromBodyURI('id') # 'notify-A6S1-1BW6-SCAX-5FSH'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'Notification'
    # 27 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # 'oxf://AbsenceRequest/Notification.xform'
    # 2 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page254(self):
    """POST updates.htm (request 25401)."""
    result = request25401.POST('/ui-fw/updates.htm',
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

  def page255(self):
    """GET empty.jsp (request 25501)."""
    result = request25501.GET('/ui-fw/script/empty.jsp')

    return result

  def page256(self):
    """POST updates.htm (request 25601)."""
    result = request25601.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 25 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '11d1def534ea1be0:-22d659cb:13b835e25e8:-...'
    self.token_type = \
      httpUtilities.valueFromBodyURI('type') # 'PATask'
    # 22 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/RepeatEvery_PXEI_897/Forms/P...'
    # 3 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page257(self):
    """POST login.htm (requests 25701-25702)."""
    self.token_actionName = \
      'logOut'
    
    # Expecting 302 'Moved Temporarily'
    result = request25701.POST('/ui-fw/login.htm',
      ( NVPair('actionName', self.token_actionName),
        NVPair('formURL', self.token_formURL),
        NVPair('taskType', self.token_taskType),
        NVPair('isViewTask', self.token_isViewTask),
        NVPair('searchUser', self.token_searchUser),
        NVPair('currTab', self.token_currTab), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))
    self.token_prevAction = \
      httpUtilities.valueFromLocationURI('prevAction') # '/ui-fw'

    request25702.GET('/login.htm' +
      '?prevAction=' +
      self.token_prevAction)
    self.token_actionName = \
      httpUtilities.valueFromHiddenInput('actionName') # 'logIn'

    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    self.page1()      # GET / (requests 101-139)

    grinder.sleep(162)
    self.page2()      # GET data.json (requests 201-205)
    self.page3()      # GET templates.html (requests 301-302)
    self.page4()      # GET dsState.json (requests 401-402)

    grinder.sleep(126)
    self.page5()      # GET task_summary.jsp (request 501)
    self.page6()      # GET user_task_count.jsp (request 601)
    self.page7()      # GET notifications.jsp (request 701)
    self.page8()      # GET instance_status_cnt.jsp (request 801)
    self.page9()      # GET ws_response_time.jsp (request 901)
    self.page10()     # GET avg_completion_time.jsp (request 1001)
    self.page11()     # GET vacation_summary.jsp (requests 1101-1103)

    grinder.sleep(82)
    self.page12()     # GET notifications.jsp (request 1201)
    self.page13()     # GET vacation_summary.jsp (request 1301)
    self.page14()     # GET task_summary.jsp (requests 1401-1402)
    self.page15()     # GET user_task_count.jsp (request 1501)
    self.page16()     # GET avg_completion_time.jsp (request 1601)

    grinder.sleep(484)
    self.page17()     # GET instance_status_cnt.jsp (request 1701)
    self.page18()     # GET ws_response_time.jsp (requests 1801-1803)

    grinder.sleep(959)
    self.page19()     # POST login.htm (request 1901)

    grinder.sleep(1501)
    self.page20()     # POST login.htm (requests 2001-2002)

    grinder.sleep(211)
    self.page21()     # GET data.json (request 2101)

    grinder.sleep(48)
    self.page22()     # GET dsState.json (request 2201)

    grinder.sleep(113)
    self.page23()     # GET vacation_summary.jsp (request 2301)
    self.page24()     # GET instance_status_cnt.jsp (request 2401)
    self.page25()     # GET notifications.jsp (request 2501)
    self.page26()     # GET user_task_count.jsp (request 2601)
    self.page27()     # GET task_summary.jsp (request 2701)
    self.page28()     # GET avg_completion_time.jsp (request 2801)
    self.page29()     # GET ws_response_time.jsp (request 2901)

    grinder.sleep(139)
    self.page30()     # GET user_task_count.jsp (request 3001)
    self.page31()     # GET notifications.jsp (request 3101)
    self.page32()     # GET vacation_summary.jsp (request 3201)
    self.page33()     # GET task_summary.jsp (request 3301)

    grinder.sleep(39)
    self.page34()     # GET avg_completion_time.jsp (request 3401)
    self.page35()     # GET instance_status_cnt.jsp (request 3501)

    grinder.sleep(394)
    self.page36()     # GET ws_response_time.jsp (request 3601)

    grinder.sleep(2039)
    self.page37()     # GET tasks.htm (requests 3701-3703)

    grinder.sleep(112)
    self.page38()     # GET empty.jsp (request 3801)

    grinder.sleep(19)
    self.page39()     # POST vacation.htm (request 3901)

    grinder.sleep(104)
    self.page40()     # POST updates.htm (request 4001)
    self.page41()     # POST updates.htm (request 4101)

    grinder.sleep(29)
    self.page42()     # POST updates.htm (request 4201)

    grinder.sleep(293)
    self.page43()     # GET empty.jsp (request 4301)

    grinder.sleep(143)
    self.page44()     # POST updates.htm (request 4401)

    grinder.sleep(836)
    self.page45()     # POST updates.htm (request 4501)

    grinder.sleep(4522)
    self.page46()     # GET ServerLaunch.html (request 4601)

    grinder.sleep(108)
    self.page47()     # GET config.xml (requests 4701-4702)
    self.page48()     # GET appCanvas.xml (request 4801)
    self.page49()     # GET translations.xml (requests 4901-4906)
    self.page50()     # GET TaskManagementServicesMapping.xml (request 5001)

    grinder.sleep(65)
    self.page51()     # GET Tidy.xsl (request 5101)
    #self.page52()     # POST validation (request 5201)

    grinder.sleep(32755)
    self.page53()     # GET TaskManagementServicesMapping.xml (request 5301)

    grinder.sleep(23)
    self.page54()     # GET FormModelMapping.xml (request 5401)

    grinder.sleep(12)
    #self.page55()     # POST validation (request 5501)

    grinder.sleep(13)
    self.page56()     # GET empty.jsp (request 5601)

    grinder.sleep(32)
    self.page57()     # POST updates.htm (request 5701)

    grinder.sleep(4472)
    self.page58()     # GET ServerLaunch.html (request 5801)

    grinder.sleep(105)
    self.page59()     # GET config.xml (requests 5901-5902)
    self.page60()     # GET translations.xml (request 6001)
    self.page61()     # GET appCanvas.xml (requests 6101-6106)
    self.page62()     # GET TaskManagementServicesMapping.xml (request 6201)

    grinder.sleep(63)
    self.page63()     # GET Tidy.xsl (request 6301)
    #self.page64()     # POST validation (request 6401)

    grinder.sleep(13373)
    self.page65()     # GET TaskManagementServicesMapping.xml (request 6501)

    grinder.sleep(64)
    self.page66()     # GET FormModelMapping.xml (request 6601)

    grinder.sleep(53)
    #self.page67()     # POST validation (request 6701)

    grinder.sleep(17)
    self.page68()     # GET empty.jsp (request 6801)

    grinder.sleep(38)
    self.page69()     # POST updates.htm (request 6901)

    grinder.sleep(4517)
    self.page70()     # GET init (request 7001)

    grinder.sleep(1851)
    self.page71()     # POST xforms-server (request 7101)

    grinder.sleep(15460)
    self.page72()     # POST xforms-server (request 7201)

    grinder.sleep(47)
    self.page73()     # POST init (request 7301)

    grinder.sleep(37)
    self.page74()     # GET tasks.htm (request 7401)

    grinder.sleep(144)
    self.page75()     # GET empty.jsp (request 7501)

    grinder.sleep(26)
    self.page76()     # POST vacation.htm (request 7601)

    grinder.sleep(103)
    self.page77()     # POST updates.htm (request 7701)
    self.page78()     # POST updates.htm (request 7801)
    self.page79()     # POST updates.htm (request 7901)

    grinder.sleep(151)
    self.page80()     # GET empty.jsp (request 8001)

    grinder.sleep(177)
    self.page81()     # POST updates.htm (request 8101)

    grinder.sleep(1869)
    self.page82()     # POST updates.htm (request 8201)

    grinder.sleep(1081)
    self.page83()     # GET ServerLaunch.html (request 8301)

    grinder.sleep(100)
    self.page84()     # GET config.xml (requests 8401-8402)
    self.page85()     # GET translations.xml (request 8501)
    self.page86()     # GET appCanvas.xml (requests 8601-8626)
    self.page87()     # GET TaskManagementServicesMapping.xml (requests 8701-8702)

    grinder.sleep(51)
    self.page88()     # GET Tidy.xsl (request 8801)
    self.page89()     # POST validation (requests 8901-8903)

    grinder.sleep(4376)
    self.page90()     # POST updates.htm (request 9001)

    grinder.sleep(89)
    self.page91()     # GET empty.jsp (request 9101)

    grinder.sleep(280)
    self.page92()     # POST updates.htm (request 9201)

    grinder.sleep(1450)
    self.page93()     # GET ServerLaunch.html (request 9301)

    grinder.sleep(111)
    self.page94()     # GET config.xml (requests 9401-9402)
    self.page95()     # GET translations.xml (request 9501)
    self.page96()     # GET appCanvas.xml (requests 9601-9606)
    self.page97()     # GET TaskManagementServicesMapping.xml (request 9701)

    grinder.sleep(67)
    self.page98()     # GET Tidy.xsl (request 9801)
    self.page99()     # POST validation (request 9901)

    grinder.sleep(28063)
    self.page100()    # GET TaskManagementServicesMapping.xml (request 10001)

    grinder.sleep(60)
    self.page101()    # GET FormModelMapping.xml (request 10101)

    grinder.sleep(17)
    self.page102()    # POST validation (request 10201)

    grinder.sleep(18)
    self.page103()    # GET empty.jsp (request 10301)

    grinder.sleep(28)
    self.page104()    # POST updates.htm (request 10401)

    grinder.sleep(2225)
    self.page105()    # GET ServerLaunch.html (request 10501)

    grinder.sleep(98)
    self.page106()    # GET config.xml (requests 10601-10602)
    self.page107()    # GET translations.xml (request 10701)
    self.page108()    # GET appCanvas.xml (requests 10801-10806)
    self.page109()    # GET TaskManagementServicesMapping.xml (request 10901)

    grinder.sleep(65)
    self.page110()    # GET Tidy.xsl (request 11001)
    self.page111()    # POST validation (request 11101)

    grinder.sleep(17646)
    self.page112()    # GET TaskManagementServicesMapping.xml (request 11201)

    grinder.sleep(63)
    self.page113()    # GET FormModelMapping.xml (request 11301)

    grinder.sleep(11)
    self.page114()    # POST validation (request 11401)
    self.page115()    # GET empty.jsp (request 11501)

    grinder.sleep(31)
    self.page116()    # POST updates.htm (request 11601)

    grinder.sleep(4704)
    self.page117()    # GET ServerLaunch.html (request 11701)

    grinder.sleep(108)
    self.page118()    # GET config.xml (requests 11801-11802)
    self.page119()    # GET appCanvas.xml (request 11901)
    self.page120()    # GET translations.xml (requests 12001-12005)
    self.page121()    # GET TaskManagementServicesMapping.xml (request 12101)

    grinder.sleep(62)
    self.page122()    # GET Tidy.xsl (request 12201)
    self.page123()    # POST validation (request 12301)

    grinder.sleep(15513)
    self.page124()    # GET TaskManagementServicesMapping.xml (request 12401)

    grinder.sleep(61)
    self.page125()    # GET FormModelMapping.xml (request 12501)

    grinder.sleep(12)
    self.page126()    # POST validation (request 12601)
    self.page127()    # GET empty.jsp (request 12701)

    grinder.sleep(30)
    self.page128()    # POST updates.htm (request 12801)

    grinder.sleep(2250)
    self.page129()    # GET ServerLaunch.html (request 12901)

    grinder.sleep(106)
    self.page130()    # GET config.xml (request 13001)
    self.page131()    # GET translations.xml (requests 13101-13102)
    self.page132()    # GET appCanvas.xml (requests 13201-13206)
    self.page133()    # GET TaskManagementServicesMapping.xml (request 13301)

    grinder.sleep(56)
    self.page134()    # GET Tidy.xsl (request 13401)
    self.page135()    # POST validation (request 13501)

    grinder.sleep(23907)
    self.page136()    # POST updates.htm (request 13601)

    grinder.sleep(2545)
    self.page137()    # GET ServerLaunch.html (request 13701)

    grinder.sleep(118)
    self.page138()    # GET config.xml (requests 13801-13802)
    self.page139()    # GET appCanvas.xml (request 13901)
    self.page140()    # GET translations.xml (requests 14001-14006)
    self.page141()    # GET TaskManagementServicesMapping.xml (request 14101)

    grinder.sleep(59)
    self.page142()    # GET Tidy.xsl (request 14201)
    self.page143()    # POST validation (request 14301)

    grinder.sleep(3660)
    self.page144()    # POST updates.htm (request 14401)

    grinder.sleep(1745)
    self.page145()    # GET ServerLaunch.html (request 14501)

    grinder.sleep(113)
    self.page146()    # GET config.xml (request 14601)

    grinder.sleep(50)
    self.page147()    # GET translations.xml (requests 14701-14702)
    self.page148()    # GET appCanvas.xml (requests 14801-14806)

    grinder.sleep(11)
    self.page149()    # GET TaskManagementServicesMapping.xml (request 14901)

    grinder.sleep(63)
    self.page150()    # GET Tidy.xsl (request 15001)
    self.page151()    # POST validation (request 15101)

    grinder.sleep(28948)
    self.page152()    # POST updates.htm (request 15201)

    grinder.sleep(11)
    self.page153()    # GET empty.jsp (request 15301)

    grinder.sleep(208)
    self.page154()    # POST updates.htm (request 15401)

    grinder.sleep(1344)
    self.page155()    # GET ServerLaunch.html (request 15501)

    grinder.sleep(105)
    self.page156()    # GET config.xml (request 15601)

    grinder.sleep(74)
    self.page157()    # GET translations.xml (requests 15701-15702)

    grinder.sleep(12)
    self.page158()    # GET appCanvas.xml (requests 15801-15806)
    self.page159()    # GET TaskManagementServicesMapping.xml (request 15901)

    grinder.sleep(61)
    self.page160()    # GET Tidy.xsl (request 16001)
    #self.page161()    # POST validation (request 16101)

    grinder.sleep(2276)
    self.page162()    # POST updates.htm (request 16201)
    self.page163()    # GET empty.jsp (request 16301)

    grinder.sleep(185)
    self.page164()    # POST updates.htm (request 16401)

    grinder.sleep(1041)
    self.page165()    # GET ServerLaunch.html (request 16501)

    grinder.sleep(98)
    self.page166()    # GET config.xml (requests 16601-16602)
    self.page167()    # GET appCanvas.xml (requests 16701-16706)
    self.page168()    # GET TaskManagementServicesMapping.xml (request 16801)

    grinder.sleep(65)
    self.page169()    # GET Tidy.xsl (request 16901)
    self.page170()    # POST validation (request 17001)

    grinder.sleep(1085)
    self.page171()    # POST updates.htm (request 17101)
    self.page172()    # GET empty.jsp (request 17201)

    grinder.sleep(162)
    self.page173()    # POST updates.htm (request 17301)

    grinder.sleep(801)
    self.page174()    # GET init (request 17401)

    grinder.sleep(15518)
    self.page175()    # POST xforms-server (request 17501)

    grinder.sleep(1043)
    self.page176()    # POST xforms-server (request 17601)

    grinder.sleep(224)
    self.page177()    # POST init (request 17701)

    grinder.sleep(34)
    self.page178()    # GET tasks.htm (request 17801)

    grinder.sleep(112)
    self.page179()    # GET empty.jsp (request 17901)

    grinder.sleep(22)
    self.page180()    # POST vacation.htm (request 18001)

    grinder.sleep(103)
    self.page181()    # POST updates.htm (request 18101)
    self.page182()    # POST updates.htm (request 18201)

    grinder.sleep(27)
    self.page183()    # POST updates.htm (request 18301)

    grinder.sleep(273)
    self.page184()    # GET empty.jsp (request 18401)

    grinder.sleep(103)
    self.page185()    # POST updates.htm (request 18501)

    grinder.sleep(5412)
    self.page186()    # GET act (requests 18601-18603)

    grinder.sleep(12731)
    self.page187()    # POST xforms-server (request 18701)

    grinder.sleep(3908)
    self.page188()    # POST xforms-server (request 18801)

    grinder.sleep(63)
    self.page189()    # POST act (request 18901)

    grinder.sleep(32)
    self.page190()    # GET tasks.htm (request 19001)

    grinder.sleep(108)
    self.page191()    # GET empty.jsp (request 19101)

    grinder.sleep(22)
    self.page192()    # POST vacation.htm (request 19201)

    grinder.sleep(101)
    self.page193()    # POST updates.htm (request 19301)
    self.page194()    # POST updates.htm (request 19401)

    grinder.sleep(34)
    self.page195()    # POST updates.htm (request 19501)

    grinder.sleep(224)
    self.page196()    # GET empty.jsp (request 19601)

    grinder.sleep(135)
    self.page197()    # POST updates.htm (request 19701)

    grinder.sleep(10398)
    self.page198()    # GET ServerLaunch.html (request 19801)

    grinder.sleep(110)
    self.page199()    # GET config.xml (requests 19901-19902)
    self.page200()    # GET appCanvas.xml (request 20001)
    self.page201()    # GET translations.xml (requests 20101-20105)
    self.page202()    # GET TaskManagementServicesMapping.xml (request 20201)

    grinder.sleep(67)
    self.page203()    # GET Tidy.xsl (request 20301)
    self.page204()    # POST validation (request 20401)
    self.page205()    # GET FormModelMapping.xml (request 20501)

    grinder.sleep(1203)
    self.page206()    # GET TaskManagerProcessMapping.xml (request 20601)

    grinder.sleep(64)
    self.page207()    # GET FormModelMapping.xml (request 20701)
    self.page208()    # POST validation (request 20801)

    grinder.sleep(13)
    self.page209()    # GET empty.jsp (request 20901)

    grinder.sleep(46)
    self.page210()    # POST updates.htm (request 21001)

    grinder.sleep(17278)
    self.page211()    # POST proxy.jsp (request 21101)

    grinder.sleep(2317)
    self.page212()    # POST proxy.jsp (request 21201)

    grinder.sleep(966)
    self.page213()    # POST proxy.jsp (request 21301)

    grinder.sleep(2170)
    self.page214()    # POST updates.htm (request 21401)

    grinder.sleep(1399)
    self.page215()    # GET ServerLaunch.html (request 21501)

    grinder.sleep(100)
    self.page216()    # GET config.xml (requests 21601-21602)
    self.page217()    # GET appCanvas.xml (request 21701)
    self.page218()    # GET translations.xml (requests 21801-21806)
    self.page219()    # GET TaskManagementServicesMapping.xml (request 21901)

    grinder.sleep(62)
    self.page220()    # GET Tidy.xsl (request 22001)
    self.page221()    # POST validation (request 22101)
    self.page222()    # GET FormModelMapping.xml (request 22201)

    grinder.sleep(1564)
    self.page223()    # GET TaskManagerProcessMapping.xml (request 22301)

    grinder.sleep(37)
    self.page224()    # GET FormModelMapping.xml (request 22401)

    grinder.sleep(48)
    self.page225()    # POST validation (request 22501)
    self.page226()    # GET empty.jsp (request 22601)

    grinder.sleep(33)
    self.page227()    # POST updates.htm (request 22701)

    grinder.sleep(19013)
    self.page228()    # POST proxy.jsp (request 22801)

    grinder.sleep(1907)
    self.page229()    # POST proxy.jsp (request 22901)

    grinder.sleep(757)
    self.page230()    # POST proxy.jsp (request 23001)

    grinder.sleep(2207)
    self.page231()    # POST updates.htm (request 23101)

    grinder.sleep(2680)
    self.page232()    # GET ServerLaunch.html (request 23201)

    grinder.sleep(115)
    self.page233()    # GET config.xml (requests 23301-23302)
    self.page234()    # GET appCanvas.xml (request 23401)
    self.page235()    # GET translations.xml (requests 23501-23506)
    self.page236()    # GET TaskManagementServicesMapping.xml (request 23601)

    grinder.sleep(63)
    self.page237()    # GET Tidy.xsl (request 23701)
    self.page238()    # POST validation (request 23801)

    grinder.sleep(11)
    self.page239()    # GET FormModelMapping.xml (request 23901)

    grinder.sleep(2088)
    self.page240()    # GET TaskManagerProcessMapping.xml (request 24001)

    grinder.sleep(33)
    self.page241()    # GET FormModelMapping.xml (request 24101)

    grinder.sleep(47)
    self.page242()    # POST validation (request 24201)

    grinder.sleep(12)
    self.page243()    # GET empty.jsp (request 24301)

    grinder.sleep(36)
    self.page244()    # POST updates.htm (request 24401)

    grinder.sleep(21218)
    self.page245()    # GET act (request 24501)

    grinder.sleep(2802)
    self.page246()    # POST xforms-server (request 24601)

    grinder.sleep(579)
    self.page247()    # POST xforms-server (request 24701)

    grinder.sleep(59)
    self.page248()    # POST act (request 24801)

    grinder.sleep(27)
    self.page249()    # GET tasks.htm (request 24901)

    grinder.sleep(109)
    self.page250()    # GET empty.jsp (request 25001)

    grinder.sleep(21)
    self.page251()    # POST vacation.htm (request 25101)

    grinder.sleep(103)
    self.page252()    # POST updates.htm (request 25201)
    self.page253()    # POST updates.htm (request 25301)
    self.page254()    # POST updates.htm (request 25401)

    grinder.sleep(187)
    self.page255()    # GET empty.jsp (request 25501)

    grinder.sleep(130)
    self.page256()    # POST updates.htm (request 25601)

    grinder.sleep(9962)
    self.page257()    # POST login.htm (requests 25701-25702)

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
instrumentMethod(Test(6600, 'Page 66'), 'page66')
instrumentMethod(Test(6700, 'Page 67'), 'page67')
instrumentMethod(Test(6800, 'Page 68'), 'page68')
instrumentMethod(Test(6900, 'Page 69'), 'page69')
instrumentMethod(Test(7000, 'Page 70'), 'page70')
instrumentMethod(Test(7100, 'Page 71'), 'page71')
instrumentMethod(Test(7200, 'Page 72'), 'page72')
instrumentMethod(Test(7300, 'Page 73'), 'page73')
instrumentMethod(Test(7400, 'Page 74'), 'page74')
instrumentMethod(Test(7500, 'Page 75'), 'page75')
instrumentMethod(Test(7600, 'Page 76'), 'page76')
instrumentMethod(Test(7700, 'Page 77'), 'page77')
instrumentMethod(Test(7800, 'Page 78'), 'page78')
instrumentMethod(Test(7900, 'Page 79'), 'page79')
instrumentMethod(Test(8000, 'Page 80'), 'page80')
instrumentMethod(Test(8100, 'Page 81'), 'page81')
instrumentMethod(Test(8200, 'Page 82'), 'page82')
instrumentMethod(Test(8300, 'Page 83'), 'page83')
instrumentMethod(Test(8400, 'Page 84'), 'page84')
instrumentMethod(Test(8500, 'Page 85'), 'page85')
instrumentMethod(Test(8600, 'Page 86'), 'page86')
instrumentMethod(Test(8700, 'Page 87'), 'page87')
instrumentMethod(Test(8800, 'Page 88'), 'page88')
instrumentMethod(Test(8900, 'Page 89'), 'page89')
instrumentMethod(Test(9000, 'Page 90'), 'page90')
instrumentMethod(Test(9100, 'Page 91'), 'page91')
instrumentMethod(Test(9200, 'Page 92'), 'page92')
instrumentMethod(Test(9300, 'Page 93'), 'page93')
instrumentMethod(Test(9400, 'Page 94'), 'page94')
instrumentMethod(Test(9500, 'Page 95'), 'page95')
instrumentMethod(Test(9600, 'Page 96'), 'page96')
instrumentMethod(Test(9700, 'Page 97'), 'page97')
instrumentMethod(Test(9800, 'Page 98'), 'page98')
instrumentMethod(Test(9900, 'Page 99'), 'page99')
instrumentMethod(Test(10000, 'Page 100'), 'page100')
instrumentMethod(Test(10100, 'Page 101'), 'page101')
instrumentMethod(Test(10200, 'Page 102'), 'page102')
instrumentMethod(Test(10300, 'Page 103'), 'page103')
instrumentMethod(Test(10400, 'Page 104'), 'page104')
instrumentMethod(Test(10500, 'Page 105'), 'page105')
instrumentMethod(Test(10600, 'Page 106'), 'page106')
instrumentMethod(Test(10700, 'Page 107'), 'page107')
instrumentMethod(Test(10800, 'Page 108'), 'page108')
instrumentMethod(Test(10900, 'Page 109'), 'page109')
instrumentMethod(Test(11000, 'Page 110'), 'page110')
instrumentMethod(Test(11100, 'Page 111'), 'page111')
instrumentMethod(Test(11200, 'Page 112'), 'page112')
instrumentMethod(Test(11300, 'Page 113'), 'page113')
instrumentMethod(Test(11400, 'Page 114'), 'page114')
instrumentMethod(Test(11500, 'Page 115'), 'page115')
instrumentMethod(Test(11600, 'Page 116'), 'page116')
instrumentMethod(Test(11700, 'Page 117'), 'page117')
instrumentMethod(Test(11800, 'Page 118'), 'page118')
instrumentMethod(Test(11900, 'Page 119'), 'page119')
instrumentMethod(Test(12000, 'Page 120'), 'page120')
instrumentMethod(Test(12100, 'Page 121'), 'page121')
instrumentMethod(Test(12200, 'Page 122'), 'page122')
instrumentMethod(Test(12300, 'Page 123'), 'page123')
instrumentMethod(Test(12400, 'Page 124'), 'page124')
instrumentMethod(Test(12500, 'Page 125'), 'page125')
instrumentMethod(Test(12600, 'Page 126'), 'page126')
instrumentMethod(Test(12700, 'Page 127'), 'page127')
instrumentMethod(Test(12800, 'Page 128'), 'page128')
instrumentMethod(Test(12900, 'Page 129'), 'page129')
instrumentMethod(Test(13000, 'Page 130'), 'page130')
instrumentMethod(Test(13100, 'Page 131'), 'page131')
instrumentMethod(Test(13200, 'Page 132'), 'page132')
instrumentMethod(Test(13300, 'Page 133'), 'page133')
instrumentMethod(Test(13400, 'Page 134'), 'page134')
instrumentMethod(Test(13500, 'Page 135'), 'page135')
instrumentMethod(Test(13600, 'Page 136'), 'page136')
instrumentMethod(Test(13700, 'Page 137'), 'page137')
instrumentMethod(Test(13800, 'Page 138'), 'page138')
instrumentMethod(Test(13900, 'Page 139'), 'page139')
instrumentMethod(Test(14000, 'Page 140'), 'page140')
instrumentMethod(Test(14100, 'Page 141'), 'page141')
instrumentMethod(Test(14200, 'Page 142'), 'page142')
instrumentMethod(Test(14300, 'Page 143'), 'page143')
instrumentMethod(Test(14400, 'Page 144'), 'page144')
instrumentMethod(Test(14500, 'Page 145'), 'page145')
instrumentMethod(Test(14600, 'Page 146'), 'page146')
instrumentMethod(Test(14700, 'Page 147'), 'page147')
instrumentMethod(Test(14800, 'Page 148'), 'page148')
instrumentMethod(Test(14900, 'Page 149'), 'page149')
instrumentMethod(Test(15000, 'Page 150'), 'page150')
instrumentMethod(Test(15100, 'Page 151'), 'page151')
instrumentMethod(Test(15200, 'Page 152'), 'page152')
instrumentMethod(Test(15300, 'Page 153'), 'page153')
instrumentMethod(Test(15400, 'Page 154'), 'page154')
instrumentMethod(Test(15500, 'Page 155'), 'page155')
instrumentMethod(Test(15600, 'Page 156'), 'page156')
instrumentMethod(Test(15700, 'Page 157'), 'page157')
instrumentMethod(Test(15800, 'Page 158'), 'page158')
instrumentMethod(Test(15900, 'Page 159'), 'page159')
instrumentMethod(Test(16000, 'Page 160'), 'page160')
instrumentMethod(Test(16100, 'Page 161'), 'page161')
instrumentMethod(Test(16200, 'Page 162'), 'page162')
instrumentMethod(Test(16300, 'Page 163'), 'page163')
instrumentMethod(Test(16400, 'Page 164'), 'page164')
instrumentMethod(Test(16500, 'Page 165'), 'page165')
instrumentMethod(Test(16600, 'Page 166'), 'page166')
instrumentMethod(Test(16700, 'Page 167'), 'page167')
instrumentMethod(Test(16800, 'Page 168'), 'page168')
instrumentMethod(Test(16900, 'Page 169'), 'page169')
instrumentMethod(Test(17000, 'Page 170'), 'page170')
instrumentMethod(Test(17100, 'Page 171'), 'page171')
instrumentMethod(Test(17200, 'Page 172'), 'page172')
instrumentMethod(Test(17300, 'Page 173'), 'page173')
instrumentMethod(Test(17400, 'Page 174'), 'page174')
instrumentMethod(Test(17500, 'Page 175'), 'page175')
instrumentMethod(Test(17600, 'Page 176'), 'page176')
instrumentMethod(Test(17700, 'Page 177'), 'page177')
instrumentMethod(Test(17800, 'Page 178'), 'page178')
instrumentMethod(Test(17900, 'Page 179'), 'page179')
instrumentMethod(Test(18000, 'Page 180'), 'page180')
instrumentMethod(Test(18100, 'Page 181'), 'page181')
instrumentMethod(Test(18200, 'Page 182'), 'page182')
instrumentMethod(Test(18300, 'Page 183'), 'page183')
instrumentMethod(Test(18400, 'Page 184'), 'page184')
instrumentMethod(Test(18500, 'Page 185'), 'page185')
instrumentMethod(Test(18600, 'Page 186'), 'page186')
instrumentMethod(Test(18700, 'Page 187'), 'page187')
instrumentMethod(Test(18800, 'Page 188'), 'page188')
instrumentMethod(Test(18900, 'Page 189'), 'page189')
instrumentMethod(Test(19000, 'Page 190'), 'page190')
instrumentMethod(Test(19100, 'Page 191'), 'page191')
instrumentMethod(Test(19200, 'Page 192'), 'page192')
instrumentMethod(Test(19300, 'Page 193'), 'page193')
instrumentMethod(Test(19400, 'Page 194'), 'page194')
instrumentMethod(Test(19500, 'Page 195'), 'page195')
instrumentMethod(Test(19600, 'Page 196'), 'page196')
instrumentMethod(Test(19700, 'Page 197'), 'page197')
instrumentMethod(Test(19800, 'Page 198'), 'page198')
instrumentMethod(Test(19900, 'Page 199'), 'page199')
instrumentMethod(Test(20000, 'Page 200'), 'page200')
instrumentMethod(Test(20100, 'Page 201'), 'page201')
instrumentMethod(Test(20200, 'Page 202'), 'page202')
instrumentMethod(Test(20300, 'Page 203'), 'page203')
instrumentMethod(Test(20400, 'Page 204'), 'page204')
instrumentMethod(Test(20500, 'Page 205'), 'page205')
instrumentMethod(Test(20600, 'Page 206'), 'page206')
instrumentMethod(Test(20700, 'Page 207'), 'page207')
instrumentMethod(Test(20800, 'Page 208'), 'page208')
instrumentMethod(Test(20900, 'Page 209'), 'page209')
instrumentMethod(Test(21000, 'Page 210'), 'page210')
instrumentMethod(Test(21100, 'Page 211'), 'page211')
instrumentMethod(Test(21200, 'Page 212'), 'page212')
instrumentMethod(Test(21300, 'Page 213'), 'page213')
instrumentMethod(Test(21400, 'Page 214'), 'page214')
instrumentMethod(Test(21500, 'Page 215'), 'page215')
instrumentMethod(Test(21600, 'Page 216'), 'page216')
instrumentMethod(Test(21700, 'Page 217'), 'page217')
instrumentMethod(Test(21800, 'Page 218'), 'page218')
instrumentMethod(Test(21900, 'Page 219'), 'page219')
instrumentMethod(Test(22000, 'Page 220'), 'page220')
instrumentMethod(Test(22100, 'Page 221'), 'page221')
instrumentMethod(Test(22200, 'Page 222'), 'page222')
instrumentMethod(Test(22300, 'Page 223'), 'page223')
instrumentMethod(Test(22400, 'Page 224'), 'page224')
instrumentMethod(Test(22500, 'Page 225'), 'page225')
instrumentMethod(Test(22600, 'Page 226'), 'page226')
instrumentMethod(Test(22700, 'Page 227'), 'page227')
instrumentMethod(Test(22800, 'Page 228'), 'page228')
instrumentMethod(Test(22900, 'Page 229'), 'page229')
instrumentMethod(Test(23000, 'Page 230'), 'page230')
instrumentMethod(Test(23100, 'Page 231'), 'page231')
instrumentMethod(Test(23200, 'Page 232'), 'page232')
instrumentMethod(Test(23300, 'Page 233'), 'page233')
instrumentMethod(Test(23400, 'Page 234'), 'page234')
instrumentMethod(Test(23500, 'Page 235'), 'page235')
instrumentMethod(Test(23600, 'Page 236'), 'page236')
instrumentMethod(Test(23700, 'Page 237'), 'page237')
instrumentMethod(Test(23800, 'Page 238'), 'page238')
instrumentMethod(Test(23900, 'Page 239'), 'page239')
instrumentMethod(Test(24000, 'Page 240'), 'page240')
instrumentMethod(Test(24100, 'Page 241'), 'page241')
instrumentMethod(Test(24200, 'Page 242'), 'page242')
instrumentMethod(Test(24300, 'Page 243'), 'page243')
instrumentMethod(Test(24400, 'Page 244'), 'page244')
instrumentMethod(Test(24500, 'Page 245'), 'page245')
instrumentMethod(Test(24600, 'Page 246'), 'page246')
instrumentMethod(Test(24700, 'Page 247'), 'page247')
instrumentMethod(Test(24800, 'Page 248'), 'page248')
instrumentMethod(Test(24900, 'Page 249'), 'page249')
instrumentMethod(Test(25000, 'Page 250'), 'page250')
instrumentMethod(Test(25100, 'Page 251'), 'page251')
instrumentMethod(Test(25200, 'Page 252'), 'page252')
instrumentMethod(Test(25300, 'Page 253'), 'page253')
instrumentMethod(Test(25400, 'Page 254'), 'page254')
instrumentMethod(Test(25500, 'Page 255'), 'page255')
instrumentMethod(Test(25600, 'Page 256'), 'page256')
instrumentMethod(Test(25700, 'Page 257'), 'page257')
