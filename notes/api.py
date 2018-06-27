from rest_framework import serializers
class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
    fields = (‘title’, ‘content’)
