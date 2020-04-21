# lfi-win
Local File Inclusion for windows. This script will grab important files and databases and outputs them. 
Website: https://www.bibikski.com
Twitter: https://www.twitter.com/bibikdev

The location of files array is not created by me, but was copied from this website
https://gracefulsecurity.com/path-traversal-cheat-sheet-windows/

Make sure to change the 'url' varible in the code and include 'http://'. If the website requires a cookie, copy and paste the cookie in the 'c' varible. If the website has any headers, add them in the headers function 'headers={'user-agent' : 'example'}'.
 If you need to slow the script for any reason, like not overloading the server, etc. Please adjust the time varible. This will add time in between requests.

If the script cannot download the content of the page, the output file will include the lfi that worked. This allows you to manually inject the LFI.

If you are using this script for business purposes, i.e. bug bounty, and you obtained one of these files. This would be labeled as critical, since the webuser should not be able to escape the web directory.

This was a really fun project and I hope you guys enjoy it!
Please check out the cheat sheet because the creator took a lot of time to make that.
Thanks for using my script! ~Bibikski
