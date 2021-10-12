FORMS = {
    'Номера(Украина)': [
        r'\+?\(\d{4}\) \d{2}\-\d{2}\-\d{2}',  # (0472) 32-45-67
        r'\+?\(\d{4}\) \d{2} \d{2}\-\d{2}',  # (0472) 32 45-67
        r'\+?\(\d{4}\) \d{2} \d{2} \d{2}',  # (0472) 32 45 67
        r'\+?\d{4} \d{2}\-\d{2}\-\d{2}',  # 0472 32-45-67
        r'\+?\d{4} \d{2} \d{2}\-\d{2}',  # 0472 32 45-67
        r'\+?\d{4} \d{2} \d{2} \d{2}',  # 0472 32 45 67
        r'\+?\(\d{3}\) \d\-\d{2}\-\d{2}\-\d{2}',  # +(099) 1-82-83-83
        r'\+?\d{3} \d{3}\-\d{2}\-\d{2}', # +380 615-11-34
        r'\+?\d{3} \d{3} \d{2}\-\d{2}', # +380 615 11-34
        r'\+?\d{3} \d{3} \d{2} \d{2}',   # +380 615 11 34
        r'\+?\(\d{3}\) \d{3}\-\d{2}\-\d{2}', # +(380) 615-11-34
        r'\+?\(\d{3}\) \d{3} \d{2}\-\d{2}', # +(380) 615 11-34
        r'\+?\(\d{3}\) \d{3} \d{2} \d{2}', # +(380) 615 11 34
        r'\+?\(\d{3}\) \d{3}\-\d\-\d{3}',  # +(380) 615-1-134
        r'\+?\(\d{3}\) \d{3} \d\-\d{3}',  # +(380) 615 1-134
        r'\+?\(\d{3}\) \d{3} \d \d{3}',  # +(380) 615 1 134
        r'\+?\(\d{3}\) \d{1}\-\d{3}\-\d{3}',  # +(380) 9-961-511
        r'\+?\(\d{3}\) \d{1} \d{3}\-\d{3}',  # +(380) 9 961-511
        r'\+?\(\d{3}\) \d{1} \d{3} \d{3}',  # +(380) 9 961 511
        r'\+?\(\d{3}\) \d{3}\-\d{3}\-\d',  # +(380) 996-151-1
        r'\+?\(\d{3}\) \d{3} \d{3}\-\d',  # +(380) 996 151-1
        r'\+?\(\d{3}\) \d{3} \d{3} \d',  # +(380) 996 151 1
        r'\+?\d{2} \d{3}\-\d{3}\-\d{2}\-\d{2}',  # +38 099-615-11-34
        r'\+?\d{2} \d{3} \d{3}\-\d{2}\-\d{2}',  # +38 099 615-11-34
        r'\+?\d{2} \d{3} \d{3} \d{2}\-\d{2}',  # +38 099 615 11-34
        r'\+?\d{2} \d{3} \d{3} \d{2} \d{2}',  # +38 099 615 11 34
        r'\+?\d{2} \(\d{3}\) \d{3}\-\d{2}\-\d{2}', # +38 (099) 615-11-34
        r'\+?\d{2} \(\d{3}\) \d{3} \d{2}\-\d{2}', # +38 (099) 615 11-34
        r'\+?\d{2} \(\d{3}\) \d{3} \d{2} \d{2}', # +38 (099) 615 11 34
    ],
    "Номера(Россия)": [
        r'\+\d{8}', #+8801723283638
        r'\+?\d\-\d{3}\-\d{3}\-\d{3}', # 0-800-505-707
        r'\+?\d\-\d{3} \d{3}\D\d{3}',  # 0-800 505 707
        r'\+?\d \d{3} \d{3}\-\d{3}', # 0 800 505-707
        r'\+?\d \d{3} \d{3}\D\d{3}',  # 0 800 505 707,
        r'\+?\(\d{4}\) \d{2}\-\d{2}\-\d{2}',  # (0472) 32-45-67
        r'\+?\(\d{4}\) \d{2} \d{2}\-\d{2}',  # (0472) 32 45-67
        r'\+?\(\d{4}\) \d{2} \d{2} \d{2}',  # (0472) 32 45 67
        r'\+?\d{4} \d{2}\-\d{2}\-\d{2}',  # 0472 32-45-67
        r'\+?\d{4} \d{2} \d{2}\-\d{2}',  # 0472 32 45-67
        r'\+?\d{4} \d{2} \d{2} \d{2}',  # 0472 32 45 67
        r'\+?\(\d{3}\) \d\-\d{2}\-\d{2}\-\d{2}',  # (099) 1-82-83-83
        r'\+?\d \d{3} \d{3}-\d{2}-\d{2}', # +7 499 577-73-34
        r'\+?\d \d{3} \d{3} \d{2}-\d{2}', # +7 499 577 73-34
        r'\+?\d \d{3} \d{3} \d{2} \d{2}',  # +7 499 577 73 34
        r'\+?\d \(\d{3}\) \d{3}-\d{2}-\d{2}', # +7 (499) 577-73-34
        r'\+?\d \(\d{3}\) \d{3} \d{2}-\d{2}', # +7 (499) 577 73-34
        r'\+?\d \(\d{3}\) \d{3} \d{2} \d{2}',  # +7 (499) 577 73 34
    ],

    'Почты': [r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b']
}
