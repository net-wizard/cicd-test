try:
    from app import app
    import unittest

except Exception as e:
    print("Some modules are missing {} ".format(e))

class FlaskTest(unittest.TestCase):
    #check for response  200
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/',content_type='html')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    
if __name__== "__main__":
    unittest.main()