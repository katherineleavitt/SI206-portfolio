import webapp2
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):

        try:
            logging.info(self.request.path)
            template = JINJA_ENVIRONMENT.get_template('templates/' + self.request.path)
            self.response.write(template.render())
        except:
            logging.info(self.request.path)
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/.*', MainHandler)
], debug=True)
