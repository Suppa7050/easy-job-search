#by suppa


# users/serializers.py

from rest_framework import serializers
from .models import Job, Question

# class QuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = ['question_text']

# class JobSerializer(serializers.ModelSerializer):
#     questions = QuestionSerializer(many=True)

#     class Meta:
#         model = Job
#         fields = ['job_id', 'job_name', 'job_role', 'job_description', 'last_date', 'questions']

#     def create(self, validated_data):
#         questions_data = validated_data.pop('questions')
#         job = Job.objects.create(**validated_data)
#         for question_data in questions_data:
#             Question.objects.create(job=job, **question_data)
#         return job


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_text']

class JobSerializer(serializers.ModelSerializer):
    # Set read_only=True if you're also using this serializer to list jobs
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = ['job_id', 'job_name', 'job_role', 'job_description', 'last_date', 'questions']

    def create(self, validated_data):
        # Ensure questions are handled if passed
        questions_data = self.context['request'].data.get('questions', [])
        job = Job.objects.create(**validated_data)
        
        # Create questions linked to the job
        for question_data in questions_data:
            Question.objects.create(job=job, **question_data)
        
        return job
