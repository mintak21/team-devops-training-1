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

# 留意事項
- この時点では役の判定は不完全です。(一部の役は判定されない)
