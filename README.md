# Mail Sendler
## Project Description
Job test project, send email by fastapi use gmail stmp server.

### Technologies

The project makes use of the following technologies:

- Python 3.11.4
- Docker version 24.0.5
- Docker Compose version v2.17.2
- Python 3.11.4
- FastAPI 0.95.2

## Getting started

#### Prepare ur google account
In the POP/IMAP forwarding section of your Gmail mailbox, switch the IMAP status to enabled.
![imap.png](app%2Fmedia%2Fimap.png)
In the security section of your Google account, enable add Two-Step Verification.
![safety.png](app%2Fmedia%2Fsafety.png)
![two-factor authentication.png](app%2Fmedia%2Ftwo-factor%20authentication.png)
Also, in the two-step verification section at the bottom, create an application password.
![app_password.png](app%2Fmedia%2Fapp_password.png)

#### Clone projects: 

```git clone https://gitlab.com/me4533521/Docker_FastAPI_Mail_sendler.git```

#### Move to directory:

```cd Docker_FastAPI_Mail_sendler/```

#### Add .env file

for example:
```
STMP_USERNAME=your gmail user
STMP_PASSWORD=your app password
```

#### Build image:

```sudo docker-compose build```

#### Run container:

```sudo docker-compose up```

## Usage

#### By FastAPI Docs

```http://127.0.0.1:8000/docs#/```

#### post method:
    http://127.0.0.1:8000/api/send_email

fill in the fields to send a message

#### By Postman

#### post method:

    ```http://127.0.0.1:8000/api/send_email```

#### request body json:

```
{
  "to": "example@mail.ru",
  "subject": "Test email",
  "message": "This is a test email."
}
```

## Test

In folder ```tests```.