import os, sys
import xml.etree.cElementTree as ET
from nose.tools import *
from nose_parameterized import parameterized
import unittest

cwd = os.path.abspath(os.path.normpath(os.path.dirname(__file__)))
spark_path = os.path.abspath(os.path.join(cwd, '..', 'en-US.xml'))
sut = ET.parse(open(spark_path, 'r'))
root = sut.getroot()

def test_Title():
    eq_(root.attrib['TITLE'], u'Site Administrator for SharePoint\xae 5.2.4')

@parameterized([
'Home',
'Prerequisites',
'Documentation',
'Install',
'Support',
'Free Tools',
'Contact Us'
])
def test_Sections(name):
    assert_in( name, [item.attrib['NAME'] for item in root if item.tag == 'SECTION'] )

def getSection(name):
    return [item for item in root if item.tag == 'SECTION' and item.attrib['NAME'] == name][0]

class testHome:

    def setUp(self):
        self.home = getSection('Home')

    def testIcon(self):
        eq_(self.home.attrib['ICON'], 'home')

    def testType(self):
        eq_(self.home.attrib['TYPE'], 'html')

        
class testPrerequisites:

    def setUp(self):
        self.sut = getSection('Prerequisites')

    def testIcon(self):
        eq_(self.sut.attrib['ICON'], 'prerequisites')

    def testType(self):
        eq_(self.sut.attrib['TYPE'], 'list')

    @parameterized.expand([
    'Read this First',
    'Software Prerequisites'
    ])
    def testGroups(self, group='Read this First' ):
        groups = [item for item in self.sut.iter('GROUP')]
        eq_(len(groups), 2, groups)

class testDocumentation:

    def setUp(self):
        self.sut = getSection('Documentation')

    def testIcon(self):
        eq_(self.sut.attrib['ICON'], 'documentation')

    def testType(self):
        eq_(self.sut.attrib['TYPE'], 'list')

    @parameterized.expand([
    'Online Resources',
    u'Site Administrator for SharePoint\xae Documentation'
    ])
    def testGroups(self, group='Read this First' ):
        groups = [item for item in self.sut.iter('GROUP')]
        eq_(len(groups), 2, groups)
        
        
class testInstall:

    def setUp(self):
        self.sut = getSection('Install')

    def testIcon(self):
        eq_(self.sut.attrib['ICON'], 'install')

    def testType(self):
        eq_(self.sut.attrib['TYPE'], 'list')

    @parameterized.expand([
    'Install'
    ])
    def testGroups(self, group='Read this First' ):
        groups = [item for item in self.sut.iter('GROUP')]
        eq_(len(groups), 1, groups)
                