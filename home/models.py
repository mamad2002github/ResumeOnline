from django.db import models


class Resume(models.Model):
    # اطلاعات شخصی
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    skills = models.TextField(blank=True, help_text="مهارت‌ها را با کاما جدا کنید")
    languages = models.TextField(blank=True, help_text="زبان‌ها را با کاما جدا کنید")

    # تحصیلات
    edu1_degree = models.CharField(max_length=100, blank=True)
    edu1_college = models.CharField(max_length=150, blank=True)
    edu1_year = models.CharField(max_length=4, blank=True)

    edu2_degree = models.CharField(max_length=100, blank=True)
    edu2_college = models.CharField(max_length=150, blank=True)
    edu2_year = models.CharField(max_length=4, blank=True)

    edu3_degree = models.CharField(max_length=100, blank=True)
    edu3_college = models.CharField(max_length=150, blank=True)
    edu3_year = models.CharField(max_length=4, blank=True)

    # پروژه‌ها
    proj1_title = models.CharField(max_length=150, blank=True)
    proj1_duration = models.CharField(max_length=50, blank=True)
    proj1_description = models.TextField(blank=True)

    proj2_title = models.CharField(max_length=150, blank=True)
    proj2_duration = models.CharField(max_length=50, blank=True)
    proj2_description = models.TextField(blank=True)

    # تجربیات
    exp1_company = models.CharField(max_length=150, blank=True)
    exp1_post = models.CharField(max_length=150, blank=True)
    exp1_duration = models.CharField(max_length=50, blank=True)
    exp1_description = models.TextField(blank=True)

    exp2_company = models.CharField(max_length=150, blank=True)
    exp2_post = models.CharField(max_length=150, blank=True)
    exp2_duration = models.CharField(max_length=50, blank=True)
    exp2_description = models.TextField(blank=True)

    # دستاوردها
    achievement_first = models.CharField(max_length=255, blank=True)
    achievement_second = models.CharField(max_length=255, blank=True)
    achievement_third = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
