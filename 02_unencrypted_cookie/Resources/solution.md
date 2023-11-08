# 02 - unencrypted cookie

## Instructions to reproduce

Check the page get a cookie i_am_admin : 68934a3e9455fa72420237eb05902327.
Encrypt this in md5 and here we are.
Now just change the cookie and refresh.

## How to prevent

Don't store your admin cookie in the client side.
And if you do, encrypt it.
Always use HTTPS for your website or application to encrypt data transmitted between the client (browser) and the server.
This includes cookies that are exchanged during the session.
HTTPS ensures that data is encrypted in transit, making it difficult for attackers to intercept sensitive information.
