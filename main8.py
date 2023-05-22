import webapp2
import urllib2
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<html><body>')
        self.response.write('<form action="/forecast" method="post">')
        self.response.write('Latitude: <input type="number" step="any" name="lat"><br>')
        self.response.write('Longitude: <input type="number" step="any" name="lon"><br>')
        self.response.write('Forecast Type: <select name="type">')
        self.response.write('<option value="temperature_2m">Hourly</option>')
        self.response.write('<option value="daily">Daily</option>')                        
        self.response.write('</select><br>')
        self.response.write('<input type="submit" value="Search">')
        self.response.write('</form></body></html>')

class ForecastHandler(webapp2.RequestHandler):
    def post(self):
        lat = self.request.get('lat')
        lon = self.request.get('lon')
        forecast_type = self.request.get('type')
        url = 'https://api.open-meteo.com/v1/forecast?latitude='+lat+'&longitude='+lon+'&hourly='+forecast_type
        response = urllib2.urlopen(url).read()
        data = json.loads(response)
        self.response.write('<html><body>')
        self.response.write('<h1>Weather Forecast for '+'('+lat+','+lon+') - '+'Hourly'+' Forecast</h1><ul>')
        if forecast_type == 'temperature_2m':
            self.response.write('<table><tr><th>Time</th><th>\t\t</th><th>temperature</th><th>\t\t</th><th>timezone</th></tr>')
            for i in range(len(data['hourly']['temperature_2m'])):
                loc=data['elevation']
                time_=data['hourly']['time'][i]
                temperature_=data['hourly']['temperature_2m'][i]
                self.response.write('<tr><td>'+time_+'</td>'+'<td>\t\t</td>'+'<td>'+str(temperature_)+'</td>'+'<td>\t\t</td>'+'<td>'+str(loc)+'</td></tr>')
                self.response.write('</table>')
        elif forecast_type == 'daily':
            pass
        self.response.write('</ul></body></html>')

app = webapp2.WSGIApplication([('/', MainPage),('/forecast', ForecastHandler)], debug=True)

