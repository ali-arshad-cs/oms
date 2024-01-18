from django.db import models


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cnic_number = models.CharField(max_length=100)
    hire_date = models.DateField()
    position = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    # department = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    emergency_contact_number = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='shared_images/', null=True, blank=True)
    id_card = models.ImageField(upload_to='shared_images/', null=True, blank=True)
    date_left = models.DateField(null=True, blank=True)
    responsibility = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.full_name}"


class MonthlySalary(models.Model):
    salary_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    notes = models.TextField(null=True, blank=True)
    salary_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bonus_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_paid_date = models.DateField(null=True, blank=True)
    salary_receipt = models.ImageField(upload_to='shared_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.month.strftime('%B, %Y')}"