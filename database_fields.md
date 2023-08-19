# Database Fields

## Wiki
-     page_name = Column(db.String(80), unique=True, nullable=False)
-     page_title = Column(db.String(80), unique=True, nullable=False)
-     content = Column(db.Text, nullable=False)
-     last_edit = dt.utcnow()
