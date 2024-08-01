# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25567627")

API_HASH = os.environ.get("API_HASH", "82ca826376543f3237e83a88454bff49")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7103623471:AAGw9SS8hAGmVtn3wD1z64nakYbP5v49Gu8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "THE_REBEL_SQUAD") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "rebel-author")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://rebel-author:VuUxgpLdU5DGZviT@rebel-author.hy88gql.mongodb.net/?retryWrites=true&w=majority&appName=rebel-author")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
