from datetime import datetime
from time import time

seconds = time()
x = datetime.now()

print("Seconds since January 1, 1970: {0:,.4f} or {0:.2e}"
      " in scientific notation".format(seconds))
# alternate method
# print("Seconds since January 1, 1970: "
#       f"{seconds:,.4f} or {seconds:.2e} in scientific notation")
print(x.strftime("%b %d %Y"))
