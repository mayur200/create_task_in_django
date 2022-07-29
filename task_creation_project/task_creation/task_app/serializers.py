from rest_framework import serializers
from .models import Task, TaskMedia



class TaskMediaSerializer(serializers.ModelSerializer):
     class Meta:
        model = TaskMedia
        fields =  ('task','file',)



class TaskSerializer(serializers.ModelSerializer):
    # file = serializers.ListField(
    #         child=serializers.FileField( max_length=100000,
    #                                     allow_empty_file=False,
    #                                 use_url=True ))

    task_media = TaskMediaSerializer(many=True, required = False)


    class Meta():
        model = Task
        fields = ('task_id','task_ref_number','instructions','task_media')


    # def create(self, validated_data):
    #     # if 'task_media' in validated_data:
    #     task_media=validated_data.pop('task_media')
    #     task_instance = Task.objects.create(file=task_media,**validated_data)
    #     for img in task_instance:
    #         TaskMedia.objects.create(**img, task=task_instance)
    #     return task_instance





