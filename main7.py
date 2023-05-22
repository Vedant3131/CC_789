import webapp2
import urllib2
import json

class Mainpage(webapp2.RequestHandler):
      def get(self):
          self.response.write('<h1>Enter the pincode name</h1><br>')
          self.response.write('<form action="/res" method="post">')
          self.response.write('Zip code: <input type="number" name="zipcode" pattern="[0-9]-{6}" required><br>')
          #self.response.write('Branch: <input type="text" name="branch"><br>')
          self.response.write('<input type="submit" value="Search"><br>')
          self.response.write('</form><br>')
class result(webapp2.RequestHandler):
      def post(self):
          zipcode=self.request.get('zipcode')
          
          if len(zipcode)!=6 or not zipcode.isdigit():
             self.response.write('<h1>Error<h1>')
             self.response.write('<h2>Enter a valid 6 digit zipcode<h2>')
             self.response.write('<a href="/">Go back to form</a>')
          else:
             url='https://api.postalpincode.in/pincode/'+zipcode
             response=urllib2.urlopen(url).read()
             data=respoonse=json.loads(response)
             if data[0]['Status']=="Error":
                self.response.write('<h1>Error</h1>')
                self.response.write('<p>'+data[0]['Message']+'</p><br>')
                self.response.write('<a href="/">Go back to form</a>')
             else :
                  found=False
                  for obj in data[0]['PostOffice'] :
                    if not found:
                      self.response.write('Name:' + obj['Name']+'<br>')
                      self.response.write('Pincode:' + obj['Pincode']+'<br>')
                      self.response.write('Region:' + obj['Region']+'<br>')
                      self.response.write('Country:' + obj['Country']+'<br>')
                      found=True
                      
                  if not found :
                        self.response.write('<h1>not found any details</h1>')
                      
app = webapp2.WSGIApplication([('/', Mainpage),('/res', result)], debug=True)  
             
          
          
