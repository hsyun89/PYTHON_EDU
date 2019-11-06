from django.db import models
class Genre(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.id}번 장르 - {self.name}'
class Movie(models.Model):
    title = models.CharField(max_length=10)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.id}번 영화 : {self.title}({self.genre.name}) - {self.audience}명'
class Score(models.Model):
    content = models.CharField(max_length=20)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.movie.title} - {self.score}점'