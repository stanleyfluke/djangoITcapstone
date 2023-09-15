from django.db import models
from django.utils import timezone

# Create your models here.
# Database model based on schema_creation.sql
class User(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.TextField()
    contact = models.TextField()

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    teamLead = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    teamName = models.TextField()

class InTeam(models.Model):
    id = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    teamID = models.ForeignKey(Team, on_delete=models.CASCADE)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    categoryName = models.TextField()
    parentCategory = models.ForeignKey('self', null=True,on_delete=models.CASCADE)

class Record(models.Model):
    id = models.AutoField(primary_key=True)
    isDeleted = models.BooleanField()
    status = models.TextField()
    creationTime = models.DateTimeField(default=timezone.now)
    recordCreator = models.TextField()
    recordOwner = models.TextField()
    technicalTeam = models.TextField()
    subsystem = models.TextField()
    carYear = models.TextField()
    failureTime = models.DateTimeField()
    failureTitle = models.TextField()
    failureDescription = models.TextField()
    failureImpact = models.TextField()
    failureCause = models.TextField()
    failureMechanism = models.TextField()
    responseActionPlan = models.TextField()
    correctiveActionPlan = models.TextField()
    resolutionStatus = models.TextField()
    teamLead = models.TextField()
    reviewDate = models.DateTimeField()
    reportCreationTime = models.DateTimeField()
    dueDate = models.DateTimeField()
    isResolved = models.BooleanField()
    resolveDate = models.DateTimeField()
    isRecordValidated = models.BooleanField()
    isAnalysisValidated = models.BooleanField()
    isCorrectionValidated = models.BooleanField()
    isReviewed = models.BooleanField()
    category = models.TextField()
    subcategory = models.TextField()

class UserRecordMapping(models.Model):
    id = models.AutoField(primary_key=True)
    userID = models.ForeignKey('User', on_delete=models.CASCADE)
    recordID = models.ForeignKey('Record', on_delete=models.CASCADE)
    mappingType = models.IntegerField()
    creationTime = models.DateTimeField(default=timezone.now)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    recordID = models.ForeignKey(Record, on_delete=models.CASCADE)
    parentCommentID = models.ForeignKey('self', on_delete=models.CASCADE)
    commenter = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    creationTime = models.DateTimeField(default=timezone.now)
    commentText = models.TextField()