enroll-sms
==========

Help SF residents find health insurance under the ACA via text message.

Text START to (415) 767-1553 to see a live demo.

deploy
-------
Quick deploy using Heroku and Twilio:

(1) Clone repo

```
$ git clone https://github.com/lippytak/enroll-sms.git
```

(2) Add environment variables in a /.env file

```
TWIL_NUMBER=[TWILIO PHONE NUMBER e.g., +14157671553]
ACCOUNT_SID=[TWILIO ACCOUNT SID]
AUTH_TOKEN=[TWILIO AUTHENTICATION TOKEN]
DATABASE_URL=[OPTIONAL LOCAL PG DB CONNECTION STRING]
```

(3) Create heroku app

```
$ heroku create
```

(4) Set environment variables on heroku: 

```
$ heroku config:add TWIL_NUMBER=[TWILIO PHONE NUMBER e.g., +14157671553]
$ heroku config:add ACCOUNT_SID=[TWILIO ACCOUNT SID]
$ heroku config:add AUTH_TOKEN=[TWILIO AUTHENTICATION TOKEN]
```

(5) Provision heroku database: 

```
$ heroku addons:add heroku-postgresql
```

(6) Push

```
$ git push heroku master
```
