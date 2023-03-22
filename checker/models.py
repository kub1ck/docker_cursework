from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models


class FileStatus(models.TextChoices):
    NEW = 'new', 'Новый'
    UPDATED = 'updated', 'Обновленный'
    VERIFIED = 'verified', 'Подтвержденный'


class File(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')
    file = models.FileField(upload_to='files', validators=[FileExtensionValidator(['py'])], verbose_name='Файл')
    status = models.CharField(max_length=20, choices=FileStatus.choices, default=FileStatus.NEW, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['status']

    def delete(self, *args, **kwargs):
        storage, path = self.file.storage, self.file.path
        super().delete(*args, **kwargs)
        storage.delete(path)


class Logs(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, verbose_name='Файл')
    info = models.TextField(verbose_name='Информация')
    send_mail = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
        ordering = ['created_at']
