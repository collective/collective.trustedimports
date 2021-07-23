icalendar
=========

I can import html2text, it's helper function and it's class

>>> teval("import html2text")

>>> teval("from html2text import html2text")

>>> teval("from html2text import HTML2Text")

I can use the html2text helper function

#>>> import pdb; pdb.set_trace()

>>> teval("""import html2text; return html2text.html2text("<p><strong>Zed's</strong> dead baby, <em>Zed's</em> dead.</p>")""")
u"**Zed's** dead baby, _Zed's_ dead.\n\n"

