from django.db import models

class CodingStat(models.Model):

    PLATFORM_CHOICES = [
        ("leetcode", "LeetCode"),
        ("gfg", "GeeksforGeeks"),
        ("codechef", "CodeChef"),
        ("codeforces", "Codeforces"),
        ("hackerrank", "HackerRank"),
    ]

    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    problems_solved = models.PositiveIntegerField()
    rating = models.CharField(max_length=50, blank=True)
    profile_url = models.URLField(blank=True)

    def __str__(self):
        return self.get_platform_display()

    class Meta:
        ordering = ["-problems_solved"]