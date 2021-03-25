#!/usr/bin/env python
# coding: utf-8

# ### Install Libraries
# conda install -c conda-forge exchangelib
# 
# ### References
# https://ecederstrand.github.io/exchangelib/

# #### Load Libraries

from datetime import timedelta
from exchangelib import *

# #### Enter Credentials

username = 'Your Email Address'
password = 'Your Password'
sharedmailbox = 'Shared Mail Box' # User must have a member of this mailbox

# #### Create Connection
credentials = Credentials(username, password)
config = Configuration(server='smtp.office365.com', credentials=credentials)
account = Account(primary_smtp_address=sharedmailbox, config=config,
          autodiscover=False, access_type=DELEGATE)


# #### Reading First 100 EMails
for item in account.inbox.all().order_by('-datetime_received')[:100]:
    print(item.subject, item.sender, item.datetime_received)

