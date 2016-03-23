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
    euler_problem_count = '542'
    download_string = 'https://projecteuler.net/problem='+ euler_problem_count
    
    """ download_command =
    'curl https://projecteuler.net/problem='+ euler_problem_count + '
    | sed -n -e \'/problem_content/,/div/ p\''
   
    curl_command = subprocess.Popen(["curl", download_string], \
        stdout=subprocess.PIPE, shell=False)
    sed_command = subprocess.check_output(["sed", "-n", "-e", sed_regex],\
        stdout=subprocess.PIPE, shell=False)
    sed_regex = '\'/problem_content/,/div/ p\''
  
    """
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

            #match = re.search(r'<p>.*</p>', paragraph, re.DOTALL)
            content = re.search(r'<div class="problem_content" role="problem">.*</div><br />', content, re.DOTALL).group(0)
    except AttributeError:
            # problem content not found
            found = '' # apply your error handling
            print "problem content not found" 
            return

    # delete html tags from content
    p = re.compile(r'<.*?>')
    content = p.sub('', content)

    # debug output
    print content


if __name__ == "__main__":
    init()

