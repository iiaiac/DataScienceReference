# Quick Background:
# If you want to download the attachment of an e-mail you received over your outlook application on your machine at a specific date.

# Import Required Libraries and specify the location to download attachments.
import datetime
import os
import win32com.client
import datetime
path = os.path.expanduser(r"Your Path")

# Initialize the application with MAPI
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Specify the folder  default 6 for Inbox
inbox = outlook.GetDefaultFolder(6) 

# Get the Inbox e-mail details
messages = inbox.Items

# Filter and Download the e-mails (in this script, yesterday is set for download)
for i in messages:
    if str(i).find('Report') == 0 & (datetime.datetime.strptime(str(i.Senton.date()), '%Y-%m-%d').date() == (datetime.datetime.today().date()-datetime.timedelta(1))):
        attachments = i.Attachments
        attachment = attachments.Item(1)
        attachment.SaveAsFile(os.path.join(path, str(attachment)))
        print(attachment)

