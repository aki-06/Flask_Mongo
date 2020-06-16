# 基本操作
## サーバ接続

```
mongo <IP>:<PORT>/<DATABASE>
```

- IP
    - 接続先IPアドレスを指定。
    - デフォルトは127.0.0.1。
- PORT
    - 接続先ポートを指定。
    - デフォルトは27017。
- DATABASE
    - 接続先データベース。
    - デフォルトはtest。

## サーバ切断

```
exit
```

## 利用したいdatabaseを指定

```
use <DATABASE>
```
- useを実行しただけではデータベースは作成されない。
- データを入れると初めて作成される。

## 接続中データベース確認

```
db
```

## データベース一覧表示

```
show dbs
```

## データベース削除

```
use <DATABASE>
db.dropDatabase()
```

## コレクション作成

```
db.createCollection(<COLLECTION>)
```

## コレクション一覧表示

```
show collections
```

## コレクション名変更

```
db.<SOURCE>.renameCollection(<TARGET>, <DROP>)
```

- SOURCE
    - 変更元コレクション名
- TARGET
    - 変更後の新しいコレクション名
- DROP
    - 古いコレクションを削除するか。デフォルトはfalse。


## ドキュメント作成

```
db.<TARGET>.insert(<DOCUMENTS>)
```

- DOCUMENTS
    - 挿入したいドキュメント(オブジェクト)
    - 複数の場合は配列を指定。

## ドキュメント一覧表示

```
db.<TARGET>.find(<QUERY>)
```

- QUERY
    - 検索条件
    - 何もしなければ全件表示。

## ドキュメント更新

```
db.<TARGET>.update(<QUERY>, <UPDATE>, <OPTION>)
```

- QUERY
    - 検索条件
- UPDATE
    - 更新方法および更新するドキュメント。
- OPTION
    - 更新オプション
    - 何も指定しなければ最初にヒットした1件のみ更新
        - 条件に合致する全てを更新したい場合は{multi: true}を指定。

## ドキュメント削除

```
db.<TARGET>.remove(<QUERY>, <JUSTONE>)
```

- QUERY
    - 検索条件
- JUSTONE
    - 最初に一致した1件のみを対象とする場合は"true"
    - 全件対象の場合は"false"
        - デフォルト"false"

## ドキュメント件数取得

```
db.<TARGET>.count(<QUERY>)

db.<TARGET>.find(<QUERY>).count()
```

- QUERY
    - 検索条件

## 検索結果のソート

```
cursor.sort(<ORDER>)
```

- ORDER
    - 昇順は1、降順は-1。

## インデックス作成

```
db.<TARGET>.createIndex(<KEYS>, <OPTIONS>)
```

- 指定したコレクションのキーに対してインデックスを作成する。
- KEYS
    - インデックス作成するキーおよび方向(昇順は1、降順は-1)を指定。
- OPTIONS
    - インデックス作成に関するオプションを指定。
        - インデックス名(name)や一意制約({unique: true})など。

## インデックス確認

```
db.<TARGET>.getIndexes()
```

- 指定したコレクションに設定されているインデックス一覧を取得。

## インデックス削除

```
db.<TARGET>.dropIndex(<NAME>)
```

- NAME
    - 削除したいインデックス名。