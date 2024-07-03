from taskmanager import db


# create 2 separate tables represented by class-based models using SQLAlchemy's ORM
# table 1 for various categories
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True) #unique id acting as our primary key
    category_name = db.Column(db.String(25), unique=True, nullable=False) # nullable for required field
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True) #
    
    
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


# table 2 for task
class Task(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     task_name = db.Column(db.String(50), unique=True, nullable=False) # string similar to inputs
     task_description = db.Column(db.Text, nullable=False) #text is similar to textarea vs inputs
     is_urgent = db.Column(db.Boolean, default=False, nullable=False)
     due_date = db.Column(db.Date, nullable=False) # to include datetime use db.DateTime or db.Time
     category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
