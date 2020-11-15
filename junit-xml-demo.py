import sys

def isPython2():
    version = sys.version
    return version.startswith('2.')

import junit_xml

class Testcase (junit_xml.TestCase):
    Count = 0
    def __init__(self, description):
        self.tcId = Testcase.Count
        Testcase.Count += 1

        self.description = description

        if (isPython2()):
            super(Testcase, self).__init__(name=description)
        else:
            super().__init__(name=description)

    def execute(self):
        if (3 != self.tcId):
            self.add_failure_info('Test is failed', 'Value: {0:d} | Expected: {1:d}'.format(self.tcId, 3), 'Values are mismatched!')

class Testsuite (junit_xml.TestSuite):
    Count = 0
    def __init__(self, description):
        self.tsId = Testsuite.Count
        Testsuite.Count += 1

        self.description = description
        if (isPython2()):
            super(Testsuite, self).__init__(name=description)
        else:
            super().__init__(name=description)

    def addTestcase(self, testcase):
        self.test_cases.append(testcase)

    def execute(self):
        for tc in self.test_cases:
            tc.execute()

tc0 = Testcase('Testcase 0')
tc1 = Testcase('Testcase 1')
tc2 = Testcase('Testcase 2')
tc3 = Testcase('Testcase 3')
tc4 = Testcase('Testcase 4')

testsuites = []
testsuites.append(Testsuite('Testsuite 0'))
testsuites.append(Testsuite('Testsuite 1'))

testsuites[0].addTestcase(tc0)
testsuites[0].addTestcase(tc1)
testsuites[1].addTestcase(tc2)
testsuites[1].addTestcase(tc3)
testsuites[1].addTestcase(tc4)

testsuites[0].execute()
testsuites[1].execute()

print(junit_xml.TestSuite.to_xml_string(testsuites))
