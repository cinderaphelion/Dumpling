#!/usr/bin/python2.7

import cgi
import json
import subprocess
import os

jarpath = '/var/www/direwolf/javaApi/TypeTagJsonGenerator.jar'
tmpfile = 'tmpType.txt'
#resultpath = '/var/www/direwolf/javaApi/'

def main():
    form = cgi.FieldStorage()
    text = form.getvalue('text', '')
    typetext = form.getvalue('type', '')
    dh = open(tmpfile,'w')
    dh.write(typetext+'\n')
    dh.write(text)
    dh.close()
    os.chmod(tmpfile, 0777)
    result_code = subprocess.call(['java', '-jar', jarpath, os.getcwd()+'/'+tmpfile])
    fh = open('typeTagResult.txt','r')
    results = fh.read()
    fh.close()
    #log_handler = open('typelog','w')
    #log_handler.write(results)
    #log_handler.close()
    print 'Content-Type: text/plain\r\n'
    print results

if __name__ == '__main__':
    main()

