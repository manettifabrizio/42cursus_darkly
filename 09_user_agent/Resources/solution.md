# 00_hidden_input

## Instructions to reproduce

On the albatross page, we can see comments like : `from https://nsa.gov/` and "use browser ft_bornToSec".
To exploit we'll do a curl command :

`curl --user-agent "ft_bornToSec" http://192.168.64.13/index.php\?page\=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f --referer "https://www.nsa.gov/"`

## How to prevent 

Just check the user-agent with HTTPS request.
