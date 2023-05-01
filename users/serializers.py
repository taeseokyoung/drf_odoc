from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # Article.objects.get(id=1) 하나만 가져온다. (단일 object)
    # Article.objects.filter(id__gte=1) 해당내용 전부 다 가져온다.(object의 집합. 쿼리셋으로 결과물이 도출된다.)

    class Meta:
        model = User
        fields = "__all__"
        # fields = ('id', 'email', 'name', 'nickname',
        #           'gender', 'age', 'introduction')
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }
        # "required":False

        # is_valid, save() : write
        # .data로 직렬화 : read

        # read_only_fields = []

    def validate(self, attrs):
        # attrs 에는 샤용자에게 입력 받은 내용이 dict 로 들어온다.
        """
        serializer 의 validate
        1. 필드에 대한 유효성 검사
        2. 커스텀 validate
        """
        age = attrs["age"]
        if age < 14:
            raise serializers.ValidationError("14세 미만은 가입할 수 없습니다.")
        return super().validate(attrs)

    # 커스텀이 필요할 때는 '오버라이딩' 하여 사용하는 것.
    # .save() 호출해야 create 실행
    def create(self, validated_data):
        """
        3. set password
        """
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user
