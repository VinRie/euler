"""
This app initializes a new empty project euler workspace.
- creates problemXXX.txt files
"""
import subprocess
import pycurl
import cStringIO


def init():
    """ initializes the repository """
    euler_base_url = 'https://projecteuler.net/problem='
    euler_problem_count = '542'

    """ download_command =
    'curl https://projecteuler.net/problem='+ euler_problem_count + '
    | sed -n -e \'/problem_content/,/div/ p\''
    """


    download_string = 'https://projecteuler.net/problem='+ euler_problem_count
    sed_regex = '\'/problem_content/,/div/ p\''

#    curl_command = subprocess.Popen(["curl", download_string], \
#           stdout=subprocess.PIPE, shell=False)
   # sed_command = subprocess.check_output(["sed", "-n", "-e", sed_regex],\
    #      stdout=subprocess.PIPE, shell=False)

    buf = cStringIO.StringIO()

    pycurl_command = pycurl.Curl()
    pycurl_command.setopt(pycurl.URL, download_string)
    pycurl_command.setopt(pycurl_command.WRITEFUNCTION, buf.write)
    pycurl_command.perform()

    content = buf.getvalue()

    buf.close()

if __name__ == "__main__":
    init()

