# PythonFlaskSimpleAPI
Python+Flask Simple API

## Usage
프로젝트별 가상환경을 설정하기 위해 [Virtualenv](https://virtualenv.pypa.io/en/latest/)를 global하게 install합니다. 가상환경을 설정해야 프로젝트별 독립성을 보장할 수 있습니다. python 버전에 따라 pip 또는 pip3를 사용합니다.

```bash
$ sudo pip3 install virtualenv
```
\
Virtualenv가 설치되면 이 프로젝트 폴더 위치로 이동해서 아래처럼 가상환경을 설정합니다.\
ENV는 원하는 이름으로 변경하고 설정한 가상환경을 activate 해줍니다.

```bash
$ virtualenv ENV
$ source ENV/bin/activate
```
성공적으로 activate 되었다면 아래처럼 (ENV)로 활성화된 것을 확인할 수 있습니다.

![](https://user-images.githubusercontent.com/38330816/48984203-3687c780-f13c-11e8-8ec1-0fa06b942b56.png)

\
가상환경이 activate된 상태에서 flask를 install합니다.
```bash
$ pip3 install flask
```

shell script로 되어있는 develop, production 환경별 파일을 실행하면 Running on 메세지로 서버가 실행된 것을 확인할 수 있습니다.
```bash
$ sh run_dev
```
![](https://user-images.githubusercontent.com/38330816/48984204-38ea2180-f13c-11e8-843c-f3bf7941a661.png)



## Add API
data폴더에 필요한 api이름의 json파일을 넣으면 같은 이름으로 접근할 수 있습니다.

<img src="https://user-images.githubusercontent.com/38330816/48916456-b9ebb380-eec5-11e8-9992-2c0739dfadb2.png" width="400">
