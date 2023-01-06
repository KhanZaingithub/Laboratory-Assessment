import unittest
import otp

class TestStringMethods(unittest.TestCase):

    def testcase1(self):
        Email = otp.validate_email('zainulkhan032@gmail.com')
        self.assertEquals(True,Email)

    def testcase2(self):
        size = 4
        OTP = otp.generate_otp()
        self.assertEqual(len(OTP), size)

    def testcase3(self):
        Email = otp.send_mail("8080")
        self.assertEquals(True,Email)

    # def testcase4(self):
    #     size = 4
    #
    #     Email = MYOTP.emailsender
    #     self.assertIn("@", Email)
    #     self.assertIn(".", Email)
    #     self.assertIn("com", Email)
    #
    #     res = MYOTP.otp(4)
    #     self.assertEqual(len(res), size)

if __name__ == '__main__':
    unittest.main()