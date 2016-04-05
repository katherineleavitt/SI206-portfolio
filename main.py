#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from mailer import Mailer
from mailer import Message
import webapp2
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        self.response.write(template.render())

class EducationHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/education.html')
        self.response.write(template.render())


class WorkHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/work.html')
        self.response.write(template.render())

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render())

    def post(self):
        logging.info("TRYING TO Contact")
        message = Message(From=self.request.get('email'),
                  To="ksleavit@umich.edu")
        message.Subject = self.request.get('subject')
        message.Html = self.request.get('message')

        sender = Mailer('smtp.example.com')
        sender.send(message)

        template = JINJA_ENVIRONMENT.get_template('templates/contacted.html')
        self.response.write(template.render())       


app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/home', HomeHandler),
    ('/education', EducationHandler),
    ('/work', WorkHandler),
    ('/contact', ContactHandler),
    ('/contacted', ContactHandler),
], debug=True)