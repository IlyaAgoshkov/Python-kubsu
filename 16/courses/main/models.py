from django.db import models




class Instructor(models.Model):
    instructor_name = models.CharField('Имя инструктора', max_length=100)
    instructor_id = models.CharField('ID инструктора', max_length=100, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.instructor_name

    class Meta:
        verbose_name = 'Инструктор'
        verbose_name_plural = 'Инструкторы'


class Subject(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    subject_name = models.CharField('Название предмета', max_length=100)

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Course(models.Model):
    course_name = models.CharField('Название курса', max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
