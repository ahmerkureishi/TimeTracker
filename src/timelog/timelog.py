import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users

from config import jinja_environment
from datetime import datetime
from time import strptime

class TimeTracker(webapp2.RequestHandler):

    def get(self):
        for d in demodata:
            try:
                d['datetime'] = datetime(*strptime(d['datetime'], 
                                                   '%m-%d-%Y %H:%M')[0:6])
            except TypeError:
                pass

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
            data = demodata
            template = jinja_environment.get_template('timelog.html')
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            data = []
            template = jinja_environment.get_template('index.html')

        template_values = {
            'data': data,
            'greetings': [],
            'url': url,
            'url_linktext': url_linktext,
        }

        self.response.out.write(template.render(template_values))

    def post(self):
        pass

class Help(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('help.html')
        self.response.out.write(template.render())

class Settings(webapp2.RequestHandler):

    def get(self):
        template_values = {}
        template = jinja_environment.get_template('settings.html')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', TimeTracker),
                               ('/help', Help),
                               ('/settings', Settings)],
                              debug=True)

demodata = [{'activities': ['bavaria', 'com', 'meeting'],
  'activity': 'bavaria :: com :: meeting',
  'date': '07-05-2011',
  'datetime': '07-05-2011 16:00',
  'pause': False,
  'start': False,
  'time': '16:00'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '07-05-2011',
  'datetime': '07-05-2011 08:00',
  'pause': False,
  'start': False,
  'time': '08:00'},
 {'activities': ['knmp', 'sfk', 'design integration'],
  'activity': 'knmp :: sfk :: design integration',
  'date': '07-04-2011',
  'datetime': '07-04-2011 17:00',
  'pause': False,
  'start': False,
  'time': '17:00'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '07-04-2011',
  'datetime': '07-04-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'},
 {'activities': ['knmp', 'sfk', 'design integration'],
  'activity': 'knmp :: sfk :: design integration',
  'date': '07-01-2011',
  'datetime': '07-01-2011 17:00',
  'pause': False,
  'start': False,
  'time': '17:00'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '07-01-2011',
  'datetime': '07-01-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'},
 {'activities': ['bavaria', 'com', 'release/check'],
  'activity': 'bavaria :: com :: release/check',
  'date': '06-30-2011',
  'datetime': '06-30-2011 22:00',
  'pause': False,
  'start': False,
  'time': '22:00'},
 {'activities': ['diner **'],
  'activity': 'diner **',
  'date': '06-30-2011',
  'datetime': '06-30-2011 19:00',
  'pause': True,
  'start': False,
  'time': '19:00'},
 {'activities': ['bavaria', 'com', 'issue 102'],
  'activity': 'bavaria :: com :: issue 102',
  'date': '06-30-2011',
  'datetime': '06-30-2011 17:45',
  'pause': False,
  'start': False,
  'time': '17:45'},
 {'activities': ['bavaria', 'com', 'issue 101'],
  'activity': 'bavaria :: com :: issue 101',
  'date': '06-30-2011',
  'datetime': '06-30-2011 16:45',
  'pause': False,
  'start': False,
  'time': '16:45'},
 {'activities': ['bavaria', 'com', 'issue 99'],
  'activity': 'bavaria :: com :: issue 99',
  'date': '06-30-2011',
  'datetime': '06-30-2011 15:45',
  'pause': False,
  'start': False,
  'time': '15:45'},
 {'activities': ['bavaria', 'com', 'issue 98'],
  'activity': 'bavaria :: com :: issue 98',
  'date': '06-30-2011',
  'datetime': '06-30-2011 15:15',
  'pause': False,
  'start': False,
  'time': '15:15'},
 {'activities': ['bavaria', 'com', 'issue 93'],
  'activity': 'bavaria :: com :: issue 93',
  'date': '06-30-2011',
  'datetime': '06-30-2011 14:15',
  'pause': False,
  'start': False,
  'time': '14:15'},
 {'activities': ['lunch **'],
  'activity': 'lunch **',
  'date': '06-30-2011',
  'datetime': '06-30-2011 12:45',
  'pause': True,
  'start': False,
  'time': '12:45'},
 {'activities': ['bavaria', 'com', 'issue 93'],
  'activity': 'bavaria :: com :: issue 93',
  'date': '06-30-2011',
  'datetime': '06-30-2011 12:30',
  'pause': False,
  'start': False,
  'time': '12:30'},
 {'activities': ['bavaria', 'com', 'issue 92'],
  'activity': 'bavaria :: com :: issue 92',
  'date': '06-30-2011',
  'datetime': '06-30-2011 11:30',
  'pause': False,
  'start': False,
  'time': '11:30'},
 {'activities': ['bavaria', 'com', 'issue 91'],
  'activity': 'bavaria :: com :: issue 91',
  'date': '06-30-2011',
  'datetime': '06-30-2011 11:00',
  'pause': False,
  'start': False,
  'time': '11:00'},
 {'activities': ['bavaria', 'com', 'issue 85'],
  'activity': 'bavaria :: com :: issue 85',
  'date': '06-30-2011',
  'datetime': '06-30-2011 10:00',
  'pause': False,
  'start': False,
  'time': '10:00'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-30-2011',
  'datetime': '06-30-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'},
 {'activities': ['bavaria', 'com', 'tube promo fix'],
  'activity': 'bavaria :: com :: tube promo fix',
  'date': '06-29-2011',
  'datetime': '06-29-2011 17:22',
  'pause': False,
  'start': False,
  'time': '17:22'},
 {'activities': ['bavaria', 'com', 'glow'],
  'activity': 'bavaria :: com :: glow',
  'date': '06-29-2011',
  'datetime': '06-29-2011 16:37',
  'pause': False,
  'start': False,
  'time': '16:37'},
 {'activities': ['bavaria', 'com', 'pubfacts'],
  'activity': 'bavaria :: com :: pubfacts',
  'date': '06-29-2011',
  'datetime': '06-29-2011 14:15',
  'pause': False,
  'start': False,
  'time': '14:15'},
 {'activities': ['bavaria',
                 'com',
                 'update plone, add audiopool, add patches'],
  'activity': 'bavaria :: com :: update plone, add audiopool, add patches',
  'date': '06-29-2011',
  'datetime': '06-29-2011 12:15',
  'pause': False,
  'start': False,
  'time': '12:15'},
 {'activities': ['bavaria', 'com', 'functionaliteit'],
  'activity': 'bavaria :: com :: functionaliteit',
  'date': '06-29-2011',
  'datetime': '06-29-2011 10:15',
  'pause': False,
  'start': False,
  'time': '10:15'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-29-2011',
  'datetime': '06-29-2011 09:14',
  'pause': False,
  'start': False,
  'time': '09:14'},
 {'activities': ['vvv', 'plone patch'],
  'activity': 'vvv :: plone patch',
  'date': '06-28-2011',
  'datetime': '06-28-2011 21:00',
  'pause': False,
  'start': False,
  'time': '21:00'},
 {'activities': ['nuffic', 'plone patch'],
  'activity': 'nuffic :: plone patch',
  'date': '06-28-2011',
  'datetime': '06-28-2011 20:30',
  'pause': False,
  'start': False,
  'time': '20:30'},
 {'activities': ['bavaria', 'com', 'plone patch'],
  'activity': 'bavaria :: com :: plone patch',
  'date': '06-28-2011',
  'datetime': '06-28-2011 19:30',
  'pause': False,
  'start': False,
  'time': '19:30'},
 {'activities': ['diner **'],
  'activity': 'diner **',
  'date': '06-28-2011',
  'datetime': '06-28-2011 19:00',
  'pause': True,
  'start': False,
  'time': '19:00'},
 {'activities': ['bavaria', 'com', 'demo'],
  'activity': 'bavaria :: com :: demo',
  'date': '06-28-2011',
  'datetime': '06-28-2011 18:30',
  'pause': False,
  'start': False,
  'time': '18:30'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-28-2011',
  'datetime': '06-28-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'},
 {'activities': ['bavaria', 'com', 'demo and research'],
  'activity': 'bavaria :: com :: demo and research',
  'date': '06-27-2011',
  'datetime': '06-27-2011 17:28',
  'pause': False,
  'start': False,
  'time': '17:28'},
 {'activities': ['knmp', 'nl', 'script'],
  'activity': 'knmp :: nl :: script',
  'date': '06-27-2011',
  'datetime': '06-27-2011 11:25',
  'pause': False,
  'start': False,
  'time': '11:25'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-27-2011',
  'datetime': '06-27-2011 09:43',
  'pause': False,
  'start': False,
  'time': '09:43'},
 {'activities': ['at', 'issue 612 en 613'],
  'activity': 'at :: issue 612 en 613',
  'date': '06-23-2011',
  'datetime': '06-23-2011 15:13',
  'pause': False,
  'start': False,
  'time': '15:13'},
 {'activities': ['bavaria', 'com', 'uitzoeken WebGL/Java Applet'],
  'activity': 'bavaria :: com :: uitzoeken WebGL/Java Applet',
  'date': '06-23-2011',
  'datetime': '06-23-2011 10:00',
  'pause': False,
  'start': False,
  'time': '10:00'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-23-2011',
  'datetime': '06-23-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'},
 {'activities': ['knmp', 'nl', 'login removal'],
  'activity': 'knmp :: nl :: login removal',
  'date': '06-22-2011',
  'datetime': '06-22-2011 17:15',
  'pause': False,
  'start': False,
  'time': '17:15'},
 {'activities': ['bavaria', 'com', 'release, overleg'],
  'activity': 'bavaria :: com :: release, overleg',
  'date': '06-22-2011',
  'datetime': '06-22-2011 13:15',
  'pause': False,
  'start': False,
  'time': '13:15'},
 {'activities': ['lunch **'],
  'activity': 'lunch **',
  'date': '06-22-2011',
  'datetime': '06-22-2011 12:45',
  'pause': True,
  'start': False,
  'time': '12:45'},
 {'activities': ['bavaria', 'com', 'release, overleg'],
  'activity': 'bavaria :: com :: release, overleg',
  'date': '06-22-2011',
  'datetime': '06-22-2011 12:30',
  'pause': False,
  'start': False,
  'time': '12:30'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-22-2011',
  'datetime': '06-22-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'},
 {'activities': ['bavaria', 'com', 'issue pubfacts'],
  'activity': 'bavaria :: com :: issue pubfacts',
  'date': '06-21-2011',
  'datetime': '06-21-2011 23:59',
  'pause': False,
  'start': False,
  'time': '23:59'},
 {'activities': ['diner **'],
  'activity': 'diner **',
  'date': '06-21-2011',
  'datetime': '06-21-2011 20:15',
  'pause': True,
  'start': False,
  'time': '20:15'},
 {'activities': ['bavaria', 'com', 'issue pubfacts'],
  'activity': 'bavaria :: com :: issue pubfacts',
  'date': '06-21-2011',
  'datetime': '06-21-2011 18:15',
  'pause': False,
  'start': False,
  'time': '18:15'},
 {'activities': ['lunch **'],
  'activity': 'lunch **',
  'date': '06-21-2011',
  'datetime': '06-21-2011 12:45',
  'pause': True,
  'start': False,
  'time': '12:45'},
 {'activities': ['bavaria', 'com', 'issue pubfacts'],
  'activity': 'bavaria :: com :: issue pubfacts',
  'date': '06-21-2011',
  'datetime': '06-21-2011 12:30',
  'pause': False,
  'start': False,
  'time': '12:30'},
 {'activities': ['__start_'],
  'activity': '__start_',
  'date': '06-21-2011',
  'datetime': '06-21-2011 09:15',
  'pause': False,
  'start': False,
  'time': '09:15'},
 {'activities': ['bavaria', 'com', 'issue 91'],
  'activity': 'bavaria :: com :: issue 91',
  'date': '06-20-2011',
  'datetime': '06-20-2011 16:07',
  'pause': False,
  'start': False,
  'time': '16:07'},
 {'activities': ['knmp', 'sfk', 'meeting'],
  'activity': 'knmp :: sfk :: meeting',
  'date': '06-20-2011',
  'datetime': '06-20-2011 10:48',
  'pause': False,
  'start': False,
  'time': '10:48'},
 {'activities': ['zeelandia', 'sync'],
  'activity': 'zeelandia :: sync',
  'date': '06-20-2011',
  'datetime': '06-20-2011 09:40',
  'pause': False,
  'start': False,
  'time': '09:40'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-20-2011',
  'datetime': '06-20-2011 09:16',
  'pause': False,
  'start': False,
  'time': '09:16'},
 {'activities': ['bavaria', 'com', 'issue 94'],
  'activity': 'bavaria :: com :: issue 94',
  'date': '06-17-2011',
  'datetime': '06-17-2011 20:07',
  'pause': False,
  'start': False,
  'time': '20:07'},
 {'activities': ['bavaria', 'com', 'issue 89'],
  'activity': 'bavaria :: com :: issue 89',
  'date': '06-17-2011',
  'datetime': '06-17-2011 20:07',
  'pause': False,
  'start': False,
  'time': '20:07'},
 {'activities': ['bavaria', 'com', 'issue 91'],
  'activity': 'bavaria :: com :: issue 91',
  'date': '06-17-2011',
  'datetime': '06-17-2011 12:15',
  'pause': False,
  'start': False,
  'time': '12:15'},
 {'activities': ['bavaria', 'com', 'issue 89'],
  'activity': 'bavaria :: com :: issue 89',
  'date': '06-17-2011',
  'datetime': '06-17-2011 11:45',
  'pause': False,
  'start': False,
  'time': '11:45'},
 {'activities': ['bavaria', 'com', 'issue 105'],
  'activity': 'bavaria :: com :: issue 105',
  'date': '06-17-2011',
  'datetime': '06-17-2011 10:00',
  'pause': False,
  'start': False,
  'time': '10:00'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-17-2011',
  'datetime': '06-17-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'},
 {'activities': ['at', 'issue 624'],
  'activity': 'at :: issue 624',
  'date': '06-16-2011',
  'datetime': '06-16-2011 17:15',
  'pause': False,
  'start': False,
  'time': '17:15'},
 {'activities': ['at', 'issue 593'],
  'activity': 'at :: issue 593',
  'date': '06-16-2011',
  'datetime': '06-16-2011 16:45',
  'pause': False,
  'start': False,
  'time': '16:45'},
 {'activities': ['at', 'issue 323'],
  'activity': 'at :: issue 323',
  'date': '06-16-2011',
  'datetime': '06-16-2011 16:15',
  'pause': False,
  'start': False,
  'time': '16:15'},
 {'activities': ['at', 'issue 549'],
  'activity': 'at :: issue 549',
  'date': '06-16-2011',
  'datetime': '06-16-2011 15:45',
  'pause': False,
  'start': False,
  'time': '15:45'},
 {'activities': ['at', 'issue 613'],
  'activity': 'at :: issue 613',
  'date': '06-16-2011',
  'datetime': '06-16-2011 13:15',
  'pause': False,
  'start': False,
  'time': '13:15'},
 {'activities': ['lunch **'],
  'activity': 'lunch **',
  'date': '06-16-2011',
  'datetime': '06-16-2011 12:45',
  'pause': True,
  'start': False,
  'time': '12:45'},
 {'activities': ['at', 'issue 613'],
  'activity': 'at :: issue 613',
  'date': '06-16-2011',
  'datetime': '06-16-2011 12:30',
  'pause': False,
  'start': False,
  'time': '12:30'},
 {'activities': ['at', 'issue 566'],
  'activity': 'at :: issue 566',
  'date': '06-16-2011',
  'datetime': '06-16-2011 10:30',
  'pause': False,
  'start': False,
  'time': '10:30'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-16-2011',
  'datetime': '06-16-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'},
 {'activities': ['bavaria', 'com', 'issue 105'],
  'activity': 'bavaria :: com :: issue 105',
  'date': '06-15-2011',
  'datetime': '06-15-2011 17:15',
  'pause': False,
  'start': False,
  'time': '17:15'},
 {'activities': ['vvv', 'patch'],
  'activity': 'vvv :: patch',
  'date': '06-15-2011',
  'datetime': '06-15-2011 15:15',
  'pause': False,
  'start': False,
  'time': '15:15'},
 {'activities': ['nuffic', 'issues'],
  'activity': 'nuffic :: issues',
  'date': '06-15-2011',
  'datetime': '06-15-2011 13:15',
  'pause': False,
  'start': False,
  'time': '13:15'},
 {'activities': ['lunch **'],
  'activity': 'lunch **',
  'date': '06-15-2011',
  'datetime': '06-15-2011 12:45',
  'pause': True,
  'start': False,
  'time': '12:45'},
 {'activities': ['nuffic', 'issues'],
  'activity': 'nuffic :: issues',
  'date': '06-15-2011',
  'datetime': '06-15-2011 12:30',
  'pause': False,
  'start': False,
  'time': '12:30'},
 {'activities': ['fenelab', 'style fix and release'],
  'activity': 'fenelab :: style fix and release',
  'date': '06-15-2011',
  'datetime': '06-15-2011 10:30',
  'pause': False,
  'start': False,
  'time': '10:30'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-15-2011',
  'datetime': '06-15-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'},
 {'activities': ['at', 'issue 612'],
  'activity': 'at :: issue 612',
  'date': '06-14-2011',
  'datetime': '06-14-2011 17:45',
  'pause': False,
  'start': False,
  'time': '17:45'},
 {'activities': ['lunch **'],
  'activity': 'lunch **',
  'date': '06-14-2011',
  'datetime': '06-14-2011 12:45',
  'pause': True,
  'start': False,
  'time': '12:45'},
 {'activities': ['at', 'issue 612'],
  'activity': 'at :: issue 612',
  'date': '06-14-2011',
  'datetime': '06-14-2011 12:30',
  'pause': False,
  'start': False,
  'time': '12:30'},
 {'activities': ['at', 'overleg'],
  'activity': 'at :: overleg',
  'date': '06-14-2011',
  'datetime': '06-14-2011 10:00',
  'pause': False,
  'start': False,
  'time': '10:00'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-14-2011',
  'datetime': '06-14-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'},
 {'activities': ['pareto', 'feestdag'],
  'activity': 'pareto :: feestdag',
  'date': '06-13-2011',
  'datetime': '06-13-2011 17:00',
  'pause': False,
  'start': False,
  'time': '17:00'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-13-2011',
  'datetime': '06-13-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'},
 {'activities': ['bavaria', 'com', 'beer selector'],
  'activity': 'bavaria :: com :: beer selector',
  'date': '06-10-2011',
  'datetime': '06-10-2011 21:00',
  'pause': False,
  'start': False,
  'time': '21:00'},
 {'activities': ['diner **'],
  'activity': 'diner **',
  'date': '06-10-2011',
  'datetime': '06-10-2011 19:00',
  'pause': True,
  'start': False,
  'time': '19:00'},
 {'activities': ['bavaria', 'com', 'beer selector'],
  'activity': 'bavaria :: com :: beer selector',
  'date': '06-10-2011',
  'datetime': '06-10-2011 17:00',
  'pause': False,
  'start': False,
  'time': '17:00'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-10-2011',
  'datetime': '06-10-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'},
 {'activities': ['bavaria', 'com', 'pub facts'],
  'activity': 'bavaria :: com :: pub facts',
  'date': '06-09-2011',
  'datetime': '06-09-2011 21:00',
  'pause': False,
  'start': False,
  'time': '21:00'},
 {'activities': ['diner **'],
  'activity': 'diner **',
  'date': '06-09-2011',
  'datetime': '06-09-2011 19:00',
  'pause': True,
  'start': False,
  'time': '19:00'},
 {'activities': ['bavaria', 'com', 'quality'],
  'activity': 'bavaria :: com :: quality',
  'date': '06-09-2011',
  'datetime': '06-09-2011 17:00',
  'pause': False,
  'start': False,
  'time': '17:00'},
 {'activities': ['bavaria', 'com', 'tricoid link and rotation'],
  'activity': 'bavaria :: com :: tricoid link and rotation',
  'date': '06-09-2011',
  'datetime': '06-09-2011 13:00',
  'pause': False,
  'start': False,
  'time': '13:00'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-09-2011',
  'datetime': '06-09-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'},
 {'activities': ['bavaria', 'com', 'tricoid link and rotation'],
  'activity': 'bavaria :: com :: tricoid link and rotation',
  'date': '06-08-2011',
  'datetime': '06-08-2011 17:00',
  'pause': False,
  'start': False,
  'time': '17:00'},
 {'activities': ['bavaria', 'com', 'background blue'],
  'activity': 'bavaria :: com :: background blue',
  'date': '06-08-2011',
  'datetime': '06-08-2011 16:00',
  'pause': False,
  'start': False,
  'time': '16:00'},
 {'activities': ['bavaria', 'com', 'translation'],
  'activity': 'bavaria :: com :: translation',
  'date': '06-08-2011',
  'datetime': '06-08-2011 15:00',
  'pause': False,
  'start': False,
  'time': '15:00'},
 {'activities': ['nuffic', 'issues'],
  'activity': 'nuffic :: issues',
  'date': '06-08-2011',
  'datetime': '06-08-2011 13:00',
  'pause': False,
  'start': False,
  'time': '13:00'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-08-2011',
  'datetime': '06-08-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'},
 {'activities': ['fenelab', 'additional styling'],
  'activity': 'fenelab :: additional styling',
  'date': '06-07-2011',
  'datetime': '06-07-2011 17:00',
  'pause': False,
  'start': False,
  'time': '17:00'},
 {'activities': ['floravontuur', 'issues'],
  'activity': 'floravontuur :: issues',
  'date': '06-07-2011',
  'datetime': '06-07-2011 10:00',
  'pause': False,
  'start': False,
  'time': '10:00'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-07-2011',
  'datetime': '06-07-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'},
 {'activities': ['floravontuur', 'issues'],
  'activity': 'floravontuur :: issues',
  'date': '06-06-2011',
  'datetime': '06-06-2011 17:00',
  'pause': False,
  'start': False,
  'time': '17:00'},
 {'activities': ['start'],
  'activity': 'start',
  'date': '06-06-2011',
  'datetime': '06-06-2011 09:00',
  'pause': False,
  'start': False,
  'time': '09:00'}]