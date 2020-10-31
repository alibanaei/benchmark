import os
from time import sleep

users = [
        "08d179ee-78e3-4e46-bddc-daa19fad7643:kt8uNrgH2Hbu5SsIFeKGwLku3PQuhU6YIjQFa4HIaNC5JUvYyi0tk7B4QFybg6TJ",
        "09b950dc-1abc-4a97-a3f2-3271b7dcd022:lq5emgNNTMhc2tZCgSC0Ud0iN6fx6vWcTMKN9kihdAHZ6eRM1uyHUvPi5TsaHnCg",
        "6c8cab13-176a-492c-a90c-22932c59cbaf:FzkqFsv8dh0DUZ5Bu1AGaBm6oOkhvsIApnXYp9BpBHm5VKecL5Aqycv3tFaabXWh",
        "2f69ac41-3094-4380-a489-8f3360559d58:EJZq9uy60Ts16HkSLwIQBa5jHaifR55xArERsp74RdbBLi7BdrVIsR0T3Cq6nVvm",
        "4c3802e8-47b9-4bb6-a79a-320a67c0641f:uyhDuggKQ2MkgTMDJJ36gyi5jdWFu2kwAramI2sb5oedQKn3lmqrxC08EBYrcKXU"
    ]

delay = 5

os.system("~/whisk/bin/wsk property set --auth " + users[0])
sleep(delay)

os.system("~/whisk/bin/wsk -i action create delay512php delay.php -m 512 -t 300000")
sleep(delay)
os.system("~/whisk/bin/wsk -i action create delay256php delay.php -m 256 -t 300000")
sleep(delay)
os.system("~/whisk/bin/wsk -i action create delay128php delay.php -m 128 -t 300000")
sleep(delay)


os.system("~/whisk/bin/wsk -i action create prime512php primeNumber.php -m 512 -t 300000")
sleep(delay)
os.system("~/whisk/bin/wsk -i action create prime256php primeNumber.php -m 256 -t 300000")
sleep(delay)
os.system("~/whisk/bin/wsk -i action create prime128php primeNumber.php -m 128 -t 300000")
sleep(delay)

os.system("~/whisk/bin/wsk -i action create factorial512php factorial.php -m 512 -t 300000")
sleep(delay)
os.system("~/whisk/bin/wsk -i action create factorial256php factorial.php -m 256 -t 300000")
sleep(delay)
os.system("~/whisk/bin/wsk -i action create factorial128php factorial.php -m 128 -t 300000")
sleep(delay)

os.system("~/whisk/bin/wsk -i action create fib512php fibonacci.php -m 512 -t 300000")
sleep(delay)
os.system("~/whisk/bin/wsk -i action create fib256php fibonacci.php -m 256 -t 300000")
sleep(delay)
os.system("~/whisk/bin/wsk -i action create fib128php fibonacci.php -m 128 -t 300000")
sleep(delay)

os.system("~/whisk/bin/wsk -i action create matrix512php matrix.php -m 512 -t 300000")
sleep(delay)
os.system("~/whisk/bin/wsk -i action create matrix256php matrix.php -m 256 -t 300000")
sleep(delay)
os.system("~/whisk/bin/wsk -i action create matrix128php matrix.php -m 128 -t 300000")
sleep(delay)


os.system("~/whisk/bin/wsk -i action create memory512php memory.php -m 512 -t 300000")
sleep(delay)
os.system("~/whisk/bin/wsk -i action create memory256php memory.php -m 256 -t 300000")
sleep(delay)
os.system("~/whisk/bin/wsk -i action create memory128php memory.php -m 128 -t 300000")
sleep(delay)

sleep(delay)
