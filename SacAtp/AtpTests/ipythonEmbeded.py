#!/usr/bin/env python
"""An example of how to embed an IPython shell into a running program.

Please see the documentation in the IPython.Shell module for more details.

The accompanying file embed_class_short.py has quick code fragments for
embedding which you can cut and paste in your code once you understand how
things work.

The code in this file is deliberately extra-verbose, meant for learning."""
from __future__ import print_function

# The basics to get you going:

# IPython injects get_ipython into builtins, so you can know if you have nested
# copies running.

# Try running this code both at the command line and from inside IPython (with
# %run example-embed.py)
#from traitlets.config.loader import Config
#from IPython import Config
#try:
#    get_ipython
#except NameError:
#    nested = 0
#    cfg = Config()
#    prompt_config = cfg.PromptManager
#    prompt_config.in_template = 'In <\\#>: '
#    prompt_config.in2_template = '   .\\D.: '
#    prompt_config.out_template = 'Out<\\#>: '
#else:
#    print("Running nested copies of IPython.")
#    print("The prompts for the nested copy have been modified")
#    cfg = Config()
#    nested = 1

## First import the embeddable shell class
#from IPython.terminal.embed import InteractiveShellEmbed

# Now create an instance of the embeddable shell. The first argument is a
# string with options exactly as you would type them if you were starting
# IPython at the system command line. Any parameters you want to define for
# configuration can thus be specified here.
#ipshell = InteractiveShellEmbed(config=cfg,
#                       banner1 = 'Dropping into IPython',
#                       exit_msg = 'Leaving Interpreter, back to program.')

## Make a second instance, you can have as many as you want.
#cfg2 = cfg.copy()
#prompt_config = cfg2.PromptManager
#prompt_config.in_template = 'In2<\\#>: '
#if not nested:
#    prompt_config.in_template = 'In2<\\#>: '
#    prompt_config.in2_template = '   .\\D.: '
#    prompt_config.out_template = 'Out<\\#>: '
#ipshell2 = InteractiveShellEmbed(config=cfg,
#                        banner1 = 'Second IPython instance.')

#print('\nHello. This is printed from the main controller program.\n')

# You can then call ipshell() anywhere you need it (with an optional
# message):
#ipshell('***Called from top level. '
#        'Hit Ctrl-D to exit interpreter and continue program.\n'
#        'Note that if you use %kill_embedded, you can fully deactivate\n'
#        'This embedded instance so it will never turn on again')

#print('\nBack in caller program, moving along...\n')

#---------------------------------------------------------------------------
# More details:

# InteractiveShellEmbed instances don't print the standard system banner and
# messages. The IPython banner (which actually may contain initialization
# messages) is available as get_ipython().banner in case you want it.

# InteractiveShellEmbed instances print the following information everytime they
# start:

# - A global startup banner.

# - A call-specific header string, which you can use to indicate where in the
# execution flow the shell is starting.

# They also print an exit message every time they exit.

# Both the startup banner and the exit message default to None, and can be set
# either at the instance constructor or at any other time with the
# by setting the banner and exit_msg attributes.

# The shell instance can be also put in 'dummy' mode globally or on a per-call
# basis. This gives you fine control for debugging without having to change
# code all over the place.

# The code below illustrates all this.


# This is how the global banner and exit_msg can be reset at any point
#ipshell2.banner = 'Entering interpreter - New Banner'
#ipshell2.exit_msg = 'Leaving interpreter - New exit_msg'

#def foo(m):
#    s = 'spam'
#    ipshell2('***In foo(). Try whos, or print s or m:')
#    print('foo says m = ',m)

#def bar(n):
#    s = 'eggs'
#    ipshell2('***In bar(). Try %whos, or print s or n:')
#    print('bar says n = ',n)
    
## Some calls to the above functions which will trigger IPython:
#print('Main program calling foo("eggs")\n')
#foo('eggs')

## The shell can be put in 'dummy' mode where calls to it silently return. This
## allows you, for example, to globally turn off debugging for a program with a
## single call.
#ipshell.dummy_mode = True
#print('\nTrying to call IPython which is now "dummy":')
#ipshell()
#print('Nothing happened...')
## The global 'dummy' mode can still be overridden for a single call
#print('\nOverriding dummy mode manually:')
#ipshell(dummy=False)

## Reactivate the IPython shell
#ipshell.dummy_mode = False

#print('You can even have multiple embedded instances:')
#ipshell2()

#print('\nMain program calling bar("spam")\n')
#bar('spam')

#print('Main program finished. Bye!')


"""Quick code snippets for embedding IPython into other programs.

See embed_class_long.py for full details, this file has the bare minimum code for
cut and paste use once you understand how to use the system."""

#---------------------------------------------------------------------------
# This code loads IPython but modifies a few things if it detects it's running
# embedded in another IPython session (helps avoid confusion)

try:
    get_ipython
except NameError:
    banner=exit_msg=''
else:
    banner = '*** Nested interpreter ***'
    exit_msg = '*** Back in main IPython ***'
import IPython
from IPython.lib.demo import Demo
IPython.start_ipython([r'C:\Users\admin\Source\Repos\PythonProjects\SacAtp\SacAtp\SacAtp\DirectTestsList.py'])

#mydemo = Demo(r'C:\Users\admin\Source\Repos\PythonProjects\SacAtp\SacAtp\SacAtp\ex_demo.py')
# First import the embed function
#from IPython.terminal.embed import InteractiveShellEmbed
## Now create the IPython shell instance. Put ipshell() anywhere in your code
## where you want it to open.
#ipshell = InteractiveShellEmbed(banner1=banner, exit_msg=exit_msg)

##---------------------------------------------------------------------------
## This code will load an embeddable IPython shell always with no changes for
## nested embededings.

#from IPython import embed
## Now embed() will open IPython anywhere in the code.

##---------------------------------------------------------------------------
## This code loads an embeddable shell only if NOT running inside
## IPython. Inside IPython, the embeddable shell variable ipshell is just a
## dummy function.

#try:
#    get_ipython
#except NameError:
#    from IPython.terminal.embed import InteractiveShellEmbed
#    ipshell = InteractiveShellEmbed()
#    # Now ipshell() will open IPython anywhere in the code
#else:
#    # Define a dummy ipshell() so the same code doesn't crash inside an
#    # interactive IPython
#    def ipshell(): pass

