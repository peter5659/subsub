멋쟁이사자처럼 8기 장고 프로젝트 "음식구독 서비스 섭섭"을 위한 레포입니다.

아래 규칙에 따라주시기 바랍니다.

#1. 파일, 함수, 변수명은 자바컨벤션(카멜케이스)을 따릅니다.
    ex. mainAttributes.css
    ex. def exampleOneTwoThree() :
    ex. function exampleOneTwoThree() {}
#2. 클래스, 모델은 첫글자만 대문자로 작성합니다.
    ex. class Example : Models
#3. 함수 작성 시 도입부에 간단한 설명을 주석으로 달아둡니다.
    ex. def func() :
        # 그냥 함수
    ex. function example() {
        // 자바스크립트 함수
    }
#4. 키를 필요로 하는 API등은 keys.json에 추가하고 .gitignore로 보호합니다.
#5. html 클래스, id, 장고앱 이름은 전부 소문자로 작성합니다.
#6. url, html 클래스, id의 공백은 '-'를 사용합니다.
    ex. <div class="ex-one ex-two" id="division-one">
    ex. http://localhost/subserve-example
#7. 클래스를 상속받거나 프로토콜을 사용할 일이 있을때는 파일을 따로 만들어서 모아둡니다.
#8. 잘 모르겠으면 물어봅니다.
#9. 에러코드는 그대로 복붙해서 구글에 치면 해결방법 많이 나옵니다.
#10. migrations 디렉토리 안의 파일들은 절대로 지우지 않도록 합니다.


------
필요한 파이선 모듈:
urllib3

------
기타 필요한거:
ajax, jQuery, nodejs(아마도?)