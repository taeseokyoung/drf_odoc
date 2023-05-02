# drf_odoc


2. User 모델
1. USERNAME_FIEOLD = 'email' 
2.
email = models.EmailField(unique=True)  
password = models.CharField(max_length=256)  
join_date = models.DateTimeField(auto_now_add=True)
GENDERS = ( ("F", "여성"),("M", "남성"),("X", "공개하지 않음"),)
gender = models.BooleanField or CharField(choices=GENDERS)
introduction = models.TextField(blank=True, default="")

AUTH_USER_MODEL = 'users.User' user를 나타내는 users app 안에 있는 (class) User 테이블을 인증할 때 사용되는 모델로 지정하겠다.


3. views.py
class UserView(APIview):
get : 사용자 정보를 response합니다.
post : 사용자 정보를 입력받아 회원가입을 진행합니다.
put : 회원 정보를 수정합니다.
delete : 회원 탈퇴를 진행합니다.

class UserLoginView(APIview):
post : 로그인
class UserLogoutView(APIview):
post : 로그아웃

3. Todo 모델
1. views.py
class UserView(APIview):
get(pk=None) : pk값의 유무에 따라 목록 혹은 상세정보를 response 합니다.
post : 내용을 입력받아 todo를 생성합니다.
put : todo를 수정합니다.
delete : todo를 삭제합니다.

class TodoCompleteView(APIview):  
put : 지정된 todo를 complete합니다. (UserView의 put에 들어가도 된다.)

* 로그아웃
세션 로그아웃 : 티켓 주문번호
데이터를 서버에서 관리한다.
서버에서 티켓 주문번호를 지워버린다.장고에서 사용자의 세션이 지워진다. 
JWT 로그아웃 : 구매자, 구매일자, *만료기간, 티켓 서명
서버가 필요없다. 티켓만 보고 입장여부를 결정한다.
프론트엔드에서 토큰 자체를 없애버리는 것을 로그아웃 기능을 한다고 말한다.
백에서 구현하는 방법은 액세스 토큰 유효기간을 짧게, 리프레시 토큰을 블랙리스트에 등록한다.
(재로그인) 리프레시가 되지 않으면서 로그아웃된다.


jwt
access 짧게
refresh 길게
