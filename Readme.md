## 요구사항
- server requirements
  - Nodejs >= 10.x
  - NPM
---

## 설치 방법
1. 프로젝트 실행 전에 NPM과 Nodejs를 우선적으로 설치해야 합니다. 현재 사용하고 계시는 플랫폼에 맞게 [다운로드](https://nodejs.org/ko/download/) 받으시길 바랍니다.
2. Nodejs가 설치된 후 프로젝트 폴더에서 `npm install` 명령어를 command line에 입력합니다. 해당 명령어는 웹 서버에서 사용하는 모듈을 설치하는 명령어 입니다.
3. 모듈 설치가 완료된 후, `npm run serve` 명령어를 command line에 입력합니다. 해당 명령어는 웹 서버를 실행시켜 줍니다.

### 참고사항
1. Translator: 현재 translator.py는 input 값 입력받고, string 길이만큼 랜덤하게 문자열 리턴하는 파일입니다.
실행하시고자 하시는 파일을 프로젝트 폴더에 넣으신 후, 설치 방법의 3번을 실행하시기 전에 `export translatorFile=만드신 파일 이름.py` command line에 입력해주신 후, 3번의 과정을 진행하시면 됩니다. 만약, translator.py로 파일명 실행 시에는 하지 않으셔도 됩니다.
2. I am translator: 현재 write-file.py는 en, ko 두 가지의 string을 입력받고 파일에 저장하는 파일입니다.
마찬가지로 실행하시고자 하는 파일을 프로젝트 폴더에 넣으신 후, 설치 방법의 3번을 실행하시기 전에 `export translatorWriteFile=만드신 파일 이름.py` command line에 입력해주신 후, 3번의 과정을 진행하시면 됩니다. 
만약, write-file.py로 파일명 실행 시에는 하지 않으셔도 됩니다.