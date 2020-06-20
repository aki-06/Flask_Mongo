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

## 関係演算子

- $eq: 等価

```
{<FLD>: {$eq: <VAL>}}
```

- $ne: 非等価

```
{<FLD>: {$eq: <VAL>}}
```

- $gt: より大きい

```
{<FLD>: {$gt: <VAL>}}
```

- $gte: より大きいか等しい

```
{<FLD>: {$gte: <VAL>}}
```

- $lt: より小さい

```
{<FLD>: {$lt: <VAL>}}
```

- $lte: より小さいか等しい

```
{<FLD>: {$lte: <VAL>}}
```

- $in: いずれか

```
{<FLD>: {$in: <VAL>...}}
```

## 論理演算子

- $and: 論理積

```
{$and: [<EXP1>, <EXP2>...]}
```

- $or

```
{$or: [<EXP1>, <EXP2>...]}
```

- $not
    - 文字比較の場合、正規表現を利用する

```
{$<FLD>: {$not: <EXP>}}
```

## 正規表現

- $regex
    - $regexは省略可能

```
{<FLD>: {$regex: /<REGEX>/<OPT>}}
{<FLD>: {/<REGEX>/<OPT>}}
```

## 要素演算子

- exists: フィールドが存在しているか

```
{<FLD>: {$exists: <BOOL>}}
```

- type: データ型

```
{<FLD>: {$type: <TYPE>}}
```

## 配列演算子

- $elemMatch: 要素と一致

```
{<FLD>: {$elemMatch: {<EXP1>, ...}}}
```

- $size: 要素数

```
{<FLD>: {$size: <SIZE>}}
```

## フィールドの更新

```
db.<TARGET>.update(<QUERY>, {$set: <FIELD>: xxx}, <OPTION>)
```

- OPTION
    - 更新オプション
        - multi: 条件に合致する全てを更新するかどうか
        - upsert: 存在すれば更新、なければ挿入
        - arrayFilters: 配列更新時に使う修飾子

## フィールドの削除

```
db.<collection>.update(
    <QUERY>,
    {$unset: {<FIELD1>: "", ...}}
)
```

- 指定された条件に一致するフィールドを削除する。
- バリューには""(空文字)を固定で指定する

## フィールド名の変更

```
db.<COLLECTION>.update(
    <QUERY>,
    {$rename: {<FIELD1>: <NEW_NAME1>, ...}}
)
```

## フィールドを現在日時で更新

```
db.<COLLECTION>.update(
    <QUERY>,
    {$currentDate: {<FIELD>: true, ...}}
)
```

- Date型: "date"
- Timestamp型: "timestamp"

## フィールドを加算して更新

```
db.<COLLECTION>.update(
    <QUERY>,
    {$inc: {<FIELD1>: <VALUE>, ...}}
)
```

- 引き算の場合はVALUEに負の値を指定

## フィールドを乗算して更新

```
db.<COLLECTION>.update(
    <QUERY>,
    {$mul: {<FIELD1>: <VALUE1>, ...}}
)
```

- 割り算の場合はVALUEに逆数を指定


## 配列要素の追加

```
db.<COLLECTION>.update(
    <QUERY>,
    {$push: {"<FIELD1>": <VALUE1>, ...}}
)
```

- FIELDにVALUEを追加する

- 修飾子
    - $each: 複数要素を同時に追加
    - $slice: 配列要素を指定数に切り取り
    - $sort: 配列要素をソート
    - $position: 指定した位置へ要素を追加

## 配列要素の更新

```
db.<COLLECTION>.update(
    <QUERY>,
    {<OPERATOR>: {"<ARRAY>.$[]": <VALUE>, ...}}
)
```

- 全ての要素を更新

```
db.<COLLECTION>.update(
    <QUERY>,
    {<OPERATOR>: {"<ARRAY>.$[<ID>]": <VALUE>, ...}},
    {arrayFilters: [<EXPRESSION>]}
)
```

- 特定の要素を更新

## 配列の削除

```
db.<COLLECTION>.update(
    <QUERY>,
    {$pop: {"<ARRAY>" : <-1 / 1>, ...}}
)
```

- 配列の先頭/末尾の削除

```
db.<COLLECTION>.update(
    <QUERY>,
    {$pull: {"<ARRAY>": <EXPRESSION>, ...}}
)
```

- ARRAYから条件EXPRESSIONに一致する要素を削除する。
