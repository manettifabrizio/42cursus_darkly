# 10_traversal_directory

## Instructions to reproduce

On the OWASP documentation, We can see there is Directory Traversal exploit is possible when url looks like : `http://example.com/index.php?file=content`

So we can do the test :

add ../ in the path and there is strange messages like `Wtf?` or `You can DO it !!!  :]` when you add more ../.
  
When this message appear many times, we'll add `/etc/passwd` (as the doc said) and there is the flag !

## How to prevent

To prevent this kind of attack, we can use a whitelist of authorized files and check the path before opening it.
