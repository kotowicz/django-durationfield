DurationField
=============

Reusable application for a DurationField in Django.

See http://django-durationfield.readthedocs.org

You are looking at a fork of https://github.com/johnpaulett/django-durationfield.

In this version time durations are interpreted differently: `[[hh:]mm:]ss`.
That is, if you provide:

 - a single number, we assume you mean 'seconds (ss)'.
 - two numbers (delimited by ':'), we assume you mean 'minutes (mm) : seconds (ss)'
 - three numbers (delimited by ':'), we assume you mean 'hours (hh) : minutes (mm) : seconds (ss)'


