# The Grinder 3.11
# HTTP script recorded by TCPProxy at Dec 20, 2012 12:08:30 PM

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
  [ NVPair('Accept', 'application/xml, text/xml, */*; q=0.01'),
    NVPair('Referer', 'http://aries:8080/ui-fw/tasks.htm'),
    NVPair('Cache-Control', 'no-cache'), ]

headers1= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://aries:8080/ui-fw/tasks.htm'), ]

headers2= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://aries:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=debd128f-c4a7-4b05-bdf2-c1b0ab270178&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NTIzNTgwOCYmaXNXb3JrZmxvd0FkbWluPT10cnVlJiZyb2xlcz09aW50YWxpb1xQcm9jZXNzTWFuYWdlcixpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yJiZvdT09UGVvcGxlJiZlbWFpbD09YWRtaW5AaW50YWxpby5vcmcmJmNuPT1hZG1pbiYmbGFzdG5hbWU9PUFkbWluaXN0cmF0b3ImJmZpcnN0bmFtZT09QURNSU4mJm9iamVjdGNsYXNzPT1vcmdhbml6YXRpb25hbFBlcnNvbixwZXJzb24saW5ldE9yZ1BlcnNvbix0b3AmJm5vbmNlPT00NDIzODUyNzQzODgyODYzODM0JiZ0aW1lc3RhbXA9PTEzNTU5ODUyMzU4MjUmJmRpZ2VzdD09QzhJN2dXZ2lybmZpdVZpZXNZWGw5QTlaZy9RPSYmJiZUT0tFTg==&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers3= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://aries:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=debd128f-c4a7-4b05-bdf2-c1b0ab270178&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NTIzNTgwOCYmaXNXb3JrZmxvd0FkbWluPT10cnVlJiZyb2xlcz09aW50YWxpb1xQcm9jZXNzTWFuYWdlcixpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yJiZvdT09UGVvcGxlJiZlbWFpbD09YWRtaW5AaW50YWxpby5vcmcmJmNuPT1hZG1pbiYmbGFzdG5hbWU9PUFkbWluaXN0cmF0b3ImJmZpcnN0bmFtZT09QURNSU4mJm9iamVjdGNsYXNzPT1vcmdhbml6YXRpb25hbFBlcnNvbixwZXJzb24saW5ldE9yZ1BlcnNvbix0b3AmJm5vbmNlPT00NDIzODUyNzQzODgyODYzODM0JiZ0aW1lc3RhbXA9PTEzNTU5ODUyMzU4MjUmJmRpZ2VzdD09QzhJN2dXZ2lybmZpdVZpZXNZWGw5QTlaZy9RPSYmJiZUT0tFTg==&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers4= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://aries:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=debd128f-c4a7-4b05-bdf2-c1b0ab270178&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NTIzNTgwOCYmaXNXb3JrZmxvd0FkbWluPT10cnVlJiZyb2xlcz09aW50YWxpb1xQcm9jZXNzTWFuYWdlcixpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yJiZvdT09UGVvcGxlJiZlbWFpbD09YWRtaW5AaW50YWxpby5vcmcmJmNuPT1hZG1pbiYmbGFzdG5hbWU9PUFkbWluaXN0cmF0b3ImJmZpcnN0bmFtZT09QURNSU4mJm9iamVjdGNsYXNzPT1vcmdhbml6YXRpb25hbFBlcnNvbixwZXJzb24saW5ldE9yZ1BlcnNvbix0b3AmJm5vbmNlPT00NDIzODUyNzQzODgyODYzODM0JiZ0aW1lc3RhbXA9PTEzNTU5ODUyMzU4MjUmJmRpZ2VzdD09QzhJN2dXZ2lybmZpdVZpZXNZWGw5QTlaZy9RPSYmJiZUT0tFTg==&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers5= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://aries:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=debd128f-c4a7-4b05-bdf2-c1b0ab270178&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NTIzNTgwOCYmaXNXb3JrZmxvd0FkbWluPT10cnVlJiZyb2xlcz09aW50YWxpb1xQcm9jZXNzTWFuYWdlcixpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yJiZvdT09UGVvcGxlJiZlbWFpbD09YWRtaW5AaW50YWxpby5vcmcmJmNuPT1hZG1pbiYmbGFzdG5hbWU9PUFkbWluaXN0cmF0b3ImJmZpcnN0bmFtZT09QURNSU4mJm9iamVjdGNsYXNzPT1vcmdhbml6YXRpb25hbFBlcnNvbixwZXJzb24saW5ldE9yZ1BlcnNvbix0b3AmJm5vbmNlPT00NDIzODUyNzQzODgyODYzODM0JiZ0aW1lc3RhbXA9PTEzNTU5ODUyMzU4MjUmJmRpZ2VzdD09QzhJN2dXZ2lybmZpdVZpZXNZWGw5QTlaZy9RPSYmJiZUT0tFTg==&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers6= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://aries:8080/ui-fw/style/jqueryui/jquery.alerts.css'), ]

