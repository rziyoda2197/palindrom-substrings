def top_palindrom_substringlar(matn):
    n = len(matn)
    palindromlar = set()

    for uzunlik in range(1, n + 1):
        for bosh in range(n - uzunlik + 1):
            tekshirilayotgan_palindrom = matn[bosh:bosh + uzunlik]
            if tekshirilayotgan_palindrom == tekshirilayotgan_palindrom[::-1]:
                palindromlar.add(tekshirilayotgan_palindrom)

    return palindromlar

matn = input("Matnni kiriting: ")
print(top_palindrom_substringlar(matn))
```

Kodni ishlatish uchun quyidagicha amal qiling:

1. Matnni kiriting.
2. Matnning barcha palindrom substringlarini topib, ularni setda saqlab, keyin setni chiqarib beradi.
