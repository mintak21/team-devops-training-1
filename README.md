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
- パラメータ
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
pytest -vv
```

# デプロイ
TODO

# ディレクトリ構成
レイヤードアーキテクチャライクな構成としています。(あくまでライク)

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
- 一部の役は判定されない
- パラメータのバリデーションを行っていない
