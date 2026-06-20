from rest_framework import serializers
from .models import Singer,Song

class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(read_only=True,many = True)
    # song = serializers.PrimaryKeyRelatedField(many = True,read_only = True)
    # song = serializers.HyperlinkedRelatedField(many = True,read_only = True,view_name = 'song-detail')
    # song = serializers.SlugRelatedField(many = True,read_only = True,slug_field='title')
    song = serializers.HyperlinkedRelatedField(view_name='song-detail',read_only=True,many=True)
    class Meta:
        model = Singer
        fields = ['id','name','gender','song']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','duration','singer']

