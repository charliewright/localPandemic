import web
from loadvenues import *

urls = (
    #'/', 'index',
    '/data/(.+)', 'data'
    )
class index:
  def GET(self):
    #render the index.html
    pass

class data:
  def GET(self,code):
    return get_venues(code)
if __name__ == "__main__": 
  app = web.application(urls, globals())
  app.run()        
