email = models.EmailField(
    verbose_name="이메일",
    max_length=255,
    unique=True,
)
name = models.CharField('이름', max_length=10)
nickname = models.CharField('닉네임', max_length=10)
genderPick = (
    ('F', '남성'),
    ('M', '여성'),
    ('X', '젠더X'),
)
gender = models.CharField('성별', choices=genderPick, max_length=1)
age = models.IntegerField('나이')  # 제한을 주고싶을 때 어떻게 하면 되는지
introduction = models.TextField('간단 소개글', max_length=100)

{
    "name": "태서경",
    "nickname": "떠경",
    "gender": "F",
    "age": 32,
    "email": "Ejrud@sparta.com",
    "password": "1234",
    "introduction": "안녕하세요 떠경입니다. 반갑습니다!",
}
