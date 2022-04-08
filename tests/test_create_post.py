import base64
import unittest
import app


# WARNING -> NEED FILES 'voyage.jpg' & 'testfile.json' IN THE TEST FOLDER
class MyTestCase(unittest.TestCase):

    def test_base64_image_png_string_should_return_true(self):
        with open("voyage.jpg", "rb") as image_file:
            base64_string = base64.b64encode(image_file.read()).decode('ascii')
            string_img = 'data:image/png;base64,{}'.format(base64_string)
            self.assertEqual(True, app.check_valid_base64_images(string_img))

    def test_base64_json_file_should_return_false(self):
        with open("testfile.json", "rb") as file:
            base64_string = base64.b64encode(file.read()).decode('ascii')
            string_file = 'data:application/json;base64,{}'.format(base64_string)
            self.assertEqual(False, app.check_valid_base64_images(string_file))


if __name__ == '__main__':
    unittest.main()
