# アプリケーションの実行(Local)
```bash
make run
curl -v http://localhost:5000/api/v1/poker/judge?cards=S2,S3,S4,S5,S6
```

# アクセスポイント
## ヘルスチェック

- ルート：GET `api/v1/health/`
- パラメータ
  - なし
- レスポンス
  - Class : string
  - Value : pass(固定)

## 役判定

- ルート：GET `/api/v1/poker/judge`
- リクエストパラメータ

  |名前|概要|データ型
  |:---|:---|:---
  |cards|判定したい手札一覧(5枚)|string(カンマ区切り)
  Sample：`http://localhost:5000/api/v1/poker/judge?cards=S2,S3,S4,S5,S6`

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
    "result": "ハイカード"
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

# デプロイ
`master`にPRをマージ(`bump`)すると、これをトリガーにしてCI->CDが実行されます。
ブランチのCIが正常完了した場合、自動的に`heroku`へデプロイするように設定しています。

# ディレクトリ構成
レイヤードアーキテクチャライクな構成としています。(あくまでライク)
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
- 一部の役は判定されない(2ペア、フルハウス、ストレート、ロイヤルストレートが判定できない)
- パラメータのバリデーションを行っていない

# Ref.
- CI: CircleCI
