import base64
import sys
from email.mime.text import MIMEText
from googleapiclient import errors


def create_message(sender, to, subject, message_text):
    """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': compat_urlsafe_b64encode(message.as_string())}


def send_message(service, user_id, message):
    """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.Error as error:
        print('An error occurred: %s' % error)

def compat_urlsafe_b64encode(v):
    """A urlsafe ba64encode which is compatible with Python 2 and 3.
    Args:
      v: A string to encode.
    Returns:
      The encoded string.
    """
    if sys.version_info[0] >= 3:  # pragma: NO COVER
        return base64.urlsafe_b64encode(v.encode('UTF-8')).decode('ascii')
    else:
        return base64.urlsafe_b64encode(v)