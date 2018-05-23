import datetime
import pytz

#not timezone aware
#pass integers, no leading zeros
d = datetime.date(2016, 7, 24)

#get today's curent local date
today = datetime.date.today()

#today.year
#today.month
#today.day

# <--------------------------------------------------------------------------->
#today.weekday()
#Monday = 0 Sunday = 6


#today.isoweekday()
#Monday = 1 Sunday = 7

#calculate time change
#tdelta = datetime.timedelta(days=7)
# print(today + tdelta) <-- adds 7 days to current local date



# <--------------------------------------------------------------------------->

# .today() returns current local datetime with timezone = None
#dt_today = datetime.datetime.today()


# .now() gives option to pass in timezone
#dt_now = datetime.datetime.now(tz=pytz.UTC)


# .utcnow() still must explicitly set timezone
#dt_utcnow = datetime.datetime.utcnow()
#dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=ptz.UTC)

#example of how to change timezone to mountain time
#dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))

#pip install pytz 

#dt = datetime.datetime(2016, 7, 26, 12, 36, 45, tzinfo=pytz.UTC)

#to see all timezones
#for tz in pytz.all_timezones:
    #print tz


# <--------------------------------------------------------------------------->

#make naive datetime timezone aware

# .now() not timezone aware
#dt_mtn = datetime.datetime.now()

# instantiate a timezone var
#mtn_tz = pytz.timezone('US/Mountain')

# run .localize() to make timezone aware
#dt_mtn = mtn_tz.localize(dt_mtn)

# <--------------------------------------------------------------------------->
#displaying datetime

# this format is an international standard
#print dt_mtn.isoformat()

#print dt_mtn.strftime('%B' %d, %Y)
# %B = full month
# %d = 2 digit day
# %Y = full year
# ex: July 26, 2018

#convert str to dt to perform methods/functions
#dt_str = 'July 26, 2018'

#dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')

#strftime - Datetime to string
#strptime - String to Datetime








