import os  # osモジュールの読み込み
import sqlite3  # sqlite3モジュールの読み込み

# path_mod_spatialite = '/opt/homebrew/lib'  # mod_spatialite.dllの入っているフォルダ
# os.environ['PATH'] = '{}:{}'.format(path_mod_spatialite, os.environ['PATH'])  # 環境変数に追加

con = sqlite3.connect('sample.spatialite')  # メモリ上に仮想データベースを生成
con.enable_load_extension(True)  # SQLite拡張機能の読み込みを有効にする（デフォルトはFalse）
con.execute("SELECT load_extension('/opt/homebrew/lib/mod_spatialite');")  # SQLiteデータベースに拡張機能を読み込み
print(con.execute("SELECT spatialite_version();").fetchone()[0])  # SpatiaLiteのバージョンを表示
con.execute("SELECT InitSpatialMetaData(1);")  # メタデータを生成

