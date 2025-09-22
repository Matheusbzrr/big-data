from mongo_utils import GerenciadorMongo

def menu():
    print("\n=== gerenciador mongoDB CLI ===")
    print("1 - listar todos os bancos")
    print("2 - listar coleções de um banco")
    print("3 - adicionar nova coleção")
    print("0 - sair")
    escolha = input("escolha uma opçao: ")
    return escolha

def main():
    gerente = GerenciadorMongo()
    
    while True:
        opcao = menu()
        
        if opcao == "1":
            bancos = gerente.listar_bancos()
            print("\nbancos disponiveis:")
            for banco in bancos:
                print(f"- {banco}")
        
        elif opcao == "2":
            db_nome = input("digite o nome do banco: ")
            try:
                colecoes = gerente.listar_colecoes(db_nome)
                print(f"\ncoleçoes do banco '{db_nome}':")
                for c in colecoes:
                    print(f"- {c}")
            except Exception as e:
                print(f"erro: {e}")
        
        elif opcao == "3":
            db_nome = input("digite o nome do banco: ")
            nome_colecao = input("digite o nome da nova coleçao: ")
            try:
                gerente.adicionar_colecao(nome_colecao, db_nome)
            except Exception as e:
                print(f"Erro: {e}")
        
        elif opcao == "0":
            print("saindo...")
            break
        
        else:
            print("opçao invalida, tente novamente")

if __name__ == "__main__":
    main()