headers7= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://aries:8080/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/IntalioInternal/ServerLaunch.html?id=40afb042-444e-46e4-86b5-9073e6350f89&type=PIPATask&url=%2Fgi%2Fapppath%2FSampleAjaxPAWithTimer%2FsamplePipa.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NTIzNTgwOCYmaXNXb3JrZmxvd0FkbWluPT10cnVlJiZyb2xlcz09aW50YWxpb1xQcm9jZXNzTWFuYWdlcixpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yJiZvdT09UGVvcGxlJiZlbWFpbD09YWRtaW5AaW50YWxpby5vcmcmJmNuPT1hZG1pbiYmbGFzdG5hbWU9PUFkbWluaXN0cmF0b3ImJmZpcnN0bmFtZT09QURNSU4mJm9iamVjdGNsYXNzPT1vcmdhbml6YXRpb25hbFBlcnNvbixwZXJzb24saW5ldE9yZ1BlcnNvbix0b3AmJm5vbmNlPT00NDIzODUyNzQzODgyODYzODM0JiZ0aW1lc3RhbXA9PTEzNTU5ODUyMzU4MjUmJmRpZ2VzdD09QzhJN2dXZ2lybmZpdVZpZXNZWGw5QTlaZy9RPSYmJiZUT0tFTg==&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers8= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://aries:8080/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/IntalioInternal/ServerLaunch.html?id=40afb042-444e-46e4-86b5-9073e6350f89&type=PIPATask&url=%2Fgi%2Fapppath%2FSampleAjaxPAWithTimer%2FsamplePipa.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NTIzNTgwOCYmaXNXb3JrZmxvd0FkbWluPT10cnVlJiZyb2xlcz09aW50YWxpb1xQcm9jZXNzTWFuYWdlcixpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yJiZvdT09UGVvcGxlJiZlbWFpbD09YWRtaW5AaW50YWxpby5vcmcmJmNuPT1hZG1pbiYmbGFzdG5hbWU9PUFkbWluaXN0cmF0b3ImJmZpcnN0bmFtZT09QURNSU4mJm9iamVjdGNsYXNzPT1vcmdhbml6YXRpb25hbFBlcnNvbixwZXJzb24saW5ldE9yZ1BlcnNvbix0b3AmJm5vbmNlPT00NDIzODUyNzQzODgyODYzODM0JiZ0aW1lc3RhbXA9PTEzNTU5ODUyMzU4MjUmJmRpZ2VzdD09QzhJN2dXZ2lybmZpdVZpZXNZWGw5QTlaZy9RPSYmJiZUT0tFTg==&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers9= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://aries:8080/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/IntalioInternal/ServerLaunch.html?id=40afb042-444e-46e4-86b5-9073e6350f89&type=PIPATask&url=%2Fgi%2Fapppath%2FSampleAjaxPAWithTimer%2FsamplePipa.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NTIzNTgwOCYmaXNXb3JrZmxvd0FkbWluPT10cnVlJiZyb2xlcz09aW50YWxpb1xQcm9jZXNzTWFuYWdlcixpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yJiZvdT09UGVvcGxlJiZlbWFpbD09YWRtaW5AaW50YWxpby5vcmcmJmNuPT1hZG1pbiYmbGFzdG5hbWU9PUFkbWluaXN0cmF0b3ImJmZpcnN0bmFtZT09QURNSU4mJm9iamVjdGNsYXNzPT1vcmdhbml6YXRpb25hbFBlcnNvbixwZXJzb24saW5ldE9yZ1BlcnNvbix0b3AmJm5vbmNlPT00NDIzODUyNzQzODgyODYzODM0JiZ0aW1lc3RhbXA9PTEzNTU5ODUyMzU4MjUmJmRpZ2VzdD09QzhJN2dXZ2lybmZpdVZpZXNZWGw5QTlaZy9RPSYmJiZUT0tFTg==&user=intalio%5Cadmin&claimTaskOnOpen=false'), ]

