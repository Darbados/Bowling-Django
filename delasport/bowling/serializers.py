from rest_framework import serializers
from models import Game, Frame

class FrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frame
        fields = ('id','attempt1','attempt2','attempt3','total_score_in_frame')

class GameSerializer(serializers.ModelSerializer):
    frames = FrameSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ('id','player','total_score','frames')
