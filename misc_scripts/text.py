import smtplib

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP( "smtp.gmail.com", 587 )

server.starttls()

server.login('kuzie.chambers@gmail.com','Kc24962387103!' )

# Send text message through SMS gateway of destination number
server.sendmail('MORG', '9402311617@mms.att.net', 'Howdy pal\nwhats up?' )