headers10= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://aries:8080/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/IntalioInternal/ServerLaunch.html?id=40afb042-444e-46e4-86b5-9073e6350f89&type=PIPATask&url=%2Fgi%2Fapppath%2FSampleAjaxPAWithTimer%2FsamplePipa.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NTIzNTgwOCYmaXNXb3JrZmxvd0FkbWluPT10cnVlJiZyb2xlcz09aW50YWxpb1xQcm9jZXNzTWFuYWdlcixpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yJiZvdT09UGVvcGxlJiZlbWFpbD09YWRtaW5AaW50YWxpby5vcmcmJmNuPT1hZG1pbiYmbGFzdG5hbWU9PUFkbWluaXN0cmF0b3ImJmZpcnN0bmFtZT09QURNSU4mJm9iamVjdGNsYXNzPT1vcmdhbml6YXRpb25hbFBlcnNvbixwZXJzb24saW5ldE9yZ1BlcnNvbix0b3AmJm5vbmNlPT00NDIzODUyNzQzODgyODYzODM0JiZ0aW1lc3RhbXA9PTEzNTU5ODUyMzU4MjUmJmRpZ2VzdD09QzhJN2dXZ2lybmZpdVZpZXNZWGw5QTlaZy9RPSYmJiZUT0tFTg==&user=intalio%5Cadmin&claimTaskOnOpen=false'),
    NVPair('Cache-Control', 'no-cache'), ]

url0 = 'http://aries:8080'

request101 = createRequest(Test(101, 'POST updates.htm'), url0, headers0)

request201 = createRequest(Test(201, 'GET ServerLaunch.html'), url0, headers1)

request301 = createRequest(Test(301, 'GET config.xml'), url0, headers2)

request302 = createRequest(Test(302, 'GET style.css'), url0)

request401 = createRequest(Test(401, 'GET translations.xml'), url0, headers2)

request501 = createRequest(Test(501, 'GET appCanvas.xml'), url0, headers2)

request502 = createRequest(Test(502, 'GET Packages.js'), url0, headers3)

request503 = createRequest(Test(503, 'GET logic.js'), url0, headers3)

request504 = createRequest(Test(504, 'GET attachments.gif'), url0, headers4)

request505 = createRequest(Test(505, 'GET error.gif'), url0, headers4)

request506 = createRequest(Test(506, 'GET close.png'), url0, headers4)

request601 = createRequest(Test(601, 'GET TaskManagementServicesMapping.xml'), url0, headers2)

request701 = createRequest(Test(701, 'GET Tidy.xsl'), url0, headers2)

request801 = createRequest(Test(801, 'POST validation'), url0, headers5)

request901 = createRequest(Test(901, 'GET TaskManagementServicesMapping.xml'), url0, headers2)

request1001 = createRequest(Test(1001, 'GET FormModelMapping.xml'), url0, headers2)

request1101 = createRequest(Test(1101, 'POST validation'), url0, headers5)

request1201 = createRequest(Test(1201, 'GET empty.jsp'), url0, headers2)

request1301 = createRequest(Test(1301, 'POST updates.htm'), url0, headers0)

