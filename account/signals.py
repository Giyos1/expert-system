from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from account.models import Student, ExportEmployee


@receiver(post_save, sender=ExportEmployee)
def creat_employee(sender, instance, created, **kwargs):
    if created:
        s1 = Student.objects.create(username=instance.username,
                                    first_name=instance.first_name,
                                    last_name=instance.last_name,
                                    email=instance.email,
                                    password=instance.password,
                                    phone_number=instance.phone_number,
                                    is_active=False)
        ExportEmployee.objects.filter(username=instance.username).update(user=s1)

    if not created:
        if instance.activ:
            s1 = Student.objects.filter(username=instance.username).first()
            s1.is_active = True
            s1.save()
            if s1.is_active:
                    send_mail(
                        subject='Activation link',
                        message=f'Siz muvaffaqiyatli ro`yxatdan o`tdingiz. saytdan foydalanish uchun linkni bosing: http://localhost:8000/accounts/login/',
                        from_email='giyosoripov4@gmail.com',
                        recipient_list=[instance.email],
                        fail_silently=False
                )
        else:
            s1 = Student.objects.filter(username=instance.username).first()
            s1.active = False
            s1.save()
