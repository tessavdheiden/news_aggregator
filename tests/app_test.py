import unittest
import json


from app import create_app
from app import db


class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.text = 'In an attempt to build an AI-ready workforce, Microsoft announced Intelligent Cloud Hub which has been launched to empower the next generation of students with AI-ready skills. Envisioned as a three-year collaborative program, Intelligent Cloud Hub will support around 100 institutions with AI infrastructure, course content and curriculum, developer support, development tools and give students access to cloud and AI services. As part of the program, the Redmond giant which wants to expand its reach and is planning to build a strong developer ecosystem in India with the program will set up the core AI infrastructure and IoT Hub for the selected campuses. The company will provide AI development tools and Azure AI services such as Microsoft Cognitive Services, Bot Services and Azure Machine Learning.According to Manish Prakash, Country General Manager-PS, Health and Education, Microsoft India, said, With AI being the defining technology of our time, it is transforming lives and industry and the jobs of tomorrow will require a different skillset. This will require more collaborations and training and working with AI. That’s why it has become more critical than ever for educational institutions to integrate new cloud and AI technologies. The program is an attempt to ramp up the institutional set-up and build capabilities among the educators to educate the workforce of tomorrow. The program aims to build up the cognitive skills and in-depth understanding of developing intelligent cloud connected solutions for applications across industry. Earlier in April this year, the company announced Microsoft Professional Program In AI as a learning track open to the public. The program was developed to provide job ready skills to programmers who wanted to hone their skills in AI and data science with a series of online courses which featured hands-on labs and expert instructors as well. This program also included developer-focused AI school that provided a bunch of assets to help build AI skills.'

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_documentlist_creation(self):
        """Test API can create a documentlist (POST request)"""
        res = self.client().post('/api/documents/', json={'text': self.text})
        self.assertEqual(res.status_code, 201)
        self.assertIn('id', str(res.data))

    def test_api_can_get_all_documentlists(self):
        """Test API can get a documentlist (GET request)."""
        res = self.client().post('/api/documents/', json={'text': self.text})
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/api/documents/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Microsoft', str(res.data))
        self.assertIn('AI', str(res.data))

    def test_api_can_get_document_by_id(self):
        """Test API can get a single document by using it's id."""
        rv = self.client().post('/api/documents/', json={'text': self.text})
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(f'/api/documents/{result_in_json["id"]}')
        self.assertEqual(result.status_code, 200)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
