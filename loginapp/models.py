from django.db import models

# Create your models here.
class asdf(models.Model):
    yourid = models.TextField(null=True)
    name = models.TextField()
    school = models.TextField()
    gender = models.TextField()
    birth = models.TextField()
    hobby = models.TextField()
    mbti = models.TextField()
    kakao = models.TextField()
    
    def generate_filename(self, filename):
        url = "images/%s.png" % (self.yourid)
        return url

    img = models.ImageField(upload_to=generate_filename,blank=True, null=True)


    def __str__(self):
        return self.yourid+" "+self.name+" "+self.school + " "+self.gender + " "+self.birth + " "+self.hobby + " " + self.mbti +" "+ self.yourid + " " + self.kakao