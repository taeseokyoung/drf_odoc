from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
            age=0,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="이메일",
        max_length=255,
        unique=True,
    )
    name = models.CharField('이름', max_length=10)
    nickname = models.CharField('닉네임', max_length=10)
    genderPick = (
        ('F', '남성'),
        ('M', '여성'),
        ('X', '젠더X'),
    )
    gender = models.CharField('성별', choices=genderPick, max_length=1)
    age = models.IntegerField('나이')  # 제한을 주고싶을 때 어떻게 하면 되는지
    introduction = models.TextField('간단 소개글', max_length=100)

    # null=true 빈값상관없다 #blank=true isvalid에서 null값이더라도 통과!

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # null true 안 줄 것들

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
