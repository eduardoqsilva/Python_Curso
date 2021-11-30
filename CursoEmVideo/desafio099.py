from time import sleep

def maior(*str):
    if len(str) > 0:
        print("-="*20)
        sleep(1)
        print(f"Analisando os valores passados...")
        print(f"{str} Foram informados {len(str)} valores ao todo.")
        print(f"O maior valor informado foi: {max(str)}")

    else:
        print("-=" * 20)
        sleep(1)
        print(f"Analisando os valores passados...")
        print(f"Foram informados {len(str)} valores ao todo.")
        print(f"O maior valor informado foi: 0")
        print("-=" * 20)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
