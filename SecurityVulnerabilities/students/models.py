from django.db import models
from accounts.models import Student

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.IntegerField()
    SUBJECT_CHOICES = (
        ('IC', '計算機概論'),
        ('CN', '計算機網路'),
        ('C', '微積分'),
        ('LN', '線性代數'),
        ('DM', '離散數學'),
        ('P', '程式設計'),
    )
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    grade = models.FloatField()
    
    def __str__(self):
        return self.student.username + '-' + self.subject + '-' + str(self.grade)
    
class Board(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.author.username + '-' + self.content