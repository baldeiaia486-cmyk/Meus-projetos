# APP DE TAREFAS DO IANIS

try:
    with open("tarefas.txt", "r") as f:
        tarefas = f.read().splitlines()
except:
    tarefas = []

while True:
    print("\n--- LISTA DO IANIS ---")
    print("1 - Ver tarefas")
    print("2 - Adicionar")
    print("3 - Apagar")
    print("4 - Sair")

    op = input("Escolhe: ")

    if op == "1":
        if not tarefas:
            print("Nada ainda, brabo!")
        else:
            for i, t in enumerate(tarefas):
                print(f"{i+1}. {t}")

    elif op == "2":
        nova = input("Nova tarefa: ")
        tarefas.append(nova)
        with open("tarefas.txt", "w") as f:
            for t in tarefas:
                f.write(t + "\n")
        print("Salvo!")

    elif op == "3":
        num = int(input("Numero pra apagar: ")) - 1
        if 0 <= num < len(tarefas):
            tarefas.pop(num)
            with open("tarefas.txt", "w") as f:
                for t in tarefas:
                    f.write(t + "\n")
            print("Apagado!")
    
    elif op == "4":
        print("Falou, brabo! Ate amanha!")
        break
