from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class VideoDetail(db.Model):
    __tablename__ = 'video_details'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    published_at = db.Column(db.DateTime, nullable=False)
    channel_title = db.Column(db.String(255), nullable=False)
    view_count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<VideoDetail {self.title}: {self.view_count} views>"

