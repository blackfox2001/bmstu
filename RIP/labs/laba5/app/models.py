from django.db import models


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Films(models.Model):
    idfilm = models.AutoField(db_column='idFilm', primary_key=True)  # Field name made lowercase.
    namefilm = models.CharField(db_column='nameFilm', max_length=45)  # Field name made lowercase.
    aboutfilm = models.CharField(db_column='aboutFilm', max_length=450)  # Field name made lowercase.
    idfilmgenre = models.ForeignKey('Genres', models.DO_NOTHING, db_column='idFilmGenre')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'films'

    def __str__(self):
        return f'Название фильма: {self.namefilm}, О фильме: {self.aboutfilm}, {self.idfilmgenre}'

class Genres(models.Model):
    idgenres = models.AutoField(db_column='idGenres', primary_key=True)  # Field name made lowercase.
    namegenre = models.CharField(db_column='NameGenre', max_length=45)  # Field name made lowercase.
    aboutgenre = models.CharField(db_column='AboutGenre', max_length=450)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'genres'
        unique_together = (('idgenres', 'namegenre'),)

    def __str__(self):
        return f'Жанр: {self.namegenre}, О жанре: {self.aboutgenre}'