request1401 = createRequest(Test(1401, 'POST updates.htm'), url0, headers0)

request1402 = createRequest(Test(1402, 'GET hl.png'), url0)

request1403 = createRequest(Test(1403, 'GET title.gif'), url0, headers6)

request1404 = createRequest(Test(1404, 'GET info.gif'), url0, headers6)

request1501 = createRequest(Test(1501, 'GET ServerLaunch.html'), url0, headers1)

request1601 = createRequest(Test(1601, 'GET config.xml'), url0, headers7)

request1701 = createRequest(Test(1701, 'GET translations.xml'), url0, headers7)

request1702 = createRequest(Test(1702, 'GET style.css'), url0)

request1801 = createRequest(Test(1801, 'GET appCanvas.xml'), url0, headers7)

request1802 = createRequest(Test(1802, 'GET Packages.js'), url0, headers8)

request1803 = createRequest(Test(1803, 'GET logic.js'), url0, headers8)

request1804 = createRequest(Test(1804, 'GET attachments.gif'), url0, headers9)

request1805 = createRequest(Test(1805, 'GET close.png'), url0, headers9)

request1901 = createRequest(Test(1901, 'GET TaskManagementServicesMapping.xml'), url0, headers7)

request2001 = createRequest(Test(2001, 'GET Tidy.xsl'), url0, headers7)

request2101 = createRequest(Test(2101, 'POST validation'), url0, headers10)

request2201 = createRequest(Test(2201, 'GET FormModelMapping.xml'), url0, headers7)

request2301 = createRequest(Test(2301, 'GET TaskManagementServicesMapping.xml'), url0, headers7)

request2401 = createRequest(Test(2401, 'GET FormModelMapping.xml'), url0, headers7)

request2501 = createRequest(Test(2501, 'POST validation'), url0, headers10)

request2601 = createRequest(Test(2601, 'GET empty.jsp'), url0, headers7)

