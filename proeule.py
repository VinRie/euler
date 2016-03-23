"""
ProEule is a commandline tool that initializes a Project Euler workspace for you. 
 - downloads Problem descriptions for all problems
 - creates language specific templates,
 containing the description of the problem as multiline comment
"""

import cStringIO
import os
import re
import pycurl
from cement.core.foundation import CementApp
from cement.utils.misc import init_defaults

defaults = init_defaults('ProEule')
defaults['ProEule']['lang'] = 'none'
defaults['ProEule']['dir'] = ''

class ProEule(CementApp):
    class Meta:
        label = 'ProEule'
        config_defaults = defaults
        arguments_override_config = True

def init():
    """ initializes the repository """
    # general setup
    euler_base_url = 'https://projecteuler.net/problem='
    euler_problem_count = 542
    

    config_dir = app.config.get('ProEule', 'dir')
    
    if not config_dir.startswith('/'):
        config_dir = '/' + config_dir 
   
    if not config_dir.endswith('/'):
        config_dir = config_dir + '/'


    directory_path = os.getcwd() + config_dir

   
    if not os.path.isdir(directory_path):
        print directory_path + ' is not a directory'
        return 

    # language specific setup
    # print app.config.get('ProEule','lang')
    supported_languages = ['ruby', 'python', 'none']
    if app.config.get('ProEule', 'lang') not in supported_languages:
        print "language is not supported. Supported languages are "\
                +  ', '.join(map(str, supported_languages))
        print app.args.print_help()
        return
    else:
        if app.config.get('ProEule', 'lang') == 'python':
            file_ending = '.py'
            comment_begin = '"""'
            comment_end = '"""'
        elif app.config.get('ProEule', 'lang') == 'ruby':
            file_ending = '.rb'
            comment_begin = '=begin'
            comment_end = '=end'
        else:
            file_ending = '.txt'
            comment_begin = ''
            comment_end = ''

    for problem_number in range(1, euler_problem_count+1):
        download_string = euler_base_url \
                + str(problem_number)

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
            content = re.search(\
                r'<div class="problem_content" role="problem">.*</div><br />',\
                content, re.DOTALL).group(0)
        except AttributeError:
            # problem content not found
            print "problem content not found"
            return

        # delete html tags from content
        re_p = re.compile(r'<.*?>')
        content = re_p.sub('', content)
        
        content = comment_begin + '\n' +  content + '\n' + comment_end


        # set the filename
        if problem_number < 10:
            filename = "problem00" + str(problem_number) + file_ending
        elif problem_number < 100:
            filename = "problem0" + str(problem_number) + file_ending
        else:
            filename = "problem" + str(problem_number) + file_ending

        filename = directory_path + filename
        # write to file
        filestream = open(filename, 'w')
        filestream.write(content)
        filestream.close()

        print str(problem_number) + ": created "\
                + str(problem_number)\
                + " from "\
                + str(euler_problem_count)

with ProEule() as app:
    app.args.add_argument('--lang', \
        help='default is none, ruby and python are supported', action='store', dest='lang')
    app.args.add_argument('--dir',\
        help='default is the current working directory.\
        provide path to directory from current directory', action='store', dest='dir')
    app.run()
    init()
