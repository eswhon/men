import os
import logging

api_id = int(os.environ.get("API_ID", "28509321"))
api_hash = os.environ.get("API_HASH", "ecab5787223afbadb69907b8b5ec405e")
bot_token = os.environ.get("BOT_TOKEN", "5849560668:AAED22x-VqDch98Z0g9GEap4r8tdiM7a-OU=")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://ubot:ubot@ubot.walq0cc.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "menfess")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001919784012"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001705648485"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001981609904"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1863087128"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "5"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "80"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "70"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "60"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "40"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "30"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#wts #wtb #admin #help #Girl #Boy #Ask #Find #Spill #Story").replace(" ", "|").lower()
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", "Hai {fullname} 🌱\n\nIni adalah bot menfess, semua pesan yang kamu kirim akan masuk ke channel secara anonymous. ketik /help")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, Silahkan ketik /help untuk menggunakan bot ini
""")
