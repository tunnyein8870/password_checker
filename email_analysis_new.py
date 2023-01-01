# Script:    email_analysis.py
# Desc:      extracts email addresses and IP numbers from a text file
#                or webpage; for example, from a saved email header
# Author   Petra Lemich Nov2018
#
# IMPORTANT: wget may fetch a byte object, but regex only works with strings

import sys
import urllib.request
import re
# imports your own webpage_get module
import webpage_get as wg


def txtget(filename):
    '''Suitable function doc string here'''
    # open file read-only, get file contents and close
    with open(filename,'r') as email_text:
        file_contents = email_text.read()
    return file_contents


def findIPv4(text):
    '''Suitable function doc string here'''
    ips =  re.findall(r'[0-9][0-9]?[0-9]?\.[0-9][0-9]?[0-9]?\.[0-9][0-9]?[0-9]?\.[0-9][0-9]?[0-9]?',text)  # ... ADD YOUR CODE HERE
    return ips


def findemail(text):
    '''Suitable function doc string here'''
    emails = re.findall(r'[\w+\.]+@[\w+\.]+', text)  # ... ADD YOUR CODE HERE
    return emails


def main():
#     url arguments for testing
#     un-comment one of the following 4 tests at a time
#     sys.argv.append('http://napier.ac.uk/Pages/home.aspx')
#     sys.argv.append('http://asecuritysite.com/email101.txt')
#     sys.argv.append('http://asecuritysite.com/email02.txt')
#     sys.argv.append('email_sampe.txt')
#     Check args
    try:
        entry = 'http://napier.ac.uk/Pages/home.aspx'
        url_link = re.search(r'(https|http|ftp)\:\//(www.)?[\w+\.\/]+',entry)
        file_get = re.search(r'[\w+_-]+\.txt', entry)    
    # GET and analysis web page
        if file_get:
            print(f'{entry} is a text file.')
            emails = txtget(entry)
            sys.argv.append(emails)       
        elif url_link:
            print(f'{entry} is a url.')
            urls = wg.wget(entry) 
            sys.argv.append(urls)
            
        if len(sys.argv) != 2:
            print('[-] Usage: email_analysis URL/filename')
            return 
        # call wget() or txtget() as appropriate
        print('[+] Analysisng %s' %entry)
        print('[+] IP addresses found: ')
        found_ips = findIPv4(sys.argv[1])
        print(found_ips)
        print(f'Total IPs count: {len(found_ips)}')
        print('[+] email addresses found: ')
        found_emails = findemail(sys.argv[1])
        print(found_emails)
        print(f'Total Emails count: {len(found_emails)}')

    except Exception:
        # error trapping goes here
        print('The website cannot fetch contents.')


if __name__ == '__main__':
    main()
