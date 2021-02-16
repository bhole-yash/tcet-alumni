from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

Department =( 
    ("COMP", "Computer Engineering"), 
    ("ELEX", "Electronics Engineering"), 
    ("MECH", "Mechanical Engineering"), 
    ("CIVIL", "Civil Engineering"), 
    ("EXTC", "Electronics & Telecommunication"), 
	("N/A","Enter your Department"),
)


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username,department, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')
		if not department:
			raise ValueError('Users must have a department')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			department=department,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username,department, password):
		user = self.create_user(
			email=self.normalize_email(email),
			department =department,
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	department 				= models.CharField(max_length= 10,choices=Department,default = 'N/A')
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username','department']

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True













