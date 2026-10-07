# Political Institution Theory Quiz App — プロジェクト概要

## このプロジェクトについて
名古屋大学大学院（GSID）の授業「Political Institution Theory」向けのAI搭載クイズWebアプリ。
学生は指定文献を読んだ後、AIチューター（Claude）とソクラテス式対話をしてから短い回答を提出する。
回答（会話ログ＋最終回答）はGoogle Sheetsに自動保存される。
Comparative Methods Quiz App（`cm_quiz_app.py`）と同じ仕組みで、別リポジトリ・別アプリとして運用する。

## ファイル構成

| ファイル | 役割 |
|---|---|
| `pit_quiz_app.py` | Streamlitメインアプリ（基本的に触らない） |
| `pit_quizzes.py` | クイズ定義ファイル（毎週ここだけ編集） |
| `requirements.txt` | Pythonパッケージ一覧 |
| `.gitignore` | 認証情報（secrets.toml, *.json）をコミットしないための設定 |

## アプリの仕様

- **フレームワーク**: Streamlit
- **AIモデル**: `MODEL` 定数（初期値 claude-opus-4-6）
- **最大会話往復数**: 7回（`MAX_EXCHANGES`）／ **提出に必要な最低往復数**: 3回（`MIN_EXCHANGES`）
- **時刻**: すべて日本時間（`Asia/Tokyo`）。Streamlit Cloud は UTC で動くためコード側で固定
- **締切**: `due_date`（JST）を過ぎるとチャットと提出が自動で閉じる
- **保存先**: Google Sheets（クイズIDごとに別タブを自動作成）
- **保存内容**: Timestamp (JST)、Student Name、Quiz ID、Quiz Title、Final Answer、Word Count、Exchange Count、Conversation Log
- 提出後、学生は自分の提出内容をJSONでダウンロードできる

## Secrets（Streamlit Cloud, TOML）
Comparative Methods と同じサービスアカウントを流用し、`GOOGLE_SHEET_ID` だけ新しいシートのIDにする。

```toml
ANTHROPIC_API_KEY = "sk-ant-..."
GOOGLE_SHEET_ID = "PIT用スプレッドシートのID"

[GOOGLE_CREDENTIALS]
type = "service_account"
# ...（CMアプリと同じ値）
```

## 毎週のクイズ追加手順
`pit_quizzes.py` の `PIT_QUIZZES` リストに辞書を追加して push する。
キー: `id`, `active`, `week_label`, `title`, `assigned_date`, `due_date`（"YYYY-MM-DD HH:MM", JST）,
`reading`, `scenario`, `question`, `word_limit`, `concepts`, `opening_message`, `tutor_extra`。

## 現在登録済みのクイズ

| ID | タイトル | 文献 | 締切（JST） | 状態 |
|---|---|---|---|---|
| pit-1 | Calculus vs. Cultural Approaches to Institutions | Hall & Taylor (1996) | 2026-10-13 12:00 | active |
