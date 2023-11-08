# 12_xss

## Instructions to reproduce

In the feedback section, you have a comment textarea and we see we can inject HTML.
`<div><h1>hello</h1></div>`.

After that, we try to inject some script in it like : `<script>alert(1)</script>`

and here you go, you got the flag !

## How to prevent

To prevent this type of HTML Injection, we can use a whitelist of authorized tags and check the input before displaying it.
