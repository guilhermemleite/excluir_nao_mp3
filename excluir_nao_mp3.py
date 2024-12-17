import os
from send2trash import send2trash

def excluir_nao_mp3(pasta):
    try:
        # Percorre a pasta principal e suas subpastas
        for raiz, _, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                # Caminho completo do arquivo
                caminho_completo = os.path.join(raiz, arquivo)
                # Verifica se o arquivo não é .mp3
                if not arquivo.lower().endswith('.mp3'):
                    try:
                        # Move o arquivo para a lixeira
                        send2trash(caminho_completo)
                        print(f"Arquivo movido para a lixeira: {caminho_completo}")
                    except Exception as erro:
                        print(f"Erro ao mover para a lixeira {caminho_completo}: {erro}")
        print("\nProcesso concluído: arquivos não .mp3 foram movidos para a lixeira.")
    except Exception as e:
        print(f"Erro geral: {e}")

# Função principal para interação com o usuário
def main():
    while True:
        # Solicita ao usuário o caminho da pasta
        pasta = input("\nDigite o caminho da pasta principal: ").strip()
        if not os.path.isdir(pasta):
            print("O caminho fornecido não é válido. Tente novamente.")
            continue

        # Chama a função para excluir arquivos não .mp3
        excluir_nao_mp3(pasta)

        # Pergunta se o usuário deseja processar outra pasta
        repetir = input("\nDeseja realizar o processo em outra pasta? (S para Sim / N para Não): ").strip().upper()
        if repetir == "N":
            print("Encerrando o programa. Até logo!")
            break
        elif repetir != "S":
            print("Opção inválida. Encerrando o programa.")
            break

# Executa o programa
if __name__ == "__main__":
    try:
        from send2trash import send2trash
    except ImportError:
        print("A biblioteca 'send2trash' não está instalada. Instale-a com o comando: pip install send2trash")
    else:
        main()
