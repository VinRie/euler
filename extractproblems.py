"""
This app initializes a new empty project euler workspace.
- creates problemXXX.txt files
"""

import subprocess
import pycurl
import cStringIO
import re


def init():
    """ initializes the repository """

    euler_base_url = 'https://projecteuler.net/problem='
    euler_problem_count = 542

    for problem_number in range (1, euler_problem_count):
        
        download_string = 'https://projecteuler.net/problem='+ str(problem_number)
    
        # download HTML source with pycurl
        buf = cStringIO.StringIO()
        pycurl_command = pycurl.Curl()
        pycurl_command.setopt(pycurl.URL, download_string)
        # configure pycurl to write downloaded content to buffer
        pycurl_command.setopt(pycurl_command.WRITEFUNCTION, buf.write)
        pycurl_command.perform()
    
        # save HTML content to content variable
        content = buf.getvalue()
        buf.close() # close buffer!
    
        # extract porblem_content dif
        try:
                content = re.search(r'<div class="problem_content" role="problem">.*</div><br />', content, re.DOTALL).group(0)
        except AttributeError:
                # problem content not found
                print "problem content not found" 
                return
    
        # delete html tags from content
        p = re.compile(r'<.*?>')
        content = p.sub('', content)
    
        # set the filename
        if problem_number < 10:
            filename = "problem00" + str(problem_number) + ".txt"
        elif problem_number < 100: 
            filename = "problem0" + str(problem_number) + ".txt"
        else:
            filename = "problem" + str(problem_number) + ".txt"

        # write to file
        f = open( filename, 'w' )
        f.write( content )
        f.close()

        print str(problem_number) + ": created " + str(problem_number) + " from " + str(euler_problem_count)


if __name__ == "__main__":
    init()

