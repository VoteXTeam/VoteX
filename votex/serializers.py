from typing import List

from rest_framework import serializers

from votex.controllers import ElectionController
from votex.models import Voter, Election, Location, LocalElection, GlobalElection, Candidate


class LoginUserInputSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=145)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['city']


class RetrieveElectionsSerializer(serializers.Serializer):
    class Meta:
        model = Location
        fields = '__all__'


class CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class VoterSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False)

    class Meta:
        model = Voter
        fields = [
            'id', 'full_name', 'email', 'passport_id', 'birthdate', 'location'
        ]


class VoterRegistrationSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False)

    class Meta:
        model = Voter
        fields = [
            'id', 'full_name', 'email', 'passport_id', 'birthdate', 'password', 'location'
        ]


class ElectionSerializer(serializers.ModelSerializer):
    @classmethod
    def to_representation(cls, instance):
        if isinstance(instance, LocalElection):
            return LocalElectionSerializer(instance=instance)
        elif isinstance(instance, GlobalElection):
            return GlobalElectionSerializer(instance=instance)

    class Meta:
        model = Election
        fields = '__all__'


class GlobalElectionSerializer(serializers.ModelSerializer):
    candidates = CandidatesSerializer(many=True)

    class Meta:
        model = GlobalElection
        fields = ['id', 'name', 'description', 'is_flexible', 'start_date', 'end_date', 'candidates']


class LocalElectionSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False)
    candidates = CandidatesSerializer(many=True)

    class Meta:
        model = LocalElection
        fields = ['id', 'name', 'description', 'is_flexible', 'start_date', 'end_date', 'location', 'candidates']


class MessageSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=250)


class UserIDSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()


class VoteInputSerializer(serializers.Serializer):
    election_id = serializers.IntegerField()
    candidate_id = serializers.IntegerField()


class StatisticSerializer(serializers.ModelSerializer):
    statistic = serializers.SerializerMethodField(read_only=False)

    def get_statistic(self, obj):
        controller = ElectionController(obj)
        statistic = controller.get_percents_by_candidate_for_election()
        return statistic

    class Meta:
        model = Election
        fields = '__all__'


class CandidateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = [
            'full_name'
        ]


class VotingResultSerializer(serializers.Serializer):
    candidate_names = CandidateNameSerializer(many=True)
    vote_count = serializers.ListField(child=serializers.IntegerField())


class ElectionFullSerializer(serializers.ModelSerializer):
    vote_results = serializers.ListField(
        child=VotingResultSerializer()
    )

    class Meta:
        model = Election
        fields = '__all__'
