Mimetypes
==========

We can use stdlibs email to work with email attachments

>>> print teval("from email.mime.multipart import MIMEMultipart; msg = MIMEMultipart(); msg.add_header('From', 'blah'); return msg")
From nobody ...
Content-Type: multipart/mixed; boundary="===============...=="
MIME-Version: 1.0
From: blah
<BLANKLINE>
--===============...==
<BLANKLINE>
--===============...==--

>>> print teval("from email.mime.multipart import MIMEMultipart; from email.mime.text import MIMEText; msg = MIMEMultipart(); msg.attach(MIMEText('blah', 'plain')); return msg")
From nobody ...
Content-Type: multipart/mixed; boundary="===============...=="
MIME-Version: 1.0
<BLANKLINE>
--===============...==
Content-Type: text/plain; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
<BLANKLINE>
blah
--===============...==--

>>> print teval("import email; attach=email.mime.base.MIMEBase('application', 'octet-stream'); attach.set_payload('blah'); from email.encoders import encode_base64; encode_base64(attach); return attach")
From nobody ...
Content-Type: application/octet-stream
MIME-Version: 1.0
Content-Transfer-Encoding: base64
<BLANKLINE>
YmxhaA==

#TODO test M2Crypto