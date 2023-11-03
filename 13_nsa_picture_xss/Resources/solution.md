# 13_nsa_picture_xss

## Instructions to reproduce

In the homepage clicking on the nasa image brings you to a page where the image is shown using an `<object>` html tag. 

Inside the object tag the data tag isn't filtered so is vulnerable to a xss injection through the src parameter in the url. 

I've tried with
```
data:text/html,<script>alert('42');</script>
```

It works but no flag is given. So I've tried to encode it in base64 and we get the flag.
```
data:text/html;base64,PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4=
```

## How to prevent

Can be prevented usign data encoding and input validation.

[Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)