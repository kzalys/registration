# HACKATHON PERSONALIZATION
import os

from django.utils import timezone

HACKATHON_NAME = 'GreatUniHack'
# What's the name for the application
HACKATHON_APPLICATION_NAME = 'GreatUniHack registration'
# Hackathon timezone
TIME_ZONE = 'UTC'
# This description will be used on the html and sharing meta tags
HACKATHON_DESCRIPTION = 'HackAssistant is an organization to mantain ' \
                        'a few open-source projects related with hackathon management'
# Domain where application is deployed, can be set by env variable
HACKATHON_DOMAIN = os.environ.get('DOMAIN', 'localhost:8000')
# Hackathon contact email: where should all hackers contact you. It will also be used as a sender for all emails
HACKATHON_CONTACT_EMAIL = 'contact@hacksoc.com'
# Hackathon logo url, will be used on all emails
HACKATHON_LOGO_URL = 'https://scontent-waw1-1.xx.fbcdn.net/v/t1.0-9/16939013_1269791483102772_5192019247591528681_n.png?_nc_cat=0&oh=543c592337a5791be3f24cd82395da42&oe=5C2F2A57'

HACKATHON_OG_IMAGE = 'https://hackcu.org/img/hackcu_ogimage870x442.png'
# (OPTIONAL) Track visits on your website
# HACKATHON_GOOGLE_ANALYTICS = 'UA-7777777-2'
# (OPTIONAL) Hackathon twitter user
HACKATHON_TWITTER_ACCOUNT = 'greatunihack'
# (OPTIONAL) Hackathon Facebook page
HACKATHON_FACEBOOK_PAGE = 'GreatUniHack'
# (OPTIONAL) Github Repo for this project (so meta)
HACKATHON_GITHUB_REPO = 'https://github.com/kzalys/registration/'

# (OPTIONAL) Applications deadline
# HACKATHON_APP_DEADLINE = timezone.datetime(2018, 2, 24, 3, 14, tzinfo=timezone.pytz.timezone(TIME_ZONE))
# (OPTIONAL) When to arrive at the hackathon
HACKATHON_ARRIVE = 'Registration opens at 3:00 PM and closes at 6:00 PM on Friday October 13th, ' \
                   'the opening ceremony will be at 7:00 pm.'

# (OPTIONAL) When to arrive at the hackathon
HACKATHON_LEAVE = 'Closing ceremony will be held on Sunday October 15th from 3:00 PM to 5:00 PM. ' \
                  'However the projects demo fair will be held in the morning from 10:30 AM to 1 PM.'
# (OPTIONAL) Hackathon live page
# HACKATHON_LIVE_PAGE = 'https://gerard.space/live'

# (OPTIONAL) Regex to automatically match organizers emails and set them as organizers when signing up
REGEX_HACKATHON_ORGANIZER_EMAIL = '^.*@gerard\.space$'

# (OPTIONAL) Sends 500 errors to email whilst in production mode.
HACKATHON_DEV_EMAILS = []

# Reimbursement configuration
REIMBURSEMENT_ENABLED = True
CURRENCY = '£'
REIMBURSEMENT_EXPIRY_DAYS = 5
REIMBURSEMENT_REQUIREMENTS = 'You have to submit a project and demo it during the event in order to get reimbursed'
REIMBURSEMENT_DEADLINE = timezone.datetime(2018, 2, 24, 3, 14, tzinfo=timezone.pytz.timezone(TIME_ZONE))

# (OPTIONAL) Max team members. Defaults to 4
TEAMS_ENABLED = True
HACKATHON_MAX_TEAMMATES = 4

# (OPTIONAL) Slack credentials
# Highly recommended to create a separate user account to extract the token from
SLACK = {
    'team': os.environ.get('SL_TEAM', 'test'),
    # Get it here: https://api.slack.com/custom-integrations/legacy-tokens
    'token': os.environ.get('SL_TOKEN', None)
}

# (OPTIONAL) Logged in cookie
# This allows to store an extra cookie in the browser to be shared with other application on the same domain
LOGGED_IN_COOKIE_DOMAIN = '.gerard.space'
LOGGED_IN_COOKIE_KEY = 'hackassistant_logged_in'
