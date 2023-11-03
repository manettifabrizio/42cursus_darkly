# 00_hidden_input

## Instructions to reproduce

In the recover page, inspecting with the console we can see that there is a hidden input:

```
<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
```

using the console any value can be injected in the input. We've changed the value and here it is the flag.

## How to prevent

Using input validation and sanitation you can prevent malicious inputs from being processed by the web application.
