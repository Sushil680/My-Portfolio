import unittest
import json
from app import app

class PortfolioAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_home_page(self):
        """Test GET / loads successfully and contains key content."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sushil Nath Yogi', response.data)
        self.assertIn(b'Portfolio', response.data)
        self.assertIn(b'section-about', response.data)
        self.assertIn(b'section-contact', response.data)

    def test_static_assets(self):
        """Test that static images and CV PDF can be served without 404."""
        assets_to_test = [
            '/static/assets/favicon.ico',
            '/static/assets/cv.pdf',
            '/static/assets/images/1.jpg',
            '/static/assets/images/2.jpg',
            '/static/assets/images/3.jpg',
            '/static/assets/images/4.jpg',
            '/static/assets/images/5.jpg',
            '/static/assets/images/6.jpg',
            '/static/assets/images/my.jpg',
            '/static/assets/images/image_1.jpg',
            '/static/custom.js',
            '/static/style.css',
        ]
        for asset in assets_to_test:
            res = self.client.get(asset)
            self.assertEqual(res.status_code, 200, f"Asset failed to load: {asset}")

    def test_404_page(self):
        """Test 404 handler returns 404 template with return button."""
        response = self.client.get('/this-page-does-not-exist')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'404', response.data)
        self.assertIn(b'Return to Portfolio', response.data)

    def test_submit_form_post_standard(self):
        """Test standard form POST submission and redirect."""
        payload = {
            'name': 'Test User',
            'email': 'tester@example.com',
            'message': 'Hello from test suite!'
        }
        response = self.client.post('/submit_form', data=payload, follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/#section-contact', response.location)

    def test_submit_form_post_ajax(self):
        """Test AJAX form POST returns JSON response."""
        payload = {
            'name': 'Test User',
            'email': 'tester@example.com',
            'message': 'Hello via AJAX test!'
        }
        response = self.client.post(
            '/submit_form',
            data=payload,
            headers={'X-Requested-With': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data.get('status'), 'success')
        self.assertIn('Thank you', data.get('message'))

    def test_submit_form_validation(self):
        """Test validation fails when required fields are missing."""
        payload = {
            'name': '',
            'email': 'not-an-email',
            'message': ''
        }
        response = self.client.post(
            '/submit_form',
            data=payload,
            headers={'X-Requested-With': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data.get('status'), 'error')

if __name__ == '__main__':
    unittest.main()
