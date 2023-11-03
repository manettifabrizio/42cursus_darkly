# 01_sign_in

## Instructions to reproduce

-   ### Option 1: Bruteforce using Burp Suite

-   ### Option 2: SQL Injection in the Members Area

    In the members area we've noticed that the input was vulnerable to SQL Injection. Using this query we got all the tables with the columns available on the db:

    ```
    1 AND 1=2 UNION SELECT table_name, column_name FROM information_schema.columns
    ```

    we noticed that there was an db_default table in the Meber_Brute_Force db. Using another query we got the users to sign in:

    ```
    1 AND 1=2 UNION SELECT username, password FROM Member_Brute_Force.db_default
    ```

    Decripting password of root user using MD5 we got the password: shadow. We logged in in the sign_in page and we got the flag.

## How to prevent

-   ### Option 1: Bruteforce using Burp Suite

-   ### Option 2: SQL Injection in the Members Area
    
    The preferred option is to use a safe API, which avoids using the interpreter entirely, provides a parameterized interface, or migrates to Object Relational Mapping Tools (ORMs).

    [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)