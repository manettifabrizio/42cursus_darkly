# 03_whatever_admin_pswd

## Instructions to reproduce

In the robot.txt index we can find a /whatever route. This route contains a downloadable file that contains:

```
root:437394baff5aa33daa618be47b75cb49
```

decripting the password using MD5 we get **qwerty@123** password. We tried it in the /admin sign_in and we got the flag.

## How to prevent

Protect you htpasswd. Avoid leaving robot.txt open.
