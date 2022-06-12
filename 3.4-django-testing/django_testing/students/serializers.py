from rest_framework import serializers

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        students = Course.objects.filter(id=self.context["request"].id)
        if len(students) + len(self.context["request"].students) > 20:
            raise serializers.ValidationError('На курсе не может быть больше 20 студентов!')

        return data
