#!/usr/bin/env python
# Copyright (c) 2009 Noe Nieto <tzicatl@gmail.com>
# Use this script under the GPL v2.0 License.

# Took the first Idea from http://jacobian.org/writing/django-apps-with-buildout/
# Also taking ideas from the pinax buildout
# http://github.com/pinax/pinax-buildout/blob/master/buildout.cfg

import os,sys
def touch(path,contents=""):
    f=open(path,"w")
    f.write(contents)
    f.close()

def wget(url):
    os.system("wget "+url)


print "Django Barebones Buildout "
PROJECT_NAME= raw_input("Please type the name of the directory(no spaces or special chars):")

try:
    os.mkdir(PROJECT_NAME)
except OSError:
    print "Woa!, the directory ",PROJECT_NAME, "Already exists."
    print "I iz coward and refuuzzez do anything elz."
    print "kthnxbye"
    sys.exit(0)

os.chdir(PROJECT_NAME)
touch("LICENSE", "Put the License Here")
touch("README","""**Describe your project Here**
--Run bootstrap.py to create a bin/ directory with the buildout script.
--Then run bin/buildout to make the magic happen
--Later look inside the parts directory, this where django is installed.

""")

wget("http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py")
BUILDOUTCFG ="""
[buildout]
executable=/usr/bin/python2.6
parts = 
    zlib
    PIL
    python
    django

eggs = 
    PIL


# Build zlib for PIL, and PIL so we don not rely on something in the system
[zlib]
recipe = hexagonit.recipe.cmmi
url = http://www.zlib.net/zlib-1.2.3.tar.gz
configure-options = --shared
 
[PIL]
recipe = zc.recipe.egg:custom
egg = PIL
find-links = http://dist.repoze.org/
include-dirs = ${zlib:location}/include
library-dirs = ${zlib:location}/lib
rpath = ${zlib:location}/lib

[python]
recipe = zc.recipe.egg
interpreter = python
eggs = ${buildout:eggs}

[django]
recipe = djangorecipe
version = 1.1.1
eggs = ${buildout:eggs}


"""
touch ("buildout.cfg",BUILDOUTCFG)

SETUPPY='''
#Make modifications to this file.
from setuptools import setup, find_packages

setup(
    name = "%s",
    version = "1.0",
    url = "http://www.iservices.com.mx",
    license = "BSD",
    description = "Django barebones buildout",
    author = "Noe Nieto <tzicatl@gmail.com>",
    packages = find_packages("src"),
    package_dir = {'': "src"},
    install_requires = ["setuptools"],
)
'''%(PROJECT_NAME)

touch ("setup.py",SETUPPY)

print "Finished, take a look at your ", PROJECT_NAME, "directory."
print "Run bootstrap.py to create a bin/ directory with the buildout script."
print "Then run bin/buildout to make the magic happen"
print "Later look inside the parts directory, this where django is installed."
print "Cheers."


