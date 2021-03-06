[![CircleCI](https://circleci.com/gh/mintak21/team-devops-training-1.svg?style=shield)](https://circleci.com/gh/mintak21/team-devops-training-1) [![codecov](https://codecov.io/gh/mintak21/team-devops-training-1/branch/develop/graph/badge.svg)](https://codecov.io/gh/mintak21/team-devops-training-1)  [![](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/mintak21/team-devops-training-1/blob/master/LICENSE)

# アプリケーションの実行
## Local(Non-Docker)

```bash
make run
curl -v http://localhost:5000/api/v1/poker/judgement?cards=S2,S3,S4,S5,S6
```

## Local(Docker)

```bash
make run_docker
curl -v http://localhost:5000/api/v1/poker/judgement?cards=S2,S3,S4,S5,S6
```

## Prod

```text
https://team-devops-training-1.herokuapp.com/api/v1/poker/judgement?cards=S2,S3,S4,S5,S6
```

# アクセスポイント
ローカルではポート5000番でLISTENしています。

## ヘルスチェック

- ルート：GET `api/v1/health/`
- パラメータ
  - なし
- レスポンス
  - Class : string
  - Value : pass(固定)

## 役判定

- ルート：GET `/api/v1/poker/judgement`
- リクエストパラメータ

  |名前|概要|データ型
  |:---|:---|:---
  |cards|判定したい手札一覧(5枚)|string(カンマ区切り)

  Sample：`http://localhost:5000/api/v1/poker/judgement?cards=S2,S3,S4,S5,S6`

- レスポンス
  - Class : string(json)
  - Content Type: application/json
  - Response Columns

  |名前|概要|
  |:---|:---|
  |param_cards|リクエストパラメータ(cards)
  |result|判定結果|


  Sample:
  ```text
  {
    "param_cards": "S2,S3,S4,S5,S6",
    "result": "フラッシュ"
  }
  ```

# テスト実施
```bash
make test
```

## カバレッジ

- `Stmts`: コード行数
- `Miss` : テストされていない行数合計
- `Cover`: テストカバー率
- `Missing` : テストされていない行

```bash
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
app/domain/model/cards.py         66      6    91%   28, 31-33, 36, 99
app/domain/model/hands.py         17      0   100%
app/handler/health.py              6      0   100%
app/handler/poker.py               8      0   100%
app/manage.py                      8      1    88%   13
app/usecase/poker.py              30      0   100%
------------------------------------------------------------
```

# CI/CD
各ブランチにおいて、`push`を契機として`CircleCI`にてテストが実施されます。<br>
また、`master`にPRをマージ(`bump`)することをトリガーにしてデプロイが実行されます。<br>
(`master`ブランチの変更を検知し、CIが正常完了したのち自動的に`heroku`側のリポジトリにpushし、
デプロイがされるように(Herokuで)設定を行っています。)

# ディレクトリ構成
レイヤードアーキテクチャライクな構成としています。(あくまでライク)<br>
依存関係：`handler` --> `usecase` --> `domain`

- `handler` : 通信プロトコルに関わる部分、`http`関連の処理をここに記載
- `usecase` : ビジネスロジックに関わる部分、今回はポーカー判定ロジックをここに記載
- `domain`  : モデルをここで定義

```text
app                                ルートディレクトリ
├── config                         設定ファイル
│   └── gunicorn_setting.py
├── domain                         ドメインレイヤー
│   └── model
├── handler                        HTTP/プロトコルレイヤー
│   ├── health.py
│   └── poker.py
├── manage.py                      Launch Point
└── usecase                        ビジネスルールレイヤー
    └── poker.py
```

# 留意事項
以下の点は意図的に未完成となっています。
- 一部の役は判定されない(2ペア、フルハウス、ストレート、ストレートフラッシュが判定できない)
- パラメータのバリデーションを行っていない
