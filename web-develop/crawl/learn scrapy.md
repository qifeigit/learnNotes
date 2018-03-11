#learn scrapy

'  File "/usr/local/lib/python2.7/dist-packages/scrapy/mail.py", line 23, in <module>
    from twisted.mail.smtp import ESMTPSenderFactory
ImportError: No module named mail.smtp
'
in ubuntu ,we can install twisted like this:
'sudo apt-get install  python-twisted-mail'

[Scrapy uses Request and Response objects for crawling web sites.](http://doc.scrapy.org/en/latest/topics/request-response.html)


python爬json
```python
def parse(self, response):
         jsonresponse = json.loads(response.body_as_unicode())

         item = MyItem()
         item["firstName"] = jsonresponse["firstName"]             

         return item

```
