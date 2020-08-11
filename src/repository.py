import logging


from app import db

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='document.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

class DocumentList(db.Model):
    """This class represents the documentlist table."""

    __tablename__ = 'documentlists'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=False)

    def save(self):
        logger.info(f'Created document summary: {self.summary}')
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return DocumentList.query.all()
