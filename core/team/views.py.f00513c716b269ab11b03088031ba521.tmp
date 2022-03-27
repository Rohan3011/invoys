from rest_framework import viewsets

from .models import Team
from .serializers import TeamSerializer

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def get_queryset(self):
        teams = self.request.user.teams.all()

        if not teams:
            Team.objects.create(name='',CIN='',created_by=self.request.user)

        return self.queryset.filter(created_by = self.request.user)