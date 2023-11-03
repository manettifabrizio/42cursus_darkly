# 06_file_upload

## Instructions to reproduce

In the add image section of the website we uploaded a php script file. Using Burp Suite we intercept the request and change the file type from text/php to image/jpg to avoid website type checks, and we got the flag.

## How to prevent

Use file content-type validation.

[OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html#content-type-validation)
