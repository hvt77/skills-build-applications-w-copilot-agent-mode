from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='testuser', team='Test Team', type='Running', duration=30)
        self.assertEqual(activity.type, 'Running')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(leaderboard.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', difficulty='Easy')
        self.assertEqual(workout.difficulty, 'Easy')

    def test_user_creation(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
        self.assertEqual(user.username, 'testuser')
