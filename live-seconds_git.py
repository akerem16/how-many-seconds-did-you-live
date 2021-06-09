# For python 3.6
# Made in Turkey
# By @akerem16

# [EN] A program that calculates all the seconds you have lived since the day you were born.
# [EN] The method is simple: we subtract the time we were born from and convert it to seconds.

# [TR] Doğduğunuz günden itibaren yaşadığınız tüm saniyeleri hesaplayan bir program.
# [TR] Yöntem basit: Şimdiki zamandan doğduğumuz zamanı çıkartıp saniye türüne çeviriyoruz.


# [EN] We also use the datetime library.
# [TR] datetime kütüphanesinden de yararlanıyoruz.
from datetime import *

birthdate = datetime.strptime(input("[EN] Your birth date (dd.mm.yyyy): "), "%d.%m.%Y")
age = datetime.now() - birthdate
allseconds = age.total_seconds()  # [EN] This is total seconds you survived

print(f"""
[EN] You survived {allseconds} seconds.
[TR] {allseconds} saniyedir hayattasın.
""")
