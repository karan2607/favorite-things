Q.) How long did you spend on the coding test below? What would you add to your solution if you had more time? 
If you didn't spend much time on the coding test then use this as an opportunity to explain what you would add.
Ans. -> I spent about 15 minutes for this coding test. I believe I could have removed the "b" which is at the start of the 
second output and just kept the link as the output if I worked a bit more on it.

Q.) What was the most useful feature that was added to the latest version of your chosen language?
Please include a snippet of code that shows how you've used it.
Ans. -> So the lastest version of Python that have worked on is Python 3.6. The most useful feature that they added in that 
according to me was formatted string literals. I used in my Secure Programming project which I have given a brief description about
in my resume. 
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
        
        
Q.) How would you track down a performance issue in production? Have you ever had to do this?
Ans. -> Yes, I have done performance testing for one of my projects. I would use something like Jmeter to check the 
performance regularly and if there is an issue I would get to know about it.