request2701 = createRequest(Test(2701, 'POST updates.htm'), url0, headers0)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """POST updates.htm (request 101)."""
    result = request101.POST('/ui-fw/updates.htm',
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
    # 2 different values for token_token found in response, using the first one.
    self.token_token = \
      httpUtilities.valueFromBodyURI('token') # 'VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlz...'
    self.token_user = \
      httpUtilities.valueFromBodyURI('user') # 'intalio\\admin'
    self.token_claimTaskOnOpen = \
      httpUtilities.valueFromBodyURI('claimTaskOnOpen') # 'false'
    self.token_claim2000TaskOnOpen = \
      httpUtilities.valueFromBodyURI('''claim\r
2000\r
TaskOnOpen''') # 'false'

    return result

  def page2(self):
    """GET ServerLaunch.html (request 201)."""
    self.token_id = \
      'debd128f-c4a7-4b05-bdf2-c1b0ab270178'
    self.token_url = \
      '/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html'
    result = request201.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html' +
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

  def page3(self):
    """GET config.xml (requests 301-302)."""
    result = request301.GET('/gi/apppath/SubstarctDates/form.gi/config.xml')

    grinder.sleep(74)
    request302.GET('/gi/apppath/SubstarctDates/form.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://aries:8080/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html?id=debd128f-c4a7-4b05-bdf2-c1b0ab270178&type=PIPATask&url=%2Fgi%2Fapppath%2FSubstarctDates%2Fform.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NTIzNTgwOCYmaXNXb3JrZmxvd0FkbWluPT10cnVlJiZyb2xlcz09aW50YWxpb1xQcm9jZXNzTWFuYWdlcixpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yJiZvdT09UGVvcGxlJiZlbWFpbD09YWRtaW5AaW50YWxpby5vcmcmJmNuPT1hZG1pbiYmbGFzdG5hbWU9PUFkbWluaXN0cmF0b3ImJmZpcnN0bmFtZT09QURNSU4mJm9iamVjdGNsYXNzPT1vcmdhbml6YXRpb25hbFBlcnNvbixwZXJzb24saW5ldE9yZ1BlcnNvbix0b3AmJm5vbmNlPT00NDIzODUyNzQzODgyODYzODM0JiZ0aW1lc3RhbXA9PTEzNTU5ODUyMzU4MjUmJmRpZ2VzdD09QzhJN2dXZ2lybmZpdVZpZXNZWGw5QTlaZy9RPSYmJiZUT0tFTg==&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page4(self):
    """GET translations.xml (request 401)."""
    result = request401.GET('/gi/apppath/SubstarctDates/form.gi/jss/translations.xml')

    return result

  def page5(self):
    """GET appCanvas.xml (requests 501-506)."""
    result = request501.GET('/gi/apppath/SubstarctDates/form.gi/components/appCanvas.xml')

    grinder.sleep(27)
    request502.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/Packages.js')
    self.token_imgsrc = \
      httpUtilities.valueFromBodyURI('<img src') # ''
    self.token_ahref = \
      httpUtilities.valueFromBodyURI('<a href') # ''

    grinder.sleep(48)
    request503.GET('/gi/apppath/SubstarctDates/form.gi/js/logic.js')

    grinder.sleep(181)
    request504.GET('/gi/apppath/SubstarctDates/form.gi/images/attachments.gif')

    request505.GET('/gi/apppath/SubstarctDates/form.gi/images/error.gif')

    request506.GET('/gi/apppath/SubstarctDates/form.gi/images/close.png')

    return result

  def page6(self):
    """GET TaskManagementServicesMapping.xml (request 601)."""
    result = request601.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page7(self):
    """GET Tidy.xsl (request 701)."""
    result = request701.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/Tidy.xsl')

    return result

  def page8(self):
    """POST validation (request 801)."""
    result = request801.POST('/gi/validation',
      ( NVPair('assembly', 'SubstarctDates'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>debd128f-c4a7-4b05-bdf2-c1b0ab270178</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NTIzNTgwOCYmaXNXb3JrZmxvd0FkbWluPT10cnVlJiZyb2xlcz09aW50YWxpb1xQcm9jZXNzTWFuYWdlcixpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yJiZvdT09UGVvcGxlJiZlbWFpbD09YWRtaW5AaW50YWxpby5vcmcmJmNuPT1hZG1pbiYmbGFzdG5hbWU9PUFkbWluaXN0cmF0b3ImJmZpcnN0bmFtZT09QURNSU4mJm9iamVjdGNsYXNzPT1vcmdhbml6YXRpb25hbFBlcnNvbixwZXJzb24saW5ldE9yZ1BlcnNvbix0b3AmJm5vbmNlPT00NDIzODUyNzQzODgyODYzODM0JiZ0aW1lc3RhbXA9PTEzNTU5ODUyMzU4MjUmJmRpZ2VzdD09QzhJN2dXZ2lybmZpdVZpZXNZWGw5QTlaZy9RPSYmJiZUT0tFTg==</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page9(self):
    """GET TaskManagementServicesMapping.xml (request 901)."""
    result = request901.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page10(self):
    """GET FormModelMapping.xml (request 1001)."""
    result = request1001.GET('/gi/apppath/SubstarctDates/form.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page11(self):
    """POST validation (request 1101)."""
    result = request1101.POST('/gi/validation',
      ( NVPair('assembly', 'SubstarctDates'),
        NVPair('form', 'form.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:initRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>debd128f-c4a7-4b05-bdf2-c1b0ab270178</jsx1:taskId><jsx1:input><a0:FormModel xmlns:a0=\"http://www.intalio.com/gi/form.gi\"><date1>2012-12-18</date1><date2>2012-12-22</date2></a0:FormModel></jsx1:input><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NTIzNTgwOCYmaXNXb3JrZmxvd0FkbWluPT10cnVlJiZyb2xlcz09aW50YWxpb1xQcm9jZXNzTWFuYWdlcixpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yJiZvdT09UGVvcGxlJiZlbWFpbD09YWRtaW5AaW50YWxpby5vcmcmJmNuPT1hZG1pbiYmbGFzdG5hbWU9PUFkbWluaXN0cmF0b3ImJmZpcnN0bmFtZT09QURNSU4mJm9iamVjdGNsYXNzPT1vcmdhbml6YXRpb25hbFBlcnNvbixwZXJzb24saW5ldE9yZ1BlcnNvbix0b3AmJm5vbmNlPT00NDIzODUyNzQzODgyODYzODM0JiZ0aW1lc3RhbXA9PTEzNTU5ODUyMzU4MjUmJmRpZ2VzdD09QzhJN2dXZ2lybmZpdVZpZXNZWGw5QTlaZy9RPSYmJiZUT0tFTg==</jsx1:participantToken><jsx1:formUrl>/gi/apppath/SubstarctDates/form.gi/IntalioInternal/ServerLaunch.html</jsx1:formUrl></jsx1:initRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page12(self):
    """GET empty.jsp (request 1201)."""
    result = request1201.GET('/ui-fw/script/empty.jsp')

    return result

  def page13(self):
    """POST updates.htm (request 1301)."""
    result = request1301.POST('/ui-fw/updates.htm',
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
    # 14 different values for token_type found in response; the first matched
    # the last known value of token_type - don't update the variable.
    # 40 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/AjaxPA1/form.gi/IntalioInter...'
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def page14(self):
    """POST updates.htm (requests 1401-1404)."""
    result = request1401.POST('/ui-fw/updates.htm',
      ( NVPair('page', '1'),
        NVPair('rp', '15'),
        NVPair('sortname', 'undefined'),
        NVPair('sortorder', 'undefined'),
        NVPair('query', ''),
        NVPair('qtype', '_description'),
        NVPair('type', 'PIPATask'),
        NVPair('update', 'true'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))
    # 26 different values for token_id found in response; the first matched
    # the last known value of token_id - don't update the variable.
    # 14 different values for token_type found in response; the first matched
    # the last known value of token_type - don't update the variable.
    # 39 different values for token_url found in response; the first matched
    # the last known value of token_url - don't update the variable.
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    grinder.sleep(5134)
    request1402.GET('/ui-fw/images/flexigrid/hl.png', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://aries:8080/ui-fw/style/flexigrid.css'), ))

    grinder.sleep(1960)
    request1403.GET('/ui-fw/style/jqueryui/images/title.gif')

    request1404.GET('/ui-fw/style/jqueryui/images/info.gif')

    return result

  def page15(self):
    """GET ServerLaunch.html (request 1501)."""
    self.token_id = \
      '40afb042-444e-46e4-86b5-9073e6350f89'
    self.token_url = \
      '/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/IntalioInternal/ServerLaunch.html'
    result = request1501.GET('/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/IntalioInternal/ServerLaunch.html' +
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

  def page16(self):
    """GET config.xml (request 1601)."""
    result = request1601.GET('/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/config.xml')

    return result

  def page17(self):
    """GET translations.xml (requests 1701-1702)."""
    result = request1701.GET('/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/jss/translations.xml')

    request1702.GET('/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/css/style.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://aries:8080/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/IntalioInternal/ServerLaunch.html?id=40afb042-444e-46e4-86b5-9073e6350f89&type=PIPATask&url=%2Fgi%2Fapppath%2FSampleAjaxPAWithTimer%2FsamplePipa.gi%2FIntalioInternal%2FServerLaunch.html&token=VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NTIzNTgwOCYmaXNXb3JrZmxvd0FkbWluPT10cnVlJiZyb2xlcz09aW50YWxpb1xQcm9jZXNzTWFuYWdlcixpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yJiZvdT09UGVvcGxlJiZlbWFpbD09YWRtaW5AaW50YWxpby5vcmcmJmNuPT1hZG1pbiYmbGFzdG5hbWU9PUFkbWluaXN0cmF0b3ImJmZpcnN0bmFtZT09QURNSU4mJm9iamVjdGNsYXNzPT1vcmdhbml6YXRpb25hbFBlcnNvbixwZXJzb24saW5ldE9yZ1BlcnNvbix0b3AmJm5vbmNlPT00NDIzODUyNzQzODgyODYzODM0JiZ0aW1lc3RhbXA9PTEzNTU5ODUyMzU4MjUmJmRpZ2VzdD09QzhJN2dXZ2lybmZpdVZpZXNZWGw5QTlaZy9RPSYmJiZUT0tFTg==&user=intalio%5Cadmin&claimTaskOnOpen=false'), ))

    return result

  def page18(self):
    """GET appCanvas.xml (requests 1801-1805)."""
    result = request1801.GET('/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/components/appCanvas.xml')

    grinder.sleep(45)
    request1802.GET('/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/IntalioInternal/Packages.js')

    grinder.sleep(23)
    request1803.GET('/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/js/logic.js')

    request1804.GET('/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/images/attachments.gif')

    grinder.sleep(203)
    request1805.GET('/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/images/close.png')

    return result

  def page19(self):
    """GET TaskManagementServicesMapping.xml (request 1901)."""
    result = request1901.GET('/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page20(self):
    """GET Tidy.xsl (request 2001)."""
    result = request2001.GET('/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/IntalioInternal/Tidy.xsl')

    return result

  def page21(self):
    """POST validation (request 2101)."""
    result = request2101.POST('/gi/validation',
      ( NVPair('assembly', 'SampleAjaxPAWithTimer'),
        NVPair('form', 'samplePipa.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:getTaskRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>40afb042-444e-46e4-86b5-9073e6350f89</jsx1:taskId><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NTIzNTgwOCYmaXNXb3JrZmxvd0FkbWluPT10cnVlJiZyb2xlcz09aW50YWxpb1xQcm9jZXNzTWFuYWdlcixpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yJiZvdT09UGVvcGxlJiZlbWFpbD09YWRtaW5AaW50YWxpby5vcmcmJmNuPT1hZG1pbiYmbGFzdG5hbWU9PUFkbWluaXN0cmF0b3ImJmZpcnN0bmFtZT09QURNSU4mJm9iamVjdGNsYXNzPT1vcmdhbml6YXRpb25hbFBlcnNvbixwZXJzb24saW5ldE9yZ1BlcnNvbix0b3AmJm5vbmNlPT00NDIzODUyNzQzODgyODYzODM0JiZ0aW1lc3RhbXA9PTEzNTU5ODUyMzU4MjUmJmRpZ2VzdD09QzhJN2dXZ2lybmZpdVZpZXNZWGw5QTlaZy9RPSYmJiZUT0tFTg==</jsx1:participantToken></jsx1:getTaskRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page22(self):
    """GET FormModelMapping.xml (request 2201)."""
    result = request2201.GET('/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page23(self):
    """GET TaskManagementServicesMapping.xml (request 2301)."""
    result = request2301.GET('/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/IntalioInternal/TaskManagementServicesMapping.xml')

    return result

  def page24(self):
    """GET FormModelMapping.xml (request 2401)."""
    result = request2401.GET('/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/IntalioInternal/FormModelMapping.xml')

    return result

  def page25(self):
    """POST validation (request 2501)."""
    result = request2501.POST('/gi/validation',
      ( NVPair('assembly', 'SampleAjaxPAWithTimer'),
        NVPair('form', 'samplePipa.gi'),
        NVPair('message', '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:SOAP-ENC=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">
<SOAP-ENV:Body><jsx1:initRequest xmlns:jsx1=\"http://www.intalio.com/BPMS/Workflow/TaskManagementServices-20051109/\"><jsx1:taskId>40afb042-444e-46e4-86b5-9073e6350f89</jsx1:taskId><jsx1:input><a0:FormModel xmlns:a0=\"http://www.intalio.com/gi/samplePipa.gi\"/></jsx1:input><jsx1:participantToken>VE9LRU4mJnVzZXI9PWludGFsaW9cYWRtaW4mJmlzc3VlZD09MTM1NTk4NTIzNTgwOCYmaXNXb3JrZmxvd0FkbWluPT10cnVlJiZyb2xlcz09aW50YWxpb1xQcm9jZXNzTWFuYWdlcixpbnRhbGlvXFByb2Nlc3NBZG1pbmlzdHJhdG9yJiZvdT09UGVvcGxlJiZlbWFpbD09YWRtaW5AaW50YWxpby5vcmcmJmNuPT1hZG1pbiYmbGFzdG5hbWU9PUFkbWluaXN0cmF0b3ImJmZpcnN0bmFtZT09QURNSU4mJm9iamVjdGNsYXNzPT1vcmdhbml6YXRpb25hbFBlcnNvbixwZXJzb24saW5ldE9yZ1BlcnNvbix0b3AmJm5vbmNlPT00NDIzODUyNzQzODgyODYzODM0JiZ0aW1lc3RhbXA9PTEzNTU5ODUyMzU4MjUmJmRpZ2VzdD09QzhJN2dXZ2lybmZpdVZpZXNZWGw5QTlaZy9RPSYmJiZUT0tFTg==</jsx1:participantToken><jsx1:formUrl>/gi/apppath/SampleAjaxPAWithTimer/samplePipa.gi/IntalioInternal/ServerLaunch.html</jsx1:formUrl></jsx1:initRequest></SOAP-ENV:Body>
</SOAP-ENV:Envelope>'''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page26(self):
    """GET empty.jsp (request 2601)."""
    result = request2601.GET('/ui-fw/script/empty.jsp')

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
    # 27 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '6d316302-675f-46d7-b65d-14e904fdd1e0'
    # 14 different values for token_type found in response; the first matched
    # the last known value of token_type - don't update the variable.
    # 40 different values for token_url found in response, using the first one.
    self.token_url = \
      httpUtilities.valueFromBodyURI('url') # '/gi/apppath/AjaxPA1/form.gi/IntalioInter...'
    # 1 different values for token_token found in response; the first matched
    # the last known value of token_token - don't update the variable.

    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    self.page1()      # POST updates.htm (request 101)

    grinder.sleep(3573)
    self.page2()      # GET ServerLaunch.html (request 201)

    grinder.sleep(97)
    self.page3()      # GET config.xml (requests 301-302)
    self.page4()      # GET translations.xml (request 401)
    self.page5()      # GET appCanvas.xml (requests 501-506)
    self.page6()      # GET TaskManagementServicesMapping.xml (request 601)

    grinder.sleep(33)
    self.page7()      # GET Tidy.xsl (request 701)
    self.page8()      # POST validation (request 801)

    grinder.sleep(6030)
    self.page9()      # GET TaskManagementServicesMapping.xml (request 901)

    grinder.sleep(16)
    self.page10()     # GET FormModelMapping.xml (request 1001)

    grinder.sleep(47)
    self.page11()     # POST validation (request 1101)

    grinder.sleep(17)
    self.page12()     # GET empty.jsp (request 1201)

    grinder.sleep(24)
    self.page13()     # POST updates.htm (request 1301)

    grinder.sleep(3370)
    self.page14()     # POST updates.htm (requests 1401-1404)

    grinder.sleep(5375)
    self.page15()     # GET ServerLaunch.html (request 1501)

    grinder.sleep(112)
    self.page16()     # GET config.xml (request 1601)

    grinder.sleep(79)
    self.page17()     # GET translations.xml (requests 1701-1702)
    self.page18()     # GET appCanvas.xml (requests 1801-1805)
    self.page19()     # GET TaskManagementServicesMapping.xml (request 1901)

    grinder.sleep(58)
    self.page20()     # GET Tidy.xsl (request 2001)
    self.page21()     # POST validation (request 2101)

    grinder.sleep(13)
    self.page22()     # GET FormModelMapping.xml (request 2201)

    grinder.sleep(1470)
    self.page23()     # GET TaskManagementServicesMapping.xml (request 2301)

    grinder.sleep(56)
    self.page24()     # GET FormModelMapping.xml (request 2401)
    self.page25()     # POST validation (request 2501)

    grinder.sleep(13)
    self.page26()     # GET empty.jsp (request 2601)

    grinder.sleep(30)
    self.page27()     # POST updates.htm (request 2701)


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
