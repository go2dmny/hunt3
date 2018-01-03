# hunt3
A script that utilizes Pyhunter for collecting business intelligence

To do:
1) Install Python 3
2) pip3 install pyhunter
3) Change code for your own API key from www.hunter.io
4) Change Line 18 for your domain

Use --help for optional switches.
Most common: Use -fe to provide a text file with domains. Must be in format www.domainname.com

Output will be raw text (output.txt).

To grep email addresses use the following line in a terminal:
grep -E -o "\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b" output.txt > emails.txt
