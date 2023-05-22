import webapp2
import urllib2
import json

class MainPage(webapp2.RequestHandler):
      def get(self):
          self.response.write("<html><body>")
          self.response.write("<h1>Enter the name of university</h1>")
          self.response.write('<form action="/uni" method="post">')
          self.response.write('Name: <input type="text" name="nm"> <br>')
          self.response.write('<input type="submit" value="Search"><br>')
          self.response.write("</form></body></html>")
          
class result(webapp2.RequestHandler):
    def post(self):
      name=self.request.get('nm')
      url='http://universities.hipolabs.com/search?name='+name
      response=urllib2.urlopen(url).read()
      data=json.loads(response)
      self.response.write("<html><body>")
      self.response.write('<h1> Showing results for the Name: '+name+'</h1>')
      for obj in data:
          self.response.write("Name:"+ obj["name"] + "<br>")
          self.response.write("alpha_two_code:"+ obj["alpha_two_code"] + "<br>")
          self.response.write("country:"+ obj["country"] + "<br>")
          self.response.write("domain:"+ obj["domains"][0] + "<br>")
          self.response.write("<br><br>")
      self.response.write("<body><html>")
      
      
app=webapp2.WSGIApplication([("/",MainPage),("/uni",result)],debug=True)
          
