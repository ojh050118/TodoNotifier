# TodoNotifier

명령어 **한번**으로 내가 해야할 *작업*을 추가하세요!

## 상태

핵심 기능을 구현하였고 잘 작동합니다.

**중요:** 개발이 진행됨에 따라 프로젝트는 끊임없이 변화하고 있습니다. 항상 안정적이지 못할 수 있습니다. 핵심 기능에 문제가 생겼다면 언제든지 이슈를 열어주세요!

## TodoNotifier 실행

Python으로 작성되었기 때문에 단독 실행 파일이 존재하지 않습니다. 최소 Python 3.8~[최신](https://www.python.org/downloads) 버전에서 가상환경을 만들어 실행하는 것을 권장합니다.

**중요:** 이 프로젝트는 실행시 프로젝트 파일에 있는 [config.json](files/config.json)과 `Cog`를 동적으로 추가하기때문에 프로젝트 실행경로에 의존합니다.
작업 디렉터리는 **../TodoNotifier**로 설정하세요! 상위 또는 하위 디렉터리에서 작업하면 실행에 실패합니다.

작업 디렉터리 설정을 완료했다면 [config.json](files/config.json)에 자신의 Discord Application ID와 봇 토큰을 기입해주세요. 
혹은 `todonotifier_application_id`와 `todonotifier_token`의 환경변수를 만들어 올바른 값으로 할당하여 주세요. (환경 변수부터 먼저 확인합니다!)

마지막으로 `main.py`를 실행하면 됩니다!

## TodoNotifier 개발

다음 전제조건에 만족하는지 확인하세요:
* Python 3.8이상으 버전이 설치되어있는 데스크탑 플랫폼.
* 코딩 작업을 한다면 구문 강조와 자동 완성 기능과 제공되는 다음과 같은 최신 버전의 IDE를 권장합니다: 
[Visual Studio Code](https://code.visualstudio.com), [JetBrains Pycharm](https://www.jetbrains.com/pycharm) 등.

### 소스 코드 다운로드

 저장소를 복제합니다:
 
 ```shell
 git clone https://github.com/ojh050118/TodoNotifier
 cd TodoNotifier
 ```
 
소스 코드를 최신 커밋으로 업데이트 하려면 `TodoNotifier`폴더에서 다음 명령을 실행하세요:

```shell
git pull
```

## 기여
프로젝트에 기여하는 것과 관련하여 도움을 줄 수 있는 두 가지 주요 작업은 문제 보고와 풀 리퀘스트 제출입니다. 
풀 리퀘스트 제출시, `master`브랜치에 작성된 코드에 따라 콛 컨벤션을 준수하여 제출하세요.
가능한 한 트러블 없이 이 프로젝트에 기여할 수 있도록 모든 피드백을 환영합니다.

## 라이선스

TodoNotifier으 소스코드는 MIT 라이선스에 따라 라이선스가 부여됩니다. 자세하 내용은 [License 파일](License)으 참조하세요. 
[TL;DR](https://tldrlegal.com/license/mit-license) 소프트웨어/소스 코드 사본에 원본 저작권 미 라이선스 고지를 포함하는 한 원하는 모든 작업을 수행할 수 있습니다.
